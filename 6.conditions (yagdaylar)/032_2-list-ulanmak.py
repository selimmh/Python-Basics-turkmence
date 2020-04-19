# elementiň sanawda ýokdugyny barlamak

admin_users = ['selim', 'perman']

# ulanyjy adyny soramak
username = input("Ulanyjy adyny giriz: ")

# ulanyjynyň administrator ulanyjydygyny ýa-da ýokdugyny barlamak
if username not in admin_users:
    print("Siziň ygtyýaryňyz ýok")
else:
    print("Admin paneline hoş geldiňiz")
