#Operator Logika (Logical)
#Operator logika digunakan untuk menggabungkan beberapa kondisi boolean.
#Hasil dari operasi ini adalah nilai boolean: True atau False.

a = True
b = False

#1. AND (and)
#AND adalah operator yang mengembalikan True hanya jika kedua operandnya True.
# true and true = true
# true and false = false 
# false and true = false
# false and false = false
print(a and b)  # Output: False, karena True and False = False

#2. OR (or)
#OR adalah operator yang mengembalikan True jika salah satu operandnya True.
# true or true = true
# true or false = true
# false or true = true
# false or false = false
print(a or b)   # Output: True, karena True or False = True

#3. NOT (not)
#NOT adalah operator yang membalik nilai boolean.
# not true = false
# not false = true
print(not a)    # Output: False, karena not True = False
print(not b)    # Output: True, karena not False = True