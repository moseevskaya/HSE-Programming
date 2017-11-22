#какой процент от общего количества слов не оканчивается знаком препинания (можно взять только запятую и точку)

with open("pater_noster.txt", encoding="utf-8") as f:
    text = f.read()
    with open("pater_noster.txt", encoding="utf-8") as f:
        lines = f.readlines()
        slov = text.count(" ") + len(lines)
        nuzhnyh_slov = slov - text.count(",") - text.count(".")
        procent = (nuzhnyh_slov / slov) * 100
        print(procent)
    
