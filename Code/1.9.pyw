#This project made by Keremkunduk
import os
from time import sleep as slp
from tkinter import *
import sys
#pencere = Tk()


kaynak = os.getcwd()
dosyalar = os.listdir(kaynak)
tipler = ['.docx', '.ico', '.jar', '.jpeg', '.jpg', '.mp4', '.pdf', '.png', '.zip', '.rar', '.exe']


def yap(tip, yeni_kaynak, kaynak, dosyalar):
        for d in dosyalar:
            dosya, uzanti = os.path.splitext(d)
            if uzanti == tip:
                try:
                    eski = kaynak + '/' + d
                    yeni = yeni_kaynak + '/' + d
                    os.rename(eski, yeni)
                except:
                    print(dosya + uzanti + ' Adlı Dosya Zaten Var!')



pencere = Tk()
pencere.geometry('300x200') #300x200
pencere.resizable(0, 0)
pencere.title('Desktop Cleaner')

#f = sys._MEIPASS + '\\desk.ico'
# f = 'desk.ico'

f = 'D:\Desktop Cleaner\desk.ico'
pencere.iconbitmap(f)
#pencere.iconwindow()
pencere.configure(bg = '#9B59B6' )#'#9B59B6')

def selected():
    dosyalar = os.listdir(kaynak)
    if 'Desktop Files' not in os.listdir():
        os.mkdir('Desktop Files')
        os.chdir('Desktop Files')
        os.mkdir('exe')
        os.mkdir('ico')
        os.mkdir('jar')
        os.mkdir('jpeg')
        os.mkdir('jpg')
        os.mkdir('mp4')
        os.mkdir('pdf')
        os.mkdir('png')
        os.mkdir('rar')
        os.mkdir('zip')
        os.mkdir('docx')
        print('Klasörler Oluşturulduktan sonra düzenleme aşamasına geçilecek!')

    os.chdir(kaynak)

    tips = []

    if secim1.get()==1:
        tip = '.docx'
        tips = tips + [tip]
    if secim2.get()==1:
        tip = '.ico'
        tips = tips + [tip]
    if secim3.get()==1:
        tip = '.jar'
        tips = tips + [tip]
    if secim4.get()==1:
        tip = '.jpeg'
        tips = tips + [tip]
    if secim5.get()==1:
        tip = '.jpg'
        tips = tips + [tip]
    if secim6.get()==1:
        tip = '.mp4'
        tips = tips + [tip]
    if secim7.get()==1:
        tip = '.pdf'
        tips = tips + [tip]
    if secim8.get()==1:
        tip = '.png'
        tips = tips + [tip]
    if secim9.get()==1:
        tip = '.rar'
        tips = tips + [tip]
    if secimm.get()==1:
        tip = '.zip'
        tips = tips + [tip]
    if secim11.get()==1:
        tip = '.exe'
        tips = tips + [tip]

    for tip in tips:
        file_type = tip.replace('.', '')
        yeni_kaynak = kaynak + f'\Desktop Files\{file_type}'
        yap(tip, yeni_kaynak, kaynak, dosyalar)
    

    # tip = '.SADECERANDOMEZZZZ'
    # yeni_kaynak=kaynak + 'EZZZZZ'


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

fo = ('Bahnschrift', 8, 'bold')

onay1 = Checkbutton(text='Docx',variable=secim1, bg = '#9B59B6')
onay1.place(relx=0.0,rely=0.05)

onay1.configure(font=fo)

onay2 = Checkbutton(text='Ico',variable=secim2, bg = '#9B59B6')
onay2.place(relx=0.0,rely=0.15)

onay2.configure(font=fo)

onay3 = Checkbutton(text='Jar',variable=secim3, bg = '#9B59B6')
onay3.place(relx=0.0,rely=0.25)

onay3.configure(font=fo)

onay4 = Checkbutton(text='Jpeg',variable=secim4, bg = '#9B59B6')
onay4.place(relx=0.0,rely=0.35)

onay4.configure(font=fo)

onay5 = Checkbutton(text='Jpg',variable=secim5, bg = '#9B59B6')
onay5.place(relx=0.0,rely=0.45)

