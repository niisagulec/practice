def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b == 0:
        return "Sıfıra bölünemez!"
    return a / b

print("Basit Hesap Makinesi")
print("İşlem Seçin:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Seçiminizi yapın (1/2/3/4): ")

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

if secim == '1':
    print("Sonuç:", topla(sayi1, sayi2))
elif secim == '2':
    print("Sonuç:", cikar(sayi1, sayi2))
elif secim == '3':
    print("Sonuç:", carp(sayi1, sayi2))
elif secim == '4':
    print("Sonuç:", bol(sayi1, sayi2))
else:
    print("Geçersiz seçim!")
