import tkinter.messagebox
from tkinter import *

# cores -----------------------------------------------------------------------------------------------------------------------------------
cor1 = '#fffefc' #branco
cor2 = '#050505' #preto


#criando janela ----------------------------------------------------------------------------------------------------------------------------
janela = Tk()
janela.geometry('550x220')
janela.configure(bg=cor1)

#configurando a jenela----------------------------------------------------------------------------------------------------------------------
tela = Label(janela, bg=cor2, width=40, height=10, bd=1)
tela.grid(row=0, column=0)

frame_direita = Frame(janela, bg=cor1)
frame_direita.grid(row=0, column=1, padx=8)

frame_baixo = Frame(janela, bg=cor1)
frame_baixo.grid(row=1, column=0, columnspan=2)

#função
def escala(valor):
    r=slide_red.get()
    g=slide_green.get()
    b=slide_blue.get()

    rgb = f'{r}, {g}, {b}'
   
    hexadecimal = '#%02x%02x%02x' % (r, g, b)
    
    #Alterando a cor da tela
    tela['bg'] = hexadecimal
    
    #Alterando a Entry
    cor.delete(0, END)
    cor.insert(0, hexadecimal)
    
    
    
    
#função onclik
def onClick():
    tkinter.messagebox.showinfo('cor', "copiado")
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(cor.get())
    clip.destroy()
    
#configurando o frame da direita---------------------------------------------------------------------------------------------------------
direita_red=Label(frame_direita, text='Vermelho', width=8, bg=cor1, fg='red', anchor= 'nw', font=('Times New Roman', 12, 'bold'))
direita_red.grid(row=0, column=0)
slide_red = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor1, fg='red', orient=HORIZONTAL)
slide_red.grid(row=0, column=1)

direita_green = Label(frame_direita, text='Verde', width=7, bg=cor1, fg='green', anchor= 'nw', font=('Times New Roman', 12, 'bold'))
direita_green.grid(row=1, column=0)
slide_green = Scale(frame_direita, command=escala,  from_=0, to=255, length=150, bg=cor1, fg='green', orient=HORIZONTAL)
slide_green.grid(row=1, column=1)

direita_blue = Label(frame_direita, text='Azul', width=7, bg=cor1, fg='blue', anchor= 'nw', font=('Times New Roman', 12, 'bold'))
direita_blue.grid(row=2, column=0)
slide_blue = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor1, fg='blue', orient=HORIZONTAL)
slide_blue.grid(row=2, column=1)


#configurando frame de baixo--------------------------------------------------------------------------------------------------------
baixo_rgb = Label(frame_baixo, text='CÓDIGO RGB:', bg=cor1, font=('Times New Roman', 12, 'bold'))
baixo_rgb.grid(row=0, column=0, padx=5)

#Codigo de cores--------------------------------------------------------------------------------------------------------------------
cor = Entry(frame_baixo, width=12, font=('Times New Roman', 12, 'bold'), justify=CENTER)
cor.grid(row=0, column=1, padx=5)

#botões-----------------------------------------------------------------------------------------------------------------------------
botao_copiar = Button(frame_baixo, command=onClick, text='Copiar', bg=cor1, font=('Times New Roman', 10, 'bold'), relief=RAISED, overrelief=RIDGE)
botao_copiar.grid(row=0, column=2, padx=5)


#app Nome---------------------------------------------------------------------------------------------------------------------------
label_appnome = Label(frame_baixo, text='Seletor de Cores',  bg=cor1, font=('Ivy', 13, 'bold'))
label_appnome.grid(row=0, column=3, padx=63)



janela.mainloop()               