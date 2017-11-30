
import tkinter as tk
# Kas see kood kaob ara voi ei kao, eks me näe
def ekraani_suurus(w, h):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    return ('%dx%d+%d+%d' % (w, h, x, y))

def ekraani_vahetamine(*milline):
    uus_frame = tk.Frame(root)
    uus_frame.config(bg="green")
    uus_frame.tkraise()
    frame.pack_forget()
    uus_frame.pack(fill=tk.BOTH, expand=1)

root = tk.Tk()

root.title("Poomismäng")
root.geometry(ekraani_suurus(1000, 700))
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

logo = tk.PhotoImage(file="noose.gif")

msg = tk.Message(frame,text = "POOMISMÄNG")
msg.config(bg = "lightgreen", font = ("times", 60),aspect = 500,pady=20,width = 1000)
nupp1=tk.Button(frame,text = "Start(avan uue akna)",font = ("arial",30), command=ekraani_vahetamine)
nupp2= tk.Button(frame,text = "Välju",font = ("arial",30), command = root.destroy)
msg.pack(pady=10)
w1 = tk.Label(frame, image=logo).pack()
nupp1.place(x=90,y=500)
nupp2.place(x=610,y=500)
root.mainloop()
    