onay5.configure(font=fo)

onay6 = Checkbutton(text='mp4',variable=secim6, bg = '#9B59B6')
onay6.place(relx=0.0,rely=0.55)

onay6.configure(font=fo)

onay7 = Checkbutton(text='pdf',variable=secim7, bg = '#9B59B6')
onay7.place(relx=0.0,rely=0.65)

onay7.configure(font=fo)

onay8 = Checkbutton(text='png',variable=secim8, bg = '#9B59B6')
onay8.place(relx=0.0,rely=0.75)

onay8.configure(font=fo)

onay9 = Checkbutton(text='rar',variable=secim9, bg = '#9B59B6')
onay9.place(relx=0.0,rely=0.85)

onay9.configure(font=fo)

onay10 = Checkbutton(text='zip',variable=secimm, bg = '#9B59B6')
onay10.place(relx=0.8,rely=0.1)

onay10.configure(font=fo)

onay11 = Checkbutton(text='exe',variable=secim11, bg = '#9B59B6')
onay11.place(relx=0.8,rely=0.2)

onay11.configure(font=fo)

def all():
    dosyalar = os.listdir(kaynak)
    if 'Desktop Files' not in os.listdir():
        os.mkdir('Desktop Files')
        os.chdir('Desktop Files')
        os.mkdir('exe')
        os.mkdir('ico')
        os.mkdir('jar')
        os.mkdir('jpeg')
        os.mkdir('jpg')
        os.mkdir('mp4')
        os.mkdir('pdf')
        os.mkdir('png')
        os.mkdir('rar')
        os.mkdir('zip')
        os.mkdir('docx')
        print('Klasörler Oluşturulduktan sonra düzenleme aşamasına geçilecek!')
        #slp(1.5)

    os.chdir(kaynak)

    #tipler =

    for tip in tipler:
        file_type = tip.replace('.', '')
        yeni_kaynak = kaynak + f'\Desktop Files\{file_type}'
        yap(tip, yeni_kaynak, kaynak, dosyalar)
        
    

