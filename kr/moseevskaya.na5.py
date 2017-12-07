with open("quotes.txt", encoding="utf-8") as f:
    for line in f:
        if line.count(' ') < 10:
            if line[5] == " ":
                print(line[:-1])
