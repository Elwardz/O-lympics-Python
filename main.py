import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

# Carregar o Arquivo do Excel
df = pd.read_excel('questions.xlsx') #Ler o excel

#Pegar as perguntas aleatoriamente
questions = df.values.tolist() #Pega o valor de todas as perguntas.


# variaveis globais
score = 0
current_question = 0


#Funcao para verificar a resposta
def check_answer(answer):
    global score, current_question

    if answer == correct_answer.get():
        score+=1

    current_question += 1

    if current_question < len(questions):
        display_question()
    else:
        show_result()


# Funcao para exibir a proxima pergunta
def display_question():
    question, option1, option2, option3, option4, answer = questions[current_question]
    question_label.config(text=question)
    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda:check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda:check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda:check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda:check_answer(4))

    correct_answer.set(answer)


#Funcao para exibir o resultado final
def show_result():
    messagebox.showinfo("O-lympics Finalizado", f"Parabéns! Você completou o O-lympics. \n\nPontuação Final: {score}/{len(questions)}")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)
    play_again_btn.pack()


#Funcao para jogar novamente
def play_again():
    global score, current_question
    score = 0
    current_question = 0
    random.shuffle(questions)
    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk.NORMAL)
    play_again_btn.pack_forget()


janela = tk.Tk()
janela.title('O-lympics')
janela.geometry("600x400")

#definindo cores
background_color = "#1E1E2F"  # Cor de fundo escura
text_color = "#F5FFFA"  # Texto branco suave
button_color = "#FF6347"  # Cor vibrante para os botões
button_text_color = "#FFFFFF"  # Texto branco nos botões


janela.config(bg=background_color)
janela.option_add('*Font', 'Arial')  #define cor para toda a interface


#icone na tela
app_icon = PhotoImage(file="icons8-quiz-100.png")
app_label = tk.Label(janela, image=app_icon, bg=background_color)
app_label.pack(pady=10)

#componentes da Interface #Apresenta as perguntas
question_label = tk.Label(janela, text="", wraplength=380, bg=background_color, fg=text_color, font=("Arial",12,"bold"))
question_label.pack(pady=20)

correct_answer = tk.IntVar()

#buttons
option1_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option1_btn.pack(pady=10)

option2_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option2_btn.pack(pady=10)

option3_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option3_btn.pack(pady=10)

option4_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option4_btn.pack(pady=10)

play_again_btn = tk.Button(janela, command=play_again, text="Jogar Novamente", width=30, bg=button_color, fg=button_text_color, font=("Arial", 10, "bold"))


display_question()


janela.mainloop()