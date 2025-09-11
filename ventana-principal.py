import tkinter as tk
from vista import Ventana

root = tk.Tk()
root.geometry("700x400")
root.title("Cursos")
app = Ventana(master=root)
app.mainloop()