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
    #Layout
    n = GerarValorDoDado()
    layout2 = [
        [sg.Text('',key='textodado')],
        [sg.Text(f'{GerarValorDoDado()}',key='textojogarnovamente')],
        [sg.Button('sim'), sg.Button('Não')]
    ]
    return sg.Window('Simulador de Dado', layout=layout2,finalize=True)

def GerarValorDoDado():
    print(random.randint(1, 6))
    

janela, janela2 = Janela(), None

    #Ler eventos
while True:
    window, evento, valores = sg.read_all_windows()
    if window == janela and evento == sg.WIN_CLOSED:
        break
    elif window == janela and evento =='sim':

        janela2 = Janela_Dado()
        janela.hide()
    elif evento == 'não' or evento == 'n':
        break
    else:
        print('Favor digitar sim ou não')
        




