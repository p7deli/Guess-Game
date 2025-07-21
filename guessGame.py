import tkinter as tk
from customtkinter import CTkButton, CTkLabel, CTkEntry
import random

WIDTH, HEIGHT = 650, 650
PATHCOLOR = '#222'

class GuessGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.x = ((self.winfo_screenwidth() // 2) - (WIDTH // 2))
        self.y = ((self.winfo_screenheight() // 2) - (HEIGHT // 2)) - 30

        self.title('Guess Game')
        self.geometry(f'{WIDTH}x{HEIGHT}+{self.x}+{self.y}')
        self.config(bg='#222')
        self.resizable(False, False)

        CTkButton(self, text='Again!', font=('Press Start 2P', 20),
                  fg_color='white', corner_radius=0, text_color='black',
                  hover_color='gray', width=150, height=70).place(x=20, y=20)
        
        CTkLabel(self, text='<Between 1 and 20>', text_color='white', font=('Press Start 2P', 15, 'bold')).place(x=340, y=30)
        CTkLabel(self, text='Guess My\nNumber!', text_color='white', font=('Press Start 2P', 40, 'bold')).place(x=160, y=110)

        CTkLabel(self, text='='*500, font=('Press Start 2P', 20, 'bold')).place(x=0, y=280)

        self.lbl_number = CTkLabel(self, text='?', font=('Press Start 2P', 40, 'bold'),
                 width=160, height=140, fg_color='white', text_color='black')
        self.lbl_number.place(x=240, y=220)

        self.txt_guess = CTkEntry(self, width=250, height=120, fg_color='#222', font=('Press Start 2P', 45),
                            text_color='white', border_color='white', justify='center',
                            border_width=4, corner_radius=0)
        self.txt_guess.place(x=20, y=375)

        self.message = CTkLabel(self, text='Start\nguessing...', font=('Press Start 2P', 20, 'bold'),
            text_color='white', anchor='ne')
        self.message.place(x=350, y=400)

        CTkLabel(self, text='💯 Score: ', font=('Press Start 2P', 15, 'bold'),
            text_color='white', anchor='ne').place(x=350, y=540)
        self.lbl_score = CTkLabel(self, text='20', font=('Press Start 2P', 15, 'bold'),
            text_color='white', anchor='ne')
        self.lbl_score.place(x=500, y=540)

        CTkLabel(self, text='🥇 Highscore: ', font=('Press Start 2P', 15, 'bold'),
            text_color='white', anchor='ne').place(x=350, y=580)
        self.lbl_highscore = CTkLabel(self, text='0', font=('Press Start 2P', 15, 'bold'),
            text_color='white', anchor='ne')
        self.lbl_highscore.place(x=560, y=580)

        CTkButton(self, text='Check!', font=('Press Start 2P', 20),
            fg_color='white', corner_radius=0, text_color='black',
            hover_color='gray', width=150, height=70).place(x=70, y=540)


if __name__ == '__main__':
    game = GuessGame()
    game.mainloop()