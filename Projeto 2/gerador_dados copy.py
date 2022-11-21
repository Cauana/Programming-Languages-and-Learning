#window root#

window = Tk()
window.title ('Jogando dado')

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
                 text='Iniciar o Jogo', command='', fg='#000000',
                 anchor=CENTER, relief="raised", overrelief=RIDGE)
binicio.place(x=140,y=360)

bpararjogo = Button(window,
                 text='Reiniciar o jogo', command='', fg='#000000',
                 anchor=CENTER, relief="raised", overrelief=RIDGE)
bpararjogo.place(x=260,y=360)



window.resizable(False,False)
window.mainloop()