def read_table(file_name):
    lines = []
    with open(file_name, encoding="utf-8") as f:
        lines = f.readlines()[8:]
        print(len(lines))
        
    return lines





def main():
    print('start')
    lines = read_table('file_name.tab')

if __name__ == '__main__':
    main()
#эта хреновина делает что-то важное


#AT LAST THIS FUCKING WORKS
#Я НЕ СОВСЕМ ИДИОТ
#УРААААААА, Я УМЕЮ СПИСЫВАТЬ С ДОСКИ
