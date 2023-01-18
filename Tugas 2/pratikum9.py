from tkinter import *

root = Tk()
root.title("Biodata")
root.geometry("500x500")

lblAngka1 = Label(root, text = "Masukan Nama : ")
lblAngka1.grid(column=0, row=0)

lblAngka2 = Label(root, text = "NRP : ")
lblAngka2.grid(column=0, row=1)

lblAngka3 = Label(root, text="Umur : ")
lblAngka3.grid(column=0, row=2)

lblAngka4 = Label(root, text="Jenis Kelamin : ")
lblAngka4.grid(column=0, row=3)

inputNama = Entry(root, width=20)
inputNama.grid(column=1, row=0)

inputNRP = Entry(root, width=20)
inputNRP.grid(column=1, row=1)

inputUmur = Entry(root, width=20)
inputUmur.grid(column=1, row=2)

inputJK = Entry(root, width=20)
inputJK.grid(column=1, row=3)

root.mainloop()