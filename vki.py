yas = int(input("yasinizi giriniz: "))
kilo = float(input("kilonuzu girin(kg): "))
boy = float(input("boyunuzu girin (metre): "))

vki = kilo / (boy**2)

print("Beden kitle indeksiniz: ", round(vki,2))

if yas >= 20:
    print("askere gitme yasi gelmis.")
else:
    print("askere gitme yasi henüz gelmedi.")

if vki < 18.5:
    print("zayıfsınız.")
elif 18.5 <= vki <= 24.9:
    print("normal kilolusunuz.")
elif 25 <= vki <= 29.9:
    print("fazla kilolusunuz.")
else:
    print("obezsiniz.")

ideal_kilo = 22*(boy**2)
kilo_farki = kilo - ideal_kilo
if kilo_farki > 0:
    print("ideal kilonuzun üzerindesiniz. ideal kiloya ulaşmak için", round(abs(kilo_farki), 2), "kg vermelisiniz.")
elif kilo_farki < 0:
    print("ideal kilonun altındasınız. ideal kiloya ulaşmak için", round(abs(kilo_farki), 2), "kg almalısınız.")
else:
    print("ideal kilodasınız.")

