#with open("quotes.txt", encoding="utf-8") as f:
#    text = f.readlines()

i = 0
with open("quotes.txt", encoding="utf-8") as f:
    for line in f:    # здесь строки тоже заканчиваются на символ переноса строки
        if line[5] == " ":
#            words = line.split
            print(line)
        
    


#with open("text.txt", encoding="utf-8") as f:
 #   text = f.read()
# Выходим из блока with ... as, больше читать из файла нечего
#lines = text.splitlines() 
