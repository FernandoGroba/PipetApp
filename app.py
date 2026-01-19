import tkinter as tk
import datetime
from tkinter import ttk, messagebox
from database import Database
from model.mascota import Mascota


class PipetApp:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title('PipetApp')

        # Geometry
        self.root.geometry('414x600')
        self.root.resizable(False, False)

        # Estilos
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#f5f5f5')
        style.configure('Treeview', rowheigth=35)

        # Header
        header = ttk.Frame(self.root, padding='10')
        header.pack(fill='x')
        ttk.Label(header,
                  text='Mis Mascotas',
                  font=('Roboto', 16, 'bold')).pack()

        self.ent_buscar = ttk.Entry(header)
        self.ent_buscar.pack(fill='x',
                             pady=10)
        self.ent_buscar.insert(0, 'Buscar mascota...')

        # --- LISTA CENTRAL (Treeview) ---
        self.tree = ttk.Treeview(self.root,
                                 columns=('Nombre', 'Vencimiento'),
                                 show='headings'
                                 )
        self.tree.heading('Nombre', text='Mascota')
        self.tree.heading('Vencimiento', text='Vencimiento')
        self.tree.column('Nombre', width=200)
        self.tree.column('Vencimiento', width=150)
        self.tree.pack(fill='both',
                       expand=True,
                       padx=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = PipetApp(root)
    root.mainloop()
