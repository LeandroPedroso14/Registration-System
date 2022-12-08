import PySimpleGUI as sg

class TelaPython:
    def ___init___(self):
      #Layout
      layout = [
        [sg.Txt('Produto'),sg.Input ()],
        [sg.Txt('Peso'),sg.Input ()],
        [sg.Botton()]
    ]
      #Window
      window = sg.Window("Cadastro do Produto").layout(layout)

      #Data extraction
      self.button, self.values = window.read()

      def Iniciar(self):
        print(self.values)




