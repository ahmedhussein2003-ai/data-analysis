x=1/2
y=float(input("base = "))
z=float(input("height = "))
print("The area of the triangle = " , x*y*z )


a=5
b=10
old_a=a
a=b
b=old_a
print("a:" , a)
print("b:" , b)
#another way
d=5
f=10
d , f = f ,d
print("d:" , d)
print("f:" , f)


km=float(input("Enter the distance in KM: "))
miles= km/1.609344
print(f"{km} km = {miles} miles")
