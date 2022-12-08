import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
         layout = [
             [sg.Txt('Produto',size=(10,0)),sg.Input (size=(38,0),key='Produto')],
             [sg.Txt('Conteúdo',size=(10,0)),sg.Input (size=(38,0),key='Conteúdo')],
             [sg.Txt('Peso',size=(10,0)),sg.Input (size=(38,0),key='Peso')],
             [sg.Txt('Qual o tipo do produto ?')],
             [sg.Checkbox('Liquido',key='Liquído'),sg.Checkbox('Comprimido',key='Comprimido'),sg.Checkbox('Pó',key='Pó')],
             [sg.Button('Enviar dados')]
         ]
         #Window
         self.window = sg.Window("Cadastro do Produto").layout(layout)

         
         

    def Start(self):
        while True: #Data extraction
            self.button, self.values = self.window.read()
        Produto = self.values['Produto']
        Conteúdo = self.values['Conteúdo']
        Peso = self.values['Peso']
        tipo_liquido = self.values['Liquído']
        tipo_comprimido = self.values['Comprimido']
        tipo_pó = self.values['Pó']
        print(f'Prduto:{Produto}')
        print(f'Conteúdo:{Conteúdo}')
        print(f'Peso:{Peso}')
        print(f'tipo_liquido:{tipo_liquido}')
        print(f'tipo_comprimido:{tipo_comprimido}')
        print(f'tipo_pó:{tipo_pó}')
                    


tela = TelaPython()
tela.Start()


