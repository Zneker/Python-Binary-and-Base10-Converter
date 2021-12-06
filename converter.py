#Choice
choice = input("1 for Binary to Base10, 0 for Base10 to Binary")



#Binary to Base10 Converter
if choice == "1":
    binary = input("You have chosen to use a Binary to Base10 Converter")
    base = int(binary, 2)
    print(base)

#Base to Binary Converter
if choice == "0":
    bass10 = input("You have chosen to use a Base10 to Binary Converter")
    bass10 = int(bass10)
    print(bass10)

    base10 = bin(bass10)
    print(base10-"b")