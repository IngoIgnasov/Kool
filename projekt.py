from tkinter import  Tk, BOTH
from tkinter.ttk import Frame


# Tekitan õige suurusega akna ja paigutan selle ekraanil õigesse kohta

class Example(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Sain selle akna lopuks keskele")
        self.pack(fill=BOTH, expand=1)
        self.aken_keskele()

    def aken_keskele(self):
        w = 700
        h = 700

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2

        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    root = Tk()
    app = Example()
    root.mainloop()

if __name__== "__main__":
    main()