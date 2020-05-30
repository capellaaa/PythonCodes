import os.path
import sys

temp_dict = {}
# curentUser = ""
ogr_kayit = {}
ders_kayit = {}
user_kayit = {}
ders_list = []
ders_bilgi = {}
ilk = True


def userMenu():
    global ogr_kayit
    global ders_kayit
    global ilk
    global userName
    global userPass

    if ilk:  # Sadece ilk başta giriş yazısının görünmesini sağladım.
        print("Online Ders otomasyonumuza hoşgeldiniz!")
        userLogin()
        ilk = False

    secim = 0
    while secim != 9:
        print("""
            *******************************************************
             *          1- Ders Ekleme                           *   
             *          2- Ders Silme                            *
             *          3- Öğrenci Bilgilerini Güncelleme        *
             *          4- Ogrenci Ekleme                        *
             *          5- Ogrenci Silme                         *
             *          6- Fatura Hesaplama                      *
             *          7- Öğrenci ve Ders Listeleme             *
             *          8- Öğrenciye Ders Ekleme                 *
             *          9- Çıkış                                 *                                       
            *******************************************************
        """)

        secim = input("Ne yapmak istiyorsunuz?")
        if secim.isnumeric():  # rakam kontrolü yapılır.
            secim = int(secim)  # string almasın diye int e çevirme işlemi yapılır.

            if secim == 1:
                ders_ekle()
            elif secim == 2:
                ders_silme()
            elif secim == 3:
                guncelle()
            elif secim == 4:
                ogr_ekle()
            elif secim == 5:
                ogr_silme()
            elif secim == 6:
                faturaBas()
            elif secim == 7:
                liste("ogr")
                liste("ders")
            elif secim == 8:
                ogrenciyeDersEkle()
            elif secim == 9:
                cikis()


def dosya_oku(dosyaYolu):
    dosya = open(dosyaYolu, "r")
    veri = dosya.read()
    dosya.close()
    return veri


def dosya_yaz(veri, dosyaYolu):
    # Dosya Oluşturacak ve içine verileri yazacak
    with open(dosyaYolu, "w") as file:
        file.write(str(veri))
        file.close()


def ogr_ekle():
    ogr_no = int(input("Ögrenci numarasını giriniz: "))
    ogr_ad = input("Adını giriniz: ")
    ogr_soyad = input("Soyadını giriniz: ")
    ogr_tel = input("Telefon numarasını giriniz: ")
    liste("ders")
    ogr_ders = int(input("Eğitim gördüğü dersin numarasini giriniz: "))
    ogr_kayit[ogr_no] = [ogr_ad, ogr_soyad, ogr_tel, ders_list[ogr_ders]]
    print(ogr_kayit[ogr_no])
    dosya_yaz(ogr_kayit, "ogr.txt")
    userMenu()


def ders_ekle():
    ders_ad = input("Ders adini giriniz: ")
    ders_ucret = int(input("Ders ücretini giriniz: "))
    ders_kayit[ders_ad] = ders_ucret
    print(ders_ad, ders_ucret)
    dosya_yaz(ders_kayit, "ders.txt")
    userMenu()


def arama(dosyaYolu="ogr.txt"):  # veriler dosyadan okunup sözlüğe atanır
    dosya = open(dosyaYolu, "r")
    veri = dosya.read()
    temp_dict = eval(veri)
    # print(temp_dict)
    # print(type(temp_dict))
    dosya.close()
    return temp_dict


def ogrenciArama():
    liste("ogr")
    sec = int(input("öğrenci numarasini giriniz: "))
    print(ogr_kayit[sec])
    print("""
    1-Bir Ust Menu
    2-Ana Menu
    """)
    sec2 = int(input("İşlemi seciniz: "))
    if sec2 == 1:
        ogrenciArama()
    else:
        userMenu()


