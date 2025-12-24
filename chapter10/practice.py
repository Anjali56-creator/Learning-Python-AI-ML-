#create a class laptop with attributes:brand,RAM,price
#create 2 objects with different values
class laptop:
    brand="HP"
    RAM="8GB"
    price="1000000"

laptop1=laptop()
laptop1.brand="Dell"
laptop1.RAM="16GB"
laptop1.price="80000"
print("laptop 1 details:")
print("brand:",laptop1.brand)
print("RAM:",laptop1.RAM)
print("price:",laptop1.price)

laptop2=laptop()
laptop2.brand="Apple"
print("laptop 2 details:")
print("brand:",laptop2.brand)
print("RAM:",laptop2.RAM)