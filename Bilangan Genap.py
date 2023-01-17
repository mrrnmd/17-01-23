def contains_even_number(l):
    for ele in l:
        if ele % 2 == 0:
            print("List Berisi Bilangan Genap")
            break
    else:
        print("List Tidak Berisi Bilangan Genap")

print("For List 1 :")
contains_even_number([1,9,8])
print("\nFor Lise 2 :")
contains_even_number([3,7,9])