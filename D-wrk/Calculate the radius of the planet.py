from math import pi
r = input("Radius of the orbit")
v = input("Orbital Speed")
r = float(r)
v = float(v)

r = r*100000000
year = 2 *pi*r/v
year = year / (60*60*24)