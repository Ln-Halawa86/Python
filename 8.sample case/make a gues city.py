import random

soal = {
    'Indonesia': 'Jakarta',
    'Singapura': 'Singapura',
    'Malaysia': 'Kuala Lumpur',
    'Thailand': 'Bangkok',
    'Inggris': 'London',
    'Belanda': 'Den Haag',
    'Perancis': 'Paris',
    'Belgia': 'Brussel',
    'Tiongkok': 'Beijing',
    'Jepang': 'Tokyo',
    'Rusia': 'Moscow',
    'Australia': 'Sydney'
}

negara = random.choice(list(soal.keys()))
print("Apa nama ibu kota dari negara: " + negara)
jawab = input("Jawaban: ")
if jawab == soal[negara]:
    print("Benar")
else:
    print("Salah")
    print("Jawaban yang benar adalah: " + soal[negara])
    #ouput: Apa nama ibu kota dari negara: Malaysia
    # Jawaban: Jakarta
    # Salah
    # Jawaban yang benar adalah: Kuala Lumpur