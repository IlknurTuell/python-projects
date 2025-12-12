#TIC-TAK-TOE (X-0)

board = [" "] * 9

#Tahtayı ekrana yazdıralım:
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+--+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+--+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

#Kazananı kontrol etme fonksiyonu oluşturalım:
def check_winner(player):
    win_patterns = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for a, b, c in win_patterns:
        if board[a] == board[b] == board[c] == player:
            return True
    return False
    
#Berabere kontrolü yapalım:
def check_draw():
    return " " not in board

#Oyun Döngüsü

current_player = "X"

print("     TIC TAC TOE OYUNUNA HOŞ GELDİNİZ     ")
print_board()

while True:
    print(f"Sıra: {current_player}")
    move = int(input("0-8 arası bir pozisyon seçiniz: "))

    if move < 0 or move > 8 or board[move] != " ": #Geçersiz hamle kontrolü
        print("Geçersiz hamle! Tekrar deneyiniz.")
        continue

    #Hamleyi işleyelim:
    board[move] = current_player
    print_board()

    #Kazanma kontrolü yapalım:
    if check_winner(current_player):
        print(f"Tebrikler! {current_player} kazandı.")
        break

    #Berabere kontrolü yapalım:
    if check_draw():
        print("Oyun berabere!")
        break

    #Oyuncu değiştir:
    current_player = "0" if current_player == "X" else "X"
