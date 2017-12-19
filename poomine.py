# Faili alguses impordime kõik vajaminevad moodulid ja funktsioonid
import tkinter as tk
from random import randint
from testproj import teesõnadjatähed
from tkinter import PhotoImage
import winsound
from time import sleep

# Funktsioon, mis arvestab ekraani suurust ja paigutab loodava akna eraani keskele.
def ekraani_suurus(w, h):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    return ('%dx%d+%d+%d' % (w, h, x, y))

# Loome Tkinteri akna vajalike paramaatritega ja sinna sisse fraimi.
root = tk.Tk()
root.title("Poomismäng")
root.geometry(ekraani_suurus(1000, 700))
root.resizable(width="false", height="false")
frame = tk.Frame()
frame.pack(fill=tk.BOTH, expand=1)

# Defineerime kõik globaalsed muutujad, mida järjnevalt koodis kasutame
sõnadjatähed = teesõnadjatähed("eesti_keel.txt")
sõnad = sõnadjatähed[0]
tähed = sõnadjatähed[1]
arvamise_korrad = 0
raskusaste = ""
arvatud_tähed = ""
vihje = ""
sõna = ""
võit_kaotus = ""
pildid = []

# Loen hiljem kasutatavad pildid listi
for i in range(0,11):
    i = tk.PhotoImage(file="pildid/staadiumid/kriips%d.png" %(i))
    pildid.append(i)

# Selle koodilõigu peaks siit ära eemaldama!
#===============================================================================
# def a(event):
#     nupuvajutus("a")
# def b(event):
#     nupuvajutus("b")
# def c(event):
#     nupuvajutus("c")
# def d(event):
#     nupuvajutus("d")
# def e(event):
#     nupuvajutus("e")
# def f(event):
#     nupuvajutus("f")
# def g(event):
#     nupuvajutus("g")
# def h(event):
#     nupuvajutus("h")
# def i(event):
#     nupuvajutus("i")
# def j(event):
#     nupuvajutus("j")
# def k(event):
#     nupuvajutus("k")
# def l(event):
#     nupuvajutus("l")
# def m(event):
#     nupuvajutus("m")
# def n(event):
#     nupuvajutus("n")
# def o(event):
#     nupuvajutus("o")    
# def p(event):
#     nupuvajutus("p")
# def q(event):
#     nupuvajutus("q")
# def r(event):
#     nupuvajutus("r")
# def s(event):
#     nupuvajutus("s")
# def t(event):
#     nupuvajutus("t")
# def u(event):
#     nupuvajutus("u")
# def v(event):
#     nupuvajutus("v")
# def z(event):
#     nupuvajutus("z")
# def ä(event):
#     nupuvajutus("ä")
# def õ(event):
#     nupuvajutus("õ")
# def ö(event):
#     nupuvajutus("ö")
# def ü(event):
#     nupuvajutus("ü")
#     
# funktsioonid = {"a": a,
#                 "b": b,
#                 "c": c,
#                 "d": d,
#                 "e": e,
#                 "f": f,
#                 "g": g,
#                 "i": i,
#                 "j": j,
#                 "k": k,
#                 "l": l,
#                 "m": m,
#                 "n": n,
#                 "o": o,
#                 "p": p,
#                 "q": q,
#                 "r": r,
#                 "s": s,
#                 "t": t,
#                 "u": u,
#                 "v": v,
#                 "z": z,
#                 "ä": ä,
#                 "õ": õ,
#                 "ö":ö,
#                 "ü":ü}
#===============================================================================


