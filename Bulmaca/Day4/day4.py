def kontrol1(range1, range2):
    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        return True
    return False

def kontrol_pairs(pairs):
    count = 0
    for pair in pairs:
        first_range = pair[0]
        second_range = pair[1]
        if kontrol1(first_range, second_range) or kontrol1(second_range, first_range):
            count += 1
    return count

def read_pairs_from_file(file_name):
    pairs = []
    with open(file_name, 'r') as file:
        for line in file:
            ranges = line.strip().split(',')
            pair = tuple(tuple(map(int, rng.split('-'))) for rng in ranges)
            pairs.append(pair)
    return pairs

file_name = 'veriler.txt'  # Dosya adını güncelleyin

pairs = read_pairs_from_file(file_name)
completely_within_count = kontrol_pairs(pairs)
print("Bir aralık diğerini tamamen içeren çift sayısı:", completely_within_count)


# ------------------------------------------------------------------------

# -- Part 2 
with open("veriler.txt","r") as file:
    lines = file.read()
    pairs = []
    overlaps = 0
    for line in lines.split('\n'):
        print("line: " ,line)
        parcala = line.split(',')
        veri1 = parcala[0].split("-")
        veri2 = parcala[1].split("-")
        veri1_min = int(veri1[0])
        veri1_max = int(veri1[1])
        veri2_min = int(veri2[0])
        veri2_max = int(veri2[1])
        result = list(range(veri1_min,veri1_max + 1)) 
        for i in result:
            if(veri2_min <= i <= veri2_max):
                kontrol = True
                break
            else:
                kontrol = False
        if kontrol == True:
            overlaps = overlaps + 1
        print("overlaps: ",overlaps)