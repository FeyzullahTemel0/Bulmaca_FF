with open('veriler.txt', 'r') as file:
    datas = file.readlines()

puanlama = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}
# semboller = ["A", "B", "C", "A", "C"] # Bu sıralamayı kullandığımda ise yine part1 için doğru sonucu almama fakat part 2 için yanlış sonucu almama sebep oldu part2= 9953 False
# semboller = ["B", "C", "A", "C", "A"] # Bu sıralamayı kullandığımda ise yine part1 için doğru sonucu almama fakat part 2 için yanlış sonucu almama sebep oldu part2= 18296 False
# semboller = ["B", "C", "A", "A", "C"] # Bu sıralamayı kullandığımda ise yine part1 için doğru sonucu almama fakat part 2 için yanlış sonucu almama sebep oldu part2= 13388 False
# semboller = ["B", "C", "A", "B", "A"] # Bu sıralamayı kullandığımda ise yine part1 için doğru sonucu almama fakat part 2 için yanlış sonucu almama sebep oldu part2= 15964 False
# semboller = ["A", "C", "B", "A", "C"] # Bu sıralamayı kullandığımda ise yine part1 için doğru sonucu almama fakat part 2 için yanlış sonucu almama sebep oldu part2= 12735 False
# semboller = ["C", "B", "A", "C", "A"] # Bu sıralamayı kullandığımda ise yine part1 için doğru sonucu almama fakat part 2 için yanlış sonucu almama sebep oldu part2= 14808 False
semboller = ["C", "A", "B", "C", "A"] # Son deneme ile bu sıralamayı kullanarak her iki part içinde doğru sonucu elde etmiş oldum. part2 = 12683 True

# Part1 
def function1(rakip, ben):

    my_score = puanlama[ben]
    other_score = puanlama[rakip]

    hesapla = my_score - other_score

    if hesapla == 0:
        my_score += 3
    elif hesapla == 1 or hesapla == -2:
        my_score += 6

    return my_score

score1 = 0

for data in datas:
    data = data.strip()
    splitted = data.split(" ") 
    other = splitted[0]
    mine = splitted[1]
    score1 += function1(other, mine)

print("SKOR PART1:", score1)

# Part 2
score2 = 0
def function2(rakip, ben):
    symbol_ = puanlama[rakip]

    if ben == "X":
        return function1(rakip, semboller[symbol_ - 1])
    elif ben == "Z":
        return function1(rakip, semboller[symbol_ + 1])
    else:
        return function1(rakip, rakip)
    
for data in datas:
    data = data.strip()
    splitted = data.split(" ")
    rakip = splitted[0]
    ben = splitted[1]
    score2 += function2(rakip, ben)

print("SKOR PART2:", score2)
