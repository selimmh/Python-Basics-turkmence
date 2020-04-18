# san listini döretmek

nums = list(range(1,11))
print(nums)

# täk sanlary print etmek
odd_nums = list(range(1,22, 2))
print(odd_nums)

# jübüt sanlary print etmek
even_nums = list(range(0,22, 2))
print(even_nums)

# kwadratlary print etmek
squares = []
for value in range (0,11):
    square = value ** 2
    squares.append(square)
print(squares)

# listdäki elementleriň jemi
nums = list(range(0,101))
sum = sum(nums)
print("0 we 100 aralygyndaky sanlaryň jemi: " + str(sum))