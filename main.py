import tkinter as tk
from vote_gui import VoteGUI

def main():
    root = tk.Tk()
    app = VoteGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
