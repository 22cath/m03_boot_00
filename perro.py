# definiendo la clase, class y  con el nombre con mayuscula y ():
# función init, con la clase vacia, self, definiendo el constructor, que nos permitira crear las instancias.

class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p

# definicion la función/metodo, e indicanco el primer parametro de la clase, por norma, self, ie la propia clase.
# defininiendo las funcionalidades de las diferentes instancias de nuestro objeto
    def ladrar(self):
        if self.peso>=8:
            print('GUAU, GUAU, GUAU')
        else:
            print('guau, guau')          
    
    def __str__(self):
        return 'Perro {}, e: {}, p: {}'.format(nombre, edad, peso)
        return 'soy el perro {}'.format(self.nombre)
               
# Subclase & Herencia
class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, pero, amo):
        Perro.__init__(self, nombre, edad, peso, amo)
        self.amo = amo
        
# Funcion para devolver una cadena cuando digamos PRINT

    def __str__(self):
        return 'Perro de asistencia de {}'.format(self.amo)
    
    

'''
    def __str__(self):
        return 'Perro {}, e: {}, p: {}'.format(nombre, edad, peso)
'''  
    
            
    
