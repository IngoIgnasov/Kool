import tkinter as tk
from PIL import *



def ekraani_suurus(w, h):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    return ('%dx%d+%d+%d' % (w, h, x, y))

def raskusastme_valimine():
    global Frame
    frame.pack_forget()

    menu2_frame = tk.Frame(root, width=root.winfo_width(), height=350)
    menu2_frame.config()
    menu2_frame.tkraise()
    menu2_frame.pack(fill="both", expand=1)

    """
    joonistamine1 = tk.Canvas(menu2_frame, width=200, height=200)
    joonistamine1.pack()
    joonistamine1.create_line(0, 0, 200, 100)
    joonistamine1.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
    """

    pealkiri = tk.Label(menu2_frame, text= "Keel ja raskusaste", font = ("Times", 40))

    pealkiri.config(bg="yellow")
    pealkiri.pack(fill="x")






# Loome Tkinteri akna vajalike paramaatritega ja sinna sisse fraimi.

root = tk.Tk()
root.title("Poomismäng")
root.geometry(ekraani_suurus(1000, 700))
root.resizable(width="false", height="false")
frame = tk.Frame()
frame.pack(fill=tk.BOTH, expand=1)



#  Teen alumise freimi, panen taustaks pildi ja lisan nupud
muster = tk.PhotoImage(file="pildid/pealkiri.png")
peamine = tk.PhotoImage(file= "pildid/peamine.png")


pealkirja_frame = tk.Frame(frame)
pealkirja_frame.config(width= 1000, height=150)
pealkirja_frame.pack(fill=tk.BOTH, expand=1)
pealkirja_taust = tk.Label(pealkirja_frame, image=muster, width= 1000, height= 150, text="POO_ISMÄN_!", compound="center", font="Times 50 bold", pady= 0)
pealkirja_taust.pack(expand=1 , fill="both")


Alumine_osa = tk.Frame(frame)
Alumine_osa.config(width= 1000, height=550)
Alumine_osa.pack(fill="y", expand=1, side="left")
vasak_taust = tk.Label(Alumine_osa, image= peamine, width=1000, height= 550).pack(fill= "both", expand=1, pady = 0)


nupp_alusta=tk.Button(Alumine_osa,text = "Alusta",font = ("arial",30), command=raskusastme_valimine)
nupp_alusta.place(x=425,y=92)
nupp_alusta.config(image=muster, activebackground="green", anchor="center", bd=10, height=60, width= 120, compound="center")

nupp2= tk.Button(Alumine_osa, text = "Välju",font = ("arial",24), command = root.destroy, compound="center")
nupp2.place(x=435,y=200)
nupp2.config(image=muster, activebackground="red", anchor="center", bd=10, height= 50, width= 100)


root.mainloop()