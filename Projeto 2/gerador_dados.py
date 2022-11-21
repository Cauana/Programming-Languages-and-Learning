import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        
        sg.theme('DarkAmber')
        #Layout
        self.layout = [
            [sg.Text('Jogar o dado?',key='textoprincipal')],
            [sg.Button('sim'), sg.Button('Não')]
        ]
        
    def Iniciar(self):
        
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        #Ler eventos
        self.eventos, self.valores = self.janela.Read()
        try:
            if self.eventos =='sim' or self.eventos =='s':
                self.janela['textoprincipal'].update(f"Valor do dado:{self.GerarValorDoDado()}\n Quer jogar novamente?")
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Ok, Finalizando gerador de dados')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta!')
            
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()

