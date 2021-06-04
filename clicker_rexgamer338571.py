# IMPORT
from tkinter import *
import time

# Tworzenie ekranu/okna
ws10 = Tk()
# CONFIG Okna
ws10.title("Test aplikacji Tkinter")
ws10.geometry("600x600") # "Szerokość x wysokość okna"
ws10.configure(bg = "orange")

# Zmienna
liczbaScore = 0
multi = 1
cost_upgrade = 100

# Funkcje
def add_click():
    global liczbaScore
    # Zwiekszamy wartość zmiennej liczbaScore
    liczbaScore = liczbaScore + multi
    #
    # Zmieniamy tekst w naszym elemencie score
    score.configure(text = liczbaScore)

def upgrade():
    global multi, liczbaScore, cost_upgrade
    # Zwiększamy mnożnik kliknięć
    if liczbaScore >= cost_upgrade:
        multi = multi * 2
        # Odejmujemy koszt upgrade od licznika
        liczbaScore = liczbaScore - cost_upgrade
        # Aktualizujemy ilość kliknięć
        score.configure(text = liczbaScore)
        # Zwiększamy koszt upgrade'u
        cost_upgrade = cost_upgrade * 2
        # Aktualizujemy koszt upgrade'u
        upgrade_button.configure(text = "UPGRADE:" + str(cost_upgrade))

# Tworzymy elementy naszej apki
#Label
header = Label(ws10,
               text = "CLICKS:",
               fg = "red",
               bg = "orange",
               font = ("Calvin", 60),
               )
header.pack()

# Label 2
score = Label(ws10,
              text = "0",
              fg = "blue",
              bg = "orange",
              font = ("Calvin", 80)
              )
score.pack()

# Przycisk
test_button = Button(ws10,
                     text = "CLICK ME, PLS",
                     fg = "red",
                     bg = "black",
                     font = ("Calvin", 40),
                     borderwidth = 15,
                     command = add_click
                     )
test_button.pack()

# Button
upgrade_button = Button(ws10,
                     text = "UPGRADE",
                     fg = "lime",
                     bg = "black",
                     font = ("Consolas", 40), # "Consolas"
                     borderwidth = 15, # border = ramka / width = szerkosc
                     command = upgrade,
                     )
upgrade_button.pack()
                     
                     
                              








# mainloop
mainloop()
