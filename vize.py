from tkinter import *
from tkinter import messagebox as tkMessageBox
import sqlite3

def EKLE():
    Lb1.insert(END, inputno.get() + ' ' +  inputisim.get() + ' ' + inputsoy.get())
    baglanti.execute("INSERT INTO Ogrenciler VALUES(?,?,?)",
                     [inputno.get(), inputisim.get(), inputsoy.get()])
    baglanti.commit()

def SİL():
    if tkMessageBox.askyesno("UYARI", "Seçili Kayıtları silmek istediğinize emin misiniz?"):
        for i in range(Lb1.size(), 0,-1):
            if Lb1.select_includes(i):
                baglanti.execute("DELETE FROM Ogrenciler WHERE OgrNo=? AND Ad=? AND Soyad=?",
                                 Lb1.get(i).split(' '))
                baglanti.commit()
                Lb1.delete(i)



pen = Tk()
pen.geometry("878x380")

frame = Frame(pen, bg="#dddddd", bd=5, relief=RIDGE)
frame.pack(side=LEFT, fill=Y)

yazi1=Label(frame, text="ÖĞRENCİLER",font="Calibri 20",height=1,bg="#dddddd",anchor=CENTER)
yazi1.grid(row=0,column=1)


yazino=Label(frame,text="ÖğrNo : ",font="Calibri",anchor=E,width=7,bg="#dddddd")
yazino.grid(row=1, column=0)
inputno = Entry(frame, font="Calibri")
inputno.grid(row=1, column=1)

yaziisim=Label(frame,text="Adı : ",font="Calibri",anchor=E,width=7,bg="#dddddd")
yaziisim.grid(row=2, column=0)
inputisim=Entry(frame, font="Calibri")
inputisim.grid(row=2,column=1)

yazisoy=Label(frame,text="Soyadı : ",font="Calibri",anchor=E,width=7,bg="#dddddd")
yazisoy.grid(row=3, column=0)
inputsoy=Entry(frame, font="Calibri")
inputsoy.grid(row=3,column=1)


eklemebutonu=Button(frame,font="Calibri",text="EKLE",command=EKLE)
eklemebutonu.grid(row=4,column=1)


Lb1=Listbox(frame,width=25,height=7 ,font="Calibri",selectmode="extended",exportselection=0)
Lb1.grid(row=6,column=1)


silmebutonu = Button(frame, text="Seçili olanları sil", font="Calibri",command=SİL)
silmebutonu.grid(row=8, column=1)

baglanti = sqlite3.connect("data.db")
baglanti.execute("CREATE TABLE IF NOT EXISTS Ogrenciler (ÖğrNo, Ad, Soyad)")


for kayıt in baglanti.execute("SELECT * FROM Ogrenciler"):
    Lb1.insert(END, kayıt[0] + ' ' + kayıt[1] + ' ' + kayıt[2])



def DERSEKLE():
    Lb2.insert(END, inputdersisim.get() + ' ' +  inputdersno.get())
    baglanti.execute("INSERT INTO Dersler VALUES(?,?)",
                     [inputdersisim.get(), inputdersno.get()])
    baglanti.commit()


def DERSSİL():
    if tkMessageBox.askyesno("UYARI", "Seçili Kayıtları silmek istediğinize emin misiniz?"):
        for i in range(Lb2.size(), 0,-1 ):
            if Lb2.select_includes(i):
                DersKodu = Lb2.get(i).split(' ')[0]
                baglanti.execute("DELETE FROM Dersler WHERE DersKodu='" + DersKodu + "'")
                baglanti.commit()
                Lb2.delete(i)


frame2 = Frame(pen, bg="#dddddd", bd=5, relief=RIDGE)
frame2.pack(side=LEFT, fill=Y)

yazi2=Label(frame2, text="DERSLER",font="Calibri 20",height=1,bg="#dddddd",anchor=CENTER)
yazi2.grid(row=0,column=1)


yazidersno=Label(frame2,text="Ders Kodu : ",font="Calibri",anchor=E,width=10,bg="#dddddd")
yazidersno.grid(row=1, column=0)
inputdersno = Entry(frame2, font="Calibri")
inputdersno.grid(row=1, column=1)