# Funktsioon, milles määratakse sõna, mida mängus arvama hakatakse ja sellele sõnale vastav vihje, kus teatud arv tähti
# on asendatud alakriipsuga
def sõna_valimine(raskusaste):
    if raskusaste == "kerge":
        pikkus = randint(4, 6)
    elif raskusaste == "keskmine":
        pikkus = randint(7, 10)
    elif raskusaste == "raske":
        pikkus = randint(10, len(sõnad)-1)

    sõna_asukoht = randint(0, len(sõnad[pikkus]) - 1)
    sõna = sõnad[pikkus][sõna_asukoht]
    vihje = ""
    lisatavad_tähed = [sõna[0], sõna[-1]]

    if raskusaste == "kerge":
        for element in range(len(sõna)):
            if element == 0 or element == len(sõna) - 1:
                vihje = vihje + sõna[element]
            elif sõna[element] in lisatavad_tähed:
                vihje = vihje + sõna[element]
            else:
                vihje = vihje + "_"

    elif raskusaste == "keskmine":
        for element in range(len(sõna)):
            if element == 0 or element == len(sõna) - 1:
                lisatavad_tähed.append(sõna[element])
                vihje = vihje + sõna[element]
            else:
                vihje = vihje + "_"

    else:
        vihje = "_" * len(sõna)

    return vihje, sõna

# Funktsioon, mis käivitatakse peale iga pakkumist, et uuendada vihjet ekraanil
def sõna_uuendamine(pakkumine, label_sona, label_pilt):
    global vihje
    global frame
    global arvamise_korrad
    global arvatud_tähed
    global võit_kaotus
    uuendatud_sona = ""

    # Suurendame pakkumiste korra arvu
    if pakkumine not in sõna and pakkumine not in arvatud_tähed:
        arvamise_korrad += 1
        label_pilt.config(image=pildid[arvamise_korrad])

    # Uuendame pakutud pakkumisi
    if pakkumine not in arvatud_tähed and pakkumine not in sõna:
        if len(arvatud_tähed) == 0:
            arvatud_tähed = arvatud_tähed + pakkumine
        else:
            arvatud_tähed = arvatud_tähed + ", " + pakkumine

    # Uuendame vihjet, mida ekraanile kuvada
    for element in range(len(vihje)):
        if pakkumine == sõna[element]:
            uuendatud_sona = uuendatud_sona + pakkumine
        else:
            uuendatud_sona = uuendatud_sona + vihje[element]
    vihje = uuendatud_sona
    label_sona.config(text=vihje + "\n" + "Arvatud: " + arvatud_tähed)


    # Järgnevad 2 if lauset kontrollivad, kas mäng on lõppend

    # Juhul, kui on arvatud 10 korda
    if arvamise_korrad == 10:
        arvamise_korrad = 0
        arvatud_tähed = ""
        võit_kaotus = "kaotus"
        top = tk.Toplevel()
        top.title("Kaotus!")
        top.geometry(ekraani_suurus(400, 200))
        msg = tk.Message(top, text="Kaotasite. Uuesti?", font=("arial", 30, "bold"), aspect=500)
        msg.pack()
        button = tk.Button(top, text="Lõpeta", font=("arial", 20, "bold"), command=root.destroy)
        button.pack()
        button2 = tk.Button(top, text="Uuesti", font=("arial", 20, "bold"), command=lambda: lõpustuuesti(top))
        button2.pack()


    # Juhul kui sõna on ära arvatud, loon lõpuakna
    if vihje == sõna:
        arvamise_korrad = 0
        arvatud_tähed = ""
        võit_kaotus = "võit"
        top = tk.Toplevel()
        top.title("Õnnitlused")
        top.geometry(ekraani_suurus(400, 200))
        msg = tk.Message(top, text="Õnnitlused", font=("arial", 30, "bold"), aspect=500)
        msg.pack()
        button = tk.Button(top, text="Lõpeta", font=("arial", 20, "bold"), command=root.destroy)
        button.pack()
        button2 = tk.Button(top, text="Uuesti", font=("arial", 20, "bold"), command=lambda: lõpustuuesti(top))
        button2.pack()

# see on mul pooleli
"""
def hävitajaasenda():
    global frame
    frame.destroy()

    frame = tk.Frame()
    frame.pack(fill=tk.BOTH, expand=1)
    muster = tk.PhotoImage(file="pildid/pealkiri.png")
    tk.Label(frame, image=muster, width=1000, height=700).pack(fill="both", expand=1, pady=0)
"""





# Funktsioon, mis laseb lõpust uuesti alustad ja kutsub välja esiekraani
def lõpustuuesti(aken):
    aken.destroy()
    esiekraan()
    

