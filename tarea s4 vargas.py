# Tarea Asincrónica

# Clase Motor
class Motor:
    def __init__(self, tipo, potencia):
        self._tipo = tipo
        self._potencia = potencia

    # Property para tipo
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor

    # Property para potencia
    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, valor):
        self._potencia = valor

    # Metodo para encender el motor
    def encender_motor(self):
        print("Motor encendido")

    # Metodo para detener el motor
    def detener_motor(self):
        print("Motor detenido")

    # Metodo str para mostrar informacion
    def __str__(self):
        return f"Motor: {self._tipo},con potencia de:: {self._potencia} HP"


# Clase Vehiculo - Clase padre
class Vehiculo:
    def __init__(self, marca, modelo, anio, motor):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._motor = motor

    # Properties
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, valor):
        self._anio = valor

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    # Metodo para encender vehiculo
    def encender(self):
        print(f"{self._marca} {self._modelo} encendido")
        self._motor.encender_motor()

    # Metodo para apagar vehiculo
    def apagar(self):
        print(f"{self._marca} {self._modelo} apagado")
        self._motor.detener_motor()

    # Metodo str
    def __str__(self):
        return f"Vehiculo: {self._marca} {self._modelo} ({self._anio})\n{self._motor}"


# Clase Automovil - hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, motor, numero_puertas):
        super().__init__(marca, modelo, anio, motor)
        self._numero_puertas = numero_puertas

    @property
    def numero_puertas(self):
        return self._numero_puertas

    @numero_puertas.setter
    def numero_puertas(self, valor):
        self._numero_puertas = valor

    # Metodo para abrir maletero
    def abrir_maletero(self):
        print("Maletero abierto")

    # Metodo para tocar claxon
    def tocar_claxon(self):
        print("biP biP")

    # Sobrescribir str usando super
    def __str__(self):
        return f"Automovil:\n{super().__str__()}\nPuertas: {self._numero_puertas}"


# Clase Motocicleta - hereda de Vehiculo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, motor, cilindraje):
        super().__init__(marca, modelo, anio, motor)
        self._cilindraje = cilindraje

    @property
    def cilindraje(self):
        return self._cilindraje

    @cilindraje.setter
    def cilindraje(self, valor):
        self._cilindraje = valor

    # Metodo para hacer caballito
    def hacer_caballito(self):
        print("Haciendo caballito")

    # Metodo para usar patada de arranque
    def usar_patada_arranque(self):
        print("Usando patada de arranque")
        self._motor.encender_motor()

    # Sobrescribir str usando super
    def __str__(self):
        return f"Motocicleta:\n{super().__str__()}\nCilindraje: {self._cilindraje}cc"


# PROGRAMA PRINCIPAL
print("=" * 50)
print("SISTEMA DE GESTION DE VEHICULOS")
print("=" * 50)

# Crear motores
print("\nCreando motores...")
motor1 = Motor("Gasolina", 150)
motor2 = Motor("Diesel", 200)
motor3 = Motor("2 tiempos", 50)
motor4 = Motor("4 tiempos", 80)

# Crear 2 automoviles
print("\nCreando automoviles...")
auto1 = Automovil("Toyota", "Corolla", 2020, motor1, 4)
auto2 = Automovil("Nissan", "Versa", 2022, motor2, 4)

# Crear 2 motocicletas
print("Creando motocicletas...")
moto1 = Motocicleta("Yamaha", "R15", 2021, motor3, 150)
moto2 = Motocicleta("Honda", "CBR", 2023, motor4, 600)

# Probar automovil 1
print("\n" + "=" * 50)
print("PROBANDO AUTOMOVIL 1:")
print("=" * 50)
print(auto1)
print("\nAcciones:")
auto1.encender()
auto1.tocar_claxon()
auto1.abrir_maletero()
auto1.apagar()

# Probar automovil 2
print("\n" + "=" * 50)
print("PROBANDO AUTOMOVIL 2:")
print("=" * 50)
print(auto2)
print("\nAcciones:")
auto2.encender()
auto2.tocar_claxon()
auto2.apagar()

# Probar motocicleta 1
print("\n" + "=" * 50)
print("PROBANDO MOTOCICLETA 1:")
print("=" * 50)
print(moto1)
print("\nAcciones:")
moto1.encender()
moto1.hacer_caballito()
moto1.apagar()

# Probar motocicleta 2
print("\n" + "=" * 50)
print("PROBANDO MOTOCICLETA 2:")
print("=" * 50)
print(moto2)
print("\nAcciones:")
moto2.usar_patada_arranque()
moto2.hacer_caballito()
moto2.apagar()

print("\n" + "=" * 50)
print("PROGRAMA CULMINADO")
print("=" * 50)