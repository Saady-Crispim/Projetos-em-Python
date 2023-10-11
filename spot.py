import tkinter as tk
import pyautogui as py
import time
def spotify():
    py.press('winleft')
    py.write('power shell')
    time.sleep(3)
    py.press('enter')
    time.sleep(3)
    py.write('iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.ps1 | iex')
    time.sleep(5)
    py.press('enter')
    time.sleep(5)
    py.write('iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-marketplace/main/resources/install.ps1 | iex')
    py.press('enter')
    time.sleep(5)
    py.write('y')
    time.sleep(5)
    py.press('enter')

janela = tk.Tk()
janela.title("Cotação Atual de Moedas")
texto = tk.Label(janela, text="Clique no botão para instalar extensões no spotify")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = tk.Button(janela, text="Adicionar extensões", command=spotify)
botao.grid(column=0, row=1, padx=10, pady=10)

janela.mainloop()