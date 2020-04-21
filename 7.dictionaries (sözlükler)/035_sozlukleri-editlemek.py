# sözlükdäki elementleri editlemek

books = {'author' : 'Khaled Hosseini', 'name' : 'Kite runner'}

print(books.get('author'))
print(books.get('name'))
print(books.get('publisher', 'Tapylmady'))
