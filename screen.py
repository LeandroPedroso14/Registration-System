import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
         layout = [
             [sg.Txt('Produto',size=(10,0)),sg.Input (size=(38,0),key='Produto')],
             [sg.Txt('Conteúdo',size=(10,0)),sg.Input (size=(38,0),key='Conteúdo')],
             [sg.Txt('Peso'),sg.Input ()],
             [sg.Txt('Qual o tipo do produto ?')],
             [sg.Checkbox('Liquido',key='liquido'),sg.Checkbox('Comprimido',key='comprimido'),sg.Checkbox('Pó',key='pó')],
             [sg.Button('Enviar dados')]
         ]
         #Window
         window = sg.Window("Cadastro do Produto").layout(layout)

         #Data extraction
         self.button, self.values = window.read()

    def Start(self):
        Produto = self.values['produto']
        Conteúdo = self.values['conteudo']
        Peso = self.values['peso']
        tipo_liquido = self.values['liquído']
        tipo_comprimido = self.values['comprimido']
        tipo_pó = self.values['pó']
        print(f'Prduto:{Produto}')
        print(f'Conteúdo:{Conteúdo}')
        print(f'Peso:{Peso}')
        print(f'tipo_liquido:{tipo_liquido}')
        print(f'tipo_comprimido:{tipo_comprimido}')
        print(f'tipo_pó:{tipo_pó}')
                    


tela = TelaPython()
tela.Start()


