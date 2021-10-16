#This project made by Keremkunduk
import os
from time import sleep as slp
from tkinter import *
#pencere = Tk()

kaynak=os.getcwd()
dosyalar = os.listdir(kaynak)
pencere = Tk()
pencere.geometry('300x200') #300x200
pencere.title('Düzen Uygulaması')
#pencere.iconwindow()
pencere.configure(bg = 'green')
def ekranaYaz():  
    try:
        gel = os.getcwd()
        os.mkdir("düzen")
        os.chdir("düzen")
        os.mkdir("lnk")
        os.mkdir("ico")
        os.mkdir("jar")
        os.mkdir("jpeg")
        os.mkdir("jpg")
        os.mkdir("mp4")
        os.mkdir("pdf")
        os.mkdir("png")
        os.mkdir("py")
        os.mkdir("rar")
        os.mkdir("zip")
        os.mkdir("docx")
        print("Klasörler Oluşturulduktan sonra düzenleme aşamasına geçilecek!")
        #(1.5)
        os.chdir(gel)                       #kaynakk=os.getcwd()
                                            #dosyalarr = os.listdir(kaynakk)
                                            #konumone = os.getcwd()
                                            #uzunluk = len(os.getcwd())
                                            #uzunluk = uzunluk - 5
                                            #konumtwo = konumone[:uzunluk]
                                            #os.chdir(konumtwo)
    except:
        print("Klasörler Oluşturulmuş, Düzenlenme Aşamasına Geçiliyor.")
        #slp(1.5)

    tip = ".SADECERANDOMEZZZZ"
    sayac = 0
    yeni_kaynak=kaynak + "EZZZZZ"

    def yap(sayac, tip, yeni_kaynak, kaynak):
            for d in dosyalar:
                dosya, uzanti = os.path.splitext(d)
                if uzanti == tip:
                    try:
                        eski = kaynak + "/" + d
                        yeni = yeni_kaynak + "/" + d
                        os.rename(eski,yeni)
                    except:
                        print("'" + dosya + uzanti + "'" + "Adlı Dosya Zaten Var!")

    if secim1.get()==1:
        tip = ".docx"
        sayac = 0
        yeni_kaynak=kaynak + "\düzen\docx"
        yap(sayac, tip, yeni_kaynak, kaynak)
    if secim2.get()==1:
        tip = ".ico"
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\ico"
        yap(sayac, tip, yeni_kaynak, kaynak)
    if secim3.get()==1:
        tip = ".jar"
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\jar"
        yap(sayac, tip, yeni_kaynak, kaynak)
    if secim4.get()==1:
        tip = ".jpeg"
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\jpeg"
        yap(sayac, tip, yeni_kaynak, kaynak)
    if secim5.get()==1:
        tip = ".jpg"
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\jpg"
        yap(sayac, tip, yeni_kaynak, kaynak)
    if secim6.get()==1:
        tip = ".mp4"
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\mp4"
        yap(sayac, tip, yeni_kaynak, kaynak)
    if secim7.get()==1:
        tip = ".pdf"
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\pdf"
        yap(sayac, tip, yeni_kaynak, kaynak)
    if secim8.get()==1:
        tip = ".png"
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\png"
        yap(sayac, tip, yeni_kaynak, kaynak)
    if secim9.get()==1:
        pisr = "rar"
        pis = "\\\\\\"
        pis = pis[0:1]
        tip = ".rar"
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen" + pis + pisr
        yap(sayac, tip, yeni_kaynak, kaynak)
    if secimm.get()==1:
        tip = ".zip"
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\zip"
        yap(sayac, tip, yeni_kaynak, kaynak)
    if secim11.get()==1:
        tip = ".lnk"
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\lnk"
        yap(sayac, tip, yeni_kaynak, kaynak)
secim1=IntVar()
secim1.set(0)

secim2=IntVar()
secim2.set(0)

secim3=IntVar()
secim3.set(0)