# Raskusastme valimise aken
def raskusastme_valimine(valitud):
    global frame
    frame.destroy()
    frame = tk.Frame()
    frame.pack(fill=tk.BOTH, expand=1)

    muster = tk.PhotoImage(file="pildid/taust.gif")
    Kerge = tk.PhotoImage(file="pildid/lihtne.gif")
    Keskmine = tk.PhotoImage(file="pildid/keskmine.gif")
    Raske = tk.PhotoImage(file="pildid/raske.gif")


    if valitud == "kerge":
        tk.Label(frame, image=Kerge, width=1000, height=700).pack(fill="both", expand=1)
        raskusaste = "kerge"
    elif valitud == "keskmine":
        tk.Label(frame, image=Keskmine, width=1000, height=700).pack(fill="both", expand=1)
        raskusaste = "keskmine"
    elif valitud == "raske":
        tk.Label(frame, image=Raske, width=1000, height=700).pack(fill="both", expand=1)
        raskusaste = "raske"
    else:
        tk.Label(frame, image=muster, width=1000, height=700).pack(fill="both", expand=1)


    tagasi_nupp = tk.Button(frame, command=esiekraan, text="tagasi")
    tagasi_nupp.config(font=("arial", 24), width = 100, height= 50, image=muster, compound="center", activebackground="red", bd = 10, relief="ridge")
    tagasi_nupp.place(x = 435, y = 600)


    kerge = tk.Button(frame, text="Kerge")
    kerge.config(font=("arial", 24), width=100, height=50, image=muster, compound="center",
                       activebackground="green", bd=10, command=lambda: raskusastme_valimine("kerge"))
    kerge.place(x=435, y=230)

    keskmine = tk.Button(frame, text="Keskmine")
    keskmine.config(font=("arial", 24), width=150, height=50, image=muster, compound="center",
                 activebackground="orange", bd=10, command=lambda: raskusastme_valimine("keskmine"))
    keskmine.place(x=410, y=320)

    raske = tk.Button(frame, text="Raske")
    raske.config(font=("arial", 24), width=100, height=50, image=muster, compound="center",
                 activebackground="red", bd=10, command=lambda: raskusastme_valimine("raske"))
    raske.place(x=435, y=410)

    mängima_nupp = tk.Button(frame, text="MÄNGIMA")
    mängima_nupp.config(font=("arial", 30, "bold"), command=lambda: põhiaken(valitud), width=200, height=100, image=muster, compound="center",
                        activebackground="red", bd=10)
    if valitud != 1:
        mängima_nupp.place(x=383, y=70)
    
    root.mainloop()

    