yazidersisim=Label(frame2,text="Ders Adı : ",font="Calibri",anchor=E,width=10,bg="#dddddd")
yazidersisim.grid(row=2, column=0)
inputdersisim=Entry(frame2, font="Calibri")
inputdersisim.grid(row=2,column=1)


eklemebutonu2=Button(frame2,font="Calibri",text="EKLE",command=DERSEKLE)
eklemebutonu2.grid(row=4,column=1)


Lb2=Listbox(frame2,width=25,height=7 ,font="Calibri",selectmode="extended",exportselection=0)
Lb2.grid(row=6,column=1)


silmebutonu = Button(frame2, text="Seçili olanları sil", font="Calibri",command=DERSSİL)
silmebutonu.grid(row=8, column=1)

baglanti = sqlite3.connect("data.db")
baglanti.execute("CREATE TABLE IF NOT EXISTS Dersler (DersKodu, DersAdı)")


for kayıt2 in baglanti.execute("SELECT * FROM Dersler"):
    Lb2.insert(END, kayıt2[0] + ' ' + kayıt2[1])








def NOTEKLE():
    Lb3.insert(END, [Lb1.get(ACTIVE).split(' ')[0], Lb2.get(ACTIVE).split(' ')[0], inputvize.get(),
                          inputfinal.get()])
    baglanti.execute("INSERT INTO Notlar VALUES(?,?,?,?)",
                     [Lb1.get(ACTIVE).split(' ')[0], Lb2.get(ACTIVE).split(' ')[0], inputvize.get(),
                      inputfinal.get()])
    baglanti.commit()


def NOTSİL():
    if tkMessageBox.askyesno("UYARI", "Seçili Kayıtları silmek istediğinize emin misiniz?"):
        for i in range(Lb3.size(), 0,-1 ):
            if Lb3.select_includes(i):
                if type(Lb3.get(i))==tuple:
                    b=' '.join(Lb3.get(i))
                    print(b)
                    ogrenciNo = b.split(' ')[0]
                    dersKod = b.split(' ')[1]
                    baglanti.execute("DELETE FROM Notlar WHERE OgrNo=? AND DersKodu=?",
                                     [ogrenciNo, dersKod])
                    baglanti.commit()

                    Lb3.delete(i)

                else:
                    ogrenciNo = Lb3.get(i).split('  ')[0]
                    dersKod = Lb3.get(i).split('  ')[1]
                    baglanti.execute("DELETE FROM Notlar WHERE OgrNo=? AND DersKodu=?",
                                     [ogrenciNo, dersKod])
                    baglanti.commit()

                    Lb3.delete(i)



frame3 = Frame(pen, bg="#dddddd", bd=5, relief=RIDGE)
frame3.pack(side=LEFT, fill=Y)

yazi3=Label(frame3, text="NOTLAR",font="Calibri 20",height=1,bg="#dddddd",anchor=CENTER)
yazi3.grid(row=0,column=1)


yazivize=Label(frame3,text="Vize Notu : ",font="Calibri",anchor=E,width=10,bg="#dddddd")
yazivize.grid(row=1, column=0)
inputvize = Entry(frame3, font="Calibri")
inputvize.grid(row=1, column=1)

yazifinal=Label(frame3,text="Final Notu : ",font="Calibri",anchor=E,width=10,bg="#dddddd")
yazifinal.grid(row=2, column=0)
inputfinal=Entry(frame3, font="Calibri")
inputfinal.grid(row=2,column=1)


eklemebutonu3=Button(frame3,font="Calibri",text="EKLE",command=NOTEKLE)
eklemebutonu3.grid(row=4,column=1)


Lb3=Listbox(frame3,width=25,height=7 ,font="Calibri",selectmode="extended",exportselection=0)
Lb3.grid(row=6,column=1)


silmebutonu3 = Button(frame3, text="Seçili olanları sil", font="Calibri",command=NOTSİL)
silmebutonu3.grid(row=8, column=1)


baglanti = sqlite3.connect("data.db")
baglanti.execute("CREATE TABLE IF NOT EXISTS Notlar(Vize,Final)")

for kayıt in baglanti.execute("SELECT * FROM Notlar"):
    Lb3.insert(END, kayıt[0] + '  ' + kayıt[1] + '  ' + kayıt[2] + ' ' + kayıt[3] + ' ')




pen.mainloop()