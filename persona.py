
class Persona:
    '''
    Clase que permite crear un objeto de tipo Persona
    '''
    def __init__(self, cedula:str, nombre:str, email:str, genero:str = None
                 , ocupacion:str = None, edad:int = None):
        self._cedula = cedula
        self._email = email
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion
        self._edad = edad
        self._activo = True

if __name__ == '__main__':
    persona1 = {"nombre":"Carlos", "ocupacion":"Estudiante"}
    print(persona1["nombre"])
    print(type(persona1))

    print("*".center(80, "*"))

    persona2 = Persona(nombre = 'Carlos Perez', genero = 'H', ocupacion='Estudiante', edad=20,
                       cedula = '0987654312', email = 'cperez@mail.com', )
    print(persona2._nombre)

    print(type(persona2))
    print(f'Nombre: {persona2._nombre}')
    print(f'Cedula: {persona2._cedula}')
    print(f'Email: {persona2._email}')
    print(f'Ocupacion: {persona2._ocupacion}')

    print("*".center(80, "*"))

    persona4 = Persona('0987654321', 'Maria Perez', 'mperez@mail.com',
                       'M', 'Doctora', 30)
    print(f'Nombre: {persona4._nombre}')
    print(f'Cedula: {persona4._cedula}')
    print(f'Email: {persona4._email}')
    print(f'Ocupacion: {persona4._ocupacion}')

    print("*".center(80, "*"))

    persona5 = Persona(nombre='Luis Paz', genero = 'H', ocupacion='Ingeniero'
                       , edad='Veinticinco',
                       cedula = 1987654314, email = 'lperez@mail.com')
    print(f'Nombre: {persona5._nombre}')
    print(f'Cedula: {persona5._cedula}')
    print(f'Email: {persona5._email}')
    print(f'Ocupacion: {persona5._ocupacion}')
    print(f'Edad: {persona5._edad}')