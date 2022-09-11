from tkinter import *
from tkinter import ttk
from random import randint
from PIL import ImageTk, Image

global rounds
global pmaquina
global pjogador
global btn
rounds = 0
pmaquina = 0
pjogador = 0
btn = 1

def btninicio_clicked():
    print('começo')
    global imgpedra
    global imgpapel
    global imgtesoura
    global bpedra
    global bpapel
    global btesoura
    global rounds
    global pmaquina
    global pjogador
    global jogue
    global sinalizadorevd
    global btn
    global binicio

    # Zerar o placar
    rounds = 0
    pmaquina = 0
    pjogador = 0
    btn == 0

    jogue = Label(frame_baixo,text= 'Você quer: Pedra, Papel ou Tesoura?', font= '30')
    jogue.place(x=50,y=60)

    imgpedra = Image.open('pedra.png')
    imgpedra = imgpedra.resize((70, 70))
    imgpedra = ImageTk.PhotoImage(imgpedra)

    bpedra = Button(frame_baixo, image=imgpedra, command=btnpedra_clicked, relief="flat")
    bpedra.place(x=60, y=140, width=80, height=80)

    imgpapel = Image.open('papel.png')
    imgpapel = imgpapel.resize((70, 70))
    imgpapel = ImageTk.PhotoImage(imgpapel)

    bpapel = Button(frame_baixo, image=imgpapel, command=btnpapel_clicked, relief="flat")
    bpapel.place(x=218, y=140, width=80, height=80)

    imgtesoura = Image.open('tesoura.png')
    imgtesoura = imgtesoura.resize((80, 80))
    imgtesoura = ImageTk.PhotoImage(imgtesoura)

    btesoura = Button(frame_baixo, image=imgtesoura, command=btntesoura_clicked, relief="flat")
    btesoura.place(x=360, y=140, width=80, height=80)

    if btn == 0:
        binicio['command'] = ''


def btn_zerarojogo():
    global rounds
    global pmaquina
    global pjogador
    global jogue
    global imgpedrapc
    global imgpapelpc
    global imgtesourapc
    global jog1pontos
    global jog2pontos
    global contador
    global sinalizadorevd
    global labelzerar
    rounds = 0
    pjogador = 0
    pmaquina = 0
    jog1pontos['text'] = pjogador
    jog2pontos['text'] = pmaquina
    contador['text'] = 0
    sinalizadorevd['text'] = '\n\n\n'
    imgclear = Image.open('clear.png')
    imgclear = ImageTk.PhotoImage(imgclear)
    imgclear1 = Label(window, image=imgclear)
    imgclear1.place(x=240, y=100)

#window root#

window = Tk()
window.title ('Pedra Papel Tesoura...')

#Dimensão da screen para abrir o programa no meio da tela
largura = 500
altura = 400
largura_screen = window.winfo_screenwidth()
altura_screen = window.winfo_screenheight()
posx = largura_screen/2-largura/2
posy = altura_screen/2-altura/2
window.geometry('%dx%d+%d+%d' % (largura,altura,posx,posy))

#Estrutura da página | Frames#

frame_baixo = Frame(window, width=500, height=500, bg='#f0f0f0', pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)
frame_cima = Frame(window, width=500, height=100, bg='#722f37', pady=0,padx=0, relief='raised')
frame_cima.grid(row = 0, column=0, sticky=NW)


#Config Frame CIMA

jog1pontos = Label(frame_cima, text='0', height=1, anchor='center', font=('bold',38), bg='#722f37', fg='#FFFFFF')
jog1pontos.place(x=133,y=5)

jog2pontos = Label(frame_cima, text='0', height=1, anchor='center', font=('bold',38), bg='#722f37', fg='#FFFFFF')
jog2pontos.place(x=305,y=5)

jog1 = Label(frame_cima, text='Você', height=1, anchor='center', font='extrabold', bg='#722f37', fg='#FFFFFF')
jog1.place(x=25,y=30)

jog2 = Label(frame_cima, text='Máquina', height=1, anchor='center', font='extrabold', bg='#722f37', fg='#FFFFFF')
jog2.place(x=400,y=30)

sinalizador = Label(frame_cima, text=':', height=1, anchor='center', font=('extrabold', 25), bg='#722f37', fg='#FFFFFF')
sinalizador.place(x=240,y=40,anchor=CENTER)

textcont = Label(frame_cima, text= 'Número de Jogadas:',height=1, anchor='center', font=('extrabold', 12), bg='#722f37', fg='#FFFFFF')
textcont.place(x=25,y=78)
contador = Label(frame_cima, text= '0', height=1, anchor='center', font=('extrabold', 12), bg='#722f37', fg='#FFFFFF')
contador.place(x=175,y=78)

#Botão Iniciar e jogada pc
binicio = Button(window,
                 text='Iniciar o Jogo', command=btninicio_clicked, fg='#000000',
                 anchor=CENTER, relief="raised", overrelief=RIDGE)
binicio.place(x=140,y=360)

bpararjogo = Button(window,
                 text='Reiniciar o jogo', command=btn_zerarojogo, fg='#000000',
                 anchor=CENTER, relief="raised", overrelief=RIDGE)
bpararjogo.place(x=260,y=360)

