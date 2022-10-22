try:
    with open("secim.txt","r") as dosya: #BURADA BULUNAN KOMUT DOSYAYI ACMAKTADIR ISI BITINCE OTOMATIK KAPATILMAKTADIR
        toplam_parti_sayisi=int(dosya.readline())
        toplam_milletvekili_kontenjani=[0]*toplam_parti_sayisi
        toplam_gecerli_oy_sayisi_listesi=[0]*toplam_parti_sayisi #BURADA BULUNAN LISTELER TURKİYE GENELİ İSTATİSTİKLERİ İCİNDİR
        toplam_oy_yuzdesi_listesi=[]
        toplam_mv_say_yuzdesi=[]
        sifir_mv_li_il_say=[0]*toplam_parti_sayisi
        while not dosya=="":
            milletvekili_sayisi_listesi=[0]*toplam_parti_sayisi
            il_plaka_kodu_listesi = []
            milletvekili_kontenjani_listesi = [] #BURADA BULUNAN LISTELER ISE HER BIL IL ICIN OLUSTURULMUSTUR VE DONGU DONDUKCE SIFIRLANMAKTADIR
            oy_sayilari_listesi = []
            oy_yuzdesi_listesi = []
            o_ilin_plaka_kodu=(dosya.readline())
            if o_ilin_plaka_kodu=="": #DOSYADA ELEMAN BITINCE WHİLE DONGUSUNDEN CIKMAMIZI SAGLAMAKTADIR
                break
            il_plaka_kodu_listesi.append(o_ilin_plaka_kodu)
            o_ilin_milletvekili_kontenjani=int(dosya.readline())
            milletvekili_kontenjani_listesi.append(o_ilin_milletvekili_kontenjani)

            for oy_pusulasi_sira in range(toplam_parti_sayisi): #HER ILDEKI OY SAYILARI SIRASIYLA BURADA HESAPLANMAKTADIR
                o_ilin_oy_sayilari=int(dosya.readline())
                oy_sayilari_listesi.append(int(o_ilin_oy_sayilari))
                toplam_gecerli_oy_sayisi_listesi[oy_pusulasi_sira]+=o_ilin_oy_sayilari #BU LISTE TUM ULKE ICIN GECERLIDIR

            for yuzde_hesaplama in oy_sayilari_listesi: #HER ILIN OY SAYILARININ YUZDESI BURADA HESAPLANMAKTADIR
                i=yuzde_hesaplama*100/sum(oy_sayilari_listesi)
                oy_yuzdesi_listesi.append(i)

            sahte_liste = oy_sayilari_listesi[:]#BURADAKI SAHTE LISTE ALTTAKI FOR DONGUSUNDEKI ISLEMLERI DAHA RAHAT YAPMAK ICIN ATANMISTIR
            for milletvekili_belirleme in range(o_ilin_milletvekili_kontenjani):
                en_yuksek_oy=max(sahte_liste)
                sirasi=sahte_liste.index(en_yuksek_oy)
                x=en_yuksek_oy//2
                sahte_liste[sirasi]=x
                milletvekili_sayisi_listesi[sirasi]+=1
                toplam_milletvekili_kontenjani[sirasi]+=1 #BURADAKİ LISTE TUM ILLER ICINDIR

            for v in range(toplam_parti_sayisi): #BURADAKI FOR DONGUSU 0 MV'LI IL SAYISINI BELIRLEMEK ICINDIR
                if milletvekili_sayisi_listesi[v]==0:
                    sifir_mv_li_il_say[v]+=1

            #BU SATIRDAKI KODLAR TEK BIR IL ICIN GECERLIDIR
            print("İl plaka kodu:", o_ilin_plaka_kodu)
            print("Milletvekili kontenjanı:", o_ilin_milletvekili_kontenjani)
            print("Gecerli oy sayisi:", sum(oy_sayilari_listesi))
            print("Pusula sira   Oy say   Oy Yuzde   MV Say")
            print("----------   -------   --------   --------")
            for oy_pusulasi_sira in range(toplam_parti_sayisi) :
                print(format(oy_pusulasi_sira+1, "6d"),end="")
                print(format(oy_sayilari_listesi[oy_pusulasi_sira], "12d"),end="     ")
                print("%",format(oy_yuzdesi_listesi[oy_pusulasi_sira],"5.2f"),end="     ")
                print(format(milletvekili_sayisi_listesi[oy_pusulasi_sira], "2d"))

        #ALTTAKI IKI FOR DONGUSU TUM ULKE ICIN GECERLIDIR
        for toplam_yuzde_hesaplama in toplam_gecerli_oy_sayisi_listesi:
            b = toplam_yuzde_hesaplama * 100 / sum(toplam_gecerli_oy_sayisi_listesi)
            toplam_oy_yuzdesi_listesi.append(b)
        for toplam_mv_say_yuzdesi_hesaplama in toplam_milletvekili_kontenjani:
            c = toplam_mv_say_yuzdesi_hesaplama * 100 / sum(toplam_milletvekili_kontenjani)
            toplam_mv_say_yuzdesi.append(c)

    #BURADAN ITIBAREN OLAN KODLAR TUM TURKIYE ICIN GECERLIDIR
    print("Turkiye geneli")
    print("Milletvekili kontenjani:",sum(toplam_milletvekili_kontenjani))
    print("Gecerli oy sayisi:",sum(toplam_gecerli_oy_sayisi_listesi))
    print("Pusula sira   Oy say   Oy Yuzde   MV Say   MV Yuzde  0 MV Il Say")
    print("----------   -------   --------   ------   -------   -----------")
    for oy_pusulasi_sira in range(toplam_parti_sayisi):
        print(format(oy_pusulasi_sira + 1, "6d"),end="")
        print(format(toplam_gecerli_oy_sayisi_listesi[oy_pusulasi_sira], "12d"),end="     ")
        print("%", format(toplam_oy_yuzdesi_listesi[oy_pusulasi_sira], "5.2f"),end="     ")
        print(format(toplam_milletvekili_kontenjani[oy_pusulasi_sira], "2d"),end="      ")
        print("%", format(toplam_mv_say_yuzdesi[oy_pusulasi_sira], "5.2f"),end="      ")
        print(format(sifir_mv_li_il_say[oy_pusulasi_sira], "2d"))

except: #EGER PROGRAMDA BIR HATA OLUSURSA BU KOMUT DEVREYE GIRMEKTEDIR RUNTIME HATASINI ENGELLER
    print("Bir hata olustu")











