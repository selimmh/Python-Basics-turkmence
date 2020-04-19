# ulanyjy adynyň elýeterliligi

users = ['user1', 'user2', 'user3']

username = input("Ulanyjy adyny gir: ")

if username in users:
    print("Bagyşlaň, ulanyjy ady eýýäm alyndy")
else:
    print("Ulanyjy ady sanawa goşuldy")
    users.append(username)

print(users)