import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
         layout = [
             [sg.Txt('Produto',size=(10,0)),sg.Input (size=(38,0))],
             [sg.Txt('Conteúdo',size=(10,0)),sg.Input (size=(38,0))],
             [sg.Txt('Peso'),sg.Input ()],
             [sg.Txt('Qual o tipo do produto ?')],
             [sg.Checkbox('Liquido'),sg.Checkbox('Comprimido'),sg.Checkbox('Pó')],
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


