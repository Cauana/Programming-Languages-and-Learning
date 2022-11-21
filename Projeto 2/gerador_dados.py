import random
import PySimpleGUI as sg

def Janela():
    sg.theme('DarkAmber')
    #Layout
    layout1 = [
        [sg.Text('Jogar o dado?',key='textoprincipal')],
        [sg.Button('sim'), sg.Button('Não')]
    ]
    return sg.Window('Simulador de Dado', layout=layout1, finalize=True)

def Janela_Dado():
    sg.theme('DarkAmber')
    #valor do dado
    dado = random.randint(1,6)
    if dado == 1:
        dado1 = sg.Image("Projeto 2\dado1.png")
    elif dado == 2:
        dado1 = sg.Image("Projeto 2\dado2.png")
    elif dado == 3:
        dado1 = sg.Image("Projeto 2\dado3.png")
    elif dado == 4:
        dado1 = sg.Image("Projeto 2\dado4.png")
    elif dado == 5:
        dado1 = sg.Image("Projeto 2\dado5.png")
    elif dado == 6:
        dado1 = sg.Image("Projeto 2\dado6.png")
    
    #Layout
    layout2 = [
        [sg.Text('',key='textodado')],
        [sg.Text(f'O dado gerou o valor:\n {dado}')],
        [dado1],
        [sg.Text(f'Jogar novamente?',key='textojogarnovamente')],
        [sg.Button('sim'), sg.Button('Não')]
        ]
    return sg.Window('Simulador de Dado', layout=layout2,finalize=True)

    

janela, janela2 = Janela(), None

    #Ler eventos
while True:
    window, evento, valores = sg.read_all_windows()
    if evento == "Não" or evento == sg.WIN_CLOSED:
        break
    elif evento =='sim':
        janela2 = Janela_Dado()
        janela.hide()
    
janela.close()
        




