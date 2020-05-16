# and ýagdaýy

username = input("Ulanyjy adyny gir: ")
password = input("Paroly gir: ")

if username == 'selim' and password != 'selim123':
    print("Ýalňyş parol")

elif username != 'selim' and password == 'selim123':
    print("Ýalňyş ulanyjy ady")

elif username != 'selim' and password != 'selim123':
    print("Ýalňyş ulanyjy ady we paroly")
    
else:
    print("Berekella")
