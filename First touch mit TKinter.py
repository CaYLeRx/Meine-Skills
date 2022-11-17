import tkinter as tk

root = tk.Tk()
root.title("Willkommen")
root.geometry("450x450")
root.minsize(width=250, height=250) 


label1 = tk.Label(root, text="Hallo CaYLeR", bg="Black")
label1.pack(side="top", expand=True, fill="both")

label2 = tk.Label(root, text= "Wie geht es dir?", bg="Red")
label2.pack(side="top", expand=True, fill="both")

label3 = tk.Label(root,text= "Hast du gerade etwas gelernt?", bg="Gold")
label3.pack(side="top", expand=True, fill="both")


root.maxsize(width=920, height=1000)
root.resizable(width=False, height=True)


root.mainloop()
