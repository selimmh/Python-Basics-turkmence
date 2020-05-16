# "a" - Append. Birleşdirmek üçin bir faýl açýar, faýl ýok bolsa error berer

f = open("text.txt", "a")
f.write("\nbu text birleşdirildi")
f.close()