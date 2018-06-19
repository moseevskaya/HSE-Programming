import os
import shutil
import re

#частотный словарь из предложений, какие найдутся в файлах, какие найдутся в папках
def countsentences():
    dic = {}
    for root, dirs, files in os.walk('news'):
        for f in files:
            with open(os.path.join(root, f), 'r', encoding='windows-1251') as text:
                t = text.read()
            counter = len(re.findall('<se>', t))
            dic[f] = str(counter)
    return dic

#поиск информации из мета и запись в массив
def findmeta(text_str):
    doc_id = re.search(r'<title>', text_str).group(1)
    author = re.search(r'<meta content="(.*)" name="author">', text_str).group(1)
    created = re.search(r'<meta content="(.*)" name="created">', text_str).group(1)
    topic = re.search(r'<meta content="(.*)" name="topic">', text_str).group(1)
    tagging = re.search(r'<meta content="(.*)" name="tagging">', text_str).group(1)
    
    arr = [doc_id, title, author, topic, tagging]
    return arr

#запись в цсв
def writeintocsv(arr, name):
    with open(name, 'a', encoding='windows-1251') as f:
        f.write(arr[2]+'\t'+arr[0]+'\t'+arr[1]+'\n')
         
#запись текста в строку            
def write_s(smth, filename):
    with open(filename, 'a', encoding = 'utf-8') as f:
        f.write(smth)

#заполнение таблицы, которое почему-то не работает        
def createatable():
    arrayofarr = []
    for root, dirs, files in os.walk('news'):
        for f in files:
            with open(os.path.join(root, f), 'r', encoding='windows-1251') as text:
                t = text.read()
            arr = findmeta(t)
            arr.append(f)
            arrayofarr.append(arr)
    for arr in arrayofarr:
        writeintocsv(arr, 'metatable.csv')        

def main():
#1:
    d = countsentences()
    for key in d.keys():
        write_s(key+'\t'+d[key]+'\n', 'sentences.txt')
    
    with open('metatable.csv', 'a', encoding='windows-1251') as f:
        f.write('doc_id'+'\t'+'author'+'\t'+'created'+'\t'+'topic'+'\t'+'tagging'+'\n')
    createatable()
    print('I sincerely hope 1 done')

if __name__ == '__main__':
    main()
#и вообще ничего не работает.
