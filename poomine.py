
import tkinter as tk

def ekraani_suurus(w, h):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    return ('%dx%d+%d+%d' % (w, h, x, y))




root = tk.Tk()

root.title("Poomismäng")
root.geometry(ekraani_suurus(700, 700))
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

msg = tk.Message(frame,text = "POOMISMÄNG")
msg.config(bg = "lightgreen", font = ("times", 60),aspect = 500,pady=20,width = 1000)
msg.pack(pady=10)
nupp1=tk.Button(frame,text = "Start")
nupp1.pack(anchor=tk.SW)
root.mainloop()
    