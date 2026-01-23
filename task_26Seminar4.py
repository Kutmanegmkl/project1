brand = ['Acer', 'HP', 'Lenovo', 'Asus', 'Honor', 'Apple']
price = [20000, 27000, 95000, 15000, 50000, 90000]
input_ = input()
new_brand=input_[:input_.index('-')].capitalize()
new_price=int(input_[input_.index('-')+1:])

if new_brand in brand:
  if new_price==0:
    del (price[brand.index(new_brand)])
    brand.remove(new_brand)
  else:
    price[brand.index(new_brand)]=new_price
elif new_brand=='Hp':
  if new_price==0:
    del price[brand.index(new_brand.upper())]
    brand.remove(new_brand.upper())
  else:
    price[brand.index(new_brand.upper())]=new_price
else:
  if new_price !=0:
    brand.append(new_brand)
    price.append(new_price)
 
print(brand)
print(price)