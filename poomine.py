import tkinter as tk

def ekraani_suurus(w, h):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    return ('%dx%d+%d+%d' % (w, h, x, y))


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
    if valitud == "keskmine":
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
    kerge.place(x=435, y=150)

    keskmine = tk.Button(frame, text="Keskmine")
    keskmine.config(font=("arial", 24), width=150, height=50, image=muster, compound="center",
                 activebackground="orange", bd=10, command=lambda: raskusastme_valimine("keskmine"))
    keskmine.place(x=410, y=240)

    raske = tk.Button(frame, text="Raske")
    raske.config(font=("arial", 24), width=100, height=50, image=muster, compound="center",
                 activebackground="red", bd=10, command=lambda: raskusastme_valimine("raske"))
    raske.place(x=435, y=330)




    root.mainloop()





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