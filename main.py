import random

print("merhaba zar atma oyununa hoş geldiniz!\n")
feyzamin=1
chaosmax=6
while True:
    deger=int(input("lütfen 1-6 aralığında değer giriniz (çıkmak için 9'a basın):"))
    if deger==9:
        break
    elif 1<=deger<=6:
        x=random.randint(feyzamin,chaosmax)
        if x==deger:
            print("tebrikler kazandınız!")
        else:
            print("kazanamadınız! bilgisayarın tahmin ettiği değer :",x)
    else:
            print("eksik ya da hatalı tuşlama yaptınız!")

