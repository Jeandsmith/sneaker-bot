# sneaker-bot

What it does:
- given site, search terms, size, and quantity:
  - finds products whose titles contain all seacrh terms
  - add given quantity of each product to cart
    - same quantity for all products for now (something to work on)
  - print cart information (pretty format)
  
- given credit card information (currently hard-coded):
  - post to shopify vault link
  - print session token (will be needed for checkout)
  
What it doesn't do:
- checkout cart:
  - create checkout, obtain checkout token
    - (I've actually been able to get this before, but my method doesn't work consistently **¯\\\_(ツ)_/¯** )
  - post shipping, billing address
  - get shipping rates given zip code (from shipping address), select rate
  - post payment (using token from vault)
  - complete checkout?