secim4=IntVar()
secim4.set(0)

secim5=IntVar()
secim5.set(0)

secim6=IntVar()
secim6.set(0)

secim7=IntVar()
secim7.set(0)

secim8=IntVar()
secim8.set(0)

secim9=IntVar()
secim9.set(0)

secimm=IntVar()
secimm.set(0)

secim11=IntVar()
secim11.set(0)

onay1 = Checkbutton(text="Docx",variable=secim1, bg = 'green')
onay1.place(relx=0.0,rely=0.1)

onay2 = Checkbutton(text="Ico",variable=secim2, bg = 'green')
onay2.place(relx=0.0,rely=0.2)

onay3 = Checkbutton(text="Jar",variable=secim3, bg = 'green')
onay3.place(relx=0.0,rely=0.3)

onay4 = Checkbutton(text="Jpeg",variable=secim4, bg = 'green')
onay4.place(relx=0.0,rely=0.4)

onay5 = Checkbutton(text="Jpg",variable=secim5, bg = 'green')
onay5.place(relx=0.0,rely=0.5)

onay6 = Checkbutton(text="mp4",variable=secim6, bg = 'green')
onay6.place(relx=0.0,rely=0.6)

onay7 = Checkbutton(text="pdf",variable=secim7, bg = 'green')
onay7.place(relx=0.0,rely=0.7)

onay8 = Checkbutton(text="png",variable=secim8, bg = 'green')
onay8.place(relx=0.0,rely=0.8)

onay9 = Checkbutton(text="rar",variable=secim9, bg = 'green')
onay9.place(relx=0.0,rely=0.9)

onay = Checkbutton(text="zip",variable=secimm, bg = 'green')
onay.place(relx=0.8,rely=0.1)

onayy = Checkbutton(text="lnk",variable=secim11, bg = 'green')
onayy.place(relx=0.8,rely=0.2)

def a():
    pass

def filtrele():
    try:
        kaynak=os.getcwd()
        os.mkdir("düzen")
        os.chdir("düzen")
        os.mkdir("lnk")
        os.mkdir("ico")
        os.mkdir("jar")
        os.mkdir("jpeg")
        os.mkdir("jpg")
        os.mkdir("mp4")
        os.mkdir("pdf")
        os.mkdir("png")
        os.mkdir("py")
        os.mkdir("rar")
        os.mkdir("zip")
        os.mkdir("docx")
        print("Klasörler Oluşturulduktan sonra düzenleme aşamasına geçilecek!")
        #slp(1.5)
        
        dosyalar = os.listdir(kaynak)
        os.chdir(kaynak)

        tip = ".docx"
        sayac=0
        yeni_kaynak=kaynak + "\düzen\docx"

        def yap(sayac, tip, yeni_kaynak, kaynak,):
            for d in dosyalar:

                dosya, uzanti=os.path.splitext(d)
                if ( uzanti == tip ):
                    try:
                        sayac+=1
                        eski=kaynak+"/"+d
                        yeni=yeni_kaynak+"/"+d
                        os.rename(eski,yeni)
                    except:
                        print("'" + dosya + uzanti + "'" + "Adlı Dosya Zaten Var!")
                    

        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".ico"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\ico"

        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".jar"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\jar"

        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".jpeg"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\jpeg"

        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".jpg"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\jpg"

        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".mp4"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\mp4"

        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".pdf"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\pdf"

        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".png"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\png"

        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".zip"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\zip"

        yap(sayac, tip, yeni_kaynak, kaynak)

        pisr = "rar"
        pis = "\\"
        pis = pis[0:1]
        tip = ".rar"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen" + pis + pisr

        yap(sayac, tip, yeni_kaynak, kaynak)
        
        tip = ".lnk"
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\lnk"
        yap(sayac, tip, yeni_kaynak, kaynak)
    except:
        print("Klasörler Oluşturulmuş, Düzenlenme Aşamasına Geçiliyor.")
        #slp(1.5)
        
        kaynak=os.getcwd()

        dosyalar = os.listdir(kaynak)

        tip = ".docx"
        sayac=0
        yeni_kaynak=kaynak + "\düzen\docx"

        def yap(sayac, tip, yeni_kaynak, kaynak,):
            for d in dosyalar:
                dosya, uzanti=os.path.splitext(d)
                if ( uzanti == tip ):
                    try:
                        sayac+=1
                        eski=kaynak+"/"+d
                        yeni=yeni_kaynak+"/"+d
                        os.rename(eski,yeni)
                    except:
                        print("'" + dosya + uzanti + "'" + "Adlı Dosya Zaten Var!")


        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".ico"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\ico"

        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".jar"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\jar"

        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".jpeg"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\jpeg"

        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".jpg"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\jpg"

        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".mp4"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\mp4"

        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".pdf"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\pdf"

        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".png"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\png"

        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".zip"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\zip"

        yap(sayac, tip, yeni_kaynak, kaynak)

        pisr = "rar"
        pis = "\\"
        pis = pis[0:1]
        tip = ".rar"
        sayac=0
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen" + pis + pisr
        
        yap(sayac, tip, yeni_kaynak, kaynak)

        tip = ".lnk"
        yeni_kaynak=yeni_kaynak=kaynak + "\düzen\lnk"
        
        yap(sayac, tip, yeni_kaynak, kaynak)
        
    

