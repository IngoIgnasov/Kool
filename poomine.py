
import tkinter as tk
# Kas see kood kaob ara voi ei kao, eks me näe
def ekraani_suurus(w, h):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    return ('%dx%d+%d+%d' % (w, h, x, y))

def raskusastme_valimine(*milline):
    global Frame

    frame.pack_forget()

    menu2_frame = tk.Frame(root, width=root.winfo_width(), height=350, bg="green")
    menu2_frame.config()
    menu2_frame.tkraise()
    menu2_frame.pack(fill="both", expand=1)

    pealkiri = tk.Label(menu2_frame, text= "Keel ja raskusaste", font = ("Times", 40))

    pealkiri.config(bg="yellow")
    pealkiri.pack(fill="x")



root = tk.Tk()

root.title("Poomismäng")
root.geometry(ekraani_suurus(1000, 700))
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

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
    
