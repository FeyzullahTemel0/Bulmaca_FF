# Day1
# Part 1
with open("veriler.txt","r") as file:
    input = file.read()


    lines = input.split("\n")
current_elf_calories = 0 #Mevcut elfin kalori miktarını güncellemek için kullandım
max_calories = 0


for line in lines:
    # Elf'ler arasındaki ayrım boşluğu ise if çalışır.
    if line.strip() == "":
        max_calories = max(max_calories, current_elf_calories) # Karşılaştırma sonucunda max kalori değişkene atar
        current_elf_calories = 0
    else:
        current_elf_calories += int(line)

max_calories = max(max_calories, current_elf_calories)

print(max_calories) # Sonuç oalrak MAX kalori yazdırılır

#################################################################################################################################

# Part 2
with open("veriler.txt", "r") as file:
    input_data = file.read()

# Process the data
lines = input_data.split("\n")
current_elf_calories = 0
top_calories = []  

for line in lines:
    if line.strip() == "":
        if current_elf_calories > 0:
            top_calories.append(current_elf_calories)
        current_elf_calories = 0
    else:
        current_elf_calories += int(line)

if current_elf_calories > 0:
    top_calories.append(current_elf_calories)

top_calories.sort(reverse=True)

total_calories = sum(top_calories[:3])

print(total_calories)