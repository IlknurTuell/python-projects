import random

#Kelime listesi oluşturalım:
words = ["python", "matematik", "programlama", "bilgisayar", "veribilimi", "yazılım"]

#Rastgele kelime seçelim:
def choose_word():
    return random.choice(words)

#Ekrana o anki durumunu yazdırsın:
def display_game(secret_word, guessed_letters, attempts):
    print("\nKalan hakkın: ", attempts)
    print("Tahmin edilen harfler: ", " ".join(sorted(guessed_letters)))

    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("Kelime: ", display)

# Oyunun ana fonksiyonunu yazalım:
def play_hangman():
    secret_word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("ADAM ASMACA OYUNUNA HOŞ GELDİN!")
    print("\nKelimeyi tahmin etmeye çalış!")

    while attempts > 0 : #Hak bitene kadar döngü devam edecek
        display_game(secret_word, guessed_letters, attempts )

        guess = input("Bir harf giriniz: ").lower()

        if len(guess) != 1 or not guess.isalpha(): #Hatalı giriş kontrolü yapalım
            print("Lütfen sadece 1 harf giriniz.")
            continue
        if guess in guessed_letters:  # Tekrar tahmin kontrolü yaptık.
            print("Bu harfi zaten tahmin ettiniz.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Tebrikler! Doğru tahmin.")

            if all(letter in guessed_letters for letter in secret_word):
                print("\nTebrikler! Kelimeyi bildin: ", secret_word)
                break

        else:
            print("Yanlış tahmin.")
            attempts -= 1
        
    # Oyunu kaybetme durumuna bakalım:
    if attempts ==0:
        print("\nHakkın bitti! Kelime: ", secret_word)

play_hangman()
