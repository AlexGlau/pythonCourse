def format_price(price):
    cast = int(price)
    return 'Price: ${var}'.format(var=price)

res = format_price(56.24)
print(res)