#imagenspc
imgpedrapc = Image.open('pedra_pc.png')
imgpedrapc = imgpedrapc.resize((150,110))
imgpedrapc = ImageTk.PhotoImage(imgpedrapc)

imgpapelpc = Image.open('papel_pc.jpg')
imgpapelpc = imgpapelpc.resize((150,100))
imgpapelpc = ImageTk.PhotoImage(imgpapelpc)

imgtesourapc = Image.open('tesoura_pc.png')
imgtesourapc = imgtesourapc.resize((150,110))
imgtesourapc = ImageTk.PhotoImage(imgtesourapc)

#Funções e Lógica do Jogo#

def btnpedra_clicked():
    global rounds
    global jogue
    global sinalizadorevd
    jogue.destroy()
    while True:
        global pmaquina
        global pjogador
        list = ('Pedra', 'Papel', 'Tesoura')
        computador = randint(0, 2)
        rounds +=1
        if computador == 0:
            img1 = Label(window, image=imgpedrapc)
            img1.place(x=280, y=100)
            print(img1)
            sinalizadorevd = Label(frame_baixo, text='A Máquina... \njogou Pedra. \n EMPATE ', font='30',width=20)
            sinalizadorevd.place(x=20, y=15)
            break
        if computador == 1:
            img2 = Label(window, image=imgpapelpc)
            img2.place(x=280, y=110)
            print(img2)
            pmaquina += 10
            sinalizadorevd = Label(frame_baixo, text='Você... \nPERDEU, infelizmente: \n Ponto para Máquina ', font='30',width=20)
            sinalizadorevd.place(x=20, y=15)
            break
        if computador == 2:
            img3 = Label(window, image=imgtesourapc)
            img3.place(x=280, y=100)
            print(img3)
            pjogador += 10
            sinalizadorevd = Label(frame_baixo, text='VOCÊ...\n GANHOU. Parabéns, \nvocê ganhou do pc', font='30',width=20)
            sinalizadorevd.place(x=20, y=15)
            break
    jog1pontos['text'] = pjogador
    jog2pontos['text'] = pmaquina
    contador['text'] = rounds
def btnpapel_clicked():
    global rounds
    global jogue
    global sinalizadorevd
    jogue.destroy()
    while True:
        global pmaquina
        global pjogador
        list = ('Pedra', 'Papel', 'Tesoura')
        computador = randint(0, 2)
        rounds += 1
        if computador == 0:
            img1 = Label(window, image=imgpedrapc)
            img1.place(x=280, y=100)
            print(img1)
            pjogador += 10
            sinalizadorevd = Label(frame_baixo, text='VOCÊ...\n GANHOU. Parabéns, \nvocê ganhou do pc', font='30',
                                   width=20)
            sinalizadorevd.place(x=20, y=15)
            break
        if computador == 1:
            img2 = Label(window, image=imgpapelpc)
            img2.place(x=280, y=110)
            print(img2)
            sinalizadorevd = Label(frame_baixo, text='A Máquina... \njogou Papel. \n EMPATE ', font='30', width=20)
            sinalizadorevd.place(x=20, y=15)
            break
        if computador == 2:
            img3 = Label(window, image=imgtesourapc)
            img3.place(x=280, y=100)
            print(img3)
            pmaquina+=10
            sinalizadorevd = Label(frame_baixo, text='Você... \nPERDEU, infelizmente: \n Ponto para Máquina ',
                                   font='30', width=20)
            sinalizadorevd.place(x=20, y=15)
            break
        jog1pontos['text'] = pjogador
        jog2pontos['text'] = pmaquina
    jog1pontos['text'] = pjogador
    jog2pontos['text'] = pmaquina
    contador['text'] = rounds
def btntesoura_clicked():
    global rounds
    global jogue
    global sinalizadorevd
    jogue.destroy()
    while True:
        global pmaquina
        global pjogador
        list = ('Pedra', 'Papel', 'Tesoura')
        computador = randint(0, 2)
        rounds += 1
        if computador == 0:
            img1 = Label(window, image=imgpedrapc)
            img1.place(x=280, y=100)
            print(img1)
            pmaquina += 10
            sinalizadorevd = Label(frame_baixo, text='Você... \nPERDEU, infelizmente: \n Ponto para Máquina ',
                                   font='30', width=20)
            sinalizadorevd.place(x=20, y=15)
            break
        if computador == 1:
            img2 = Label(window, image=imgpapelpc)
            img2.place(x=280, y=110)
            print(img2)
            pjogador += 10
            sinalizadorevd = Label(frame_baixo, text='VOCÊ...\n GANHOU. Parabéns, \nvocê ganhou do pc', font='30',
                                   width=20)
            sinalizadorevd.place(x=20, y=15)
            break
        if computador == 2:
            img3 = Label(window, image=imgtesourapc)
            img3.place(x=280, y=100)
            print(img3)
            sinalizadorevd = Label(frame_baixo, text='A Máquina... \njogou Tesoura. \n EMPATE ', font='30', width=20)
            sinalizadorevd.place(x=20, y=15)
            break
    jog1pontos['text'] = pjogador
    jog2pontos['text'] = pmaquina
    contador['text'] = rounds


window.resizable(False,False)
window.mainloop()