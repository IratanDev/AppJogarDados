import random

class SimuladorDados:
    def __init__(self):
        self.mensagem = 'Jogar o dado? '
        self.valor_minimo = 1
        self.valor_maximo = 6

    def Inicio(self):
        resposta = (input(self.mensagem)).upper()
        while resposta != 'SIM' and resposta != 'NAO':
            resposta = (input('A resposta deve ser sim ou não. Jogar o dado? ')).upper()
        if resposta == 'SIM':
            self.GerarDado()
        else:
            print('Até a próxima!')

    def GerarDado(self):
        valor = random.randint(self.valor_minimo, self.valor_maximo)
        print(f'O dado vale {valor}.')
        return self.Inicio()
