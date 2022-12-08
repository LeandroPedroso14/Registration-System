import PySimpleGUI as sg

class TelaPython:
    def ___init___(self):
      #Layout
      layout = [
        [sg.Txt('Produto'),sg.Input ()],
        [sg.Txt('Peso'),sg.Input ()],
        [sg.Botton('Enviar dados')]
    ]
      #Window
      window = sg.Window("Cadastro do Produto").layout(layout)

      #Data extraction
      self.button, self.values = window.read()

    def Start(self):
        print(self.values)

tela = TelaPython()
tela.Start()


