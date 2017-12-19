import tkinter as tk
from random import randint
from testproj import teesõnadjatähed
from tkinter import PhotoImage
import winsound



sõnadjatähed = teesõnadjatähed("eesti_keel.txt")
sõnad = sõnadjatähed[0]
tähed = sõnadjatähed[1]
arvamise_korrad = 0



def ekraani_suurus(w, h):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    return ('%dx%d+%d+%d' % (w, h, x, y))


def sõna_valimine(raskusaste):
    if raskusaste == "kerge":
        pikkus = randint(4, 6)
    elif raskusaste == "keskmine":
        pikkus = randint(7, 10)
    else:
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


def sõna_uuendamine(pakkumine, sõna, eelmine_sõna):
    uuendatud_sona = ""
    for element in range(len(eelmine_sõna)):
        if pakkumine == sõna[element]:
            uuendatud_sona = uuendatud_sona + pakkumine
        else:
            uuendatud_sona = uuendatud_sona + eelmine_sõna[element]
    return uuendatud_sona




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
    elif valitud == "keskmine":
        tk.Label(frame, image=Keskmine, width=1000, height=700).pack(fill="both", expand=1)
    elif valitud == "raske":
        tk.Label(frame, image=Raske, width=1000, height=700).pack(fill="both", expand=1)
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
    taustraam = tk.Frame(root)
    taustraam.config(bg="green")
    taustraam.pack(fill="both")
    taust_sonale = tk.PhotoImage(file="pildid/taust.png")

    sõna = sõna_valimine(raskus)


    tekstiraam=tk.Frame(taustraam,width = 1000,height=200)
    tekstiraam.config(bg="red")
    tekstiraam.pack(fill = "both", expand= 1)
    tk.Label(tekstiraam, image = taust_sonale, text = sõna_valimine(raskus)[0], font=("Arial", 40, "bold"), compound = "center",
             width = 1000, height = 200).pack(expand= 1)
    
    nupuraam = tk.Frame(taustraam,width = 700,height=500)
    nupuraam.pack(side="left")
    
    pixel = tk.PhotoImage(width=1, height=1)
    nupupilt = tk.PhotoImage(file="pildid/sininenupp.png")
    nupupilt2 = tk.PhotoImage(file="pildid/sininenupp2.png")
    for i in range(6):
        tk.Button(nupuraam,image=nupupilt,width = 90,font=("arial", 40),height=90               
                  ,text=str(tähed[i]),compound="c",command=lambda:nupuvajutus(i)).place(x=10+(115*i),y=0)
    for i in range(6,12):
        tk.Button(nupuraam,image=nupupilt,width = 90,font=("arial", 40),height=90
          ,text=str(tähed[i]),compound="c",command=lambda:nupuvajutus(i)).place(x=10+(115*(i-6)),y=110)
    for i in range(12,18):
        tk.Button(nupuraam,image=nupupilt,width = 90,font=("arial",40),height=90
          ,text=str(tähed[i]),compound="c",command=lambda:nupuvajutus(i)).place(x=10+(115*(i-12)),y=220)
    for i in range(18,24):
        tk.Button(nupuraam,image=nupupilt,width = 90,font=("arial", 40),height=90
        ,text=str(tähed[i]),compound="c",command=lambda:nupuvajutus(i)).place(x=10+(115*(i-18)),y=330)
    for i in range(24,27):

        tk.Button(nupuraam,image=nupupilt2,width=190,font=("arial", 40),height=35
        ,text=str(tähed[i]),compound="c",command=lambda:nupuvajutus(i)
        ).place(x=10+(235*(i-24)),y=440)

        
    pildiraam = tk.Frame(taustraam,width = 300,height=500)
    pildiraam.config(bg="yellow")
    pildiraam.pack(side="right")
    root.mainloop()
    
#funktsioon, kui nuppu vajutatakse
def nupuvajutus(täht):
    winsound.PlaySound('pildid/nupp.wav', winsound.SND_FILENAME)
    # sõna_uuendamine(arvamise_korrad, )

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

# Loome Tkinteri akna vajalike paramaatritega ja sinna sisse fraimi.
root = tk.Tk()
root.title("Poomismäng")
root.geometry(ekraani_suurus(1000, 700))
root.resizable(width="false", height="false")
frame = tk.Frame()
frame.pack(fill=tk.BOTH, expand=1)
esiekraan()