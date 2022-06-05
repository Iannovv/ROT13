def ROT_13(tekst):
    zaszyfrowana_wiadomosc = ""
    male_litery = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    duze_litery = ["A","B","C","D","E","F","G","H", "I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    for i in tekst:
        if i in male_litery:
            index = male_litery.index(i)
            szyfrowanie = (index + 13) % 26
            zaszyfrowana_wiadomosc += male_litery[szyfrowanie]
        elif i in duze_litery:
            index = duze_litery.index(i)
            szyfrowanie = (index + 13) % 26
            zaszyfrowana_wiadomosc += duze_litery[szyfrowanie]
        else:
            zaszyfrowana_wiadomosc += i
    return zaszyfrowana_wiadomosc

text_1 = open("tekst_poczatkowy.txt", 'r')
text_2 = open("tekst_koncowy.txt", 'w')
text_2.write(ROT_13(text_1.read()))
text_1.close
text_2.close
