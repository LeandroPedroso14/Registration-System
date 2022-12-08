import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
         layout = [
             [sg.Txt('Produto'),sg.Input ()],
             [sg.Txt('Conteúdo'),sg.Input ()],
             [sg.Txt('Peso'),sg.Input ()],
             [sg.Button('Enviar dados')]
         ]
         #Window
         window = sg.Window("Cadastro do Produto").layout(layout)

         #Data extraction
         self.button, self.values = window.read()

    def Start(self):
        print(self.values)

tela = TelaPython()
tela.Start()