def põhiaken(raskus):
    # loon 3 eraldi frame, kuhu panna sõna, nupud ja poomispilt
    global frame
    frame.pack_forget()
    frame = tk.Frame(root)
    frame.config(bg="green")
    frame.pack(fill="both")
    taust_sonale = tk.PhotoImage(file="pildid/taust.png")
    võllapuu = tk.PhotoImage(file="pildid/staadiumid/kriips0.png")

    sõnajavihje = sõna_valimine(raskus)
    global sõna
    global vihje
    global arvatud_tähed

    sõna = sõnajavihje[1]
    vihje = sõnajavihje[0]

    tekstiraam=tk.Frame(frame,width = 1000,height=200)
    tekstiraam.config(bg="red")
    tekstiraam.pack(fill = "both", expand= 1)

    pildiraam = tk.Frame(frame,width = 300,height=500)
    pildiraam.config(bg="yellow")
    pildiraam.pack(side="right")
    
    sõnalabel =tk.Label(tekstiraam, image = taust_sonale, text = vihje + "\n" + "Arvatud: ", font=("Arial", 40, "bold"), compound = "center",
             width = 1000, height = 200)
    sõnalabel.pack(expand= 1)


    

    nupuraam = tk.Frame(frame,width = 700,height=500, bg="white")
    nupuraam.pack(side="left")

    pildi_label= tk.Label(pildiraam, image = võllapuu, width= 300, height= 500)
    pildi_label.pack(fill="both", expand= 1)


    nupupilt = tk.PhotoImage(file="pildid/sininenupp.png")
    nupupilt2 = tk.PhotoImage(file="pildid/sininenupp2.png")
    for i in range(6):
        tk.Button(nupuraam,image=nupupilt,width = 90,font=("arial", 40),height=90
                  ,text=str(tähed[i]),compound="c",command=lambda j=i:nupuvajutus(tähed[j],sõnalabel, pildi_label)).place(x=10+(115*i),y=0)
    for i in range(6,12):
        tk.Button(nupuraam,image=nupupilt,width = 90,font=("arial", 40),height=90
          ,text=str(tähed[i]),compound="c",command=lambda j=i:nupuvajutus(tähed[j],sõnalabel, pildi_label)).place(x=10+(115*(i-6)),y=110)
    for i in range(12,18):
        tk.Button(nupuraam,image=nupupilt,width = 90,font=("arial",40),height=90
          ,text=str(tähed[i]),compound="c",command=lambda j=i:nupuvajutus(tähed[j],sõnalabel, pildi_label)).place(x=10+(115*(i-12)),y=220)
    for i in range(18,24):
        tk.Button(nupuraam,image=nupupilt,width = 90,font=("arial", 40),height=90
        ,text=str(tähed[i]),compound="c",command=lambda j=i:nupuvajutus(tähed[j],sõnalabel, pildi_label)).place(x=10+(115*(i-18)),y=330)
    for i in range(24,27):
        tk.Button(nupuraam,image=nupupilt2,width=190,font=("arial", 40),height=35
        ,text=str(tähed[i]),compound="c",command=lambda j=i:nupuvajutus(tähed[j],sõnalabel, pildi_label)
        ).place(x=10+(235*(i-24)),y=440)
    tk.Button(nupuraam,image=nupupilt,width = 90,font=("arial", 40),height=90
                  ,text=str(tähed[i]),compound="c",command=lambda j=i:nupuvajutus(tähed[j],sõnalabel, pildi_label)).place(x=10+(115*i),y=0)
        
    root.mainloop()
    
#funktsioon, kui nuppu vajutatakse
def nupuvajutus(täht,label_sona, label_pilt):
    winsound.PlaySound('pildid/nupp.wav', winsound.SND_FILENAME)
    sõna_uuendamine(täht, label_sona, label_pilt)


def esiekraan():
    global frame
    frame.destroy()
    
    frame = tk.Frame()
    frame.pack(fill=tk.BOTH, expand=1)

    muster = tk.PhotoImage(file="pildid/pealkiri.png")
    peamine = tk.PhotoImage(file="pildid/peamine.png")

    pealkirja_frame = tk.Frame(frame)
    pealkirja_frame.config(width=1000, height=150)
    pealkirja_frame.pack(fill=tk.BOTH, expand=1)
    pealkirja_taust = tk.Label(pealkirja_frame, image=muster, width=1000, height=150, text="POO_ISMÄN_!",
                               compound="center", font="Times 50 bold", pady=0)
    pealkirja_taust.pack(expand=1, fill="both")

    Alumine_osa = tk.Frame(frame)
    Alumine_osa.config(width=1000, height=550)
    Alumine_osa.pack(fill="y", expand=1, side="left")
    tk.Label(Alumine_osa, image=peamine, width=1000, height=550).pack(fill="both", expand=1, pady=0)

    nupp_alusta = tk.Button(Alumine_osa, text="Alusta", font=("arial", 30), command=lambda :raskusastme_valimine(1))
    nupp_alusta.place(x=425, y=92)
    nupp_alusta.config(image=muster, activebackground="green", anchor="center", bd=10, height=60, width=120,
                       compound="center")

    nupp2 = tk.Button(Alumine_osa, text="Välju", font=("arial", 24), command=root.destroy, compound="center")
    nupp2.place(x=435, y=200)
    nupp2.config(image=muster, activebackground="red", anchor="center", bd=10, height=50, width=100)

    root.mainloop()

esiekraan()