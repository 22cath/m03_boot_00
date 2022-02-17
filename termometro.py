class Termometro():
    def __init__(self):
        self.unidadMedida = 'C'
        self.temperatura = 0
    
    def conversor(self, temperatura, unidad):
        if unidad == 'C'
            return '{}ºF'.format(temperatura*9/5 +32)
        elif unidad == 'F':
            return '{}ºF'.format(temperatura - 32 *5/)