def save():
    dosyalar = os.listdir(kaynak)
    if 'Desktop Files' not in os.listdir():
        os.mkdir('Desktop Files')
        os.chdir('Desktop Files')
        os.mkdir('exe')
        os.mkdir('ico')
        os.mkdir('jar')
        os.mkdir('jpeg')
        os.mkdir('jpg')
        os.mkdir('mp4')
        os.mkdir('pdf')
        os.mkdir('png')
        os.mkdir('rar')
        os.mkdir('zip')
        os.mkdir('docx')
        print('Klasörler Oluşturulduktan sonra düzenleme aşamasına geçilecek!')

    os.chdir(kaynak)

    #tipler =

    for tip in tipler:
        file_type = tip.replace('.', '')
        yeni_kaynak = kaynak + f'\Desktop Files\{file_type}'
        yap(tip, yeni_kaynak, kaynak, dosyalar)
    if 'quickload' in dosyalar: #'hızlıyükledim.düzen' gözyaşım pıt
        os.rename('quickload', 'quick.txt')
        asa = open('quick.txt', 'r')
        oku = asa.read()
        asa.close()
        if 'docx' in oku:
            tip = '.docx'
            yeni_kaynak=kaynak + '\Desktop Files\docx'
            yap(tip, yeni_kaynak, kaynak, dosyalar)

        if 'ico' in oku:
            tip = '.ico'
            yeni_kaynak=yeni_kaynak=kaynak + '\Desktop Files\ico'
            yap(tip, yeni_kaynak, kaynak, dosyalar)

        if 'jar' in oku:
            tip = '.jar'
            yeni_kaynak=yeni_kaynak=kaynak + '\Desktop Files\jar'
            yap(tip, yeni_kaynak, kaynak, dosyalar)

        if 'jpeg' in oku:
            tip = '.jpeg'
            yeni_kaynak=yeni_kaynak=kaynak + '\Desktop Files\jpeg'
            yap(tip, yeni_kaynak, kaynak, dosyalar)

        if 'jpg' in oku:
            tip = '.jpg'
            yeni_kaynak=yeni_kaynak=kaynak + '\Desktop Files\jpg'
            yap(tip, yeni_kaynak, kaynak, dosyalar)

        if 'mp4' in oku:
            tip = '.mp4'
            yeni_kaynak=yeni_kaynak=kaynak + '\Desktop Files\mp4'
            yap(tip, yeni_kaynak, kaynak, dosyalar)

        if 'pdf' in oku:
            tip = '.pdf'
            yeni_kaynak=yeni_kaynak=kaynak + '\Desktop Files\pdf'
            yap(tip, yeni_kaynak, kaynak, dosyalar)

        if 'png' in oku:
            tip = '.png'
            yeni_kaynak=yeni_kaynak=kaynak + '\Desktop Files\png'
            yap(tip, yeni_kaynak, kaynak, dosyalar)

        if 'zip' in oku:
            tip = '.zip'
            yeni_kaynak=yeni_kaynak=kaynak + '\Desktop Files\zip'
            yap(tip, yeni_kaynak, kaynak, dosyalar)

        if 'rar' in oku:
            pisr = 'rar'
            pis = '\\\\\\'
            pis = pis[0:1]
            tip = '.rar'
            yeni_kaynak=yeni_kaynak=kaynak + '\Desktop Files' + pis + pisr
            yap(tip, yeni_kaynak, kaynak, dosyalar)
            
        if 'exe' in oku:
            tip = '.exe'
            yeni_kaynak=yeni_kaynak=kaynak + '\Desktop Files\exe'
            yap(tip, yeni_kaynak, kaynak, dosyalar)

        os.rename('quick.txt', 'quickload')
    if 'quickload' not in dosyalar:     
        asa = open('quick.txt', 'a')
        asa.close()
        asa = open('quick.txt', 'w')
        asa.write('')
        asa.close()
        if secim1.get()==1:
            asa = open('quick.txt', 'a')
            asa.write('\ndocx')
            asa.close()
        if secim2.get()==1:
            asa = open('quick.txt', 'a')
            asa.write('\nico')
            asa.close()
        if  secim3.get()==1:
            asa = open('quick.txt', 'a')
            asa.write('\njar')
            asa.close()
        if  secim4.get()==1:
            asa = open('quick.txt', 'a')
            asa.write('\njpeg')
            asa.close()
        if secim5.get()==1:
            asa = open('quick.txt', 'a')
            asa.write('\njpg')
            asa.close()
        if secim6.get()==1:
            asa = open('quick.txt', 'a')
            asa.write('\nmp4')
            asa.close()
        if secim7.get()==1:
            asa = open('quick.txt', 'a')
            asa.write('\npdf')
            asa.close()
        if secim8.get()==1:
            asa = open('quick.txt', 'a')
            asa.write('\npng')
            asa.close()
        if secim9.get()==1:
            asa = open('quick.txt', 'a')
            asa.write('\nrar')
            asa.close()
        if secimm.get()==1:
            asa = open('quick.txt', 'a')
            asa.write('\nzip')
            asa.close()
        if secim11.get()==1:
            asa = open('quick.txt', 'a')
            asa.write('\nexe')
            asa.close()
        os.rename('quick.txt', 'quickload')



buton1 = Button(text='SELECTED FILES',command=selected, bg = '#00a8ff', activebackground = '#00a8ff')#3498db')#'#ff6600')
buton1.place(relx=0.34,rely=0.1,relheight=0.2,relwidth=0.4)

buton1.configure(font=fo)

buton2 = Button(text='ALL',command=all, bg = '#C21807', activebackground = '#C21807') #'#ff4d4d') #c23616
buton2.place(relx=0.34,rely=0.35,relheight=0.2,relwidth=0.4)

buton2.configure(font=fo)

buton3 = Button(text='SAVE   |  LOAD',command=save, bg = '#f1c40f', activebackground = '#f1c40f')
buton3.place(relx=0.34,rely=0.60,relheight=0.2,relwidth=0.4)

buton3.configure(font=fo)

labell = Label(text = 'Made By: Keremkunduk', bg = '#9B59B6')



labell.configure(font=fo)
labell.place(relx=0.29,rely=0.83,relheight=0.2,relwidth=0.5)

mainloop()



