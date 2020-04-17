import random
import sys

hak = 0
fake = []
board = []
satir = 0
sutun = 0
gemi_yon = True
gecici = 0
visible = 0
sys.setrecursionlimit(150)


def gec(uzunluk):
    randomyan(uzunluk)


def gel(uzunluk):
    randomdik(uzunluk)


def randomyan(uzunluk):
    satir = random.randint(0, 9)
    sutun = random.randint(0, 9)
    g_gemi_list = board[satir]
    say = 0
    durum = 1
    for y in range(10):
        for g in board[satir][y]:
            if g == "X":
                durum = 0
    if sutun + uzunluk >= 10:
        durum = 0
    if durum == 0:
        # print("fazla geldi",sutun)
        gec(uzunluk)
    else:
        for n in range(0, 10):
            if n >= sutun and say < uzunluk:
                g_gemi_list[n] = "X"
                say += 1
                for r in g_gemi_list[n]:
                    if r == "X":
                        durum = 1
                    else:
                        durum = 0
    if durum == 0:
        durum = 0
    else:
        board[satir] = g_gemi_list


def randomdik(uzunluk):
    satir = random.randint(0, 9)
    sutun = random.randint(0, 9)
    #
    # print("uzunluk",uzunluk)
    # print("satir",satir)
    # print("sütun",sutun)
    g_gemi_list = board[satir]
    say = 0
    durum = 1
    for y in range(10):
        for g in board[satir][y]:
            if g == "X":
                # print(board[satir])
                # print("aynı satır",satir)
                durum = 0

    if satir + uzunluk >= 10:
        durum = 0

    if durum == 0:
        # print("fazla geldi",sutun)
        gel(uzunluk)
    else:
        g_satir = satir
        for s in range(0, uzunluk):
            for n in range(0, 10):
                say = 0
                if n == sutun and say < 1:
                    g_gemi_list[n] = "X"
                    say += 1
                    for r in g_gemi_list[n]:
                        if r == "X":
                            durum = 1
                        else:
                            # print("listede bulunamadı")
                            durum = 0
            if durum == 0:
                gel(uzunluk)
            else:
                board[g_satir] = g_gemi_list
                g_satir += 1


def gemiyerlestir():
    print("gemi4 yerleştiriliyor")
    gemi_yon = random.choice([True, False])
    if gemi_yon:
        randomyan(4)
    else:
        randomdik(4)
    print("gemi3 yerleştiriliyor")
    gemi_yon = random.choice([True, False])
    if gemi_yon:
        randomyan(3)
    else:
        randomdik(3)
    print("gemi2 yerleştiriliyor")
    gemi_yon = random.choice([True, False])
    if gemi_yon:
        randomyan(2)
    else:
        randomdik(2)
    print("gemi1 yerleştiriliyor")
    gemi_yon = random.choice([True, False])
    if gemi_yon:
        randomyan(1)
    else:
        randomdik(1)


def newboard():
    for i in range(10):
        board.append(["?"] * 10)

    gemiyerlestir()


def boardprint(visible):
    if visible == 1:
        for satir in board:
            print(" ".join(satir))

    else:
        for satir2 in fake:
            print(" ".join(satir2))

    userinput()


def faketable():
    for i in range(10):
        fake.append(["?"] * 10)


def kontrol():
    u = 0
    for satir in board:
        for t in range(10):
            if satir[t] == "X":
                u = u + 1
    if u < 10:
        newboard()


def menu(son):
    global visible
    if son:
        while True:
            print("""
__________________________________________________

                -AMIRAL BATTI-

Düşman gemilerini görmek ister misiniz?

1 -> evet
0 -> hayır

___________________________________________________
""")
            secim = input("seçiminiz : ")
            if secim.isdigit():

                if secim == "1":
                    visible = 1
                    faketable()
                    newboard()
                    kontrol()
                    boardprint(1)

                elif secim == "0":
                    visible = 0
                    newboard()
                    faketable()
                    boardprint(0)

                else:
                    print("0  ya da 1 seçimi yapınız ")


def sonkontrol():
    #global hak
    u = 0
    for satir in board:
        for t in range(10):
            if satir[t] == "X":
                u = u + 1
    if u == 0:
        son()

    elif hak >= 32:
        son()
    else:
        boardprint(visible)
    boardprint(visible)


def son():
    print("""-----son-----------


       Puanınız : {}


    Yeniden başlamak ister misin? 

    1 --> Evet
    Diğer her şey --> çık



    """.format(abs(hak - 32)))
    sec = input("seçimiz: ")
    if sec == "1":
        menu(True)
    else:
        sys.exit(0)


def userinput():
    global hak
    x = input("Satır Seçiniz : ")
    y = input("Sütun Seçiniz : ")
    if x.isdigit() or y.isdigit():
        x = int(x)
        y = int(y)
        if x > 10 or y > 10:
            print("aralık dışında aralık 10-10")
        else:
            if board[x][y] == "X":
                print("Vurdun")
                board[x][y] = "x"  # küçük x (Xx)

                fake[x][y] = "x"
                hak += 1

            elif board[x][y] == "?":
                print("karavana")
                board[x][y] = "*"
                fake[x][y] = "*"
                hak += 1

            elif board[x][y] == "*" or board[x][y] == "x":
                print("zaten vurdun")

            # önlem alalım
            else:
                print("bilinmeyen bir sorun var gibi yeniden deneyin")

        sonkontrol()
    else:
        print("sadece rakamlar ")
        boardprint(visible)


menu(True)