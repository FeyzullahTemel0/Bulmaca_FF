
# Part 1
def hesapla_sirt_cantasi(bicim):
    birinci_bolme = bicim[:len(bicim)//2]
    ikinci_bolme = bicim[len(bicim)//2:]
    
    birinci_turler = set(birinci_bolme)
    ikinci_turler = set(ikinci_bolme)
    
    ortak_turler = birinci_turler.intersection(ikinci_turler) #intersection() metodu, iki veya daha fazla set arasında kesişimi bulmak için kullanılır.
    
    toplam = 0
    for tur in ortak_turler:
        if tur.islower():
            toplam += ord(tur) - ord('a') + 1
        else:
            toplam += ord(tur) - ord('A') + 27
    
    return toplam


dosya_adi = "veriler.txt"
toplam_öncelik = 0

with open(dosya_adi, "r") as dosya:
    for satir in dosya:
        canta = satir.strip()
        toplam_öncelik += hesapla_sirt_cantasi(canta)

print("Öğe türlerinin toplam önceliği:", toplam_öncelik)


#Part2
def hesapla_oncelikler(group):
    common_items = set(group[0])
    for i in range(1, len(group)):
        common_items = common_items.intersection(set(group[i]))

    # Rozete karşılık gelen öğe türünün önceliğini hesaplama
    priority = 0
    for item in common_items:
        if 'a' <= item <= 'z':
            priority += ord(item) - ord('a') + 1
        elif 'A' <= item <= 'Z':
            priority += ord(item) - ord('A') + 27

    return priority


# Dosyayı okuyarak sırt çantalarını gruplara ayırma
with open('veriler.txt', 'r') as file:
    lines = file.readlines()

backpacks = [lines[i:i+3] for i in range(0, len(lines), 3)]

# Gruplara ait rozet öğe türlerini bulma ve öncelikleri hesaplama
total_priority = 0
for group in backpacks:
    priority = hesapla_oncelikler(group)
    total_priority += priority

print("Rozetlere karşılık gelen öğe türlerinin önceliklerinin toplamı:", total_priority)