import requests
import json

headers={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

URL = input('Enter URL: ')
URL = 'https://' + URL

jsonURL = URL + '/products.json'
addToCartURL = URL + '/cart/add.json'
cartURL = URL + '/cart.json'

# shopify payment vault
ccVaultURL = 'https://elb.deposit.shopifycs.com/sessions'

search = input('Enter term: ')
size = input('      size: ')
quant = input('      quantity: ')

r = requests.get(jsonURL, headers=headers)
r = r.json()
s = requests.Session()

# search terms and title will both be converted to
# lowercase so searching is not case-sensitive
search = search.lower()
searchList = search.split()

for x in range(0, 30):
    title = r['products'][x]['title']
    title = title.lower()
    titleList = title.split()

    # searching for term(s)
    check = 1

    for term in searchList:
        for word in titleList:
            if word == term:
                break
            elif word == titleList[-1]:
                check = 0
                break

        if check == 0:
            break

    # if term(s) found
    if check == 1:
        vars = r['products'][x]['variants']

        # search for size in variant title
        for var in vars:
            varTitle = var['title']
            varTitleList = varTitle.split()

            for info in varTitleList:
                # size found, add to cart
                if size == info:
                    payload_cart = {'items':[{'quantity':quant,'id':var['id']}]}
                    s.post(addToCartURL, json=payload_cart)
                    break

# print cart information, formatted
getCart = s.get(cartURL)
getCart = getCart.json()
print(json.dumps(getCart, indent = 4))

# credit card information
payload_cc = {
    'credit_card': {
            'number':'4207123456783456',
            'first_name':'E',
            'last_name':'C',
            'month':'8',
            'year':'2023',
            'verification_value':'123'
    }
}


# post cc information to shopify vault, returns
# payment token (will be needed for checkout)
cc = s.post(ccVaultURL, json=payload_cc)
cc = cc.json()
print('Session id from vault:', cc['id'])