def ky():
    try:
        kaynak=os.getcwd()
        os.mkdir("düzen")
        os.chdir("düzen")
        os.mkdir("lnk")
        os.mkdir("ico")
        os.mkdir("jar")
        os.mkdir("jpeg")
        os.mkdir("jpg")
        os.mkdir("mp4")
        os.mkdir("pdf")
        os.mkdir("png")
        os.mkdir("py")
        os.mkdir("rar")
        os.mkdir("zip")
        os.mkdir("docx")
        os.chdir(kaynak)
    except:
        pass
    kaynak = os.getcwd()
    tip = ".SADECERANDOMEZZZZ"
    sayac = 0
    yeni_kaynak=kaynak + "EZZZZZ"
    def yap(sayac, tip, yeni_kaynak, kaynak):
            for d in dosyalar:
                dosya, uzanti=os.path.splitext(d)
                if ( uzanti == tip ):
                    try:
                        sayac+=1
                        eski=kaynak+"/"+d
                        yeni=yeni_kaynak+"/"+d
                        os.rename(eski,yeni)
                    except:
                        print("'" + dosya + uzanti + "'" + "Adlı Dosya Zaten Var!")
    kaynak = os.getcwd()
    dosyalar = os.listdir(kaynak)
    print(dosyalar)
    if "hızlıyükledim.düzen" in dosyalar:
        os.rename("hızlıyükledim.düzen", "quick.txt")
        asa = open("quick.txt", "r")
        oku = asa.read()
        asa.close()
        if "docx" in oku:
            tip = ".docx"
            sayac = 0
            yeni_kaynak=kaynak + "\düzen\docx"
            yap(sayac, tip, yeni_kaynak, kaynak)

        if "ico" in oku:
            tip = ".ico"
            yeni_kaynak=yeni_kaynak=kaynak + "\düzen\ico"
            yap(sayac, tip, yeni_kaynak, kaynak)

        if "jar" in oku:
            tip = ".jar"
            yeni_kaynak=yeni_kaynak=kaynak + "\düzen\jar"
            yap(sayac, tip, yeni_kaynak, kaynak)
        if "jpeg" in oku:
            tip = ".jpeg"
            yeni_kaynak=yeni_kaynak=kaynak + "\düzen\jpeg"
            yap(sayac, tip, yeni_kaynak, kaynak)
        if "jpg" in oku:
            tip = ".jpg"
            yeni_kaynak=yeni_kaynak=kaynak + "\düzen\jpg"
            yap(sayac, tip, yeni_kaynak, kaynak)
        if "mp4" in oku:
            tip = ".mp4"
            yeni_kaynak=yeni_kaynak=kaynak + "\düzen\mp4"
            yap(sayac, tip, yeni_kaynak, kaynak)
        if "pdf" in oku:
            tip = ".pdf"
            yeni_kaynak=yeni_kaynak=kaynak + "\düzen\pdf"
            yap(sayac, tip, yeni_kaynak, kaynak)
        if "png" in oku:
            tip = ".png"
            yeni_kaynak=yeni_kaynak=kaynak + "\düzen\png"
            yap(sayac, tip, yeni_kaynak, kaynak)
        if "zip" in oku:
            tip = ".zip"
            yeni_kaynak=yeni_kaynak=kaynak + "\düzen\zip"
            yap(sayac, tip, yeni_kaynak, kaynak)
        if "rar" in oku:
            pisr = "rar"
            pis = "\\\\\\"
            pis = pis[0:1]
            tip = ".rar"
            yeni_kaynak=yeni_kaynak=kaynak + "\düzen" + pis + pisr
            yap(sayac, tip, yeni_kaynak, kaynak)
        if "lnk" in oku:
            tip = ".lnk"
            yeni_kaynak=yeni_kaynak=kaynak + "\düzen\lnk"
            yap(sayac, tip, yeni_kaynak, kaynak)
        os.rename("quick.txt", "hızlıyükledim.düzen")
    if "hızlıyükledim.düzen" not in dosyalar:     
        asa = open("quick.txt", "a")
        asa.close()
        asa = open("quick.txt", "w")
        asa.write("")
        asa.close()
        if secim1.get()==1:
            asa = open("quick.txt", "a")
            asa.write("\ndocx")
            asa.close()
        if secim2.get()==1:
            asa = open("quick.txt", "a")
            asa.write("\nico")
            asa.close()
        if  secim3.get()==1:
            asa = open("quick.txt", "a")
            asa.write("\njar")
            asa.close()
        if  secim4.get()==1:
            asa = open("quick.txt", "a")
            asa.write("\njpeg")
            asa.close()
        if secim5.get()==1:
            asa = open("quick.txt", "a")
            asa.write("\njpg")
            asa.close()
        if secim6.get()==1:
            asa = open("quick.txt", "a")
            asa.write("\nmp4")
            asa.close()
        if secim7.get()==1:
            asa = open("quick.txt", "a")
            asa.write("\npdf")
            asa.close()
        if secim8.get()==1:
            asa = open("quick.txt", "a")
            asa.write("\npng")
            asa.close()
        if secim9.get()==1:
            asa = open("quick.txt", "a")
            asa.write("\nrar")
            asa.close()
        if secimm.get()==1:
            asa = open("quick.txt", "a")
            asa.write("\nzip")
            asa.close()
        if secim11.get()==1:
            asa = open("quick.txt", "a")
            asa.write("\nlnk")
            asa.close()
        os.rename("quick.txt", "hızlıyükledim.düzen")

buton1 = Button(text="BUNLARI DÜZENLE",command=ekranaYaz, bg = 'light blue')
buton1.place(relx=0.34,rely=0.1,relheight=0.2,relwidth=0.4)

buton2 = Button(text="HEPSİNİ DÜZENLE",command=filtrele, bg = 'red')
buton2.place(relx=0.34,rely=0.3,relheight=0.2,relwidth=0.4)

buton2 = Button(text="KAYDET / YÜKLE",command=ky, bg = 'yellow')
buton2.place(relx=0.34,rely=0.5,relheight=0.2,relwidth=0.4)

labell = Label(text = "Made By: Keremkunduk", bg = "green")
labell.place(relx=0.3,rely=0.7,relheight=0.2,relwidth=0.5)
#ekranaYaz()
mainloop()

#DOSYA İŞLEMLERİ KISMI -------------------------------------------------



