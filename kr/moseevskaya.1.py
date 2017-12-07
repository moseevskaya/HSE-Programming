with open("quotes.txt", encoding="utf-8") as f:
    for line in f:
        if line.count(' ') < 10:
            if line[5] == " ":
                
                print(line)
        
    


#with open("text.txt", encoding="utf-8") as f:
 #   text = f.read()
# Выходим из блока with ... as, больше читать из файла нечего
#lines = text.splitlines() 
