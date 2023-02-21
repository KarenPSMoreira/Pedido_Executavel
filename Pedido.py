#importar biblioteca tkinter no qual pode manipular widgets/ caixas de alerta
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

count = 0

msg_box = messagebox.showwarning("ALERTA", "VOCÊ FOI HACKEADO")

if msg_box =='ok':
    msg_box = messagebox.showwarning("ALERTA!","PARA SER DESHACKEADO RESPONDA A SEGUINTE PERGUNTA...")
    
if msg_box =='ok':
    msg_box = messagebox.askquestion("O QUE ACHA?", "QUER SER O MEU AMOR PARA A VIDA TODA?")

#criar um loop de 5 tentativas caso a resposta seja não.
while msg_box == 'no':
    count += 1
    msg_box = messagebox.askquestion("O QUE ACHA?", "QUER SER O MEU AMOR PARA TODA VIDA?")
    if (count == 5):
        msg_box = messagebox.showwarning("IHHHH JA ERA","CONTRATO VITALÍCIO")
        break
if msg_box == 'yes':
    msg_box == messagebox.showinfo("EXCELENTE ESCOLHA!", "CONTRATO RENOVADO \n Validade: NUNCA")
    msg_box == messagebox.showinfo("VOCÊ É O AMOR DA MINHA VIDA!", "OBRIGADA POR ME FAZER TÃO FELIZ \n TE AMO... COM AMOR, XAYAHZINHA <3")
    