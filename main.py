from tkinter import Tk
from src.view.menu import Menu

def main():
    root = Tk()
    # Nastavíme ikonu alebo názov globálne ak treba
    root.title("3D Piškvorky")
    app = Menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
