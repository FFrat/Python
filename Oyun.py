#Yapılacak şeyler :
#   ordu kur
#   fabrika kur
# fabrika ve ordu özelliklerini kaldırdın
import time

print("yeni")
print("███████████████████████████")
print("███████▀▀▀░░░░░░░▀▀▀███████")
print("████▀░░░░░░░░░░░░░░░░░▀████")
print("███│░░░░░░░░░░░░░░░░░░░│███")
print("██▌│░░░░░░░░░░░░░░░░░░░│▐██")
print("██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
print("██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
print("██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
print("██▌░│██████▌░░░▐██████│░▐██")
print("███░│▐███▀▀░░▄░░▀▀███▌│░███")
print("██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
print("██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
print("████▄─┘██▌░░░░░░░▐██└─▄████")
print("█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
print("████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
print("█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
print("███████▄░░░░░░░░░░░▄███████")
print("██████████▄▄▄▄▄▄▄██████████")
print("███████████████████████████\n\n")
print("Hoşgeldiniz!\n")
time.sleep(0.5)
print("=> Oyuna başlamadan önce karakterinize bir isim verin.\n")
time.sleep(0.5)
isimkoy = input("Karakter adı   >    ")
time.sleep(0.5)
print("\n=> Hoşgeldin",isimkoy,"\n")


class Oyuncu:
    def __init__(self):
        self.isim = isimkoy
        self.saglik = 100
        self.para = 170
        self.enerji = 100
        self.kuvvet = 30
        self.dayaniklilik = 25
        self.fabrika = 0
        self.kerestefabrikasi = 0
        self.demircelikfabrikasi = 0
        self.elmasislemefabrikasi = 0
    def goster(self):
        print("\nİsim : ",self.isim,"\n")
        time.sleep(0.5)
        print("Sağlık : ",self.saglik,"\n")
        time.sleep(0.5)
        print("Para : ",self.para,"\n")
        time.sleep(0.5)
        print("Enerji : ",self.enerji,"\n")
        time.sleep(0.5)
        print("Kuvvet : ",self.kuvvet,"\n")
        time.sleep(0.5)
        print("Dayanıklılık : ",self.dayaniklilik,"\n")
        time.sleep(0.5)
    def fabrikagoster(self):
        print("\nKereste fabrikası : ",self.kerestefabrikasi)
        print("\nDemir-çelik fabrikası : ",self.demircelikfabrikasi)
        print("\nElmas işleme fabrikası : ",self.elmasislemefabrikasi)
oyuncu = Oyuncu()

class Kolaydusman(Oyuncu):
    def __init__(self):
        Oyuncu.__init__(self)
        self.isim = "Thedore Bagwell"
        self.enerji = 100
        self.para = 40
        self.kuvvet = 60
        self.dayaniklilik = 50
    def goster(self):
        Oyuncu.goster(self)
kolaydusman = Kolaydusman()

class Ortadusman(Oyuncu):
    def __init__(self):
        Oyuncu.__init__(self)
        self.isim = "Lincoln Burrows"
        self.enerji = 100
        self.para = 60
        self.kuvvet = 100
        self.dayaniklilik = 110
    def goster(self):
        Oyuncu.goster(self)
ortadusman = Ortadusman()

class Zordusman(Oyuncu):
    def __init__(self):
        Oyuncu.__init__(self)    
        self.isim = "Michael Scofield"
        self.enerji = 100
        self.para = 200
        self.kuvvet = 300
        self.dayaniklilik = 300
    def goster(self):
        Oyuncu.goster(self)
zordusman = Zordusman()

class Goblin(Oyuncu):
    def __init__(self):
        Oyuncu.__init__(self)
        self.isim = "Goblin"
        self.enerji = 100
        self.para = 10
        self.kuvvet = 15
        self.dayaniklilik = 15
        self.miktar = 1
    def goster(self):
        Oyuncu.goster(self)
        print("Savaşacağın goblin sayısı : ",self.miktar,"\n\n")
goblin = Goblin()

class Devörümcek(Oyuncu):
    def __init__(self):
        Oyuncu.__init__(self)
        self.isim = "Dev örümcek"
        self.enerji = 100
        self.para = 25
        self.kuvvet = 50
        self.dayaniklilik = 40
        self.miktar = 1
    def goster(self):
        Oyuncu.goster(self)
        print("Savaşacağın Dev örümcek miktarı : ",self.miktar,"\n\n")
devörümcek = Devörümcek()

class Dev(Oyuncu):
    def __init__(self):
        Oyuncu.__init__(self)
        self.isim = "Dev"
        self.enerji = 100
        self.para = 40
        self.kuvvet = 70
        self.dayaniklilik = 100
        self.miktar = 1
    def goster(self):
        Oyuncu.goster(self)
        print("Savaşacağın Dev miktarı : ",self.miktar,"\n\n")
dev = Dev()
class Savasici():
    def kolaysavasici(self):
        while True:
            if oyuncu.enerji>0:
                print("\n=> Düşmana Saldırdın!\n")
                time.sleep(0.5)
                oyuncu.enerji = oyuncu.enerji - (oyuncu.kuvvet/oyuncu.dayaniklilik)*5
                print("\nKalan Enerji : ",oyuncu.enerji,"\n")
                time.sleep(0.5)
                kolaydusman.saglik = kolaydusman.saglik - (oyuncu.kuvvet/kolaydusman.dayaniklilik)*10
                print("\nDüşman Sağlığı : ",kolaydusman.saglik,"\n")
                time.sleep(1)
                if kolaydusman.saglik>0 and kolaydusman.enerji>0:
                    print("\n\n=> Düşman saldırıya geçti!\n")
                    time.sleep(0.5)
                    kolaydusman.enerji = kolaydusman.enerji -(kolaydusman.kuvvet/kolaydusman.dayaniklilik)*5
                    oyuncu.saglik = oyuncu.saglik - (kolaydusman.kuvvet/oyuncu.dayaniklilik)*5
                    print("\nDüşmanın Enerjisi : ",kolaydusman.enerji,"\n")
                    print("\nSağlık : ",oyuncu.saglik,"\n")
                    time.sleep(0.5)
                    if oyuncu.saglik<=0:
                        print("=> Öldün!\n\n")
                        time.sleep(2)
                        print("=> Oyun kapatılıyor...")
                        time.sleep(3)
                        quit()
                    elif kolaydusman.saglik<=0:
                        print("\n=> Düşmanı öldürdün tebrikler!\n")
                        time.sleep(0.5)
                        oyuncu.para = oyuncu.para + kolaydusman.para
                        print("\nDüşmanın tüm parasını aldın.\n")
                        time.sleep(0.5)
                        print("Para : ",oyuncu.para)
                        time.sleep(0.5)
                        print("Sağlık : ",oyuncu.saglik,"\n")
                        time.sleep(0.5)
                        print("\n=> Ana menüye yönlendiriliyorsun...\n\n")
                        time.sleep(3)
                        kolaydusman.saglik = kolaydusman.saglik + 100
                        baslangıc2()
                    else:
                        pass
                elif kolaydusman.saglik<=0:
                    print("\n=> Düşmanı öldürdün tebrikler!\n")
                    time.sleep(0.5)
                    oyuncu.para = oyuncu.para + kolaydusman.para
                    print("\nDüşmanın tüm parasını aldın.\n")
                    time.sleep(0.5)
                    print("Para : ",oyuncu.para,"\n\n")
                    time.sleep(0.5)
                    print("Sağlık : ",oyuncu.saglik,"\n")
                    time.sleep(0.5)
                    print("\n=> Ana menüye yönlendiriliyorsun...\n\n")
                    time.sleep(3)
                    kolaydusman.saglik = kolaydusman.saglik + 100
                    baslangıc2()
                elif kolaydusman.enerji<=0:
                    print("\n\nDüşmanınızın enerjisi bitti.\n\n")
                    time.sleep(0.5)
                    oyuncu.para = oyuncu.para + kolaydusman.para
                    kolaydusman.saglik = kolaydusman.saglik - kolaydusman.saglik + 100
                    print("Düşmanınızın tüm parasını aldınız.\n\n")
                    time.sleep(0.5)
                    print("Para : ",oyuncu.para,"\n\n")
                    time.sleep(0.5)
                    print("Ana menüye yönlendiriliyorsunuz...")
                    time.sleep(3)
                    baslangıc2()
                else:
                    pass
                break
            elif oyuncu.enerji<=0:
                    print("\n\nDaha fazla saldıramazsın.\n\n")
                    time.sleep(0.5)
                    print("Enerjin bitti.\n\n")
                    time.sleep(0.5)
                    print("Geri çekiliyorsun.\n\n")
                    time.sleep(0.5)
                    print("=> Ana menüye yönlendiriliyorsun...")
                    time.sleep(3)
                    kolaydusman.saglik = kolaydusman.saglik - kolaydusman.saglik + 100
                    baslangıc2()
            else:
                pass
    def ortasavasici(self):
        while True:
            if oyuncu.enerji>0:
                print("\n=> Düşmana Saldırdın!\n")
                time.sleep(0.5)
                oyuncu.enerji = oyuncu.enerji - (oyuncu.kuvvet/oyuncu.dayaniklilik)*5
                print("\nKalan Enerji : ",oyuncu.enerji,"\n")
                time.sleep(0.5)
                ortadusman.saglik = ortadusman.saglik - (oyuncu.kuvvet/ortadusman.dayaniklilik)*10
                print("\nDüşman sağlığı : ",ortadusman.saglik,"\n")
                time.sleep(1)
                if ortadusman.saglik>0 and ortadusman.enerji>0:
                    print("\n\n=> Düşman saldırıya geçti!\n")
                    time.sleep(0.5)
                    ortadusman.enerji = ortadusman.enerji -(ortadusman.kuvvet/ortadusman.dayaniklilik)*5
                    oyuncu.saglik = oyuncu.saglik - (ortadusman.kuvvet/oyuncu.dayaniklilik)*5
                    print("\nSağlık : ",oyuncu.saglik,"\n")
                    time.sleep(0.5)
                    if oyuncu.saglik<=0:
                        print("=> Öldün!\n\n")
                        time.sleep(2)
                        print("=> Oyun kapatılıyor...")
                        time.sleep(3)
                        quit()
                    elif ortadusman.saglik<=0:
                        print("\n=> Düşmanı öldürdün tebrikler!\n")
                        time.sleep(0.5)
                        oyuncu.para = oyuncu.para + ortadusman.para
                        print("\nDüşmanın tüm parasını aldın.\n")
                        time.sleep(0.5)
                        print("Para : ",oyuncu.para)
                        time.sleep(0.5)
                        print("Sağlık : ",oyuncu.saglik,"\n")
                        time.sleep(0.5)
                        print("\n=> Ana menüye yönlendiriliyorsun...\n\n")
                        time.sleep(3)
                        ortadusman.saglik = ortadusman.saglik + 100
                        baslangıc2()
                    else:
                        pass
                elif ortadusman.saglik<=0:
                    print("\n=> Düşmanı öldürdün tebrikler!\n")
                    time.sleep(0.5)
                    oyuncu.para = oyuncu.para + ortadusman.para
                    print("\nDüşmanın tüm parasını aldın.\n")
                    time.sleep(0.5)
                    print("Para : ",oyuncu.para,"\n\n")
                    time.sleep(0.5)
                    print("Sağlık : ",oyuncu.saglik,"\n")
                    time.sleep(0.5)
                    print("\n=> Ana menüye yönlendiriliyorsun...\n\n")
                    time.sleep(3)
                    ortadusman.saglik = ortadusman.saglik + 100
                    baslangıc2()
                elif ortadusman.enerji<=0:
                    print("\n\nDüşmanınızın enerjisi bitti.\n\n")
                    time.sleep(0.5)
                    oyuncu.para = oyuncu.para + ortadusman.para
                    ortadusman.saglik = ortadusman.saglik - ortadusman.saglik + 100
                    print("Düşmanınızın tüm parasını aldınız.\n\n")
                    time.sleep(0.5)
                    print("Para : ",oyuncu.para,"\n\n")
                    time.sleep(0.5)
                    print("Ana menüye yönlendiriliyorsunuz...")
                    time.sleep(3)
                    baslangıc2()
                else:
                    pass
                break
            elif oyuncu.enerji<=0:
                    print("\n\nDaha fazla saldıramazsın.\n\n")
                    time.sleep(0.5)
                    print("Enerjin bitti.\n\n")
                    time.sleep(0.5)
                    print("Geri çekiliyorsun.\n\n")
                    time.sleep(0.5)
                    print("=> Ana menüye yönlendiriliyorsun...")
                    time.sleep(3)
                    ortadusman.saglik = ortadusman.saglik - ortadusman.saglik + 100
                    baslangıc2()
            else:
                pass
    def zorsavasici(self):
        while True:
            if oyuncu.enerji>0:
                print("\n=> Düşmana Saldırdın!\n")
                time.sleep(0.5)
                oyuncu.enerji = oyuncu.enerji - (oyuncu.kuvvet/oyuncu.dayaniklilik)*5
                print("\nKalan Enerji : ",oyuncu.enerji,"\n")
                time.sleep(0.5) 
                zordusman.saglik = zordusman.saglik - (oyuncu.kuvvet/zordusman.dayaniklilik)*10
                print("\nDüşman sağlığı : ",zordusman.saglik,"\n")
                time.sleep(1)
                if zordusman.saglik>0 and zordusman.enerji>0:
                    print("\n\n=> Düşman saldırıya geçti!\n")
                    time.sleep(0.5)
                    zordusman.enerji = zordusman.enerji -(zordusman.kuvvet/zordusman.dayaniklilik)*5
                    oyuncu.saglik = oyuncu.saglik - (zordusman.kuvvet/oyuncu.dayaniklilik)*5
                    print("\nSağlık : ",oyuncu.saglik,"\n")
                    time.sleep(0.5)
                    if oyuncu.saglik<=0:
                        print("=> Öldün!\n\n")
                        time.sleep(2)
                        print("=> Oyun kapatılıyor...")
                        time.sleep(3)
                        quit()
                    elif zordusman.saglik<=0:
                        print("\n=> Düşmanı öldürdün tebrikler!\n")
                        time.sleep(0.5)
                        oyuncu.para = oyuncu.para + zordusman.para
                        print("\nDüşmanın tüm parasını aldın.\n")
                        time.sleep(0.5)
                        print("Para : ",oyuncu.para)
                        time.sleep(0.5)
                        print("Sağlık : ",oyuncu.saglik,"\n")
                        time.sleep(0.5)
                        print("\n=> Ana menüye yönlendiriliyorsun...\n\n")
                        time.sleep(3)
                        zordusman.saglik = zordusman.saglik + 100
                        baslangıc2()
                    else:
                        pass
                elif zordusman.saglik<=0:
                    print("\n=> Düşmanı öldürdün tebrikler!\n")
                    time.sleep(0.5)
                    oyuncu.para = oyuncu.para + zordusman.para
                    print("\nDüşmanın tüm parasını aldın.\n")
                    time.sleep(0.5)
                    print("Para : ",oyuncu.para,"\n\n")
                    time.sleep(0.5)
                    print("Sağlık : ",oyuncu.saglik,"\n")
                    time.sleep(0.5)
                    print("\n=> Ana menüye yönlendiriliyorsun...\n\n")
                    time.sleep(3)
                    zordusman.saglik = zordusman.saglik + 100
                    baslangıc2()
                elif zordusman.enerji<=0:
                    print("\n\nDüşmanınızın enerjisi bitti.\n\n")
                    time.sleep(0.5)
                    oyuncu.para = oyuncu.para + zordusman.para
                    zordusman.saglik = zordusman.saglik - zordusman.saglik + 100
                    print("Düşmanınızın tüm parasını aldınız.\n\n")
                    time.sleep(0.5)
                    print("Para : ",oyuncu.para,"\n\n")
                    time.sleep(0.5)
                    print("Ana menüye yönlendiriliyorsunuz...")
                    time.sleep(3)
                    baslangıc2()
                else:
                    pass
                break
            elif oyuncu.enerji<=0:
                    print("\n\nDaha fazla saldıramazsın.\n\n")
                    time.sleep(0.5)
                    print("Enerjin bitti.\n\n")
                    time.sleep(0.5)
                    print("Geri çekiliyorsun.\n\n")
                    time.sleep(0.5)
                    print("=> Ana menüye yönlendiriliyorsun...")
                    time.sleep(3)
                    zordusman.saglik = zordusman.saglik - zordusman.saglik + 100
                    baslangıc2()
            else:
                pass
    def goblinsavaşiçi(self):
        while True:
            if oyuncu.enerji>0:
                print("\n=> Düşmana Saldırdın!\n")
                time.sleep(0.5)
                oyuncu.enerji = oyuncu.enerji - (oyuncu.kuvvet/oyuncu.dayaniklilik)*5
                print("\nKalan Enerji : ",oyuncu.enerji,"\n")
                time.sleep(0.5) 
                goblin.saglik = goblin.saglik - (oyuncu.kuvvet/(goblin.dayaniklilik*goblin.miktar))*10
                print("\nDüşman sağlığı : ",goblin.saglik,"\n")
                time.sleep(1)
                if goblin.saglik>0 and goblin.enerji>0:
                    print("\n\n=> Düşman saldırıya geçti!\n")
                    time.sleep(0.5)
                    goblin.enerji = goblin.enerji -(goblin.kuvvet/goblin.dayaniklilik)*5
                    oyuncu.saglik = oyuncu.saglik - ((goblin.kuvvet*goblin.miktar)/oyuncu.dayaniklilik)*5
                    print("\nSağlık : ",oyuncu.saglik,"\n")
                    time.sleep(0.5)
                    if oyuncu.saglik<=0:
                        print("=> Öldün!\n\n")
                        time.sleep(2)
                        print("=> Oyun kapatılıyor...")
                        time.sleep(3)
                        quit()
                    elif goblin.saglik<=0:
                        print("\n=> Düşmanı öldürdün tebrikler!\n")
                        time.sleep(0.5)
                        oyuncu.para = oyuncu.para + (goblin.para*goblin.miktar)
                        print("\nDüşmanın tüm parasını aldın.\n")
                        time.sleep(0.5)
                        print("Para : ",oyuncu.para)
                        time.sleep(0.5)
                        print("Sağlık : ",oyuncu.saglik,"\n")
                        time.sleep(0.5)
                        goblin.miktar = goblin.miktar + 1
                        time.sleep(0.5)
                        print("\n=> Ana menüye yönlendiriliyorsun...\n\n")
                        time.sleep(3)
                        goblin.saglik = goblin.saglik - goblin.saglik + 100
                        baslangıc2()
                    else:
                        pass
                elif goblin.saglik<=0:
                    print("\n=> Düşmanı öldürdün tebrikler!\n")
                    time.sleep(0.5)
                    oyuncu.para = oyuncu.para + (goblin.para*goblin.miktar)
                    print("\nDüşmanın tüm parasını aldın.\n")
                    time.sleep(0.5)
                    print("Para : ",oyuncu.para,"\n\n")
                    time.sleep(0.5)
                    print("Sağlık : ",oyuncu.saglik,"\n")
                    time.sleep(0.5)
                    goblin.miktar = goblin.miktar + 1
                    time.sleep(0.5)
                    print("\n=> Ana menüye yönlendiriliyorsun...\n\n")
                    time.sleep(3)
                    goblin.saglik = goblin.saglik - goblin.saglik + 100
                    baslangıc2()
                elif goblin.enerji<=0:
                    print("\n\nDüşmanınızın enerjisi bitti.\n\n")
                    time.sleep(0.5)
                    oyuncu.para = oyuncu.para + goblin.para
                    goblin.saglik = goblin.saglik - goblin.saglik + 100
                    print("Düşmanınızın tüm parasını aldınız.\n\n")
                    time.sleep(0.5)
                    print("Para : ",oyuncu.para,"\n\n")
                    time.sleep(0.5)
                    print("Ana menüye yönlendiriliyorsunuz...")
                    time.sleep(3)
                    baslangıc2()
                else:
                    pass
                break
            elif oyuncu.enerji<=0:
                    print("\n\nDaha fazla saldıramazsın.\n\n")
                    time.sleep(0.5)
                    print("Enerjin bitti.\n\n")
                    time.sleep(0.5)
                    print("Geri çekiliyorsun.\n\n")
                    time.sleep(0.5)
                    print("=> Ana menüye yönlendiriliyorsun...")
                    time.sleep(3)
                    goblin.saglik = goblin.saglik - goblin.saglik + 100
                    baslangıc2()
            else:
                pass
    def devörümceksavaşiçi(self):
        while True:
            if oyuncu.enerji>0:
                print("\n=> Düşmana Saldırdın!\n")
                time.sleep(0.5)
                oyuncu.enerji = oyuncu.enerji - (oyuncu.kuvvet/oyuncu.dayaniklilik)*5
                print("\nKalan Enerji : ",oyuncu.enerji,"\n")
                time.sleep(0.5) 
                devörümcek.saglik = devörümcek.saglik - (oyuncu.kuvvet/(devörümcek.dayaniklilik*devörümcek.miktar))*10
                print("\nDüşman sağlığı : ",devörümcek.saglik,"\n")
                time.sleep(1)
                if devörümcek.saglik>0 and devörümcek.enerji>0:
                    print("\n\n=> Düşman saldırıya geçti!\n")
                    time.sleep(0.5)
                    devörümcek.enerji = devörümcek.enerji -(devörümcek.kuvvet/devörümcek.dayaniklilik)*5
                    oyuncu.saglik = oyuncu.saglik - ((devörümcek.kuvvet*devörümcek.miktar)/oyuncu.dayaniklilik)*5
                    print("\nSağlık : ",oyuncu.saglik,"\n")
                    time.sleep(0.5)
                    if oyuncu.saglik<=0:
                        print("=> Öldün!\n\n")
                        time.sleep(2)
                        print("=> Oyun kapatılıyor...")
                        time.sleep(3)
                        quit()
                    elif devörümcek.saglik<=0:
                        print("\n=> Düşmanı öldürdün tebrikler!\n")
                        time.sleep(0.5)
                        oyuncu.para = oyuncu.para + (devörümcek.para*devörümcek.miktar)
                        print("\nDüşmanın tüm parasını aldın.\n")
                        time.sleep(0.5)
                        print("Para : ",oyuncu.para)
                        time.sleep(0.5)
                        print("Sağlık : ",oyuncu.saglik,"\n")
                        time.sleep(0.5)
                        devörümcek.miktar = devörümcek.miktar + 1
                        time.sleep(0.5)
                        print("\n=> Ana menüye yönlendiriliyorsun...\n\n")
                        time.sleep(3)
                        devörümcek.saglik = devörümcek.saglik - devörümcek.saglik + 100
                        baslangıc2()
                    else:
                        pass
                elif devörümcek.saglik<=0:
                    print("\n=> Düşmanı öldürdün tebrikler!\n")
                    time.sleep(0.5)
                    oyuncu.para = oyuncu.para + (devörümcek.para*devörümcek.miktar)
                    print("\nDüşmanın tüm parasını aldın.\n")
                    time.sleep(0.5)
                    print("Para : ",oyuncu.para,"\n\n")
                    time.sleep(0.5)
                    print("Sağlık : ",oyuncu.saglik,"\n")
                    time.sleep(0.5)
                    devörümcek.miktar = devörümcek.miktar + 1
                    time.sleep(0.5)
                    print("\n=> Ana menüye yönlendiriliyorsun...\n\n")
                    time.sleep(3)
                    devörümcek.saglik = devörümcek.saglik - devörümcek.saglik + 100
                    baslangıc2()
                elif devörümcek.enerji<=0:
                    print("\n\nDüşmanınızın enerjisi bitti.\n\n")
                    time.sleep(0.5)
                    oyuncu.para = oyuncu.para + devörümcek.para
                    devörümcek.saglik = devörümcek.saglik - devörümcek.saglik + 100
                    print("Düşmanınızın tüm parasını aldınız.\n\n")
                    time.sleep(0.5)
                    print("Para : ",oyuncu.para,"\n\n")
                    time.sleep(0.5)
                    print("Ana menüye yönlendiriliyorsunuz...")
                    time.sleep(3)
                    baslangıc2()
                else:
                    pass
                break
            elif oyuncu.enerji<=0:
                    print("\n\nDaha fazla saldıramazsın.\n\n")
                    time.sleep(0.5)
                    print("Enerjin bitti.\n\n")
                    time.sleep(0.5)
                    print("Geri çekiliyorsun.\n\n")
                    time.sleep(0.5)
                    print("=> Ana menüye yönlendiriliyorsun...")
                    time.sleep(3)
                    devörümcek.saglik = devörümcek.saglik - devörümcek.saglik + 100
                    baslangıc2()
            else:
                pass
    def devsavaşiçi(self):
        while True:
            if oyuncu.enerji>0:
                print("\n=> Düşmana Saldırdın!\n")
                time.sleep(0.5)
                oyuncu.enerji = oyuncu.enerji - (oyuncu.kuvvet/oyuncu.dayaniklilik)*5
                print("\nKalan Enerji : ",oyuncu.enerji,"\n")
                time.sleep(0.5) 
                dev.saglik = dev.saglik - (oyuncu.kuvvet/(dev.dayaniklilik*dev.miktar))*10
                print("\nDüşman sağlığı : ",dev.saglik,"\n")
                time.sleep(1)
                if dev.saglik>0 and dev.enerji>0:
                    print("\n\n=> Düşman saldırıya geçti!\n")
                    time.sleep(0.5)
                    dev.enerji = dev.enerji -(dev.kuvvet/dev.dayaniklilik)*5
                    oyuncu.saglik = oyuncu.saglik - ((dev.kuvvet*dev.miktar)/oyuncu.dayaniklilik)*5
                    print("\nSağlık : ",oyuncu.saglik,"\n")
                    time.sleep(0.5)
                    if oyuncu.saglik<=0:
                        print("=> Öldün!\n\n")
                        time.sleep(2)
                        print("=> Oyun kapatılıyor...")
                        time.sleep(3)
                        quit()
                    elif dev.saglik<=0:
                        print("\n=> Düşmanı öldürdün tebrikler!\n")
                        time.sleep(0.5)
                        oyuncu.para = oyuncu.para + (dev.para*dev.miktar)
                        print("\nDüşmanın tüm parasını aldın.\n")
                        time.sleep(0.5)
                        print("Para : ",oyuncu.para)
                        time.sleep(0.5)
                        print("Sağlık : ",oyuncu.saglik,"\n")
                        time.sleep(0.5)
                        dev.miktar = dev.miktar + 1
                        time.sleep(0.5)
                        print("\n=> Ana menüye yönlendiriliyorsun...\n\n")
                        time.sleep(3)
                        dev.saglik = dev.saglik - dev.saglik + 100
                        baslangıc2()
                    else:
                        pass
                elif dev.saglik<=0:
                    print("\n=> Düşmanı öldürdün tebrikler!\n")
                    time.sleep(0.5)
                    oyuncu.para = oyuncu.para + (dev.para*dev.miktar)
                    print("\nDüşmanın tüm parasını aldın.\n")
                    time.sleep(0.5)
                    print("Para : ",oyuncu.para,"\n\n")
                    time.sleep(0.5)
                    print("Sağlık : ",oyuncu.saglik,"\n")
                    time.sleep(0.5)
                    dev.miktar = dev.miktar + 1
                    time.sleep(0.5)
                    print("\n=> Ana menüye yönlendiriliyorsun...\n\n")
                    time.sleep(3)
                    dev.saglik = dev.saglik - dev.saglik + 100
                    baslangıc2()
                elif dev.enerji<=0:
                    print("\n\nDüşmanınızın enerjisi bitti.\n\n")
                    time.sleep(0.5)
                    oyuncu.para = oyuncu.para + dev.para
                    dev.saglik = dev.saglik - dev.saglik + 100
                    print("Düşmanınızın tüm parasını aldınız.\n\n")
                    time.sleep(0.5)
                    print("Para : ",oyuncu.para,"\n\n")
                    time.sleep(0.5)
                    print("Ana menüye yönlendiriliyorsunuz...")
                    time.sleep(3)
                    baslangıc2()
                else:
                    pass
                break
            elif oyuncu.enerji<=0:
                    print("\n\nDaha fazla saldıramazsın.\n\n")
                    time.sleep(0.5)
                    print("Enerjin bitti.\n\n")
                    time.sleep(0.5)
                    print("Geri çekiliyorsun.\n\n")
                    time.sleep(0.5)
                    print("=> Ana menüye yönlendiriliyorsun...")
                    time.sleep(3)
                    dev.saglik = dev.saglik - dev.saglik + 100
                    baslangıc2()
            else:
                pass
savasici = Savasici()

class Fabrikalar:
    def Kerestefabrikasi(self,miktar):
        self.miktar = input("\n\nKaç adet kereste fabrikası kurmak istiyorsun   >    \n\n")
        print("Fabrika kuruluyor...")
        time.sleep(3)
        oyuncu.fabrika = oyuncu.fabrika + self.miktar
        oyuncu.kerestefabrikasi = oyuncu.kerestefabrikası + self.miktar
        print("\n\nTebrikler",self.miktar,"adet kereste fabrikası kurdunuz.\n\n")
        time.sleep(0.5)
    def Demircelikfabrikasi(self,miktar):
        self.miktar = input("\n\nKaç adet demir-çelik fabrikası kurmak istiyorsun   >    \n\n")
        print("Fabrika kuruluyor...")
        time.sleep(3)
        oyuncu.fabrika = oyuncu.fabrika + self.miktar
        oyuncu.demircelikfabrikasi = oyuncu.demircelikfabrikasi + self.miktar
        print("\n\nTebrikler",self.miktar,"adet demir-çelik fabrikası kurdunuz.\n\n")
        time.sleep(0.5)
    def Elmasislemefabrikasi(self,miktar):
        self.miktar = input("\n\nKaç adet elmas işleme fabrikası kurmak istiyorsun   >    \n\n")
        print("Fabrika kuruluyor...")
        time.sleep(3)
        oyuncu.fabrika = oyuncu.fabrika + self.miktar
        oyuncu.elmasislemefabrikasi = oyuncu.elmasislemefabrikasi + self.miktar
        print("\n\nTebrikler",self.miktar,"adet elmas işleme fabrikası kurdunuz.\n\n")
        time.sleep(0.5)
    def fabrikakur(self):
        while True:
            print("\n\nFabrika kur | Fabrikalarımı göster\n\n")
            fabrikaislem = input("Yukarıdaki işlemlerden birini giriniz.   >    ")
            if fabrikaislem=="Fabrika kur" or fabrikaislem=="fabrika kur" or fabrikaislem=="kur" or fabrikaislem=="Kur":
                print("\n\nFabrikalar : \n\n")
                print("Kereste fabrikası : \n\n\t10 saniyede bir 5 para\n\n150 para\n\n")
                print("Demir-çelik fabrikası : \n\n\t20 saniyede bir 20 para\n\n300 para\n\n")
                print("Elmas işleme fabrikası : \n\n\t30 saniyede bir 40 para\n\n500 para\n\n")
                print("\n\nKereste fabrikası | Demir-çelik fabrikası | Elmas işleme fabrikası | Geri \n\n")
                fabrikasec = input("Yukarıdaki fabrikalardan birini seçiniz   >    ")
                if fabrikasec=="Kereste fabrikası" or fabrikasec=="kereste fabrikası" or fabrikasec=="Kereste" or fabrikasec=="kereste":
                    fabrikalar.Kerestefabrikasi()
                elif fabrikasec=="Demir-çelik fabrikası" or fabrikasec=="demir-çelik fabrikası" or fabrikasec=="Demir-çelik" or fabrikasec=="demir-çelik":
                    fabrikalar.Demircelikfabrikasi()
                elif fabrikasec=="Elmas işleme fabrikası" or fabrikasec=="elmas işleme fabrikası" or fabrikasec=="Elmas işleme" or fabrikasec=="elmas işleme":
                    fabrikalar.Elmasislemefabrikasi()
                elif fabrikasec=="Geri" or fabrikasec=="geri":
                    baslangıc2()
                else:
                    time.sleep(0.5)
                    print("\n\n",fabrikasec,"bir seçenek değil\n\n")
                    time.sleep(0.5)
            elif fabrikaislem=="Fabrikalarımı göster" or fabrikaislem=="fabrikalarımı göster" or fabrikaislem=="göster" or fabrikaislem=="Göster":
                oyuncu.fabrikagoster()
fabrikalar = Fabrikalar()
class Oyun:
    def market(self):
        while True:
            print("\nSilah | Zırh | İksirler | Geri\n")
            time.sleep(0.5)
            marketsecenekler = input("Yukarıdaki katagorilerden birini seçiniz   >    ")
            if marketsecenekler=="zırh" or marketsecenekler=="Zırh":
                print("\n\n███████████████████")
                print("███░░░░█████░░░░███")
                print("██░░░░░░███░░░░░░██")
                print("███░░░░░░░░░░░░░███")
                print("████░░░░░░░░░░░████")
                print("█████░░░░░░░░░█████")
                print("███████████████████\n")
                print("\nZırhlar : \n\n")
                time.sleep(0.5)
                print("Deri zırh :\n\n\t30 dayanıklılık\n\t10 para\n\n")
                time.sleep(0.5)
                print("Altın zırh :\n\n\t70 dayanıklılık \n\t70 para\n\n")
                time.sleep(0.5)
                print("Demir zırh :\n\n\t150 dayanıklılık \n\t100 para\n\n")
                time.sleep(0.5)
                print("Elmas zırh :\n\n\t350 dayanıklılık \n\t290 para\n\n")
                time.sleep(0.5)
                while True:
                    print("Deri zırh | Altın zırh | Demir zırh | Elmas zırh | Geri\n\n")
                    zırhsec = input("Yukarıdaki zırhlardan birini seçiniz   >    ")
                    if zırhsec=="deri zırh" or zırhsec=="Deri zırh" or zırhsec=="Deri Zırh" or zırhsec=="deri Zırh" or zırhsec=="deri" or zırhsec=="Deri":
                        if oyuncu.para>=10:
                            oyuncu.dayaniklilik-oyuncu.dayaniklilik
                            oyuncu.dayaniklilik = oyuncu.dayaniklilik + 30
                            oyuncu.para = oyuncu.para - 10
                            time.sleep(0.5)
                            print("\nZırh başarıyla alınmıştır!","\n")
                            time.sleep(0.5)
                            print("Kalan para : ",oyuncu.para,"\n")
                            time.sleep(0.5)
                            print("Dayanıklılık : ",oyuncu.dayaniklilik,"\n")
                            time.sleep(0.5)
                            break
                        else:
                            time.sleep(0.5)
                            print("\nBu zırhı alamazsınız . Yeterli paranız yok !\n")
                            time.sleep(0.5)
                    elif zırhsec=="altın zırh" or zırhsec=="Altın zırh" or zırhsec=="Altın Zırh" or zırhsec=="altın Zırh" or zırhsec=="altın" or zırhsec=="Altın":
                        if oyuncu.para>=70:    
                            oyuncu.dayaniklilik-oyuncu.dayaniklilik
                            oyuncu.dayaniklilik = oyuncu.dayaniklilik + 70
                            oyuncu.para = oyuncu.para - 70
                            time.sleep(0.5)
                            print("\nZırh başarıyla alınmıştır!","\n")
                            time.sleep(0.5)
                            print("Kalan para : ",oyuncu.para,"\n")
                            time.sleep(0.5)
                            print("Dayanıklılık : ",oyuncu.dayaniklilik,"\n")
                            time.sleep(0.5)
                            break
                        else:
                            time.sleep(0.5)
                            print("\nBu zırhı alamazsınız . Yeterli paranız yok !\n")
                            time.sleep(0.5)
                    elif zırhsec=="demir zırh" or zırhsec=="Demir zırh" or zırhsec=="Demir Zırh" or zırhsec=="demir Zırh" or zırhsec=="demir" or zırhsec=="Demir":
                        if oyuncu.para>=100:    
                            oyuncu.dayaniklilik-oyuncu.dayaniklilik
                            oyuncu.dayaniklilik = oyuncu.dayaniklilik + 150
                            oyuncu.para = oyuncu.para - 100
                            time.sleep(0.5)
                            print("\nZırh başarıyla alınmıştır!","\n")
                            time.sleep(0.5)
                            print("Kalan para : ",oyuncu.para,"\n")
                            time.sleep(0.5)
                            print("Dayanıklılık : ",oyuncu.dayaniklilik,"\n")
                            time.sleep(0.5)
                            break
                        else:
                            time.sleep(0.5)
                            print("\nBu zırhı alamazsınız . Yeterli paranız yok !\n")
                            time.sleep(0.5)
                    elif zırhsec=="elmas zırh" or zırhsec=="Elmas zırh" or zırhsec=="Elmas Zırh" or zırhsec=="elmas Zırh" or zırhsec=="elmas" or zırhsec=="Elmas":
                        if oyuncu.para>=290:  
                            oyuncu.dayaniklilik-oyuncu.dayaniklilik 
                            oyuncu.dayaniklilik = oyuncu.dayaniklilik + 350
                            oyuncu.para = oyuncu.para - 290
                            time.sleep(0.5)
                            print("\nZırh başarıyla alınmıştır!","\n")
                            time.sleep(0.5)
                            print("Kalan para : ",oyuncu.para,"\n")
                            time.sleep(0.5)
                            print("Dayanıklılık : ",oyuncu.dayaniklilik,"\n")
                            time.sleep(0.5)
                            break
                        else:
                            time.sleep(0.5)
                            print("\nBu zırhı alamazsınız . Yeterli paranız yok !\n")
                            time.sleep(0.5)
                    elif zırhsec=="geri" or zırhsec=="Geri":
                        break
                    else:
                        time.sleep(0.5)
                        print("\n",zırhsec,"bir seçenek değil.\n")            
                        time.sleep(0.5)
            elif marketsecenekler=="silah" or marketsecenekler=="Silah":
                print("\n\n███████████████")
                print("███████░███████")
                print("██████░░░██████")
                print("██████░░░██████")
                print("██████░░░██████")
                print("█████░░░░░█████")
                print("█████░░░░░█████")
                print("██░░░░░░░░░░░██")
                print("██████░░░██████")
                print("██████░░░██████")
                print("███████████████\n")
                print("\nSilahlar : \n\n")
                time.sleep(0.5)
                print("Taş kılıç :\n\n\t30 kuvvet \n\t10 para\n\n")
                time.sleep(0.5)
                print("Altın kılıç :\n\n\t70 kuvvet \n\t70 para\n\n")
                time.sleep(0.5)
                print("Demir kılıç :\n\n\t150 kuvvet \n\t100 para\n\n")
                time.sleep(0.5)
                print("Elmas kılıç :\n\n\t350 kuvvet \n\t300 para\n\n")
                time.sleep(0.5)
                while True:
                    print("Taş kılıç | Altın kılıç | Demir kılıç | Elmas kılıç | Geri\n\n")
                    silahsec = input("Yukarıdaki silahlardan birini seçiniz   >    ")
                    if silahsec=="taş kılıç" or silahsec=="Taş kılıç" or silahsec=="Taş Kılıç" or silahsec=="taş Kılıç" or silahsec=="taş" or silahsec=="Taş":
                        if oyuncu.para>=10:
                            oyuncu.kuvvet-oyuncu.kuvvet
                            oyuncu.kuvvet = oyuncu.kuvvet + 30
                            oyuncu.para = oyuncu.para - 10
                            time.sleep(0.5)
                            print("\nKılıç başarıyla alınmıştır!","\n")
                            time.sleep(0.5)
                            print("Kalan para : ",oyuncu.para,"\n")
                            time.sleep(0.5)
                            print("Kuvvet : ",oyuncu.kuvvet,"\n")
                            time.sleep(0.5)
                            break
                        else:
                            time.sleep(0.5)
                            print("\nBu kılıçı alamazsınız . Yeterli paranız yok !\n")
                            time.sleep(0.5)
                    elif silahsec=="altın kılıç" or silahsec=="Altın kılıç" or silahsec=="Altın Kılıç" or silahsec=="altın Kılıç" or silahsec=="altın" or silahsec=="Altın":
                        if oyuncu.para>=70:    
                            oyuncu.kuvvet-oyuncu.kuvvet
                            oyuncu.kuvvet = oyuncu.kuvvet + 70
                            oyuncu.para = oyuncu.para - 70
                            time.sleep(0.5)
                            print("\nKılıç başarıyla alınmıştır!","\n")
                            time.sleep(0.5)
                            print("Kalan para : ",oyuncu.para,"\n")
                            time.sleep(0.5)
                            print("Kuvvet : ",oyuncu.kuvvet,"\n")
                            time.sleep(0.5)
                            break
                        else:
                            time.sleep(0.5)
                            print("\nBu kılıçı alamazsınız . Yeterli paranız yok !\n")
                            time.sleep(0.5)
                    elif silahsec=="demir kılıç" or silahsec=="Demir kılıç" or silahsec=="Demir Kılıç" or silahsec=="demir Kılıç" or silahsec=="demir" or silahsec=="Demir":
                        if oyuncu.para>=100:    
                            oyuncu.kuvvet-oyuncu.kuvvet
                            oyuncu.kuvvet = oyuncu.kuvvet + 150
                            oyuncu.para = oyuncu.para - 100
                            time.sleep(0.5)
                            print("\nKılıç başarıyla alınmıştır!","\n")
                            time.sleep(0.5)
                            print("Kalan para : ",oyuncu.para,"\n")
                            time.sleep(0.5)
                            print("Kuvvet : ",oyuncu.kuvvet,"\n")
                            time.sleep(0.5)
                            break
                        else:
                            time.sleep(0.5)
                            print("\nBu kılıçı alamazsınız . Yeterli paranız yok !\n")
                            time.sleep(0.5)
                    elif silahsec=="elmas kılıç" or silahsec=="Elmas kılıç" or silahsec=="Elmas Kılıç" or silahsec=="elmas Kılıç" or silahsec=="elmas" or silahsec=="Elmas":
                        if oyuncu.para>=300:  
                            oyuncu.kuvvet-oyuncu.kuvvet 
                            oyuncu.kuvvet = oyuncu.kuvvet + 350
                            oyuncu.para = oyuncu.para - 300
                            time.sleep(0.5)
                            print("\nKılıç başarıyla alınmıştır!","\n")
                            time.sleep(0.5)
                            print("Kalan para : ",oyuncu.para,"\n")
                            time.sleep(0.5)
                            print("Kuvvet : ",oyuncu.kuvvet,"\n")
                            time.sleep(0.5)
                            break
                        else:
                            time.sleep(0.5)
                            print("\nBu kılıçı alamazsınız . Yeterli paranız yok !\n")
                            time.sleep(0.5)
                    elif silahsec=="geri" or silahsec=="Geri":
                        break
                    else:
                        time.sleep(0.5)
                        print("\n",silahsec,"bir seçenek değil.\n")            
                        time.sleep(0.5)
            elif marketsecenekler=="İksirler" or marketsecenekler=="iksirler" or marketsecenekler=="iksir" or marketsecenekler=="İksir":
                print("\n\n███████████████")
                print("█████░░░░░█████")
                print("██████░█░██████")
                print("████░░░█░░░████")
                print("██░░███████░░██")
                print("██░░███████░░██")
                print("██░░███████░░██")
                print("████░░░░░░░████")
                print("███████████████")
                print("\n\nİksirler : \n\n")
                time.sleep(0.5)
                print("Sağlık iksiri: \n\n\tSağlığını doldurur.\n\t50 para\n\n")
                time.sleep(0.5)
                print("Enerji iksiri : \n\n\tEnerjinizi doldurur.\n\t40 para\n\n")
                time.sleep(0.5)
                while True:
                    print("Sağlık iksiri | Enerji iksiri | Geri\n\n")
                    time.sleep(0.5)
                    iksirsec = input("Yukarıdaki iksirlerden birini seçiniz   >    \n\n")
                    if iksirsec=="Sağlık iksiri" or iksirsec=="sağlık iksiri" or iksirsec=="Sağlık" or iksirsec=="sağlık":
                        if oyuncu.para >= 50 :
                            oyuncu.para = oyuncu.para - 50
                            oyuncu.saglik = oyuncu.saglik - oyuncu.saglik + 100
                            print("Sağlık iksiri başarıyla alınmıştır")
                            print("\n\nKalan para : ",oyuncu.para,"\n")
                        else:
                            time.sleep(0.5)
                            print("\n\nBu iksiri alamazsınız . Yeterince paranız yok !\n\n")
                            time.sleep(0.5)
                    elif iksirsec=="Enerji iksiri" or iksirsec=="enerji iksiri" or iksirsec=="Enerji" or iksirsec=="enerji":
                        if oyuncu.para >= 40 :
                            oyuncu.para = oyuncu.para - 40
                            oyuncu.enerji = oyuncu.enerji - oyuncu.enerji + 100
                            print("Enerji iksiri başarıyla alınmıştır")
                            print("\n\nKalan para : ",oyuncu.para,"\n")
                        else:
                            time.sleep(0.5)
                            print("\n\nBu iksiri alamazsınız . Yeterince paranız yok !\n\n")
                            time.sleep(0.5)
                    elif iksirsec=="Geri" or iksirsec=="geri":
                        break
                    else:
                        print(iksirsec,"bir seçenek değil.")
            elif marketsecenekler=="geri" or marketsecenekler=="Geri":
                    baslangıc2()
            else:
                    print("\n",marketsecenekler,"bir seçenek değil.")
    def savas(self):
        while True:
            print("\n\nMağara | Arena | Geri\n\n")
            savaşseç = input("Yukarıdaki savaş türlerinden birini giriniz   >    \n\n") 
            if savaşseç=="Mağara" or savaşseç=="mağara":
                print("\n\nMağaraya giriliyor...")
                time.sleep(3)
                while True:
                    print("\n\n\nHangi tür düşmanlarla savaşmak istiyorsun ? ")
                    print("\n\nGoblin | Dev örümcek | Dev | Geri\n\n")
                    mağaradüşmanseç = input(">")
                    if mağaradüşmanseç=="Goblin" or mağaradüşmanseç=="goblin":
                        print("\n\nGoblinlerin özellikleri : \n\n")
                        goblin.goster()
                        while True:
                            print("\nSavaşa girmek istediğine eminmisin ? \n\n")
                            savasgirmekdogrula = input(">")
                            if savasgirmekdogrula=="Evet" or savasgirmekdogrula=="evet":
                                print("\n\nSavaş başlıyor...\n")
                                time.sleep(2)
                                print("\nSavaşa her zaman oyuncu başlar.\n\n")
                                time.sleep(0.5)
                                goblin.saglik = goblin.saglik*goblin.miktar
                                while True:
                                    print("\nSaldır | Geri çekil\n")
                                    saldırıicisecenekler = input("\n>")
                                    if saldırıicisecenekler=="Saldır" or saldırıicisecenekler=="saldır":
                                        savasici.goblinsavaşiçi()
                                    elif saldırıicisecenekler=="geri çekil" or saldırıicisecenekler=="Geri çekil":
                                        goblin.saglik = goblin.saglik - goblin.saglik + 100
                                        baslangıc2()
                                    else:
                                        print("\n",saldırıicisecenekler,"bir seçenek değil.")
                            elif savasgirmekdogrula=="Hayır" or savasgirmekdogrula=="hayır":
                                break
                            else:
                                time.sleep(0.5)
                                print("\n",savasgirmekdogrula,"bir seçenek değil.")
                                time.sleep(0.5)
                    elif mağaradüşmanseç=="Dev örümcek" or mağaradüşmanseç=="dev örümcek" or mağaradüşmanseç=="örümcek" or mağaradüşmanseç=="Örümcek":
                        print("\n\nDev örümceklerin özellikleri : ")
                        devörümcek.goster()
                        while True:
                            print("\nSavaşa girmek istediğine eminmisin ? \n\n")
                            savasgirmekdogrula = input(">")
                            if savasgirmekdogrula=="Evet" or savasgirmekdogrula=="evet":
                                print("\n\nSavaş başlıyor...\n")
                                time.sleep(2)
                                print("\nSavaşa her zaman oyuncu başlar.\n\n")
                                time.sleep(0.5)
                                devörümcek.saglik = devörümcek.saglik*devörümcek.miktar
                                while True:
                                    print("\nSaldır | Geri çekil\n")
                                    saldırıicisecenekler = input("\n>")
                                    if saldırıicisecenekler=="Saldır" or saldırıicisecenekler=="saldır":
                                        savasici.devörümceksavaşiçi()
                                    elif saldırıicisecenekler=="geri çekil" or saldırıicisecenekler=="Geri çekil":
                                        devörümcek.saglik = devörümcek.saglik - devörümcek.saglik + 100
                                        baslangıc2()
                                    else:
                                        print("\n",saldırıicisecenekler,"bir seçenek değil.")
                            elif savasgirmekdogrula=="Hayır" or savasgirmekdogrula=="hayır":
                                break
                            else:
                                time.sleep(0.5)
                                print("\n",savasgirmekdogrula,"bir seçenek değil.")
                                time.sleep(0.5)
                    elif mağaradüşmanseç=="Dev" or mağaradüşmanseç=="dev":
                        print("\n\nDevlerin özellikleri : ")
                        dev.goster()
                        while True:
                            print("\nSavaşa girmek istediğine eminmisin ? \n\n")
                            savasgirmekdogrula = input(">")
                            if savasgirmekdogrula=="Evet" or savasgirmekdogrula=="evet":
                                print("\n\nSavaş başlıyor...\n")
                                time.sleep(2)
                                print("\nSavaşa her zaman oyuncu başlar.\n\n")
                                time.sleep(0.5)
                                dev.saglik = dev.saglik*dev.miktar
                                while True:
                                    print("\nSaldır | Geri çekil\n")
                                    saldırıicisecenekler = input("\n>")
                                    if saldırıicisecenekler=="Saldır" or saldırıicisecenekler=="saldır":
                                        savasici.devsavaşiçi()
                                    elif saldırıicisecenekler=="geri çekil" or saldırıicisecenekler=="Geri çekil":
                                        dev.saglik = dev.saglik - dev.saglik + 100
                                        baslangıc2()
                                    else:
                                        print("\n",saldırıicisecenekler,"bir seçenek değil.")
                            elif savasgirmekdogrula=="Hayır" or savasgirmekdogrula=="hayır":
                                break
                            else:
                                time.sleep(0.5)
                                print("\n",savasgirmekdogrula,"bir seçenek değil.")
                                time.sleep(0.5)
                    elif mağaradüşmanseç=="Geri" or mağaradüşmanseç=="geri":
                        print("\n\nMağaradan çıkılıyor...")
                        time.sleep(0.5)
                        oyun.savas()
                    else:
                        time.sleep(0.5)
                        print(mağaradüşmanseç,"bir seçenek değil.\n\n")
                        time.sleep(0.5)
            elif savaşseç=="Arena" or savaşseç=="arena":
                while True:    
                    print("\n\n\nHangi zorlukta düşmanlarla savaşmak istiyorsun ? ")
                    print("\n\nKolay | Orta | Zor | Geri\n\n")
                    savaszorluk = input(">")
                    if savaszorluk == "kolay" or savaszorluk=="Kolay":
                        print("\n\nDüşmanın özellikleri : ")
                        kolaydusman.goster()
                        while True:
                            print("\nSavaşa girmek istediğine eminmisin ? \n\n")
                            savasgirmekdogrula = input(">")
                            if savasgirmekdogrula=="Evet" or savasgirmekdogrula=="evet":
                                print("\n\nSavaş başlıyor...\n")
                                time.sleep(2)
                                print("\nSavaşa her zaman oyuncu başlar.\n\n")
                                time.sleep(0.5)
                                while True:
                                    print("\nSaldır | Geri çekil\n")
                                    saldırıicisecenekler = input("\n>")
                                    if saldırıicisecenekler=="Saldır" or saldırıicisecenekler=="saldır":
                                        savasici.kolaysavasici()
                                    elif saldırıicisecenekler=="geri çekil" or saldırıicisecenekler=="Geri çekil":
                                        kolaydusman.saglik = kolaydusman.saglik - kolaydusman.saglik + 100
                                        baslangıc2()
                                    else:
                                        print("\n",saldırıicisecenekler,"bir seçenek değil.")
                            elif savasgirmekdogrula=="Hayır" or savasgirmekdogrula=="hayır":
                                break
                            else:
                                time.sleep(0.5)
                                print("\n",savasgirmekdogrula,"bir seçenek değil.")
                                time.sleep(0.5)
                    elif savaszorluk=="Orta" or savaszorluk=="orta":
                        print("\n\nDüşmanın özellikleri : ")
                        ortadusman.goster()
                        while True:
                            print("\nSavaşa girmek istediğine eminmisin ? \n\n")
                            savasgirmekdogrula = input(">")
                            if savasgirmekdogrula=="Evet" or savasgirmekdogrula=="evet":
                                print("\n\nSavaş başlıyor...\n")
                                time.sleep(2)
                                print("\nSavaşa her zaman oyuncu başlar.\n\n")
                                time.sleep(0.5)
                                while True:
                                    print("\nSaldır | Geri çekil\n")
                                    saldırıicisecenekler = input("\n>")
                                    if saldırıicisecenekler=="Saldır" or saldırıicisecenekler=="saldır":
                                        savasici.ortasavasici()
                                    elif saldırıicisecenekler=="geri çekil" or saldırıicisecenekler=="Geri çekil":
                                        ortadusman.saglik = ortadusman.saglik - ortadusman.saglik + 100
                                        baslangıc2()
                                    else:
                                        print("\n",saldırıicisecenekler,"bir seçenek değil.")
                            elif savasgirmekdogrula=="Hayır" or savasgirmekdogrula=="hayır":
                                oyun.savas()
                            else:
                                time.sleep(0.5)
                                print("\n",savasgirmekdogrula,"bir seçenek değil.")
                                time.sleep(0.5)
                    elif savaszorluk=="Zor" or savaszorluk=="zor":
                        print("\n\nDüşmanın özellikleri : ")
                        zordusman.goster()
                        while True:
                            print("\nSavaşa girmek istediğine eminmisin ? \n\n")
                            savasgirmekdogrula = input(">")
                            if savasgirmekdogrula=="Evet" or savasgirmekdogrula=="evet":
                                print("\n\nSavaş başlıyor...\n")
                                time.sleep(2)
                                print("\nSavaşa her zaman oyuncu başlar.\n\n")
                                time.sleep(0.5)
                                while True:
                                    print("\nSaldır | Geri çekil\n")
                                    saldırıicisecenekler = input("\n>")
                                    if saldırıicisecenekler=="Saldır" or saldırıicisecenekler=="saldır":
                                        savasici.zorsavasici()
                                    elif saldırıicisecenekler=="geri çekil" or saldırıicisecenekler=="Geri çekil":
                                        zordusman.saglik = zordusman.saglik - zordusman.saglik + 100
                                        baslangıc2()
                                    else:
                                        print("\n",saldırıicisecenekler,"bir seçenek değil.")
                            elif savasgirmekdogrula=="Hayır" or savasgirmekdogrula=="hayır":
                                oyun.savas()
                            else:
                                time.sleep(0.5)
                                print("\n",savasgirmekdogrula,"bir seçenek değil.")
                                time.sleep(0.5)
                    elif savaszorluk=="Geri" or savaszorluk=="geri":
                        oyun.savas()
                    else:
                        time.sleep(0.5)
                        print("\n\n",savaszorluk,"bir seçenek değil.\n\n")
                        time.sleep(0.5)
            elif savaşseç=="Ordu" or savaşseç=="ordu" or savaşseç=="Ordu savaşları" or savaşseç=="ordu savaşları":
                pass
            elif savaşseç=="Geri" or savaşseç=="geri":
                baslangıc2()
            else:
                time.sleep(0.5)
                print("\n",savaşseç,"bir seçenek değil.")
                time.sleep(0.5)
    def bilgilendirme(self):
        print("\n\n=> OYUN SADECE KLAVYE İLE OYNANILIR , MOUSE KULLANILMAZ !!!\n\n")
        time.sleep(0.5)
        print("=> Mağarada Goblinlerle veya Dev örümceklerle savaşırsın her kazandığın savaş sonrası sayıları birer birer artar\n\n")
        time.sleep(0.5)
        print("=> Oyuna ilk başladığında Arena savaşlarında düşmanlarını yenemeyebilirsin onun için ilk başta mağaraya gitmen önerilir.\n")
        time.sleep(0.5)
        print("=> Düşmanı öldürürsen düşmanın parasının hepsini alırsın.\n\n")
        time.sleep(0.5)
        print("=> Savaş ortasında enerjin biterse otomatik geri çekilirsin.\n\n")
        time.sleep(0.5)
        print("=> Enerjin biterse marketten iksir alabilirsin.\n\n")
        time.sleep(0.5)
        print("=> Sağlığın azalırsa marketten sağlık iksiri alabilirsin.\n\n")
        time.sleep(0.5)
        print("=> Fabrika kurarak savaşa girmeden belli süre aralıklarında para kazanabilirsin.\n\n")
        time.sleep(0.5)
    def hile(self):
        while True:
            print("\n\nSağlık | Para | Enerji | Kuvvet | Dayanıklılık\n\n")
            hileseç = input("Yukarıdaki seçeneklerden birini seçiniz   >    ")
            if hileseç=="Sağlık" or hileseç=="sağlık":
                try:
                    hilemiktarı = int(input("\n\nMiktar   >    "))
                    oyuncu.saglik = oyuncu.saglik + hilemiktarı
                    print("\nHile yapılıyor...\n\n")
                    time.sleep(0.7)
                    print("\nSağlık : ",oyuncu.saglik,"\n")
                    continue
                except ValueError:
                    print("Lütfen bir sayı giriniz.")
            elif hileseç=="Para" or hileseç=="para":
                try:
                    hilemiktarı = int(input("\n\nMiktar   >    "))
                    oyuncu.para = oyuncu.para + hilemiktarı
                    print("\nHile yapılıyor...\n\n")
                    time.sleep(0.7)
                    print("\nPara : ",oyuncu.para,"\n")
                    continue
                except ValueError:
                    print("Lütfen bir sayı giriniz.")
            elif hileseç=="Enerji" or hileseç=="enerji":
                try:
                    hilemiktarı = int(input("\n\nMiktar   >    "))
                    oyuncu.enerji = oyuncu.enerji + hilemiktarı
                    print("\nHile yapılıyor...\n\n")
                    time.sleep(0.7)
                    print("\nEnerji : ",oyuncu.enerji,"\n")
                    continue
                except ValueError:
                    print("Lütfen bir sayı giriniz.")
            elif hileseç=="Kuvvet" or hileseç=="kuvvet":
                try:
                    hilemiktarı = int(input("\n\nMiktar   >    "))
                    oyuncu.kuvvet = oyuncu.kuvvet + hilemiktarı
                    print("\nHile yapılıyor...\n\n")
                    time.sleep(0.7)
                    print("\nKuvvet : ",oyuncu.kuvvet,"\n")
                    continue
                except ValueError:
                    print("Lütfen bir sayı giriniz.")
            elif hileseç=="Dayanıklılık" or hileseç=="dayanıklılık":
                try:
                    hilemiktarı = int(input("\n\nMiktar   >    "))
                    oyuncu.dayaniklilik = oyuncu.dayaniklilik + hilemiktarı
                    print("\nHile yapılıyor...\n\n")
                    time.sleep(0.7)
                    print("\nDayanıklılık : ",oyuncu.dayaniklilik,"\n")
                    continue
                except ValueError:
                    print("Lütfen bir sayı giriniz.")
            else:
                print(hileseç,"bir seçenek değil.\n")
                continue
oyun = Oyun()

def baslangıc2():
    while True:
        time.sleep(0.5)
        print("\n\nSavaş | Market |  Özelliklerim | Bilgilendirme | Hile |Kapat \n\n")
        time.sleep(0.5)
        islem_gir = input("Yukarıdaki işlemlerden birini giriniz   >    ")
        if islem_gir=="özelliklerim" or islem_gir=="Özelliklerim" or islem_gir=="özellikler" or islem_gir=="Özellikler":
            oyuncu.goster()
        elif islem_gir=="kapat" or islem_gir=="Kapat" :
            quit()
        elif islem_gir=="Market" or islem_gir=="market":
            oyun.market()
        elif islem_gir=="Fabrika" or islem_gir=="fabrika":
            fabrikalar.fabrikakur()
        elif islem_gir=="savaş" or islem_gir=="Savaş":
            oyun.savas()
        elif islem_gir=="Bilgilendirme" or islem_gir=="bilgilendirme":
            oyun.bilgilendirme()
        elif islem_gir=="Hile" or islem_gir=="hile":
            oyun.hile()
        else:
            print("\n\n",islem_gir,"bir seçenek değil\n\n")

baslangıc2()

time.sleep(100)
