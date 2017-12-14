import tkinter as tk
from tkinter import PhotoImage
def ekraani_suurus(w, h):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    return ('%dx%d+%d+%d' % (w, h, x, y))

def raskusastme_valimine():
    global Frame

    frame.pack_forget()

    menu2_frame = tk.Canvas(root, width=root.winfo_width(), height=350)
    #===========================================================================
    # menu2_frame.config()
    # menu2_frame.tkraise()
    #===========================================================================
    menu2_frame.pack()
    avatud = PhotoImage(file="lihtnetest.png")
    suletud= PhotoImage(file="lihtnetest2.png")
    pildid.add(avatud)
    pildid.add(suletud)
    #===============================================================================
#     joonistamine1 = tk.Canvas(menu2_frame,width=500,height=600,background="white")
#     joonistamine1.pack(fill="both",expand=1)
#     
# 
#     joonistamine1.create_line(0, 0, 200, 100)
#     joonistamine1.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
#     img = (300, 400, image=suletud, activeimage=avatud)
#===============================================================================

    pealkiri = tk.Label(menu2_frame, text= "Keel ja raskusaste", font = ("Times", 40),anchor = tk.N)
    pealkiri.config(bg="yellow")
    pealkiri.pack(fill="x")
    

root = tk.Tk()

root.title("Poomismäng")
root.geometry(ekraani_suurus(1000, 700))
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)
pildid = set()
logo = tk.PhotoImage(file="noose.gif")

msg = tk.Message(frame,text = "POOMISMÄNG")
msg.config(bg = "lightgreen", font = ("times", 60),aspect = 500,pady=20,width = 1000)
nupp1=tk.Button(frame,text = "Start(avan uue akna)",font = ("arial",30), command=raskusastme_valimine)
nupp2= tk.Button(frame,text = "Välju",font = ("arial",30), command = root.destroy)
msg.pack(pady=10)
w1 = tk.Label(frame, image=logo).pack()
nupp1.place(x=90,y=500)
nupp1.config(bg="green", activebackground="yellow", anchor="center", bd=10)
nupp2.place(x=610,y=500)
nupp2.config(bg="red", activebackground="orange", anchor="center", bd=10)
root.mainloop()
    
