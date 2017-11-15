slovo = input("Введите слово: ")
if slovo != '':
    if slovo == 'Ave Maria':
        print("Deus vult!")
    else:
        for i in range(len(slovo)):
            print(slovo) 
            slovo = slovo[-1:] + slovo[:-1]
else:
    print("Вы не ввели слово. Извините, я одноразовый.")
        
# Ни на что не надеюсь, но вдруг. А можно спросить?
# Помогут ли какие-нибудь танцы с бубном заработать вот такой записи:
###    print(slovo[:i], slovo[-(len(slovo) - i):], sep='')
# Я так и не смогла понять, почему она работает так, как надо,
# только если разделитель ненулевой...
