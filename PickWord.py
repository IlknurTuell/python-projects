import random

words = []
with open ("sowpods.txt","r") as f: #sowpods dosyasını okuyoruz
    line = f.readline().strip() # readline(): dosyadan ilk satırı okur. strip(): satırın başındaki\ sonundaki boşluk ve \n yeni yatır karakterini siler.
    words.append(line) # ilk kelimeyi listeye ekler.
    while line:
        line = f.readline().strip() 
        words.append(line) #Tüm karakterleri dosyadan çekip words listesine doldurduk.

random_index = random.randint(0,len(words)-1)  # Liste içinde rastgele bir index sseçilir.

print("Random word : ", words[random_index]) #seçilen indeksteki kelimeyi ekrana yazdırır.