def liste(ne_liste):
    global ders_kayit
    global ders_list
    global ogr_kayit
    global ders_bilgi

    if ne_liste == "ders":
        ders_kayit = arama("ders.txt")
        # print(ders_kayit)
        ders_list = list(ders_kayit.keys())
        print("**" * 50)
        for i in ders_list:
            print("Ders Numarası: {} Ders Adı: {} Ders Ucreti: {}".format(ders_list.index(i), i, ders_kayit[i]))
            print("--" * 50)
        print("**" * 50)

    elif ne_liste == "ogr":
        ogr_kayit = arama("ogr.txt")
        # print(ders_kayit)
        ogr_list = list(ogr_kayit.keys())
        print("**" * 50)
        for i in ogr_list:
            print("Öğrenci Id: {} Öğrenci Numarası: {} Öğrenci Adı: {} Öğrenci Soyadı: {} Aldığı Ders: {}"
                  "".format(ogr_list.index(i), ogr_list[ogr_list.index(i)], ogr_kayit[i][0], ogr_kayit[i][1],
                            ogr_kayit[i][3]))
            print("--" * 50)


def ogr_silme():
    liste("ogr")

    def ogr_sil(numara):
        del ogr_kayit[int(numara)]
        ogr = ogr_kayit
        dosya_yaz(ogr, "ogr.txt")
        print("""
                1-Bir Ust Menu
                2-Ana Menu
                """)
        sil = input("İşlemi seciniz: ")
        if sil == "1":
            ogr_silme()
        elif sil == "2":
            userMenu()
        else:
            print("Lutfen 1 ya da 2 giriniz!")
            ogr_silme()

    sil = int(input("Silinmesini istediğiniz öğrencinin numarasini giriniz: "))
    ogr_sil(sil)
    userMenu()


def ders_silme():
    liste("ders")

    def ders_sil(ders_ad):
        del ders_kayit[ders_ad]
        ders = ders_kayit
        dosya_yaz(ders, "ders.txt")
        print("""
                    1-Bir Ust Menu
                    2-Ana Menu
                    """)
        sil = input("İşlemi seciniz: ")
        if sil == "1":
            ders_silme()
        elif sil == "2":
            userMenu()
        else:
            print("Lutfen 1 ya da 2 giriniz!")
            ders_silme()

    sil = input("Silinmesini istediğiniz dersin adını giriniz: ")
    ders_sil(sil)
    userMenu()


def guncelle():
    liste("ogr")

    def ogr_update(numara):
        ogr_ad = input("Yeni Adı giriniz: ")
        ogr_soyad = input("Yeni Soyadı giriniz: ")
        ogr_tel = input("Yeni Telefon numarasını giriniz: ")
        liste("ders")
        ogr_ders = int(input("Eğitim gördüğü dersin numarasını giriniz: "))
        del ogr_kayit[int(numara)]
        ogr_kayit[numara] = [ogr_ad, ogr_soyad, ogr_tel, ders_list[ogr_ders]]
        print(ogr_kayit)
        dosya_yaz(ogr_kayit, "ogr.txt")

        print("""
                1-Öğrenci Bilgilerini Güncelleme
                2-Ana Menu
                """)

        sil = input("İşlemi seciniz: ")
        if sil == "1":
            guncelle()
        else:
            userMenu()

    update = int(input("Güncellemek istediğiniz öğrencinin id'sini veya numarasını giriniz: "))
    ogr_update(update)
    userMenu()


def faturaBas():  # tum öğrenciler için fatura bilgisi hesaplama

    try:
        ders_bilgi = arama("ders_bilgi.txt")
        ders_bilgi_list = list(ders_bilgi.keys())

        for i in ders_bilgi_list:
            if ders_bilgi[i][2] > 100:
                y_dersucret = ders_bilgi[i][2] * 0.1
                y_dersucret = ders_bilgi[i][2] - y_dersucret
                print("Öğrenci No:", i, "Ders Adı:", ders_bilgi[i][0],
                      "Ders Saati:", ders_bilgi[i][1], "Ders Ücreti:", ders_bilgi[i][2], "İndirimli Ders Ucreti:",
                      y_dersucret)

    except:
        print("Dosya okunamıyor!")
        userMenu()
    userMenu()


def ogrenciyeDersEkle():
    liste("ogr")
    no = int(input("Öğrenci numarasini giriniz: "))
    print(ogr_kayit[no])
    liste("ders")
    ders = ogr_kayit[no][3]
    print(ders)
    saatlik = ders_kayit[ders]
    ders_saat = float(input("Yapılan ders saatini giriniz: "))
    ucret = ders_saat * saatlik
    print(ucret)  # Ogrencinin aldığı ders saatine göre toplam ders ucretini hesaplanır.
    ders_bilgi[no] = [ders, ders_saat, ucret]
    dosya_yaz(ders_bilgi, "ders_bilgi.txt")


