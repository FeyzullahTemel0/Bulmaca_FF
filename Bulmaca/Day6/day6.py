
# Part 1
def find_start_of_packet(ff):
    with open(ff, 'r') as file:
        file_buffer = file.read().strip()
        
    for i in range(3, len(file_buffer)):
        if len(set(file_buffer[i-3:i+1])) == 4:
            return i + 1
    return -1

datastream_file = "veriler.txt"
result = find_start_of_packet(datastream_file)
print("İlk paket başlangıcı", result, ". karakterde bulunuyor.")


#-------------------------------------------------------------------------------#

# Part 2

def find_start_of_message(datastream):
    with open(datastream, 'r') as file:
        buffer = file.read().strip()

    for i in range(13, len(buffer)):
        if len(set(buffer[i-13:i+1])) == 14:
            return i + 1
    return -1

datastream_file = "veriler.txt"
result = find_start_of_message(datastream_file)
print("İlk mesaj başlangıcı", result, ". karakterde bulunuyor.")
