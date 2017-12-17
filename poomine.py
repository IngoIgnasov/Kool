import tkinter as tk
from testproj import teesõnadjatähed
from tkinter import PhotoImage

m = teesõnadjatähed("eesti_keel.txt")
sõnad = m[0]
tähed = m[1]
print(sõnad[500])
print(tähed)
print(len(tähed))
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

    pealkiri = tk.Label(menu2_frame, text= "Keel ja raskusaste", font = ("Times", 40))

    pealkiri.config(bg="yellow")
    pealkiri.pack(fill="x")
    
def põhiaken():
    #loon 3 eraldi frame, kuhu panna sõna, nupud ja poomispilt
    global frame
    frame.pack_forget()
    taustraam = tk.Frame(root)
    taustraam.config(bg="green")
    taustraam.pack(fill="both",expand =1)
    
    tekstiraam=tk.Frame(root,width = 1000,height=150)
    tekstiraam.config(bg="red")
    tekstiraam.pack()
    
    nupuraam = tk.Frame(root,width = 700,height=550)
    nupuraam.config(bg="blue")
    nupuraam.pack(side="left")
    
    pildiraam = tk.Frame(root,width = 300,height=550)
    pildiraam.config(bg="yellow")
    pildiraam.pack(side="right")

    for i in range(9):
        tk.Button(nupuraam,text=tähed[i],height=200,width = 70).grid(row=0,column=i)
    tk.BUtton(nupuraam,text = "I").grid(row=1,column=1)
    

root = tk.Tk()
root.title("Poomismäng")
root.geometry(ekraani_suurus(1000, 700))
root.resizable(width="false", height="false")
frame = tk.Frame()
frame.pack(fill=tk.BOTH, expand=1)


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


nupp_alusta=tk.Button(Alumine_osa,text = "Alusta",font = ("arial",30), command=põhiaken)
nupp_alusta.place(x=425,y=92)
nupp_alusta.config(image=muster, activebackground="green", anchor="center", bd=10, height=60, width= 120, compound="center")

nupp2= tk.Button(Alumine_osa, text = "Välju",font = ("arial",24), command = root.destroy, compound="center")
nupp2.place(x=435,y=200)
nupp2.config(image=muster, activebackground="red", anchor="center", bd=10, height= 50, width= 100)



root.mainloop()