# Dosya boş mu dolu mu kontrol edilir. Boşsa varsayılan değer verilir.
def dosya_kontrol():
    global ogr_kayit
    global ders_kayit
    global user_kayit

    if not os.path.exists('users.txt'):  # Dosya var mı yok mu ona bakılır.
        file = open('users.txt', 'w')
        file.close()

    if not os.path.exists('ders.txt'):
        file = open('ders.txt', 'w')
        file.close()

    if not os.path.exists('ders_bilgi.txt'):
        file = open('ders_bilgi.txt', 'w')
        file.close()

    try:
        ogr_kayit = arama("ogr.txt")
        ders_kayit = arama("ders.txt")
        user_kayit = arama("users.txt")

    except:
        # Dosya boşsa ya da okunamadıysa expect e girer.
        veri = {185: ['esra', 'demir', '562', 'mat']}  # ogr.txt boş kalmasın diye veri ekledim
        veri2 = {'mat': 124}  # ders.txt boş kalmasın diye veri ekledim
        u_kontrol = {'Esra': '123'}
        dosya_yaz(veri, "ogr.txt")  # dosyaya verileri yazdırır
        dosya_yaz(veri2, "ders.txt")
        dosya_yaz(u_kontrol, "users.txt")
        print("Örnek veriler eklendi!")
        userMenu()


def cikis():
    # secim = {"cikis": ["evet", "hayır"]}
    # secim.get(cikis,"Lutfen gecerli karakter giriniz!")

    sec = input("Çıkıs yapmak istediğinize emin misiniz?")
    if sec == 'e' or sec == 'E' or sec == "yes" or sec == "evet":
        print("Çıkış yapılıyor..")
        sys.exit()
    else:
        print("Ana Menüye yöneltiliyorsunuz...")
        userMenu()


# Kullanıcı Girişi
def userLogin():
    print("Varsayılan; Kullanıcı Adı: Esra , Kullanıcı Parola: 123")

    userName = input("Kullanıcı İsmi Gir: ")
    userPass = input("Parolanızı Giriniz: ")
    # user_data = [] #user_data listeye atandı.

    try:
        if str(user_kayit[userName]) == userPass:
            print("Giriş İşlemi Başarılı!")
        else:
            print("Tekrar Deneyiniz!")
            userMenu()
    except:
        print("Tekrar Deneyiniz!")
        userMenu()


#     for user in user_kayit:
#         users_data.append(user.split())
#     sec = 0
#     login_success = 0
#     while sec < len(users_data):
#         username = users_data[sec][0]
#         password = users_data[sec][1]
#         if username == UserName and password == UserPass:
#             login_success = 1
#         sec += 1
#     if login_success == 1:
#         userMenu()
#     else:
#         print('Kullanıcı adı veya parola hatalı')
#         cikis()
#
# ques = input("Hesabınız var mı /yes/no: ")
# if ques == "yes" or ques == "y":
#     userLogin()
# else:
#     userRegister()

# Varsayılan kullanıcı adı ve parola belirtildiği için register fonksiyonunu yorum satırına alındı.
# def userRegister(): #Birden fazla kullanıcı için girisi olsaydı
#     print("\nÖzel Ders Otomasyonu kayıt ekranına hoş geldiniz!\n")
#     print("Giriş ekranına dönmek için 'E' tuşlayınız\n")
#     userSelect = input("Seçim: ")
#     if userSelect == "e" or userSelect == "E":
#         print("Kullanıcı giriş sayfasına yönlendiriliyorsunuz...")
#         userMenu()
#     UserName = input('Kullanıcı İsmi Gir: ')
#     if UserName in open('users.txt', 'r').read():
#         print("Bu kullancı zaten kayıtlı")
#         cikis()
#     UserPass = input('Parolanızı Giriniz: ')
#     c_password = input('Parolanızı Tekrar Giriniz: ')
#     if UserPass != c_password:
#         print('Üzgünüz Parola eşleşmiyor')
#         cikis()
#     handle = open('users.txt', 'a')
#     abc = UserName + ' ' + UserPass + '\n'
#     str_abc = str(abc)
#     handle.write(str_abc)
#     handle.close()
#     print('Kullanıcı kayıdı başarıyla oluşturuldu!')
#     userMenu()

dosya_kontrol()
userMenu()
