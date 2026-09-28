import random

caragteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Ingrese la longitud de la palabra: "))
password = ""
for i in range(longitud):
    password += random.choice(caragteres)

print("La contraseña generada es:", password)
