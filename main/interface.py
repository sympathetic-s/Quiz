import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

# Carregar o arquivo do Excel
df = pd.read_excel('questoes.xlsx')

# Pegar as perguntas aleatoriamente
questoes = df.sample(n=5).values.tolist()

# Variáveis globais 
score = 0
current_question = 0


# Função para verificar a resposta 
def check_answer(answer): 
    global score, current_question

    if answer == correct__answer.get():
        score+=1

    current_question +=1

    if current_question < len(questoes):
        display_question()
    else:
        show_result()

# Função para exibir a próxima pergunta
def display_question():
    question, option1, option2, option3, option4, answer = questoes[current_question]
    question_label.config(text=question)
    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda:check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda:check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda:check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda:check_answer(4))

    correct__answer.set(answer)



# Função apra exibir o resultado final
def show_result():
    messagebox.showinfo("Quiz Finalizado", f"Parabéns! Você completou o quiz.\n\nPontuação final: {score}/{len(questoes)}")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)
    play_again_btn.pack()



# Função para jogar novamente
def play_again():
    global score, current_question
    score = 0 
    current_question = 0
    random.shuffle(questoes)
    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk.NORMAL)
    play_again_btn.pack_forget()




janela = tk.Tk()
janela.title("Quiz da Loucura")
janela.geometry("400x450")

# Definindo as cores

background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"
button_color1 = "#555D4C"
button_text_color = "#FFFFFF"


janela.config(bg=background_color)
janela.option_add("*Font", "Arial")

# Icon na tela

app_icon = PhotoImage(file="logo.png")
app_label = tk.Label(janela, image=app_icon, bg=background_color)
app_label.pack(pady=10)

question_label = tk.Label(janela, text="", wraplength=380, bg=background_color, fg=text_color, font=("Arial", 12, "bold"))
question_label.pack(pady=20)

correct__answer = tk.IntVar()

option1_btn = tk.Button(janela, text="", width=40, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option1_btn.pack(pady=10)

option2_btn = tk.Button(janela, text="", width=40, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option2_btn.pack(pady=10)

option3_btn = tk.Button(janela, text="", width=40, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option3_btn.pack(pady=10)

option4_btn = tk.Button(janela, text="", width=40, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option4_btn.pack(pady=10)

play_again_btn = tk.Button(janela, command=play_again, text="Jogar novamente", width=40, bg=button_color1, fg=button_text_color, font=("Arial", 10, "bold"))



display_question()

janela.mainloop()