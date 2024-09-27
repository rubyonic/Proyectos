import random
import os
import time
import pygame
from colorama import Fore, Style, Back, init
init(autoreset=True)

minijuego = "sonidos/minijuego.mp3"
captura = "sonidos/captura.mp3"
safari = "sonidos/safari.mp3"
huir = "sonidos/huir.mp3"
atrapado = "sonidos/atrapado.mp3"
pygame.init()
pygame.mixer.init()


class Pokemon:
    def __init__(self, imagen, nombre, tipo, categoria, generacion, instalacion, area, alimentacion, cuidados):
        self.imagen = imagen
        self.nombre = nombre
        self.tipo = tipo
        self.categoria = categoria
        self.generacion = generacion
        self.instalacion = instalacion
        self.area = area
        self.alimentacion = alimentacion
        self.cuidados = cuidados

class Trabajador:
    def __init__(self, nombre, edad, zona_asignada):
        self.nombre = nombre
        self.edad = edad
        self.zona_asignada = zona_asignada

class Cliente:
    def __init__(self, nombre, es_entrenador):
        self.nombre = nombre
        self.es_entrenador = es_entrenador

def obtener_numero_entradas():
    while True:
        try:
            num_entradas = int(input("\t\t\t\t\t¿Cuántas entradas desea vender? "))
            if num_entradas <= 0:
                print("\t\t\t\t\tIngrese un número válido de entradas.")
            else:
                return num_entradas
        except ValueError:
            print("\t\t\t\t\tPor favor, ingrese un número válido.")

def calcular_precio_entrada(cliente):
    return 10 if cliente.es_entrenador else 15

def vender_entradas():
    global ganancias_totales
    num_entradas = obtener_numero_entradas()

    for _ in range(num_entradas):
        nombre_cliente = input("\t\t\t\t\tIntroduce el nombre del cliente: ")
        es_entrenador = input("\t\t\t\t\t¿Es entrenador Pokémon? Introduce S para Si, Enter se tomara como No: ").upper() == "S"
        cliente = Cliente(nombre_cliente, es_entrenador)
        precio_entrada = calcular_precio_entrada(cliente)
        ganancias_totales += precio_entrada
        lista_ventas.append((cliente, precio_entrada))
        print(f"\t\t\t\t\tVenta realizada a {cliente.nombre}. Precio de la entrada: €{precio_entrada}")
    
    return ganancias_totales

def mostrar_ventas():
    os.system("cls")
    print(clientes_imagen)
    print(Fore.LIGHTYELLOW_EX + f"\t\t\t\t\tGanancias totales: {ganancias_totales}€" + Fore.RESET)
    print("\n\t\t\t\t\tLista de clientes y si son entrenadores:")
    for venta in lista_ventas:
        cliente, precio = venta
        print(Fore.LIGHTMAGENTA_EX + f"\t\t\t\t\tCliente: {cliente.nombre}, Precio entrada: €{precio}, Entrenador: {'Sí' if cliente.es_entrenador else 'No'}" + Fore.RESET)
    input("\n\t\t\t\t\tPulsa ENTER para continuar.")

# Variables globales
ganancias_totales = 0
lista_ventas = []


class Instalaciones:
    def __init__(self, nombre, area, estado, pokemon_primera_generacion):
        self.nombre = nombre
        self.area = area
        self.estado = estado
        self.pokemon_primera_generacion = pokemon_primera_generacion
        self.trabajadores = []
        self.pokemon_atrapados = []
    
    def comprobar_estado_instalaciones(self, instalacion):
        # De que instalacion quieres comprobar el estado 1, 2, 3
        # Si esta sucio que lo limpie
        pass    

    def mostrar_pokemon_area(self, area):       
            pokemons_area = []
            for pokemon in self.pokemon_primera_generacion:
                if pokemon.instalacion == area:
                    pokemons_area.append(pokemon)
                    

            if pokemons_area:
                print(f"\t\t\t\t\tPokemon en {area}:")
                for pokemon in pokemons_area:
                    print(f"{pokemon.imagen}")
                    print(f"\t\t\t\t\tNombre: {pokemon.nombre}")
                    print(f"\t\t\t\t\tTipo: {pokemon.tipo}")
                    print(f"\t\t\t\t\tCategoría: {pokemon.categoria}")
                    print(f"\t\t\t\t\tGeneración: {pokemon.generacion}")
                    print(f"\t\t\t\t\tInstalación: {pokemon.instalacion}")
                    print(f"\t\t\t\t\tAlimentación: {pokemon.alimentacion}")
                    print(f"\t\t\t\t\tCuidados: {pokemon.cuidados}")
                    print("\t\t\t\t\t----------------------")
            else:
                print(f"\t\t\t\t\tNo hay Pokémon en el área {area}.")

    def mostrar_pokemon_por_numero_usuario(self):
        while True:
            numero = input("\t\t\t\t\tIntroduce el número del Pokémon que deseas ver.\n\t\t\t\t\t0. Para volver.\n\t\t\t\t\t-> ")
            os.system("cls")
            if numero == '0':
                break
            elif numero.isdigit():
                numero = int(numero)
                if 1 <= numero <= len(self.pokemon_primera_generacion):
                    pokemon = self.pokemon_primera_generacion[numero - 1]
                    os.system("cls")
                    print(buscar_imagen)
                    print(f"{pokemon.imagen}")
                    print(f"\t\t\t\t\tPokemon {numero}:")
                    print(f"\t\t\t\t\tNombre: {pokemon.nombre}")
                    print(f"\t\t\t\t\tTipo: {pokemon.tipo}")
                    print(f"\t\t\t\t\tCategoría: {pokemon.categoria}")
                    print(f"\t\t\t\t\tGeneración: {pokemon.generacion}")
                    print(f"\t\t\t\t\tInstalación: {pokemon.instalacion}")
                    print(f"\t\t\t\t\tAlimentación: {pokemon.alimentacion}")
                    print(f"\t\t\t\t\tCuidados: {pokemon.cuidados}")
                    print("\t\t\t\t\t----------------------")
                else:
                    print("\t\t\t\t\tNúmero de Pokémon no válido.")
                    input("\t\t\t\t\tPulsa ENTER para continuar.")
                    os.system("cls")
            else:
                print("\t\t\t\t\tPor favor, introduce un número válido.")
                input("\t\t\t\t\tPulsa ENTER para continuar.")
                os.system("cls")

    def agregar_trabajador(self, nombre, edad, zona_asignada):
        trabajador = Trabajador(nombre, edad, zona_asignada)
        self.trabajadores.append(trabajador)

    def mostrar_trabajadores(self, zona):
        for i, trabajador in enumerate(self.trabajadores, start=1):
            if trabajador.zona_asignada == zona:
                print(f"\t\t\t\t\t{i}. Nombre: {trabajador.nombre}, Edad: {trabajador.edad}")
        if not self.trabajadores:
            print("\t\t\t\t\tNo hay trabajadores en esta zona.")

    def modificar_trabajador(self, zona, numero_trabajador, nuevo_nombre, nueva_edad):
        if self.area == zona:
            if 1 <= numero_trabajador <= len(self.trabajadores):
                trabajador = self.trabajadores[numero_trabajador - 1]
                trabajador.nombre = nuevo_nombre
                trabajador.edad = nueva_edad
                print("\t\t\t\t\tTrabajador modificado exitosamente.")
            else:
                print("\t\t\t\t\tNúmero de trabajador no válido.")
        else:
            print("\t\t\t\t\tZona no válida.")

    def eliminar_trabajador(self, zona, numero_trabajador):
        if self.area == zona:
            if 1 <= numero_trabajador <= len(self.trabajadores):
                self.trabajadores.pop(numero_trabajador - 1)
                print("\t\t\t\t\tTrabajador eliminado exitosamente.")
            else:
                print("\t\t\t\t\tNúmero de trabajador no válido.")
        else:
            print("\t\t\t\t\tZona no válida.")
          
    def atrapar_pokemon(self, area):
        os.system("cls")
        pokemons_disponibles = self.pokemon_disponibles_en_area(area)
        if not pokemons_disponibles:
            print(f"\t\t\t\t\tNo quedan Pokémon en el área {area}!")
            input("\t\t\t\t\tPulsa ENTER para continuar.")
            return
        pygame.mixer.music.load(captura)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)
        print("\t\t\t\t\t¡Un Pokémon salvaje apareció!")
        pokemon_aleatorio = random.choice(pokemons_disponibles)
        while True:
            print(atrapalo_imagen)
            print(f"{pokemon_aleatorio.imagen}")
            print(f"\t\t\t\t\tNombre: {pokemon_aleatorio.nombre}")
            print(f"\t\t\t\t\tTipo: {pokemon_aleatorio.tipo}")
            print(f"\t\t\t\t\t¡Intenta atraparlo!")
            opcion = input("\t\t\t\t\tSelecciona una opción:\n\t\t\t\t\t1. Tirar piedra\n\t\t\t\t\t2. Tirar pokeball\n\t\t\t\t\t3. Huir\n\t\t\t\t\t-> ")
            probabilidad_huir = 0.5
            probabilidad_captura = 0.6
            if opcion == '1':
                probabilidad_huir += 0.1
                probabilidad_captura = +0.2
                if random.uniform(0, 1) < probabilidad_huir:
                    for letra in conver_captura:
                            print(letra, end="", flush=True)
                            time.sleep(0.1)
                    pygame.mixer.music.load(huir)
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.5)
                    print("\t\t\t\t\t¡El Pokémon se asustó y huyó!")
                    input("\t\t\t\t\tPulsa ENTER para continuar.")
                    os.system("cls")
                    break
                else:
                    for letra in conver_captura:
                            print(letra, end="", flush=True)
                            time.sleep(0.1)                    
                    print("\t\t\t\t\tEl Pokémon parece enfadado...")
                    input("\t\t\t\t\tPulsa ENTER para continuar.")
                    os.system("cls")
            elif opcion == '2':
                if random.uniform(0, 1) < probabilidad_huir:
                    for letra in conver_captura:
                            print(letra, end="", flush=True)
                            time.sleep(0.1)
                    print("\t\t\t\t\t¡El Pokémon se escapo y huyó!")
                    pygame.mixer.music.load(huir)
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.5)
                    input("\t\t\t\t\tPulsa ENTER para continuar.")
                    os.system("cls")
                    break
                elif random.uniform(0, 1) < probabilidad_captura:
                    for letra in conver_captura:
                            print(letra, end="", flush=True)
                            time.sleep(0.1)
                    pygame.mixer.music.load(atrapado)
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.5)
                    print("\t\t\t\t\t¡Has atrapado al Pokémon!")
                    self.pokemon_atrapados.append(pokemon_aleatorio)
                    input("\t\t\t\t\tPulsa ENTER para continuar.")
                    os.system("cls")
                    break
                else:
                    for letra in conver_captura:
                            print(letra, end="", flush=True)
                            time.sleep(0.1)
                    print("\t\t\t\t\t¡El Pokémon se escapó de la pokeball!")
                    input("\t\t\t\t\tPulsa ENTER para continuar.")
                    os.system("cls")
            elif opcion == '3':
                print("\t\t\t\t\tHas huido del Pokémon salvaje.")
                pygame.mixer.music.load(huir)
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.5)
                input("\t\t\t\t\tPulsa ENTER para continuar.")
                os.system("cls")
                break
            else:
                print("\t\t\t\t\tOpción no válida. Inténtalo de nuevo.")
                input("\t\t\t\t\tPulsa ENTER para continuar.")
                os.system("cls")

    def pokemon_disponibles_en_area(self, area):
        pokemons_disponibles = [pokemon for pokemon in self.pokemon_primera_generacion if pokemon.area == area]
        pokemons_no_atrapados = [pokemon for pokemon in pokemons_disponibles if pokemon not in self.pokemon_atrapados]
        return pokemons_no_atrapados

    def agregar_pokemon_atrapado(self, pokemon):
            self.pokemon_atrapados.append(pokemon)

    def mostrar_pokemon_atrapados(self):
        os.system("cls")
        print(pokedex_imagen)
        print("\t\t\t\t\tPokémon atrapados:")
        nombres_pokemon_atrapados = {pokemon.nombre for pokemon in self.pokemon_atrapados}
        contador = 1
        for pokemon in pokemon_primera_generacion:
            if pokemon.nombre in nombres_pokemon_atrapados:
                print(f"\t\t\t\t\t{contador}. {pokemon.nombre}")
            else:
                print(f"\t\t\t\t\t{contador}. ???")
            contador += 1
        input("\t\t\t\t\tPulsa ENTER para continuar.")
        os.system("cls")
        if len(self.pokemon_atrapados) == 151:
            print("¡Felicidades! Has atrapado a los 151 Pokémon.")
        
def agregar_trabajador(instalacion):
    nombre = input("\t\t\t\t\tIntroduzca el nombre del trabajador: ")
    while True:
        edad_input = input("\t\t\t\t\tIntroduzca la edad del trabajador: ")
        if edad_input.isdigit():
            edad = int(edad_input)
            break
        else:
            print("\t\t\t\t\tPor favor, introduzca un número entero para la edad.")
    zona_asignada = instalacion.area
    trabajador = Trabajador(nombre, edad, zona_asignada)
    instalacion.trabajadores.append(trabajador)

AREAS = ["Bosque", "Cueva", "Pradera", "Volcán", "Cementerio", "Mar", "Ciudad", "Río", "Montaña"]  

conver_captura = """\t\t\t\t\t1...2...3...
"""

logo=("""
\t\t\t\t"""+ Fore.RED +"●"+Fore.LIGHTYELLOW_EX+"""═════════════════════════════════════════════════════════════════════════════════════════════════"""+ Fore.RED +"●"+Fore.LIGHTYELLOW_EX+"""
\t\t\t\t║\t     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄         ║
\t\t\t\t║\t    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌        ║
\t\t\t\t║\t    ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀         ║
\t\t\t\t║\t    ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌             ║
\t\t\t\t║\t    ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌             ║
\t\t\t\t║\t    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌             ║
\t\t\t\t║\t     ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀      ▐░▌             ║
\t\t\t\t║\t              ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌     ▐░▌       ▐░▌             ║
\t\t\t\t║\t     ▄▄▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌      ▐░▌  ▄▄▄▄█░█▄▄▄▄         ║
\t\t\t\t║\t    ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌        ║
\t\t\t\t║\t     ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀            ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀         ║
\t\t\t\t║\t                                                                                          ║
\t\t\t\t║\t ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄     ║
\t\t\t\t║\t▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌    ║
\t\t\t\t║\t▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌    ║
\t\t\t\t║\t▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌  ▐░▌          ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌    ║
\t\t\t\t║\t▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▐░▌ ▐░▌▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌    ║
\t\t\t\t║\t▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░▌    ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌    ║
\t\t\t\t║\t▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░▌░▌   ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▀   ▐░▌▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌    ║
\t\t\t\t║\t▐░▌          ▐░▌       ▐░▌▐░▌▐░▌  ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌    ║
\t\t\t\t║\t▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌    ║
\t\t\t\t║\t▐░▌          ▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌    ║
\t\t\t\t║\t ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀     ║
\t\t\t\t"""+ Fore.RED +"●"+Fore.LIGHTYELLOW_EX+"""═════════════════════════════════════════════════════════════════════════════════════════════════"""+ Fore.RED +"●"+Fore.LIGHTYELLOW_EX+"""
\t\t\t\t║\t                                                                                          ║
\t\t\t\t║\t\t\t\t\t"""+ Fore.LIGHTMAGENTA_EX + "1. Θ Ver los Pokémon" +Fore.LIGHTYELLOW_EX + """                                      ║  
\t\t\t\t║\t\t\t\t\t"""+ Fore.LIGHTGREEN_EX + "2. ☻ Empleados" +Fore.LIGHTYELLOW_EX + """                                            ║
\t\t\t\t║\t\t\t\t\t"""+ Fore.LIGHTYELLOW_EX + "3. ▓ Entradas" +Fore.LIGHTYELLOW_EX + """                                             ║
\t\t\t\t║\t\t\t\t\t"""+ Fore.LIGHTCYAN_EX +"4. ♫ Minijuego" +Fore.LIGHTYELLOW_EX + """                                            ║
\t\t\t\t║\t\t\t\t\t                                                          ║
\t\t\t\t║\t\t\t\t\t"""+ Fore.LIGHTRED_EX + "0. ╚>Salir" + Fore.LIGHTYELLOW_EX + """                                                ║
\t\t\t\t║\t                                                                                          ║
\t\t\t\t╚═════════════════════════════════════════════════════════════════════════════════════════════════╝
"""+Fore.RESET)
buscar_imagen = (Fore.LIGHTYELLOW_EX+"""
\t\t\t\t\t ▄               ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄     ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄                             
\t\t\t\t\t▐░▌             ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌   ▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                            
\t\t\t\t\t ▐░▌           ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌   ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀                            
\t\t\t\t\t  ▐░▌         ▐░▌  ▐░▌          ▐░▌       ▐░▌   ▐░▌          ▐░▌       ▐░▌▐░▌                                     
\t\t\t\t\t   ▐░▌       ▐░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌   ▐░▌          ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄                            
\t\t\t\t\t    ▐░▌     ▐░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌   ▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌                            
\t\t\t\t\t     ▐░▌   ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀    ▐░▌          ▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌                            
\t\t\t\t\t      ▐░▌ ▐░▌      ▐░▌          ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌          ▐░▌                            
\t\t\t\t\t       ▐░▐░▌       ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌    ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌                            
\t\t\t\t\t        ▐░▌        ▐░░░░░░░░░░░▌▐░▌       ▐░▌   ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                            
\t\t\t\t\t         ▀          ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀     ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                              
\t\t\t\t\t ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄ 
\t\t\t\t\t▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌
\t\t\t\t\t▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌
\t\t\t\t\t▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌  ▐░▌          ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌
\t\t\t\t\t▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▐░▌ ▐░▌▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌ 
\t\t\t\t\t▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░▌    ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌
\t\t\t\t\t▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░▌░▌   ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▀   ▐░▌▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌
\t\t\t\t\t▐░▌          ▐░▌       ▐░▌▐░▌▐░▌  ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌
\t\t\t\t\t▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌
\t\t\t\t\t▐░▌          ▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌  
\t\t\t\t\t ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀      
"""+Fore.RESET)

pokedex_imagen = (Fore.LIGHTYELLOW_EX+"""
\t\t\t\t\t ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄ 
\t\t\t\t\t▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌     ▐░▌
\t\t\t\t\t▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▐░▌   ▐░▌
\t\t\t\t\t▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌  ▐░▌          ▐░▌       ▐░▌▐░▌            ▐░▌ ▐░▌
\t\t\t\t\t▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄    ▐░▐░▌
\t\t\t\t\t▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░▌    ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌    ▐░▌
\t\t\t\t\t▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░▌░▌   ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀    ▐░▌░▌
\t\t\t\t\t▐░▌          ▐░▌       ▐░▌▐░▌▐░▌  ▐░▌          ▐░▌       ▐░▌▐░▌            ▐░▌ ▐░▌
\t\t\t\t\t▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄  ▐░▌   ▐░▌
\t\t\t\t\t▐░▌          ▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌     ▐░▌
\t\t\t\t\t ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀                                                                           
"""+Fore.RESET)

atrapalo_imagen = (Fore.LIGHTYELLOW_EX+""" 
\t\t\t\t\t ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄ 
\t\t\t\t\t▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌
\t\t\t\t\t▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░▌
\t\t\t\t\t▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌
\t\t\t\t\t▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌       ▐░▌▐░▌
\t\t\t\t\t▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌▐░▌
\t\t\t\t\t▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░▌       ▐░▌▐░▌ 
\t\t\t\t\t▐░▌       ▐░▌     ▐░▌     ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌ ▀  
\t\t\t\t\t▐░▌       ▐░▌     ▐░▌     ▐░▌      ▐░▌ ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌ ▄  
\t\t\t\t\t▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌
\t\t\t\t\t ▀         ▀       ▀       ▀         ▀  ▀         ▀  ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀ 
"""+Fore.RESET)

minijuego_imagen = (Fore.LIGHTYELLOW_EX+"""
\t\t\t\t\t ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
\t\t\t\t\t▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌  
\t\t\t\t\t▐░▌░▌   ▐░▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌ ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀▀█░█▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
\t\t\t\t\t▐░▌▐░▌ ▐░▌▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌     ▐░▌           ▐░▌    ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌
\t\t\t\t\t▐░▌ ▐░▐░▌ ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌     ▐░▌           ▐░▌    ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌
\t\t\t\t\t▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌     ▐░▌           ▐░▌    ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌▐░░░░░░░░▌▐░▌       ▐░▌
\t\t\t\t\t▐░▌   ▀   ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌     ▐░▌           ▐░▌    ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌ ▀▀▀▀▀▀█░▌▐░▌       ▐░▌
\t\t\t\t\t▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌     ▐░▌           ▐░▌    ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌
\t\t\t\t\t▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌ ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄█░▌    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ 
\t\t\t\t\t▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
\t\t\t\t\t ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀      ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀   
                                                                               """+Fore.RESET)

clientes_imagen = (Fore.LIGHTYELLOW_EX+"""
\t\t\t\t\t ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
\t\t\t\t\t▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ 
\t\t\t\t\t▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
\t\t\t\t\t▐░▌          ▐░▌▐░▌    ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌         
\t\t\t\t\t▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄  
\t\t\t\t\t▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌  
\t\t\t\t\t▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌     ▐░▌     ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌ 
\t\t\t\t\t▐░▌          ▐░▌    ▐░▌▐░▌     ▐░▌     ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌
\t\t\t\t\t▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌     ▐░▌     ▐░▌      ▐░▌ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌ 
\t\t\t\t\t▐░░░░░░░░░░░▌▐░▌      ▐░░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌
\t\t\t\t\t ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀       ▀       ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀   ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀                                               
"""+Fore.RESET)


empleados_imagen = (Fore.LIGHTYELLOW_EX+"""
\t\t\t\t\t ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
\t\t\t\t\t▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ 
\t\t\t\t\t▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀    
\t\t\t\t\t▐░▌          ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
\t\t\t\t\t▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄  
\t\t\t\t\t▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌ 
\t\t\t\t\t▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌  
\t\t\t\t\t▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌   
\t\t\t\t\t▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌ 
\t\t\t\t\t▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌  
\t\t\t\t\t ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
"""+Fore.RESET)


pokemon_primera_generacion = [
            Pokemon(Fore.GREEN+"""\t\t\t\t\t                                 ▒██▒       
\t\t\t\t\t                      ████████▒▒▒▒▒▒█▓      
\t\t\t\t\t                  █▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓█      
\t\t\t\t\t                 ▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▓▓      
\t\t\t\t\t      █▒▒▒█░░░░░▒▒▒█▒▒░░▒▒▒▒▒▒▒▒▒▒▒▓▒▒█     
\t\t\t\t\t      ▒░░░░░░░█▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒█    
\t\t\t\t\t     ▒▒░░░█▓▓▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒█▒▒█   
\t\t\t\t\t    ▒░▒▒▒█▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▓▓▓▓▓▓▓▓▒▒▒   
\t\t\t\t\t   ▓░▓▒▒▒▒▒▒▒▒▒▒▓░▒░▓▓█▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓  
\t\t\t\t\t   ▓░▓▒▒▒▒▒▓▓░▒▒░▒░▓▒ ▓▓▒▒▒█▒▓▓▒▓▒▒▒▓▓▒▒▒▒  
\t\t\t\t\t  ▓ ░▓▒▒▒▒▒▒▒▒▒▒▒  █▓ ▓▓▒▒▒▒▒▒▓▓▓▓▒█▓▒▒▒▒█  
\t\t\t\t\t  ▒▒▒▓░▒▒▒▒▒▒▒▒▒▒   ▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓   
\t\t\t\t\t   ▒█▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒███    
\t\t\t\t\t     █▒█▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█     
\t\t\t\t\t       ▒█▒▒█▒▒▒▒▓▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒█▓▒▒▒     
\t\t\t\t\t      ▒▒▒█▒▒▓▓▓▒▒▓▓▓▒█▒▒▓▒▒▒▒▒▒▓▓▓▓▒▒▒█    
\t\t\t\t\t       █▒▒▓▒▒▒▒█▒▒▒▒▒▓▒▒█▒▒▒▒▒▓▒▒█▓▓▒▒▒█    
\t\t\t\t\t        █▒▒▒▒▒▒▒  █▓▓▓▓▓▒▒▒▒▒▓█▒▒▒▒▒▒▒▒█    
\t\t\t\t\t         ▒▒▒▒▒▒    █ ▒▓▒▒▒▒▒█  ▒▒▒▒▒▒▒█     
\t\t\t\t\t                    ▓█ █▓▒█      ████       """+ Fore.RESET,"Bulbasaur", "Planta", "Semilla", "Primera", "Zona 1", "Bosque", "Hierbas", "Exposición a la luz solar"),
            Pokemon(Fore.GREEN+"""\t\t\t\t\t                        ░                                
\t\t\t\t\t                    ███ █▒▒▒▒▒                           
\t\t\t\t\t                    ░░▒▒█▒▒▒▒▒▒▒       ▒▒▒▒█             
\t\t\t\t\t                   ▒░▒▓▒▒▒▒▒▒▒▒▒▒▒  ▒▒ ▒▒▒▒█▒▒█          
\t\t\t\t\t                  ▓░▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒█▒▒▒▒▒▒▒▒▒▒           
\t\t\t\t\t                  ▒▒▒▒▓▒▒▒▒▒▒▒▒▒█▓▓▒▒▒▒▒▓▒▒▒▒▒▒          
\t\t\t\t\t      ▒▒▒ ███    ▓▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▓▒▒▒▒▒▒▒▒▒█             
\t\t\t\t\t     ▒█▒▒▒ ▒▒▒ ▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▓▒▒▒▒▒▒▒            
\t\t\t\t\t   ▒█ ▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░░░▓▓▓█▒▒▒       
\t\t\t\t\t   █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒█      
\t\t\t\t\t   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒█▓▓▒▒▒▒█▓▒▒▒▒▒▓▓▒▒▒▒▒▒     
\t\t\t\t\t    ▓ ▒▒▒▒▒▒▒▒▒▒▒▒█▓▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒█ ▒▒█▓▒▒▒▒▒▒▒▒▒▒▓    
\t\t\t\t\t      ▓█▒▒▒▒▒▒▒▒▒▒▒██▓▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒  ▓▒▒▓▒▒▒▒▒▒▒▒▒▓    
\t\t\t\t\t         ██ ▓▒▒▒▒▒▓▓▓▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   
\t\t\t\t\t                ▓█▓▒▒▓▒▒█▓▓▒▒▒▒▒▒▒▒▒▒▒█░░▒▒▒▒▒▒▒▒▒▓▒██   
\t\t\t\t\t            █▒▒▒▒▓▓▓▓▓▓▓▓█▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     
\t\t\t\t\t         ▒▒▒▒▒▒▒▒▓█░▒▒▓▓▓▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t        ▒█▒▒▒▒▓▒▓▒░▒▒▓▓▓▓░▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t        █▒ ▒▒█ ▓█▒▒██▒▒▒▒▒▒░░░▒▒▒▒▒▒▓█▒▒▒▒█▓▓▓▓▓         
\t\t\t\t\t                ▒▒▒▒▒▒▒▒▒▒█░░▒█▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓█▓▒        
\t\t\t\t\t               ▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▓▓▓▓█▒█▓▓▓▓█▒▓▓▒▓▓▓        
\t\t\t\t\t               ▓▓▓▒▒▒▒▓▓▓▓▓▒▒▒▒█▓▓█▒▒▒▒ █▓▓▓▒▓▒▓▓█       
\t\t\t\t\t              ██▓▒▒▓▓▒▒█▓▓▓▓▒▒▒▓▒▒▒▒▒    ▓▓▓▒▒▒▒▒█       
\t\t\t\t\t              █▒▒▒▒▓▓▒     ██▒▒▓▒▒▒▒▒     ▓▒▒▒▒▒▒█       
\t\t\t\t\t               ▓▓▒▒▒▓█       █▒▒▒▒▒▒▒█     █▒░░░░▓█      
\t\t\t\t\t                               ██░ █░                    """+ Fore.RESET,"Ivysaur", "Planta", "Semilla", "Primera", "Zona 1", "Bosque", "Hierbas", "Exposición a la luz solar"),
            Pokemon(Fore.GREEN+"""\t\t\t\t\t                  █▒░▒▒▒▒▒▒██ ▒▒▒▒░░▒▓                   
\t\t\t\t\t              ▒░░░▒▒▒▒▒▒██░▓░▒█░▒▒█▒░▒▒▓█                
\t\t\t\t\t          █▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒░░░▒▒▒█▒▒░░░▒▒           
\t\t\t\t\t         ▒▒▒▒▓█▒▒▒░░░▒▒░░░▒████▒▒▒▒▒▒░░▒▒▒█▒▒▒▒█         
\t\t\t\t\t         ▒█ █▒▒▒▒▒▒░▒▒▒▒ ███████ ▒▒▒▒▒▒▒▒▒▒▒▒█▒▒         
\t\t\t\t\t           █▒▒▒▒▒▒▒▒▒▓  ██▓██████  ▒▒░░▒▒▒▒▒▒▒           
\t\t\t\t\t               █▒▒▒▒▓  ▓▓▓▓▓▓▓▓▓▓   ▒▒▒▒▒▒▒█             
\t\t\t\t\t             ██▓▓███▓▓▓▓██▓▓▓█▓█▓▓▓▓▒▒███                
\t\t\t\t\t       █▒▒▒▓▒▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓██▓▓████▓▓▓▒▓▒▓▓█       
\t\t\t\t\t   ▒▒▒▒▒▒▓▒▓▓▓▓▓▒▒▒▒▒█▒█▓▒▓▓█▓▒▒▓▒▓▒▒▒▒█▒▓▓█▓▓▓▒▒▒▒▒     
\t\t\t\t\t  █▒▒▒▒▒▓▓▒▓▓▓▓██▓▓▒▒▒▓▓▒▓▓▓▓▓▓▒▓▒█▒▒▓▓█▓█▓▓▓▓▒▓▓▒▒▒█▒▒▓ 
\t\t\t\t\t ██▒▒▓▒▒▓▒█▓▓▓█▓▓▒▒▒▒▒▒▒██▒▒▒▒▓▓▓▒▒▒▒▒▒█▓▓▓██▓▓█▒ ▒▒▒▒▒  
\t\t\t\t\t        ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▒▒▓▒▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓█       
\t\t\t\t\t       ▓▓▓▓█▓▓▒▒▒▒▒░▒▒▒▒▒▒▒▓▒▒▒▒▒▒▓▒ █▒▒▒▒▓▓▓▓▓▓▓▓█      
\t\t\t\t\t       ▓▓▓▓▒▒▓▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓      
\t\t\t\t\t       ▓▓▓▓▓▓▓▓▒▒▒▒░█▓▒▒▒▒▒▒▒▒▒▒▒█▓▓░▒▓▒▒▓▓▓▓▓▓▓▓▓▓      
\t\t\t\t\t        ▓▓▓▓▓▓▓▓▓▓▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓       
\t\t\t\t\t        █▓▓▓▓▓▒▓▓▓▓▓▒▓█▒▒▒▒▒▒▒▒▒▒░▓▒█▓▓▓▓▓▓▓▓▓▓▓▓        
\t\t\t\t\t           ▒ ▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓█▒█▓▓▓▓▓▓▓▓▓█▒█          
\t\t\t\t\t               ▓▓▓▓▓▓▓           ▓▓▓▓▓▓▓▓▓▓▓             
\t\t\t\t\t               ███░▓█▓           ▓▓▓▓▓▓▓▓▓               
\t\t\t\t\t                                ░ ▓░░▓▓░█                """+ Fore.RESET,"Venusaur", "Planta", "Semilla", "Primera", "Zona 1", "Bosque", "Hierbas", "Exposición a la luz solar"),
            Pokemon(Fore.RED+"""\t\t\t\t\t                 ▓░▒░▒█                                  
\t\t\t\t\t             █░░░░░▒▒▒░▒▒                                
\t\t\t\t\t            ░░░░░░░▒▒▒░░▒▒█                              
\t\t\t\t\t           ░▒░▒▒▒░░░▒▒░▒▓▒▒                              
\t\t\t\t\t          ██░▒▒▒▒░░▒▒▒▒█ █▒▒                             
\t\t\t\t\t          █░▒▒▒▒░░░▒▒░░█░██▒                             
\t\t\t\t\t          ▓█░░▒▒▒▒░░▒▒░███▓▒▒                            
\t\t\t\t\t          ▒▓░▒▒▒░░░░░░▒▒▒▒▒▒▒                            
\t\t\t\t\t         ▓░░░░▒▒░▒▒▒░░░░▒▒▒▒▒                  ▓         
\t\t\t\t\t          ▒▒█▒▒▒▒▒▒▒▒▓▓▒▒█▒▒                   ▒▒        
\t\t\t\t\t           █▒▒▓▒▒▒▒▒▒▒▒░▒▒▒█                 ░ ▒▒        
\t\t\t\t\t              █▒▒█░▒▒▓▒▒▒▒▒                 ░░▒▒░▓       
\t\t\t\t\t               █▒▒▒▒▒▒▒▒▒▒▒░░░█             ▒▒▒▒▒▒▒      
\t\t\t\t\t           █░░░▒░░▒░░░░▒▒░▒░░░░░▒▒░██░      ░▒▒▒▒░░      
\t\t\t\t\t      █▒▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒░▒▒░▒▒▒▒    ░░░▒▒░░▓░     
\t\t\t\t\t        ▒▒▒▒▒░▒▒░░░░░░░░░░▒▒░░░▒▒▒▓█▒█     ░░░░░░▒▒      
\t\t\t\t\t        █       ░░░░░░░░░░░░▒▒▒             ▓░░░▒▒▓      
\t\t\t\t\t               █░░░░░░░░░░░░▒▒▒░               ▒         
\t\t\t\t\t               ░░░░░░░░░░░░░▒░░░░             ░░         
\t\t\t\t\t               █░░░░░░░░░░░░░░░░░▒█          ▒▒█         
\t\t\t\t\t             ░░░░░░░░░░░░░░░▒░░░░▒▒█       ▒▒▒▓          
\t\t\t\t\t            ░░░░░░░░░░░░░░░▒░░░░░░░▒█▒▒▒▒▒▒▒▒░           
\t\t\t\t\t           ░░░▒▒▒▒░░░░░░░░░█░░░▒░▒▒▒▒▒▒▒▒▒▒█░            
\t\t\t\t\t           ▒▒▒▒▒▒▒▒▒▓░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒█▒▒              
\t\t\t\t\t           █▒▒▒▒▒▒▒▒█      ██▒▒▒▒▒▒▒▒▒█                  
\t\t\t\t\t          ██▒▒▒▒▒▒▒            ▒▒▒▒▒▒█                   
\t\t\t\t\t        █ ░█░█                 █▒▒▒▒░█░█                 
\t\t\t\t\t                                  █░ ██                  """+Fore.RESET,"Charmander", "Fuego", "Lagartija", "Primera", "Zona 3", "Volcán", "Bayas y pequeños roedores", "Entorno cálido"),
            Pokemon(Fore.RED+"""\t\t\t\t\t                          █▒▒█                           
\t\t\t\t\t                       █▒▒▒▒█                            
\t\t\t\t\t                  █▒▒▒▒▒▒▒▒                              
\t\t\t\t\t                ▓▒▒▒▒▒▒▒▒▒▒█                             
\t\t\t\t\t              █▒▒▒▒▒▒▒▒▒▒▒▒▒█                            
\t\t\t\t\t               ▒▒▒▒▒▒▒░░▒▒▒▒▒                            
\t\t\t\t\t               █▒▒▒▒██▒░▒▒▒▒▒▓                           
\t\t\t\t\t              ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒                            
\t\t\t\t\t             █▒▒▒▒▒▒▓▒▒▒▓▓▒▓                             
\t\t\t\t\t               ▓█▒▓▓▒▒▓▓▓▓▓             ▓▒               
\t\t\t\t\t                     █▒▓▓▒▒█             ▓▒▒▓            
\t\t\t\t\t                    ▒▒▒▒▒▒▒▒█             ▒▒▓▒▓          
\t\t\t\t\t                █▒▒▒▒░░░▒▒▒▒▒▒▒▒         ▓▓▒▒░▒▒         
\t\t\t\t\t            ▒▒▒▒▒▒█░░░░░░▒▒▒▒█▒▒▒▒▒▒      ▓▒░░░▒░▒       
\t\t\t\t\t          ▓▒▒▒▒   ▒░░░░░░░▒▒▒▒▒   ▒▒▒█    ░░░░▒▒░▒       
\t\t\t\t\t        █▒▒▒▒▒    ░░░░░░░░▒▒▒▒▒▒  ▒▒▒▒█   ▓▒░░░▒▒░▒      
\t\t\t\t\t       ▒▒▒░░▒    ░░░░░░░░░█▒▒▒▒▒█ ▒▒▒▒▒    ▒░░░░▒        
\t\t\t\t\t      █░░█░      ░░░░░░░░░░▒▒▒▒▒▒ ▒▒▒▒▒▒    ▓░░░▓        
\t\t\t\t\t      █░░        ░░░░░░░░░▒▒▒▒▒▒▒█ ░▒░░▒█     ▒          
\t\t\t\t\t               ▓▒▒░░░░░░░▒▒▒▒▒▒▒▒▒█▓ ░░░    █▒▒          
\t\t\t\t\t             █▒▒▒▒▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▓█   █▒▒▓░           
\t\t\t\t\t            ▒▒▒▒▒▒▓▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓█            
\t\t\t\t\t            ▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒████▓▒▒█              
\t\t\t\t\t             ▒▓▓▓▒▓▒       ▒▒▒▒▒▒▒▒█▒██                  
\t\t\t\t\t             ▒▒▓▓▓▒▒         ▒▒▒▒▒▒▒                     
\t\t\t\t\t          ██░█▒▒▒▒█          ▒▒▒▒▒▒▒                     
\t\t\t\t\t          ▒ ░█             █░█▒░█▒░▒                     """+Fore.RESET,"Charmeleon", "Fuego", "Llama", "Primera", "Zona 3", "Volcán", "Bayas y pequeños roedores", "Entorno cálido"),
            Pokemon(Fore.RED+"""\t\t\t\t\t                     ░░▒▒█                               
\t\t\t\t\t                 ▒█  ▒▒▒▒█▒▒▒▒█                          
\t\t\t\t\t           █▒▒▒▒▒     ▒▒▒▒▒▒▒▒▒▒▒█         ▒█            
\t\t\t\t\t         ▒▒█▓▒▒▓▒       ▒▒▒▒▒▒▒             ▒█           
\t\t\t\t\t      ▒▓▒▒▒▒▒▒▓██▒         █▒▒▒            █▓▓▓▒▒        
\t\t\t\t\t    █▒▒▒▒▒▒▒▒▒▓▒▓▒         █▒▒▒▒          ▒▓▓▓▓▓▓▒       
\t\t\t\t\t    ▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒         ▒▒▒▒         ▒▓▓▓▓▓▒▒▓▒▒     
\t\t\t\t\t  ██▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒█     ▒▒▒▒▒       ▒▓▓▓▓▓▓▓▒▒▒▒▓▒   
\t\t\t\t\t  ▓▓▓▓      ▒▒▓▓▓▓▓▓▓▓▓▓▒▒█ ▒▒▒▒▒ ▒▒▒▒▓▓▓▓▒▒▒▓▓▓▒▒▒▒▒▓▓  
\t\t\t\t\t █▓▓         ▓▓▓▓█ █▓▓▓▓█░▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▒▒█▓▓█ ▓▒▒▓▓█  
\t\t\t\t\t  ▓           ▓    ▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒  █▒▓▓   ▒▒▓▓▓▓  
\t\t\t\t\t  ▓             ▒▒▒█   █▒▒▒░░░░░░▓▒▓    ▒▒  ▓    ▒░  ▓▓  
\t\t\t\t\t               ▒ ▒▒▒   ▒▒▒░░░░░░░░░▒   ░▒▒▒▒▒    ░▒░  ▓  
\t\t\t\t\t                 █ █ █▒▒▒░░░░░░░░░░░▓     ▒     ░░░   ▒  
\t\t\t\t\t                    ▒▒▒▒░░░░░░░░░░░░░           ░▒░▒▒    
\t\t\t\t\t           █▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░▒▓         ░░░░▓    
\t\t\t\t\t         ▒▒▒▒▒▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░░▓▒▒▒         ▒       
\t\t\t\t\t        ▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░█▒▒▒▒▒▒    █▒         
\t\t\t\t\t        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░█▒▒▒▒▒▒▒▒▒▒█▒▒          
\t\t\t\t\t         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  █▒▒▒▒▒▒▒▒▒▒▒▓              
\t\t\t\t\t               ▒▒▒▒▒█                ▒▒▒▒█▓              
\t\t\t\t\t              █░░░▒░                                     """+Fore.RESET,"Charizard", "Fuego", "Llama", "Primera", "Zona 3", "Volcán", "Bayas y pequeños roedores", "Entorno cálido"),
            Pokemon(Fore.BLUE+"""\t\t\t\t\t                  ░░░░▒▒▒▒▒▒▒█                           
\t\t\t\t\t               █▒░░░▒▒▒▒▒▒▒▒▒▒▒█                         
\t\t\t\t\t              █▒▒▒▒▒▒▒▒▒░█ █▒▒▒▒▒                        
\t\t\t\t\t              █▒▒▒▒▒▒▒▒▒█████▒▒▒▒▒                       
\t\t\t\t\t             ▓█▒▒▒▒▒▒▒▒▒███▒█▒▒▒▒▒█                      
\t\t\t\t\t             ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒█                      
\t\t\t\t\t            █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                       
\t\t\t\t\t             ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓                       
\t\t\t\t\t              █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓                       
\t\t\t\t\t                █▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒                      
\t\t\t\t\t           █▒▒▒▒█▒▒▒▒▒█▓▒██▒▒▒▒▒▒█▒▒█                    
\t\t\t\t\t        █░░▒▒▒▒░░░░░▒▒▒▒▒▒▒░░▒▒▒▒▒█▒▓█                   
\t\t\t\t\t     ▒▒▒▒▒▒▒▒▒░░░░▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒                   
\t\t\t\t\t     █▒█▒▒▒▒▒█░░░░░░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒                  
\t\t\t\t\t    ██▒▒▒▒▒▒▒█░░░░░░░░░░▒█▒▒▒▒▒▒▒▒░▒▒▒▒                  
\t\t\t\t\t             ░░░░░░░█░░▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒                  
\t\t\t\t\t             ░▒█░░░░▒░░░░░░█▒▒▒▒▒▒░▓▒▒▒                  
\t\t\t\t\t             ░░░░░░░▒░░░░░░▒▒▒▒▒▒▒░▓▓█▓   ▒▒▒▒▒▒▒▒▓      
\t\t\t\t\t            ▒▒░░░░░░░░░░░░▒▒▒▓▒▒▒█░▒▓▓  ▒▒▒▒▒▒▒▒▒▒▒▒     
\t\t\t\t\t           ░░░▒░░░░░█░░░▒▒▒░▒▒▒▒▒▒▒█▓█ ▒▒▒▒▒▒█▒█▒▒▒▒     
\t\t\t\t\t          █░░░▒▒█▒▒█▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒▒▒     
\t\t\t\t\t          ▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒▒▒     
\t\t\t\t\t          ▒▒▒▒▒▒▒▒▒    ██▓▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒█      
\t\t\t\t\t        █▒▒▒▒▒▒▒▒▒          ▒▒▒▒▒▒▒▒▓ █▓▒▒▒▒▒▒▒█         
\t\t\t\t\t            ▒█              █▒▒▒▒▒▒▒▓                    
\t\t\t\t\t                             ▒▒▒▒▒▒▒▒                    """+Fore.RESET,"Squirtle", "Agua", "Tortuga", "Primera", "Zona 2", "Río", "Peces y algas", "Entorno húmedo"),
            Pokemon(Fore.BLUE+"""\t\t\t\t\t            ▓█                                           
\t\t\t\t\t           █░░█                   █░░░                   
\t\t\t\t\t           ░░░░                 █░░░░█                   
\t\t\t\t\t          ░░░░░░               ░▒░░░█                    
\t\t\t\t\t          █░░░█░   █▒▒▒░░█   ▒░░░░░░░                    
\t\t\t\t\t           ░░░█░░▒▒▒▒▒▒▒░░░▒░░░░░░░░░                    
\t\t\t\t\t          ░▒░░░░░░░▒░░░░░░░▒░░░░░░░░                     
\t\t\t\t\t          ░░░░░░░░░░░░░░░░▒░░█░░░░█                      
\t\t\t\t\t            ░░░░░░░░░░▒░░░░░█░░░░░          ░░░░░▓       
\t\t\t\t\t            ░░░░░░░░░░░▒▓░░░▒▒▒▓█        █░░░░░░░░░█     
\t\t\t\t\t            ▒ ░░░░░░░░████ ▓▒▒▒▒░       ▓░░░░█░░░░░░     
\t\t\t\t\t             ░██░░░░░░░██▓ █▒▒▒▓░█▒█    ░░░░░░░░░░░█     
\t\t\t\t\t           ██░░░▒░░░░░░░░▒▒▓▒▒▒▒░░▒░░▒▒░░▒▓░░░░░░░█      
\t\t\t\t\t     █░░░░░░░░▓▒▓░░░▒▒▒▒█▒░█▓░▒▒▒▒▒▒▒▒▒░░▒ ░█░░░░░░      
\t\t\t\t\t   ██░░▒▒░░░░▒▒▒░░█▒▒▒▒▒██░░░░▒▒▒▒▒▒▒▒░░░ ▒░█░█░░█░▓     
\t\t\t\t\t    █▒░░█▒▒▒▒▒▒█░░░░░█▓▒░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░▓    
\t\t\t\t\t       ██▒▒▒▒▒▒▓░░░░░░▒░░░░░░░░░░███░▓▒▒█░░░░░░░░░█░░▓   
\t\t\t\t\t               █░░░░░░░░░░░░░░░░░░░█░█▒▒▒░░░░░░░░░░░░░   
\t\t\t\t\t                ░░░░░░░░░░░░░░░░░░▒░░░▒▒▒░░░░░░░░░░░░█   
\t\t\t\t\t                ▒░░░▓▒░█░░░▒█░░░░░░░▓░░▒▒░░░░░░░░░░░░    
\t\t\t\t\t                ▒░░░░░░░░░░░░░░░░░▒▒▒▒▒██░░░░▒░░░░░█     
\t\t\t\t\t              █░░░█░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░       
\t\t\t\t\t             █░░░▒▒▒▒░░█░░░░▓░░░░▒▒▒▒▒▒▒▒▒░░░░░          
\t\t\t\t\t             ▒▒▒▒▒▒▒▓▓▓▒░░░░░░░░▒▒▒░░░░▒▒▒▒              
\t\t\t\t\t             ▓▒▒▓▒▒▓▓▓           █░░░░░▒▒▒▒▒             
\t\t\t\t\t            ▒▒▒▒▒▒▓▓█             █▒▒▒▒▒▒▒▒▒             
\t\t\t\t\t             █▒  ▓                ▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t                                       ▒▒                """+Fore.RESET,"Wartortle", "Agua", "Tortuga", "Primera", "Zona 2", "Mar", "Peces y algas", "Entorno húmedo"),
            Pokemon(Fore.BLUE+"""\t\t\t\t\t                                █░██▒▒▒                  
\t\t\t\t\t                           ███▒▒▒▒██▒▒▒█▒▒▒█             
\t\t\t\t\t                            ▒▓▒▒▒▒▒▒▒▒▒▒▒█▒██            
\t\t\t\t\t                             ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒             
\t\t\t\t\t                            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█             
\t\t\t\t\t          ▓░█           ▒▒░▒▒▒▒▒░░░▒▒▒▒▒▒░█              
\t\t\t\t\t         ░░░░░     █▒▒▒▒▒▒▒▒▒▒▒▓▒▒▓▓░█░░                 
\t\t\t\t\t         █░░░░▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓░█░░░░░░█          
\t\t\t\t\t           ░▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▓▓▒▒▒█░░░░░░░█▓         
\t\t\t\t\t           ▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▒▒▒▒░░░░░░░░█         
\t\t\t\t\t          ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒█▓▒▒▒▒░░█▓▒▒▓█           
\t\t\t\t\t        █▒▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓█▓▓▓▓▓▓▓█░░░░░▒▒▒▒▓▒░█         
\t\t\t\t\t       █▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░█▒▒▒▒▒▒▒▒▓█       
\t\t\t\t\t        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▒▒▒▒▒▒▒▒▒█▒█      
\t\t\t\t\t         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░▓▒▒▒▒▒▒▒▒▒▒▒░     
\t\t\t\t\t        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▒▒█▒▒▒█▓▒▒░░      
\t\t\t\t\t        ▓█▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▒▒░                
\t\t\t\t\t       ▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▒▒▒                 
\t\t\t\t\t      ▒▒▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓░░░░░░░▒▒░                  
\t\t\t\t\t     █▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░▒▒▒▓▒▒                 
\t\t\t\t\t     ▒▒▒█▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▒░░░░░░▒▒▒▒▒▒▓▒▒█               
\t\t\t\t\t     ▒▒▒░▓█░░░░▓▓▓▓▓▓▓▓░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒               
\t\t\t\t\t     ▓▒▓▒░░░░░░░░░░░░░░░░░░░░▓▒▒▒▒▒▒▒▒▒▒▒▒               
\t\t\t\t\t     ▓▓▓▓▒▒▒▒▒▓▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓               
\t\t\t\t\t     ▒░░▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒░░█▓▓▓▓▓▓▓▓▓▓▓▓▓                
\t\t\t\t\t     ██▒▒▒▒▓▓▓▓▓▓████        ▓▓▓▓▓▓▓▓▓▓▓                 
\t\t\t\t\t     ▒▒▒▒▓▓▒▒▒▒█             ░░░█▓▓▓▓▓▓░░░█              
\t\t\t\t\t     █▓▓▓▓█                 ░░░░█                        """+Fore.RESET,"Blastoise", "Agua", "Marisco", "Primera", "Zona 2", "Mar", "Peces y algas", "Entorno húmedo"),
            Pokemon(Fore.LIGHTGREEN_EX+"""\t\t\t\t\t                    ██████                               
\t\t\t\t\t    ███       █░░░░░░░▒▒▒▒▒█▒▒                           
\t\t\t\t\t   ▒▒▒▒▒▒  █▒░░░░░░█▒░▒▒▒▒▒▓▒▒▒▒▒                        
\t\t\t\t\t   █▓▒▒▒▒▒▒▒█▒▒█▒▒▒▒▒▒▒▓▒▒█▒█░░░█▒▒                      
\t\t\t\t\t       █▓▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒█░░█▓▓▓░░▒                     
\t\t\t\t\t       ░▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░██▓▓▓▓█░▒                    
\t\t\t\t\t       ▒▒▒▒▒█▓▓▓▒▒▒▒▒▒▒▒▒▒░░███████░▒█                   
\t\t\t\t\t       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░███████░▒▒                   
\t\t\t\t\t       ▒▒▒▒▓▓▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒░░███░░▒▒▒                   
\t\t\t\t\t       ▒▒█▒░░░░▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▓▒▒▒▒██                  
\t\t\t\t\t        █▒░░░███▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░                 
\t\t\t\t\t        █▒█░░░▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                
\t\t\t\t\t         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███▒▒▒▒▒▒▒▒▒▒▒▒▒░                
\t\t\t\t\t          ▒▒▒▒▒▒▒▒▒▒█▒█████▒▒▒▒▒▒▒▒▒▒▒░░░                
\t\t\t\t\t             ▒▒▒▒▒▒█▒▒▒░░▒█▒▒▒▒▒▒▒▒░▒▒░░░                
\t\t\t\t\t             ░░░░░░░░░░░░░▒▒▒▒▒▒▒░▒▒▒▒░░█         █░░█   
\t\t\t\t\t            ██░░░░░░░░░░░▒█▒▒▒▒▒▒░▒▒▒▒▒▒         █░░░▒   
\t\t\t\t\t           █░░░█░░░░░░░░░░░░█▒▒▒▒▒░░▒▒▒          ░░░░▒   
\t\t\t\t\t            ░░▒▒░░░░░░█░░░░▒▒█▒▒▒▒▒▒▓           █░░░▒    
\t\t\t\t\t             ██▒▒░░░░░▒█▒▒▒▒▒▒▒▒▒▒▒▒            █░░▒█    
\t\t\t\t\t               ░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░█             ▒▒▒     
\t\t\t\t\t               ▒░░░░░░░▒▒▒██▒█▒▒░░▒▒▒            ██      
\t\t\t\t\t               ░▒▒▒▒▒▒▒▒░░░▒▒█▒▒▒█▒▒░▒▒        █▒█       
\t\t\t\t\t               █▒▒▒▒▒▒▒▒░░░▒▒▒█▒▒▒▒▒▒▒░▒▒▒▒▒▒█▒▒▒█       
\t\t\t\t\t                     ▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒█▒▒▒▒▒█▒█        
\t\t\t\t\t                       ▒░░░░▒▒▒▒█▒▒█▒▒▒▒▒▒▒▒▒▓▒          
\t\t\t\t\t                          █▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒█            
\t\t\t\t\t                                ████▒███                 """+Fore.RESET,"Caterpie", "Bicho", "Oruga", "Primera", "Zona 1", "Pradera", "Hojas", "Protección contra depredadores"),
            Pokemon(Fore.LIGHTGREEN_EX+"""\t\t\t\t\t               █░░░                                      
\t\t\t\t\t              ░░░░░█                                     
\t\t\t\t\t             ░▒▒░▒▒░                                     
\t\t\t\t\t             ░▒░░▒░░▒                                    
\t\t\t\t\t            ░░░▒▒░▒▒▒▒                                   
\t\t\t\t\t           ░░░░▒░░▒▒▒▒▒                                  
\t\t\t\t\t          ░░░▒░░░░░▒░▒▒█                                 
\t\t\t\t\t         ▒▒░░░░░░░░░░██▒▒▒                               
\t\t\t\t\t        █░░░░░░░▒▒█░░░█░░▒▒▒                             
\t\t\t\t\t        ░░░█░░░▒▒▒▒▒▒░░░▒▒▒▒▒▒█                          
\t\t\t\t\t        ▒▒█░░▓▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒                       
\t\t\t\t\t       █░▒░░░░░▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░█                   
\t\t\t\t\t       █░▒░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                    
\t\t\t\t\t       ░░▒▒▒▒░░▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                     
\t\t\t\t\t       ░▒▒▒▒░▒░░▒░▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒█                      
\t\t\t\t\t        ▒▒▓▒░▒░░▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                       
\t\t\t\t\t         ▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                       
\t\t\t\t\t            ▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                     
\t\t\t\t\t             ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                    
\t\t\t\t\t              █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                  
\t\t\t\t\t                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                
\t\t\t\t\t                  ▓▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▓              
\t\t\t\t\t                     ▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▓█▒▒▒▒▒▒▒            
\t\t\t\t\t                           ▓▒▒█▒▒▒▓▒▒▒▒███▒▒▒▒▒▒         
\t\t\t\t\t                               █▒▒▒▒▓▒▒█▒▒▒▒▓▒▒▒▒▒       
\t\t\t\t\t                                     █▒▒▒▓██▒▒▒█         """+Fore.RESET,"Metapod", "Bicho", "Capullo", "Primera", "Zona 1", "Bosque", "Hojas", "Protección contra depredadores"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t             ▓█                                          
\t\t\t\t\t             ██             ▓█             ░░░░░░█▓▓     
\t\t\t\t\t     ██      █            ███          ░░░░░░░░░░▒█▓▓█   
\t\t\t\t\t   █░░░░░    █           █          ░░░░░░░░░█░█░░░░░██  
\t\t\t\t\t  ██░░░░░░░  █          █         ░░░░░░░░░░▓░░░░░░░░░█  
\t\t\t\t\t  ▓░░░░░░░░░██        █         ░░░███▓████░░░░░░░░░░██  
\t\t\t\t\t  ░░░░▒▓▓█▓░░█       █        ░░░░░░░░░░░██▓░░█░░░░░░██  
\t\t\t\t\t  ▓░░░█▓░░░░▒░░     █       ░░░░░░░░░░░░██░░░░░░░░░░██  
\t\t\t\t\t  ░░░░██░░░░░▒█░    █      █░░░░░░░░░░░░▓░░░░░░░░░░░░█   
\t\t\t\t\t  █░░░░░█░░░░░░░▓   █     █░█░░░░░░░░░░░░░░░░░▓███████   
\t\t\t\t\t   ░░░░░▒░█░░░░█░▓▓█▓▓▓▓ █░█░░░░░░░░█░░░░░░░░░░░░░░██    
\t\t\t\t\t    ░░░░░░░░░░▒▒▒▒▒▓▓█▒▒▓▓█░░░░░░░░░░░░░░░░░░░░░░░░██    
\t\t\t\t\t    █░░░░░░░░▒▒▒▒▓▓▓▓▒░▒▒▓█░█░░░░░░░░░░░░░░░░░░░░░░█     
\t\t\t\t\t     █░▓█░░░▒▒▒▓▓▓▓▓▓█▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░██     
\t\t\t\t\t      ░░░░░░▒▒▓▓▓▓▓██▓▓▓▓▓▓█░░░░░░░░░░░░░░░░░░░░███      
\t\t\t\t\t       ░░░░░█▓▓▓▓▒▒▒▒█▓▓▓▓█░░░░░░░░░░░░░░░░░░░░░░██      
\t\t\t\t\t       █░░░░░░█▓▓▓▓▓▓▓▓▓█▓▓▓░░█░░░░░░░░░░░░░░░░░░█       
\t\t\t\t\t        ░░░░█░░░░░▓▓▓▓▓▓▒▒▓▓▓░░░░░░░░░░░░░░░░░░░██       
\t\t\t\t\t         █░░░░░░░▒█▓▓▓▓▓█▒█▓▓█░░░░▒░░░░░░░▒░░░███        
\t\t\t\t\t           ░░░░░░░▒▓▓▓▓▓▓▓▓▓▓░░░█▒▒▒▒▒▒▒▒░░░████         
\t\t\t\t\t              ███░░░▓▓▓▓▓▓▓▓▓█░░░░░░█▒▒▒░▒▒███           
\t\t\t\t\t                █░░░░░░▓▓█ ▓▓▓█░░░░░░░▒░░██              
\t\t\t\t\t                ▓░░░░░█▓▓▓ █▓▓▓░░█░▓░░░░███              
\t\t\t\t\t                █▓░░░░░▒▒▒▒ ▒▒▒▒░░░░░░░░███              
\t\t\t\t\t                  ██░░░░▒▒▒ █▒▒▒ ██░░░███                
\t\t\t\t\t                    ███  ░▒   ░▒                         
\t\t\t\t\t                                                         """+Fore.RESET,"Butterfree", "Bicho", "Mariposa", "Primera", "Zona 1", "Pradera", "Néctar de flores", "Polinización"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                          ░                              
\t\t\t\t\t                        ░ ░                              
\t\t\t\t\t                      █░░░░                              
\t\t\t\t\t                    █░░░░░░                              
\t\t\t\t\t              █▒░░░▒░░░░░░░                              
\t\t\t\t\t            ▒▒░░▒▒▒▒▒▒▒▒▒▓█▒▒█                           
\t\t\t\t\t           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                          
\t\t\t\t\t        █▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                         
\t\t\t\t\t        ▒▒▒▒▒▒▒▒▒█▒▒▒▒█░█▒▒▒▒▒▒▒                         
\t\t\t\t\t         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                        
\t\t\t\t\t         █▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                         
\t\t\t\t\t          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                         
\t\t\t\t\t           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                          
\t\t\t\t\t            █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                           
\t\t\t\t\t            █▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                             
\t\t\t\t\t          ▒▓▒▒▒▒▒▒▒▒▓█▒▒▒▒                               
\t\t\t\t\t          ▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                              
\t\t\t\t\t            ▒▒▒▒▒▒▒▒░▒█▒▒▒                    █          
\t\t\t\t\t             █▒▒▒▒▒▓▒▒▒▒▒▒                    ░░         
\t\t\t\t\t              ▒▒█▒▒▒▒▒█▒▒▒█                 █░░░█        
\t\t\t\t\t             █▒▒▒▒▒▒▒▒▒▒▒▒█                ░░░░░█        
\t\t\t\t\t              ▒▒▒▒▒▒█░▒█▒█▒▒              ▓░░░░░         
\t\t\t\t\t                 █▒▒▒███▒▒▒▒▓▒█        █▒▒▒░░░░          
\t\t\t\t\t                 █▒▒▒▒▒▒█▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t                  ██▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒██            
\t\t\t\t\t                      ▒▒▒▒▒▓█▒▒█▒▒▒▒▒▒▒██▒▒▒▓            
\t\t\t\t\t                        ▓▒▒▒▒█▒▒▒▒▒▓▒▒█▒                 
\t\t\t\t\t                             █▒▒▒▒▒                      """+Fore.RESET,"Weedle", "Bicho", "Peluche", "Primera", "Zona 1", "Pradera", "Hierbas", "Protección contra depredadores"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                          █████                          
\t\t\t\t\t                     █░░░░░░░░░░░░░█                     
\t\t\t\t\t                   ░░░░░░░░░░░░░░░░░░░                   
\t\t\t\t\t                 ░░░░░░░░░░░░░░░░░░░░░░█                 
\t\t\t\t\t                ░░░░░░░░░░░░░░░░░░░░░░░░█                
\t\t\t\t\t               █░░░░░░░░░░░░░░░░░░░░░░░░░                
\t\t\t\t\t              ██░░░░░░░░░░░░██████░░░░░░░█               
\t\t\t\t\t              █▓█░░░░░░░░░█ ███████░░░░▓▒                
\t\t\t\t\t               ▓░░░░░░░░░▓░█▓▓▓█░░░░▒▒▒█                 
\t\t\t\t\t                 ▒░░░░░░░░░░░░▒▓▒▒▒▒▒▓░                  
\t\t\t\t\t                  ▓░▒▒█▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒░                 
\t\t\t\t\t                 ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░                
\t\t\t\t\t                ▓░█░▒▒█▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒██               
\t\t\t\t\t                 ░░░░░▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▓█▒█                
\t\t\t\t\t                ░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                 
\t\t\t\t\t                ▓░▒█░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░                 
\t\t\t\t\t                 ▒░░░░▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒▒█                 
\t\t\t\t\t                 ▒░█░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                  
\t\t\t\t\t                 █░░░░▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒█                  
\t\t\t\t\t                  ░░█░▒▒▒▒▒▒▒▒▒█▒▒▒▒▒░                   
\t\t\t\t\t                  █▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                    
\t\t\t\t\t                   ▒░░█▒▒▒▒▒▒▒▒▒▒▒▒▒█                    
\t\t\t\t\t                    ░█░▒▒▒▒▒▒▒▒█▒▒▒                      
\t\t\t\t\t                    █░░▒▒▒▒▒▒▒▒▒▒░                       
\t\t\t\t\t                     ░░▒▒▒▒▒▒▒▓▒█                        
\t\t\t\t\t                      █▒▒▒▒▒▒▒█                          
\t\t\t\t\t                      ░▒▒▒█▒                            
\t\t\t\t\t                        █▒▒                              """+Fore.RESET,"Kakuna", "Bicho", "Capullo", "Primera", "Zona 1", "Bosque", "Hierbas", "Protección contra depredadores"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                                   ░                     
\t\t\t\t\t                   ░░░█            ░░    ░░░░░░░█        
\t\t\t\t\t                  ░░░▒████▒        ░░░▒░░░█░░░░░░        
\t\t\t\t\t                  ▓█░░░░░█         ░░▒▒░░░░░░░░░░        
\t\t\t\t\t                ▒▒░░░░░░░░        ░░░░░░▒█░░░░░░░        
\t\t\t\t\t              ▒█  ░░░░░░█░░░▒▒   ░░░░░░░░░░░░▒░░░        
\t\t\t\t\t                   ░░░░░░▓░▓▓▒▒ ░░░░░░░░░░░░░▓░░█        
\t\t\t\t\t                   ░░░░░▓▒▒▒▒▒▓██░░░░░░░▒░░░░░░▓         
\t\t\t\t\t                    ░░░░░░▒▒▒▒░█░░░░░█░▓░█░░░░█          
\t\t\t\t\t                   ▒▓▓░▒▓▓▒░░░░░▓▓▓▓▓░▒▓▒▒▒▒▒░           
\t\t\t\t\t                 ▒▓█  █░▒▒▒░░░░▒▒██░▒▒▒▒▒▓░░░░░          
\t\t\t\t\t             ░░░░█     ░█▒▒░▒▒▒▒█▒█░░░░░░░▓░░░░█         
\t\t\t\t\t           █░░░░▒▒     ██░░█░░▒▒▒▒▒▒▒░░░░░░░░░░░         
\t\t\t\t\t           ░░░░░░▒     ██▓▓░░▒▓▓▓█▒██▒▒░█░░░░░░          
\t\t\t\t\t          ░░░░░░     ▒▓▓█░▓░░░░░░░░▒▒██░░░░░░░█          
\t\t\t\t\t         ░░░░▓      ▒▓    ░░▓▓▓▓███▒▒▒▒█░░░░█            
\t\t\t\t\t        ░░░█        ▓▓    █▓▓░░░█████▒▒█▓                
\t\t\t\t\t       █▒          ▒▓█     ▒░░░▒▒▒▒▓██  ▒▒               
\t\t\t\t\t                  ▒▓▓       ▓▒█▒▒▒▒▒█    ▒▒              
\t\t\t\t\t                  █▓         █░░▒▒█       ▒▒             
\t\t\t\t\t                   ▓          ░▒▒         ▓▒▓            
\t\t\t\t\t                  ▒▓          ░█           ▒▓█           
\t\t\t\t\t              █▒▓█                         █▓▓           
\t\t\t\t\t                                            ▓█           
\t\t\t\t\t                                            ▓█           
\t\t\t\t\t                                             ▒           """+Fore.RESET,"Beedrill", "Bicho", "Abeja", "Primera", "Zona 1", "Bosque", "Néctar de flores", "Polinización"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                     █                                   
\t\t\t\t\t                  █▒▒                                    
\t\t\t\t\t             █▒ ▒▒▒▒▒▓█                                  
\t\t\t\t\t            ░░░░▒▒▒▓▓▓████                               
\t\t\t\t\t           ▒█▒▒▓▒░░░░░░░░░█                              
\t\t\t\t\t         ████▒█▒██░███▓▓▓▓███                            
\t\t\t\t\t       ▒▒▒▒▒▒█░░█ █████▓▓▒                               
\t\t\t\t\t         █▒▒▒▒░░░░░█████▓▓█                              
\t\t\t\t\t          █▒▒█░░░░░░███▓▓▓▓                              
\t\t\t\t\t         ██▒▒█░░░░░██▒▒▓▓▓▓▓                             
\t\t\t\t\t           ░░░░░░░░▒▒▒▓▓▓▓▒▒█                            
\t\t\t\t\t          █░░░░░░░▒▒▒▒▓▓▒▒▒▒▒▒▒▒█                        
\t\t\t\t\t         █░░░░░░░░░▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒█                     
\t\t\t\t\t         ░░░░░░░░░░░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓██       █▒▓█        
\t\t\t\t\t        ░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓█     ▒▒▒▒▒▒▒▒▒     
\t\t\t\t\t        ░░░░░░░░░░░▒▒░▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓█▓█▓▓▓▒▒▒▒█▒█▓▓█   
\t\t\t\t\t       █░░░░█░░░░░▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒█▓▓▓█▓▓▓▒▒▒▒▒▒    
\t\t\t\t\t        █░░░█░░░░▒▒▒██▒▓▓▓▓▓▓▓▓█▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓█     
\t\t\t\t\t         ▒▒▓▒▒░▒▒░▒▒░▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒░░                
\t\t\t\t\t           ██▒▒▒▒▒▒█▒▒▒▒▒█▓▓▓▓▓▓█▒▒▒░░░░█                
\t\t\t\t\t             █▒░▒▒░▒▒▒▒▒▒▒▒██▒▒▒▒▒░░░░░░░█               
\t\t\t\t\t                █░░░░░▒▒▒▒▒▒▒▒▒█▒▒▒▒█░░░░█               
\t\t\t\t\t                    █▒▒▒▒▒▒▒▒▒▒░█   █░░░░▓               
\t\t\t\t\t               █  █▒▒▒▓    ▒▒                            
\t\t\t\t\t          █░█▒█░▒▒▒▒▒██▒█▒▒▒▒▒▒▒▒                        
\t\t\t\t\t             █░█ ░ ▒▒▒▒▓░▒▒▒█ ██▓██                      
\t\t\t\t\t                █     ░▓▒▒█                              
\t\t\t\t\t                    ▓                                    """+Fore.RESET,"Pidgey", "Normal", "Pajarito", "Primera", "Zona 1", "Pradera", "Bayas y semillas", "Protección contra depredadores"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t         ██                                              
\t\t\t\t\t         ░░▒                                █▒▓░░░       
\t\t\t\t\t        ░▒░▒▒                           ▒▒█░▒▒▒░         
\t\t\t\t\t        ░░▒░▒▒                       ▒▒░░░░░░▒░░░░█      
\t\t\t\t\t        ░▒▒░░▒█                    ▒█▒░░░▓█░▒▒░░         
\t\t\t\t\t       █░█░▒▒▒▒▓                 ▒▓▒░░░░░░░█▒▒░░░░       
\t\t\t\t\t        ░▒▓▒▒░░▒▓▒ ▒▒▒▒▒▒▒▒     █▒▒░░░░░░▒▓▒▒░░█         
\t\t\t\t\t        ░█▒█░░░░▓▓▒▒▓▒▒▒▒▒██▒▒  ▒▒░░░░░░░░██░░░░▓        
\t\t\t\t\t         ░▒░░░░▒▒▓▒▒█▓▓▒▒▒   ▓▓▒▒░░░░░░█▒▒▒░░░           
\t\t\t\t\t          ░▒▒▒▒▒▒▓▓░█▒██▒▒█   ▒▒░░░░░░░░▒███             
\t\t\t\t\t          █░▒░░▒▒░▒░░▒▒▒▒▒▒ ▒█▒░░░░░░░▒▒░░░░             
\t\t\t\t\t             █▒▒▒▒█░▒░▒▒▒▒▒█▒░░░░░▒▒▒▒▒░▓                
\t\t\t\t\t             ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░█▒▒███▒█                 
\t\t\t\t\t               ▓▒▒░░░░░█▒▒▒▒█▓▒▒▒█▒░░                    
\t\t\t\t\t                 ▒░░░░░░░▒▒▒▒▒░░█░█                      
\t\t\t\t\t                 ░░░░░░░▒▒▒▒▒▒                           
\t\t\t\t\t                 ░░░░░░▒▒░░░░▒                           
\t\t\t\t\t               █░▒▒▒▒▒▒░▒ ██░▒                           
\t\t\t\t\t         ░░    ░░░▒▒▒▒▒█▒█▒▒▒▒                           
\t\t\t\t\t       ░░▒ ▒  █░▒░▒░▒▒▒▒▒░▒▒▒                            
\t\t\t\t\t          ▒▒▒█          ▒▒█░█▓                           
\t\t\t\t\t            █▒█        █▓█▓░▒▓▓▓█                        
\t\t\t\t\t            ░░█        ▓█▒▓▓▒▒▓▓▓▓█                      
\t\t\t\t\t                      █▒▓▒▓▓█▒▒█▓▓▓▒                     
\t\t\t\t\t                      █▒▒░▓▓▓▒▒▒▒▓▓▒▒                    
\t\t\t\t\t                      █▒▒░░▒▓▓░░░░ █                     
\t\t\t\t\t                         ██░▒▒▒░                         
\t\t\t\t\t                             ██                          """+Fore.RESET,"Pidgeotto", "Normal", "Pájaro", "Primera", "Zona 1", "Pradera", "Bayas y semillas", "Protección contra depredadores"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                                       ░█                
\t\t\t\t\t     ░░░▒█░░█                          ▒▒                
\t\t\t\t\t       ░░░░░░▒▒█░░▒                   ░▒▒▓               
\t\t\t\t\t       ░░░█░░░░░░░░░█▒▒              █▒▒▒▒               
\t\t\t\t\t        ▓░░░░░░░░▓░░░░░▒▒▒            ▒▒▒▒               
\t\t\t\t\t          ░░█░░░▓░░░░░░░░█▒▒          ▒▒▒▓               
\t\t\t\t\t           ░░░░░░░░░░░░░░░█▒          █▓▓▓               
\t\t\t\t\t              █░░░░░░░░░░░░▓▒█░░▓     ▒▓▓█               
\t\t\t\t\t               ░░░░░▒░░░█░░░▓▒ ▒░░░░░░░░░░░░░░░█         
\t\t\t\t\t              ▒▒█▓░░░░░░░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░       
\t\t\t\t\t                   ░░░░░░░░░░░░░▒     ▓▓▒▓████░█▒█▒      
\t\t\t\t\t                      █░░░░░░░░░░░▒▒  ▒▒▓██░░░░▓▒▒▒░     
\t\t\t\t\t                         █░░░░░░░░░░▓▒▓▓▓▓██░░░░▒░       
\t\t\t\t\t                           ▒██░░░░░░░▓▒▒▓▓▒▒░░░░         
\t\t\t\t\t                              ░░░░░░░░░░░░░░░░█          
\t\t\t\t\t                              ▓▓▓░░░░░░░░░░░░░           
\t\t\t\t\t                             █▒▓░░░░░░░░░░░░░            
\t\t\t\t\t                             ▒▒▒░░░░░░░░░░░░░            
\t\t\t\t\t                            █▒▒░░░░░░░░░░░░░             
\t\t\t\t\t                            ▒▒░░█▒░▒░░░░░░░              
\t\t\t\t\t                            ▒░░▒▒▒▒▓░░░░░                
\t\t\t\t\t                       ▓▒▒▒▒▒░░░▒█░░░█▒▒▒                
\t\t\t\t\t                   ▒▒▒▒▒▒▒▒▒▒▒▒                          
\t\t\t\t\t               █▒▒▒▒▒▒▒▒▒▒█▒▒▒▒                          
\t\t\t\t\t               ▒▒▒▒▒▒▒▒▒█▒▒▒▒▒                           
\t\t\t\t\t                   ▒▒▒█▒▒▒▒▒▒▒                           """+Fore.RESET,"Pidgeot", "Normal", "Pájaro", "Primera", "Zona 1", "Pradera", "Bayas y semillas", "Protección contra depredadores"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t                                 █▒▒▒▒▒▒█                
\t\t\t\t\t                                 ▒▒▒▒▒▓▒▒▒▒█             
\t\t\t\t\t                                 █▒▒▒▒▓▓▒▒▒▒▒            
\t\t\t\t\t                                   ▒▓▓▓▒▒  ▓▒▒█          
\t\t\t\t\t                                             ▒▒▒         
\t\t\t\t\t               ▒▒▒▓█                          █▒█        
\t\t\t\t\t              ▒▓▒▒▓▓█                          ▒▒        
\t\t\t\t\t              ▒▒▒█▓▓█          ▒▒▒▒▒▒           ▒▒       
\t\t\t\t\t              ▒▒▒▒▒▒▒▒▒▒▒▒▒ ▓▒▒▒█▒▒█▒█          █▓       
\t\t\t\t\t        █▓    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█           ▓       
\t\t\t\t\t           ▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒█           ▒       
\t\t\t\t\t         ▒▒▒▒▒▒▒▒▒▒▒▒▒▓░░█▓▒▒▒░░░░▒▓▒ █▒▒▒▒▒▒▒█ ▓▓       
\t\t\t\t\t         ▒▒▒▒▒▒▒▒▒▒▓░▓█  ▒▒▒▒▒▒░░░█▒█▒▒▒▒▒▒▒▒▒▒▒▒█       
\t\t\t\t\t          ░░░░░░░░░░░░░░░▒▒▓███▓▒▒▓█████▓▒▒▒▒▒▒▒▒        
\t\t\t\t\t           ░░░░█▒░░░░░░░░█░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█       
\t\t\t\t\t      ▓▒▒▒ ▒ ░█▒▒▒▓░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t    ▒░█░█▓██ █▓▓█▒▒▒▒░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█      
\t\t\t\t\t   ░▒░░▒██████▓▒▒▒▒▒▒▒░░░░░░█▒▒▒▒▒▒▒▓▒░░░░░░▒▒▒▒▒▓▓█     
\t\t\t\t\t                 ▓░░░▒░░░█ ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▓▓▓▓▓   
\t\t\t\t\t                 ░░░█░░   ▒▒▒▒▒▒▒▒█▓█▒▒▒██    █▓▓▓▓▒▒▒█  
\t\t\t\t\t                         █▒▒▒▒▒▒▒▒▒▒▒▓            ▓▓▓▓█  
\t\t\t\t\t                        █▓▒▒▒▓▓█                ░█░░░░   
\t\t\t\t\t                      ▓░░░░▒▓█                  █░ ░█    
\t\t\t\t\t                      █░█░░                              """+Fore.RESET,"Rattata", "Normal", "Ratón", "Primera", "Zona 1", "Pradera", "Bayas y semillas", "Protección contra depredadores"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t               █                                         
\t\t\t\t\t               ▓▒█                                       
\t\t\t\t\t              █▒█▓█                                      
\t\t\t\t\t   █         ▓▒▒▒▒▓▓▒▒▒▒▒                                
\t\t\t\t\t    ░█      █▒▒▒▒▒▒▒▒▒▒▒▒█  █▒▒▒▒▒▒▒▒▓█      ░█          
\t\t\t\t\t      ░  ▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ░▓        
\t\t\t\t\t    ░█ ▒█▒░░░▒▒▒▒███░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒           █░       
\t\t\t\t\t       ░▒░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒█            ░█     
\t\t\t\t\t    █░▒░▒    ░░░░░░░░░░░░░░░░░░██▒▒█               ░▓    
\t\t\t\t\t        ▒   ░▒█░░░░░░░░░░░░█▓▒▒▒▒▒▒                █░█   
\t\t\t\t\t        ░ ▒ ▒▒▒░░░░░░░▒▒▒▓▓▓▓▓▓▓▓▓▓▓█               ░▒   
\t\t\t\t\t        █▓▒ ▒▒▒▓░░░░░░▒░░▒▓▓▓▓▓▓▓▓▓▓▓▓              █░█  
\t\t\t\t\t        ██░ █▒▒▒░░░░░░▒▒▒▒▓░▓▓▓▓▓▓▓▓▓▓█             █░▓  
\t\t\t\t\t         ░░░░▓▒░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓             ░░▓  
\t\t\t\t\t     █░░▒█ █▒░░░▒░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓            ░▒█  
\t\t\t\t\t     █ ▒▒░▒▒░░▒▒░░░░░▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒█          ░░▒   
\t\t\t\t\t     █▒█▒▒▒█░░░░░░░░░░▓▒█░▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒         ░░▒▓   
\t\t\t\t\t     ██    █░░░░░░░░░░▒▒█▒▒█░▓▓▓▓▓▓▓▓▓▒▒▒       █░░█▓    
\t\t\t\t\t            ░░░░░░░░░░░▓▒▒▒█░▓▓▓▓▓▓▓▓▓▒▒▒    █▒░░▒▒█     
\t\t\t\t\t            ░░░░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒█▒▒▒▒▒▒█       
\t\t\t\t\t             █▒▒▒░▓░█░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒█          
\t\t\t\t\t           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██                
\t\t\t\t\t         ░▒▒░▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓█                   
\t\t\t\t\t        ▒  ▒▓        ▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒                   
\t\t\t\t\t                        ▒▒▒░░▒▒▒▒▒▒▒                     
\t\t\t\t\t                       ▒█▒▒▒█▒▒░░▒▒                      
\t\t\t\t\t                        ▓     █░▒                        
\t\t\t\t\t                               █                         """+Fore.RESET,"Raticate", "Normal", "Ratón", "Primera", "Zona 1", "Pradera", "Bayas y semillas", "Protección contra depredadores"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                               █  ▓█  █▒▒▒               
\t\t\t\t\t                               ▓▓▓▓▒▒▒▒▒▒                
\t\t\t\t\t                              █▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓          
\t\t\t\t\t                             ▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓█            
\t\t\t\t\t                             ▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓█         
\t\t\t\t\t     █░░░    ██               █░▓▒██░░▓▓▓▓▓▓▓▓▓▓▒█       
\t\t\t\t\t      ▓░░░░░░ ▒░░░█░        ░░░▒▒▒█▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒█      
\t\t\t\t\t      █░█░░░░░░░▒░▒▒▒▒▒▒   █░░█▓▒█▒▓▓▓▓▓▓▓▓▓█            
\t\t\t\t\t       ░░░░░░░░░░▒▒▓▒▒▒▒▒▒█  █▒▒░▒▓▓▓▓▓▓▓▓▓▓             
\t\t\t\t\t        ░░░░░░▒▒▒░▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓             
\t\t\t\t\t         █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▒▒▒▒▒▒▒▓▓▓▓▓█▒            
\t\t\t\t\t          ░▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓█▒▒▒▒▒▒▒▓▓█▓▓             
\t\t\t\t\t           ▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▓▒▒▒▒▒▒▒██▓▓             
\t\t\t\t\t    ▒▒▒▒▒█  ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▓███▒▒▒▒▒█▒▒█▓▓             
\t\t\t\t\t     ▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒░░░░▒░█▒█             
\t\t\t\t\t       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▒░░░░░░░▓▒              
\t\t\t\t\t           █▓▓▓███░▓▓▓▓▓▓▓▓▓░░░█░░░░░░░░▓█               
\t\t\t\t\t        ▓▒▓▓▓▓▓▓█  ░░░░░░░░░░░░░░░░░░░░                  
\t\t\t\t\t                    █░░░░░░░░░░░░░░░▓                    
\t\t\t\t\t                    █░░░░░▓░░░░░░▓░░                     
\t\t\t\t\t                     ░░░░       █▒██                     
\t\t\t\t\t                     ▒▒▒         █▒░                     
\t\t\t\t\t                     ▒▒           █▒▒▒█                  
\t\t\t\t\t                    █░▒▓        ▒▒█▒▒▒░▒▒▒░░░            
\t\t\t\t\t                 ██▒░░▒▒█             ▒ █   █░           
\t\t\t\t\t               ░░▒█    █▒░                               
\t\t\t\t\t               █           █                             """+Fore.RESET,"Spearow", "Normal", "Pájaro", "Primera", "Zona 1", "Pradera", "Bayas y semillas", "Protección contra depredadores"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                    ░░                                   
\t\t\t\t\t                   ░░░ ░░                                
\t\t\t\t\t                 ░░░░█░░▓░░                              
\t\t\t\t\t                ▓░▒▒▒▒░░▓░░                    █   █░░   
\t\t\t\t\t                ▒▒▒▒▒▒▒█░░ ░▒               █░░ ░░░░░    
\t\t\t\t\t                ▓▒▒▒▒▒▒▒▒▒▒▒█             ▒▒▒▒▒░░░█░░░░  
\t\t\t\t\t                 ▒▒▒▒▒▓▓▓▓▒▒█▒          ▒▓▒▒▒▒▒▓▒░░░░    
\t\t\t\t\t                 ▒▒▒▒▓▓▓▓▓▓▓▒▒        ▒▒▒▒▓▒▒▒▒▒▒▒ ░░█   
\t\t\t\t\t                 ▒▒▒▒▓▓▓▓▓█▒▒       ▒▒▒▒▒▒▒▒▒▒█▒▒░░░     
\t\t\t\t\t                  ▒▓▓▓▓▓▓█▓▓█▒     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▓     
\t\t\t\t\t                  ▒▓▓▓▓▓▓▓▓▓▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░      
\t\t\t\t\t                  █▓▓▓▓▓▓▓▓▓█▒    ▒▒▒▒▒▒▒█▒▒▒▒▒░         
\t\t\t\t\t                   ▓▓▓▓▓▓▓▓▓▒█   ▓▓▒▒▒▒▒▒▒▒▒░░░░         
\t\t\t\t\t               ░     ▓▓▓▓▓▒▒█▒   ▒▒▒▒▒▒▒▒▒▒▒█            
\t\t\t\t\t             ▒█▓      █▓▓▒▒▒▒░ ▒▒█▒▒▒▒▒▒▒▒░░             
\t\t\t\t\t             ▒▒█▒      █▒▒▒▒▒█▒▒█▒▒▒▒▒▒▒░░░              
\t\t\t\t\t           ░▒▒▒▒▒    ▒▓ ▒▒▒▒▒█▒▒▒▒▒▒█▒▒░░                
\t\t\t\t\t           ▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░                 
\t\t\t\t\t           ▒▓░▒▒▒█      ▒▒▒▒▒▒▒▓▒▒▒▒▒                    
\t\t\t\t\t         █░▒█▒▒▒        ▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▓█           
\t\t\t\t\t       ░░ ░█            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒█▒▒▒▒▒        
\t\t\t\t\t  █░░█   ▒░              █ █▒▒▒▒▒▒▒▒ █▒█▒▒█▒▒           
\t\t\t\t\t  ██                            ▒▒ █▓█ ▒                 
                                ▒▒   █▒▒                 
                               ░░░   ░░██                
                                 ░   ▒███                """+Fore.RESET,"Fearow", "Normal", "Pájaro", "Primera", "Zona 1", "Pradera", "Bayas y semillas", "Protección contra depredadores"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t              █▒░▒▒█                                     
\t\t\t\t\t          ░░░░░░░▒▒▒▒▒▓█                                 
\t\t\t\t\t        ░░░░░▒▒▒██░█▓▓▓▓▓                   ░░▒          
\t\t\t\t\t      ▒▒▒▒▒▒█▒▒░░░▓░█▓▓▓▓▓                   █░░▒        
\t\t\t\t\t    ▒▒▒▒▒▒▒▒▒▒▒█░░░░▓▓▓▓▓▓▓                   ▒▒▓░       
\t\t\t\t\t   █▒░▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒                 ░░░▒█     
\t\t\t\t\t    ▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒                █░░▒█    
\t\t\t\t\t          ▓▓▓▓▓█▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▒▒               █░░▒▒    
\t\t\t\t\t          ▒█░░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒               █░░▒█   
\t\t\t\t\t         █▒░░░░░▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒               ▓▒▒▒▓█  
\t\t\t\t\t         ██▒▒▒▒▒█▓▓▒▓▓▓▓▓▓▓▓▒▒▓▓▒█                ▒█▓█   
\t\t\t\t\t            ███  █░▒▒▒▓▓▓▓▒▒▒▒▓░░                 ▒░▒▓▓  
\t\t\t\t\t               █░░░▒▒▒▒▒▒▒▒▒▒▒▒░█                █▒░▒▓▓█ 
\t\t\t\t\t             █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█ █████           ▒▒▒▒▓▓  
\t\t\t\t\t           ▒▒▒▒▓▓▓█▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓█▓▓█▓      █▒▒▒▓▓▓  
\t\t\t\t\t         █▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓█▓▓▓▓▓     ▒▒▒▓▓▓█  
\t\t\t\t\t         ▒▒░░▒▒▒█▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓  █▓▒▓▓▓█▓   
\t\t\t\t\t        █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▓▓▓▓▓▓▓ ▓▓▓▓▓▓█▓    
\t\t\t\t\t         ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓     
\t\t\t\t\t       ▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓█▓███▓▓▓▓▓▓▓      
\t\t\t\t\t     ▒▒▒▒▒▓█▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓        
\t\t\t\t\t   █▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▓▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█        
\t\t\t\t\t   ▓▒▒▒▒▒▒▒░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓        
\t\t\t\t\t    ▓▓▒▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓█        
\t\t\t\t\t     █▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█         
\t\t\t\t\t      █▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒▒            
\t\t\t\t\t         █▒▒▓█▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒▒▒▒▒▓█               
\t\t\t\t\t                 ████▓▒▒▒▒▒▒▓████                        """+Fore.RESET,"Ekans", "Veneno", "Serpiente", "Primera", "Zona 1", "Bosque", "Roedores", "Mordedura venenosa"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t                           █▒▒██                         
\t\t\t\t\t                      █▒▒▒▒▒▒▒▒▒▒▓▒▒                     
\t\t\t\t\t                    ▒░░▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒█                  
\t\t\t\t\t                  ▒▒░▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓█▒▒▒▒               
\t\t\t\t\t                ▒▒▒▒▒▒▒▒▒▒░▓▒▒▒█▓▓▓▓▓▓▓▓▓▒▒▒█            
\t\t\t\t\t               ░▒█▒▒▒▒▒▒██▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒           
\t\t\t\t\t              █▒▓██▒▒▒▒▓▒▒▓▒▓██▓▓███▓▓▓████▓▓▒▒█         
\t\t\t\t\t              ▓▒▓▓█▓█▓█▒█▓███████▓▓███▓▓▒▒█▓▓▓▒▒█        
\t\t\t\t\t               ▒▓▓█▓█░▓▒▒▒▒████▓███▓▓▓▒▒▓██▓▓▓▓▒▒█       
\t\t\t\t\t               █▒▓░█▓▒▒██▓█▓█▓▓██▓▒▒▒▒▒▓▓█▓▓▓▓▓▓▒▒       
\t\t\t\t\t                █░▒▓██▓▓▓▓█▒▒▒██▒▒▒▒▒▒▓██▓▓▓▓▓▓▓▒▒       
\t\t\t\t\t                  ▒▓█▒▓███▒▒▒▒▒█▒▒▒▒▒███▓██▓▓▓▓▓▒▒       
\t\t\t\t\t                   ▒▒█████████▒▒▒███▓▒▒███▓▓▓▓▓█▒▒       
\t\t\t\t\t                    █▒▒██████████████████▒▓▓▓▓▓▒▒        
\t\t\t\t\t                      ▒▒▒████▓██████████▒▒▒▓▓▒▒▒         
\t\t\t\t\t                       █▒▒▒▒▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒           
\t\t\t\t\t        █▒▒█           █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█             
\t\t\t\t\t         █▓▒           ▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒█                
\t\t\t\t\t        █▒▒           █▒▒░░▒▒▒▒▒▒▒▒▒▒█                   
\t\t\t\t\t       ▒▒▒           █▒▒▒░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓█               
\t\t\t\t\t     ▓▒▒▒▓          ▓▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓           
\t\t\t\t\t     ▒▒▒▒▒      █▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▓▓         
\t\t\t\t\t     ▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▒▒▒▒▓▒▒▒▒▓▓        
\t\t\t\t\t      █▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▓▓        
\t\t\t\t\t         █▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▓▓█        
\t\t\t\t\t                      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓          
\t\t\t\t\t                        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓█            
\t\t\t\t\t                              ██▓▒███▓                   """+Fore.RESET,"Arbok", "Veneno", "Cobra", "Primera", "Zona 1", "Bosque", "Roedores", "Mordedura venenosa"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t            ██                                           
\t\t\t\t\t           ███                                           
\t\t\t\t\t          ██░░                                      ░    
\t\t\t\t\t         █░░░░                      ██████       █░░░█   
\t\t\t\t\t         ░░░░░               █░░░░░██████      █░░░░░░   
\t\t\t\t\t         ░░░░█            ░░░░░░░░█████      █░░░░░░░░█  
\t\t\t\t\t         ░░░░░░░░░░░░░ ░░░░░░░░░░██        █░░░░░░░░░░░  
\t\t\t\t\t         ░░░░░░░░██░░░░░░░░░░░▓          █░░░░░░░░░░░░░  
\t\t\t\t\t       ░▓░░░░░░░████░░░░░░█             ░░░░░░░░░░░░░░░  
\t\t\t\t\t      ░██░░░░░░░░░░░▒▒█░░░░           ░░░░░░░░░░░░░░░    
\t\t\t\t\t     █░░░░█▓▓▓▓░░░░▒▒▒▒█░░░░         ░░░░░░░░░░░░░       
\t\t\t\t\t     █▒░░░░▓▓▓▓░░░░▒▒▒▒░░░░░░        ▓░░░░░░░░░          
\t\t\t\t\t      ▒▒░░░░▓▒▒░░░░░░░░░░░░░░▓        ▒▒░░░░             
\t\t\t\t\t       █░░░░░░░░░░░░░░░░░█░█░░█        ▒▒▒               
\t\t\t\t\t        █░░░░░░░░░░░░░░░░░░░░░░▒       ▒▒▒▒              
\t\t\t\t\t  █░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░░   █▒▒▒▒▒█              
\t\t\t\t\t  ░▒█░░░░░░░░░░░░░░░░░░█░░░░░░░░░░  ▒▒▒█                 
\t\t\t\t\t    █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█  ▒▒▒                
\t\t\t\t\t            ░░░░░░░░░░░░░░░░░░░░░░░░▓ ▓▓▓▓█              
\t\t\t\t\t             ░░░░░░░░░░░░░░░░░░░░░░░▒█▓                  
\t\t\t\t\t             ░░░░░░░░░░░░░░░░░░░░░░░▒▒▓█                 
\t\t\t\t\t             ░░░░░░░░░░░░░░░░░░░░░░▒▒▒                   
\t\t\t\t\t             █░░░░░░░░░▒░░░░░░░░▒▒▒▒▒▒                   
\t\t\t\t\t               ▒░░▒▒▒▒▒▒▓█▒▒▒▒▒▒▒▒▒▒▒                    
\t\t\t\t\t                 █▓▒▓            █▒▒▒                    
\t\t\t\t\t                   ▓█             ▒░░                    """+Fore.RESET,"Pikachu", "Eléctrico", "Ratón", "Primera", "Zona 1", "Bosque", "Bayas", "Estática"),
            Pokemon(Fore.YELLOW+"""\t\t\t\t\t       ▓                    █▓█                          
\t\t\t\t\t       █▓█              █▓▓▒█                            
\t\t\t\t\t        ▒▓▓           ▓▓▓▒▒█                             
\t\t\t\t\t    ▓██░░█▓█   ███   ▓▓▒▒░░░  █                          
\t\t\t\t\t        ░░▓░░░░░░░░░░░▓▒░░   █                           
\t\t\t\t\t         ▒░██░░░░░░█░░▒                                  
\t\t\t\t\t         ░░░░▒▓▒▓▒░█░░█▒                                 
\t\t\t\t\t         ░░░░░░░░░░░░░▒▒                                 
\t\t\t\t\t          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                 
\t\t\t\t\t     ██▒▒░▒▒▒░░░░▒▒▒▒▒▒░░▒▓▓       █                     
\t\t\t\t\t   ▓▓▓▒░░░░░░░░░░░░▒▒▒▒▒▒▒▓▓▓▓       ▒▒▒▒█               
\t\t\t\t\t     ▓▒▒▒▒░░░░░░░░░░▒▒▒▒██            ▓▒▒▒▒▒▒█           
\t\t\t\t\t         ░░░░░░░░░░░░░█░░░█   █▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░█        
\t\t\t\t\t         ░░░░░░░░░░░░░░░░░░        █▒▒▒▒▒▒▒▒░░░░░░░      
\t\t\t\t\t        █░░░░░░░░░░░▒░░░░░░░          █▒░░░    █░░░░░    
\t\t\t\t\t         ░░░░░░░░░░░▒▒▒▒▓█▒▒             ▒░█         ░░  
\t\t\t\t\t         ▒░░░░░░░░░▒▒▒▒▒▒▒▒█               ░             
\t\t\t\t\t         █▒▒▒░░░▒▒▒██    █░▒                             
\t\t\t\t\t       ██   ▒▒▒▒▒   █                                    
\t\t\t\t\t       ▓      ▒▒▒   █                                    
\t\t\t\t\t       ▓      ▒▒▒███                                     
\t\t\t\t\t        ▓     ▒░░▓                                       
\t\t\t\t\t          ███▓▒▓▓                                        
\t\t\t\t\t            ▓▓▓▓                                         """+Fore.RESET,"Raichu", "Eléctrico", "Ratón", "Primera", "Zona 1", "Bosque", "Bayas", "Estática"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                 ██▓██                                   
\t\t\t\t\t         ▒▒░░░░█░░░░░░░░░█░░░░░▒██                       
\t\t\t\t\t         ▒▒░█░░░░░░░░░░░░░░░▒▒▒▒▒                        
\t\t\t\t\t          ▒░░░░░░░░░░░░░░░░░▒▓░░█                        
\t\t\t\t\t          ░░▓░░░░░░░▒░░░░░░░▒▒▒▒                         
\t\t\t\t\t         ▓░░░░░░░░░░░░░░░░░░▒▒▒▒█                        
\t\t\t\t\t         ░█░░░░▒░░░░░░░▒  ██▒▒▒▒▒▒▓                      
\t\t\t\t\t         ░ ░░░░░░░░▒░░░█░███▒▒▒▒▒▒▒▒                     
\t\t\t\t\t         ███░░░░░░░░░░░█▓██▒▒▒▒▒▒▒▒▒▒                    
\t\t\t\t\t           ▓░░░░░░░░░░░█░░░█▒▒▒█▒▒▒▒▒▓                   
\t\t\t\t\t         ░░░░░░░░░░░░░░░░▒▒▒█░█▒▒▒▒▒▒▒                   
\t\t\t\t\t        ▒▒░░▓█░░░░░░░█▒▒▒▒▒░░░░░▒█▒▒▒▒▒                  
\t\t\t\t\t       ░░░░░░▒▒█░░░█▒▒▒▒▒░░░█░░░▒▓█▒▒▒▒             █    
\t\t\t\t\t       ░░▒░░░░█▒▒▒▒▒▒▒▒▓█░░░█░░▒▒▒▓▒▒▒▒            ░░    
\t\t\t\t\t       ░▒░░░░░▒▒▒▒▒▒▒▒░░░░░▒░░▒▒▒▒▒▒▓▒▒         ░░░▒▒    
\t\t\t\t\t        ▒░░░█▒░▒▒▒▒▒░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒█  ██▒▒░▒▒▒▒▒█    
\t\t\t\t\t          ▒▒█▒█░░░░░█░░░▒▒▒▒▒▒▓░░░░░░░░▒▒▒█▒▒▒▒██▒▒▒     
\t\t\t\t\t         █░░▒░░░░░░░░░░░░░░░░█░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▒      
\t\t\t\t\t         ░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░▒▒▒▒▒█▒▒▒▒█       
\t\t\t\t\t        █▒█▓░░█░░░░░░░░░░░░░░▒▒░░░░▒█░▒█▒▒▒▒█▒▒▒         
\t\t\t\t\t        █░░░▒▒▒▒░░░░░░░▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒           
\t\t\t\t\t         █▒▒▒▒▒█▒▒█▒▒▒▒▒▒▒▒▒█░░░▒▒▒▒▒▒▒▒▒▒█              
\t\t\t\t\t          ██▒▒▒▒▒▒▒▓   █▓▒▒▒█▒▒▒██▒▒▒█▒▒▒                
\t\t\t\t\t        ░░░░▒▒▒▒▒▒█            ▒▒▒▒▒▒▒▒▒                 
\t\t\t\t\t      █░░░▒▒█                     ▓▒▒▒▒▒▒                
\t\t\t\t\t                                  ▒░░▒░░█                
\t\t\t\t\t                                   █░░░▒█                
\t\t\t\t\t                                     █░█                 """+Fore.RESET,"Sandshrew", "Tierra", "Ratón", "Primera", "Zona 1", "Bosque", "Bayas y raíces", "Taladrar"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                           ▓    █                        
\t\t\t\t\t                     █     ▓▓█  ▓▒█     ▒                
\t\t\t\t\t                     ▓▓▓█ ░█▓▓▓ ▓▓▓▓    ▓▓     █         
\t\t\t\t\t                 ▒▒▒▓█▓▓▓▓▓░░░█▓▓▓▓▓▓▓ ▓▓▓█  ▒░▒         
\t\t\t\t\t                  ▒▒▓▓▓▓▓█▓░░░░▒▓▓▓▓▓▓▓██▓▓▒░░▒▒▒▒▒█     
\t\t\t\t\t             ███   ▓▓▓▓▓▓▓▓▓░░░░▒█▓▓▓▓▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒   
\t\t\t\t\t              ▒▒▒▓▓▓▓▓█▓▓▓▓▓▓░░░░▒▓▓▓▓▓░░░█▓▒▒▒▒▒▒▒█▒▒░  
\t\t\t\t\t           █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒▒▓░░░░▒▒▒   ▓▒▒▒░░  
\t\t\t\t\t             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓░░░▒▒░░▒░░░░▒▒█      ▓░░  
\t\t\t\t\t     ▒▒▒▒▒▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓█▓░░██░░░░▒▒▒█░▒▒       ░░  
\t\t\t\t\t       ▒▓▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒▓▓▓▓▓░░██ █░░░▒░░░█            
\t\t\t\t\t          ▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▒░░███░░░░░░ █            
\t\t\t\t\t     █▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒░▒▒▓░░▒░░░░░▒             
\t\t\t\t\t       ▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒░█░░░░░▒▓▓░░░░░█              
\t\t\t\t\t    █▒▒▓▓▓▓▓▓▓▓▓▓█░░░░░░░▒░░░░░░░░░░▓  ░░█               
\t\t\t\t\t       ██████▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒█                
\t\t\t\t\t         █▒▒▒▒▒▓░░░░░░░░░░█░░▒░░░░░░░░░░░                
\t\t\t\t\t      █▒▒▒▒▒▒▒▒▒▒░░░░░░░░░█░░░░▒▒▒▒▓█░ ░░░░░             
\t\t\t\t\t    ▒▒▒▒▒▒▒▒▒▒▒█▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒░░░░░█░░░░░░░▓         
\t\t\t\t\t █▒▒▒▒▒▒▒▒▒▓█  ▓▒▒▒▒▒▒▒▒█ ▒▒▒▒▒▒   █░░░░░░░█░░░░░░█      
\t\t\t\t\t              █▒▒▒▒        █▒▒▒          ████            
\t\t\t\t\t              █▒▒▒▒        ░▒▒█                          
\t\t\t\t\t              █▒░░░░       ░▓█                           
\t\t\t\t\t               ░░░░░                                     
\t\t\t\t\t               █░░▒▒                                     
\t\t\t\t\t                ░░▓░                                     
\t\t\t\t\t                 ░█░                                     
\t\t\t\t\t                  ██                                     """+Fore.RESET,"Sandslash", "Tierra", "Ratón", "Primera", "Zona 1", "Bosque", "Bayas y raíces", "Taladrar"),
            Pokemon(Fore.CYAN+"""\t\t\t\t\t                     ██                                  
\t\t\t\t\t                    █▒▒              █░░                 
\t\t\t\t\t       █░░░░░░░░░█████▒ █▒▒▒█  ██░░░██░░░░░▒             
\t\t\t\t\t       ▓░░░░░░░░░░░▒░░░░░░▓▒▒▒░░░░░░░░░░░░░░░░█          
\t\t\t\t\t      ░░░░░░░░░░░░░█▓▓░░░░░░▒▒▒▒▒▒█▓▓▓█▓▓▓▓█▒░░░░█       
\t\t\t\t\t     █░░░░░░░░░░░░░░░░░░░░░░░▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░█    
\t\t\t\t\t      ░░░░█░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓█░░░░░░█ 
\t\t\t\t\t      ▒░  ░▓▓█░░░░░░░░█░░░░░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒█     
\t\t\t\t\t     ██░░█▓▓▓▓░░░░░░░░░░░█░░░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒█      
\t\t\t\t\t    ▒▒ ░░░▒▓▓▓░░░░░░░█░░░█░░█░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒        
\t\t\t\t\t  ██   █░░▒▒▒▒█░░░░░░▒░░░░░░░█░░░░░░░█▓█▓▓▓▓▓▓▒▒         
\t\t\t\t\t      ▒ ▓░█░░▒█░░░░░░░░░▓░░░░░░░░░░░░░░░ █████           
\t\t\t\t\t         █░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█  █░░░░█       
\t\t\t\t\t           ░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░▒▒▒▒▒         
\t\t\t\t\t           ░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░▒▓▒█          
\t\t\t\t\t          █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒█           
\t\t\t\t\t          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒███         
\t\t\t\t\t          ░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░▒▒▒▒▒▒█         
\t\t\t\t\t          ░░▒░░░░░░░░░░░░░░░░░░░▒▒▒░░░░▒▒▒▒▒▒▒           
\t\t\t\t\t          ░▒▒▒▒▒░░░░░▒░░░░░░░░░░░▒░░▒▒▒▒▒▒▒▓▓▒           
\t\t\t\t\t          ▓▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░░▒▒▒▒▒▒▒▓▓▒█           
\t\t\t\t\t          █▒▒▒▒▒▓▒▒▒▒▒▒▒░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▒░▒▒▒▒▒▒▒▒▒▒▒▒             
\t\t\t\t\t           █▒▒▒▒▒▒    █▒█▒░░░░▒▒▒▒▒▒▒▒▒▒▒█▒▒▒            
\t\t\t\t\t            ░░▒▒▒      ░░▒▒▒▒▒▒▒▒▒▒▓█▒▒▒▒▒▒▒▒            
\t\t\t\t\t              █          ▒▒▒▒▒▒█  ░░░▒▒▒░░▓▒             
\t\t\t\t\t                         ░█░ ░█                          
\t\t\t\t\t                           █░█                           """+Fore.RESET,"Nidoran♀", "Veneno", "Pincho", "Primera", "Zona 1", "Bosque", "Bayas", "Piel venenosa"),
            Pokemon(Fore.CYAN+"""\t\t\t\t\t                            ░▒                           
\t\t\t\t\t                      ░   ▒▒▒                            
\t\t\t\t\t                      ▒ ▒▒▒▒▒▒                           
\t\t\t\t\t                     █▒▒▒▒▒▒▒▒▒              ░░░▒        
\t\t\t\t\t                     █▒▒▒▒▒▒▒▒▒▒      ░  ▓░░░▒▒▒█        
\t\t\t\t\t                    █ ▒▒▒▒▒▒▒▒▒█     ░▒░░▒▓▓▓▓▓▓▒▒░█     
\t\t\t\t\t                    █▒▒▒▒▒▒▒▒▒▒     ░░▒▓▓▓▓▓▓▓▓▓█▒▒      
\t\t\t\t\t                      ▒▒▒▒▒░░░░░░░░▓░▒▓▓█▓▓▓▓▓▓▓▓▒       
\t\t\t\t\t                       ▒▒▒░░░░░░░░░▒▓▓▓▓▓▓▓▒▓▓▒▒▒▒       
\t\t\t\t\t                       █░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▒█       
\t\t\t\t\t                       ░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒         
\t\t\t\t\t             ░░        █░░░░░░░▒░▒▒▓▒▒▒▒█▒▒▒█            
\t\t\t\t\t              ░░░▓     ░▒░░░▒▒▒░▒▓▓░░▒▒▒▒▒               
\t\t\t\t\t              █░░░░░█░█░▓▒▒▒▒▒▒█░▒▒█▒▒▒▒▒                
\t\t\t\t\t            ██ ░░░░░░░░░░▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒                
\t\t\t\t\t             ▒▒█░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▒▒▒▒                
\t\t\t\t\t      █░      ░░░░░░░░░░▒▒▒▒▒█▒▒▒▒▒░▒▒██▒██              
\t\t\t\t\t       ▒▒▒▒█ ░░▓▓░░░░░░░░▒▒▒▒▒▓█▒▒▒▒▒▓▒▒▒▒▒              
\t\t\t\t\t       ▒▒▒▒▒█▒░░░░░░░░░░░▒▒▒▒▒░░░░░▒▒▒▒▒▒▒▒▒             
\t\t\t\t\t        ▒▒▒▒░░░░░░░░░▒░▒░░▒▒▒▒░░░░░░█ ▒▒▒▒▒▒             
\t\t\t\t\t         ▒▒▒░▒▒░░░░░▒░▒▒░░▒▒▒▒░░░░░░  █▒░░░▒             
\t\t\t\t\t          ▒░▓▓▓░░░░░█░░█▒░▒▒▒▒█░░░░▒  █░░░░░             
\t\t\t\t\t           ▒▓▓░░░░░▒▒░░░▒▒▒▒▒▒▒█░░▒▒█ ██░░▒█             
\t\t\t\t\t           ▒▒▒░▓▒▒▒▒▒░░░░░█▒▒▒▒▒▒▓▒▒    ░                
\t\t\t\t\t           ▒▒▒▒▓▒▒▒▒▒░░░░░░▓▒▒▒█░▒▒                      
\t\t\t\t\t            ▒▒▒▒▒▒▒█         █ ▒░▒                       
\t\t\t\t\t            ░█▒▓░█▒▓                                     
\t\t\t\t\t               █░░                                       """+Fore.RESET,"Nidorina", "Veneno", "Pincho", "Primera", "Zona 1", "Bosque", "Bayas", "Piel venenosa"),
            Pokemon(Fore.CYAN+"""\t\t\t\t\t                       ▓▒               ████▒▒           
\t\t\t\t\t                       ▒▒▒▒      ▒▒ ▒▒▓▓▓▓▓█▒            
\t\t\t\t\t                     █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓█▓▓▒            
\t\t\t\t\t                    ▒▒▒▒▒▒▒█ ▓ ░▒▒▒▒▓▓▓▓▓▓▒▒▓            
\t\t\t\t\t                   ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓█▒▒▒            
\t\t\t\t\t                    ██▒▒▒▒▒▒▒█▒▒▒█▒▒▒█▓▓▒▒▒▒             
\t\t\t\t\t                       ▒▒▒▒▓▓▓▓█░░░▒▒▒▒                  
\t\t\t\t\t                         ▓▒▓▒▒▒█░░░░▒▒▒██                
\t\t\t\t\t                         ▒▓▒▒▒▒░░░░░▒▒▒▒▓▓▓▓█            
\t\t\t\t\t                        █▒░░░░▓░░░░▒▒▒▒▒██               
\t\t\t\t\t                    ▒▒▒▒▒▒█▒▒░░░░░▒▒▒▒▒▒▒▒▒▒             
\t\t\t\t\t                  █▒▒▒▒▒░░█░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓          
\t\t\t\t\t             ██▒▒█▒▒▒▒░░░░█▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒█           
\t\t\t\t\t        ▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒░░░▒▒▒▒▒▒▒▒▒           
\t\t\t\t\t       ▒▒█░▓▒▒▒▒▒▒▒▓█░░░░░░░▒▒▒▒░░░░░░▒▒▒▒▒█▒▒▒          
\t\t\t\t\t       ░█▒▒▒▒▒▒▒▒▒   ░░░░░░░▒▒▒░░░░░░░░░░░█▒▒█▒▒         
\t\t\t\t\t        ▒▒▒▒▒▒▒▒█   ▒▒░░░░█▒▒▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t        ░░████      ▒▒▒▒▒▒▒▒▒▒▒▒▓░░░▒▒▒▒▒▒▒▒▒▒▒▒█        
\t\t\t\t\t             ▒▓ ▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t             ▓▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▓          
\t\t\t\t\t   ▒▒▓▓▓▓▓▓▓▓█▒▒▒▒▒▒██░░░░░░░░▒▒▒▒▒▒▒█▒▒▒█▒▒▒▒▒▒         
\t\t\t\t\t   █▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▒▒▒▒▒▒▓        
\t\t\t\t\t     ▓▓▓▓█▓▓▓▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓█       
\t\t\t\t\t       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓█       
\t\t\t\t\t          ▓▓▒▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓    █▓▓▓▓▓▓▓▓▓█      
\t\t\t\t\t          ▒▒▒▒▒▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█       █▓▓▓▓▓▓▓▓▓██     
\t\t\t\t\t        ░░▒▒▒▒▒░░▓▓▓▓█                    ▓▓▒░░▒▒▒▓░░    
\t\t\t\t\t              █░                              █          """+Fore.RESET,"Nidoqueen", "Veneno", "Taladro", "Primera", "Zona 1", "Bosque", "Bayas", "Piel venenosa"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t                     ▒                                   
\t\t\t\t\t                   █▒▒                                   
\t\t\t\t\t                  ▓▓▓▓█▓█              █▒▒█              
\t\t\t\t\t                █▓▓▓▓▓▓▓         █  █▒▒▒▒                
\t\t\t\t\t              █▓▓▓▓▓▓▓▓▓       █▒▒▒▒▒▒▒▒▒▒               
\t\t\t\t\t           ▓█▓▓▓▓▓▓▓▓▓▓▓▓    █▒▒▒▒▒▒▓▓▓▓█▒▒▒             
\t\t\t\t\t           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▒▒▒▒▒█▓▓▓▓▓▓█▒               
\t\t\t\t\t           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▓▓▓▓▓▓▓▓▓▒█               
\t\t\t\t\t           ▓▓▓▓▓▓▓▓▓▓▓▓█▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓█▒                
\t\t\t\t\t           ▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒     █▒         
\t\t\t\t\t         █▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓█▓    ▒▒▒          
\t\t\t\t\t        █▓▓▓▓▓▓▓▓▓▓▓▓█▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓█▒   ▒▒▒▒           
\t\t\t\t\t         ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒█▒██▒▒▒▒▓            
\t\t\t\t\t          ▓▓▓▓▓▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▒▒▒▓▒█▓▓▓▓▓▓   █▒▒▒      
\t\t\t\t\t          ▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▓█▒█▓▓▓▓▓▓█▓▓▓▓▓        
\t\t\t\t\t          █▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▓▓▓▒▒▓▒▓▓▓█▒▒▒▒▓▓▓▓▓█         
\t\t\t\t\t       █▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▒▒█▓▓▓█▒█▒▒▒▒▒▒▒▒▓▓█▓▓           
\t\t\t\t\t     ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒█▓▓▒█▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓█        
\t\t\t\t\t       ▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▓█          
\t\t\t\t\t       ▒▒▒▓▓▒▒▒▒▒▒▒██▒▒▒▒▒▓▓▓▓▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓           
\t\t\t\t\t       ▒▒▒▒▒▒▒▒▒▒░▓██▒▒▒▒▒▓▓▓▓▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒█         
\t\t\t\t\t        ▒▒▒▒▒▒▒█░  ██▒▒▒▒▒▓▓▓▓▓▓▒▒▒▓▒▒▒▒▒▓▓▓▓▒▒▒█        
\t\t\t\t\t        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒█       
\t\t\t\t\t       █▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▓▓▓▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█       
\t\t\t\t\t      ░█░▓░░█▒▒▒█  █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t       █    ░    ▒▒▒▒▒▒▒▒▒▒▒▒██     █▒▒▒▒▒▒▒▒▒▒▓         
\t\t\t\t\t                █░█░░▒▒▒▒█             ▒█▒▒▓▓█           
\t\t\t\t\t                 ██                                      """+Fore.RESET,"Nidoran♂", "Veneno", "Pincho", "Primera", "Zona 1", "Bosque", "Bayas", "Piel venenosa"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t         ▒                                               
\t\t\t\t\t        ▒▒                                               
\t\t\t\t\t        ▒▒  █                            ░               
\t\t\t\t\t       █▒▒ ▓█              ▒           ░▒                
\t\t\t\t\t       ▓▒▒▒▒█             ▒▒         █▒▒                 
\t\t\t\t\t       ▒▒▒▒▒█             ▒▒       █▒▒▒      █           
\t\t\t\t\t      █▒▒▒▒▒▓        ▒   ▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒█▒▓            
\t\t\t\t\t      ▒▒▒▒▒▒▓▓       ▒█ █▒▒▒█▒▒▓▒▒▒▒▒▒▒▒▒▓▓█             
\t\t\t\t\t      ▒▒▒▒▒▒▓▓▓      ▒▒ ▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓█              
\t\t\t\t\t      █▒▒▒▒▒▓▓▒▒▓    ▒▒▓▒▒▒▒▒░▒▒▓▓▓▓▓▒▒▓▓▓               
\t\t\t\t\t      █▒▒▒▒▓▓▓▒▒▓    ▒▒▒▒▒▒▒█▒▓▓▓▓▓▓▓██▓▓▓▓▓             
\t\t\t\t\t       ▒▒▒▒▓▓▓▒▓█   ▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒██▓▓▓▓█             
\t\t\t\t\t       ▒▒▒▒▓▓▓▓▓  █▒▒▒▒▒▒▒▒█▓▓▓▓▓▒▒▒▒█▒▒▒▓▓▒▓█           
\t\t\t\t\t       ▒▒▓▓▓▓▓▓▓█▒▒▒▒▒▒▒░▒█▓▓▓▓▒▒▒▒▒▒▒▒▒▓▒▒▓▓▓▒█         
\t\t\t\t\t         ▓▓▓▓▓▓█▒▒▒▒▒▒▒█▒▒▓▓▓▓▓▒▒▒▒█▒▒▒▒▓▓▒▒▓▓▓▓█        
\t\t\t\t\t           ▓▓▓▒▒▒░░▒▓▓▒▒▒▒▓▓█▓▓▒█▒▒▒▒▒▒▒▒▓▓▒▓▓▓█▓█       
\t\t\t\t\t            █▒▒▒░▒▒▒▒▓▒▒▒▒▒▒▒██▓▓▒▒▓▓▓▒▒▒▒▒▓▓▓▓▓▓▒█      
\t\t\t\t\t           ▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▓▓▓▒▒▒▒▓▓▓█▓▓▓▓▓      
\t\t\t\t\t           ▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▓▓▓█  █░░▒▓░░     
\t\t\t\t\t           ▓▒▒▒▒▒▒▒▒▒▒▒▓░▒▒▒▒▒█▓▓▓▓▒█▒▓▓▒█               
\t\t\t\t\t         █▒░▒▒▒▒▒▒▒▒▒▒█░░▒▒▒▒▒█▓▓▓▓▒▒▒▒▒▓                
\t\t\t\t\t       █▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▓▓▓▓█▓▒▒▒▒▒▒▒                
\t\t\t\t\t           ▓█▒▒▒▒▒▒▒▒▒▒▒▓█░█▓▓▓█▒▒▒▒█▒▓▓▓▓               
\t\t\t\t\t          ▓▓▓▒▒▒▒▒▒▒▒▒▒█▓█        ▒▒▒▒▓▓▓▓█              
\t\t\t\t\t         ░░▓██░▒▒▒▒▒▒▒▓▓           ▒▒▓▒▒▓▓▓              
\t\t\t\t\t        █      ▒▒▒█                 ▒▒▓▒▓▓▓█             
\t\t\t\t\t                                    ░░▒█░░█              
\t\t\t\t\t                                        ▓                """+Fore.RESET,"Nidorino", "Veneno", "Pincho", "Primera", "Zona 1", "Bosque", "Bayas", "Piel venenosa"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t          ▓█           ▒  ▒▒▒▒▒▒                         
\t\t\t\t\t        ▓▓▓█▓█        █▒▒▒█▓▓▓▓▒                         
\t\t\t\t\t         ▓▓▓▓█▓  ▒▒ █▒▒▒█▓▓▓▓▓▓▓  █▒                     
\t\t\t\t\t          ▓▓▓▓▓▓ █▒▒▒▒█▓▓▓▓▓▓▒▒█▓▓▓                      
\t\t\t\t\t           ▒▒▓▓▓▒▒▒▒▒▒█▓▓▓▓▓▒▒█▓▓▓▓      ▓           ▒▒  
\t\t\t\t\t            ▓▒█▒▒▒▒▒▒▒▒▒▒▓█▒▓▓█▒▒▒▒▒▒▓▓░▒▒▒▒         ▒▒█ 
\t\t\t\t\t          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒      ▒▓▓ 
\t\t\t\t\t    █▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒░▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒   █▒▓▓█
\t\t\t\t\t  ▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒██▓▓█▒▒▒▓░░▒▓▒▒  ▓█▓▓▓
\t\t\t\t\t ▒▒░█▒▒▒▒▒▒▒█ █▓▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒█▒▒▒█▓▓▓   ▒▒▒▒▒▒░░ ▒▒▓▓▓▓
\t\t\t\t\t▒░▒░▒▒▒▒▒      █▓░▒██▒▒▒▒▒▒▒▒▒▒░▒▒▓▓▓▓▓█  ▒▒▒▒▒▒▒▓▒▒▓▓▓▓█
\t\t\t\t\t   █▒▒▒           ░░░░░▓░░░░░░░▒▒▒▓▓▓▓▓▓▓▓   ▒░░▒▒▓▓▓▓▓▓ 
\t\t\t\t\t    █              █▒▒▒▒▒▒▒▒▒▒█▒▒▒▒███▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓█ 
\t\t\t\t\t                  ▒▒▒▒░░░░░█▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█  
\t\t\t\t\t              ▒▒▒▒▒█░░░░░░░░░░░░▒▓▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓█    
\t\t\t\t\t             █▒▒▒▒▒▒░░░░░░░░░░░░▒██▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓█     
\t\t\t\t\t             █▒▒▒▒▒▓▓█▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓█▓█       
\t\t\t\t\t              ▒▒▒█▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▒          
\t\t\t\t\t              ░░░▓▓▓▓▓▓█     █▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t           ░░░░░░▓                ▒▒▒▒▒▒▒▒▒▒▒█           
\t\t\t\t\t                                  ▒▒▒░░░░░▒▒▒            
\t\t\t\t\t                                     ░░░░░░              """+Fore.RESET,"Nidoking", "Veneno", "Taladro", "Primera", "Zona 1", "Bosque", "Bayas", "Piel venenosa"),
            Pokemon(Fore.LIGHTMAGENTA_EX+"""\t\t\t\t\t        █▓▒▒▒▒█                                          
\t\t\t\t\t        █▓▓▓▒▒░░░░█     █░░░░░░░▒                        
\t\t\t\t\t        ██▓▓▓░░░░░░░░██░░░░░░░░░░░░                      
\t\t\t\t\t        ████░░░░░░░░░█░░░░░░░░░░░░░░███▒░░░░░░▒███       
\t\t\t\t\t        ███░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░█▒▒▓▓▓█    
\t\t\t\t\t         █▓█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓██     
\t\t\t\t\t       ░▓██▓░░░░░░░░░░█░░░░░░░░░█░░░░░░░░░░░░░░▓▓██      
\t\t\t\t\t   █░░░░░░░▓█░░░░░░░░░░░▓░░░░░░█░░░░░░░░░░░░░░░████      
\t\t\t\t\t    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████       
\t\t\t\t\t    █░░░░░░░░█░░░░░░█░██░░░░░░░█░░░░░░░░░░░█░██▓         
\t\t\t\t\t     ░░░░░░░░░░░░░░░░█░░░░░░░░░▓░░█░░░░░░░░░▓▓▓          
\t\t\t\t\t     █░░░░░░░░░░░█░░█░░░█▒██░▒░░░░░░░░░░░░░░█   ░░       
\t\t\t\t\t      ░░░░░░░░░░░░░░░░░░█▒▒▒▒░░░░█░░░░░░░██░░░░░░░░░░    
\t\t\t\t\t       ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░    
\t\t\t\t\t       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█    
\t\t\t\t\t       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░       
\t\t\t\t\t       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒█       
\t\t\t\t\t       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█▒▒▒▒       
\t\t\t\t\t        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒       
\t\t\t\t\t        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒       
\t\t\t\t\t        █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒        
\t\t\t\t\t         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▒▒▒▒▒         
\t\t\t\t\t         █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▒▒▒▒▒          
\t\t\t\t\t          █░░░░░░░░░█▒░░░░░░░░░░░░░░░░░░█▒▒▒▒            
\t\t\t\t\t           █░░░░░░░░░       ░░░░░░░░░░░▒▒█               
\t\t\t\t\t            █▓░░█░░          █░░░░░░░▒                   
\t\t\t\t\t              ██                ███                      """+Fore.RESET,"Clefairy", "Hada", "Hada", "Primera", "Zona 1", "Bosque", "Bayas y néctar", "Protección contra depredadores"),
            Pokemon(Fore.LIGHTMAGENTA_EX+"""\t\t\t\t\t        ▒▓                                               
\t\t\t\t\t         ▓▓▓▓█                                           
\t\t\t\t\t          ▓▓░░░░░                                        
\t\t\t\t\t           ▓░░░░░░░░      ░░░░░█                         
\t\t\t\t\t            ░░░░░░░░░░█ ░░░░░░░░░░█         █░██▓▓▓▓▒    
\t\t\t\t\t     █░▒▒    ░░░░░░░░░░░░░░█░░░░░░░░█░░░░░░░░░░░░▓▓      
\t\t\t\t\t      █▒▒▒▒▒  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▓        
\t\t\t\t\t        ▒█░▒▒▒█▓░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░█          
\t\t\t\t\t   ░▒█  █░░░░░▒▒█░░░░░░░░░░░░░░░░░░░░░░░░░░░    █▒░░░    
\t\t\t\t\t    ▒▒▒▒░░░░░░▒▒░░░░░░░▒░░░░░░░░░░░░░░░░░█  █▒▒▒▒▒▒      
\t\t\t\t\t      █▒▓░░░░░░░░░░░░░░░█░░░░░▒░█░░░░░░░█▒▒▒▒▒▒▒▒        
\t\t\t\t\t         ▓░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░█░░█       
\t\t\t\t\t        █ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░▒▒▒▒▒▒   
\t\t\t\t\t      ▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░▒▒█      
\t\t\t\t\t           █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██         
\t\t\t\t\t            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▒▒▒▒▒░░      
\t\t\t\t\t            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█        
\t\t\t\t\t            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░        
\t\t\t\t\t            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░        
\t\t\t\t\t            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░        
\t\t\t\t\t            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░▒        
\t\t\t\t\t            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒█▒▒▒░█        
\t\t\t\t\t             ░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒         
\t\t\t\t\t             ░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒█          
\t\t\t\t\t              ░░░░░░░░░▒ █▒▒▒░░░░░░░░░░▒▒▒▒▒▒            
\t\t\t\t\t              █░░░░░░░░     ▒░░░░░░░░░▒▒▒▒█              
\t\t\t\t\t               █░░░░░░█       ░░░░░░░                    
\t\t\t\t\t                  █▒█         ░░░░░█                     """+Fore.RESET,"Clefable", "Hada", "Hada", "Primera", "Zona 1", "Bosque", "Bayas y néctar", "Protección contra depredadores"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t           ▒▒▓▒▒▒▒▒▒█                                    
\t\t\t\t\t   ▒█     ▒▒▒▒▒▒▒▒▒▒▒▒▒                                  
\t\t\t\t\t  ██▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                                
\t\t\t\t\t   ██▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                                
\t\t\t\t\t   ▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓█▒▒▒▒▒██      █▒▒▒▒▒▒▒▒▒              
\t\t\t\t\t   █▓█▒▒▒▒▒▒▓███▒▒▒▒▒▒▒▒███▓▓▓ █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t    ▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▓████▓▓▓▓██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      
\t\t\t\t\t   █▒▒▒▒▒▒▒░▓▓▓▒▒▒▒▒▒█▓▓▓▓█ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     
\t\t\t\t\t ░▓▒▒▒▒▒▒▒▓▓▓▒▒▓▒▒▒▒█▓▓▓█ █▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒    
\t\t\t\t\t ▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒   ▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▓▒▒    
\t\t\t\t\t  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  █▒▒▒▒▒▓█▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒   
\t\t\t\t\t   █▒▓█▒▒▒▒▒▒▒▒▒▒▒▒▒█    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█ 
\t\t\t\t\t     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      ▒▒▓▓▒▒▒▒▓▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 
\t\t\t\t\t         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒█   █▒▒▒▒█▓█▓▓▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▓
\t\t\t\t\t          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▓
\t\t\t\t\t          ▒░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 
\t\t\t\t\t          ▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  
\t\t\t\t\t          █▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒█▒▒▒▒▒▒▒▒▒█    
\t\t\t\t\t           ▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    █▒▒▒▒▒▒▒▒▒█     
\t\t\t\t\t            ▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      ▒▒▒▒▒▒▒█      
\t\t\t\t\t             ▒▒▒▒▓▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒        █▓█         
\t\t\t\t\t             ▓▒▒▒█▒▒▒▒▒▒  █▓▓▓▓█▒▒▒▒▒▒                   
\t\t\t\t\t             █▓▓▓▓▓▓▒▓▒█  ▓▓▓▓   ▒▒▒▒▒                   
\t\t\t\t\t             █▓▓▓▓▓▓▓▓▓ ▒▓▓▓▓▓   ▓▓▒▒█                   
\t\t\t\t\t            ▓▒█▒▓▓▓▓▓▓   █▓█    ▓▓▓▓▓                    
\t\t\t\t\t               █▓▓▓▓▓          █▓▓▓▓                     """+Fore.RESET,"Vulpix", "Fuego", "Zorro", "Primera", "Zona 1", "Bosque", "Bayas", "Poder de fuego"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                                           █▒            
\t\t\t\t\t                  █░░░░░░░█           ▒░░░░░░░░░░░░░     
\t\t\t\t\t                ░░░░░░░░░░░░░       ░░░░░░░░░░░██        
\t\t\t\t\t            ░░░░░░░░█░░░░░░░░░   █ ░░░▒░░░░░░░░░░░░█     
\t\t\t\t\t         ░░░░░░░░░░░░░█░░░░░░░░   ░░░░░░░░░░░░░    ░░█   
\t\t\t\t\t        ░░░░░░░░░░░░░░░░░░░░░░░█░  ░░░░░░░█░░░░░█     ░  
\t\t\t\t\t       ░░░░░░░░░░░░░░░░░░░░░░░░█▓░░░░░░░░░░  ▒░░▓█       
\t\t\t\t\t      ░░░░░░░█░░░░░░░░░░░░░░░░░░░░█░░░░░░░░█   ░░        
\t\t\t\t\t    ░░░░░░░░░░░█░░░░░░░░░░░░░░░▒▒▒█░░░░░░░░░   █░        
\t\t\t\t\t   ░░░░░░░░░░░░░░░░░░░░░▒░░░░▒▒▒▒▒█  ░░░░░░░░            
\t\t\t\t\t  ░░░░░░░░░░░░░░░█░░░░░░░░░░▒▒▒▒▒▒▒█░░░░░░░░░            
\t\t\t\t\t  ░░░░░░░░░░░░░░░░░░░░░█░░▒█▒▒▒▒█▒▒░░░░░░░░░░█           
\t\t\t\t\t  █░░░░░░░░░░░░░░░░░░░░▒▒▒█▒▒▒▒▒▒▒▒░░░░░░░░░░░           
\t\t\t\t\t   ░░░░░░░░░░░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░           
\t\t\t\t\t    ░░░░░░░░░░░░▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░░█           
\t\t\t\t\t     █░░░░░░░░▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒░░░░█░░░░░░░░▓            
\t\t\t\t\t       █▓███░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░             
\t\t\t\t\t   █░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓░░░░░░░░░▒▒██░░             
\t\t\t\t\t  ░░░░░░░░░░░░░░░░░░▒▒▒▒▒▓▒░░░░░▒▒░░░░██░░░              
\t\t\t\t\t █░░░░░░░░░░░░░░░░░░░█▒▒██░░░░░░▒▒░░░█▒░░░█              
\t\t\t\t\t  ░░░░░░░░░░░░░░░░░▒░░░░▒░░░░░░█░░░░░░░░░░░░░░█          
\t\t\t\t\t   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▒▒█  █▒▒▒▒        
\t\t\t\t\t     ░░░░░░░░░█░░░░░░░░░█░░░░░░░░░▒▒█▒▒▒▒       ▒▒       
\t\t\t\t\t         ░░░░░░░░░░░░░░░░░░░░░█  █░░  ▒░░         ░      
\t\t\t\t\t           ░░░░░░░░░░░░░░░░░░░░▒▒▒░░  ░░░░               
\t\t\t\t\t                █░░░░░░░░░░░░░▒▒▒▒▒▒▒   █                
\t\t\t\t\t                                   █▒▒█                  
\t\t\t\t\t                                       █                 """+Fore.RESET,"Ninetales", "Fuego", "Zorro", "Primera", "Zona 1", "Bosque", "Bayas", "Poder de fuego"),
            Pokemon(Fore.LIGHTMAGENTA_EX+"""\t\t\t\t\t               ▓█                                        
\t\t\t\t\t              █░░░░░▒                                    
\t\t\t\t\t              ░███░░░░░█                                 
\t\t\t\t\t             ░░█████░░░░░█  █░░░░░▒                      
\t\t\t\t\t             ░███████░░░▓░░░░░░░░░░░░█                   
\t\t\t\t\t            █░▓▓▓█░░░░░░░░░░░░░░░░░░░░█                  
\t\t\t\t\t            ▒▒█░░░░░░▓░░░░░░░░░░░░░░░░░█                 
\t\t\t\t\t            ▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██           
\t\t\t\t\t           ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█     
\t\t\t\t\t          ░░░░░     ░░░░░░░░░█▒▓▒▒▒░░░░░░░░████████░░█   
\t\t\t\t\t         ░░░▒ ░▓▓▓▒ ▓█░░░░░░░▒▒█▒░░░░░░░░░░░███████░█    
\t\t\t\t\t        █░░█░░▓▓▓▓▓▓▓█░░░░░░░▒▓▒░░░░░░░░░░░░░████▒░█     
\t\t\t\t\t        ░░░▓░░▓▓▓▓▓▓▓░░░░▒▒▒▒▒▒░▓    ░░░░░░░░▓▓█▒░       
\t\t\t\t\t        ░░░░░░▒▒▒▒▒█░░░░░░░░░░░ █▓▓▓ ░░░░░░░░█▒░         
\t\t\t\t\t        ░░░░░▒░░░░█░░░░░░░░░░░ █▓▓▓▓▓▓▓█░░░░░▓           
\t\t\t\t\t   █░░░░▒▒░░░░░░░░░░▒░░░░░░░░░░█▓▓▓▓▓▓▓▒░░░░░            
\t\t\t\t\t     ░░░░▒▒░░░░░░░░░░░█░░░▓░░█░░▓▒▒▒▒▒░░░░░░▒            
\t\t\t\t\t       █▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░█░█░░░░░░             
\t\t\t\t\t          ░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒              
\t\t\t\t\t           ▓▒▒▒▒░░░░▒░░░░░░░░░░░░░░░░░░░░░               
\t\t\t\t\t             ▒▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒█░░░░░▒░█                
\t\t\t\t\t            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░█                  
\t\t\t\t\t         █░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒                    
\t\t\t\t\t         ░░░░░░░▒█    █▓▒▒▒▒▒▒█▒▒▒░░░░█                  
\t\t\t\t\t                               █▒░░░░░░░                 
\t\t\t\t\t                                   ████                  """+Fore.RESET,"Jigglypuff", "Normal", "Globo", "Primera", "Zona 1", "Pradera", "Bayas y frutas", "Canto hipnótico"),
            Pokemon(Fore.LIGHTMAGENTA_EX+"""\t\t\t\t\t                                            ▓░▒          
\t\t\t\t\t        ░░░░░░▓                           █░░░▓          
\t\t\t\t\t         ░░████░░░                       ░░█░░█          
\t\t\t\t\t          ░░▓▓▓███░░          ░░░░░░░  █░▒██▒░           
\t\t\t\t\t           ░░█▓▓████░▓        ░░░░░░░░█░▓██▓░█           
\t\t\t\t\t             ░░█▓████░░ ▒░░░░░░░░░░░░░░▒███░░            
\t\t\t\t\t               ░░░████▒░░░░░░░░░░░░░░░░█▓▒░█             
\t\t\t\t\t                  █░░░▒░░░░░░░░░░░░░░░░▒▒█               
\t\t\t\t\t                   ░░░░░░░░   ░░▒██▓░░░░░█               
\t\t\t\t\t                  ░░░░░░░ █ ░▓▓▓░░░░░░ ▓▓▓               
\t\t\t\t\t                 █░░░░░░▓ ▓▓▓▓▓░░░░░░░█▓▓░░              
\t\t\t\t\t                 ░░░░░░░░░░▓▒▒█░░░░░░░░░░▓░█             
\t\t\t\t\t                 ░░░░░░░░░░▒░░░░░▒▒▒▒▒░░░░░░█░░░▒        
\t\t\t\t\t                █░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒         
\t\t\t\t\t                ▒░░▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓          
\t\t\t\t\t                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░            
\t\t\t\t\t                ▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░            
\t\t\t\t\t               █▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒░            
\t\t\t\t\t               ▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░▒█            
\t\t\t\t\t                ▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒             
\t\t\t\t\t                 ░▒▒▒░░░░░░░░░░░░░░░░░░░░░█              
\t\t\t\t\t                   ░▒▒░░░░░░░░░░░░░░░░░░▓                
\t\t\t\t\t                     ▓▒░░░░░░░░░░░░░░█                   
\t\t\t\t\t                    █▒▒▒▒▓       ▒▒▒░░░░░░               
\t\t\t\t\t                    ░░░░░░          ██▒░▒█               
\t\t\t\t\t                    █░░░░░                               """+Fore.RESET,"Wigglytuff", "Normal", "Globo", "Primera", "Zona 1", "Pradera", "Bayas y frutas", "Canto hipnótico"),
            Pokemon(Fore.BLUE+"""\t\t\t\t\t                     █▓▒▒                                
\t\t\t\t\t                █▓▓▓▓▓▓▓                                 
\t\t\t\t\t             ▓█▓▓▓▓▓▓▓▓█                                 
\t\t\t\t\t          ▒█▓▓▓▓▓▓▓▓▓▓▒   ▒                              
\t\t\t\t\t        ▓▒▓▓▒▓▓▓▓▓▓▓▓▓▒  ▓▓▓▒                            
\t\t\t\t\t      ▓▒▒▒▒▒▒▓▓▓▓▓▓▒█▓▓  ▓▓▓▓▒                           
\t\t\t\t\t    ▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓  █▓▓▓█▒                    ██    
\t\t\t\t\t   █▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██ █▓▓▓▓▓▒▒▒█   ██▒▒▒█       ▒▒    
\t\t\t\t\t █▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓  █▓██████░▒▓▓▓▓▓▓▓▓▓     ▒▓█▒   
\t\t\t\t\t █       █▒▒▓▓▓▓▓▓▓▓▓▓▓▓█ ███████████▓▓▒▒▒▒▓    ██▓▓▓▓   
\t\t\t\t\t           █    █▓▓▓▓▓▓▓▓█▒░▓▓▓██████▓▒▒▒▓     ▓▓▓▓▓▓▓▓  
\t\t\t\t\t                     ▓▓▓█▓▓▒▒▒▒▒█░█▓        ▓██▓▒▒▒▒▒▓▓  
\t\t\t\t\t                       ▓▓▓▓▓▒▒▒▒▓▓▓    █▓▓▓▓▓▒▓█▒▒▒▒▒▒▒  
\t\t\t\t\t                       █▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▒▒▒▒▒▒▓▒▒▒▒▒▒██ 
\t\t\t\t\t                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒█ 
\t\t\t\t\t                       █▓▓▓▓▓▓▓▓█      ▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒█ 
\t\t\t\t\t                      █▓     ▓▓          ▒▒▒▒▒▓▒▒▒▒▒▒▒▒█ 
\t\t\t\t\t                     █       ▓█            ▒▒▒▒▒▒▒▒▒▒▒█  
\t\t\t\t\t                    ▓        ▓              ▒▒▒▒▒▒▒▒▒▒▒  
\t\t\t\t\t                   ▒         ▓              ▒    ▒▒▒▒▒▒  
\t\t\t\t\t                  ▒          █                     ▒▒▒   
\t\t\t\t\t                 ▓           █                      ▒▒   
\t\t\t\t\t                █           ▓                        ▒    
\t\t\t\t\t                            █                            
\t\t\t\t\t                            ▓                            
\t\t\t\t\t                            █                            """+Fore.RESET,"Zubat", "Veneno", "Murciélago", "Primera", "Zona 1", "Cueva", "Frutas", "Supersonido"),
            Pokemon(Fore.BLUE+"""\t\t\t\t\t  ▒█                                                     
\t\t\t\t\t   ▒▓▒█                                                  
\t\t\t\t\t    ▒▒▒▒▒                                        █▒▒▓▓█  
\t\t\t\t\t     ▒▒▒▒▒▒                                 █▒▓▓▒▒▒▒     
\t\t\t\t\t      ▒▒▒▒▒▒▒                            ▒▒▓▒▒▒▒▒▒       
\t\t\t\t\t      ▒▒▒▒▒▒▒▓▓                       █▓▓▒▒▒▒▒▒▒▒        
\t\t\t\t\t      █▒▒▒▒▒▒▒▓██                   ▒█▓▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t      █▒▒▒▒▒▒▒▒██▓                ▒█▓▒▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t      ▒▒▒▒█▓▓▓▓▓                 ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t     █▒▒▓▓▓▓▓▓▓                  ██▓▒▒▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t     ▓▓▓▓▓▓▓▓▓    █▒   █▓▓        ▒▓▓█▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t   █▓▓▒▒▒▒▒▒▓▓  ░█▒▒▒▒▒▓█▓▓       ▒▓▓▓▓▓█▒▒▒▒▒▒▒█        
\t\t\t\t\t  ▓▒▒▒▒▒▒▒▒▓▓▓ ▓░▓▓▒▒▒▒▓▓▓▓▓      ▒▓▓▓▓▓▓▒▒▒█▒▒▒▒        
\t\t\t\t\t█▒▒▒▒▒▒▒▒▒▓▓▓█ ████████░█▓▓▓     ▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t     ▒▒▒▒▒▓▓▓▓█▓█████████▓▓▓▓ █▒█▒▒█▓▓▓▓▒▒▒▒█            
\t\t\t\t\t       ▒▒█▓▓▓▓▓▓█████████▓▓▓▓█▓▓▒▒▒▒▓▓▓▓▓▒█              
\t\t\t\t\t        ▒▓▓▓▓▓▓▓▓▓███████▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓                
\t\t\t\t\t         ▓   ▓▓▓▓▓▓██████▓▓▓▓▓▓▒▒▒▒▒█▓▓▓                 
\t\t\t\t\t               ▓▓▓▓██████▓▓█▓██  █▒▒▒▓▓█                 
\t\t\t\t\t       █▒▒    █▓▓███████▓▓▓▓          ▓                  
\t\t\t\t\t         ▒▒  ▒▒█████░██▓▓▓▓ █▒▒                          
\t\t\t\t\t          ▓█▓▓▒█████▓▒▓▓▓█ ▓▓▒                           
\t\t\t\t\t          ▓▓   █▓▒▒▓▓▓▓▓ ▓▓▓█                            
\t\t\t\t\t          ▓▓             ▓▓█                             
\t\t\t\t\t                         ▓█                              
\t\t\t\t\t                        █▓                               """+Fore.RESET,"Golbat", "Veneno", "Murciélago", "Primera", "Zona 1", "Cueva", "Frutas", "Supersonido"),
            Pokemon(Fore.LIGHTGREEN_EX+"""\t\t\t\t\t             █                                           
\t\t\t\t\t             ▒▒              █                           
\t\t\t\t\t            ▒▒▒▒█          ▓█▓                           
\t\t\t\t\t            ▒▒▒▒▒▒      █▓▓▓▓█                           
\t\t\t\t\t            ▒▒▒▒▒▒▒   █▓▓▓▓▓▓█   ▒▒▒▒▒▒▒▒▒▒▒▒▓           
\t\t\t\t\t           █▒▒▒▒█▒▒▒ ▓▓▓█▓▓▓█▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▓▓█          
\t\t\t\t\t           ▒▒▒▒▒▒▒▒▒▒▓▓█▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ █▓▒          
\t\t\t\t\t           █▒▒▒▒▒█▒▒▒▓▓▓▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒    ▓          
\t\t\t\t\t            ▒▒▒▒▒▒▒▒▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓█       
\t\t\t\t\t             ▒▒▓▒▒█▓▓▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓█   
\t\t\t\t\t              █▓▓▓▓▓█▓▓▓▓▓▓▒▒▒▒▒▒▒▒█▓▒▒▓███▓▓▓▓▓█        
\t\t\t\t\t                 ▓▓▓▓▓█▓▓▓▓▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t            █▒▒▒▒▒▒▒▒▒▒▓▓█▒▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█   
\t\t\t\t\t          ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t        █▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█         
\t\t\t\t\t        ▓▓▓▓▓▓▓▒▒▒▒▒▒█▓▓▓▓▓▓▓▓  █▒▒▒▒▒▒▒▒▒▒▒█            
\t\t\t\t\t       █▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓                          
\t\t\t\t\t       █▓▒▓▓▓▓▓▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓                          
\t\t\t\t\t        ▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                          
\t\t\t\t\t         ▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                          
\t\t\t\t\t           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                           
\t\t\t\t\t             █▓▓▓▓▓▓▓▓▓▓▓▓▓▓█                            
\t\t\t\t\t           ▓▓▓▓▓▓ █▓▓▓▓▓█                                
\t\t\t\t\t          ▓▓▓▓▓▓▓   ▓▓▓▓▓█                               
\t\t\t\t\t          ▓▓▓▓▓▓   ▓▓▓▓▓▓█                               
\t\t\t\t\t          █▒▒▓▓    ▓▓▓▓▓▓                                
\t\t\t\t\t                   ▓▓▓▓▓█                                
\t\t\t\t\t                    █▒▒█                                 """+Fore.RESET,"Oddish", "Planta", "Semilla", "Primera", "Zona 1", "Bosque", "Hojas", "Exposición a la luz lunar"),
            Pokemon(Fore.BLUE+"""\t\t\t\t\t                          █▓▒▒▒░▓▒▓                      
\t\t\t\t\t                    █▓▓▒▒▓█▓▓▓▓▓▓▓▓▓██                █  
\t\t\t\t\t                  ▒▒▒▓▓▒▒▓▓▓█▒▒▒█▓▒▓▓░▓▓▓▓            █▒ 
\t\t\t\t\t                █▓░▒▒░▓▓▓▓█▓▓▓▓▓▓█▓▓░▓▓▓▓▓▓█          ▒▒█
\t\t\t\t\t          █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▒▓▓▓░▒▓▓▓▓█        ▒▒▒▒
\t\t\t\t\t       ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓      █▒▒▒▒█
\t\t\t\t\t     ▒▒▒▓▓▓▓▓▓▓▓█▓▓▓▓▓█▓▓▓▓▓░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓█   ▓▓▓▓▒▒▒▒ 
\t\t\t\t\t   ▒▒▒▒▒▓▓▓▓▓▓▓▓▓█▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
\t\t\t\t\t  ▒▒▒▒▒▒▒█    █▒▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓█   
\t\t\t\t\t ▒▒▒▒       █▒▒▒▒▒▒▒▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█▓██▓▓▓▓▓▓▒▒█▓▓▓█     
\t\t\t\t\t█▒▒        ▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓█▓▓▓█▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒        
\t\t\t\t\t█▒        ▓▒▒▒▒▒▒█▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒▒█      
\t\t\t\t\t█▓        ▒▒▒▒▒█ ▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓ █▒▒▒▒▒▒      
\t\t\t\t\t ▒▓▓███   ▒▒▒▒  █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓█▓▓▓▓▓   █▒▒▒▒█     
\t\t\t\t\t   ██     ▒▒▒   ▒▒▒▒▒▓▓█░░░░░░█▒▒▒█▓▓▓▓▓▓▓▓    █▒▒▒█     
\t\t\t\t\t           ▒█   ▓▒▒▒▒▓▓█▓▓▓▓▓█░░░▓▓▓▓▓▓▓▓▓▓      ▒▒█     
\t\t\t\t\t            █   █▓▒▒▒▒▒▒▒▒▒▒▒▓▒░░▓▓▓▓▓▓▓▓▓▓      █▒      
\t\t\t\t\t              ▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▒░▓▓▓▓▓▓▓▓▓▓▒▒█            
\t\t\t\t\t           █▒▒▒▒▓ █▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒         
\t\t\t\t\t            ▒▒▒     █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█   █▓▓▒▒▓         
\t\t\t\t\t                       ▓█▓▓▓▓▓▓▓▓▓█                      
\t\t\t\t\t                     █▓▓▓        █▓▓█                    
\t\t\t\t\t               █▒▒▒▒▓▓▓▓          ▓▓▓▓▓▒▒▒█              
\t\t\t\t\t              ▓▒▒▒▒▒█                █▒▒▒▒▒▒             """+Fore.RESET,"Gloom", "Planta", "Flor", "Primera", "Zona 1", "Bosque", "Hojas", "Exposición a la luz lunar"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t                                        █                
\t\t\t\t\t                                 █▒▒░▒▒▒▒▒▒▒▒▒▒▒▒█       
\t\t\t\t\t                             █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     
\t\t\t\t\t                    █▒▒▒▒▒▒█▒▒▒░░▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒   
\t\t\t\t\t                 ░▒▒▒░░▒▒▒█▒▒▒▒▒▒▒▒▒▓▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█ 
\t\t\t\t\t              ▒▒▒▒▒▒▒▒▒▒█▒▒██▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 
\t\t\t\t\t            ▒▒▒▒▒░▒▒▒█▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒░░▒▒▒▒▒▒▓ 
\t\t\t\t\t           ▒▒▒▒▒▒▒▓█▓██▒▒█▒▒▒▒█▒▒▒▒▒▒░▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▓  
\t\t\t\t\t          █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓   
\t\t\t\t\t       ▒▒░░░▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▓▓    
\t\t\t\t\t     ▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒█▒▒▒▒░░▒▒▒▒▒▒▒▓▓      
\t\t\t\t\t   █▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▓▓▓        
\t\t\t\t\t  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒░░░░░▒▒▒▒▒█▒▒▒▒▓▓▓█          
\t\t\t\t\t ▒▒▒▒░░░▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓█             
\t\t\t\t\t ▒▒▒▒▒▒▒▒▒▒█▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓▓▓               
\t\t\t\t\t█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒░░░▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓█              
\t\t\t\t\t ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓█▓▓▓▓▓▓▓▓              
\t\t\t\t\t  █▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓█▓▓▓▒▒▓▓▓▓▓▓▓▓             
\t\t\t\t\t      █████▓▓▓▓▓▓▓▓▓▓▓▓██▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       
\t\t\t\t\t                    ▓▓▓▓▓▓▓▓▓█▓█▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓█       
\t\t\t\t\t                   ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓             
\t\t\t\t\t              ▒▒▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              
\t\t\t\t\t                ██    ▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█               
\t\t\t\t\t                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                  
\t\t\t\t\t                           ▓▓█        ▓▓█                
\t\t\t\t\t                    █▒▒▓▓▓▓▓█         █▓▓▓▓▓▓▓▓          
\t\t\t\t\t                   ▓▒▒▒▓▓▓               ▓▓▓▒▒▒▓         """+Fore.RESET,"Vileplume", "Planta", "Flor", "Primera", "Zona 1", "Bosque", "Hojas", "Exposición a la luz lunar"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t                █▒░░░▒▒▓▓                                
\t\t\t\t\t              █▒▒▒░▒▒▒▒▒▓▓             ██▓▒▓█            
\t\t\t\t\t             ▒▒▒▒▒▒▒▒▒▒░░▒          ▒▒░░░░▒▒▒▒▒█         
\t\t\t\t\t            █░░▒▒░░▒▒▒▒▓▒█        █▒▒▒▒▒▒▒▒▒▒▒░░░        
\t\t\t\t\t            █░▒▒▒▒▒▒▒▒▓▓██▒▒▒▒▒▒▒██▓▒░░░▒▒▒▒▒▒▒░░        
\t\t\t\t\t             ▒▒░░▒▓▒▓█▒▒▒▒▒▒▒▒▒▒▒▒▒█▓░░▒▒▒▒▒▒░▒▒▒█       
\t\t\t\t\t                   ▒▒▒█▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒░░░░▓▓       
\t\t\t\t\t                  ▒█▒░░░░░░░▒█▒▒▒▒▒▓▒▒▒█▒▒▓▒▒░░▒▒        
\t\t\t\t\t             ░░░░░▓░░░░░▒░░░░░▒▒▓▒▒▒▒▒▒▒▒▓▓█▓▓██         
\t\t\t\t\t        ▒▒▒█░░░███░█░░░░░░░▒▒▒░░░░░▒▒▒▒▒▒▓▓▓▓            
\t\t\t\t\t     █░░░░▒█░█████░█▒▒▒▒▒▒░▒▒░ ░██░░█▒▒▒▓▓▓▓▓            
\t\t\t\t\t   █░░░░▒▒▒▒▓░█▓█░█▒▒▒▒▒▒▒▒▒░░█████░░▒▒▓▓█▒▓▓ █ ▓▓█      
\t\t\t\t\t  █░░░▒▒▒▒▒▒▒█▒▒▒▒▒▓▒▒▒█▒▒▒▒█░░▓▓▓░░█▒▒▒▒░░▒▒█▓▓▓▓▓▓▓█   
\t\t\t\t\t █▒▒▒▒▒▒▒▒▒▒▒█▓▒▒▒▒▒░▒▒▒▒▓▒▒▒▒░░░░░▒▒▒▒▒▒░░▒▒▓▓▒▒  █▓▓▓█ 
\t\t\t\t\t ▒▒▒▒▒▒▒▒▒▒▒▓   ▒░░█▒▒▒▒▓░░▒▒▒▒▒▒▒▓▒▒▒▒▒▒░░▒▒▒█▒▒▒▓   █▓ 
\t\t\t\t\t█▒▒▒▒▒▒▒▒▒▒▒    ▓█░░██▓░░░▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▓  █▒▒▒▒  ▓█
\t\t\t\t\t█▒▒▒▒▒▒▒▒▒▒        ██ ▒▒█▒███   █▒▒▒▒▒▒▒▒▒▒▒▒█     ▓▓█   
\t\t\t\t\t█▒▒▒▒▒▒▒▒▓                      ▒▒▒▒▒▒▒▒▒▒▒▒▒      █▓█   
\t\t\t\t\t ▒▒▒▒▒▒▒█                      █▒▒▒▒▒▒▒▒▒▒▒▒        ▓    
\t\t\t\t\t █░▒▓▒▒█                       ▒▒▒▒▒▒▒▒▒▒▒▒              
\t\t\t\t\t  █▒▒▒█                        ▒▒▒▒▒▒▒▒▒▒▒               
\t\t\t\t\t   █▒▒█                        █▒▒▒░▒▒▒▒                 
\t\t\t\t\t                                ▒▒░▒▒▓                   
\t\t\t\t\t                               █▒▒▒█                     
\t\t\t\t\t                                █                        """+Fore.RESET,"Paras", "Bicho", "Champiñón", "Primera", "Zona 1", "Bosque", "Hojas", "Absorber"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t                                █▓▒▒▒▒█                  
\t\t\t\t\t                            █▒▒▒▒▒▒▒▒▒▒▒▒▓               
\t\t\t\t\t                          █░░░░░▒▒▒▒▒▒▒▒▒▒▓▓             
\t\t\t\t\t                         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓            
\t\t\t\t\t                       █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓           
\t\t\t\t\t                      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓          
\t\t\t\t\t                    ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓          
\t\t\t\t\t                  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓█         
\t\t\t\t\t              █▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒         
\t\t\t\t\t           █▒▒▒▒▒▒▒▒▒░░░░▒▒▒░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒         
\t\t\t\t\t         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒█        
\t\t\t\t\t        ▓▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒        
\t\t\t\t\t        ▒▒▒▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒       
\t\t\t\t\t       █░▒▒▒▒▒▒▓▓▓░░░░█▓█░░░░▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒      
\t\t\t\t\t     ▒░░▒▒▒▒▒▒▒▓██░░░░▒▒░░░░░██▓▓▓▓▓▓▒▒▒█▓▓▓▓▓▓▓▓▒▒▓     
\t\t\t\t\t    ▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒░░░▒██▒▒▒████▒▒░░▒▒▒▓▓▓▓▓▓▓▓▒▒▓    
\t\t\t\t\t   ▒▒▒▒▒▒▒▒▒▒▒▒█▓██▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒░░▒▒▒██▓▓▓▓▓▓▒▒▒    
\t\t\t\t\t  ▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▒▒▓█▓█▓▒█▓█▒▒▒▒▒▒▒▒▒▒▓███▒▓█▒█▓█    
\t\t\t\t\t █▒▒▒▒▒▒▒▒▒▒▓▒▓   ▓▓▓ ▒▓▓▓▓▓▓▓█▒▒▒▒▒▒▒▒▒▒▒██▓▒▒▓▓▒▒▒     
\t\t\t\t\t ▒▒▒▒▒▒▒▒▓▒█▒   █▓▓       █▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒█   ▒▒█ █▒▒█   
\t\t\t\t\t ▒▒▒▒▒▒▒  ▒▒█  ▒▓█           ▒▒▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒  █▒▓  
\t\t\t\t\t ▒▒▒▒▒▒  █▒█  █▓█            ▒▒▒▒▒▒▒▒▒▒▒▒       █▒▒█  ▓█ 
\t\t\t\t\t ▒▒▒▒▒    █▒  ▓▒             ▒▒▒▒▒▒▒▒▒▒▒        █▒▒   ▓▓ 
\t\t\t\t\t ▒▒▒▒▓          ▒            ▒▒▒▒▒▒▒▒▒▒        █▒▒    █▓ 
\t\t\t\t\t  ▒▒▒                        ▒▒▒▒▒▒▒▒          ▒▒        
\t\t\t\t\t   ▒▒                         ▒▒▒▒▒█        █▒█          
\t\t\t\t\t                              ▒▒▒                        
\t\t\t\t\t                             ██                          """+Fore.RESET,"Parasect", "Bicho", "Champiñón", "Primera", "Zona 1", "Bosque", "Hojas", "Absorber"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t                   ░░░░                                  
\t\t\t\t\t                    █░░░░                                
\t\t\t\t\t                          ░                              
\t\t\t\t\t                            ░                            
\t\t\t\t\t                       ▒█    █▒                          
\t\t\t\t\t     ▓░░░░█             ▒▒▒    ░                         
\t\t\t\t\t   █░░░░░░▒    ██▒░░█    ▓▒▒▒   █                        
\t\t\t\t\t            ██▓▒▓▓▓███ █░██▒▒▒▓█▒█▒▓                     
\t\t\t\t\t              ██▒▒▒▒▒▒▒▒▒▒▒█▓▒▒▓▒▓░▓ ▓█                  
\t\t\t\t\t                    █▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒█▒▒█                 
\t\t\t\t\t              █▓▒▒▒▒▒▒▒▒▓▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▓              
\t\t\t\t\t                ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▓▒▒▒▒▒▒             
\t\t\t\t\t                ▓▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▓▒▓▓▓▓▓▒▒▒▒▒            
\t\t\t\t\t              ▓▓▓▓▓▓▒▓▒▓▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒█▒▒            
\t\t\t\t\t              ▓▓▓▓▓▒▓▓█▒▒▒▒▒▓▒▒▒█▓▓▓░░▒▒▒█░░█▓           
\t\t\t\t\t            █▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓▓█          
\t\t\t\t\t           █▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓           
\t\t\t\t\t               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓██         
\t\t\t\t\t              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓░▒▒▒          
\t\t\t\t\t              █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒█▓▓▓▓▓▓▓▓▓▓▓▒▒█          
\t\t\t\t\t              █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓           
\t\t\t\t\t                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█             
\t\t\t\t\t                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓█             
\t\t\t\t\t                    ▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ██              
\t\t\t\t\t                    ▒▒▒▒▒█▓▓▓▓▓▓██▓▒▓▓█▒▒▒▒▒█            
\t\t\t\t\t                 ▒░░░░▒▒▒▒     █   █▒▒▒▒░░░░▒█           
\t\t\t\t\t                ░░█░░░░░█              █▒▒▒█             
\t\t\t\t\t                █▒▒▒▒▒                                   """+Fore.RESET,"Venonat", "Bicho", "Polilla", "Primera", "Zona 1", "Bosque", "Hierbas", "Ojo compuesto"),
            Pokemon(Fore.LIGHTMAGENTA_EX+"""\t\t\t\t\t                                                 █░░▒▓░█ 
\t\t\t\t\t                                             ░░░░░░░░░░░░
\t\t\t\t\t                                         █░█░░░░░░░░█░░░░
\t\t\t\t\t░░░█░█                                 ░░░░░░░░░░░░░░░░░ 
\t\t\t\t\t░░░░░░▒░              ░             ░░░░░░░░░█▒░░░░░█░░  
\t\t\t\t\t ░░░░░░░░░█          ░▒           ░░░░░░░░░░░░░░░░░░░█   
\t\t\t\t\t  ░░░░░█░░░░█       █▒█         ░░░░░░░░░░░░░░░░░░░░     
\t\t\t\t\t   ░░░░░░░░░░░      ▒▒   ░    ░░░░░░░░░░░░░░░█░░░░█      
\t\t\t\t\t     ░░░░░░░░░░▒    ▒▒  ░█  ░░░░░█░░░░░░█░░░░░░░█░       
\t\t\t\t\t      ░░░░░░░░░░▒▒ ▒▒▒█▒▒  ░░░░█░░░░░░░░░█░░░░░░░█       
\t\t\t\t\t       ░█░░░░░░░█▒▒░▒▒▒▒  ░░░░░░░█░░░█░░░░░░░░░░░        
\t\t\t\t\t        ░░░░░░░░█░▒▒▒▒░░█░▓░░░█░░█░░░░░░░░░░░░░░         
\t\t\t\t\t         ░░░░░░░░░█▒▒▒░██░▓▒░░░░░░░░░░░░░░░░░░█          
\t\t\t\t\t            ░░░░░░░▓▒▒▒▓▓▓█▓▒█▒▒▒▒▒▒▒▒▒▒▒░░              
\t\t\t\t\t                ░░░▒▒█░▓▓░░█▒▒█▓░░░░░░█░░░░░             
\t\t\t\t\t             ░░░░░░▒░░░▒▒▒▒▒▒▒▒▒░░░░░▓░░░░▓              
\t\t\t\t\t              ░░░░░░░░ ░▒▒▒▒▒▒▒▒█░░░░░░░░░               
\t\t\t\t\t              █░░░░░█  █░░░░▒▒█▒▒  ░░░░█░░░░             
\t\t\t\t\t                         ░░░░░▒▒█        ██              
\t\t\t\t\t                           ▒▒▒                          """+Fore.RESET,"Venomoth", "Bicho", "Polilla", "Primera", "Zona 1", "Bosque", "Hierbas", "Polvo venenoso"),
            Pokemon(Fore.LIGHTBLACK_EX+"""\t\t\t\t\t                          ████                           
\t\t\t\t\t                    █░▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                    
\t\t\t\t\t                  ▒▒▒░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                 
\t\t\t\t\t                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█               
\t\t\t\t\t               ▒▒▒▒▒▓░░░░▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒█              
\t\t\t\t\t              ▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒█             
\t\t\t\t\t             ▓▒▒▒▒▒█▓▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒             
\t\t\t\t\t             ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█            
\t\t\t\t\t            █▒▒▒▒▒▒▒░░░░░░░▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t            █▒▒▒▒▓▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t            █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t            █▒▒▒▒▒▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t            █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t            █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t            █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t            █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t            █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t        ▒▒█ █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█           
\t\t\t\t\t      ░░▓▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒█       
\t\t\t\t\t     ▒▒▒▒▒▒▒██▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     
\t\t\t\t\t    █▒▒▒▒▒▒░░▒▒▒▓▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒░░░▒▒▒▒     
\t\t\t\t\t   █▒▒▒▒▒▒░░░░█▒▒▓█░░▒░░░░░░▒▒█▒░░░░░░░░▒▒▒▒▓░▓▒▒▒▒▒▒█   
\t\t\t\t\t   ▒▒▒▒▓▒▒██▒▒▒▒▒▒▓█▒▒▒▒░▒▒▒█▒▒▒▒▒█▒░█▒██▒▒▒▒▒▒░▓▒▒▒▒█   
\t\t\t\t\t        █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓░░█     
\t\t\t\t\t           ▓▒█     █▒▒▒▒▒▒▒▒▒▒█░░▒▒▒▒▒▒▒▒█▒▒▒▓           
\t\t\t\t\t                        █         █        █             """+Fore.RESET,"Diglett", "Tierra", "Topo", "Primera", "Zona 1", "Cueva", "Raíces", "Taladrar"),
            Pokemon(Fore.LIGHTBLACK_EX+"""\t\t\t\t\t                             ▒▒▒▒▒▒▒▒▒▒█                 
\t\t\t\t\t                           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓               
\t\t\t\t\t                         █▒▒▒▒█▓▒▒▒▒█▓▒▒▒▒▒              
\t\t\t\t\t                         ▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▓             
\t\t\t\t\t                        ▓▒▒▒▒▒█░░░░░▒█▒▒▒▒▒▒             
\t\t\t\t\t                        ▒▒▒▒▒▒▒█▒▒▒▒▒▓▒▒▒▒▒▒             
\t\t\t\t\t               █▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒             
\t\t\t\t\t            █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓             
\t\t\t\t\t           ▒▒▒▒▒▒▒░▒▒▒▒▓█▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓             
\t\t\t\t\t          ▒▒▒▒▒▒▒▒██▒▒▒▒█▒▒▒▒▓▓▓▓▓▓▓▓▓▓███▓█             
\t\t\t\t\t          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓█▒▒▒▒▒▒▒▒▒▒▒           
\t\t\t\t\t         █▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒▒█▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t         █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▓▓▒▒▒▒▒█▒▒▒▒▒█▒▒▒▒▒        
\t\t\t\t\t         █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒█       
\t\t\t\t\t         █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒█       
\t\t\t\t\t          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█       
\t\t\t\t\t          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒        
\t\t\t\t\t          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█        
\t\t\t\t\t          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t          ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█         
\t\t\t\t\t        ▒▒█▒▒▒▒█▒▒▒▒▒▒▒██▒▒▒▒▒▓▓▓▓█▓▓▓▒▓█▒▒▒█▓▒▒▒▓       
\t\t\t\t\t     ▒█▒▒█░░▒▒▒▒▓▓▓▒▒█▒▒▒▒▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒       
\t\t\t\t\t   █▒▒▒▒▒█░░▒▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▓      
\t\t\t\t\t   ▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓█   
\t\t\t\t\t       █▒▒▒▒▒▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▓▒▒▒▒▒▒▒█▒▒▒▓▓▓▓█▒▒▒░▒▓   
\t\t\t\t\t                           █▒░░▓▓▓██  ▒▒▒▒▒█             """+Fore.RESET,"Dugtrio", "Tierra", "Topo", "Primera", "Zona 1", "Cueva", "Raíces", "Taladrar"),
            Pokemon(Fore.WHITE+"""\t\t\t\t\t                       ░        ░                        
\t\t\t\t\t                       ░        █                        
\t\t\t\t\t                   ▓▓█ ▒█      ░                         
\t\t\t\t\t                  █▓▓███░░░░░█ ░  █▓▓▓▓                  
\t\t\t\t\t                  ██▓▓▒█░░░░░█░███▓█▓▓█                  
\t\t\t\t\t             ██    █▓░░░░░░▓░░░██▓▓▓▓███░█░░             
\t\t\t\t\t               █░  █░░░░░░░░░░░░░░░░▒███░░░░░█           
\t\t\t\t\t                  ▓░░░░█░░░░░░░░█░░░██   █▒░░█           
\t\t\t\t\t             ░    █░░░▒░░░░░░░░░░░█░░░░░█░░░             
\t\t\t\t\t                  ▓░░░█░░░░░░░░░░░░░░░ █░░░              
\t\t\t\t\t                    ░░█░░░░░░░░░▓░░░░▓██░                
\t\t\t\t\t                      █░█▒▒▒▒▒▓░░░░█▒░░█                 
\t\t\t\t\t                      █░░█▒░░░░▒▒▒▒▒█                    
\t\t\t\t\t                 █░░░░  ░░▒▒▒▒▒▒                         
\t\t\t\t\t              ░░░░▓    ░░░░░░░░                          
\t\t\t\t\t           █░░░░      ░░░░░░░░░                          
\t\t\t\t\t          ░░░░░░      █░░░░░░░░                          
\t\t\t\t\t           ░░░░█     ░░ ░░░░░█          █▒▒▒▒▒           
\t\t\t\t\t                   ░░█     ░░▒▒         ▒▒▓▓▓▒▒          
\t\t\t\t\t                ▒▒▒░░      ░█ █▒▒▓      ▒▒▓▓▓▒▒          
\t\t\t\t\t             ▒█▒▒▒▒▒      ░░░     ▒▒░░░▒▒▒▒▒▒█           
\t\t\t\t\t            ▓▒▒▒▒▒       ░░░░                            
\t\t\t\t\t               ▓         ▒▒▒                             
\t\t\t\t\t                        ▒▒▒▒                             
\t\t\t\t\t                       ▒▒▒▒▒                             
\t\t\t\t\t                       █▓▒▒▒                             """+Fore.RESET,"Meowth", "Normal", "Gato", "Primera", "Zona 3", "Ciudad", "Pescado", "Recogida"),
            Pokemon(Fore.WHITE+"""\t\t\t\t\t                                █▒▒                      
\t\t\t\t\t                                ▓▒▒▒█       █▓█▓▓▓       
\t\t\t\t\t                                █▒▒▒▓▓░░░░██▒▒▒▒▒██      
\t\t\t\t\t                                 █░░░░░░░░░░░▒▒▒▒█       
\t\t\t\t\t                                  ▓░░▒▒░░░░░▒░██         
\t\t\t\t\t                                 █░░█░░░░▓ ░▒▒▒█         
\t\t\t\t\t                              ▒░░░░░░░░░░▒░▒░▒▒█         
\t\t\t\t\t                               ▒█  █░█░░░░▒▒█▓▒█         
\t\t\t\t\t                                 ░  ▒░░░░▒▒▒▒▒▒  █       
\t\t\t\t\t                                  ░░░▒▒▒▒▒▒▒▒▒           
\t\t\t\t\t                               █░░░░░▒░▒▒▒▒▒▒█           
\t\t\t\t\t     ▒░█                    ▒░░░░░░░░▒░░░▒▒▒░            
\t\t\t\t\t  ░░░░░░░░        ░░░░░░░░░░░░░░░░░░░░░░░░░░             
\t\t\t\t\t ░░░░░░░░▒      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░             
\t\t\t\t\t█░░░░░░░▒█    █░░░░░░░░░░░░░░░░░░░░░░░░░░▓▒▒█            
\t\t\t\t\t▒░░▓  █       ░░░░░░░░░░░░░░░▓░░░░░░█░░░░░░▒░            
\t\t\t\t\t█░░▓          ░░░░░░░░░░░░░▒▒░░░░░░░▒▒░▒▒▒░▒▒            
\t\t\t\t\t ▒░░█        ░░░░░░░░░▒▒██▓▒▒░░░░░░    █░▒▒▒░▒           
\t\t\t\t\t  █░░░░██▓▒░░▓░░░░▒▒█▒▒▒▒▒  █░░░░▒       ░░░▒▒▒          
\t\t\t\t\t     ▒░░░░░█▒░▒▒▒░   ▒▒▒▒█  ░░░░█          ░░▒░░░░░█     
\t\t\t\t\t           ░░░░▓      ▒▒▒▒ ░░░░█               █▒▒░░░░   
\t\t\t\t\t           ░░░░        ▒▒▒▓ ░░░░                   ▒░░▒█ 
\t\t\t\t\t           ▓░░░█        ░▒▒▒█░░░                    █▒░▓ 
\t\t\t\t\t            ░░░▒          ▒▒▒░░░░                        
\t\t\t\t\t            █▒▒▒░▓░█       ██▒░░░░░█                     
\t\t\t\t\t             █░░▒░░░         █░░░░░▒▓                    
\t\t\t\t\t                               █  █                      """+Fore.RESET,"Persian", "Normal", "Gato", "Primera", "Zona 3", "Ciudad", "Pescado", "Fuga"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                                ▓█                       
\t\t\t\t\t                           ▓█  ▓█                        
\t\t\t\t\t                           ██ ██  █▓▓                    
\t\t\t\t\t                            ███████                      
\t\t\t\t\t                     █░░░░░░░░░░░█                       
\t\t\t\t\t                ▒░█░░░░░░░░░░░░░░░░░█                    
\t\t\t\t\t              ▒▒▒░░░░░░░░░░░░░░░░░░░░░██░                
\t\t\t\t\t            █▒▒▓▓░░░ ░░░░░░░█░░░░▒░░░░░░░                
\t\t\t\t\t            ▒▒▒░░░░░░▓░░░░░█░░░░░░▓░█░░░░░█              
\t\t\t\t\t           ▒▒▒▒▒░░░░█░░░░░░░░█░░█░░▒▒░░░░░░░             
\t\t\t\t\t           ▒▒▒▒▒█░░░░░░▓░░░░░░░░▒▒▒▒▒░░░░░░░░            
\t\t\t\t\t           █▒▓░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░░░░░░░░░           
\t\t\t\t\t           ░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░█          
\t\t\t\t\t          ░░░░░░░░░░░░░░░░░░░█▒▒▒▒▒▒▒▒░░░░░░░░▒          
\t\t\t\t\t          ░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒█▒▒▒▒▒░░░░█          
\t\t\t\t\t           █░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒           
\t\t\t\t\t               ░░░░░░░░░▒░░░░░░▒▒▒▒▒▒▒█▒▒▒▒▒█            
\t\t\t\t\t               ░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t              █░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒█           
\t\t\t\t\t              ░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓           
\t\t\t\t\t        ▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒█           
\t\t\t\t\t         █▒▒▒▒█▒▒░░░░░░░░░░░░░░░▒▒▒▒▒▒▓░▒▒░░▒            
\t\t\t\t\t           █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░▒░▒▒▒░░          
\t\t\t\t\t             █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░▒▒▒▒▒▒▒           
\t\t\t\t\t                █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒█            
\t\t\t\t\t                    ▒▓▒▒▒▒▒▒▒▒▒█    █░▒▒▒▒█              
\t\t\t\t\t                 █░░░░░░░▒▒▒█                            
\t\t\t\t\t                      ░░███▒░                            """+Fore.RESET,"Psyduck", "Agua", "Pato", "Primera", "Zona 2", "Río", "Peces y algas", "Confusión"),
            Pokemon(Fore.BLUE+"""\t\t\t\t\t                       █      ██                         
\t\t\t\t\t                      ▒▒    █▒▒                          
\t\t\t\t\t                  ▒  ▒▒▒  █▒▒▒▒                          
\t\t\t\t\t                  ▒▒█▒▒▓▒▒▒▒▒▒     █                     
\t\t\t\t\t                  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                      
\t\t\t\t\t                  ▒░▒▒▒▒▒▒▒▒▒▒▒▒▒                        
\t\t\t\t\t                 ▒▒▒█▒▒▒▓▒▒▒▒▒▒                          
\t\t\t\t\t                  █░░░▒▒▒▒▒▒▒▒                           
\t\t\t\t\t           ▒▒▒▓▓▓░░░░░░░░░▒▒█▓▓                       ▒  
\t\t\t\t\t        █▓▓▓▓▓▓░░░░░░▒▒▒▒▓▓▓▓▓▒▒▒▒███▒▒▒▒▒           ▒▒  
\t\t\t\t\t    █▒▒▒▓▓▓   ░░░   █▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒█        ▒▒▒   
\t\t\t\t\t   ▒▒░░▒▒▓          █▒▒▒░▓▓▒▒▒▒▒▒▓▓█▒▒▒▒▒▒        ▒▒▒█   
\t\t\t\t\t  ███░░▒█            █░▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒█       ▓▒▒▓▓    
\t\t\t\t\t    █ ░                ▒▒▒▒▒▒▒▒▒█░▒▒▒▒▒▒█    ▓▓▓▓▓▓█     
\t\t\t\t\t                      █▒▒▒▒▒█░▒░░░▒▒█░░░▒▒▓▓▓▓▓▓▓▓       
\t\t\t\t\t                      █▒▒▒▒▒▒▒▒▒▒▓▒░█▓▓██░▓▓▓▓▓▓▓        
\t\t\t\t\t                     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▓▓▓▓▓▓▓▓          
\t\t\t\t\t                   ▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓█           
\t\t\t\t\t                 █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓              
\t\t\t\t\t                 ▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒               
\t\t\t\t\t                 █▓▓▓▓▒▓▓██        █▒▒▒▓▓▒▒              
\t\t\t\t\t                 █▒▒▓▓▓▓▓█           ▓▓▓▓▓▒█             
\t\t\t\t\t             █▒▒█▒▒▒▓▓▓▓            █▓▓▓▓▓▓▓▓            
\t\t\t\t\t            ░▒▒█░░▒▒▒▓              ▓▒▓▓▓▓▓▒▒            
\t\t\t\t\t            █    ▒                  ▒▒░░▒▒░░▒▒█          
\t\t\t\t\t                                   ▒▒█░░▒▒░░░▒▓█         
\t\t\t\t\t                                   ░░   ▒ ▒   ░█         
\t\t\t\t\t                                         ░               """+Fore.RESET,"Golduck", "Agua", "Pato", "Primera", "Zona 2", "Río", "Peces y algas", "Confusión"),
            Pokemon(Fore.WHITE+"""\t\t\t\t\t    █                                                    
\t\t\t\t\t  █▒▒▒▒                                                  
\t\t\t\t\t█▒▒▓▒▒▒█      █░       ███░░░                            
\t\t\t\t\t █▓▒▒▓▓▒      █░░░▓░░░░░░░░░░█ █░█░          ▒▒▒▒        
\t\t\t\t\t      ▒▒█     ░▒▒░░░░░░░░░░░░░░░░▓▓         ▒▒▒▒▒▒       
\t\t\t\t\t      ░░░      █▒░░░░░░░░░░░░░█▒▒▒         ▒▒▒▒▒▒▒▒      
\t\t\t\t\t      █░░░░░█ ░░░░░░░░░░░░░░░░░░▒▓░       ▒▒▒█▓▒▒█       
\t\t\t\t\t       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     ░░░█         █  
\t\t\t\t\t           ░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░      ▓▓▓▒▒▒█
\t\t\t\t\t            █░░░░░▓░░░░░░░░░░░░░░░░░░░░░░░░░    ▓▓▓   ▒▒ 
\t\t\t\t\t             ░░░░░▓░▒░▒░░█░░░░░░░░░░█           ▒█  █▒▒█ 
\t\t\t\t\t             ▒░░░░░░░░░▒░░░░░░░░░░▒               ▓▓▓▓   
\t\t\t\t\t            █░█░░░░░▒▒▒▒▒▒░░░░░░▒▒             ▒▒▒▒█     
\t\t\t\t\t          ░░░░░░░▒▓░░░░░░░▒▒▒░░░░░░█  ██▒▒▒▒▒▒▒▒         
\t\t\t\t\t           ░░▒▒ █▒   █ ░ ░░  ░░░░░░░▒▒▒▒█                
\t\t\t\t\t             ▓▓▓▓              ░░░░░░                    
\t\t\t\t\t        ▒▒▒▒▒▒▓▓                 ▒▒▒█                    
\t\t\t\t\t       █▒  ▒▒█                    █▓▓                    
\t\t\t\t\t            ▒                    ▓▓▓▓▓                   
\t\t\t\t\t                                 ▒▒▓▓▒▒▒█                
\t\t\t\t\t                                ▒▒█    ▒▒                
\t\t\t\t\t                                 ██                      """+Fore.RESET,"Mankey", "Lucha", "Mono", "Primera", "Zona 1", "Pradera", "Frutas", "Fuga"),
            Pokemon(Fore.WHITE+"""\t\t\t\t\t                        █▒▒▒█▓▓█                         
\t\t\t\t\t                  ▒▒▒▒▒▒▒▒▒▒▓▓▓███                       
\t\t\t\t\t                 ▒▒▒▒▒▒▒▒▒▓▓▓▓█████                      
\t\t\t\t\t                █▒▒▒▒▒▒▒▓▓████████▓▓█                    
\t\t\t\t\t                █▒▒▒▒▒▒▓▓███████▒▒▒▓▓▓▓                  
\t\t\t\t\t                    ██  ░░░▒     ▒▒▒▒▒▓▓█                
\t\t\t\t\t            █          ░░▒█░░▒     ▓▒▒▓▓                 
\t\t\t\t\t       ▒▒▒▒▒▒▒▒      █░░█▓▒▒░░▒▒▒ █▒▓▓▓▓                 
\t\t\t\t\t      ▒▒▒▒▒▒▒▒▒    ░ ░░░████░░░░▒▒▒▒▒▓▓                  
\t\t\t\t\t     ▒▒▓▓▓▓█▓█     ░█░░░░░░░░░░░░█▒▓▓▓▓░  ░              
\t\t\t\t\t     ▓▓▓▓▓█ █▒░░░▒▒░░░░░░░░░░░░░█▓▓▓▓▓▒▒▒░               
\t\t\t\t\t    ▓░▓██▓    ░▒░░░░░░░██░▓░░░░░░▓▓▓▓▓▒▒▒▒               
\t\t\t\t\t    ▓░▓██▓     ░▒░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒              
\t\t\t\t\t     █▒▓▓       ░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒              
\t\t\t\t\t      ▒▒▒       ░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▓           
\t\t\t\t\t      ▒▒▒▒█▒▒▓ ░░░░░░░░▒░░░░░░░░░▒▒▒▒▒█▓█▒▒▒▓▓           
\t\t\t\t\t       ▒▒▒▓▓▓▓█▓░░░░░█░▒▒░░░░░░░▒▒▒▒█▒▓▓▒▒▒▓▓▓█▒▒        
\t\t\t\t\t         █▓▓▓▓▓▓░░░░░▒▒▒░░░░░░░▒▒▒▒▒▓▓▓▓▓░▓██▒▒▓▒▒▒      
\t\t\t\t\t                 ░░░░░░░░░░░░▒▒▒▒▒▒▒▓▓▓▓▓▓█▒▒▓▓▓▓▓▒▒     
\t\t\t\t\t                  █░░▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▓▓▓▓▓▓▓▓▒▒█   
\t\t\t\t\t                    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▓▓▓▓▓▓▓▓▓▓▓▒   
\t\t\t\t\t               █▓▓▓▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  █▓▓▓▓▓▓▓▓█  █    
\t\t\t\t\t             ▒▒▒▒▒▓▓▒██▓▓▓▓█▒█▒▒▒▒▒     █▓▓▓▓▓▓          
\t\t\t\t\t             █▒▒▒▒██▒▒▒▓▓▓▓      ░░         █            
\t\t\t\t\t                █▒▒▓▓▓▓▓▓▓▓                              
\t\t\t\t\t                 ▒▓▓▓▓▓▓▓                                
\t\t\t\t\t                  ▒▒▓▓▓                                  
\t\t\t\t\t                   █▒▒                                   """+Fore.RESET,"Primeape", "Lucha", "Mono", "Primera", "Zona 1", "Pradera", "Frutas", "Fuga"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t                              ░░░░░█                     
\t\t\t\t\t                            ░░░░░░░░░░░░█                
\t\t\t\t\t                          ░░░░░░░░░░░░█                  
\t\t\t\t\t                         ░░░░░░░░░░░▒░░░█                
\t\t\t\t\t                          ░█▒▒▒▒█░░░▓▒                   
\t\t\t\t\t                      █▒░░░░░▒▒▒▒▒▒▒▒▒▒▒█                
\t\t\t\t\t                     ██░░▒▒▒▒█░░▒▒▒▒▒▒▒▒▒▒               
\t\t\t\t\t                    █▒▒▓▒▒▒▒█▓ ░▒▒▒▒▒▒▒▒▒▒▒              
\t\t\t\t\t                    █░░░░░░░░░░░░░█▒▒▒█▓▒█               
\t\t\t\t\t                    █░░░░░░░░░░░░░░░▒▒▒█                 
\t\t\t\t\t                      ░░░░░█▒█░░░░░░▒▒▒▒                 
\t\t\t\t\t                       █░░░░░░░░░░█░░░▒░                 
\t\t\t\t\t               █░░▒█    ░░░░░░░░░░░░░░░░░░░              
\t\t\t\t\t          █▒░░░░░░░░░░░ ░░░░░░░░░░░░░░░█▒                
\t\t\t\t\t         ░▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█               
\t\t\t\t\t         ░░░▒░░░░░░░░░▓▓█░░░░░░░░░░░░░▒▒▒▒               
\t\t\t\t\t           ██░▒▒▒▒▒▒▓█▓▓██░░░░░░░░░░░░▒▒▒▓               
\t\t\t\t\t          ▒▒█▒▒▒▒▒▒░████▒▒▒▒░░░░░░░░▒▒▒▒▒▒█              
\t\t\t\t\t         ▒█▒▓▒▒▒▒░░░░▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒█▒▒              
\t\t\t\t\t             █▒█▓▓░░░░▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒█▒               
\t\t\t\t\t               ░░▓▓░░▒▒▒▒░░░░▒▒▒▓▒▒▒▒▒▒▒▒▒               
\t\t\t\t\t               ▓▓▓░░▒▒▒▒▒▓▓▓▓░▒▒█▒▒▒▒██▒██               
\t\t\t\t\t               ▓▒▒▒▒▒▒▒▒▒░░░▓▓███░█▒█▒███                
\t\t\t\t\t               ▒▒▒▒▒▒▒▒▒▒█▒░░▒██▒▒▒▒▒▒▒█▒                
\t\t\t\t\t                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                
\t\t\t\t\t                ▒▒▒▒▒▓█   ▒▒▒▓▒▒▒▒█▒░▓▒▒▓░               
\t\t\t\t\t                            █░█   █░                     """+Fore.RESET,"Growlithe", "Fuego", "Perro", "Primera", "Zona 3", "Ciudad", "Bayas", "Fuga"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t                 ░█░                                     
\t\t\t\t\t            █░ █░░░░                                     
\t\t\t\t\t          █░░░░░░░░▒ █ ██               █                
\t\t\t\t\t        ░█░░░░░░░░░░░░░░░          ░░░░█                 
\t\t\t\t\t  █▒▒▒██░░░░░░░░░░░░░▒█▒▓▒█     ░░░░░░░░▓                
\t\t\t\t\t   ██░▒▒█░░░░░░░░░▒▓▒▒▒░▒     ░░░░░░░░░░░█               
\t\t\t\t\t     ▒▒▒▒█▒█░░░░░░▒█░▓█▒▒▒   ░░░░░░░░░░░░░░░             
\t\t\t\t\t      ░░░░░▒▒░░█▒▓░░░░░░░░  ░░░░░░░░░░░░░░░░░█           
\t\t\t\t\t     ░░░░░░░░░░░░░░░░░░▒░░██▒░░░░░░░░░░▒▒▒▒▒▒▒▒          
\t\t\t\t\t       █░░░░░░░░░░░░░░░▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t         █░░░▒▒░░░░░▓▓█▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t         ▒░░█░░░░░░░██▓█▓█    ▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█     
\t\t\t\t\t       ░░░░░░░░░░░░░░░░░▓▓▒██▓▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒█      
\t\t\t\t\t       ░░░░░░░░░░░░░░▒▒████▒▒▒▒▒▒▒██▒▓▒▒▒ █▒▒▒▒▒▒░█      
\t\t\t\t\t         ▒█░░░░░░░░░░░▒▒▒▒████▒▒▒▒▒▒█▓█▒                 
\t\t\t\t\t        ██░░░░░░░░▒▒▒██▒████▒▒▒▒▒▒▒███▒      ░ ░░░       
\t\t\t\t\t         ▓▒░░░▒░▒▒█▒▒▒████▒▒██▒▒▒████▒█ █░ ░░░░░░░       
\t\t\t\t\t         █▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒█░░▒▒█▒▒▒▒█▓█░░░░░░░░         
\t\t\t\t\t          ▒▒▒██▒▒▒▒▒▒▒▒▒█░░░░▓▓▒▒▒▓███▒▒█░░░░░░          
\t\t\t\t\t          ▓▒▓██▒▒▒▒▒▒▒███░░░░▓▓▒▓█▒▒▒▒▒░░░▒▒▒▒█▒         
\t\t\t\t\t          █▓▓▓█▒▒▒ █▓▓██▒░░░░▒▓▓▓█▒▒▒▒▒▒▒▒▒▒▒▒█          
\t\t\t\t\t          ▒▓▒▒██   █▓▓█▒▒▒▒▒▒▓▓▓█ ▒▒▒▒▒▒▒▒▒▒             
\t\t\t\t\t          ▒▒▒▒▒▒   █▒█▒▒█▒▓▓▓▓▓▓   ▒▒▒▒▒▒▒▒██            
\t\t\t\t\t         ▒▒▒▒▒▒▒   ▒▒▒▒▒▒ ███    ▒▒▒▒▒▒▓                 
\t\t\t\t\t        ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒        ▒▒▒▒▒█                  
\t\t\t\t\t                  ▒▒▒▒▒▒█                                """+Fore.RESET,"Arcanine", "Fuego", "Perro", "Primera", "Zona 3", "Ciudad", "Bayas", "Intimidación"),
            Pokemon(Fore.BLUE+"""\t\t\t\t\t          ▒▒▒▒▒▒▒▒█░██                                   
\t\t\t\t\t       ▒▒█▒▒▒▒▒▒▒█ ░██  ▓                                
\t\t\t\t\t     ▒ ██  █▒▒▒▒▒▒▒▓▓▓█ ░▓▓                              
\t\t\t\t\t    ▒ ██████▒▒▒█░░▒▒▒▓██▓▓▓▓█                            
\t\t\t\t\t   ▒▒  █▓▓▓▒▒▒░░░░▒▒▓▓▓▓▒▓▓▓▓▓                           
\t\t\t\t\t  ▒▒▒░░░░░▒▒▒█▒▒▒▒█░░░░░░▓▒▒▒▒▓                          
\t\t\t\t\t █▒▒▒▒▒▒▒▒▒░░░░░▓█████▓░░░░▓▓▓▓▓                         
\t\t\t\t\t ▒▒▒▒▒▒▒▒▒░░░▒▒░░░░░░░░░█░░░█▓▓▓                         
\t\t\t\t\t ▒▒▒▒▒▒▒█░░░▒░░░██░░░██░░█▓░░▓▓▓█                        
\t\t\t\t\t ▓▒▒▒▒▒▓░░░█░░██░████▓░█░░█░░█▓▓█                        
\t\t\t\t\t ▓▓▓▓▓▓▓░░░█░░█░█░░░░█░█░░█░░█▓▓                         
\t\t\t\t\t ▓▓▓▓▓▓▓░░░█░░█░░█░▒█░▒█░▒█░░▓▓█                         
\t\t\t\t\t  ▓▓▓▓▓▓▓░░░█░░█░░░██░░░██▒▒▓▓█                          
\t\t\t\t\t   ▓▓▓▓▓▓▓░░░██░░██████▒▒▒█▓▓▓▓▓▓                        
\t\t\t\t\t    █▓▓▓▓▓▓▓░░▒▒█▒░░░░░░▓▓▓ ▓▓▓▓▓▓▓█                     
\t\t\t\t\t      █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█    ▓▓▓▓▒▒▒███▒▒▒▒▒▒▒▒█         
\t\t\t\t\t         ██▓▓▓▓▓▓▓▓█▓▓▓▓▓▓██▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    
\t\t\t\t\t            ▓▓▓▓▓        █▓▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░  
\t\t\t\t\t            ▓▓▓▓▓▓        █▒▒▒▓▓▓▓█▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░ 
\t\t\t\t\t             ▓▒▒▒▒▒▒        █▒▒▒▒▒▒▒▒█▓▓▓▓██░░░░░▒█░░░░░ 
\t\t\t\t\t             █▒▒▒▒▒▒█          ▓▒▒▒▒▒░░░░░░░░░░░░░░░░░░█ 
\t\t\t\t\t               ▒▒▒▒▒              █░░░░░░░░░░░░░░░░░░░   
\t\t\t\t\t                                        █░░░░░░░░░█      """+Fore.RESET,"Poliwag", "Agua", "Renacuajo", "Primera", "Zona 2", "Río", "Algas", "Absorber"),
            Pokemon(Fore.BLUE+"""\t\t\t\t\t     █░░░░░█                                             
\t\t\t\t\t  ░░░░░░░░░░░░                                           
\t\t\t\t\t█░░░░░░░░░▒░▒░░   ▒▓▒▒▒▒▓                                
\t\t\t\t\t█░░░░░░░░░░░░░░ ▓░█░░▓▓▓▓████  ▓▒░░█░▒█                  
\t\t\t\t\t █░░░░▒░░░░░░░███░▓▒░░▒▒▒▒▒▒▒▓▒░█░ ▒█▒▒▒                 
\t\t\t\t\t   █░░░░░░░░░█  ▓▒▒▒▒▒▓▓▓▒▒▒▒▓█░█████▓▒▓█                
\t\t\t\t\t       ▒░░░░░█▒▒▒█▒▓▓█▒▒▒▒▒▒▒▓▓███▓▓█▓▓▓█                
\t\t\t\t\t         █▓▓██░░▒▒███▓░░░░▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓█               
\t\t\t\t\t           █░▒▒░░░░░░░░██░░░▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓              
\t\t\t\t\t           ░▒░░▒██████░░░░█░░░▓▓▓▓▓▓▓▓▓▓▒█▓█             
\t\t\t\t\t          ░█░▓█░░█▓░░░░█░░░█░░░▓▒▒▒▒▒▒▓▓▒▒▒▒█░▓          
\t\t\t\t\t          ▒░█▒▒█░░░░▒█░░██░░█░░░▒▒▒▒▒▒▓▓▒▒▓░░░░▓░░░░░█   
\t\t\t\t\t          █░█░█░█▒▒█░░█░░█░░██░░█▒▒▒▒▒▓▓▓▓░░░░░░░░░░░░░▓ 
\t\t\t\t\t          █░█▒█░█░█░█░█░░█░░▒█░░░▓▓▓▒▒▓▓▓▓█░░░░░░░░░░░░░█
\t\t\t\t\t          █░█░█▒░░░█░░█░░█░░██░░░▒▒▒▒▓▓▓▓▓▓█░░░░░░░░░░░░█
\t\t\t\t\t           ▓░█░░░░░░░█░░░█░░██░░█▓▓▓▓▓▓▓▓▓██░░░░░░░░░░░░ 
\t\t\t\t\t            ▒░░█████░░░░█░░▓█░░░▓▓▓▓▓▓▓▓▓█  ░░░░░█░░░░░  
\t\t\t\t\t             ░██░░░░░▒█▓░░██░░░▓▓▓▓▓▓▓▓▓     █░░░░▒▓█    
\t\t\t\t\t               ░░░░░░░░░██░░░░▓▓▓▓▓▓▓▓█                  
\t\t\t\t\t                 █░░░░█░░░░░▓▓▓▓▓▓▓▓█                    
\t\t\t\t\t                    ▓█▓▓▓▓▓▓▓▓▓▓▓▓▓█                     
\t\t\t\t\t                    █▓▓▓        ▓▓▓▓                     
\t\t\t\t\t              █▒▒▒▒▒▓▓▓▓▓▓      ▓▓▓▓▓▓▓                  
\t\t\t\t\t             ▒▒▒▒▒▒▒▓▓▓▓▓     █▓▓▓▒▒▒▒▒▒▓                
\t\t\t\t\t             ▓▓▓▓▓▓▓██        █▓▓▒▒▒▒▒▒▒▒█               
\t\t\t\t\t                                █▓▓▓▓▒▒▒▒                """+Fore.RESET,"Poliwhirl", "Agua", "Renacuajo", "Primera", "Zona 2", "Río", "Algas", "Absorber"),
            Pokemon(Fore.BLUE+"""\t\t\t\t\t                      ██       █▒▒▒█▓                    
\t\t\t\t\t                    ▓▒▒▓▒▒░▒▒▒▒▒▒░ ░░▓                   
\t\t\t\t\t                   ▓  ▓░▒▒▒▒▒▒▒▒░░░░▓▓▓▓                 
\t\t\t\t\t                 █▓▒█░▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▓▓▓▒▒              
\t\t\t\t\t               █▓▓▓▓█░░░░░▒█████░░░░░█▓▓▓▓▓▒▒  █░░░░░░   
\t\t\t\t\t              ▒▒▓▒▒░░░▒▒░▓█░░██░░█▓░░░█▒▓▓▓▓▒▒█░░░░░░░░  
\t\t\t\t\t   █░░░░░░█  ▒▒▓▓▓░░░█░█░█▓░░░█░█░░█░░░▓▓▓▓▒█▒▓░░░░░░░░░ 
\t\t\t\t\t  ░░░░░░░░░█▒▒▓▒▓▓░░░█░█░█░█░█░█░█░█░░░▓▓▓▓▒▒▓█░░░░░░░░░█
\t\t\t\t\t █░░░░░░░░░█▒▓▓▓▓▓█░░█░█░██░█░░█░█░█░░█▓▓▓▓▓▓▓░▓░░░░░░░░█
\t\t\t\t\t ░░░░░░░██░░▓▓▓▓▓▓▓█░░█░▒█░░██░░█░█░░█▓▓▓▓  █▓░░▓░░░░░░░ 
\t\t\t\t\t ░░░░░░▒░░░▓▓▓█  ▓▓▓▓░░██░░░░▓█░░█░▓▓▓▓▓▓█     ███░░░█   
\t\t\t\t\t  ▒░░░░           █▓▓▓▓▓█░░░░░░░▓▓▓▓▓▓▓▓                 
\t\t\t\t\t                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                  
\t\t\t\t\t                    ▓▓▓▓▓▓  ██████▓▓▓▓▓                  
\t\t\t\t\t                   ▓▓▓▓█           ▓▓▓▓▓                 
\t\t\t\t\t                  ▒▓▓▓█             ▓▓▓▓▓                
\t\t\t\t\t             █▒▒▒▒▓▒▒▒█             █▓▓▓▓▓               
\t\t\t\t\t           ▒▒▒▒▒▒▒▓▓▓▓              ▓▓▓▓█▒▒▒▓            
\t\t\t\t\t            █▓▓▓▓▓█                  ▓▓▒▒▒▒▒▒▒▒█         
\t\t\t\t\t                                       █▓▓▓▓▓▓▓          """+Fore.RESET,"Poliwrath", "Agua", "Tritón", "Primera", "Zona 2", "Río", "Algas", "Absorber"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                                      ██                 
\t\t\t\t\t                   ▓░░▓    █░░░░░█░░░░░░                 
\t\t\t\t\t                   █░░░░░░░░░░░░░░░░░░░░                 
\t\t\t\t\t                    ░░░░░░░░░░░░░░░░░░░█                 
\t\t\t\t\t                    █░░░░░░░░░░░░░░░░░░             █▓   
\t\t\t\t\t                     ▒░░░░░░░░░░░░░░░░░▒            █░░  
\t\t\t\t\t                     ░░░░░░░░░░░░░░░░░░░            ░░░  
\t\t\t\t\t                     ░░░█░░░░░░░░░░░░░░             ░░░▓ 
\t\t\t\t\t                       ░░░░░░░░░░███▒▒▒▒           ░░░░░ 
\t\t\t\t\t                        ▒▓░░░░░███▒▒▒▒▒▒▒▒        ▒▒▒░░█ 
\t\t\t\t\t                      █▒▓▓▓█▒█████▒▒▒▒▒▓███      ░░░█▓▓  
\t\t\t\t\t                       ▓▓▓▓▓▒▒▒▒▓▓█▓▓▓▒███     █░░░░░░▓  
\t\t\t\t\t       ░░█               ▒▒█░░░░█▓▓▓░░        ░░░░░░░░   
\t\t\t\t\t        ░░▒█            ▓▒░░░░░░▒▒░░░░    █▒▒░░▒░░▒▒▒    
\t\t\t\t\t   ░░█   ▒▒░    ░░░    ▒▒░░░░░███░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒█     
\t\t\t\t\t ░░░▒▒▒▒░▒▒▒ █░░░░░░░░░░░░░░░█░░░░▒░░░░░░░░▒▒▒▒▒▒▒       
\t\t\t\t\t      █▒▒▒▒▒▒░░░░░░▓░░░░▒█░░░░░░░░░█░░▒░░░░█▒▒▒▒         
\t\t\t\t\t       █▒▒▒▒▒░░░░░░░▒▒▒█░▒░░░░░░▒▒▒▒▒▒▓█░░█▒▒            
\t\t\t\t\t        █▒▒▒▒░▓██░░      █▒░░░▒▒▒▒▒▒▒▒░░                 
\t\t\t\t\t         ▒▒▒█            █░░░░▒▒▒▒▒▒▒▒▒▒░░░              
\t\t\t\t\t       ░░▒▒               ░              ░░░             """+Fore.RESET,"Abra", "Psíquico", "Psi", "Primera", "Zona 1", "Bosque", "Frutas", "Sincronización"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                       █░                                
\t\t\t\t\t                  █░░░░█░░                               
\t\t\t\t\t                █░▒░░▒░░█▒▒░░░░░░░░█                     
\t\t\t\t\t                   ▒█▒▒▒▒▒▒▒█ ░░░░░░                     
\t\t\t\t\t                   █░▒░     █                            
\t\t\t\t\t                   █░░░░░                                
\t\t\t\t\t                    ░░ ▒▒█░░ █▒                          
\t\t\t\t\t                    ▒▓  ░▒▒█░░░░▓           ░░           
\t\t\t\t\t                     ░█  ▒▒░░░░░▒░█     █  ░▒█           
\t\t\t\t\t                    ▒▒▒▓▒▓░░░░░░░░▒░    ▓░█▒▒▒▒░░░       
\t\t\t\t\t                    ▒▒▒▓▓█▓█▒▒▒▒░░░░▓█    ▒▒▒▒▒░▒        
\t\t\t\t\t                   █▒▓▓▓▓▓▓▓█░░░▓▓▓█▒█     ▒▒▒▒█         
\t\t\t\t\t               █░░░█▓▓▓▓▓▓▓░░░▓▓▓████▒    ▒░▒            
\t\t\t\t\t            █░░░░░░░▓▓▓▓▓░░░▓▒▒▒▒▓▓██▒█▓▓▒░░             
\t\t\t\t\t           ░░░░░░░░░░▒▓█░░░▓▓▒▒▒▒▓▓▓█░█                  
\t\t\t\t\t          ░░░░░░░░░▒▒▓▓▒░░▓▒▒▓█▓▓▓▓▓ ▓                   
\t\t\t\t\t         ░░░░░░░░█▒▒█▒▒▒░█▓▓▓▓█▒▒▓█ █                    
\t\t\t\t\t         ░░░░▒▒░▓▒▒░░▒▒▒▒▒▒██▒░░░░                       
\t\t\t\t\t         ░░░░▒▒▒▓▒▒▒▒▒▒▒░░░░░▒░░░▒▒▒░                    
\t\t\t\t\t         █░░░▒▒▓▓▒▒▒▒▒▒░░▓▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒               
\t\t\t\t\t       ░  ░░▒▒▒▒▓▒▒▒░░░░░▒▓▒▒▒▒▓▒█   ▒▒▒▒                
\t\t\t\t\t       ▒▒▒█▒▒▒▒▒▒ ▒░▒▒▒▒█▒▓▓▓▓▓▓▓▓  ░▒▒▒█                
\t\t\t\t\t       █▒▒▒▒▒▒▒▒█  ░▒▒█▓▓▓▓▓▓▓▓▓      ▒▒▒                
\t\t\t\t\t          ▒▒▒▒█    ░▒▒█ ▓▓▓▓█       ░▒▒▒░░░▒▒░░          
\t\t\t\t\t                  ░░▒▒▒                     ▒░▒░▒░       
\t\t\t\t\t                ░█▒▒██▓░░                   █▒█          
\t\t\t\t\t               ▒░▒     █░                                
\t\t\t\t\t                █                                        """+Fore.RESET,"Kadabra", "Psíquico", "Psi", "Primera", "Zona 1", "Bosque", "Frutas", "Sincronización"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                     ░▒                                  
\t\t\t\t\t                     █░░█                  ░█            
\t\t\t\t\t                      ░░░░             ░░░░              
\t\t\t\t\t                       ░░░░░       ▓░░░░▒                
\t\t\t\t\t        ▒░░█           █░░░░░░░░░░░░░░▒█           █     
\t\t\t\t\t       ▓░░░░░░░         ░░░░░░░░░░░░▒▒          ▓░░░░░░  
\t\t\t\t\t     █░░░░░░░░░░░░▒▒▒█░░░░░░░░░░░▒░░▒       █░░░░░░░░    
\t\t\t\t\t    ██░░░░░░░░░░░░░█▓▓█░░▓░░░░░░▒▒▒▒▒█▒▒▒█░░░░░░░░░░     
\t\t\t\t\t                 ▓░░▒▒▓▓▓░▒░░▓░▓▒▒▒▒▒░▒▒░░░░░░░░░░░█     
\t\t\t\t\t    ███▒▒▒▒▒▒▒▒▒█▒▒▒░░▓▓▓▓░░░▒▒▒▓▓▓▓▓█░░░█▓▓▓            
\t\t\t\t\t   ░░▒▒░░░░░▒▒▒▓▓      ███▒░▒▒▓██▒░░░█▓▒▒▓▓▓█            
\t\t\t\t\t█░░░░▒▒▒▒░░░▒▒           ▓▓██▓▓▓▓▓▓▓█▒▒▒▒▒▒▒▓   ██       
\t\t\t\t\t   ░░▒ █░░░▒░░░░░░░░     █▓▓▓▓▓▓▓█   ██ ▓▓▒▒▒░░░░░░░░░   
\t\t\t\t\t    ▒█  █▒▒▒ ▒░░░░░░█   █▒▓▓▓▓▓▓▓  ░░░░░░░░▓▒░░░▒▒▒▒░░█ ▒
\t\t\t\t\t              █▒       ▓▒▒▒▒▒▒▒▒▒▒█░░░░░░░█▒▒░░░▒▒▒▒░░░░ 
\t\t\t\t\t              █▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓░▒▒██▒▒   █▒█   
\t\t\t\t\t             ▓▒▒▓▓▓▒▒    █▒▒▒▒▒█  ▓█░░▒█▒█               
\t\t\t\t\t             █▓▒▒▓▓▒       █▒█     ░░░█▒▒▒               
\t\t\t\t\t            ░░░░▒▒                 █░▒▓░░▒▒██░░█         
\t\t\t\t\t    █░░░░░░░█░░░▒█                  ░░▓░▒░░░▒▒░░█        
\t\t\t\t\t   ░░▒▒▒▒░░▓░░▒▒▒                   ░░▒▒▒▒▒▒▒▒▒          
\t\t\t\t\t        ▒▒░▒▒▒░▒▒                  █░░▒▒▒▒▒▒▒▓           
\t\t\t\t\t         █▒▒▒▒▒▒▒                   ░░░▒▒▒▒▒▒            
\t\t\t\t\t          ▒▒▒▒▒▒▒                    ░░▒▒▒▒▒             
\t\t\t\t\t            ▒▒▒▒                      ░▒▒▒               
\t\t\t\t\t             ░█                        ▓░█               """+Fore.RESET,"Alakazam", "Psíquico", "Psi", "Primera", "Zona 1", "Bosque", "Frutas", "Sincronización"),
            Pokemon(Fore.LIGHTCYAN_EX+"""\t\t\t\t\t                               █░░░░░░█                  
\t\t\t\t\t                              █░░░░░▓░▒▓░▒               
\t\t\t\t\t                              ▒░░░░░█▒▒█▒▒               
\t\t\t\t\t                            █░░░░░▒░░▒▒▒█▒█              
\t\t\t\t\t                   ██      █░░░░░░░░░▒▒▒▒█               
\t\t\t\t\t             █░░░░░░░░▒   ▒░░░░█▓█░░█▒▒▒▒█               
\t\t\t\t\t           ▒░░░░▒░░░░░▒█  ▒░░░▓█▓░░░░░▒░▒█               
\t\t\t\t\t         ▒░░░░░░░░░░░░▒▒█▒▒▒▓░▒▓▓░░░░░░░▓░               
\t\t\t\t\t        ░▒░░░░░░░░░░░░░▒▒▒▒▒▒▒░░▒▒░░░░░█▓▒▒█▒            
\t\t\t\t\t        ░░░░█░░░▓░░░░░▒▒▒░▒▒▒▒▒▒░░░░░░░▒▒▒▒▒▒▒█          
\t\t\t\t\t         ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒     █▒▒▒▒▒▒▒        
\t\t\t\t\t               ▓▓███▒▒▒▒▒░▒▒▒▒▓▒░▓▒        ▒▒▒▒▒▒        
\t\t\t\t\t                  ▒▒▒▒██░▓▒░▒▒▒▒▒▒▒        █▒▒▒▒▒        
\t\t\t\t\t                       ░░▒░░░░░░░░▒░                     
\t\t\t\t\t                      ░░░░░░░░░░░░▒░                     
\t\t\t\t\t                  █▒▒▒▒░░░░░░░░░░░░░█                    
\t\t\t\t\t                  ░▒▒▒▒▒░░░░░░░░░░░░▒                    
\t\t\t\t\t                 ░░░▒▒▒▒▒▒▒▒░░░░░▒▒▒▒                    
\t\t\t\t\t                ▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒                    
\t\t\t\t\t                █▒▒▒▓▒▒▒ ██  ▒▒░░░░▒                     
\t\t\t\t\t                █▒▒▒▒▒▒      ▒░░░░▒█                     
\t\t\t\t\t                   ▒▒█      ▒▒░░▒▒█                      
\t\t\t\t\t                           ▒▒▒▒▒▒                        
\t\t\t\t\t                         █▒▒▒▒▒▒                         
\t\t\t\t\t                         ▒▒░░░░░                         
\t\t\t\t\t                        █▒▒▒░▒▒▓▒                        """+Fore.RESET,"Machop", "Lucha", "Súperpoder", "Primera", "Zona 1", "Pradera", "Frutas", "Fuga"),
            Pokemon(Fore.LIGHTCYAN_EX+"""\t\t\t\t\t                         ▒▒▒▒▒▒                          
\t\t\t\t\t                      █▓▒░░▒▒▒▒▒                         
\t\t\t\t\t                   ░░▒▒▒▒▒▒█▒▒▒▒▒                        
\t\t\t\t\t                  █▒▒███▒▒▒▒▒▒▒▒▒                        
\t\t\t\t\t                    ▒▒▒▒▒▒▒▒▒▒▒▒▒█                       
\t\t\t\t\t                     █▒▒▒▒▒▒▒▒▒▒▒▒▒                      
\t\t\t\t\t                 ▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░░▒               
\t\t\t\t\t              █▒▒▒▒▒▒░░▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█             
\t\t\t\t\t           ▓▒▓▒▒▒▓▓░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒           
\t\t\t\t\t        ▒░▒▒▒▒▒▓▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒█░░░▓▒▒▒        
\t\t\t\t\t       █░▒▒█▒▒▒▒▒▒▒░░░▒▒▒▓▒▒▒▒▒▒▒▒▒▓▒▒▒▒░▓▒░░▓▒▒▒▒       
\t\t\t\t\t       ▒░▒░▒▒▒▒▒▒█  ▒▒▒▒███▒▒▒▒▒▒▒▒▒ ██░█░█▒░▒▒▓▒▒       
\t\t\t\t\t      █▒░▒▒▒░▒▒▒     █▒▒▒▒▓░▒▒▓██▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒        
\t\t\t\t\t       ▓▒▓▒▒▒▒▒▒     ▓░░█░░▓▓░██░▒▒▒▒▒▒▒▒▒▒▒▒▒▒          
\t\t\t\t\t       █▒▒▒▒▒▒▒▒▒▓  ▓▓▓█░░░░█▓▓▓░░░░▒▒▒▒▒█▓              
\t\t\t\t\t       ▓▓▒▒▒▒▒▒▒██▒▒█▓▓▓▓▓▓▓▓█▓▒▒▒▒▒░░▒▒▒                
\t\t\t\t\t        █▒▒▒▒▒▒█▒▒▒▒▒▒▓▓▓▓▓▓▓█▒▒▒▒▒▒▒▒▒█                 
\t\t\t\t\t             █▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒                 
\t\t\t\t\t            ▒▒▒▒▒▒▒▒▒▒▒▒     ▓▒▒▒▒▒▒▒▒▒▒▒                
\t\t\t\t\t           █▒▒▒▒▒▒▒▒▒▒▓        ▒▒▒▒▒▒▒▒▒▒                
\t\t\t\t\t           ▓░▒▒▒▒▒▒▓             ▒▒▒▒▒▒▒▒▒▒              
\t\t\t\t\t           ▒▒▒▒▒▒▒▒                ▒▒░░▒▒▓▒▒             
\t\t\t\t\t           ▒▒▒▒▒▒▒▒█               ░░▒█▒▒▒▒▒             
\t\t\t\t\t           █▒▒▒▒▒▒                 █▒▒▒▒▒▒▒▒             
\t\t\t\t\t           █▒▒▒▒▒                      ▒▒▒▒▒▒▓           
\t\t\t\t\t          ░░░░▒▒▒▒                     █▒▒▒▒▒▒           
\t\t\t\t\t       ░░█░░░░░▒▒▒                     ▒▒░░░░▒▒          
\t\t\t\t\t             █▓█                     █▒▒▓▒▒▒▓▒▓▒         """+Fore.RESET,"Machoke", "Lucha", "Súperpoder", "Primera", "Zona 1", "Pradera", "Frutas", "Fuga"),
            Pokemon(Fore.LIGHTCYAN_EX+"""\t\t\t\t\t              ░░▒                                        
\t\t\t\t\t          █▒▒▒▒▒▒▒▓                                      
\t\t\t\t\t         ░▒▒▒▒▒▒▓▓▓                                      
\t\t\t\t\t          ▒▒▒▒▓▓▓▓█                  ░█░░░▒▒█            
\t\t\t\t\t          ▒▓▓▒▒▒                     ▒▒░▒▒▒▒▒            
\t\t\t\t\t          █▒▒▒▒▒▒                    ░█▓▓▓▓█▓            
\t\t\t\t\t           ▒▒▒▒▒▒▒                      ▒▒▓▒▒█           
\t\t\t\t\t           █▒▒▒▒▒▓▓█░░█       ▒▒         ▒▒▒▒▒           
\t\t\t\t\t            ▒▒▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▓▒▒▓▒     █▒▒▒▒▒▒          
\t\t\t\t\t               █▓▓▒▒▒▒▒▒▓▓░░░▒▒▓▒▒▒█░░▒▒▒▓▒▒▓▒▒          
\t\t\t\t\t                ░░░▒▒▒▒▒▒▒▓░▒▓░▒▒▒▒▓▒▒▓▓▓▒▒▒▒▒▒          
\t\t\t\t\t           ░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░▓░▒█░▓▓▓▓▓▓▓▓              
\t\t\t\t\t        ░▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒█▒░░▒▒▒░░░█▒░░█                  
\t\t\t\t\t        ▒▒▒▒▒▒▓▓▓▓░▓▓▒▒░░▒▒▒░▓░░░▓▒▒▒▒▒▒                 
\t\t\t\t\t        █▒▒▒▒▒░█▒▒▒▒▓▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒█              
\t\t\t\t\t         █▒▒▒▒▒▒▒▒█ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒░░░░▒▒          
\t\t\t\t\t            ▒▒▒▒▒▒▒█  ▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▓░░░▒         
\t\t\t\t\t                      ▓▓█░██▓▒▒▓        █▒▒▒▒▒▒▒▒▒▓      
\t\t\t\t\t                   █▒▒▒▓▓░░░░███            ▒▒▒░▒▒▒▒     
\t\t\t\t\t                 ▒░▒▒▒▒▒█████▒▒▒▒▒▒▒        ▒▒▒█▒▒▒█▓    
\t\t\t\t\t                ▒▒▒▒▒▒▒▒████▒▒▒▒▒▓▒▒▒▒           █▒▒     
\t\t\t\t\t               ▒░▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒█                  
\t\t\t\t\t             ▒▒▒▒▒▒▒█          ▓▓▓▓▓▓▓                   
\t\t\t\t\t            ▓▒▒▒▒▒▒             ▓▓▓▓                     
\t\t\t\t\t            ▒▒▒▒▒█             ▓▓▓▓▓                     
\t\t\t\t\t           ▓▒▒▒█                ▓▓▓▒▓▒▒█                 
\t\t\t\t\t         █▒▒▒▒▒▒                  █▒▒  █                 
\t\t\t\t\t       ░▒▒█▒▒▒                                           """+Fore.RESET,"Machamp", "Lucha", "Súperpoder", "Primera", "Zona 1", "Pradera", "Frutas", "Fuga"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                         █░░░░█                          
\t\t\t\t\t                      █░░░░░░░░░░░                       
\t\t\t\t\t                     ░░░░░░░░░░░░░░                      
\t\t\t\t\t                    ░░░░░░░░░░░░░░░░                     
\t\t\t\t\t                   ▒░░░░░░░░░░░░░░░░                     
\t\t\t\t\t                   ▓░░░░░░██░░░░░░░░                     
\t\t\t\t\t                  ░░░░░░░░░░░░░░░░░                      
\t\t\t\t\t                 ░░░░░░░░░░░░░░░░░                       
\t\t\t\t\t              ░░░░░▓░░░░░░░░░░░  █                       
\t\t\t\t\t              ▒░▒██▒▒▒░░░░░█     ▓                       
\t\t\t\t\t               ░░▒███▒▒░▓       █                        
\t\t\t\t\t             ▒░░░▒▒▒▒▒▒▒▒█     ██     █░░░▒▒█            
\t\t\t\t\t           ░░█░░░░░▒█▒▒▒▒▒▒   ▓▓  ░░░█░░░░▒█▒▒▒▒         
\t\t\t\t\t          ▒░░░░░▒▒▒▒▒▒▒▒▒▒▓▒ ▒▒▒▓░░░░░░░░░▒▒▒▒▒▒▒▒       
\t\t\t\t\t         ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒█     
\t\t\t\t\t            █▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒█░░░░░░░▒▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t               █▒▒▒▒▒▒▒█  ░▒▒ █▒▒▒▒▒▒▒▒▒▒▒▒▒▒█           
\t\t\t\t\t                         ▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒█             
\t\t\t\t\t                         ▒▒▒        ███                  
\t\t\t\t\t                         ▒▒█                             
\t\t\t\t\t                         ▓▓█                             
\t\t\t\t\t                  █▒▒▒▒▒██▓▓                ▓            
\t\t\t\t\t               ▒▒         ▓▓█                 ▒█         
\t\t\t\t\t             █              ▓█           ███▒▒           
\t\t\t\t\t          █ █                 █▓       █▓     █          
\t\t\t\t\t           █                    █   ██                      
\t\t\t\t\t            ▒█                  ▒█▒                      """+Fore.RESET,"Bellsprout", "Planta", "Campana", "Primera", "Zona 1", "Pradera", "Hojas", "Exposición a la luz solar"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                                        █▒▒▒█            
\t\t\t\t\t                                     ▒▒▒▒▒▒▓▓▓▓          
\t\t\t\t\t  █▒░░░▓█                   █░░░░█░░░░▓▓      ██         
\t\t\t\t\t ▒░░░░░░░░▒▒▒▓           ░░░░░░░░░░░░░░                  
\t\t\t\t\t  █▒▒▒▒▒▒▒▒▒▒▒▒▒█      ░░░░░░░░░░░░░░░░█       ██░░▒█    
\t\t\t\t\t    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒   █░░░░░░░▒▒░░░░░░░░    ▒▒░░░░░░░░░░░█
\t\t\t\t\t    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒░░░░░░░░░░░░░░░░░██▒▒▒▒░░░░░░░░█   
\t\t\t\t\t     ▒▒▒▒▒▒▒▒▒▒▒▒▒▓░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░▒█     
\t\t\t\t\t      ▒▒▒▒▒▒▒▒▒▒█░█░░░░░░█░░░░░░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒      
\t\t\t\t\t      ▒▒▒▒▒▒▒▒▒▒░███░░░░░░████░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t       ▒▒▒▒▒▒▒▒▒░░░░░░░░░░███░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█       
\t\t\t\t\t        ▒▒▒▒▒▒██▒░░░░░░░░░░░░░░░░▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t          █░░░░░░░░░░░░░░░░░░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t         █░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒          
\t\t\t\t\t         ░░░░█████░░░░░░▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t         █▒▒▒▒████▓▓█▒░░▒▒░░░░░░░░░░░█▒▒▒▒█              
\t\t\t\t\t          █▒▒▒▒███▓▓▓▓▒▒▒▒█░░░░░░░░░                     
\t\t\t\t\t           █▒▒▒████▓▓▓▓▒▒▒▒░░░░░░░░                      
\t\t\t\t\t            █▒▒▒████▓▓▓▓▒▒▒░░░░░░                        
\t\t\t\t\t             ▒▒▒██████▓▓▒▒▒░░░░█                         
\t\t\t\t\t             ▒▒▒▒██████▒▒▒█░░                            
\t\t\t\t\t             █░░░▒███░░▒▒█                               
\t\t\t\t\t               ▒▒░░░░▒▒█                                 """+Fore.RESET,"Weepinbell", "Planta", "Planta de vuelo", "Primera", "Zona 1", "Pradera", "Hojas", "Exposición a la luz solar"),
            Pokemon(Fore.LIGHTGREEN_EX+"""\t\t\t\t\t                    █▒▒█                                 
\t\t\t\t\t                  ▒▒▒▓▒░░▒▒▒▒▒▒▒█                        
\t\t\t\t\t              ███▓▓▒▒░▒▒░▒▒▒▒▒▒▒▒▒▒▒                     
\t\t\t\t\t          █▒░░░░▒█▒▒▒▒▒▒▒▒▒▒▒▒▓█                         
\t\t\t\t\t        ▒▒▒░▒░░░▒█░▒▒▒▒▒▒▒▒▒▒  █▓█                       
\t\t\t\t\t       ▒▒▒▒▒▒▒▒░▒▓▒▒▒▒▒▒▒▒▒▒▒▒   █▓█                     
\t\t\t\t\t     █▒▒▒█▒░▒▒▒░▒▒▒▒▒▒▒▒▒████▒▒█   ▓▓                    
\t\t\t\t\t    █▒     ▒▒▒▒▒▒▒▒▒▒█████████▒▒     ▓                   
\t\t\t\t\t               ▒▒█▒▒██████████▒▒      ▓█                 
\t\t\t\t\t              █▒▒█████████████▒▒       ▓█                
\t\t\t\t\t              ▒▒██████████░██░▒░░       ▓█               
\t\t\t\t\t      ▓▒▒░█░▒▒▒██░█████████░░▒░░░░      █▓  █░░▒▒▒▒▒▒▒▒▒ 
\t\t\t\t\t    ▒▓█▒▒▒▒▒▒▓█░░░████▒░░░░█░░░░░░░    █░▒▒▒░░▒▒▒▒░▒▒█   
\t\t\t\t\t   ▒▓█  ▒▒▒▒▒▒▒▒▒▓█▓▒███▓▓█░░░░░░░▒▒ ▒▒▒░░▒▒▒▒▒▒▒▒▒█     
\t\t\t\t\t        █▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░▒▒▒▒▒▒      
\t\t\t\t\t         ▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒░░░▒▒▒▒▒▒░░▒░░░░▒▒       
\t\t\t\t\t        █▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░▒▒       
\t\t\t\t\t        █▒▒▒▒▒▒▒▒▒▒█▒░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░▒░▒▒▒▒       
\t\t\t\t\t█░      █▒▒▒▒▒▒▒▒▒█░░░░░░░░▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t█░░▒█    ▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒█        
\t\t\t\t\t ▒▒▒▒▒▒   ▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒█         
\t\t\t\t\t  ▒▒▒▒▒▒    ▒▒▒▒▒░░░░░░▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒           
\t\t\t\t\t   █▒▒▒▓█        ░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒              
\t\t\t\t\t          █▓█     ░▒░░░░░░░░░░░░░░░░                     
\t\t\t\t\t                   █░░░░░░░░░░░░░░                       
\t\t\t\t\t                       █░░░░░▓█                          """+Fore.RESET,"Victreebel", "Planta", "Planta de vuelo", "Primera", "Zona 1", "Pradera", "Hojas", "Exposición a la luz solar"),
            Pokemon(Fore.BLUE+"""\t\t\t\t\t                         ▒░▒▒░░▓▓▓▓▒                     
\t\t\t\t\t                      ░░░░▓▓░▓▓▓▓▓▓▓▓█                   
\t\t\t\t\t                    ░░░░█▒▓▓▓▓▓▓▓▓▓▓▓▓█                  
\t\t\t\t\t                  ▓░░░░░▒█▓▓▓▓▓▓▓▓▓▓▓▓▒▒                 
\t\t\t\t\t                █░░░░░░░░▒▓▓▓▓▓▒▒▒▒▓▓▓▒▒░                
\t\t\t\t\t                ░░░░▒▒░░░░█▓▓▒▒▒▒▒▒▒▒▓▒▒░█               
\t\t\t\t\t               █▓█░▓▓▒░░░█▒▒▓▓▒▒▒▒▒▒▒▒▒▒░█               
\t\t\t\t\t               █░▓▓▒▒░░░░▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒█               
\t\t\t\t\t                ▒░██░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        ▓▒█     
\t\t\t\t\t                 ░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█        ▓▒▒▒▒   
\t\t\t\t\t                 █░▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█          ▒▒▒▒▒█ 
\t\t\t\t\t                  ░░░▒▒▓░▓░░░▒█▒▒▒▒▒▒▒█            ▒▓▓▒▒ 
\t\t\t\t\t                  ░░▒▒▒▒▓▒█▒▒▒▒▒▒▒▒▒▒█▒██▒▒██       ▒▓▓▒█
\t\t\t\t\t                  █░█▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█    ▒▓▓ 
\t\t\t\t\t                  ░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒▒░█████▒    ▒▒▒ 
\t\t\t\t\t                  █░▒▒█▓▓▓▓▓▒▒▒▒▓▓███░░▓████████▒   ▒▒▒  
\t\t\t\t\t                  ███▓█████▓▒▒███████▓█████████▓   ▒▒▒   
\t\t\t\t\t                   █▒█████████████████▓▒▓▓▓▓▓█   █░▒█    
\t\t\t\t\t                 ▒▒█  ███████████████▓▓▓█▒▒▒▒▒▒▒▒▓       
\t\t\t\t\t    █▒▒▒▒▒▒▒▒▒██           ████████▓▓▓▓█                 
\t\t\t\t\t  ░░░▒▒▒█                                                
\t\t\t\t\t ░░░▒▒                                                   
\t\t\t\t\t█▒▒▒█                                                    
\t\t\t\t\t █▒█                                                     """+Fore.RESET,"Tentacool", "Agua", "Medusa", "Primera", "Zona 2", "Mar", "Algas", "Absorber"),
            Pokemon(Fore.BLUE+"""\t\t\t\t\t                            ▓▒▒▒▓███                     
\t\t\t\t\t                       █▒▓█░░░▒▓▓░▒▓▓▓▓▒                 
\t\t\t\t\t                     ▒░▒▓█░░░▒▓▓▓▓▓▓▓▓▓▓▓▒               
\t\t\t\t\t                   ▒▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓              
\t\t\t\t\t                  ▒▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓              
\t\t\t\t\t                  ▒▓▒▒▒▓▒▒▒▒▒▒▒█▓▓▒▒▒▒▒▒▓▒▓▒             
\t\t\t\t\t                  ▒▒▒▒▒░▓░▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t               ▒▒▒▒▒▒░▒▒█▓▒▒█▒▒▒▒▒▒▒▓▓▓▒▓▒▒▒▒▒▒▒▒▒█      
\t\t\t\t\t              ▒▒▒▒▒▒░▒░░▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒     
\t\t\t\t\t              █▒▒▒▒░▒▒▒░░░░░░▒▒▒█░█▓▒▒░░░▒▓▒             
\t\t\t\t\t                 █▒  █░█▒▓▒▒▒█░▒░███████▓                
\t\t\t\t\t                    █▒██▓█▒█▓▓▓█████▒▓▒██▒█              
\t\t\t\t\t                 █▒▒▒▓ ▒▒▒▒▒▒▒█▒██▒▒▓▒▒▓▒█  ██           
\t\t\t\t\t     ▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██░▒▒▒▓▓██▒ ▓ ▓▒▓█▒ █▒   ▒         
\t\t\t\t\t  ▓▒▒▒▒▓      ▒██▒  █▓░▒▒▒▒▒█▓ ▓ ▒█  ▓▓▒▒▓▒ █▒▒▒▒▒▒▒▒█   
\t\t\t\t\t ░▒▒▒█       ▒█ ▒█▓▓█▒▒▒▒▒█▒▓ ▓ █▓ ▒▒▒▓▒▒▒▒▒▒█▒██▒▒▒░░░▒ 
\t\t\t\t\t█░░▒█      █▒▒▓▒▒█  █▒▒▒▒▒▒█▒ ▓▓▓     ▓▓▓  ▒▓  ▒█  ▒▓▒▒▒▒
\t\t\t\t\t ░▒▒    █▒▒▓▒█ ▒▒█ ▒▓▒▒▒▒▓█ ▒▒▓       ▓▓█  █▒█  ▒█ █▒    
\t\t\t\t\t █▒█   ░▒█ █▒   ░▒▒▒ ▒▒▒▒▒  ▒█▒▒█    ▓▓█  █▒▒▒  ▒▒  ▒    
\t\t\t\t\t       ▒   █▒█    ▒█  ▒▒▒▒▓█▒ ▒█▒▒  ▓▒   █▒ ▒▒█  ░█      
\t\t\t\t\t            █        █▒▒▒▒▒▒█  ▒▒█ ▓▒   ▒▒  ▒▒█  ░█      
\t\t\t\t\t                      ▒█  ▒▒▒         ▒▒█   ▒▒█          
\t\t\t\t\t                                            ░▒           """+Fore.RESET,"Tentacruel", "Agua", "Medusa", "Primera", "Zona 2", "Mar", "Algas", "Absorber"),
            Pokemon(Fore.LIGHTBLACK_EX+"""\t\t\t\t\t                                                  ▒      
\t\t\t\t\t     ░▒▒▒                                      ▒░▒▒▒▒    
\t\t\t\t\t █▒▒▒█▒▒▒▒           ███▒▒▒▒▒▒▒               ▒▒▒▒▒▒▒▒▒  
\t\t\t\t\t▓▒▒▒▒▓▓▓█▒▒        ▒▒▒▒▒▒▒▒▒▒▒▒▒             ▒▒▒▒▒▒▒▒▒▒▒ 
\t\t\t\t\t▒▒▒▒█▒▒▒▒▒▒      ▒░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓           ▒▒█▒▒▒▒▒▒▒▒█
\t\t\t\t\t ▒▒▒▒▒▒▒▒       ░░░░▒▒▒░▒▒█░▓▒▒▓▓▒▒████   ░░▒▒▒▒▒▒▒▒▒▒▒▒▒
\t\t\t\t\t  ▒▒▒▓▒▒█      █▒▒░▒▒▓▒▒▓░░▓░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓█   
\t\t\t\t\t   █▒▒▒▒▒▒      █▒░░▓▒▒▒▒░▒▒▒▒▒▓▓▒█████▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t    ░▒▒▒▒▒█   ▓▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▓▒▒                      
\t\t\t\t\t     ░░▒▒▒▓ █▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓                       
\t\t\t\t\t      █▒▒▒▒▒▒▒█    █▒▒▒▒▒▒▒▓▓▒▒▒                         
\t\t\t\t\t          ▒▒█         █▒▒▓▓▓▓                            """+Fore.RESET,"Geodude", "Roca", "Roca", "Primera", "Zona 2", "Montaña", "Minerales", "Cabeza de roca"),
            Pokemon(Fore.LIGHTBLACK_EX+"""\t\t\t\t\t                     █▒░░█                               
\t\t\t\t\t                    ▓░░░░░░▒░░▒░░▒▓                      
\t\t\t\t\t                 ▒░░▒░░░░░░░░▒░░▒▒░▒▓█                   
\t\t\t\t\t               █▒░▒░░░░░░░░░░░░░▒░▒▒▒▒▒░░▓▓▒▒█           
\t\t\t\t\t               █░░░█░░░░░░░░░░░█▒▒░░░░▒░░░░░░░▒          
\t\t\t\t\t            ▒░▒█░▒░░░░░░░░░░░░▒▒░░▒▒▒▒▒▒░▒▒▒█▓░░░░░      
\t\t\t\t\t          █░░░░▒▒▒▒░░░░░░░░░░▓▒▒▒▒░░░▒▒▓ █▒▒▒░░░▒▓▓ █▒██ 
\t\t\t\t\t       ▒░░░▒▒▒░░▒▒▒▓▒▒▒▒▒▒▒▒░▒▒▒░░░░░▒▓▓   ▒▒░▒▒▓▓▓█▓▓▓▓█
\t\t\t\t\t      ▓░█▒░░█ ▒░░░░░░▒▒░▒▒▒▒▒▒▒▒▒░░░░▒█▓     █▓▓▓▓▓▓▓█   
\t\t\t\t\t    █░░░█▒▒▒  ▓▒░░░▒▒▒▒▓▒▒█▒▒▒▒▒▒▒░░▒▒▒▓    ░▒▓▓▓▓█      
\t\t\t\t\t    ▒░█▒▒▒▒    ▓░▒░░▒▒▒▒▒▒▒█▒▒░▒▒▒▒▓▓▒▒    █▒▓           
\t\t\t\t\t █░▓▓▓▓▓▒▒     ▓▓▓▒▒▒▒▒▒██▓█▓▓▓▓▓█▓▓▓██                  
\t\t\t\t\t  ██▓▓▓▓█▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓█▓▓▓                  
\t\t\t\t\t ░▒▓█▓▓██ ██        ▓▓▓▓█▓▓▓█▓▓█▓█▓▓▓█                   
\t\t\t\t\t▒░█                   ▓▓▓▓█                              """+Fore.RESET,"Graveler", "Roca", "Roca", "Primera", "Zona 2", "Montaña", "Minerales", "Cabeza de roca"),
            Pokemon(Fore.LIGHTBLACK_EX+"""\t\t\t\t\t                               █▒▒▒▒█                    
\t\t\t\t\t                       ▒▒▓█ ▒▒▒▒▒▒▒▒▒▒▒▒▒                
\t\t\t\t\t                    ▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██             
\t\t\t\t\t                  ▒▒▒▒▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓█         
\t\t\t\t\t                ▒▒▒▒█▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓█▓▓▓▓▓▓▓█      
\t\t\t\t\t               ▒▒▓█▒▒▒▒▒██▓▓▓█▒███░█▓▓▓▓░▓███▓▓▓▓▓▓▓     
\t\t\t\t\t               ▓▓▒▒▒▒▒▒▒▒▒█▓▓▓▓▓█▒▒░░▒▒▒░░▒██▓▓▓▓▓▓▓█    
\t\t\t\t\t  █          ██▓▒▒▒▒▒▒▒▒▒▒█▓▓▓▒▒▒▒▒▒▒▒▒▒█▒▒▓▓██▓▓▓▓▓▓▓   
\t\t\t\t\t   █░░▒ ░   ▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒█░▒▒▒░░▒▒▓▓▓▓█▓▓▓▓▓▓  
\t\t\t\t\t     ▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓██▓▓▓█ 
\t\t\t\t\t    █▒▒▒▒▒▒▓▒▒▒█░░░░░░▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓████▒▒▒▒▓▓▓▓▓█▓▓▓ 
\t\t\t\t\t █░▓▒▒▒▒▒▒▓██░░░░░░░▒▒▓▒▒▒█▓▒▒▒▒▒▒▒▒▓▓▓█░░▒▒▒▒▒█▓▓▓▓█▓▓▓ 
\t\t\t\t\t          ▓▓░░░░░▓░░░▒▒▒▒▒▒▓▓█▒▒▒▓▓▓▓▓▓█░░░█▒▒▒▒██████▓▓ 
\t\t\t\t\t          █▒░░░▒▒▒██▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓█░░░█▒▒▒▓▓▓█▓▓▓██ 
\t\t\t\t\t           ░░░▒▒▒▒▒▒▒██▒▒▓▓█▓▓▓▓▓▓█▓▓███▓▓▓▓▓▓▓▓▓█▓▓▓▓   
\t\t\t\t\t          ▒▓▒▒▒▒█▒▒▒▒▒▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█▓▓▓▓   
\t\t\t\t\t                ▒▒░▒▒▒▒█▓▓▓▓▓▓██▓▓▓▓▓▓█▓▓▓▓██▓███▓▓▓▓    
\t\t\t\t\t              ██░░░░▒▒▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓░░░░░░░▒▒▓▓█    
\t\t\t\t\t               █▓▓█▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓███░░░░░░░░░▒▒      
\t\t\t\t\t                ▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓█░░░░░░░░░▒▒█     
\t\t\t\t\t               ▒▒▒▒▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓░░░░░░░░░▒▒▓     
\t\t\t\t\t              █▓▓▓▓▓▓▓▓▓▓█    █▓▓▓▓▓▓▓▓▓▓█▒▒░░▒▒▒▒▒▓▓    
\t\t\t\t\t           ░█▒▒▒▓▓▓▓▓▓▓▓▒▓                 ▒▒▒▒▒▓▓▓▓▓    
\t\t\t\t\t          █▒█▒▓▒▓▒█                        ▒▒▒▒▓▓▓▓▒▓▒   
\t\t\t\t\t              █                           ▒▒▒▒▒▒▒▓▓▓▒▒   
\t\t\t\t\t                                         ░░▒░█▒▒▒░█▓▒░░  
\t\t\t\t\t                                        █  █░░  ▓░░    ░ 
\t\t\t\t\t                                           ░     ▒       """+Fore.RESET,"Golem", "Roca", "Roca", "Primera", "Zona 2", "Montaña", "Minerales", "Cabeza de roca"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t                              ▓                          
\t\t\t\t\t                            ▓▓▒                          
\t\t\t\t\t                 ░░░▒░░▒▒▒░░▒▒▒                          
\t\t\t\t\t               ░░░▒▒▒▒▒▒░░▒▒▒▒▓                          
\t\t\t\t\t              ░░▒▒▒░▒▒▒▒▒▒▒▒▒                            
\t\t\t\t\t             ▒░▒▒▒▒▒▒▒░░░▓▒▓                             
\t\t\t\t\t             ▓▒▒▓▒▒░░░░█▓▓█                              
\t\t\t\t\t             ░░░░███░░░▒░▒                               
\t\t\t\t\t           ░░░░░░█▓░░░░░█▒▒                    ▓░▓       
\t\t\t\t\t           ░░░░░░░░░░░░░░▒▒        ░▓ ░▒▒▒▒▒░▓   ░▓      
\t\t\t\t\t            ██▓   ░░░░░░░▒▒▒▒░      ▒░▒▒▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t                  ▓░░░░░░░▒▒▒       ▒▒▒░▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t                  █░░░░░░░░▒ ▓▒▒▒▓ ░▒▒▒▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t                  ░░░░░░░░░░░░░░░░░░▓▒▒▒▒▒▒▒▒            
\t\t\t\t\t                  ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒            
\t\t\t\t\t                  ░░░░░░░░░░░░░░░░░░░░░ ▓▓▒▒             
\t\t\t\t\t                  ░▒░░░░░░░░░░░░░░░░░░░▓░ ▓▓             
\t\t\t\t\t                  ░░░░░░░░░░░░░▓░░░░░░▒▒▒▒░░             
\t\t\t\t\t                  █░░░░░░░░░▒░▒▒░░░░░░▒▒▒▒▓              
\t\t\t\t\t                   ░░░░▒░░░░▒▒▒▓▒ ░░░░▒▒▒▒▒              
\t\t\t\t\t                   █░░░▒▓░░▒▒▒▒▒█  █░░░░▒▒               
\t\t\t\t\t                    ░░░  ░░░▒▓▒▒█    █░░░                
\t\t\t\t\t                    ░░░   ░░░ ▒▒█     ░░▒                
\t\t\t\t\t                    ░░    ░░ ▒▒      ▓░░                 
\t\t\t\t\t                   ▓░░   █░░░░█      ░░█                 
\t\t\t\t\t                   ░░░   ░░░██      ░░░                  
\t\t\t\t\t                  ▓██    ▒█░       ▓▓██                  
\t\t\t\t\t                        ▓███                             """+Fore.RESET,"Ponyta", "Fuego", "Caballo", "Primera", "Zona 3", "Volcán", "Bayas", "Huida"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t                                    ▓     ▓              
\t\t\t\t\t                                  ░░░░░░░░               
\t\t\t\t\t                                   ░░░░░▒                
\t\t\t\t\t                               █▒▒░░▒▒░░░▒▒▒             
\t\t\t\t\t                               ░▒▒▒▓▓░▒░▒▒▒▒▓            
\t\t\t\t\t                         ░░█   ░░░░░▒░▒▒▒▒▒▒▒▒           
\t\t\t\t\t             ░░░▓  ░░ ░░▒▒░▒▓ ░░░▓░░░░▒▒▒▒▒▒▒▒           
\t\t\t\t\t         ▒▒▒▒▓▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░▓▒▒▒▒▓▒▓           
\t\t\t\t\t         ▒░▓▓ ▓▒▒▒   ▓▓▒▒▒▒░░░░░░░▒░░░░▒▒▒               
\t\t\t\t\t                      ▒▒▒▒▒▒▒█▒▒▒░░░░░░▓ ▓               
\t\t\t\t\t                       ▒▓▒▒▓  ▓▒ ░░░░░░░                 
\t\t\t\t\t             ▓░░░          ▒  ▒▒▓░░░░░░░█                
\t\t\t\t\t              ▒▒▒▒ ▒░▓░░░▓▒░░▒▒▒░░░░░░░░░                
\t\t\t\t\t         ░░░░░▒▒▒▒▒▒▒▒▓▒▒▒▒▒░▓█░░░░░░░░░░                
\t\t\t\t\t         ░▒▒░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░  ▒░           
\t\t\t\t\t       ░▒▒▒▓▒▒▓  ▓▒▒▒▓░░░░░░░░░░░░░░░░░░░░█▓▒            
\t\t\t\t\t      ▓░▒█      ▒░▒▒▒▓░░░░▓░░░░░░░░░░░░░░░░░█            
\t\t\t\t\t                  ▒▒  ░░░░░▓░░░░░░░░░░░░░░░░░░░░░        
\t\t\t\t\t                    ▓ ░░░░░ ▒▒█▒░░░░░█   ░░▒▒▒▓░░░       
\t\t\t\t\t                    ▒▒░░░░  ▒▒▒▒  ░░░█     ▒▒▒▒░░        
\t\t\t\t\t             ▒▒ ░░░  ░░░░░ ▒▒▒▒    ░░░     ▒ ▓░░         
\t\t\t\t\t           ▓▒░░▒▒▒░▒█░░▒▒▒▒▒▒░░    ░░░      ░░░          
\t\t\t\t\t           ░     ▒▒░ ░░   ▒▒█▒▒ ▓░  ░░    ▓▓█            
\t\t\t\t\t                ▒▒▒▒▒░░   ▒▒▒▒▒▒▒░▓▒█░█                  
\t\t\t\t\t                    █▒░       ▒░█▒▒▒▒░░                  
\t\t\t\t\t                     ░░█       ██▒▒▒▒░░▒                 
\t\t\t\t\t                     █▓▓             ▒░▓                 
\t\t\t\t\t                                      ███                """+Fore.RESET,"Rapidash", "Fuego", "Caballo", "Primera", "Zona 3", "Volcán", "Bayas", "Fuga"),
            Pokemon(Fore.LIGHTMAGENTA_EX+"""\t\t\t\t\t                         █░░░░░░░░░░▒▒▓█                 
\t\t\t\t\t                      █░░░░░░░░░░▒▒▒▒▒▒░░▒▓              
\t\t\t\t\t                      █          █▒▒▒▒▒▒▒▒▒░▒█           
\t\t\t\t\t                                     ▒▒▒▒▒▒▒▒▒▒          
\t\t\t\t\t                                       ▒▒▒▒▒▒▒▒▒█        
\t\t\t\t\t                                         ▒▒▒▒▒▒▒▒▓       
\t\t\t\t\t                                          ▒▒▒▒▒▒▒▒█      
\t\t\t\t\t                                          █▒▒▒▒▒▒▒▒      
\t\t\t\t\t       ░░░▒▒▒ ██▓▒█   █░░░░▒      █        ▒▒▒▒▒▒▒▒      
\t\t\t\t\t      ░░░▒▒░░░░░░░░▒▒█▒▒░░█▒▒░░░░░░░░░░░█ █▒▒▒▒▒▒▒▒      
\t\t\t\t\t      █▒█░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒▓▒▒▒▒▒▒▒      
\t\t\t\t\t       ░░▒░░░▒▒▒▒   ░░█▒▒▒▓░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      
\t\t\t\t\t      ▓░░▓▒░░▒▓▒▒  ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒█      
\t\t\t\t\t      ░░░░░░░░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒       
\t\t\t\t\t    █░░░░░░░░░░░░░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t     ░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█       
\t\t\t\t\t     ░▒▒▒▓▓▒▒▒▒████▒▒█░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t   ░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t  █▒▒▒▒▒▒░▓█▒▒▒▒▒▒░░▓░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▓     
\t\t\t\t\t  █▒▒▒▒▒▒▒▒▒▓░░░░▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓   
\t\t\t\t\t    ▒▒▒▒▒█░░░  █▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█   
\t\t\t\t\t              ▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▓▒▒▒▒▓█             """+Fore.RESET,"Slowpoke", "Agua", "Babosa", "Primera", "Zona 2", "Río", "Algas", "Naptime"),
            Pokemon(Fore.LIGHTMAGENTA_EX+"""\t\t\t\t\t              ░░░█         █░░░▒                         
\t\t\t\t\t            █▒▒▒░░░░░░░░░░░▒▒▒▒█▒                        
\t\t\t\t\t            ░▒▒▒░░░░░░░░░░░▒░▒▒▒▒                        
\t\t\t\t\t              █░  ░░░░░░░░░  ░▒                          
\t\t\t\t\t              ░░░░░▒░░░░░▓░░░░▒▒                         
\t\t\t\t\t              ░░▓░░░░░░░░░░░░█▒▒           ░░ ▒░         
\t\t\t\t\t             █▓░░░░░░░░░░░░░░░░▒     ░█    ▓░▒▒▒█        
\t\t\t\t\t             █░░░▒▒▒▒▒▒▒▒▒▒█░░▒▒    █▒▒▓  ▒▒▒▒▒▒▓▒       
\t\t\t\t\t             █░░▓░█░░░░░░░█░▓▒▒▒     ▒░░░░░░░░░▓▒        
\t\t\t\t\t             █░░░▒▒▓░░░░░░▒▒▒▒▒▒▒   █▒█░▒░░░░░░▒▒        
\t\t\t\t\t            █░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▓░░░░░░░░▒▒▒       
\t\t\t\t\t            ░░░░▒░░░▒▒▒▒▒▒▒▒▓░░░░░▒░░░░░░░░░░░▒▒▒▒       
\t\t\t\t\t           █░░░░░▓░░▒░░░░▒▒█░░░░░░▒░░░░░░▒░░░▓▒▒▒█       
\t\t\t\t\t           █░░░░░▒▒░░░░░░░░░░░░░░░▒░░░░░░░░░▒▒▒▒▒        
\t\t\t\t\t            ░░░░░▒█▒░░░░░▒░░░░░░░▒▒▓░░▒░░░░▒░▓▒▒▒█       
\t\t\t\t\t           ▒░░░░▒▒▒▓▓▒▒▒▒▓░░░░░░▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒█     
\t\t\t\t\t          ░░░▒█▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▓▓▒▓▒        
\t\t\t\t\t         ░░░█░░░░▓░░░░░░░░▒▓▓░▒░░░░░░░▒▒▒░▓█▒▒▒▒         
\t\t\t\t\t        ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓░▒▒▒         
\t\t\t\t\t        ░░░░░░░░░░█░░░░░░░█░█░░░░░░░░░▒▒▒▒███▒▒█         
\t\t\t\t\t        █▒▒▒▒▒▒█░░░░░░░░░▒▒▒█░░░░░░▒▒▒▒▒▒██▒▒▒▒          
\t\t\t\t\t         █▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t           ▒▒▒▒▒▒▓▒▒  █▓▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█               
\t\t\t\t\t        █░░▒░░▒▒▒▒▒█          ▒▒▒▒▒▒▒▒▒                  
\t\t\t\t\t           ░█                 ▒▓░░▒▒░▒▒                  
\t\t\t\t\t                               █░░ █░░█                  """+Fore.RESET,"Slowbro", "Agua", "Ermitaño", "Primera", "Zona 2", "Mar", "Algas", "Naptime"),
            Pokemon(Fore.WHITE+"""\t\t\t\t\t                          ███                    ▒▒▒█    
\t\t\t\t\t                      ▓▓▓▓▓▓▓▒▓             ▒▒▒▒▒▒▒▒▓    
\t\t\t\t\t                     ▓▓▓▓▓█▒▓▓          ▒░░▒▒▒▒▒▒▒▒█▓▓   
\t\t\t\t\t                        ▒▓▒▒▓         ▒░░░▒▒▒█▓▓▓▓█      
\t\t\t\t\t                        ▓░░░░░░░░█   █░░░▒▓▓█            
\t\t\t\t\t                      ░░░░░░░░░░░░░░ ░░░░▒▓        █▒█   
\t\t\t\t\t                    ▒░░░░░░░░░▒░░░░░░░░░▒▒▒▓▓▒▒▒▒▒▒▒▒▒▓  
\t\t\t\t\t                   ▒░▒░░░░░░░░░█░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  
\t\t\t\t\t  ▓▓▒▒▒▒▒▒▒▒█     ▓░░░░░░░░░░░░░░░░░░░░█▒▒▒▒▒▒██▓██▓     
\t\t\t\t\t  █▓▓▓▒▒▒▒▒▒▒▒▒▒▒ █░░░░░░░░░░░░▒░░░░░░░░   █             
\t\t\t\t\t    █▓▓▓▓▓▓▓▓█▒▒▒▒█░░░░░░░░░░░░░░░▓█░█░▓                 
\t\t\t\t\t             █▓▓▒▒▒░░░░░░░░░░░░░▓▒▒▒░▒░                  
\t\t\t\t\t        ▒▒▒▒▒▒▓▒▒▒▒░▓░░█░░░░░░░░░░█▒▓░█                  
\t\t\t\t\t       ▒▒▒▒▒▒▒▒▒▓▓▓▓▓█░█░░░░░░░░░░░░░                    
\t\t\t\t\t        ▒▒▒█▓▓▓▓▓▓▓  █ █░░░░░░░░░░▒                      
\t\t\t\t\t         ▓                                               """+Fore.RESET,"Magnemite", "Eléctrico", "Imán", "Primera", "Zona 2", "Montaña", "Electricidad", "Imán"),
            Pokemon(Fore.WHITE+"""\t\t\t\t\t              ██                                         
\t\t\t\t\t            ▒▒▓▓▓█                         █▓            
\t\t\t\t\t             ▓▓▓▓▓▒         █▓██         ▒▒▒▒▓▓          
\t\t\t\t\t       █▒▓    █▓▒▒▒▒▒     ▒░░░▓░░░     ▒▒▒▒▒▒▓           
\t\t\t\t\t      ▒█▓▓▓▓    █▒▒▒▒▒      ▓██▒▓█  █▒▒▒▒▒▓▓     ▓       
\t\t\t\t\t       ▓▓▓▓▒▒▓   ██▒▒▒▒   ███▒▓█   █▒▒▒▒██    █▓▒▒▓▓     
\t\t\t\t\t         ▒▒▒▒▒▓▓▓▓▓▒▒▒▒░░░░░░░░░▒░█▒▒▒▒▓▓   ▓▒▒▒▒▒▒▓     
\t\t\t\t\t           ▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒█▒▒▒▒█▓█▒▒▒▒▒▒█       
\t\t\t\t\t             ▒▒▒▒▒▒▓█░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒          
\t\t\t\t\t                    ▒░░░░░░    ░░░▒▒▒  ▒▒▒▒▓      █▒▒    
\t\t\t\t\t   ▒▒▒▒▒▒▒▓█        ▒▒░░░░      ░░▒▒▒        ▓▒▒▒▒▒▒▒▒   
\t\t\t\t\t   ▓▒▒▒▒▒▒▒▒▒▓█     █▒▒▒░░░░░░░░░▒▒▒▒     ▓█▒▒▒▒▒▒▒▓     
\t\t\t\t\t         ▒▒▒▒▓▓     ░▓░░▒▒█░░░░▓▒▒█▒▒    █▒▒▒▒▒█         
\t\t\t\t\t ██       ▒▒▒█░░░░░▒▒░█▒▒▒▒▒▒▒▒▒░█░▓▓▒░░▒▒▒▒▒▒▒     █▓▓█ 
\t\t\t\t\t ▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒ ██▒▒█ ▓░█▒▒░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓ 
\t\t\t\t\t █▒▒▒▒▒▒▒▒▒░░░░░░░░░░░▒▒▒▒     ▓░░░░░░░░░░░▒▒░▒▓▓▓▓▓▓▓   
\t\t\t\t\t      █▓▓█▓░░  ░░░░░░░▒▒▒▒     ░░░░░░░░░░░░▒▒▒▓▓▓█       
\t\t\t\t\t           ░░░   ░░█▓▓▒▒▒▒     ▒░█▓▒░░░  ░░░▒░           
\t\t\t\t\t           ██░░░░░░░▒▒▒▒▒▒    █▒▒█▒▒░█░░░░░█░█           
\t\t\t\t\t             ▓░░░▓▒▒▒▓░▒▒▓    ▒▒▒▓█▒▒▒░░░░▒░█            
\t\t\t\t\t             ▒██░░░░░▒░▒▒▓    ▓░▒█▓▒▒▒▒░░░  ▒░▓          
\t\t\t\t\t          ▒▒░█       ░▒▓▓▓     ▓▓▓▓█                     
\t\t\t\t\t           ██▒       ░▓▓▓▓     ▒▓▓▓▓                     
\t\t\t\t\t                     ░▓███      ▓▓▓▓█                    
\t\t\t\t\t                     ░▓▓▓       ▒▒▒█▓                    
\t\t\t\t\t                     ▒███        ▓▓▓▓                    
\t\t\t\t\t                     ▒▓▓█        █▓▓                     """+Fore.RESET,"Magneton", "Eléctrico", "Imán", "Primera", "Zona 2", "Montaña", "Electricidad", "Imán"),
            Pokemon(Fore.WHITE+"""\t\t\t\t\t                            ▒▒█                          
\t\t\t\t\t                 ░          ▒▒▒▒                         
\t\t\t\t\t     █▒▓ █▓█   █░░▒       █ ▒▒▒▒                         
\t\t\t\t\t    █▓▓▓▓▓▓▓▓   ░░░▓    ░░▒█▒▒▒▒█▒▒█                     
\t\t\t\t\t     █▓▓▓▓▓▓▓█  █░░░▓█   ▒▒▒▓▒▒▓▒▒                       
\t\t\t\t\t      █▓▒▒█▓▓█░░ ░░░░▒▓   █▒▒▒▒▒▒▒█                      
\t\t\t\t\t       █▒▒▒█▓▓░░░ ░░░▒▒▓█░░▒▒▒██▒▒▒▒▒                    
\t\t\t\t\t         ▒▒▒▒▓░░░░█▒░▒▒░░██▒██▒█░▒▒▒▒▒                   
\t\t\t\t\t          ▒▒▒▒░░░░▒▒▒▒█░░░██▓▒▓░█░▒▒▒▒█                  
\t\t\t\t\t           ▒▒▒▓█▒▒▒▒▒▒██░█▒▒▒▒░░▓█▒▒▒▒▒                  
\t\t\t\t\t            ▒▒▒█ ▒▒▒▒▒▒▒░▒░░░░░░░░█▒▒▒█                  
\t\t\t\t\t             ▒░█▒▒█▒░░░░░░░░░░░░▒▒█▒▒▒                   
\t\t\t\t\t             █░░▒▒▓▒▒▒█░▒█▒▒▒▒▒▒█▒▒▒▒▒                   
\t\t\t\t\t             ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░▒▒▒▒▒█                 
\t\t\t\t\t            █▒░▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒                
\t\t\t\t\t            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒█  █▒▒         
\t\t\t\t\t            ▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒          
\t\t\t\t\t              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█          
\t\t\t\t\t              ▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█           
\t\t\t\t\t                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒░▒█            
\t\t\t\t\t                  ░░█▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░▒              
\t\t\t\t\t                  ░░░    █░░░░░░░░░░░░░░█                
\t\t\t\t\t                   ░░█      ██░░░░░░░▓█                  
\t\t\t\t\t                   ░░░      █▒▒     ▒▒█                  
\t\t\t\t\t                   ░░░░  ▓▒▒▒▒▒▒    █▒▒                  
\t\t\t\t\t                   █▒▒█░░░░░▒▒█    ▓▒▒▒▒▒                
\t\t\t\t\t                         █       ░░░░░░░▒▒░█             
\t\t\t\t\t                                     ░█                  """+Fore.RESET,"Farfetch'd", "Normal", "Pato", "Primera", "Zona 1", "Pradera", "Bayas y semillas", "Fuga"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                                       ▒                 
\t\t\t\t\t                                     █▒█                 
\t\t\t\t\t                                     ▒▒                  
\t\t\t\t\t                                    ░▒█                  
\t\t\t\t\t                              █▒██▒▒▒▒                   
\t\t\t\t\t                      ██      ▒▒▒▒▒▒█▒▒                  
\t\t\t\t\t           ░░░█     ▒▒▒▒▒▒▒   ▒▒▓▓▓▓▒▒                   
\t\t\t\t\t               ▒▒░░░█▒█▒▒▒▒▒   ▒▓▓▓▓▓█                   
\t\t\t\t\t                   ▒▒▒▓▓▓▓▓      ▒█                      
\t\t\t\t\t                    █▓▒▓▓▒       ▓█                      
\t\t\t\t\t                        █       ▒█                       
\t\t\t\t\t                        ▒█  ▓█  █                        
\t\t\t\t\t                         ██▒▒▒▒█▓▓▓                      
\t\t\t\t\t                       ▓▒▒▒▒▒▒▒▒▒▒▒▒▒                    
\t\t\t\t\t                       ▒▒▒▒▒▒▒▒▒▒▓▒▒▒█                   
\t\t\t\t\t                       ▒▒▒▒▒▒▒▒▒▒▓▓▓▒                    
\t\t\t\t\t                       █▒▒▒▒▒▒▒▒▓▓▓▓▓                    
\t\t\t\t\t                        ▓▒▒▒▒▓▓▓▓▓▓▓                     
\t\t\t\t\t                           █▓▓▓▓▓ ▒▒                     
\t\t\t\t\t                               ▒  ▒░▒                    
\t\t\t\t\t                             ▓░░▒░▓                      
\t\t\t\t\t                            ░█ ░█                        
\t\t\t\t\t                           ░  ▒▒▒                        
\t\t\t\t\t                            █▒▒▒                         
\t\t\t\t\t                        ▒▒▒█ ░▒                       
\t\t\t\t\t                           ░▒                            """+Fore.RESET,"Doduo", "Normal", "Ave", "Primera", "Zona 1", "Pradera", "Bayas y semillas", "Fuga"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                 ██              █                       
\t\t\t\t\t                   ▓█         █  ██                      
\t\t\t\t\t                    ▓░       ██▓█ ▓█                     
\t\t\t\t\t                     ▓░█▒▒░▒▒███▓█▓▓                     
\t\t\t\t\t                      ▓█░▒▒▒▒▒▒█ ▓▓▓▓█                   
\t\t\t\t\t                     ▓▒█▓▒▒▒▒▒▒ ▓█▓▓█  █                 
\t\t\t\t\t                   █████▒▒▒▒▒▒ ▒▒▒▒▒▒▒                   
\t\t\t\t\t          █▒░░ ▓▒▒█▒▓▓█   ▒   ▒▒▒░░░▒░                   
\t\t\t\t\t              ▓▒▒▒▒▓▓▓▓  █▒   █▒▒▒▒▓▓▓▓▓▒▒░░░░           
\t\t\t\t\t             ██▒▓▓▓▓▓▓   █░     █▒▒▒▒                    
\t\t\t\t\t              ▒   █ █▒    ░     ▒                        
\t\t\t\t\t             ░       █░   ░█   ░▒                        
\t\t\t\t\t                      █░  █▒▓▒▒░▒▒▒                      
\t\t\t\t\t                        ▒▒▒▒▒▒▒█▓▒▒▒                     
\t\t\t\t\t                        █▒▒▒▒▒▒▒▒▒▒▒█                    
\t\t\t\t\t                        ▓▒▒▒▒▒▒▒▒▒▒▒█                    
\t\t\t\t\t                         ▒▓▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒█             
\t\t\t\t\t                          ▓▓██▓▓▓▓▓█▒▒▒▓▒▒▒▒▒▒▒          
\t\t\t\t\t                            ▓▓▓▓▓▓▓▒▒▒▒▒▒░▒░░░░░░        
\t\t\t\t\t                             ▒▒  ▓▓ ▒▒▒░░░░░░█           
\t\t\t\t\t                             ▒▒   █▒                     
\t\t\t\t\t                            ░      ░                     
\t\t\t\t\t                           ░      ░█                     
\t\t\t\t\t                         ▓░      █░                      
\t\t\t\t\t                    ░▓░░░░░░    █░▓                      
\t\t\t\t\t                   █   █▒    █░▒░░░                      
\t\t\t\t\t                               ░  ░                      """+Fore.RESET,"Dodrio", "Normal", "Ave", "Primera", "Zona 1", "Pradera", "Bayas y semillas", "Fuga"),
            Pokemon(Fore.WHITE+"""\t\t\t\t\t                           █░░░           ▒░░░░░░█       
\t\t\t\t\t                         ░░░░░░░░░     ▓░░░░░░░░░░░░▒    
\t\t\t\t\t                       █░░░░░░░░░░░▓ █░░░░░░░░░░░░░░░░   
\t\t\t\t\t                       ░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░▓  
\t\t\t\t\t                      █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█  
\t\t\t\t\t                       ░░░░░░███░░░░░░░▓   ▓░░░░░▒░░░░   
\t\t\t\t\t                       ▓░░▓      █░░░░▓      █░░░░▒██    
\t\t\t\t\t                                 ▓░░░░░        ░░░       
\t\t\t\t\t                                █░░░░░░█                 
\t\t\t\t\t                               ░░░░░░░░░█                
\t\t\t\t\t                             ░░░░░░░░░░░░░               
\t\t\t\t\t                          █░░░░░░░░░░░░░░░░              
\t\t\t\t\t                        ░░░░░░░░░░░░░░░░░░░░             
\t\t\t\t\t                     █▒░░░░░░░░░░░░░░░░░░░░░░            
\t\t\t\t\t                    █░░░░░░░░░░░░░░░░░░░░░░░░█           
\t\t\t\t\t                    ░▓░░░░░▓░░░░░░░░░░░░░░░░░▓           
\t\t\t\t\t                 █░░░░░░░░░░░░░░░░░░░░░░░░░░░░           
\t\t\t\t\t                ░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▓           
\t\t\t\t\t              █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░            
\t\t\t\t\t        █████░░░██░░░░░░░░██░░░░░░░░░░░░░░░░█            
\t\t\t\t\t    █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░█             
\t\t\t\t\t   ░█░░░░░░░▓░░░░░░█▓█▒░░░░░░░▒░░░░▒░░░░░░░░░░░░░░░░░█   
\t\t\t\t\t █░░░░░░░░░░░░░░░░░░░░░░░░░▓░░░░░░░░░░░░░░░░░░░░░░░░░██  
\t\t\t\t\t  ▓░░░░█     ▓░░▒█▒▒▓▒▒░░░▒░░░░░░░░░░█░░░░░░░░░░░░░░░░░  
\t\t\t\t\t               █░░░░░░░░▒▒░░░░░█         ░░░░░░░░░░░░░█  
\t\t\t\t\t                  █░░░░▓                     ░░░░░░█     """+Fore.RESET,"Seel", "Agua", "Foca", "Primera", "Zona 2", "Mar", "Peces y algas", "Gordura"),
            Pokemon(Fore.WHITE+"""\t\t\t\t\t                                  ░░                     
\t\t\t\t\t                                 ░░░░                    
\t\t\t\t\t                              █░░░░░░░░                  
\t\t\t\t\t                              ░░░░░░░░░░                 
\t\t\t\t\t                  ░░         █░░░░░░░▒░░░░               
\t\t\t\t\t           █░░░░█░░░         ░░░░░░░░░░█░░░█             
\t\t\t\t\t        █░░░░░░░░░░░░░       ░░░░░░░░░░░░░░░░▓           
\t\t\t\t\t       █░░░░░░░░░░░░░░░       ░░░░█▒░░░░░░█░░░░░█        
\t\t\t\t\t     ░██░░░░░░░░░░░░░░░░      ░░░░░░░▒░░░      █░░▓      
\t\t\t\t\t    ░░░░▓▓░░░░░█▒█░░░░░░░     ░░░░█░░░          ▒░░░     
\t\t\t\t\t    ▓░░░░░░░░░█▓██░░░░░░░       █░░░             ░░░░    
\t\t\t\t\t    █▓░░░░░░░░░░░░░░░░░░░░        ░              ░░░░░   
\t\t\t\t\t       ░░░░█░░░░░░░░░░░░░░░                     ░░░░░░█  
\t\t\t\t\t         ▓░░░░░░░░░░░░░░░░░░▓                 █░░░░░░░░  
\t\t\t\t\t   █░    █░░░░░░░░░░░░░░░░░░░░░█            ░░░░░░░░░░░  
\t\t\t\t\t    ░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█  
\t\t\t\t\t  ▓░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   
\t\t\t\t\t  █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒   
\t\t\t\t\t     ░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░    
\t\t\t\t\t     █░░█░█░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░     
\t\t\t\t\t           ░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░█      
\t\t\t\t\t            █░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░        
\t\t\t\t\t              ░░░░░░░░░░░░░░█░░░░░░░░░░░░▒░░░░░          
\t\t\t\t\t                ░░░░░░░░░░█░░░░░░░░░░░░░░░░░             
\t\t\t\t\t                   ░░░░░░░░░░░░░░░░░░░░░░                
\t\t\t\t\t                       █░░░░░█░░░░░░░░░░░                
\t\t\t\t\t                               █░░░░░░░                  
\t\t\t\t\t                                  ░░░░                   """+Fore.RESET,"Dewgong", "Agua", "Foca", "Primera", "Zona 2", "Mar", "Peces y algas", "Gordura"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t                      ▓░░░░░░▒▓                          
\t\t\t\t\t                   ░░░░░░░░░░▓▒▒▒█                       
\t\t\t\t\t                 ░░▒▒▒▒▒▒▒░░░░▓▓▓▓▒                      
\t\t\t\t\t                ░░█▒▒▒▒▓▓▓░░░█▒▒▒▒▒▒                     
\t\t\t\t\t                ▒░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒                    
\t\t\t\t\t                 ▒▒▒▒▓▓▓▓████▒▓▒▒▒▒▒▒▒                   
\t\t\t\t\t                    █████████▒▒▒▒▒▒▒▒▒▒█                 
\t\t\t\t\t                   █████▓▓▓▓░▒▒▒▒▒▒▒▒▒▒▓▓▓               
\t\t\t\t\t               █▓▓▒░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒              
\t\t\t\t\t             ▓▒▒▒█░█▒▒▒▒▒▒▒░▒█▓▓▓▓▓▓▓▒▒▒▒▒▒              
\t\t\t\t\t   █▒▒▒▒▓▒▒▓▓▒▒▒▓▒░█▒▒▒▒▒▒░▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒              
\t\t\t\t\t  ░▒▒▒▒▒▒▒▓▒▒▒▓▒▒▒▒░░░░░▒▒▒▒▓▓▓▓▓▓▒▒▒▓▓▓▒▒▒▒▓▓▒█         
\t\t\t\t\t   ▒▒▒▒▒▒▒▒▒▓▒▒▓▒▒▒▒▒▓░▒▒▓▒░░░▒██▓░░▒▓▒▒▓█▓▒▒▒▒▒▓        
\t\t\t\t\t ░░▒▒▒▒░░░▒▒▒▓█ █▓▓▒▒▒▒▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒█▒▒▒▒▓▓▒        
\t\t\t\t\t ▒▒▒▓▒▒▒▓▓▒▒▓  ░░▒▒▒▓▓▓▓▓▓▒█▒▒▒▒▒▒▒▓▓▒▒▓▒▓▒▓▓▓▒▒▒▒       
\t\t\t\t\t               ▒░░▒▒▒▒▒▒▒░░▒▒▒░░░░▒▒▓▒▒▓█▒▒▒▒▒▒▒▒▒▒▒▒▒   
\t\t\t\t\t               ▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒█▒▒▓▒▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓█ 
\t\t\t\t\t             █░▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▓█▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒ 
\t\t\t\t\t             ▒▒▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███   
\t\t\t\t\t               █  █▒▒▒▒▒▒▒▒▒▒██▓▒▒▒▒▒▒▒▒▒█  █▒▒▒▓        """+Fore.RESET,"Grimer", "Veneno", "Baba", "Primera", "Zona 2", "Cementerio", "Desechos", "Hedor"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t                      ░░░░░░▒▒▒▒█                        
\t\t\t\t\t                   █░░░▓░░▒▒▒▒▒▒▓▓▓▓                     
\t\t\t\t\t                  ▒▒▓▒▒▒▓▓▓████▓▓▓▓▓▓█                   
\t\t\t\t\t                ▒▒▒▒▒██▒▓█████████▓▓█                    
\t\t\t\t\t             █▓▓▓▓▓▒████████████▓█▓                      
\t\t\t\t\t           ▒░▒▒▒▒▒▒▒████████████▓                        
\t\t\t\t\t          █▓▒▒▓▓▒▒▒▓▓▓▒▒█▒▒▓████▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▓        
\t\t\t\t\t       █▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▓▒▒███▓█▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓      
\t\t\t\t\t     ░░▒▓▓▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ █▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓  
\t\t\t\t\t    ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▓▓▒▒▒▓▓▓       ▒░▒▒▒▒▒▒▒▒▒▒  
\t\t\t\t\t   ▒▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▒▒▓▓▓▓▓█▓▓▓▓▓▓▓▓▓█              ▓▒░▒  
\t\t\t\t\t  ▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒                   
\t\t\t\t\t   ▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓                     
\t\t\t\t\t    ▒▒▒▒▒▒▒██▓▓▓▓█     █▒▒▒▒▒▒▒▓▓                        """+Fore.RESET,"Muk", "Veneno", "Lodo", "Primera", "Zona 2", "Cementerio", "Desechos", "Hedor"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t                                 █▒▒▒▒▓▓▓█               
\t\t\t\t\t                                ▒▒▓▓▓▓▓▓▓▓▓▓█   ▒▒▒      
\t\t\t\t\t                          ██▓▓▒▓██▓▓▓▓▓▓▓█▓▓▓▓▒▒▒▒▒      
\t\t\t\t\t   ░▒▒▒             █░░▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓▓▓▒▒▒▒▒       
\t\t\t\t\t   █▒▒▒▒▒█      █░░░░░▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒█▒▒▒▒▒▒        
\t\t\t\t\t    █▒▒▒▒▒▒▒▓█▒▒░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▓▒▒▒▒▒▒▒██▒▒     
\t\t\t\t\t      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓█     
\t\t\t\t\t       ▒▒▒█▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▓█       
\t\t\t\t\t       ▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t      ▒█▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓         
\t\t\t\t\t    █▒▓▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓█        
\t\t\t\t\t   █▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓█        
\t\t\t\t\t   ▒▒▓▒▒▒▒▒▒████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓▓▓▓        
\t\t\t\t\t  ▒▒▒▒▒▒▒██░░░██████████████░░░░▒▒▒▒▒▒▒▒▒██▓█▓▓▓██       
\t\t\t\t\t  ░░▒▒▒  █░░░░░▒████████████░░░░░░░▓▒▒▒████▓█▒▒▒▓▓▓█     
\t\t\t\t\t  ▒▒▒█   █░░░░░░████████████░░░░░░░░░░██████▓▒▒█▓▓▒▒▒▓   
\t\t\t\t\t   █     ██░░░░░████████████░░░░░░░░░███████▓▓▓▓▓▓▒▒▒▒▒  
\t\t\t\t\t         ▓██ ░░ ██████████████  ░░ ▓████████▓█           
\t\t\t\t\t        ▒███▓██████▒▒▒▒▒▒▒███████████████████▒           
\t\t\t\t\t      █▒███████▓██▒░░▓░░░▒▒▒██████████████▓▓▓▒█          
\t\t\t\t\t      █▒███▓█▓▓▓▒▒▒░░░░░░░░▓██████▓████████▓▓█▒█         
\t\t\t\t\t       █▒▒█  ▓▓▒▒▒▒░▒▒▒▒▒▒▒█████▓▓█▓▓▒▒▓████▓▒▒          
\t\t\t\t\t              █░░░░░░░░▒▒▒▒█▓▓▓▓▓█     █▓▒▒▒▒█           
\t\t\t\t\t              ░░░░░░░▒▒▒▒░░█                             
\t\t\t\t\t              ▒░░░░░░░▒▒▒▒░▒                             
\t\t\t\t\t              ▒▒░░░░░░░░▒▒▒▒                             
\t\t\t\t\t               ▒▒▒▒▒▒░░░░░▒█                             
\t\t\t\t\t                 █▒▒▒▒▒▒▒█                               """+Fore.RESET,"Shellder", "Agua", "Bivalvo", "Primera", "Zona 2", "Mar", "Algas", "Concha"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t                                                  ▓▒▒▓   
\t\t\t\t\t                                              █▒▒▒▒▒▒    
\t\t\t\t\t                                          █▒▒▒▒▒▒▒▒█     
\t\t\t\t\t                                       █▒▒▒▒▒▒▒▒▒█       
\t\t\t\t\t                 ██▒   ▒░▒▒▓█        █▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t ▒▒▒▒▒██        █░▓▓▓▓▓█░▓▒▒▒▒▓      █▒▒▒▒▒▒▒▒           
\t\t\t\t\t  █▒▒▒▒▒▒▒▒▒▒█▓██░▓▓▓▓▓▓▒░▓▒▒▒▒▒█   ▓▓▓▒▒▒▒▒█            
\t\t\t\t\t    █▒▒▒▒▒▒▓▓▓▓█░░░▒█▓▓▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▓                 
\t\t\t\t\t       ▒▒▒▓▓▓▓▓▓░▒▒▒░▒▒▒█▒█▓▒▒▒█▒▒▒▒▓▓▒█                 
\t\t\t\t\t         ▒▒▓█▓▓▒▒▓▓▓▒▒▒▒▒▒▓▒▓▓▓█▒▒▒▒▒▒▓▒▒                
\t\t\t\t\t             ░░▓▓▓▓▓██▒▒▒▓▓▓░█▓▓█░▒▒▒▒▒▒▒▒▒█▒▓█          
\t\t\t\t\t            ░▒▓▓▓▓▓▓▒▓██▒▒▓▓▓█▒██░▒▒▒▒▒▒▒▓▓▒▓▓▓█         
\t\t\t\t\t            ▒█▓▓▓▓█▒██▒▒▒▒▒▓▓▓██▒░▒▒▒█▒▒▓▒▒▒▒█▓█         
\t\t\t\t\t           ▒▒▒▓▓▓▓▒▓█▒▒▒▒▒▒▓▓▓█░▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓█         
\t\t\t\t\t           ██▒█▓█░▓▓▒▓▒▓▓▓▓▓▓░░░▒▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 
\t\t\t\t\t            █▒█▓▒▒▓█░░▒▓▓▓▓█░░░░░█▓▓▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 
\t\t\t\t\t            ▒░▓▓█░▓▓▓░▒▓▓▓▓██████▒▓▓▒▒▒▒▒▒▓▒▒▒▒▒██       
\t\t\t\t\t         █▓▓░█▓▓▓▓▒████▓███▒░░░███▒▓▒▒▒▒▒▒▒▒▒▓▓▓▒█       
\t\t\t\t\t       ▒▒▓▓▓▒▓▓▓▓▓▓▒███████████████░░▒▒▒▒▒▒▓▒▓█▓▓        
\t\t\t\t\t            ▓▒▓▓▓▓▓█▒▓▓███████████▒▒▒▒▒▒▒▒▓▒▓▒▓█         
\t\t\t\t\t             █▒▒▓▓▓█░▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▒▒▒▒▒▒█▒█▓▓          
\t\t\t\t\t               █▓▒▒▓▓▒▒▓▓▓▓▓██▓░▓▓▓▒▒▒▒▒▒▒▒█▓▓▓          
\t\t\t\t\t               ▒▓▓░█▓▓▓▓▒█▓▓▓▓█▓▓▓▒▒▒▒▓▒█▓██▓            
\t\t\t\t\t                ▓▓█░▓▓▓▓▓▒█▓▓▓▒▓▓░█▒▒▒▒▒▓▒▒              
\t\t\t\t\t                   █▒▒▓▓▓▓▓▓▓▓▓░█▒▒▒▒▒▒▓▓▒▒▒█            
\t\t\t\t\t                  ▓▓▓▓█▒▒▓▓▓▓▓█░█▒▒▒▒▒█  █▒▓▒▒▒          
\t\t\t\t\t                 ▒▓▓█   ▒░▓▓▓▓█▒▒▒▒▒▓█      █▒▒          
\t\t\t\t\t                         █▒▒▓  █▒▒█                      """+Fore.RESET,"Cloyster", "Agua", "Bivalvo", "Primera", "Zona 2", "Mar", "Algas", "Concha"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t                       ▒▒                                
\t\t\t\t\t                      ▒▒▒                                
\t\t\t\t\t                                                         
\t\t\t\t\t                 ▒▒   ▒▒▒▒        ▒      ▒▒▒             
\t\t\t\t\t               ▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒▒  ▒▒▒▒▒            
\t\t\t\t\t             ▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t             ▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t           ▒▒▒▒▒▒▓█▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▒▒▒   ▒▒             
\t\t\t\t\t   ▒▒     ▒▒▒▒█▓▓▓▓▓▓▓▓▓█████▓▓▓▓▓▓▓▓▓▓     ▒            
\t\t\t\t\t         ▒▒▒█▓▓▓▓█▓▓▓▓▓████████▓▓▓▓█▓▓▓▓▓▒▒▒▒▒           
\t\t\t\t\t     ▒▒▒█▒█▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒    ▒▒   
\t\t\t\t\t    ▒▒▒░░█▓▓████████████████████████▓▓▒▒▒▒▒▒▒▒▒▓   ▒▒    
\t\t\t\t\t    ▒▒█░░░███████████████████████░███▓▓▒▓▓▒▒▒▒▓    ▒▒▒▒  
\t\t\t\t\t     ▒░░░░▒███████████████████░░░░░███▓▓▓▓▓▓▓            
\t\t\t\t\t      ░░░░░░███████████████░░░░░░░░████▓▓▒▒▒▒   ▒▒▒▒     
\t\t\t\t\t       ░░░░░░████████████░░░░░░░░░░█▓██▓▓▒▒▒▒▒  ▒▒▒▒▒    
\t\t\t\t\t      █░░░░░█░█▒██▒███░░░░░░░░░░░░░█▓██▓▒▒▒▒▒▒▒▒▒▒▒▒▒    
\t\t\t\t\t      ▒░░░░░░░██████░░░▓░░░░░░░░░░░████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒   
\t\t\t\t\t     ▒▒█░░░░░░██████░░░░░░░░░░░░░░████▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒   
\t\t\t\t\t     ▒▒▒▒░░░░███████▒░░░░░░░░░░░░████▓█▒▒▒▒▒▒▒▒▒▒▒ ▒     
\t\t\t\t\t      ▒▒▒▒▒▓███████████░░░░░░░░█████▓█▒▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t         ▒░▒▒█████████████████████▓▓▒▓▓▓▒▒▒▒▒ ▒▒         
\t\t\t\t\t         ▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▓░████▓▓▓▓▓▒▒▒▓▓▓▓▒              
\t\t\t\t\t          ▒▒  ▓▓█▓█▒▒▒▒█████▓▓▓█▒▒▒▒▒▒▒▓▒▒▒              
\t\t\t\t\t               ▒▒▒▒▓▓█████▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒ ▒▒▒          
\t\t\t\t\t               ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▓▓▓▓     ▒           
\t\t\t\t\t                 ▒▒▒▒▒▒▒  ▓▓▓▓▓      ▓▓   ▒              
\t\t\t\t\t                   ▒                                     """+Fore.RESET,"Gastly", "Fantasma", "Gas", "Primera", "Zona 2", "Cementerio", "Almas", "Levitación"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t                       ▒▒                                
\t\t\t\t\t                      █▒▒█                               
\t\t\t\t\t                      ▒▒▒▒█                              
\t\t\t\t\t                     █▒▒▒▓▓█                             
\t\t\t\t\t                     ▒▒▒▓▓▓▓▓█████               ████▓▒▒█
\t\t\t\t\t                    █▒▒▒▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓█  
\t\t\t\t\t                    ▒▒▒▒▓▓▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓     
\t\t\t\t\t                █▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓█       
\t\t\t\t\t                 ▓▓▓▒▒▓▓▓▓▓▓▓▒▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓█         
\t\t\t\t\t               █▓█ █▒▒▒▒▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓            
\t\t\t\t\t                █▓ █▒▒▒▒▒▒▒▒▒▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ 
\t\t\t\t\t    █▓▓▓▓▓▓▓▓█   ▓▓░▒▒▒▒▒▒▓█░░    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     
\t\t\t\t\t  █▓▓▓▓▓▓█▓▓▓▓▓  █▓▓▓▓▓▓▓▓░      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        
\t\t\t\t\t  ▓▓▓▓▓▓▓▓▓▓▓▓█    ▓ ▓▓▓▓▓▓▓▓▓▓▓▓█▒█▓▓▓▓▓▓▓▓▓▓           
\t\t\t\t\t▓▓█▓███▒▒▒▓         ▓▒▒▒█▒▒▒▒▒▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓█        
\t\t\t\t\t ▓▓▓   ▓▓█           ▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓█           
\t\t\t\t\t                      █▓▓▓██▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓              
\t\t\t\t\t                         ▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓             
\t\t\t\t\t                            ▒▒▓▓▓▒▒▓▓▓█▓▓▓▓▓             
\t\t\t\t\t                          ▓▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓             
\t\t\t\t\t                         ▓▓▓▓▓▓▒▒▓▓▓▓▓▓█▓▓▓▓▓            
\t\t\t\t\t                        █▓█  ▓▒▓▓▓█▓▓▒▒▒   █▓▓█          
\t\t\t\t\t                        ██  █▓▓▓█  █▓▒▓█                 
\t\t\t\t\t                             ▓▓    ▓▓▓█                  
\t\t\t\t\t                             ██    █▓█                   """+Fore.RESET,"Haunter", "Fantasma", "Gas", "Primera", "Zona 2", "Cementerio", "Almas", "Levitación"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t              █                                          
\t\t\t\t\t              ▒▒▒                                        
\t\t\t\t\t              ▒▒▒▒▒                                      
\t\t\t\t\t              ▒▒▒▒▒▒▒                                    
\t\t\t\t\t              ▓▒▒▒▒▒▒▒▒  ▓  █    █▓▓▒█                   
\t\t\t\t\t              █▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓█                    
\t\t\t\t\t       ▒▒█     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓                  
\t\t\t\t\t      ▒▒▒▒▒▒█  ▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   
\t\t\t\t\t     █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     
\t\t\t\t\t        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t        █▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓         
\t\t\t\t\t          ▓▓▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█           
\t\t\t\t\t          ▒▒▒▒▒▒▒█░░▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒█             
\t\t\t\t\t         █▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒██             
\t\t\t\t\t         ▒▒▒▒▓▓ ▓▒▒▒▒█▓▒▒▒▒▒▒██░░▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█     
\t\t\t\t\t         ▒▒▒▒▓▓ ░░▓▓▓▓▒▒▒▒▒▒█░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█    
\t\t\t\t\t         ▒▒▒▓▓▓█░░░░░▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▒▓▒▒▓▓▓▓▒▒▒▒▓ ██     
\t\t\t\t\t         ▓▒▒▓▓▓▓▓░░░█░░░░░░░░▒▒█░░▓▓▓▓▓▓▓▓▓▓▓            
\t\t\t\t\t        █▓▓▓▓▓▓▓▓▓▓░░░░░░░▓░░░░░░▓▓▓▓▓▓▓█                
\t\t\t\t\t        ▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓▓▓█                 
\t\t\t\t\t       █▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█                  
\t\t\t\t\t        ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                   
\t\t\t\t\t         █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓█                   
\t\t\t\t\t           ▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓█                   
\t\t\t\t\t                    █▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓█                   
\t\t\t\t\t                      ▓▓█   ▓▓████▒▒▓                    
\t\t\t\t\t                             ▒▓▓▓▓▓█                     
\t\t\t\t\t                              ▓▓█                        """+Fore.RESET,"Gengar", "Fantasma", "Sombra", "Primera", "Zona 2", "Cementerio", "Almas", "Levitación"),
            Pokemon(Fore.LIGHTBLACK_EX+"""\t\t\t\t\t             ▒            █░▒▒▒▒░                        
\t\t\t\t\t            █▒         █░░▒░▒▒▓▒▒▒▒▒▒▓                   
\t\t\t\t\t            █▒█     █  ▒░░░░▒▒▒▒▒▒▒▒▒▒▒█▒▓▒▒▒▒█          
\t\t\t\t\t            █▒▒  ▒░░░░▒▒▒▒░█▓▓█▒▒▒▒▒█▒▓▓▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t            ▓▒▒█▓░░▒▒▒▒░░▒▒▒▒▓▓▓▒▒▓▓▓▒▒▓▒▒▒▒▒▒▒▒█▓       
\t\t\t\t\t            ▒▒▒▒▒▓▓▒░█▒░▓▒▒▒▓▓▓▓▓▓▓█▓▓▓▓▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t            ░▒▒▒▒▓█▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒▒█       
\t\t\t\t\t          ░▒░▒▒▒▒▒▒▒▓▒▒▒▒▒▒░▓▓      █▒▓▓▓▓▓▓▓▓▒▓▓█       
\t\t\t\t\t         ░▒▒░▓▒▒▒▓▒▓▒▒▒▒▒▒▓▓▒         █▓▓▓▓▓▓▓▓▓▓▓▓      
\t\t\t\t\t        ▒░░░▓▒▒▒▒▒▒▒▒▒▒█▓▓▓              ▓▒█▓▓▓▓▓▓▓█     
\t\t\t\t\t       █▒░▒▒▒▒▒▒▒▒▓▒▒▒▒██                ▓▓▓▓▓▓▓▓▓▓      
\t\t\t\t\t        ▓▓▒░▒▒▒▓░█▒▓▒▒▒█                  █▓▓▓▓▓▓▓       
\t\t\t\t\t        ░░▒░▒▒▒▒▒▒▒▒▒▒▒                   ▓▒▓▓█▓▓▓█      
\t\t\t\t\t       █▒▒░░▒▒▒░▒▒▓▓▓                   █▒▒▒▓▓▓▓█▓▓█     
\t\t\t\t\t        ▒▒░░▒▒▒░▒█▓█                   ▒▒▓▓▓▓▓▓▓▓▓▓      
\t\t\t\t\t         █▒▓▒▒▒▓▓▓▓                 ▒▒█▓▓▓▓█▓▓▓▓▓█       
\t\t\t\t\t           █▒▒▒▓█                 █▒▓▓██▓▓█▓▓▓           
\t\t\t\t\t                               █▒▒█▓▓▓▓▓▓▓▓▓▓            
\t\t\t\t\t                               ▓▒▓██▓▓▓▓▓▓               
\t\t\t\t\t                             █▒▓▓▓▓▓▓▓█                  
\t\t\t\t\t                             █▓▓▓▓▓▓▓                    
\t\t\t\t\t                            █▓█▓▓▓▓█                     
\t\t\t\t\t                              █▓▓▓▓                      
\t\t\t\t\t                                 ██▓█▒▒▒█▓▓█             
\t\t\t\t\t                                    ███▓▒██              """+Fore.RESET,"Onix", "Roca", "Serpiente", "Primera", "Zona 2", "Montaña", "Minerales", "Cabeza de roca"),
            Pokemon(Fore.YELLOW+"""\t\t\t\t\t               ░                                         
\t\t\t\t\t            ░▒▒█            █░░░░█                       
\t\t\t\t\t           ░░▒▒▒░█      ░░░░░░░░░█░█                     
\t\t\t\t\t           ░░░▒░░█░▒█░░░▓░░░░░░░░░░░░                    
\t\t\t\t\t           ░░░░░░▒▒▓▒▒▒░█░░░░░░░░░░░░░                   
\t\t\t\t\t           ░░░░░░░░░░░░░░░░▒▓▓▓░░░░░░▒                   
\t\t\t\t\t           ░░░░░░░▓░░░░░░▓▓▓▓▓▓▓█▒▒░░█                   
\t\t\t\t\t           ░░░░░░░░▒░░░░░░░▓▒▒▒▒▒█        █░░░░░         
\t\t\t\t\t           █░░░░░░░░░░░░░░░░░▒▒▒▒░     ░░░░░░░░▒█        
\t\t\t\t\t            ░░░░░░░░░░░░▒▒▒░░░░░▒▒▒▒░░░░░░░▒▒▒           
\t\t\t\t\t             ░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒            
\t\t\t\t\t             █░░░░░▒░░░░░░░░▒▒▒▒▒░░░░░░░░░░              
\t\t\t\t\t              ░░░░░█░░░░░░░░░░░░░░░░░░█░░                
\t\t\t\t\t              ░░░░▒▒░░░░░░░░░░░░░░░░░░░░                 
\t\t\t\t\t              ░░░░░░░░░░░░░░░░░░░░░░░░░░░                
\t\t\t\t\t              ░░░░█▓░░░░░░░▓▓▒░░░░▓▓▓░░░█                
\t\t\t\t\t             █░░▒▒▒▓▓▓▒░░▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓█               
\t\t\t\t\t             ▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█             
\t\t\t\t\t            █▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█            
\t\t\t\t\t            ▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
\t\t\t\t\t           █▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█           
\t\t\t\t\t           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█           
\t\t\t\t\t           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓            
\t\t\t\t\t           █▓▓▓▓▓▓▓▓▓▓▓▓           ▓▓▓▓▓▓▓▓▓█            
\t\t\t\t\t            ▓▓▓▓▓▓▓▓▓▓              █▓▓▓▓▓▓▓             
\t\t\t\t\t            █▓▓▓▓▓▓█                    █▓▓░░█           
\t\t\t\t\t            ▓░░░░▒█▓                        █▒           
\t\t\t\t\t             ▒▒▒▒█                                       """+Fore.RESET,"Drowzee", "Psíquico", "Hipopótamo", "Primera", "Zona 2", "Río", "Frutas", "Insomnio"),
            Pokemon(Fore.YELLOW+"""\t\t\t\t\t                      ░                                  
\t\t\t\t\t                     █░░                                 
\t\t\t\t\t       ▓░░░▒░        ░░░▒          ░░         █          
\t\t\t\t\t       ░▒░░░░░░      ▒░▒▒▒      █░▓▓▒       ▓░░░░░       
\t\t\t\t\t      ░░░░░░░░░     █▒▒░░░░░░░▒░█▓▓██      █░░░░░░░░     
\t\t\t\t\t          ░░░░░     ░░░░░░░░░░░█▓▒▒▒     █░░▒░░▓░░░░░▒   
\t\t\t\t\t          ░░░░░    ░░░░░░░░░░░░░░░▓▒     ░░▒▒▒▒▒▒▒▒░░░   
\t\t\t\t\t          ▒░░░░█   ░░░░░░░░░░░░░░░▒       ░▒█▒█▒▒▓▒█▒    
\t\t\t\t\t          █░░░░░   ░▓░░░░░▓░░░░░▒▒▒██      ▒▒▒▒▒▒▒       
\t\t\t\t\t          █░░░▒▒▒█░░░░░░░░░░░▒▒▒▒▒▒░░░█    ░░░▒▒▒        
\t\t\t\t\t           ░░▒▒▒█░░░░░░░░░░░▒▒▒▒▒▒▒░▒▒▒  █░░░░░░█        
\t\t\t\t\t             █▒▒▒░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒░▒█▒▒▒░░░█▓█         
\t\t\t\t\t                █░░░░░▓░░█▒█▒░░░▒▒▒░░░▒▒▒▒░█▒█▒██        
\t\t\t\t\t                 █░░░░░░░░░░░░░░░░░░░       ▒▒█▒▒        
\t\t\t\t\t                   ░░░░░░░░░░░░░░░░░█         █          
\t\t\t\t\t                     ░██░░░░░░░░▒░▒▒█                    
\t\t\t\t\t                    █░░░░░░░░░░░░░░▒▒                    
\t\t\t\t\t                   █▒▒▒░░░░░░░░░░░▒▒▒                    
\t\t\t\t\t                 ▓░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                 
\t\t\t\t\t               ░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█               
\t\t\t\t\t             ░░░░░░░░░░░▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒              
\t\t\t\t\t             ░░░░░░░░░░█          █▒▒▒▒▒▒▒▒▓             
\t\t\t\t\t            █░░▒▒░░░░            ▒▒▒▒▒▒▒▒▒▒              
\t\t\t\t\t             █▒▒▒▒▒▒▒█           ▒▒▒▒▒▒▒▒█               
\t\t\t\t\t              █▒▒▒▒▒▒▒           █▒▒▒▒▒▒▒▒█              
\t\t\t\t\t              ▒▒▒▒▒▒▒▒█            ▒░░░░░░▒█             
\t\t\t\t\t            ░░░░░░▒░░░█                                  
\t\t\t\t\t            ███░░░▒░░░                                   """+Fore.RESET,"Hypno", "Psíquico", "Hipopótamo", "Primera", "Zona 2", "Río", "Frutas", "Insomnio"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t                                     █░░░▒▒▒▒            
\t\t\t\t\t          ░░░▒▒▒▒▒▒                 ▒▒▒▒▒▒▒▒▒▒█          
\t\t\t\t\t         ▒░░▒▒▒▒▒▒▒▒▓              ▒▒▒▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t        ░░░▒▒▒▒▒▒███▒▒                 ▓▓▓▒▒▒▒▒▒▒        
\t\t\t\t\t      █▒▒▒▒▒▒▒▒▓█                       ▓▓▓▒▒▒▒▒▒▒       
\t\t\t\t\t     █▒▒▒▒▒▒▒▒▓▓█                       █▓▓█▒▒▒▒▒▒▓      
\t\t\t\t\t     ▒▒▒▒▒▒▒▒▒▓▓██             █     █░██▓▓▒▒▒▒▒▒▒▒      
\t\t\t\t\t     █▒▒▒▒▒▒▒█▓▓░░▒     ▒▒    ▒▒     █▒▒▒▒▒▒▒▒▒▒▒▒▒      
\t\t\t\t\t      ▒▒▒▒▒▒▒▒▒▒▒▒      ▒▒▓  █▒▒      ▒▒▒▒▒▒▒▒▒▒▒▒█      
\t\t\t\t\t      ▒▒▒▒▒▒▒▒▒▒▒█   ░░░░▒▒▒▒▒█░░░▓    ▒▒▒▒▓▒▒▒▒▒▓       
\t\t\t\t\t     █░▒▓▒▒▒▒▒▒▒▒ ▒▒█░░░░░▒▒▒▒░░░░░█▒▒  █▒▒▒▒▒█▒░        
\t\t\t\t\t      ░▒▒▒▒▒████ ▒█░▒▒▒▒▒▒▒░▒░░▒▒▒▒░█▒▒    ░░░░░█        
\t\t\t\t\t       ░▒ ▒▒▒   ▓█░░░░░░▒▒▒▒▒▒▓░░░░░░█▒▓█    █░░         
\t\t\t\t\t       ░░▒▒ █░░░░░░░░░░░░░░░░░░░░░░░░░░▓▒▒▒░░░░░█        
\t\t\t\t\t       ░░▓░█▒▓▓█░░░░░░░░░░░░░░░░░░░░░░░░█▒▓ █▒█░█▒       
\t\t\t\t\t      ▒▒█    █▓██▒▒▒▒▒▒░░░░░░░░░▒▒▒▒▒▒▒▓▓▓▓█   █▒▒▒      
\t\t\t\t\t  █  ▒▒▒        ███░░░▒▒▒░░▒▒▒▒█▒░░░░█           ▒▒▒▓▓▓▒ 
\t\t\t\t\t █▒▒▒▒█                                           █▒▒█ ▒ """+Fore.RESET,"Krabby", "Agua", "Cangrejo", "Primera", "Zona 2", "Mar", "Algas", "Huida"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t                                    ░░▒▒▒                
\t\t\t\t\t                                   ░░░░▒▒▒█              
\t\t\t\t\t                                  ░░░░░▒▒▒▒▒█            
\t\t\t\t\t                                 ░░░░▒▒▓▒▒▒▒▒▒▒          
\t\t\t\t\t                                 ░░░▒▒▒▒▒▒▒▒▒▒▒          
\t\t\t\t\t       ░░░░█                  ░  █▒▒▒█▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t     ▒▒▒▒██             ▒    █▒   ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t   ▒▒▒▒▒▓▓▒         ▒▒  ▒▒   ▒▓  ▒░░▒▒▒█████▒▒▒▒▒▒▒      
\t\t\t\t\t   ▒▒▒▒▓▓▓▒          ▒▒██▒▒█▒▓█ ▒▒ ░▒▒▓██████▒▒▒▒▒▒      
\t\t\t\t\t   █▒▒▒█▒▒▒▒      █▒▒ ▒▒▓░▒▒█▒█▓▓▓░ ▓▓███████▒▒▒▒▒█      
\t\t\t\t\t    ▒▒▒▒▒▒▒▒█    █  ▒▒▒▒▒▒▒▒░░░░░▓░░█ ▒███▓▓▓▒▒▒▒▒       
\t\t\t\t\t    ▒▒▒▒▒▒▒▒    █░░░░▒█▒▒▒▒░░▒▒▓▓█░░░█ ▒█▓▓▓▒▒▒▒▒▒░      
\t\t\t\t\t    █▒▒▒▒▒▒     ░░░▒▒▒▒░░░░░░▒░▓█░░░░▒░▒▓▓▓▒▒▒▒▒▒░       
\t\t\t\t\t      ██░░   ▒▓▒░░░░░░░▓██▓▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒         
\t\t\t\t\t         ▓░░░░░░░░░░░░░░░░░░░░░░░░█░░░▒▒▒▒▒▒▒▒░░█        
\t\t\t\t\t       ░▒█ ▒▒ ▒▒▒▓▒░▒░░░░░░░░░░░░░░░░░▒▒█▒▒█▒▒█ ▒▒█      
\t\t\t\t\t    ▒░▒  ▒▒▒      ▓▒░░░░░░░░░░░░░░░█          █▒██▒▒▒    
\t\t\t\t\t░░▒▒▒                                           ▒▒▒▒▒▒▒░▓"""+Fore.RESET,"Kingler", "Agua", "Cangrejo", "Primera", "Zona 2", "Mar", "Algas", "Huida"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t                   █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                    
\t\t\t\t\t               █▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒█                
\t\t\t\t\t            █▒░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒█             
\t\t\t\t\t          █▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█           
\t\t\t\t\t         ▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█         
\t\t\t\t\t       █▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t      █▒▒░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t     █▒▒▒░░░░░░░░░░░░░░░░░░░░▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      
\t\t\t\t\t    █▒▒▒▒▒░░░░░░░░░░░░░░░░░▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█     
\t\t\t\t\t    ▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    
\t\t\t\t\t   █▒▒▒▒▒▒▒▒░░░░░░░░░░░▒▒▒▒▒▒█▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   
\t\t\t\t\t   ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█  
\t\t\t\t\t   ░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  
\t\t\t\t\t   ░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  
\t\t\t\t\t   █░░░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   
\t\t\t\t\t   █░░░░░░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░█▒▒▒▒▓▒▒█▒▒▒▒█    
\t\t\t\t\t    ░░░░░░░░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░▒▒▒▒▒▒▒▒▓░░█    
\t\t\t\t\t    █░░░░░░░░░░░░░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒██░▓░░▓     
\t\t\t\t\t     █░░░░░░░░░░░░░░░░░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▒▒      
\t\t\t\t\t      █░░░░░░░░░░░░░░░░░░░░░░░░░░▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█      
\t\t\t\t\t       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        
\t\t\t\t\t         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒         
\t\t\t\t\t          █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░           
\t\t\t\t\t            █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░             
\t\t\t\t\t               █░░░░░░░░░░░░░░░░░░░░░░░░░█               
\t\t\t\t\t                  ██░░░░░░░░░░░░░░░░░█                   
\t\t\t\t\t                         ██████                          """+Fore.RESET,"Voltorb", "Eléctrico", "Bola", "Primera", "Zona 3", "Ciudad", "Electricidad", "Estática"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t                     █░░░░░░░░░░░░▒██                    
\t\t\t\t\t                 ▒░░░░░░░░░░░░░░░▒▒▒▒▒▒▒█                
\t\t\t\t\t              ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒█             
\t\t\t\t\t            ░░░   ░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒█           
\t\t\t\t\t          ░░░░   ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒█         
\t\t\t\t\t        █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t       █░░░██░░░░░░░░░░░░░░░░░█████░░░░░▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t      █░░░█░░█░░░░░░░░░░░░░░█░░░░░░░░█░▒▒▒▒▒▒▒▒▒▒▒░      
\t\t\t\t\t     █░░░▒░░░░█░░░░░░░░░░░░█░░░░░░░░░░░█▒▒▒▒▒▒▒▒▒▒▒█     
\t\t\t\t\t     ░░░█░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░█▒▒▒▒▒▒▒▒▒▒▒     
\t\t\t\t\t    █░░░░░░░░░░░█░░░░░░░█░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒█    
\t\t\t\t\t    ░░░░░░░░░░░░░█░░░░░█░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒    
\t\t\t\t\t    ░░░░░░░░░░░░░░█░░░█░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒    
\t\t\t\t\t    ░░░░░░░░░█░░░░░░░░░░░░░░░░░░░█░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒    
\t\t\t\t\t    ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒    
\t\t\t\t\t    █▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░█▒▒▓    
\t\t\t\t\t     ▒▒▒▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒     
\t\t\t\t\t     █▒▒▒▒▒▒▒█▒░░░░░░░░░░░░░░░░░░░░░░▒▒██▒▒▒▒▒▒▒▒▒▒█     
\t\t\t\t\t      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      
\t\t\t\t\t       ▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓█▒▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t        ▒▒▒▒▒▒█▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t         █▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒█▒▒▒▒▒▒▒▒▒▒▒█         
\t\t\t\t\t           █▒▒▒▒▒▒▒▒▒▒████████▒▓█▒▒▒▒▒▒▒▒▒▒▒▒▒           
\t\t\t\t\t             █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█             
\t\t\t\t\t                █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                
\t\t\t\t\t                   ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                   """+Fore.RESET,"Electrode", "Eléctrico", "Bola", "Primera", "Zona 3", "Ciudad", "Electricidad", "Estática"),
            Pokemon(Fore.LIGHTMAGENTA_EX+"""\t\t\t\t\t                                      █░░░░░             
\t\t\t\t\t                                    ░░░░░░░░░░█          
\t\t\t\t\t                ▓▓▓█▓             ░░░░░░░░░░░░░░         
\t\t\t\t\t          █░▓▓█░░░█▓░░░    ██    █░░░▒░░░░░░░░█▒█        
\t\t\t\t\t         █░░█░░░░░░░░░░░░░░░░░░░░▓░░░░░░░░░░░░█░▒        
\t\t\t\t\t         ░░░░░░░░░░░░░░░░░░░░░░░░█░█░░░░░░███▒▒█▒        
\t\t\t\t\t         ░░█░░░░░█░░░░░░░█░░░░░░░░░░░▒▒▒▒▒▒█░░░░░█       
\t\t\t\t\t         ▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░░░░░░░░█▒▒▒░░░░░░░░░░░▓    
\t\t\t\t\t      █░░░░░█▒▒▒▒▒▒░░░░░░░░▒▒░░░░░░░░░▒▒░░░░░░░░░░░░░░█  
\t\t\t\t\t    ░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░▒█ 
\t\t\t\t\t  █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░ 
\t\t\t\t\t █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░▓░░█░░▒█░░░░░░▓░░█
\t\t\t\t\t ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░█
\t\t\t\t\t█░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░█░▓░░░░░█░░ 
\t\t\t\t\t█░░░░░░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░░░░░░▒░░░░░█░░░░░░░  
\t\t\t\t\t ▓░░░░░░░░▒▒░░░░░░░░      █░░░░░░░░░░░░░░░░░░░██░░░░░░   
\t\t\t\t\t ▒░░░░░░░░░░░░░░░░░█      █░░█░░░░░░░░░░█░░░░░█░░░░█     
\t\t\t\t\t  █░░░▒░░░░░░░░░░░▓       ░░░░░░░░░░░░░█░░░░░░█          
\t\t\t\t\t    ░░░░░░░░░░░░░         ░░░░░░░░░░░░█░░░░░░░█          
\t\t\t\t\t       █░░░░░░█           █░░░░░░░░░░░░░░░░░░░           
\t\t\t\t\t                           ░░░░░░░░░▒░░░░░░░░            
\t\t\t\t\t                            █░░░░░░░░░░░░░░█             
\t\t\t\t\t                               ░░░░░░░░░░█               """+Fore.RESET,"Exeggcute", "Planta", "Huevo", "Primera", "Zona 1", "Bosque", "Bayas y semillas", "Clorofila"),
            Pokemon(Fore.GREEN+"""\t\t\t\t\t                                  █                      
\t\t\t\t\t                               ▓▒           █▓▒          
\t\t\t\t\t              ▒              █▒▒       █▒▒▒▓             
\t\t\t\t\t               ▓▒█          ▓▒▒      ▒▒▒▒                
\t\t\t\t\t                █▒▒        ▒▒▒█   █▒▒▒▒   █▒▒▒█          
\t\t\t\t\t                 █▒▒▓   █ █▒▒▒   ▒▒▒▒ █▒▒▒▒              
\t\t\t\t\t                   ▒▒▒  █ ▒▒▒  █▒▒▒█▒▒▒▒                 
\t\t\t\t\t     █▒▒▒▒▒▒▒▒▒█    ▒▒▒█▒ ▒▒▒ ▓▒▒▒▒▒▒█                   
\t\t\t\t\t  ██████▒▒▒▒▒▒▒▒▒▒▒█ ▒▒▒██▒▓██▒▒▓▒▒█  █▒▒▒▒▒▒▒▒▒▒▒▒█     
\t\t\t\t\t              █▒▒▒▒▒▒▒▓▓▓▓▓▓█▓▓█▓▓█▒▒▒▒▒▒▒██             
\t\t\t\t\t                  █▒▒▒▒▓▓▓█▓▓▓█▓▓▒▒▒▓█                   
\t\t\t\t\t        █▒▒▒▒▒▒▒▒▒▒▒▓█▓▓▓█▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒          
\t\t\t\t\t     ▒▒▒▒▓██████▓▒▓█▒▓▓▓▓▓▓█▓▓▓▓▓▓▓█        █▓▒▒▒█       
\t\t\t\t\t   █       ▒▒▒▒██▒▓▒▒█▓▓▓▓▓█▓█░░░░░░█            ▒▒      
\t\t\t\t\t        █▒▒█   █▒▒▒▓░░░░░░░▓█░░░░░░░░░                   
\t\t\t\t\t       ▒█        ▒▓░░░░░░░░░░░░░░░░░▒░█                  
\t\t\t\t\t      ▒          ▓░░░░░░█░░░█░░░░░░░░░                   
\t\t\t\t\t                  ░█▒▒▒██░░░▓▒░░░░░░░█                   
\t\t\t\t\t                   ░▒░░░░░░▒▒▒▒▒▒▒▒▒▓                    
\t\t\t\t\t                     █░░█░▒▒▒▒▒▒▒▒▒▒▒▒                   
\t\t\t\t\t                      █░░▒▒▒▒▒▒▒▒▒▓▒▒▒▒                  
\t\t\t\t\t                      ░░░▓▓▒▓▓░▒▒▒▒▒▒▒▒▒                 
\t\t\t\t\t                ░     █░░▒▒▒▒▒▒▒▒▒▒██▓▒▒█░░              
\t\t\t\t\t             █░▒▓░▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒██▒▒             
\t\t\t\t\t              █░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓░░░▒▒█            
\t\t\t\t\t               █▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒░▒▒▒▒█            
\t\t\t\t\t                 ░░░▒▒        ████    █░░░░░             
\t\t\t\t\t                                        █░▓              """+Fore.RESET,"Exeggutor", "Planta", "Coco", "Primera", "Zona 1", "Bosque", "Bayas y semillas", "Clorofila"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                █▒                        ██             
\t\t\t\t\t                ░░░░░█    █▒░░░░░▓█    ░░░░░             
\t\t\t\t\t                 ▒░░░░░░░░░░░░░░░░▓▓░░░░░░░              
\t\t\t\t\t                  █░▒░░░░░░░░░░░░░░░░░░░░▓               
\t\t\t\t\t                   ░░░░░░░░░░░░▒▒▒▒▒░░░░█                
\t\t\t\t\t                  █░░░░░░░░░░░▒▓▓▓▓▒▒░░░░                
\t\t\t\t\t                   ░░░░░░░░░░█▓▓▒▒▒▒▒▒░░░░░█             
\t\t\t\t\t                  █░░░░░░░░░░██▒█░▒▒█▒▒░░░░░░░           
\t\t\t\t\t                  ░░░░░░░░░░░▓▒░█░░▒▒▒▒░░░░░░░           
\t\t\t\t\t                 ░░░░░░░░░░░░▓███░▓▒▒▒█░░░░▒             
\t\t\t\t\t               ░░░░░░░░░░░░░░░█▓▒▒▒▒▒▓▒▒▒▒▒              
\t\t\t\t\t              ░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░▒▒▒               
\t\t\t\t\t              █░░░░░░░██▓▒░░░░░░░░░▒▒█                   
\t\t\t\t\t               ░░░░░░████▒░░░░░▒▒▒▒▒▒▒                   
\t\t\t\t\t               ░░░░░▒██▒▒░░░░░░▓▒▒▒▒▒▒▒▒                 
\t\t\t\t\t                 ▒▒▒▒▒▒█▒▒▒▒▒█▒▒▒▒▒▒▒▒▓▒▒▒█              
\t\t\t\t\t                  █▒▒▓▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒            
\t\t\t\t\t                █▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░▓▒▒▒▒▒▒          
\t\t\t\t\t               ▒▒▒▒▒▒▒▓▒▒░░░░░░░░░░░░░░░░█▒▒▒▒▒▒▒█       
\t\t\t\t\t             ▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░██ ▒▒▒▓▒        
\t\t\t\t\t          █▒▒█▓░░▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░█▒▒ █▒          
\t\t\t\t\t           ▒▒▓░░██▒░░░░▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒            
\t\t\t\t\t           ██░░▒▒▒░░░░░▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒            
\t\t\t\t\t           █░░░▒█▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░▒█▒▒▒▒▒█            
\t\t\t\t\t          ░░░░ ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒             
\t\t\t\t\t      █░░░░░░░  █▒▒▒▒▒▒▒▒█▒▒▒▒██    █▒▒▒▒▒▓▒░█           
\t\t\t\t\t      █░░▒▒░░░█  ▓▒▓▓▒▒                                  
\t\t\t\t\t            ▓░    █░░█                                   """+Fore.RESET,"Cubone", "Tierra", "Solo", "Primera", "Zona 2", "Cementerio", "Bayas y raíces", "Rostro triste"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                 ▓░░░█                                   
\t\t\t\t\t              ░░░░░▒▒▒                                   
\t\t\t\t\t              ▒▒▒▒▒░░▒█                                  
\t\t\t\t\t                   █▒░░▒                                 
\t\t\t\t\t                      ▒▒▒▒                               
\t\t\t\t\t                        █▒▓▓▓█                           
\t\t\t\t\t                        █▓▓▓▓▓▓                          
\t\t\t\t\t           ▓░░▒▒█       ▓▓▓▓▓▓█░░▒                       
\t\t\t\t\t           █▒▒▒░░░░░░░░░░░░░░░░░█▒▒                      
\t\t\t\t\t            ▒░░░░░░░░░░░░░░░░░░ █▒▒▒▒▒▒▒▓                
\t\t\t\t\t           █░░░░░░░░░░░░░░░░░█    █▒▒▒▒▒▒█               
\t\t\t\t\t          █░░░░░░░░░░░░░░▒▒▒▒▒█    ▒▒▒▒                  
\t\t\t\t\t          ░░░░░░░░░░░░▒▒░░░░▒▒      █▒█ ▓▒▒▒▒            
\t\t\t\t\t          ░░░░░░░░░▓▒▒░░░░░░░░       ▓▒▒▒█▓▓▒▒█          
\t\t\t\t\t          ▒░░░░░░░░░█░░░░░░░░▒  █▒▒▒▒▒█▓▓▓██             
\t\t\t\t\t          ░░░░░▒░░░░░░░░░▒▒▓▒▓▒▒▒▒▒▒▒▒░▒                 
\t\t\t\t\t         ░░░░░▒▒░░░░░░░▒▒▒▓▓▓▓▓▓▒▒▓█                     
\t\t\t\t\t        ██░░░▒▒▒▒░▒█▒▒█▒▒▒▓▓▓▓▓▒▓▓▓▓▓                    
\t\t\t\t\t        █░░░▒▒▒▒    ░█░▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒        ▒         
\t\t\t\t\t         █▒▒▒▒      ░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▓▒▒       
\t\t\t\t\t                   ▒▒░░░░░░░░░░░▒█▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓        
\t\t\t\t\t                  ▒▒▒▒░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓          
\t\t\t\t\t                 █▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓             
\t\t\t\t\t                  ▒▒▒▒▓▓█ █▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒              
\t\t\t\t\t                 ░░▒█               ▒▒▒▒▒▒▒█             
\t\t\t\t\t                                      ▒░▒▒██             """+Fore.RESET,"Marowak", "Tierra", "Solo", "Primera", "Zona 2", "Cementerio", "Bayas y raíces", "Cabeza ósea"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t              █▓░▒▒█                                     
\t\t\t\t\t           ▒░░░░░░░▒▒▒▒█                                 
\t\t\t\t\t          ▒░░░░░░░▒▒▒▒▒▒▒                                
\t\t\t\t\t         ▒░░░░░▒▒▒▒▒▒▒▒▒▒▒                        ░  ▓   
\t\t\t\t\t         ▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▓                     █░█▓░░  ▒
\t\t\t\t\t         █▒▒▒▒▒▒▒▒▒▒██░█▒▒█▓█                  ▒░░▒▒▒▒░░ 
\t\t\t\t\t       ▒░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒               █▒▒▒▒▒▒▒▒▒ 
\t\t\t\t\t █░░░░▓▒▒▒▒▒▒▒░░░░░█▒▒▒▒▒▒█▓▓▓▓▓▒         ▓▓░░░░░▒▒▒▒▒▒  
\t\t\t\t\t▓░░▒▒░░▓▓░░░░░░█▒▒▒▒▒▒▒▒▒▒      ▒▒▒░░░░░░░▓░░░░█░█▒▒▒    
\t\t\t\t\t  ████    █▒▒▒▒▒█▒█▒▒▒▒▒▒▒▒▒▒▒░░░░▓░░▒▒▓▒▒▒░█░█░▓▒░░     
\t\t\t\t\t           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓█▒▓              
\t\t\t\t\t            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒         ▒▒                 
\t\t\t\t\t             ▒▒▒▒▒▒▒▒▒▒▒▒█                               
\t\t\t\t\t             █▒▒▒▒▒▒▒▒▒█                                 
\t\t\t\t\t              ▒▒▒▒▒▒▒█                                   
\t\t\t\t\t              ▒▒▒▒▒▒                                     
\t\t\t\t\t               ░░░░█                                     
\t\t\t\t\t              █░▒███                                     
\t\t\t\t\t               ░░░░░                                     
\t\t\t\t\t               ░░░░▒                                     
\t\t\t\t\t               ░░░▒▒                                     
\t\t\t\t\t               ▒▒▒▒▒▒                                    
\t\t\t\t\t                ▒▒▒▒▓█                                   
\t\t\t\t\t                 ▒▒▒▒▒▒                                  
\t\t\t\t\t                █▒▒▒▒▒▒▓░                                
\t\t\t\t\t                ░░▒░░░░▓█                                """+Fore.RESET,"Hitmonlee", "Lucha", "Kickboxer", "Primera", "Zona 3", "Ciudad", "Frutas", "Indefenso"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                                   ▒▒                    
\t\t\t\t\t                              ▓▒▒ ▒▒▒█                   
\t\t\t\t\t         ░░░░░▒▒█             ▒▒▒█▒▒▒  ▒                 
\t\t\t\t\t       ░░░░░░▒▒▒▓▓          ▒▒░░▒░░░█▒▒▒▒                
\t\t\t\t\t       ▒▒▒▒▒▒▒▒▓▓▓          ▒░░░░░░░░░▒▓                 
\t\t\t\t\t       ▒▒▒▒▒█▓░▒▓█    █▒▒▒▓ ▒░░░▒░▒░▒▒▒▒▒▒               
\t\t\t\t\t          █▓▓█▓█▒▒▒▒▒▒▒▒█▒▒▒▒░█░░░░▒▒▒▒▒█                
\t\t\t\t\t                    ▒▒▒▒▒▒▒▒█▒▒▒▒▒█░░███▒▒               
\t\t\t\t\t                       █▓█▒▒▒▒▒▒▒▒▒▓▒░░░░▒▒▒▒            
\t\t\t\t\t                        ▒█▒▒▒▒▒▒▒▒▓▓▒▒░░░▒▒▒▒█           
\t\t\t\t\t                          ░░█░░▒▒▒▒█▓▓▓▒▒▓               
\t\t\t\t\t                          █▒░░░░░░░▒▒▓▓▒█▓               
\t\t\t\t\t                          █▒████▒▒▒▒█ ▒▒▒▒               
\t\t\t\t\t                       ▒▒░░▒▒▒▒▒▒▒▒   █▒▒▒               
\t\t\t\t\t                       ░░░█▒▒▒▒▒░░▒█▒░  █                
\t\t\t\t\t                       ░░▒▒▒██░░░░▒▒▒                    
\t\t\t\t\t                         ▒▒░░░░░▒▒▒▒▒█                   
\t\t\t\t\t                         ▒▒▒▒▒█▒█▒▒                      
\t\t\t\t\t                        █▒▒░░▒▒                          
\t\t\t\t\t                         █▒▒▒▒▒                          
\t\t\t\t\t                           █▒▒▒▒                         
\t\t\t\t\t                            ▒▒▒▒█                        
\t\t\t\t\t                            █▒▒▒▓                        
\t\t\t\t\t                            ▒▒▒▒▓▒                       
\t\t\t\t\t                           █░░▒▒▓▒                       
\t\t\t\t\t                         ▒░░░░░░▒                        
\t\t\t\t\t                        ▒▒▒▒░░░▒                         
\t\t\t\t\t                         █▒▒▒▒                           """+Fore.RESET,"Hitmonchan", "Lucha", "Punchboxer", "Primera", "Zona 3", "Ciudad", "Frutas", "Indefenso"),
            Pokemon(Fore.LIGHTMAGENTA_EX+"""\t\t\t\t\t                  ▓░░░░░░░░░█                            
\t\t\t\t\t               █░░░░░░░░░░░░░░░                          
\t\t\t\t\t              ▒░░░░░░░░░░░▒▓░░░░█                        
\t\t\t\t\t             ██░░░░░░░░░░░█▓░░░░░█        ███            
\t\t\t\t\t            ▓░░░░░░░░░░░░░░░░░░░░▒  █▒▒▒░░░▒▒▒▒▒▒█       
\t\t\t\t\t            ▒▓▓▒▒░░░░▒▒▒▓▓▓▓▓▒▒▒▒▒▓░▒▒▒▒░░░▒▒▒▒▒▒▒▒▓     
\t\t\t\t\t             █▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒█░░░░░░░▒▒▒▒▒▒▒▒▒▒▒    
\t\t\t\t\t        █▒▒▓█  ▓▒▒▒▒▒▒▒▒▒▒▒▒▓█▒▒▒▒▒▒█████▒▒▒▒▒▒▒▒▒▒▒▒▒   
\t\t\t\t\t     ░░░░░░░░░▓░░░▒░░░░░░░▒▒█▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒█▒▒▓  
\t\t\t\t\t   █░░░░░░░░░█░░░█░░░░░░▒▓▒▒▒█░░▒▒░░░░░░░░░░░░░░░▒▒▒▒▒▒  
\t\t\t\t\t   ▒░░░░░░░▒░░░░▒░░░░░░▒▒▒▒░░░░░▒▒▒░░░░░░░░░░░░░░░▒▒▓▒▒█ 
\t\t\t\t\t    █░█▓  ▓░░░░░░░░░░░▓░░░░░░░░▒▒░▒▒▒█▒░░░░░░░░░░░▒▒█▒▒█ 
\t\t\t\t\t        █░░░░░░░░░░░░█░░░░░░░░░▒▒░▒▒▒▒▒▒▒▒▒█░█░░▒█▒▒█▒▒▓ 
\t\t\t\t\t       ░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░▒▒▒▒▓▒▒▒█▒▒▒▒▒▒▒▒▒█ 
\t\t\t\t\t     █░░░░▒░░░░░░░░▒░░░░░░░▓░░█░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒  
\t\t\t\t\t    ░░░░░░░░░░░░░░█░░░░░░░░░█░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▒▒▒  
\t\t\t\t\t   ░░░░░░░░░░░░░░▒░░░░░░▓░░░░░░░░░░▒░░░░░░░▒▒▒▒▒▒▒▒▒▒▒█  
\t\t\t\t\t  ▒░░░░░░░░░░░░░▒░░░░░░░░░░░░░█░░░░░░░░░░░░░▒▒▒▒▒▒█▒▒▒   
\t\t\t\t\t  ░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█▒▒▒▒▒▒▒▒    
\t\t\t\t\t ▒░░░░░░░░░░░░░▒░░░░░░▒░░░░░░░█░░░▒░░█░░░░░░▒▒▒▒▒▒▒▒█    
\t\t\t\t\t ░░░░░░░░░░░░░▒▒▒█▒░░░░░░▒▒▒▒▒▒░▒░▓░█░░░░░░▒▒▒▒█▒▒▒▒     
\t\t\t\t\t █░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▓░░▓░░░█░█░░▒▒▒▒ █▒▒▒▒     
\t\t\t\t\t  ░░░░░░░░░░▒▒▒▒▒▒█▒▒█▒▒▒▒▓▒▒▒▒▒█░░█░░░░▒▒▒▒█   █▒▒▒     
\t\t\t\t\t   █▒░░░░▒▒▒▓▒▒▒▒▒▒▒▒ █▓▒▒▒▒▒▒▒█▒▒▒█▒▒▒▒▒▒▒▒       █     
\t\t\t\t\t           █▒▒▒▒▒▒▒▒█           █▒▒▒▒▒▒▒▒▒▒              
\t\t\t\t\t         █░░░▒▒██                ░░░░░░▒▒▒█              
\t\t\t\t\t                                    ███                  """+Fore.RESET,"Lickitung", "Normal", "Lame", "Primera", "Zona 3", "Ciudad", "Frutas", "Lamer"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t       ▒▒                                                
\t\t\t\t\t    ░░░░░░░                                              
\t\t\t\t\t   ▒░░░░░░░▒░▒                     ░░░░░                 
\t\t\t\t\t  ░░▒▒▒▒▒▒▒▒▒░▒                   ░░░░░▒▒     ░░░░░░▒    
\t\t\t\t\t ▒░░░▒▒▒▒▒▒▒░░▒         █▒▒▒▒      ▒▒▒▒▒    ░░░░░░░░░░░  
\t\t\t\t\t ▒▒▒▒▒▒▒▒▒▒▒▒▒         █▒▒▒▒▒▒▒▒█          ▒░░░░░░░░░░░░ 
\t\t\t\t\t  ▒▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█     ▒░░░░░░░░░░░▒▒ 
\t\t\t\t\t    ▒▒▒      ▒▓▒▒▒▒░░▒█▓█▒▒▒▒▒▒▒▒▒▓▓▒▓█    ▒▒░░▒▒▒▒▒▒▒▒▒ 
\t\t\t\t\t        ▒    █▒▒▒▒▒▒▓░    ░▒▒▒▒▒█░  ░░▓▓▒▒ ▒▒▒▒▒▒▒▒▒▒▒▒  
\t\t\t\t\t     ░░░▒▒   █░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒   ░░░░▒      
\t\t\t\t\t     ▓▒▒▒▒  █▒▒▒▒▒▒▒▓▒▒▒▓████████████▓█▓▓▓█              
\t\t\t\t\t            ▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▓▓▓▓▒▓▓▓▓▓▓              
\t\t\t\t\t           █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▒▒▓▓▓▓▓▓▓▓▓     ▒▒       
\t\t\t\t\t          █▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓█             
\t\t\t\t\t          ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░█▓▓▓▓▒▒▓▓█             
\t\t\t\t\t           ▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▓▓▓░░▓▓▓▓▓▓▓▓█             
\t\t\t\t\t            █▓▒▒▒▒▒▒▒▒▒▒░░█▓█░░░░█▓░░█▒▒▒▓▓▒             
\t\t\t\t\t             ▓▓▓▓▒▒▓▓▓▓▓▓▓█░░░▓█░░▒▓▓▒▓▒▒▓▓              
\t\t\t\t\t              ▓▓▓▒▓▓▓▓▓▓▓▓▓█░░░░░██▓▒▒▒▓█                
\t\t\t\t\t               █▒▒▓▓▓▓▓▓░░░█▓▓▓▓▓█░▓▓▓▓█  ▒▒░░▒          
\t\t\t\t\t      ░░░░░░▒   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓█  ░░░░░░░         
\t\t\t\t\t      ░░░░░░▒▒    ██ ██▓▓▓▓▓▒▒▒▒█       ▒▒░░░░░░▒        
\t\t\t\t\t     ▒░░░░░░░▒▒           █▓▓█          ▒▒▒▒▒▒░▒         
\t\t\t\t\t      ░░░░░▒▒▒    ▒                        ▒▒            
\t\t\t\t\t          ▒░▒    ▒▒                                      """+Fore.RESET,"Koffing", "Veneno", "Gas", "Primera", "Zona 3", "Cementerio", "Desechos", "Levitación"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t                          █░░                            
\t\t\t\t\t                        █░░░░░░░                         
\t\t\t\t\t                        ▒▒▒▒░▒▒▒                         
\t\t\t\t\t       ░░░░▒▒█           █▒▒▒▒▒                          
\t\t\t\t\t      ░░░░░░▒░                           █▒█             
\t\t\t\t\t      ░░░▒▒▒▒             ▒░█      ███░░░░░░▒█           
\t\t\t\t\t       █▒░░▒     █▒░░░▒▒▒▒▒▒▒▒▒  █▒▒░░▒▒▒▒▒▒▒▒▒▒▒█       
\t\t\t\t\t            ░░▒░░░░░▒▒▒▒░▒▒▒▒▒▒▒ █▒▒▒▒▒░░░▒▒▒▒▒▓▓▒       
\t\t\t\t\t           ▒░░░░░░▒▓▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒█      
\t\t\t\t\t  ░░░▒    █░▒▒▒▒▒▒▒▒▒▓░░░░░░░█▒▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓      
\t\t\t\t\t ░░░▒▒   ▒▒▒▒▒█▒▒▒▒▒▒▒▒▒░░░▒▒▒▒▒▓▒▒▒▒▒▒▒█░░░▓▒▒▒░▓▓▒     
\t\t\t\t\t   █   █▒▒▒░░░▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒█▒█▒▒▒█▒▒▓▓█     
\t\t\t\t\t        ▓▒▒█▒░░▒▒▒▒▒▓░░░█▓▓░░█▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒        
\t\t\t\t\t        ▓▒▒▒▒▒▓░▒▓▓▓▒▒▓█▓▒░░░█▓▒▒▒▒▒▓▒▓▓▓▓▓▓▒▒▒█  █░░░░█ 
\t\t\t\t\t        █▒▓░░▓▓█░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒  ██▓█ █    ▒░░░░▒ 
\t\t\t\t\t         ▒▓░▒▒▒▒█▒▒▒▒▒▓▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒ ▒▓▓▓▓▒      ▓░▒█  
\t\t\t\t\t         ▓▒▒▒▒▒▒█▒█▒▒▒█▒█▒▓▒▒▒▓▒▓▓▓▓▒▓▓▓▓▓▓▓▓            
\t\t\t\t\t          ▓▓▒▒▒▒▒▒▒██▒▒█▒█▒▒█▒▒▒▒▓▓▓   ▓▓▓▓▓█            
\t\t\t\t\t           █▒▒▒▒▓▒▒▒▓█▒█▒▒▓▓▓▒▒▒▒▒▒▓▒                    
\t\t\t\t\t             ▒▒▒▒▒▓▓░░░░░▒▒▒▒▒▒▓▒█▒█  ░░▓░█              
\t\t\t\t\t             ▒▒▒▒▓▒░▒█▒▒▒▒▒▒▒▒▒      ▒▒▒░░░              
\t\t\t\t\t                     ███▒▒▒▒         █▒▒▒▒▒▒             
\t\t\t\t\t         ▒░░▒ █                        █▓█               
\t\t\t\t\t        ▒▒░░▒▒                                           
\t\t\t\t\t         ▒▒▒▒                                            """+Fore.RESET,"Weezing", "Veneno", "Gas", "Primera", "Zona 3", "Cementerio", "Desechos", "Levitación"),
            Pokemon(Fore.LIGHTBLACK_EX+"""\t\t\t\t\t                              ░░▒█                       
\t\t\t\t\t                      ▒▒▓▓█   ▒▒▓▓▓                      
\t\t\t\t\t                     ▒▒█▓▓▓█ ▒▒▒▓▓▓                      
\t\t\t\t\t                     █▒▓▓▓▓▓▓█▓▓▓▓▓▓                     
\t\t\t\t\t                      ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓█                   
\t\t\t\t\t                     ▒▒▓▓▓▓▓▓▓█▒▒▓▓█▓▓▓▓                 
\t\t\t\t\t                ███▒▒█▒█▓▓▓▓███▒▒▒▒▒▓▓█▓▓                
\t\t\t\t\t              █▓▓▒▒▒▒▒▒▒▓▓▓▒▒█▒▒▒▒▒▒▒▓▓▓█▒█▓▓▓▓█         
\t\t\t\t\t           █░░▓█▓▒▒▒▓▒▒▒▓▓▒▒░░▒▒▒█▓▒▒░▓▓▒▒▒██▓           
\t\t\t\t\t          █▒░█▓▓▓▒▒█▒▒▒▒██▒▒░▒▒▒▒█▒█▒▒▒▒▒▒▒▒▒▒           
\t\t\t\t\t         █▒▒░█▓▓▓▒▒▒▒▒▒▒▒▒▒█░▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▓         
\t\t\t\t\t         ▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▓▓▓        
\t\t\t\t\t        ▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓█      
\t\t\t\t\t         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓█░▒▒▒▓▓▓▓▓▓      
\t\t\t\t\t         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓██▒▒▒▒▒▒▒▓█▓▓▓░░     
\t\t\t\t\t        █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓█▓▒▒▒▒█▓▓▒▒▒▓▓█     
\t\t\t\t\t       ▒▒▒▓▒▒▒▓▒▒▒▒▒▒▒▒░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓█▓     
\t\t\t\t\t       ▒▒▒▒▒▒▒▒▒░█▒▒▒█░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓█▓     
\t\t\t\t\t      █▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓█     
\t\t\t\t\t     █▓▒▒▒█▒▓▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓      
\t\t\t\t\t     ▓▓▓▒▒▒▒▒█▒▒▒▒▒▒▒▒▒░░▓▓▓▓▒▒▒▒▒▒▒▒▓▓█▓▓▓▓▓▓▓█▓▓█      
\t\t\t\t\t      ▓▒▒▓▓▓▒▒▓▒▒▒▒▒▒▒▓▒▓▓█▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓       
\t\t\t\t\t       ▒▒▓▓▓▓█▓▒░▒▒▒▒▓▓▓█▒▓▓█▒▒▒▒▒▒▒▒▒▒▓▓▓█▓▓▓▓▓▓▓       
\t\t\t\t\t        █▒▓▓▒▓▓█▓▓▓▓▓█▓▓  ███▓▒▒▒▒▒▒▒▒▓  ▓█▒▓▓▓░██       
\t\t\t\t\t        ▓▓▓▓▓▓▓▓▓█▓▓▓█      █▒▒░▒▒▒▒█▓▓        █         
\t\t\t\t\t         ░░▓█░▒█           ▒▒▒░▒▒▒▒█▒▒█                  
\t\t\t\t\t                            ▒░░░▒▒█░░▓                   
\t\t\t\t\t                              ░     ░                    """+Fore.RESET,"Rhyhorn", "Tierra", "Escarabajo", "Primera", "Zona 2", "Montaña", "Minerales", "Parachoques"),
            Pokemon(Fore.LIGHTBLACK_EX+"""\t\t\t\t\t        ▒▒█        ░█                                    
\t\t\t\t\t         ▒▓▓     ▒▓▒▒                                    
\t\t\t\t\t       ▒░░▒▒▒▒▒▒▒▒▒▒▒                                    
\t\t\t\t\t          ▓▒▒▒▒█▒▒▒▒▒█  ░▒        █                      
\t\t\t\t\t   ░█   █░▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒    █▒░░▒░░█                 
\t\t\t\t\t  ▒▒▓░▓░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▓▒▒▒▒▒▒▒▒                  
\t\t\t\t\t ▒▒▒▒▒░▒▒▓▒▒▒▒█░░▒▒▒▒▒▓▒█░░▒▒▒▒▒▒▒▒▒▒▒░                  
\t\t\t\t\t   ▒▒▓░█▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒░▒▒▓▒▒▒▒▒▒▒▒▒                    
\t\t\t\t\t    █▓▓▒▒▒▒▒▒▓▒▒▓▓▒▒█▒█▒▒▒▒▒▒▒▒▒                         
\t\t\t\t\t         ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                         
\t\t\t\t\t          ▓▒░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒                          
\t\t\t\t\t           ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒                ▓▓▒▒▒▒▒▓   
\t\t\t\t\t           ░▓█▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▓           ▒▒▒▒▒▒▓▓▓█▓▓▓ 
\t\t\t\t\t           █▓░░░░░░▓▓▒▓░░█▒▒▒▒▒▒        █▒▓▓▓▓▓▓▓██      
\t\t\t\t\t           █░░░░░░░░░░░░░░▒▒█▒▒▒▒▓    █▓█▓▓▓▓▓▒▒         
\t\t\t\t\t         ▓▒▒░░░░░░░░░░░█░░▒▒▒▒▒▒▒▒█▓▓▓█▓▓▓▓▓▓▒▒          
\t\t\t\t\t       █▒▒▒▒▓░░▒▓▓▒░░░░░▒▓░░░▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒█          
\t\t\t\t\t      █▒▒▓▓▓▒█▒▒░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒█▓▓▓█▓▒▒▒            
\t\t\t\t\t      █▓▓▓▓▒▓▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓█▒▒█             
\t\t\t\t\t       ▓▓▓▒▓▓▓▓▓▓█▓▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▓▓█▓█               
\t\t\t\t\t       ▒▓▓▓▓▓▓▓    █▓▓▓▓▓▓█▒▒▒▒▒▒▒▒▒▒▓                   
\t\t\t\t\t    █▒▒░░▒▓▓█                 ▓▒▒▒▒▒▒                    
\t\t\t\t\t                              █▒▒▒▒▒▒█                   
\t\t\t\t\t                              █░░▓▓░░█                   
\t\t\t\t\t                                 ▓                       """+Fore.RESET,"Rhydon", "Tierra", "Taladro", "Primera", "Zona 2", "Montaña", "Minerales", "Cabeza de roca"),
            Pokemon(Fore.LIGHTMAGENTA_EX+"""\t\t\t\t\t                         ██░░░░▒█                        
\t\t\t\t\t                     █░░░░░░░░░░░░░░█                    
\t\t\t\t\t      █            ░░░░░░░░░░░░░░░░░░░░                  
\t\t\t\t\t     █▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒▒                
\t\t\t\t\t░░░███▓▒▒▓██▒░░░░░░░░▓░░░░░░░░░░░░░░▒▒▒▒▒▒               
\t\t\t\t\t█░░░▒▒░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒█▒▒▒█            
\t\t\t\t\t █░░░░░░░░░░░▓░░░░░░░░░▓░▒▓░░░░░░░░░░░░▒▒▒█▒▒▒▒░▒▒░▒███  
\t\t\t\t\t  ▒░░░░░░▒▒░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░▓▒▒▒▒▒▒▒▒▒▒░░░░░█
\t\t\t\t\t         █░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░█░░░░░█▒▒▒▓█   
\t\t\t\t\t        █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░█▓  
\t\t\t\t\t        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓░▒▒░░░█▒░░░░░░░█
\t\t\t\t\t       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▒▒░░░░░███    
\t\t\t\t\t       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▒▒▒▒      
\t\t\t\t\t       ░░░░▓░░░░▒█░░░░█░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t      ▓░░░░░░█░░░░░░░░░░█░░░░░░▒░░░░░░░▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t       ░░░░░░░░░░░░░░░░░░█▒█▒░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒        
\t\t\t\t\t       █░░░░▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒█        
\t\t\t\t\t        ░░░░░▒░░░░░░░░░░░░░▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒   
\t\t\t\t\t         ▒░░▒░░░▒▒░░░░░░█▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█    
\t\t\t\t\t          █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█       
\t\t\t\t\t            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█           
\t\t\t\t\t             █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█               
\t\t\t\t\t         ▓▒▒▒▒▒▒▓▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒              
\t\t\t\t\t        █░░▒░▒▒▒▒█   █▓▒▒▒▒▒▒▒▒▒██   █▒▒▒▒▒▒             
\t\t\t\t\t                                       ░░░░░░            
\t\t\t\t\t                                          ██             """+Fore.RESET,"Chansey", "Normal", "Huevo", "Primera", "Zona 1", "Pradera", "Bayas y semillas", "Poder curativo"),
            Pokemon(Fore.LIGHTBLUE_EX+"""\t\t\t\t\t                       █▓██                              
\t\t\t\t\t            ▒      █▓▓▓▓▓▓▓▓▓▓      █▓▓▓█                
\t\t\t\t\t          █▒▓     █▒▒▒▒▒▒▒▒▒█▓▓█ ▓▓▓▓▓▓▓▓▓▓              
\t\t\t\t\t          ▒▒▒  █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒█▓▓▓▓█            
\t\t\t\t\t          ▒▒▒█▒▒▒▒▒█▓▒▒▒▓█▒▒▒▒▒▒▓▓▒█▒▒▒▒▒▒▒█▓            
\t\t\t\t\t      █▓▓▓█▓█▒▒▒▒▓▓▒█▒▒▒▓▓█▓█▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒█          
\t\t\t\t\t     ▓▓▓▓▓▒▒█▒▒▒██▒▒▒▒▓█▒▒▒▒█▓▒▒█▒▒▒▒▓▓▒▒▒▓█▓▓▓▓▓▒▒█     
\t\t\t\t\t    ▓▒▒▒▓█▒▒█▒▒▒▓▓▓▒▒▒█▓█▒▒▒▒▓▓▓▒▒▒▒█▓▓▓▒▒█▓▓▓▓▓█▒▒▒▒    
\t\t\t\t\t   ▒▒▒▒▒▓█▒▒▒▓▓▓██████▓▓▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒   
\t\t\t\t\t  ▒▒▒▓▓█▓▓▓▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒█▓███▒▒▒▒▒▓█  
\t\t\t\t\t ▓▒█▓█▓▓▓▓▒▒▒▒▒▒███▓▓██████████████████████▓▓▓▓█▓▓▒█▒▒▒█ 
\t\t\t\t\t ▓█▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓███░░░░░░▓█████░░░░░████▒▒▒▒█▓▓▓▓▒▒█▒▒█
\t\t\t\t\t█▓▓▓█▓▒▒▒▒█▓█▓▒▒▒▓██░░░░░░░░████▒░░░░░░▒█▓▒▒▒▓▓▓▓▓▓▓▓██▒▒
\t\t\t\t\t▓▓▓█▓▓▒▒▒▓▓▓▓▓▓▒▒▒██░░░░░░  ░▓▓▓█      ░█▒▒▒▓▓▓▒▒▒▓▓█  █ 
\t\t\t\t\t▓▓▓▓▓▒▒▒██▓▓▓▓█▒▒▒██░       █▓▓▓▓█     ▓█▒▒▒▒█▓▒▒▒█      
\t\t\t\t\t█▓▓█▓▒▒▒█▓▓▓▓▓▒▒▒█████  ░ ████▓▓▓▓███████▓▒▒▒▒▒▓▒▒▓█     
\t\t\t\t\t  ▓▓▓█▒▒▓▓▓▓▓▒▒▓▒▒▒▒▒▒█████▒▒▒▒▒▒▒▒█▓▓▓▓▓▒▒█▒▒▒▒▒▒▒▒▒▒   
\t\t\t\t\t   ▓▓██▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒█▓▓▓▓██▒▒▓█▓█   
\t\t\t\t\t   █▓▓█▒▒▒▒▒▓▒▒▒▓▓▓▓▓██▓▒▒▒▒█▓▓▓▓▒▒▒▓█▒▒▒▒▓█▓▓▓▓▓░░▒▒▓   
\t\t\t\t\t    █▓▓▒▒█▒▒▒▒▒▒▓▓▓▓▓█▓▒▒▒▒▓▓█▒▒▒▒▓▓█▓▓▒▒▒██▓▓▓▒▒▒▒▒▒▒▒  
\t\t\t\t\t     █▓▓▒▒▒▒▒▒▒▒▒▒█▓▓█▓▒▒▒█▓▓▓█▒▒▒▒▒▒▓▓▒▒▒██▓▒▒▒▒▒▒▒▓▓▓  
\t\t\t\t\t     █▓█▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▓▒▒▒▒▓█▒▒▒▓▒▒▒▒▒▒▒▓▓▓▓▓█ 
\t\t\t\t\t      ██▒▒▓▓▓▓▓▒▓▒▒▒██▓▓█▓▒▒▒▒█▓▓█▓▓▓▒▒▒▒█▓▒▒▒▒▒▒▓▓▓▓▓▓  
\t\t\t\t\t        ▒▒▒▓▓▓▒▒▒▒▒▒▒▓▓█▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒  ▒▓▒▒▒▒▓▓▓▓▓▓█  
\t\t\t\t\t         ▒▒▓▓▓▒▒▒▒▒▒▒█▓▓▓█ █▓▓▓▓▒▒▒▒█ ▓▓▓█ █▒▒▒▓▓▓▓▓▓█   
\t\t\t\t\t          ▒▒▒▓▓▓▓▓▒▒▒     ▓▓▓█              ▒▒▒▒▓▓▓█     
\t\t\t\t\t           █▒▒▒▒▓▒▒▒█                         ██         
\t\t\t\t\t               ███                                       """+Fore.RESET,"Tangela", "Planta", "Trepadora", "Primera", "Zona 1", "Bosque", "Hojas", "Clorofila"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                             █▒▒▒▒▓    ███               
\t\t\t\t\t                         █▒▓▓▓▒▒▓▓▓░░▒▒▒▒▒░              
\t\t\t\t\t                        ▒▒▒▒▒▒▒▒▒▒▓█▒▒▒▒▒                
\t\t\t\t\t                        █▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓                
\t\t\t\t\t                 ▓█▒▒░░░   ▓▓▓▓▒▒░▒▓▒▒▒▒▓▓   ▓░██        
\t\t\t\t\t                ▒█░░█▒░░█  ▓░░░░▒▒▓▒▒▒▒▒█   ▒░░▒░░░▓     
\t\t\t\t\t               ▒▒▒▒▒█▒█░ ██▓▓▓▓▒▒▒▒▒▒▓▒▒▒▓█░░▒▒▒░▒▒▒     
\t\t\t\t\t              █▒▒▒▒▒▒▒▓▒▓▒▒▓▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     
\t\t\t\t\t              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒█▒▒▒▒▒▒▒     
\t\t\t\t\t              ▒▒▒▒▒▒█▒▒▒▒▒▒▒░░░░░▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█    
\t\t\t\t\t               ▒▒▒▒▒▒▒▒▓░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒█    
\t\t\t\t\t                      ░░░▓░░▓█░░░░░░░▒▒▒▓▓█▓▒▒▒▒▒▒▒▒     
\t\t\t\t\t                     ░░░░██░░░▒░░░░░░░▒▒▒▒▓    █▓▓▒      
\t\t\t\t\t                    ░░░▓░░▓░▒▒▒░░░░░░░▓▒▒▒               
\t\t\t\t\t      ░    ▓▒▒▓░░▒▓░░░░░░░░░░░▒▒░░░░░░▓▒▒▒               
\t\t\t\t\t      ▒▒▒█▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▓▒▒▒▓▒▒▒▒█             
\t\t\t\t\t     ███▓▓▓▓▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░█▒▒▒██             
\t\t\t\t\t     ░▓▓▓▓▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░░▓▒▒▒              
\t\t\t\t\t      ▓▓▓▓▓▓▒▒█▒▒▒▓░░░░░░░░░░░░░░░░░░░░▒▒▒▒              
\t\t\t\t\t       ▓▓▓▓▓▒▒▒▒▒▒▒▓░░░░░░░░░░░░░░░░░▓▒▒▒▒▒▒             
\t\t\t\t\t          █   █▓▓▓█▒▓▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░            
\t\t\t\t\t             █▓▓▓▓▓▓▓▓▒▒▒▒▒░░░░░█▓▒▒▒▒▒▒█▒▒▒▒█           
\t\t\t\t\t         █▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒░░▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█           
\t\t\t\t\t       █▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█   ▒▒▒█▒▒▒▒▒▒█▓█            
\t\t\t\t\t        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█         █▓▒▒▒▒▒▒▒▒▒             
\t\t\t\t\t                                 █░░▒▓░░░░▒▒█            
\t\t\t\t\t                                      █▒▒█               """+Fore.RESET,"Kangaskhan", "Normal", "Madre", "Primera", "Zona 1", "Pradera", "Bayas y semillas", "Fuga"),
            Pokemon(Fore.LIGHTBLUE_EX+"""\t\t\t\t\t                         ░░░░░░░░░░█     ░░              
\t\t\t\t\t                      ▒░░░░░░░░░░░░░▒▒▒░░░               
\t\t\t\t\t                     ░░░░░▓░░░░░░░░▒░░░░█                
\t\t\t\t\t                    ░░░█▒░░ ▒░░░░░░░░░▓▒▒                
\t\t\t\t\t         █░█       ░░░░▒▒▒░░▓░░░░░░░▒█▒▒▒█               
\t\t\t\t\t        █▓█░░░░░░░░░░░░▓█▒░░█░░░░░░▒▒▒▒▒░░░░░░░░         
\t\t\t\t\t        █▒█░░░░░░░░░░░░▒▒░░░░░░░░░▒▒▒▒▒▒▒▒█              
\t\t\t\t\t         ▒██░░░░░░░░░░░░░░░▒░░░░▒▒▒▒▒▒▒▒▒                
\t\t\t\t\t          ▒█░░░▒▒▒▒▒▒▒▒░░░░░░░▒▒▒▒▒▒▒▒▒▒█                
\t\t\t\t\t            ███      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒░░░░█             
\t\t\t\t\t                       █▒▒▒▒▒▒▒▒▒▒▒▒▒     ██  █░░░░░█    
\t\t\t\t\t                              ▒▒▓▒▒▒▒     █▒▒░░░░░░▓▓░   
\t\t\t\t\t                             █░░▒▒▒▒▒   ▒▒▒▒▒░░░░░░░░█   
\t\t\t\t\t                            ░░░░▒▒▒▒▒▓▒▒█▒▒░░░░░░░░░▓    
\t\t\t\t\t                          ░░░█░░▒▒▒▒▒▒██▒░░░░░░░▒░▓█     
\t\t\t\t\t                       █░█░░░░░░▒▒▒▒▒▒█ █░░░░░░░░█       
\t\t\t\t\t                      ░░░░░░░░░█▒▒▒▒▒▒█                  
\t\t\t\t\t                     ▓░░░░░░░░░▒▒▒▒▒▒▒█                  
\t\t\t\t\t              █░░░░░█░░░░█░░░█░▒▒▒▒▒▒▒                   
\t\t\t\t\t            ░░░░░░░░░░░░░░░█░▒▒▒▒▒▒▒▒▒                   
\t\t\t\t\t           ░░░░░░░▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒                    
\t\t\t\t\t          ▒░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒                     
\t\t\t\t\t          ▒░░░░█░░░░░░░▓░▒▒▒▒▒▒▒▒▒▒                      
\t\t\t\t\t           ▒░░░░█░░░░░░░▒▒▒▒▒▒▒▒▒                        
\t\t\t\t\t            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                          
\t\t\t\t\t              █▒▒▒▒▒▒▒▒▒▒▒▒▒                             
\t\t\t\t\t                    ██                                   """+Fore.RESET,"Horsea", "Agua", "Caballito de mar", "Primera", "Zona 2", "Mar", "Algas", "Nado rápido"),
            Pokemon(Fore.LIGHTBLUE_EX+"""\t\t\t\t\t                          █      ▒                       
\t\t\t\t\t                   ▓░░░▒░█    █▒▒                        
\t\t\t\t\t               █░░░▒▒░▒▒█   ▓▒▒▒                         
\t\t\t\t\t ██░░▒      █░▒▒█▒░░░░▒▒▒▒▒▒▒▒▒█               ▓█        
\t\t\t\t\t ▒██░░░░░█ ░▒▒░░░░▒▒░▒▒▒▒▒▒▒▒▒▒ █▒▒████     █░░          
\t\t\t\t\t████░░░░░░░▒░░░░░░░░▒█▒▒▒▒▒▒█▒▒▒▒▒▒▒▓     ░░░░           
\t\t\t\t\t  █░░▒▒▒▒░▒▒░░░▒▓█░░░▒▒▒▒▒▒▒▒▒▓▓█      ▒░░░░█            
\t\t\t\t\t         ▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓   █░▒▒░░░              
\t\t\t\t\t           ▒█▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░▒░░░██        ██████ 
\t\t\t\t\t             ▒▒▒▒▒▒▒▒▒░░░░░░░░██▒▒▒▒▒░░░░░░░░░░░░░░░░█   
\t\t\t\t\t               █▒▒▒▒▒▒█░▒░▒░░░░░▒▒▒▒▒░░░░░▓░░░░░█        
\t\t\t\t\t                  ░░░░▒▒▒░▓▒▒█▒░░░▓▓▒▒▒▒░░░▒█            
\t\t\t\t\t                  ░░░░░▒▒░▓▒█▒▒▒▒▒▒▒▒▒▒░░█               
\t\t\t\t\t                  ░▒░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░█             
\t\t\t\t\t                 █░░░░░░▒▒█▒▒▒▒█   █▒▒▒▒▒░░░░            
\t\t\t\t\t                  ░░█▒█░▒▒▒▒▒▒▒▒▒▒         ██░░          
\t\t\t\t\t                  ░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▓                    
\t\t\t\t\t                   █▒▒█▓▓▒▒░░▒▒▒▒█▒▒▒▒                   
\t\t\t\t\t                     ░░▓░░░░░▒▒▒▒▒▒▒▒▒▒█                 
\t\t\t\t\t                      █░░░░░░░░▒▒▒▒▒▒▒▒▒                 
\t\t\t\t\t                      ░░░▒█░▒░▒▒▒▒▒▒█▒▒▒                 
\t\t\t\t\t                      ░▒▒▒▒▒▒▒█▒▒▒▒▒█▒▒▒                 
\t\t\t\t\t                      ▒░░░▒░░▒▒▒▒▒▒▒▒▒▒▒                 
\t\t\t\t\t                      █░░░▒▒█▒▒▒▒▓▒▒▒▒▒                  
\t\t\t\t\t                        ▒▒▒▒▒▒▒▒▒▒▒▒▒▓                   
\t\t\t\t\t                           █▒▒▒▒▒▒▒█                     """+Fore.RESET,"Seadra", "Agua", "Caballito de mar", "Primera", "Zona 2", "Mar", "Algas", "Nado rápido"),
            Pokemon(Fore.WHITE+"""\t\t\t\t\t                      ██                                 
\t\t\t\t\t                     ░░░░░                               
\t\t\t\t\t                 █░░░░░░░░░░█             █              
\t\t\t\t\t                ░░░░░░░░░░░░░            ░█              
\t\t\t\t\t           █    ░▒░░░░░░█▒░░░█ █        ░░               
\t\t\t\t\t       █░░░░░░███░░░░░░▒▒▒▒▒░░▒░░░▒▒██ █░░               
\t\t\t\t\t      ░░░░░░░░░░░░▒░░░▒▓▓▓▓▓▒░░░▒▒▒░░▒▒░░░               
\t\t\t\t\t     █░░░░░░░░░░░░░░░░▒▒▒▓▓▒▒▒▒▒░░░░░░░▒▒▒▒▒             
\t\t\t\t\t   █░░░░░░░░░░░░▒▒░░░░▒▒▒▒▒▒░░░░░░▓░░▒▒▒░░░░░░▒          
\t\t\t\t\t  █░░░░░░░░░░▒█▒▒▒▓▓█▓▓▓▓█▓░░░░░░░ ░▒█▓█░░░░░░░░         
\t\t\t\t\t ░░░░░░░░░░░░░░░░▒▓▓▓▓███▒█▒▒▒▒░░░░ ░░░░░░░░░░░█         
\t\t\t\t\t    ██      █░░░░░░▓░░░░▒▒▒░░░░░░░░░░░░░░░█░▒▒█▓▓        
\t\t\t\t\t                ░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒█     
\t\t\t\t\t             █░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒█   
\t\t\t\t\t            ░░░░░░░░░░░░░░█ █░░░░░░░░░░░░░  ░▒▒▒░▒▒░░░░  
\t\t\t\t\t               ░░░░░░░░░░░     ▓░░░░░░░█    ▓▒▒▒░░░░░░ █ 
\t\t\t\t\t                ▒░░░▓                                    """+Fore.RESET,"Goldeen", "Agua", "Pececillo", "Primera", "Zona 2", "Río", "Peces y algas", "Nado rápido"),
            Pokemon(Fore.WHITE+"""\t\t\t\t\t                 █                                       
\t\t\t\t\t                 ░░░░░░        █░▒                       
\t\t\t\t\t                 ░░░░░░░░▓   ░░░░░░                      
\t\t\t\t\t                 █░░░░░░░░░█░░░░░░░█           ▓░░░░░    
\t\t\t\t\t     ░▓          █░░░░░░░░░░░▒░░░░░█        ░░░░░░░░░░░  
\t\t\t\t\t      ░░▓        █▓░░░░░░░░░░░███░░█      ░░░░░███░░░░░█ 
\t\t\t\t\t      ░░░░█ ▒░░░░▒▒▒▒▒▓▓█▓░░░░░█░░░     ░░░░▒░░░░░░░░░░█ 
\t\t\t\t\t       ░░░░░▒▒▒▒▒▒▒▒▒▒▒█████░█░░░░░   ░░░░░░░▒░░░░░░░░░  
\t\t\t\t\t       ░░░▒▒▒▒▒▒█░░▒▒▒▒▒▓▓▓▓██░░█░▓  ░░░█░░░░░░░░░░░░░   
\t\t\t\t\t     █▒▒▒▒▒▒▒▒█░░░███▓▒▒▒███████░░░█░░░░░░░░░░░░░░░░░    
\t\t\t\t\t    ░▒░▓▒▒▒▒▒▒░██████░▒▒▒██▒██▓█▓░░░░░░░░░░░░░░░░░░      
\t\t\t\t\t   ██▒▒█░▒▒▒▒▒▒░██▓▓░▒▒▒▒██▒▒▓▓█▓█░░▓░░░░░░░░░░░░░       
\t\t\t\t\t    ▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒█▒▒██▒█▓▓▓▓▓░░░░░░░░░░░░░░░        
\t\t\t\t\t    ░░░░░░░░▒▒▒▒▒▒████▒▒███▓▓▓▓▓▓█░░▒░░░░░░░░░░░░█       
\t\t\t\t\t    █░░░░░░░░▒▒▒▒▒▒███▒▒██▓▓▓▓██░░█░░░░░░░░░░▓█░░░       
\t\t\t\t\t     █░░░░░░░░▒▒▒▒▒▒▒▒▒██▓▒░░░░░░░░░░█░░░░░░░░░░░░░      
\t\t\t\t\t     ██▓▓▒░░░▒▒▒▒▒▓▓▓▓█▓▓▒░░░▒░▓██░░░░░░░█░░░░░░░░░█     
\t\t\t\t\t   ░░▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▒░░░░░░█░░░░█░░░░░█░░░░░█     
\t\t\t\t\t ░░░▒█▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▓░░░░░░░░▒░░░░░░░█░░░░      
\t\t\t\t\t ░░░░▒▒▒▒▒█   █▒▒▒▒▒▒░░░░░▒▒█░░░░░▒░░░░░     ░░░░▓       
\t\t\t\t\t        ▒▓▒█           ▒▒▒▒▒ ░░░░░░░░░▒░                 
\t\t\t\t\t                     █▒▒█▒▒▒ ▓░░░░▓░░░▒░░                
\t\t\t\t\t                    █▒▒▒▒▒▒▒ █░░  ░░░░██░░░              
\t\t\t\t\t                    ▒▒░░░░░█  ░   ░░░░░░█░░░█            
\t\t\t\t\t                    █░░░░░█       ▓░░░░░░█░░░            
\t\t\t\t\t                                   ░░░░░░░░░▒            
\t\t\t\t\t                                   █░░░░░░░█             
\t\t\t\t\t                                     ████                """+Fore.RESET,"Seaking", "Agua", "Pez espada", "Primera", "Zona 2", "Río", "Peces y algas", "Nado rápido"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                            █▓▓                          
\t\t\t\t\t                           ▒▓▓▓█                         
\t\t\t\t\t                          ░░▓▓▓▓                         
\t\t\t\t\t                         ▒░░▓▓▒▓▓                        
\t\t\t\t\t                        ▒▒░█▓▓▓▓▓█                       
\t\t\t\t\t                       ▒▒▒░▓▓▓▒▒▓▒                       
\t\t\t\t\t                      ▒▒▒▒▒▓▓▓▓▓▒▓▓             █░░░▒▓█  
\t\t\t\t\t      ███            ▓▒▒▒▒▒▓▓▓▓▓▓▓▓█      █▒▒▒▒░█▒▓▓▓▓   
\t\t\t\t\t      ▒▓█░░▒▒▒▒█  ░░█▒▒▒▒░▓▓▓▓▓▓▓█░░░▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓    
\t\t\t\t\t      ▓▓▓▓▓▓▒▒▒▒▒▒▒░░░▒░░░░░░░░░░░░▒▓▓▒▒▒█▓▓▓▓▓▓▓▓▓█     
\t\t\t\t\t       ▓▓▒▓▒▓▓▓▒▒▒█░░░░░░░░░░░░░░▒░▓▓▒▓▓▓▓▓▒▓▓▓▒▓▓█      
\t\t\t\t\t        ▓▓▓▒▒▒▓▓▓░░░░░░░░░░░░░░░░░░░█▓▓▓▓▓▒▒▒▒▓▓▓        
\t\t\t\t\t         ▓▓▒▒▓▓▓░░░░░░▒░░▓▓▒▒░▓░░░░░░▓▓▓▓▓▓▓▓▓▓▓         
\t\t\t\t\t          ▓▓▓▓▓███░░░▒▓▒▓▓▓▓▒▒░░░░░░▓██▓▓▓▓▓▓▒▓          
\t\t\t\t\t           ▓▓▓░░░░░░░█▓▓▓▒▒▒░▒░█░░░░░░░░▓▓▓▓▓█           
\t\t\t\t\t            ▓▓▓█░░░░░░█▒▒▒░░▒░█▒▒▒▒▒▒▒▒▒▓▓▓▓             
\t\t\t\t\t             ▓▓▓▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒█             
\t\t\t\t\t             ▒▒▒▒█▒░░▓▒▒▒▒▒▒▒█░░█▒▒▒▓▓▓▓▓▓▒              
\t\t\t\t\t            ▓▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓              
\t\t\t\t\t            ▒▒▒▒░░▓▓▓▓▓█▒▒▒▒▒█▓█▓░█▓▓▓▓▓▓▓▓              
\t\t\t\t\t           █▒▒▒░▓▓▓▓▓▓▓▓▒▒▒█▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓█             
\t\t\t\t\t           ▒▒▒░▓▓▓▓▓▓▓▓▓█▒▒█▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓             
\t\t\t\t\t          █▒▒░▓▓▓▓▓▓▓▓█      █▒▒▒▓▓▓▓█▓▓▓▓▓▓█            
\t\t\t\t\t          ▒▒░▓▓▓▓▓▓▓█           ▒▓▓▓▓▓▓▓▓▓▓▓█            
\t\t\t\t\t          ▒▒▓▓▓▓▓▓                ▓▓▓▓▓▓▓▓▓▓▓            
\t\t\t\t\t         █▒▓▓▓▓▓                    █▓▓▓▓▓▓▓▓            
\t\t\t\t\t         ▒▓▓▓█                         ▓▓▓▓▓▓            
\t\t\t\t\t                                          ▓▓▓            """+Fore.RESET,"Staryu", "Agua", "Estrella de mar", "Primera", "Zona 2", "Mar", "Algas", "Estrella"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t                            █▒                           
\t\t\t\t\t                           ░▓▒▒█                         
\t\t\t\t\t         ██              █░░▒▒▒▒             ▒▒▒▒▒       
\t\t\t\t\t         ▒▒▒▒▒          █░░░▒▒▒▒▒        █▒▒▒▒█▓▓▓       
\t\t\t\t\t         ▒▓█▒▒▒▒▒      █░░░█▒▒▒▒▒█   █▒▒▒▒▒▒█▓▓▓▓█       
\t\t\t\t\t          ▓▓▒▒▒▒▒▒▒▒   ▒░░░▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒█▓▓▓▓▓█        
\t\t\t\t\t          █▓▓▓▒▒▒▒▒▒▒▓▒░▒▓░▒▒▒▒▒▒▒█▓▓▒▒▒█▓▓▓▓▓▓█         
\t\t\t\t\t           ▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░▓▒▒▒▒▒▒▒▓▓▒█▓▓▓▓▓▓▓█          
\t\t\t\t\t           █▓▓▓▓██▓▓█▒▒▒█░░▒▓▒▒▒▒▒▒█░▓▓▓▓▓▓▓▓█           
\t\t\t\t\t            ▓▓▓▓▓░░░▒▒█░░░░░░░░█▒░░░░█▓▓▓▓▓▓█            
\t\t\t\t\t             ▓▓▓▓▓░░░░█░░░░░██░░░░█▒▒▒▒▒█▓▓              
\t\t\t\t\t             █▓▒▒▒░░░░░░░░▒▒▒▒▒█░▒░░▒▒▒▒▒▒▒█             
\t\t\t\t\t            ▒▒▒▒▒░░█░░█▓▓▒░░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒           
\t\t\t\t\t         █▒▒▒▒▒▒█▓░░░░▓░░░░░▒█▓▒▒░░░░░░▒▒▒▒▒▒▒▒░█        
\t\t\t\t\t       ▒░░░░░░░░░░░░░░░░▒▒▒▒▒█▓▓▒░░░▒░░▒▒▒▒▓█▒░░░░▒      
\t\t\t\t\t     ░░▒▓▒▒▒▒▒▒▒█▒█▓▓▓▓▒▒▒▒▒▒▒▒▒▓░▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒█▒    
\t\t\t\t\t    ▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▓▒▒▒▒░░▒▒▓▓▒▓▓▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    
\t\t\t\t\t         ▓███▒▒▒▒▒█░░░▒▒▒▒▒▒██▒░░░▒█▒▒▒▒▓██▓▓▓▓▓▓█       
\t\t\t\t\t       █▒▒▒▒▓▓▓▒▒░░░▒▒▒▒░░░▒▒▒▒▒░░░▓▒▒▒▒▒██▓▓▓▓▓▓▒▒      
\t\t\t\t\t      ▒▒▒▒▒▓▓▓▓▒▒░██▒▒▒▒▒░░▒▒▒█▒▒▓▒▒▒▒▒▒▒▒▓▓▓█▒▒▒▒▒▒     
\t\t\t\t\t    ▒▒▒▒▓▓▓▓▓▓█▒▒▒▒▒▒▒▒▒▓░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒█   
\t\t\t\t\t  █▒▒▓▓▓▓▓▓▓▓▓▒▒▒░▒▒▒▒▒▒▒░░█▒▒▒▒▒▒▒▒█▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▒▒  
\t\t\t\t\t █▓▓▓▓▓▓▓▓▓██ ▒░░█▒▒▒▒▒▒▒█▒▒▓█▒▒▒▒▒▒▒▒▒▒▒▒▒  ███▓▓▓▓▓▓▓  
\t\t\t\t\t              ░░█▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒              
\t\t\t\t\t             █░░▒▒▒▒▒   █▒▒▓▓▓▓█  █▒▒▒▒▒▓▒▒█             
\t\t\t\t\t             ▒░▒▒▒▒      ▒▒▓▓▓█     █▒▒▒▒▓▒▒             
\t\t\t\t\t             ▒▒▒▒█        ▓▓▓█         ▓▒▒▒▒             
\t\t\t\t\t              █                           █              """+Fore.RESET,"Starmie", "Agua", "Estrella de mar", "Primera", "Zona 2", "Mar", "Algas", "Estrella"),
            Pokemon(Fore.LIGHTMAGENTA_EX+"""\t\t\t\t\t                                        ▒▒▓█             
\t\t\t\t\t    ░░▓ ░▒░ ▓░▓▓█                     █▓▓▓▓▓▓▓█          
\t\t\t\t\t  █  █░  ░ █▒▒░▓▓▓                  █▓▓▓▓▓▓▓▓▓▓▓▓        
\t\t\t\t\t ▒▒▒█ █░░░▓░░▓▓▓▓▓▓▓▓▓▓██░░░░░░ █▓▓▓▓▓▓▓▓▓▓▓             
\t\t\t\t\t    ░░░░░░░░ ▓░░▓▓▓▓▓▓░░░░░░░░░▓▓▓▓▓▓▓▓▓  █              
\t\t\t\t\t     ▒░░░░░░░░▒░▓▓▓▓█░░░░░░░░░░█▓▓▓▓▓▓▓█                 
\t\t\t\t\t      █░░░░     █▓▓█░  ░░░░░░░░░█▓▓▓▓▓▓█                 
\t\t\t\t\t       ░░         █░░░ ░░░░  ░░░░░░░                     
\t\t\t\t\t      █░█         ▒█░░░░░░░░░░▓▒▒░░░                     
\t\t\t\t\t      ░░       █▒██▒░░██▒▒▒▒░░▒▒▒▒░█▒▒█                  
\t\t\t\t\t      ░░░░░█ ▒▒▒▒▒▒▒█░░░░░▓░░░▒▒▒░▒▒▒▒▒▒████░░░█         
\t\t\t\t\t         █░░░░█▒▒▒▒▒▒░░░█░░░░░█░▒▒▒▒▒▒▒▒▒▒░█  ░░         
\t\t\t\t\t            ▒▒▒▒▒▒▒▒▒░░░░░░░░░░░▒▒▒▒▒▒▒▒▒█    █░░        
\t\t\t\t\t            ▓▒▒▒▒▒▒▒▒░░▓▒▒▒▒▒▒█░░▒▒▒▒▒▒▒█      █░█       
\t\t\t\t\t               █▓█░░░░█▒▒▒▒▒▒▒▒▒░░░░██       ░░░░░░░██░  
\t\t\t\t\t                █░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░    █░░░░░░░░░░█ █  
\t\t\t\t\t                 ██░░░▒▒▒▒▒▒▒▒▒█░░███         ░░ ░░  ░░  
\t\t\t\t\t               █▒▒▒▒▒▒░░█▒▒▒▒▒░█▒▒▒▒▒█       ░░░ █░░     
\t\t\t\t\t               ▒▒▒▒▒▒▒░░░░░░░░░▒▒▒▒▒▓█                   
\t\t\t\t\t             █░░█▒▒▒▒▒░░░░░░░░░▒▒▒▒█░░░░░█               
\t\t\t\t\t          █░░░░   ██             █     █░░░░█            
\t\t\t\t\t        █░░█▒▒▒                          █░░█            
\t\t\t\t\t         █▒▒█▒▒▒                         ░▒▒▒            
\t\t\t\t\t         █▒   █▒▒▒▓                       █▒▒▒           
\t\t\t\t\t        ▓▓ ███▓▓▓▓▓▓                      ▓▓▒▒▓▓  ▓▒▓▓   
\t\t\t\t\t       ▓▓▓▓▓▓▓▓▓▓▓█                       ▓▓▓▓▓▓▓▓▓▓▓▓▓  
\t\t\t\t\t        ▓▓▓▓▓▓▓▓                             ▓▓▓▓▓▓▓▓▓▓  
                                                 ██▓▓▓   """+Fore.RESET,"Mr. Mime", "Psíquico", "Barrera", "Primera", "Zona 3", "Ciudad", "Frutas", "Indefenso"),
            Pokemon(Fore.LIGHTGREEN_EX+"""\t\t\t\t\t               █▒█▒▒                                     
\t\t\t\t\t                  ░░░░▓█                                 
\t\t\t\t\t                   █░░░░▒                                
\t\t\t\t\t                    ░░▒░░▒     █                         
\t\t\t\t\t                    ░░░░░█     ░                         
\t\t\t\t\t                    ░░░░██    ▓▒                         
\t\t\t\t\t                      █░█▒█   ▒▒█                        
\t\t\t\t\t                        ░▒▒▒▓░░▒▒              ▒▒░░      
\t\t\t\t\t                        ▓▒▒▓▒▒░▒▒▒▒▒      ▓▒░░░░░█       
\t\t\t\t\t                         ▒▒▒▒▒▒▒▒▒     ▒░░░░░░░█         
\t\t\t\t\t                         ▒▒▒▒▒▒▓▒▒  ▒░░░░░░░░ ██         
\t\t\t\t\t                         ▓▓█░▒▒▒ ██░░█░░░░░░░█           
\t\t\t\t\t                         █░░▒░░▒▒░░░░░░░░░░              
\t\t\t\t\t                         █▒▒▒▒▒░▒▒░░░░░░█                
\t\t\t\t\t                  █▒      █▒▒▒▒░░░░░                     
\t\t\t\t\t                  ▒▒▒▒██▒▒░▒▒▓▒██░░░░▒█                  
\t\t\t\t\t                  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░▓█░░░▓▒▒█             
\t\t\t\t\t                  ▒▒▒▒▒▒░░▒▒▒▒▓▓▓█▒░░░░░░░░░░░░░░        
\t\t\t\t\t                  █▒▒▒█▒▒▒▒▒▒▒▓▓▓▓     ░░░░░░░░░▒█       
\t\t\t\t\t                ░░░   ▒▒█▒▒▒█▓▓▓▓▒█     ░░░░░░░░▒        
\t\t\t\t\t              ▒▒▒▒▒    ▓▒▒       ██▒▓    ░░░░░░░▒        
\t\t\t\t\t            █▒▒▒▒▒                ▓▓▓▓█  ░░░░░░░▒        
\t\t\t\t\t           ▒░▒▒▒▒▒                 ▒▓▓▓▓ █░░░░░░         
\t\t\t\t\t          ▒░▒▒▒▒▒▒                 ▒▒▒▓▓▓█░░░░▒          
\t\t\t\t\t         ▒▒▒▒▒▒▒▒                  ▒▒▒▒▓▒▒░▒▒            
\t\t\t\t\t       ░▒▒░▒▒▒▒▒▒                   █░▒▓▒▓▓              
\t\t\t\t\t        ▓░█▒▒░▒█                      █                  
\t\t\t\t\t       ██   █                                            """+Fore.RESET,"Scyther", "Bicho", "Mantis", "Primera", "Zona 1", "Pradera", "Hojas", "Ojo compuesto"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t                       █░░░░▓█░░░░░█                     
\t\t\t\t\t                     ░░░░░░░░░█░░░░░░▒                   
\t\t\t\t\t                   █░░░░▒▒▒░▒▒▒▒▒░░░░░░                  
\t\t\t\t\t                  ░░░░░▒▓▓▓▒▒▒▒▒▒▒░░░░░░                 
\t\t\t\t\t                 ░░░░░▓  ░▒▒▒  ░▒▒▒░░░░░░                
\t\t\t\t\t                █░▒░░▓▒░░▒░░▒░░█▒▒▒░░░▒░░░               
\t\t\t\t\t                ░░░░░▒▒▒▒░▒░░▒▒▒▒▒▓▓░░░░░░░              
\t\t\t\t\t               ▓░░░░█▓▒▒▒░░░░▒▒▒▓▓▓▓░░░░░░░              
\t\t\t\t\t               ░░░░░█▓█▓▓▓▓█▓▓██▓▓▓▓░░░░░░░░       ▒█    
\t\t\t\t\t     ▒█        ░░░░░█▓▒▒░░▓▓░░▒▒▒▓░█░░░▓░░█░  █   ▓▓ █▒  
\t\t\t\t\t █▒  ▒▓        ░░░░░░▒▒▒▒░░░▒▒▒▒▒▒▒░░░░░░░█▒ ▒▓▒ ▒▓ ▓▓█  
\t\t\t\t\t  ▓▓▓▓▓▓█▒▓▓█  ░░▒░░░▓▓▓▓░░░▒▓▓▓▓▓█░░░░░░░▒▒  █▓▓▓▓▓▓    
\t\t\t\t\t█▒▓█▓▓▓▓▓▓ █░░  ░░░░░█▓█▒▒▒▒▒█▓▓▓▓░░░░░░▓░█░░░░▓▓▓▓▓▓███ 
\t\t\t\t\t    ▓▓▓▓▓█░░░░░░█▓░░░░▓▓▓▓▓▓█▓█▓█░░░░░░░░█░░░░░░░ █ ▓▒   
\t\t\t\t\t ▒▒▓     █░░░░░█  █▓░░░▓▓▓▓▓▓▓▓░░░░▒█░░░░░█░▒░░      █   
\t\t\t\t\t            ▓░   █▒▒▒▒▒▒█▒▒▒▓░░▓░▓▓█░▓░█▒▒░░░█           
\t\t\t\t\t               █▒▒▒▒▒▒▒█▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓█                
\t\t\t\t\t            █▒▒▒▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓█               
\t\t\t\t\t             ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▓▒▓▓▓▓▒▒              
\t\t\t\t\t          █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒█▓▓█▒▒▓            
\t\t\t\t\t      ▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓██             
\t\t\t\t\t    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒█▓▓▓▓▓          
\t\t\t\t\t           ▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▒█        
\t\t\t\t\t               ▓▓▓▓▓▓▓▓▓█       ▓▓▓▓▓▒▓     █            """+Fore.RESET,"Jynx", "Hielo", "Humanoide", "Primera", "Zona 3", "Ciudad", "Frutas", "Desvía golpes"),
            Pokemon(Fore.YELLOW+"""\t\t\t\t\t                    ░░▒▒▒▒                               
\t\t\t\t\t                 █░░▒█▒█▒▓▒                              
\t\t\t\t\t               █▓░░▒▒▒▒▒▒▒▒                              
\t\t\t\t\t              ░░▓█▒█▒▒▒▒░░█                              
\t\t\t\t\t            █▓░█▒██░░  ░░                                
\t\t\t\t\t           ███▒▒██ ░░ █░                                 
\t\t\t\t\t           ░░░▒▒░░  ░ ░█     ░░▒                         
\t\t\t\t\t           ░▒░▒▒█ ▒█░░░░░░█░█                            
\t\t\t\t\t           █  ███░▓░░██░░░░░▒▒▒█                         
\t\t\t\t\t               ▒░░▓██▒░░░░░░░░▒▒   █░░░█                 
\t\t\t\t\t                █░░█░█ ░░░▒▒▒▒█   █░░█▓░▓██▓▓░░░░░░      
\t\t\t\t\t                 █▒▒▒▒▒▒▒░▒▒▒██▒██▒░░░░██░░░░░▓░░░░░░    
\t\t\t\t\t                  █░░░░▒▒▒█▒░██▒█      ██░░░░░░░░░░░█░█  
\t\t\t\t\t                 ░░█▒▒▒▒██░░░█             ░░░▒▒░▒░░░░▒  
\t\t\t\t\t               ██▓▓█████░░░░░▒▒             █▒▒ █▒▒▒▒▒█  
\t\t\t\t\t              █▓▓▓██████▒░░░▒▒▒                          
\t\t\t\t\t              █░░░░░██████░▒▒▒▒                          
\t\t\t\t\t             █░░░░█████░░▒▒▒███                          
\t\t\t\t\t             █░░████░░▒▒▒█████▒            ▓             
\t\t\t\t\t              ▒██▒▒▒▒▒████▒▒▒▒█          ████            
\t\t\t\t\t            ███▒▒▒▒▒▒▒▒▒▒▒▒▒░░         █▒▒█              
\t\t\t\t\t          ▒░░▒██ ▒▒▒▒▒▒▒▒▒▒▒██▓██    ▓▓██                
\t\t\t\t\t         █████         ████▓ █░░░▓▓██▓                   
\t\t\t\t\t       █░░░▒▒▒█             ██▒▒▒▒                       
\t\t\t\t\t    ░▓░░░░░▒▒                ▓░███                       
\t\t\t\t\t █░░░░░░▒▒█                  ░░░░░▒▒▒░█                  
\t\t\t\t\t                              ░░░█░░░░░░░                
\t\t\t\t\t                                    ░                    """+Fore.RESET,"Electabuzz", "Eléctrico", "Eléctrico", "Primera", "Zona 2", "Montaña", "Electricidad", "Estática"),
            Pokemon(Fore.RED+"""\t\t\t\t\t                                      █                  
\t\t\t\t\t                            █░░█    █░░░                 
\t\t\t\t\t                            █░░░     ░░░                 
\t\t\t\t\t                          ░░░░░░  ░░░░░                  
\t\t\t\t\t                            ░░░░  ▒░░░░░█                
\t\t\t\t\t                         ▒▒▒░▒▒▒▒░░░░▒░                  
\t\t\t\t\t                        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                  
\t\t\t\t\t                         ▓▒▒▓▓▒▒▒▒▒▓▒▒▒▒                 
\t\t\t\t\t                     █▒▓█  ░░░█▓░░░▒▒▒▒                  
\t\t\t\t\t                       ▓▓▓░░░░░░▒▒▓▒▒▓                   
\t\t\t\t\t                         ░░░▒▒▒▒█▓█▓█░░░░█               
\t\t\t\t\t   █       ██    █ ▒█▒▒▒▒░░░░███████▓▓▒▒▒▒▒▓▓▓▓▓▓ █▓▒░█  
\t\t\t\t\t   ░█     ████░▓▓▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓   
\t\t\t\t\t   ░░░░█   ▓▓▓▓▓▓▒█▓▓▓▓█▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓█▓▓▓░░█ 
\t\t\t\t\t  ░░░░░▒▓   ▒▓▓▓█▓░▓▓▓███▒▒▒▒▒▒▒█░▒▒▒▒▒░██    █          
\t\t\t\t\t    ░░▒▒▒▒           ▓▓▓▓▓▓▒▒▒▒░░░█▒▒▒▒█░░               
\t\t\t\t\t     ▒░▒▒         ▓▓█   ███▓▒▒░░░░▒▒▒▒░░▒▒▒█             
\t\t\t\t\t    ▒▒▒▒▒▒█         ▓░░░░░░░▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒            
\t\t\t\t\t     █▒▓▒           ░░░░░░░░▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒░█           
\t\t\t\t\t         ▒█        █▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            
\t\t\t\t\t          ▒▒▒       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█            
\t\t\t\t\t           ▒▒▒▒▒▒   █▒▒▒▒▒▒▒▒▒█▒███      █▓██            
\t\t\t\t\t             ▒▒▒▒▒▒▒█▓███▒▒▒▒▒▒▒▒       ▓████▓▓          
\t\t\t\t\t                ▓▒██▓███▒▒▒▒▒▒█        █▓▓▓▓▓▓▓▒▒▒       
\t\t\t\t\t                 ▒▒▒▒▒▓▓█                 █▓▓▒█░▒▒▒▒█    
\t\t\t\t\t               █░█▒▒▒▒▒▓█                    █▓░░█       
\t\t\t\t\t               ░░▓▓▓▒░▒█                                 
\t\t\t\t\t                     ░                                   """+Fore.RESET,"Magmar", "Fuego", "Ember", "Primera", "Zona 3", "Volcán", "Bayas", "Fuga"),
            Pokemon(Fore.LIGHTBLACK_EX+"""\t\t\t\t\t                             ░░                          
\t\t\t\t\t                              ░░░░░                      
\t\t\t\t\t                              ▒░░░░░█                    
\t\t\t\t\t                               █░░░░░░         █         
\t\t\t\t\t             ░░                 ░░█▒▒▒░       ░░▓▒░      
\t\t\t\t\t            █░░█                ░░░▒▒▒▒       █░▓█░▓     
\t\t\t\t\t      ░     ░░░░░               ░░░▒▒▒▒░     █░█▓▓▓      
\t\t\t\t\t     ░░█   ░░░░░░              ░░░░▒▒▒▒░█       ▒▓▓      
\t\t\t\t\t  █░▒▓▓▓░░  ░░░▒░░█             ░░▒▒▒▒▒░         ▒▒      
\t\t\t\t\t    ▒▓▓▓▓   ▒░░▒▒░░█░     ▒▒▒▒▒▒░░▒▒▒▒▒          ▒▒█     
\t\t\t\t\t     █▓▓█    ░░▒▒▒▒░▒█ █░░░▒▒▒▒▓▒▒▒▒▒▒▒          ▒▒▓     
\t\t\t\t\t      ▒▓▓     ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░  ▒▒▓▓▓▓▓         ▒▒▓     
\t\t\t\t\t       ▓▓▓     ▒░▒▒▒▒▒▒░░▒▒▒▒░▒▒▒▒▒▓▓▓▓▓▒▒▓      ▒▒█     
\t\t\t\t\t        █▓▓       ░▒▒▒▒▒▒▒▒██░░▒▒▒▒▓▓▓█▒▒▒▒▒▒▓▒▒▒▒▓      
\t\t\t\t\t          ▒▓█       █▒▒▒▒▒▒▓██░░█▒▓▓▓▓▒▒▒▒▒▒▒▓           
\t\t\t\t\t           ▒▓▒       ▒▒▒▒▒░███░░▒█▓▓▓▓▓▓▓▓▓▓             
\t\t\t\t\t             █▒▓▓▓▓▓▓▒▒▒▒▒░████░░█▓▓▓▓▓▓▓▓█              
\t\t\t\t\t                 ▒▓▓▓▓▒░▒▒▒░█░█▓██▓▓▓▓▓░░▒▒░▒            
\t\t\t\t\t                  █▓▓▓█▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▒▒▒▒█▒▒█           
\t\t\t\t\t                    ▒▓▓▒▓█▓▓▓▓▓▓▓▓▓▓█▒▓█▓▓▓█▓▒█          
\t\t\t\t\t                      ▒▒▒▒▓▓▓▓▓█▓▓▓▓▓▓▒▓▓▓▓▓▓▓█          
\t\t\t\t\t                    ░░▒▒▒█▒▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓           
\t\t\t\t\t                   ▒▒▒▒▒▒▓██▓▓▓▓▓▓▓▓▓▓▓   █▒▒▒           
\t\t\t\t\t                  ▒▒░░█▒▓▓▓▓   █▒▒▒▒█                    
\t\t\t\t\t                 ██▒▒▒▒█▓▓▓▓                             
\t\t\t\t\t               ▓▒▒▒▓▓▓▓▓▓▓▓                              
\t\t\t\t\t                     █▓█▒▒                               
\t\t\t\t\t                        █▒                               """+Fore.RESET,"Pinsir", "Bicho", "Insecto", "Primera", "Zona 1", "Pradera", "Hojas", "Hiper corte"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                                                      █▒ 
\t\t\t\t\t                                                     ▓▓▓ 
\t\t\t\t\t                           ▒█ ▒▓█  ██               ▓▓▓▓ 
\t\t\t\t\t                            ▓▓▓▓▓      ██          █     
\t\t\t\t\t                                         █      ▓        
\t\t\t\t\t                                          ▓   ▒          
\t\t\t\t\t                    █                     ▓ █            
\t\t\t\t\t               ▓▒▒▒▒▒▓▒▒▒░▒               ▓▒             
\t\t\t\t\t            ▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒            █  █▓      █   
\t\t\t\t\t █▒       ▒▒▒▒▒▒▒░▒▒▒▒▓▒▓▒▒▒▒▒▒▒▒        ▓ ▓          █  
\t\t\t\t\t█░▒     █▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓   █            █  
\t\t\t\t\t█▒░▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█            ▓  
\t\t\t\t\t  ▒▒▒█░░▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▓▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓          █   
\t\t\t\t\t    ▒▒▒▒▒▒▒▒▒▓█▒▒▒▒▒▒▓▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        ▓     
\t\t\t\t\t    █▒▒▒▒░▒▒▒▒▒▓▓▓▓▒▓▓▓▓▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▓▓▓█      
\t\t\t\t\t    █▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   █▒▓        
\t\t\t\t\t    ▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓   ▓         
\t\t\t\t\t    █▒▓█▒█  ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▒▒▒▒▒▒▒▓█▒▒▒▒▒             
\t\t\t\t\t             ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒██▓▒▒█▓▓    ▒▒▒▒▒            
\t\t\t\t\t             ▓▓▓▓▓▓▓▓▓█▒▒▒▒▒    █▓▓▓█    █▒▒▒█           
\t\t\t\t\t            ▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒     █▓▓▓      ▒▒▓           
\t\t\t\t\t           ▓▓▓▓     █  ▒▒▒▒      ▓▓█       █▒▒           
\t\t\t\t\t           ▓▓█         █▒▒█     ▓▓█         ▒▒           
\t\t\t\t\t           ▓▓█          ▒▒     ▓█▓          ▒▒▒          
\t\t\t\t\t            ▓▓█        █▒▒█   ███           ▓▓▓          
\t\t\t\t\t            ▓▓▓        ▒▒█                  ██           
\t\t\t\t\t                      ▓▓▓▓                               """+Fore.RESET,"Tauros", "Normal", "Toro", "Primera", "Zona 1", "Pradera", "Bayas y semillas", "Fuga"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t                                ░                        
\t\t\t\t\t                              █░░                        
\t\t\t\t\t                             ░░░░                        
\t\t\t\t\t                      █░█   ░░░░░                        
\t\t\t\t\t                       ░░░█░░░░░░                        
\t\t\t\t\t                       ░░░░░░░░░░░░░░░                   
\t\t\t\t\t                      ██░░░░░░░░░░░░█                    
\t\t\t\t\t                  ▓▒▒▒▒▒▒▒▒█░░░░▒▒▒                      
\t\t\t\t\t             █▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒█▒▓▒                        
\t\t\t\t\t           █▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒█                      
\t\t\t\t\t          ▒▒▒▒▒▒  █  ▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒                     
\t\t\t\t\t        ░░░▒▒▒▒      ░▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▓           ██▒▒▒   
\t\t\t\t\t          ▓░▒▒▒▒░░░░░▓▒▒▒▒█▓▓█████████▒      ▓▓█▒▒▒░█    
\t\t\t\t\t          ▓░█▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░█▒▒▓█  ▓▓█▒░░░░░░     
\t\t\t\t\t          █░░▒▒░░▓▒▒▒▒▓░░▓░░░░░░░▒▒▒▓▓▓▓▓▓▓▒░░░░▓███     
\t\t\t\t\t         ▒▒░▓▒▒▒▒░█▒▒▓▒░░░░░░░░▓▒▒▓▓█▓▓▓▓░░░░░░░░░█      
\t\t\t\t\t         ▓█▓█▓▓▒▒▒░▒▒▒▒▓░░░░░░▓▓▓▓▓▓▓▓▓▓░░░░░░░░░        
\t\t\t\t\t         █  ▓▓▓▓▓▓░▓▓▓▓▓▓█▒░░░▓▓▓▓▓█▓▓▓▓░░░░░░░█         
\t\t\t\t\t         ▒    ▓▓▓▓▒█▓▓▓▓▓▓▓▓▓░▓▓▓▓█▓▓ ▓█░░░░░░░          
\t\t\t\t\t          ▒      █▒█▓▓█▓▓█▓▓▓▓▓▓▓█    ▓▓░░█░░░░          
\t\t\t\t\t           ▓      ▒▒▓▓▓▓▓▓▓▓▓          ▓▓░░░░░░          
\t\t\t\t\t            █     █▒▒▒▒▒▒▒▒▒▒▒█         ▓░░░░░           
\t\t\t\t\t            █     ▒▒░▒▒▒▒▒▒▒░░░░         ▒░░░            
\t\t\t\t\t             ▒      ▒█  █░░░ ▓░░░         ▒█             
\t\t\t\t\t             ░       ▒█   ▒█                             
\t\t\t\t\t             ░        █░                                 
\t\t\t\t\t                        █░█                              
\t\t\t\t\t                            ░░                           """+Fore.RESET,"Magikarp", "Agua", "Pez", "Primera", "Zona 2", "Río", "Peces y algas", "Entorno húmedo"),
            Pokemon(Fore.LIGHTBLUE_EX+"""\t\t\t\t\t                         ░                               
\t\t\t\t\t                        ▓▒ █                             
\t\t\t\t\t                      ▒ ▒▒░                              
\t\t\t\t\t               ▓      ▓▒▒▒▒                              
\t\t\t\t\t        ▓     ▓       ░▒▒▒▒▒▒      ░                     
\t\t\t\t\t         ▒  ▓▒▓▒▓▒▓▓▒▒▒▒▓▓▒▒▓▒▒█ ░▓                      
\t\t\t\t\t        ▒ ▒▓▒▓▓▒▒▒█▒▓▒▒▒▓▓▒▒▒▒▒▓░                        
\t\t\t\t\t        ▒▒█▒▓▓▓█▒▒▓▓▓▓▓▓▓▓▒▓▓▒▒▒▒▓                       
\t\t\t\t\t        ▒▒▒░▒▒░▓▓▒▓██▒▒░░▓▒▒▒▒▓▓            ▒            
\t\t\t\t\t         ▒█░░▒▒▒▓▒█▓▒▒░░░▓▒▒▒▓▒▒       ▓  ░▒▒▒           
\t\t\t\t\t         ▓▒███▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒       ░█▒▒▒█            
\t\t\t\t\t          ███▒▓▓▓██▓ ▓▒ █▒▒▒▒▓█▒       ▒▒▒▒▒▒            
\t\t\t\t\t           █▒▒▒▒█   ▒  ▓░▒▒▒▒▒▒▓    ▓▒█▓▓▓▓              
\t\t\t\t\t          █▒▒▒▒█    ▓  ░░▒▒▒▒▓▒▒  ▓▒▒▓▓▓█▒▒▓             
\t\t\t\t\t          ░░█▒▒     ▒  ░▒▒▒▒▒▓▒   ▓█▓▒▒▓▓▓▓▓▓▓ ▒▒        
\t\t\t\t\t          ░         ▓ ░░▒▒▒▒▒▒▒ ▒▒▓▓▓██▓▒▒▓█▓▓▒▒▓        
\t\t\t\t\t         ▓ ▓       ▓  ░░▒▒▒▒▒▓▓▒▓▓█▒█▓█▒  ▓▒█▓▒▒         
\t\t\t\t\t                   ▓ ▓░░▒▒▒▒▓▒▒▓▓▓▓▒▓▒     ▒▒▒           
\t\t\t\t\t                     ░░░▒▒▒▒▓█▓▒▒▓▓▓▒      ░▒▓           
\t\t\t\t\t                      ░▒▒▒▒▒█▒██▓▓▒▒       ▒▒▓           
\t\t\t\t\t                       ▒▒▒▒▒▓██▒▒▒        ▒▒▓            
\t\t\t\t\t                          ▓▓▒▒▒▒        ▓▒▓▒▓▓           
\t\t\t\t\t                                      ▓▒▒▒▒▒▒            
\t\t\t\t\t                                    ▓▒▒▒▒▒▒▒▒            
\t\t\t\t\t                                        █ ▒▒▒            
\t\t\t\t\t                                           ▓             """+Fore.RESET,"Gyarados", "Agua", "Atrocidad", "Primera", "Zona 2", "Mar", "Peces y algas", "Entorno húmedo"),
            Pokemon(Fore.LIGHTBLUE_EX+"""\t\t\t\t\t                      ▒▒▒▒▓   █▒▓                        
\t\t\t\t\t                    ░ ▒▓▒▒▒▒▓░▒▒▒▒▒                      
\t\t\t\t\t                    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                     
\t\t\t\t\t                   █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                      
\t\t\t\t\t                  ▒▒▒▒▒█▒█░▓▒▒▒▒                         
\t\t\t\t\t                  ▒▒▒▒▒▒▒▒▒▒▓▒▒▓                         
\t\t\t\t\t                   █░░░░░░░░░▓▒█                         
\t\t\t\t\t                         ░▒▒▒▓▒                          
\t\t\t\t\t                         ░▓▒▒▒                           
\t\t\t\t\t                        ░▒▒▒▒▒                           
\t\t\t\t\t                       ░░▒▒▒▒                            
\t\t\t\t\t                      ░░▒▒▒▒▒   ▒░█                      
\t\t\t\t\t                     ░░▒▒█░░▒▒▒▒▒▒█                      
\t\t\t\t\t                    ░▒▒█░░▒▒▒▒▒▒▒▒▒▒ █▒                  
\t\t\t\t\t                   ░▒░█▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒                  
\t\t\t\t\t                  ░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒                
\t\t\t\t\t                 ░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒             
\t\t\t\t\t                ▒▓█▒░▒▒▒▒▒░▒▒░░▒░▒▒▒▒▒▒▒▒▒▒▒             
\t\t\t\t\t                ▒▒▒░▒▒░░░▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒              
\t\t\t\t\t                ▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█             
\t\t\t\t\t        █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓       
\t\t\t\t\t      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒█    
\t\t\t\t\t    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒░░░▒█    
\t\t\t\t\t   ▒▒▒▒▒▒▒▒▒▒▒░░▒     ▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓█▓▒▒▒▒▓▒▒▒▒      
\t\t\t\t\t   ▒█               ▒▒▒▒▒▒▒▒▒▒▒▒░░░▒▒▒▓▓▒▒█ █░░░▒▒▒▒█    
\t\t\t\t\t                    ▒▒▒░░▒▒░░█        █▒▓▒▒              """+Fore.RESET,"Lapras", "Agua", "Transporte", "Primera", "Zona 2", "Mar", "Peces y algas", "Entorno húmedo"),
            Pokemon(Fore.MAGENTA+"""\t\t\t\t\t                       ░░░░░░░██  ██▓▒█                  
\t\t\t\t\t                    █░░░░░░░░░░░░░░░░░░░░                
\t\t\t\t\t         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░               
\t\t\t\t\t        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓              
\t\t\t\t\t        ░░░░░░░░░░░░░░░░▒█░░░░░░█░░░░░░░░░░█             
\t\t\t\t\t        █░░░░░░░░░░░░░░░░░░░█░░▒▒▒▒░░░░░░░░░▒            
\t\t\t\t\t         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒          
\t\t\t\t\t          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█      
\t\t\t\t\t          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█    
\t\t\t\t\t          ▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█   
\t\t\t\t\t         █▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    
\t\t\t\t\t         ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      
\t\t\t\t\t        ▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░       
\t\t\t\t\t      █▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█       
\t\t\t\t\t     ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒       
\t\t\t\t\t   █▒▒▒▒▒▒▒▒░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▓      
\t\t\t\t\t  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒     
\t\t\t\t\t ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█   
\t\t\t\t\t█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  
\t\t\t\t\t█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 
\t\t\t\t\t █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
\t\t\t\t\t   █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 
\t\t\t\t\t              █▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█ 
\t\t\t\t\t                  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███        ████   
\t\t\t\t\t                       ██▒▒▒▒▒▒▒██                       """+Fore.RESET,"Ditto", "Normal", "Transformación", "Primera", "Zona 1", "Pradera", "Bayas y semillas", "Transformación"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t         ▒█                                              
\t\t\t\t\t        ██▓▒                                             
\t\t\t\t\t        ▒███▒                                            
\t\t\t\t\t        ▒▓▓▓█▒                                           
\t\t\t\t\t        █▓▓▓▓▓█                                          
\t\t\t\t\t         ▒█▓▓█▒                             █            
\t\t\t\t\t         █▒█████  █░  ░           █▒▒▒█████▒             
\t\t\t\t\t           ▒███▒░▒▒▒▒▒▒▒▒▒▓   █▒███▓▓▓▓▓▓▒               
\t\t\t\t\t            ▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█████▓▓▓▓▒█      ░         
\t\t\t\t\t             █▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▒▒       ░░░█        
\t\t\t\t\t             ▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█      █░░░░░░░        
\t\t\t\t\t             ▒███▒▒▒▒▒▒▒█ █▒▒▒     ▓▓▓▓▓▓▒▒▒▓░░░░        
\t\t\t\t\t             ▒███▒▒▒▒▒▒▒███▒▒    ▓▓▓▓▓▓▓▓▓▓▓▓░░░░        
\t\t\t\t\t           ░▒▒▒▒▒▒▒▒▒▒▒███▒▒▒   ▓▓▓▓▓▓▓▓▓▓▓▓▓░▒░         
\t\t\t\t\t         █░░░▒▒▒▒█▒▒▒▒▒▒▒▒▒▒░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         
\t\t\t\t\t        █░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█         
\t\t\t\t\t        ░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓█          
\t\t\t\t\t         █░░░░░░░░░░░░▒▒▒░▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓            
\t\t\t\t\t           ▒░░░░░░░░░░░▒▒▒▒▒▒▒█▒▒▒▒▓▓▓▓▓▓▓▓              
\t\t\t\t\t             ▒░░░░░░░░▒▒▒▒▒▒█▒▒▒▒▒▒█                     
\t\t\t\t\t              █▒▒▒▒▒░▒▒▒█▒▒▒▒▒▒▒▒▒▒                      
\t\t\t\t\t              █▒▒▓░░▒▒█▒▒▒▒▓▓█▒▒▒▒▒                      
\t\t\t\t\t               ▒▒▒▒▓▒▒▒▒▒█▓▓█ █▒▒▒▒                      
\t\t\t\t\t                ▒▒▒▒▒▒▒▒▒▓▓█  ▒▒▒▒                       
\t\t\t\t\t               █▒▒▒█▒▒▒▒▓▓   ▒▒▒▒█                       
\t\t\t\t\t               █▒▒▒▒▒▒▒█                                 """+Fore.RESET,"Eevee", "Normal", "Evolución", "Primera", "Zona 1", "Pradera", "Bayas y semillas", "Adaptable"),
            Pokemon(Fore.LIGHTBLUE_EX+"""\t\t\t\t\t                         ▓                               
\t\t\t\t\t                         ██                  ▓█          
\t\t\t\t\t                          ▓              █▓▒░░           
\t\t\t\t\t                          ▓▓           ▓█▒░░░▓           
\t\t\t\t\t                         ░░▓▒░░░░██  ▓█▒░░░▒             
\t\t\t\t\t                      ▓░░░▓▓▓▓▓▓▓█░▓▓▒▒░▒▒░              
\t\t\t\t\t         ▒█▓███      ░░░▒░░█▓█▒▒▒▒▓▓▒▒▒▒░░▓              
\t\t\t\t\t           ░░░░░░░▒█▓▓▓▓░░▒▒▒▒▒▒██▒▓▒▒▒▓▒░█              
\t\t\t\t\t            █▒▒▒▒▒▒▒▓▒▒▒███▒▒▒▒▒█▓▓▒▒▒░░░░▓              
\t\t\t\t\t               ░░░░▒▒▒▒█▒█▒▒▒▒▒▒▒▒▒▒░░░░█                
\t\t\t\t\t                 ░░░░░▒░▒▒▒▒▒▓▓▓▒▒▒▓░░░░                 
\t\t\t\t\t                  ░░▒░░░░▒▒▒▒▒█▒▒▓█░░░░░                 
\t\t\t\t\t                    ░░░░░░░░░░░░█░░░░░█                  
\t\t\t\t\t                       ░░░░░░░░░░▒░░▒                    
\t\t\t\t\t                     ▓▓░░▒▓░▒░░██▒▒                      
\t\t\t\t\t                    ▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓                      
\t\t\t\t\t               ▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                     
\t\t\t\t\t           █▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▓        █▒░░▓        
\t\t\t\t\t          ▓█▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      █░░░░░░░░░░█    
\t\t\t\t\t        █▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓▓▓█▓▒▒▒▒▓▓▒░░░░░░░▒      
\t\t\t\t\t        ▓▓▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒   ▒▒▒▒▒█▒█         
\t\t\t\t\t        ▓█▒▒▒▒▒▒▒▒▒▒▒▒█▓▓█▒▒▒▒▒▒▒▓      ▒▒▒▒▒▒▒          
\t\t\t\t\t        ▒█▓▓▒█▒▒▓█▓▓▓▓▓▒▒▒▒▒▒▒█▓▓█      █▒▒▒▒▒▒▒         
\t\t\t\t\t        ▒▒▒▒▒███▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓        █▒▒▒▒▒▒         
\t\t\t\t\t         ▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒ █▓▓▓▓▓           ▓▒▒▒▓        
\t\t\t\t\t           █▒▒▒▒▒▒▒▒▒▒▓     ▒▒▒▒▒              ▒▓        """+Fore.RESET,"Vaporeon", "Agua", "Burbuja", "Primera", "Zona 2", "Mar", "Peces y algas", "Absorber"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                         █░░░                            
\t\t\t\t\t                     █▒░░▒▒█                             
\t\t\t\t\t                  █▒▒▒▒▒▒▒█                              
\t\t\t\t\t                █▒▒▒▒▒▒▒▒▒ █░░░▓██░░                     
\t\t\t\t\t               ▓▒▒▓▒▒▒░░▓███████░░                       
\t\t\t\t\t              ▒░░░▒▓░█████████░░                         
\t\t\t\t\t          █░░░░░░░░█▒██████░░░░█                         
\t\t\t\t\t         ░░░░░░░░░░░░░▒██                                
\t\t\t\t\t       ░░░░████░░░▒▒▒▒▒        █░░                       
\t\t\t\t\t       ░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░    █ ▒      ░██          
\t\t\t\t\t        █▒▒▓▒▒▒▒▒▒▒▒▒▒▒░░░░░░░█  █▒▒▒█  █░░░░            
\t\t\t\t\t           ▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░█▒░░░░░░█             
\t\t\t\t\t          ░░░▒░▒░░░░░░░░░░░░▓░░░░░░░░░░░█▓░░░░░░░        
\t\t\t\t\t            ░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░█           
\t\t\t\t\t            ░░▓░░░░░░░░▓░░░▒░░░░░░░░░░░░░░░█             
\t\t\t\t\t           ░░░▒░░░░░░░░ ░░▓░ ░░░░░░░░░░░░░▒███           
\t\t\t\t\t          █ █ ▒░░░░░░░░░░░░░░░░░░▓░█░░░░░░░░             
\t\t\t\t\t          █   ▒█ █░░░░░░█░░░░░░░░░░▒▒▒░░█░░▒█            
\t\t\t\t\t              █▒░█░░░░░▒▒█     ▒▒▒░░░░░░░                
\t\t\t\t\t               ▒▒▒░░░░          ▒▒█░░░░░░█               
\t\t\t\t\t               ▒▒▒░░░░          █▒▒▒░░░░▒▒               
\t\t\t\t\t               █░░░░░          █▒▒▒    ▒▒▒▒█             
\t\t\t\t\t               █░▒░░░         ▒▒▒█      ▒▒▒▒             
\t\t\t\t\t               ░░░░░▓       ▒▒▒▓       ▒▒▒▒              
\t\t\t\t\t              ░░░░░░                 ▒▒▒▒█               
\t\t\t\t\t              ▓█░░░█                █▒▒▒                 """+Fore.RESET,"Jolteon", "Eléctrico", "Espinas", "Primera", "Zona 2", "Montaña", "Electricidad", "Absorber"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t                                                  █      
\t\t\t\t\t                █▓                                 ░░    
\t\t\t\t\t              █▓▓▓                                  ░░   
\t\t\t\t\t             ▓▓▓▓                                  █░░█  
\t\t\t\t\t          █▓▓▓▓▓▓                  ░░  ██          ░░░░  
\t\t\t\t\t          ▓▓▓▓▓▓█             ░░█ ░░░█░░░░░░░░█ █▓░░░░░  
\t\t\t\t\t         █▓▓▓█▓▓          █▒▒▒▒█░█░░░░░░░░░░░░░░░░░░░░   
\t\t\t\t\t        █▓▓▓▓▒░█     ▒▒▒▒▓████▓▒░░░░░░░░░░░░░░░░░░░░░██  
\t\t\t\t\t        ▓█░░░░░░███▒▒▒███████▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒    
\t\t\t\t\t      ░░░░░░░░░░▒█▒████████▓▒▒▒▒▒▒▒░░░░░░░░░░░░░░░▒▒     
\t\t\t\t\t     ░░░░░░░░░▒▓▒█████████▒▒▓▒▓█▒▒▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒     
\t\t\t\t\t     ░░░░░░░░▒▒▒█▒█████▓▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█     
\t\t\t\t\t     ▒░░░▒▒▒▒▒▒▒▒▒██▓░░░░░░░█▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒██   
\t\t\t\t\t    █▒▒▒██▒▒▒▒▒▒▒▒▒▓▒░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒█    
\t\t\t\t\t    █▒▒▒▒▒███░▒▒▓▓▓▒▒░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒      
\t\t\t\t\t    ▓▒▒▒▒▒███▓▓▓▓▓▓▒░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t      █▒▒▓▓▓▓▓▓▓█▒▒░░▒▒▒░░▒▒▓▒▒▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒         
\t\t\t\t\t       ▒░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░▒█▓▓█▒▒▒▒▒▓▓▓▓▒▓█             
\t\t\t\t\t       ▒░░░░░░░░░░░░▒▒░░░▒▓▓▓▓█  ▓▓▓▓▓▓▓▒▓▓▓▓            
\t\t\t\t\t         ░░░▓░░░░░░░░░░░▒▓▓▓▓█          ▓▒▓▓▓            
\t\t\t\t\t       █▓▓▓█▒░░░░░▒▒▒▒▒▓▓▓▓▓▓▒▒        ▓▓▓▓▓             
\t\t\t\t\t     █▒▒▒▒▓▓█ ██▒▒█      ▓▓▓▓▓▒       ▒▒▓▓▓              
\t\t\t\t\t  ▒▒▒▒▒▒▒▒              ▒▒▒▒▒▒      ██▒▒▒▒               
\t\t\t\t\t  ▒▒▒▒▒█              █▒▒▒▒▒▓         ██                 
\t\t\t\t\t                    █▓▒▒▒▒▒                              
\t\t\t\t\t                     █▒█▓█                               """+Fore.RESET,"Flareon", "Fuego", "Llama", "Primera", "Zona 3", "Volcán", "Bayas", "Absorber"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t                                           █░█           
\t\t\t\t\t                                           ░▓▓           
\t\t\t\t\t                   ░░░░░░░░▓              ░░▓▓           
\t\t\t\t\t                ░░░░░░░░░░▓▒▒█            ░░▓▓           
\t\t\t\t\t              ░░░░█░░░░░░▒▒▒▒▒▒          ░░█▓█           
\t\t\t\t\t            █░░░░░░░░░█▒░▓▒▒▒▒▒▒▓       █░░▓▓█           
\t\t\t\t\t           █░░░░░░░░░░░░░░░▓▓▓▓▓█       ░░░▓▓            
\t\t\t\t\t          ▒░░░░░░░░█░░██░░▒▓▓▓▓▓       █░░█▓▓            
\t\t\t\t\t         ░░░░░░░░░░░░░░░▒▒▒▓▓▓▓█       ░▒▒▓▓▓            
\t\t\t\t\t        ░░░░░░░░░░▒▒░░▒▒▒▒▓▓▓▓▓       ▒▒▒▒▓▓▓            
\t\t\t\t\t       ░░█░░░░░▒█▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒░░█▒▒▒▒▒▓▓▓▓            
\t\t\t\t\t      █░░░░░░░░█▒▒█▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓█            
\t\t\t\t\t      ░░░░░░░░▒▒██▓▓▓▓▓▓▓█▒▒▒█▓▒▒▒▒▒▒▒▒▒▒▒▓▓█            
\t\t\t\t\t      ░░░░░░░▒▒▓▓▓▓▓▓▓█▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒█▓▓▓             
\t\t\t\t\t     ▒░░░░░░▒▓▓▓▓█▓░▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██▒▓▒▒▒▒▒█        
\t\t\t\t\t      █░░░█▓▓█ ▓▓▒█░░░▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▓░░░▓▒▒▒▒▒▒▒▒▒█     
\t\t\t\t\t              █▒▒▓░░░░░░▒▒▒▒▒▒▒▒█▒▒▒▓▓░░░░░░░▒▒▒▒▓▓▓     
\t\t\t\t\t              ▓▓▓░░░░░░░░░▒▒▒▒▒▒▒▒█▓▓█░░░░░░░░░▓▓▓▓▓     
\t\t\t\t\t              ▓▒▒█▓▒░░░░░░░▒▒▒▓▓▒▓▓▓▓░░░░░░░░░▓▓▓▓▓      
\t\t\t\t\t              ▒▒▒▒▒▓█▓▓▓▓▓▓▓▓███▓▓▓▓▓░░░░░░░░░▓▓▓▓       
\t\t\t\t\t                 ██▓█  █▓▓▓▓▓▓▓▓▓▓▓▓█░░░░░░░░▓▓▓▓█       
\t\t\t\t\t                           ▓▓▓▓▓▒▓▓█▒░░░▒▒▒▒▒▓▓▓█        
\t\t\t\t\t                                █▓█ ▒▒▒▒▒▒▒▒█▓▓█         
\t\t\t\t\t                                   █▒▒▒▒▒▒▒▒▓▓▓          
\t\t\t\t\t                                    █▓▓█▒▒▒█▓▓           
\t\t\t\t\t                                        █▓▓▓▓            """+Fore.RESET,"Porygon", "Normal", "Virtual", "Primera", "Zona 3", "Ciudad", "Datos", "Adaptabilidad"),
            Pokemon(Fore.LIGHTCYAN_EX+"""\t\t\t\t\t                   █░░░░░░░██                            
\t\t\t\t\t               ▓░░░█░░░░░░░░░░░░█                        
\t\t\t\t\t             ░░░█░░░░░░░░░░░░░░░░░▒█                     
\t\t\t\t\t           ░░░░░░░░░░░░█░░░░░░░░░░░▒█                    
\t\t\t\t\t          █░░░█░░░░█░░░░░░░░░░░░░░░░▒▒█                  
\t\t\t\t\t         ░█░░░▒░░░░░░░░░░░░░░░░░░░░░░▒▒█                 
\t\t\t\t\t        ▓░░█▒░░░░█░░░░░░▓░░░░░░░░░░░░░▒▒▓                
\t\t\t\t\t        ░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒█               
\t\t\t\t\t       █░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒               
\t\t\t\t\t       ░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒              
\t\t\t\t\t       ░░░░░░░░░▒░░░█░▒░░░░░░░░░░░░░░░░▒▒▒█              
\t\t\t\t\t       ░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒              
\t\t\t\t\t       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█             
\t\t\t\t\t       ░░░█░░▓░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█             
\t\t\t\t\t       █░░▒░░░░░░░░░█░█░░░░░░░░░░░░░░░▒▒▒▒█▓             
\t\t\t\t\t        █░░█░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒             
\t\t\t\t\t        █░░░█▒▒░░░█░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒   ▒▒█       
\t\t\t\t\t         ▒░░░░░░░░▒░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▓▓░█▒▒▒█ █▒▒▒      
\t\t\t\t\t          ██░░▒░░░░░░░▒██░░▓▓▓░▒▒▒▒▒█░▓▓▓░▒▒█▒ █▒▒▒▒     
\t\t\t\t\t            ░░▒░░░░░▒▒██░░▓▓▓██▒█▓▓█░▓▓▓███▒█▒ ▓▒▒▒▒█    
\t\t\t\t\t              ▒▒░░░░░░█▓░░█████▒▒▒▓▓█▒████▒▒██▓▓▓▓▒▒█    
\t\t\t\t\t              █▒▒░░░░░░▒▒█▒▒▒▒█▒▒▒▒▓▓▓█▒▒▒▓▓▓▓▓▓▓▓▓▓     
\t\t\t\t\t             █▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      
\t\t\t\t\t           █▒▒▓▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓█        
\t\t\t\t\t             █▓▓▓▓▓█░░▒▒▒█▒░▒▒▒▒▒▒▒▓▓▓▓█▓▓▓█▓▓▓▓▓█       
\t\t\t\t\t               █░░░░░▒▒▒░░░░▒█░░▒▒█▓▓▓▓▓▓▓▓▒▒▓           
\t\t\t\t\t                     █░░░░▒▓▓░░░▓█  █▓▓▒▒██▓▒▒█          
\t\t\t\t\t                           █▒▒▓█       █▓▓               """+Fore.RESET,"Omanyte", "Roca", "Espejo", "Primera", "Zona 2", "Mar", "Algas", "Caparazón"),
            Pokemon(Fore.LIGHTCYAN_EX+"""\t\t\t\t\t                         ░         ░▓                    
\t\t\t\t\t                         ▒░░      ░▒▒                    
\t\t\t\t\t                         █░▒░▓░░█░░░░█                   
\t\t\t\t\t                       █░█░▒▒▒░░░░░░░░░░░                
\t\t\t\t\t                     █░░░░░░░░░░░░░░░░░░░░░              
\t\t\t\t\t                  ▓░█░░░░░░░░░░░░░░░░░░░█░░▒▒            
\t\t\t\t\t                  ░█░░░░▓░░░░░░░░░░░░░░░░█░░▒▒█▓         
\t\t\t\t\t                 ▒░░█░▒▒▒▒░░░░░░░░▒▒▒░░░░░░░▒▒██         
\t\t\t\t\t                █░░░░░░▒▒▒░░░░░░░▒░▒▒▓░░░░░▒▒▒▓▒         
\t\t\t\t\t                ▒░░░░░░░░░░░░░░░░▒▒▒▒░▒▓▒░█▒▒▓▒▒▓        
\t\t\t\t\t █             █░░█░░░░░░░░░░░░░█░▒▒▒█░░▒▒▒█▓▓▓▓▓ █▒▒    
\t\t\t\t\t ▒▒     ▒░░    ▒░░░░░░░░░░░░░░░░▒▒▒▒▒░░▒█▓▓▓▓▓█▓▓▒▒█     
\t\t\t\t\t  ▒▓     █░░   ░░░░░░░░░░░░░░░░░▒▒▒▒░░░▒█▓▓▓█▓▓▓▒▒█      
\t\t\t\t\t  ▒▓      ▒░░  ▒▒░░█░▒░░░▒░░██▒█▒░░█░░░▒▓▓▓▓▓▓▓▓▓▒       
\t\t\t\t\t  ▒█     █▒░░ ░░░░░░░░▒▒▓░░░░░░▒▒▒░█░░░░▒▓▓▓▓▓▓▓▓▓       
\t\t\t\t\t █▒█     █▒░░█░░▒░░░█░░░░░░░░▒░░░▒▒░░░░░░▒▓▓█▒▒█▓▓       
\t\t\t\t\t █▒▒     ▒▒░░░░░░█░░░█░░░▒█░░█░░░█░░░░░░░▒█▓▓▒█▓▓▓       
\t\t\t\t\t  ▒▒█    ▒▒░░░░░░██░▒▒▒▒▒▒▒▒▒█▓▒▒░░░░░░░░▒▓▓▒▓▓▓▓        
\t\t\t\t\t  █▒▒▓   ▒▒░░░░░░▒▒▒▒▒███░░█▒▒▒░░░░░░░░░▒▒▓▓▓▓▓█         
\t\t\t\t\t    ▓▓▓▓██▒▒░░░░░░▒░░███░░░░░█░░░░░░░░▒▒▓▓▓▓█            
\t\t\t\t\t        ███▒▒▒░░░░░░░██░░░░░░▒█░░░░▒▒▓▓█▓▓▓█             
\t\t\t\t\t         █▓▓▓█▒▒▒▒░████░█████▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓█       ▒█
\t\t\t\t\t ▒      ▓▓█ ▓▓▓▓▓▓▓▓▒▒██▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓█  █▓▓▓▓▓▒▒▒▒█ 
\t\t\t\t\t ▒▒█ █▒▒▒ █▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒ ▓▓▓     █▒▒█    
\t\t\t\t\t   ███    ▓██▒▒▓▓▓▓█           ██▓▓▓▓▒▒▒▒  █▓▒▓          
\t\t\t\t\t             ██                      █▓▓▓                """+Fore.RESET,"Omastar", "Roca", "Espejo", "Primera", "Zona 2", "Mar", "Algas", "Caparazón"),
            Pokemon(Fore.LIGHTBLACK_EX+"""\t\t\t\t\t                         ████                            
\t\t\t\t\t                 ██▒▒▒▒▒▒▒░▒▒▒▒▒▒█▓▒█                    
\t\t\t\t\t            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒█                
\t\t\t\t\t         ██▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█             
\t\t\t\t\t       ██▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒           
\t\t\t\t\t     █▒▒▒░░░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓         
\t\t\t\t\t    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█       
\t\t\t\t\t  █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓█████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒      
\t\t\t\t\t █▒▒▒▒▒████▓▓▒▒▒▒▒▓▓▓▓▓▓▓███████████▓▒▒▒▒▒▒▒▒▒▒▒▒█▒▒     
\t\t\t\t\t ▓▒▓▓███████████▓▓▓▓▓███████▒▒▒███████▓▒▒▒▒▒▒▒▒▒▒▒█▒▒    
\t\t\t\t\t ▒▓▓▓███████▒▒▒██████████▓▒▒▒▒▒▒░███████▒▒▒▒▒▒▒▒▒▒▒▓▒▒   
\t\t\t\t\t ▓▓▓▓█████░▒▒▒▒▒░████████░▒▒▒▒▒▒▒▒█████████▓▓▓▓▓▓▓▓▓▓██  
\t\t\t\t\t ▒▒▓▓█████▒▒▒▒▒▒▒▓███████▒▒▒▒▒▒▒▒█████████████▓▓▓▓▓▓▓▓▓  
\t\t\t\t\t  ▒▓▓▓████▒▒▒▒▒▒░██████████▒░░░▒█████████████████▓▓▓▓▓▒█ 
\t\t\t\t\t    █▓▓█████▓▓▓████████████████████████▒▒▒▒▒██████▓▓▓▓▒▓ 
\t\t\t\t\t     █▒▒▒████████████████████████████▒▒▒▒▒▒▒▓▓▓▓█▓▓█▓▓▒▓ 
\t\t\t\t\t    █▒▒░▒▒▒██████████████████████████▒▒▒▒▒▒▒▒▒▓▓▓█▓▓▓▓▒█ 
\t\t\t\t\t    ░░░░░░░▓█▓████████████████████████▒░░░░░░█▓▓▓▒▓▓▓▓▒  
\t\t\t\t\t    ▓░░░░░░▒█▓▓▓▓▓████████████████████░░░░░░░▒▒▒▒▒   █   
\t\t\t\t\t    █░░░░░░░░░░▒▓▓█ ▒▒█▓▓▓▓▓█       █░░░░░░░▓▒▒▒▓        
\t\t\t\t\t      █░░░░░▒▒█▓▓▒▒▒▒█         █░░░░░░░░░░█▒▒▒▒█         
\t\t\t\t\t         ███   █████             █░░░░░░█                """+Fore.RESET,"Kabuto", "Roca", "Concha", "Primera", "Zona 2", "Mar", "Algas", "Caparazón"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                    █                                    
\t\t\t\t\t                  ▒▒                                     
\t\t\t\t\t                 ▒▒██                                    
\t\t\t\t\t               █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█  █▒▒▒▒▒█                
\t\t\t\t\t               ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒                  
\t\t\t\t\t              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▓                   
\t\t\t\t\t              ▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▓                     
\t\t\t\t\t              ▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▓▓▓▓▓█▓         ░█          
\t\t\t\t\t               ▒▒▒▒▒▒▒▓█░▓▓▓▓▓▓▓█▓█ █       ░▒░          
\t\t\t\t\t       █░░█     ▓▒▒▒▓█▓▒▓▓▓▓▓▓▓█▓▓▓▓       ░█░░░         
\t\t\t\t\t       ░░▒ █▒▒█  █▓▓▓█▓███▓▓▓▓▓▓██▓▓▓▒▒ █░▒██░░░▓        
\t\t\t\t\t      ░░░░█    █▓█     ▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓█    █░░░█        
\t\t\t\t\t     ░░░░░               ░░░░░░░▒█▓▓▓▓▓▓▓█   ░░░░░       
\t\t\t\t\t    █▒░░░              █▒▒▒█░░░░▒▒▒▒▓█▓▓ ██  █░░░░       
\t\t\t\t\t    █░░░             ▒▒▒▒▒▒██░░░▒▒▒▒▓▓▓▓██    ░░░░       
\t\t\t\t\t    ▒░░░           ▒▒▒▒▒▒▒▓▓██░▒█▒▒▒▒▓▓▓██    ░░▓█       
\t\t\t\t\t    █░░░          █▒▒▒▒▓▓▓       ▒▒▒▒▓█▓▓█    ░░░        
\t\t\t\t\t     █░░          ▓███           ▒▒▒▒▓█▓▓▓▓  ░░▓         
\t\t\t\t\t      ▓░░          ▓▓█           █▒▒▓█  █▓▓▓█░░█         
\t\t\t\t\t       ░░▒           ▓▓             ▓▓▓    ▓░▒█          
\t\t\t\t\t         █▒          █▓▓█             ▓▓▓█ ░▒▓▓          
\t\t\t\t\t                     █▓▓               ▓▓▓░░   ▓         
\t\t\t\t\t             █░░▒▓▓▓▓▓▓▓                ▓▓▓█             
\t\t\t\t\t               █░▒█                     █▓▓              
\t\t\t\t\t               █                        █▒▒█             
\t\t\t\t\t                                       ▓█▒▒░             
\t\t\t\t\t                                     ░▒▒█▓▓░░            
\t\t\t\t\t                                            █            """+Fore.RESET,"Kabutops", "Roca", "Concha", "Primera", "Zona 2", "Mar", "Algas", "Caparazón"),
            Pokemon(Fore.LIGHTMAGENTA_EX+"""\t\t\t\t\t                                      ░                  
\t\t\t\t\t       ░     ░░                       ▒█░                
\t\t\t\t\t    ███▒▒   █░▒▒▒█░░                ░▒▒▒▓▓▓▓▒▒▒▒▒▒▒█▒    
\t\t\t\t\t     ░█▓▓█  █▒█▓▒▒▒▒░▒▒▒             ░▒▓▒▒▒▒▒▒▒▒▒▒█      
\t\t\t\t\t   █▓▒▒▒▒▓▒    ▓▓▓▒▒▒▒▒             ░▓▓▒▒▒▒▒▒▒▒          
\t\t\t\t\t ░▒▒▒▒▒▒▒▒▒▒█   ▒▓▓█▒██            █▓▒▒▒▒▒▒▒▒            
\t\t\t\t\t          ▒▒▒▒ █▒▒▒▒▒▓▒            ▒▓▒▒▒▒▒▒▓             
\t\t\t\t\t           ▓▒▓█▒░▒░█▒▒░  ▒       ░░██▒▒▒▒▒█              
\t\t\t\t\t             █░░░█▒ ▒░░░█▒▒   ░▓▓▓▒▒▓▓▓▓▓██              
\t\t\t\t\t            █▓▒██▒▓▓▓░░░░░░░▒▓▓▓▓▓                       
\t\t\t\t\t             █▒▒▒  ▓░░░░░░░░▓▓▓               █▒░░░░     
\t\t\t\t\t                    ░░░░░░░░░░░             █▒▒ ▒▒       
\t\t\t\t\t                    ░░░░░░░░░░▒█        ▓▒▒▒             
\t\t\t\t\t                    ▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒                
\t\t\t\t\t                    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                   
\t\t\t\t\t                    ▒▒▒█    █▒▒▒▒                        
\t\t\t\t\t                     ▒█▒       ▒▒▒                       
\t\t\t\t\t                               ▒ ▒                       
\t\t\t\t\t                                ▒                        """+Fore.RESET,"Aerodactyl", "Roca", "Fósil", "Primera", "Zona 2", "Montaña", "Minerales", "Presión"),
            Pokemon(Fore.LIGHTWHITE_EX+"""\t\t\t\t\t                     ▒▒▓▓           █▒▒                  
\t\t\t\t\t                    ▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓                  
\t\t\t\t\t                    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓                  
\t\t\t\t\t                   ▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▓▓                  
\t\t\t\t\t                 █▓▒▒░░░░░▓▒▓█░░░░░▓▓▓▓█▓█               
\t\t\t\t\t              ▒▒▒▒▒█░░░░░░░░░░░░░░░░█▓▓▓▓▓▓▓▓            
\t\t\t\t\t           ▒▒▒▒▒▒▒█▒░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▒▒▒█         
\t\t\t\t\t         ▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▒▒▒▒▒▒█       
\t\t\t\t\t       █▓▒▒▒▒▒▒▒▒▓▓▓▓▓░░░░░░░░▒░░░░▓█▓▓▓▓▓▒▒▒▒▒▒▒▒▒      
\t\t\t\t\t      ▓▓▓▓▓▓▓▓▓▓▓▓█░░░░░▒▒█▓░░░█▒▒▒▒▒▒░▓▓▓▓▓▓▒▒▒▒▒▒▒▒    
\t\t\t\t\t     ▒▓▓▓▓▓▓▓█▓▓░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓   
\t\t\t\t\t      █░ █ ▓▓▓█░░░░░░░░░░░░░░░░░░░░░░░░░░░█▓▓▓▓▓▓▓▓▓▓▓█  
\t\t\t\t\t          ▓▓▓█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▓▓▓▓▓ █░█░█  
\t\t\t\t\t          ▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓        
\t\t\t\t\t          ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▓▓▓▓▓       
\t\t\t\t\t     ░█  ░░▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▓▓▓░       
\t\t\t\t\t    ░░░░░░░░█▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░   
\t\t\t\t\t  ░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░█   
\t\t\t\t\t   ░░▒▒▒▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░    
\t\t\t\t\t   █░▒▒▒▒▓▓█░░▒▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░▓▓▒▒▒▒░░░    
\t\t\t\t\t     ░▓▓▓▓▓▓▒░░▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒░▓▓▓▓▓▒▒█▓▓▓▓▓▓░░     
\t\t\t\t\t       █░░░░░█                            ░░█▓▓▓▓▒█      """+Fore.RESET,"Snorlax", "Normal", "Dormilón", "Primera", "Zona 1", "Pradera", "Bayas y frutas", "Recogida"),
            Pokemon(Fore.LIGHTBLUE_EX+"""\t\t\t\t\t         ░▒                              █▒░░            
\t\t\t\t\t        █ ░░▓                        ▒▒▒░░  ░            
\t\t\t\t\t         ░░▓▒▒█                   ▒▒▒▒▓▒░░░▒             
\t\t\t\t\t       ░▓ ░▒▒▒▒▒                ▒▒▒▒▒▒▒░ ░░░             
\t\t\t\t\t        ▒░░▒▒▒▒█                ▒▒▒▒▒▒▒░░█               
\t\t\t\t\t       █░░▒▒▒▒▒       ▒▓       ▒▒▒▒▒▒░░░░░░              
\t\t\t\t\t          ▒▒▒▒▒     ▒▓▓  █▒▓  █▒▒▒▒▒▒▒░█░░█              
\t\t\t\t\t         ░░▒▒▒▒   ▒▓▓▒▓▓▓     ▒▒▒▒▒▒▒▒░░                 
\t\t\t\t\t        ░░██▒▒▒   ▒▒▓░▒▒      ▒▒▒▒▒▒▒░░                  
\t\t\t\t\t         ▒▒▒▒▒▒█  █▒▒▒▒▒    █▒▒▒▒▒▒                      
\t\t\t\t\t           ▒█▒▒▒▒▓░░░▒▒█ █▒▒▒▒▒▒▒▒▒░░░░                  
\t\t\t\t\t            ▒▒▒▒▒░░░░░█▒▒▒▒▒▒▒▒▒▒██░░▓                   
\t\t\t\t\t             █▒▒░░░░░░░▒▒▒▒▒▒▒▒▒░ █                      
\t\t\t\t\t                ░░░░░░░▒▒░░ ░ ░        ▒▒▒▒▒▒▒▒          
\t\t\t\t\t               █░░░░░░▒▒▒▒▓         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t                ░░░░░▒▒▒▒▒▒       ▓▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓      
\t\t\t\t\t                 ░░░▒▒▒▒▒▒▒     ▓▓▓▓▓▓▓▓▓█  ▓▓▓▓▓▓▓▓     
\t\t\t\t\t                  ▒░▒▒▓▒▒▒▒  ▓▓▓▓▓▓▓▓▓█    ▓▓▓▓▓▓▓▓      
\t\t\t\t\t                   ▒▒█  ▒▒█▓▓▓▓▓▓▓█       █▓▓▓▓▓▓▓▓      
\t\t\t\t\t                    ▒    ▓              ▒▓▓▓▓▓▓▓▓▓       
\t\t\t\t\t                   ▒     ▒           █▓▓▓▓▓▓▓▓▓▓         
\t\t\t\t\t                 ▒▒▓█  █▒▒▒██▒▒▒▓▓▓█▒▒▓▓▓▓▓▓▓▓█          
\t\t\t\t\t               ▒▓▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██▒▒▒▒▒█             
\t\t\t\t\t                ▒ ▒▒▓▒▓▒▒                                
\t\t\t\t\t                  ███ ▒ ▒                                
\t\t\t\t\t                  █▓                                     """+Fore.RESET,"Articuno", "Hielo", "Congelado", "Primera", "Zona 2", "Montaña", "Frío", "Presión"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                                                     █░  
\t\t\t\t\t               ░      █       ▒        █        █░░░█    
\t\t\t\t\t    ░░░█        ░█     █    ░▒       ░ ██   ░░░░░░       
\t\t\t\t\t      █░░░░░░ ███░█    ░   ░▒     █░░██░░░░░░░░░    ██   
\t\t\t\t\t         ░░░░░░░░░░▒░░░░▒▒░▒ ░░ ░░░█░░░░░░░░░░████▓      
\t\t\t\t\t         ██░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░████          
\t\t\t\t\t            ██░░▒▒▒▒▒▒░░░░▒░░▒▒▒▒░░░░░░░░██              
\t\t\t\t\t        ░░░░░░░░░▒▒▒░░▒░▒▒▒▒▒▒░▒▒▒░░░░░░░░░░░░░█         
\t\t\t\t\t              ░░▒▒▒▒▒▒░▒░▒▒▒▒▒█░▒▒▒░░░░░█                
\t\t\t\t\t                  ▒▒▒░▒░░░░▒░▒▒▒▒▒▒                      
\t\t\t\t\t                ░▒░▒█▒ █░░░░▒▒ █▒▒░░                     
\t\t\t\t\t              ░   ▒ █ ▒▒▓░░█▒▒▒  ▒▒█░░                   
\t\t\t\t\t               ▓▓▓█▓ ░▒▒█▒░░▒▒▒░ ▓  ▒███                 
\t\t\t\t\t              █▒▒█▓▓▓    █▒▒▒▒  ▒▓▓                      
\t\t\t\t\t                    ▒  ▒▒▒▒▒▒▒▒▒▓█                       
\t\t\t\t\t                     █░██▒▒▒▒▒▒█▒▒░                      
\t\t\t\t\t                      █ ░░█▒▒█░▒██ ░                     
\t\t\t\t\t                       ░░█ ░ █ ░                         
\t\t\t\t\t                           ░    ░                        
\t\t\t\t\t                           ░                             """+Fore.RESET,"Zapdos", "Eléctrico", "Eléctrico", "Primera", "Zona 2", "Montaña", "Electricidad", "Presión"),
            Pokemon(Fore.LIGHTRED_EX+"""\t\t\t\t\t                                                     ▒▒  
\t\t\t\t\t               ░▒░░▒▒                              ▓▒▒░  
\t\t\t\t\t                ░░░░░░  ▒                        ░▒█░░█  
\t\t\t\t\t      ▒▒▒▒█ ▒▒ ░▒▒░░░▓ ░░░░░     ░░           ▒▒░▒░▒     
\t\t\t\t\t  ▓▒▒▒▒▒▒▒▒░░█▒░░▒▒▒▒▒▒▒░░░▒     ░░░░░      ▓▒▒░░░       
\t\t\t\t\t     ▒ ▒▒░░░░░░░░█▒▒░▒▒▒▒▒▒░▒     ▒░░░░   ▓▒░░█▒▒        
\t\t\t\t\t          ▓▒░░▒▒░░▒░░░▒▒▒▒▒░░▒     ▒▓▒░▒▒▒▒█▒█           
\t\t\t\t\t            ▒▒▒▒▒░░▒▒░█░▒█ ░░▒      ▒░░░░▒▒▒             
\t\t\t\t\t                ▓ ▒▒▒▒▒░▒█░░░░░░░░░░▒▒▒▒▒▒░░             
\t\t\t\t\t                        ▒▒▒▒▒▒█░░░░░░░░░░░▒▒░▒           
\t\t\t\t\t                       █▒ ▓▒▒▒▒▒▒▒▒▒▒ █░░█░░▒            
\t\t\t\t\t                       ▒▒      ▓█        ▒▒▒▒            
\t\t\t\t\t                       ▓█                     ▒          """+Fore.RESET,"Moltres", "Fuego", "Llama", "Primera", "Zona 3", "Volcán", "Bayas", "Presión"),
            Pokemon(Fore.LIGHTCYAN_EX+"""\t\t\t\t\t                                           █             
\t\t\t\t\t                                           ░█            
\t\t\t\t\t                                           ░░█           
\t\t\t\t\t                         █░░█              █░░█          
\t\t\t\t\t                           ░░░░█    █░░░░░▒▒▒▒▒░         
\t\t\t\t\t                            ░░░░░  ░░░░░░░░░█▒▒█         
\t\t\t\t\t                             ░░░░░▒░░█ ░░░▒░░░░██        
\t\t\t\t\t                            ░░░░░▒░░░██░█░░░░░░░░░       
\t\t\t\t\t                              ▒░░░▒░▒░▓███░░░░░░░░░      
\t\t\t\t\t                               ░░░░█▒▒▒░░░░░░░░░░░▓      
\t\t\t\t\t                               █░██▒▒▒▒▒░█░░░░░░▒        
\t\t\t\t\t                                    ▒▒▒▒▒▒▒▒▒▒█          
\t\t\t\t\t                                     ▒▒▒▒▒▒░░░░          
\t\t\t\t\t                                      ▒░░░░░░░░░         
\t\t\t\t\t                                       ▒▒░░░░░░░░        
\t\t\t\t\t                                        ▒░░░░░░░░░       
\t\t\t\t\t                                         ░░░░░░░░░░      
\t\t\t\t\t                                          ░░░░░░░░░░     
\t\t\t\t\t                                          ▓░░░░░░░░░░    
\t\t\t\t\t    █▒▒▒▒▒▒▒▒▒▒█                           ░░░░░░░░░░    
\t\t\t\t\t      ██▒▒▒▒▒▒▒▒▒▒▒▒▓                      ░░░░░░░░░░░   
\t\t\t\t\t             █▒▒▒▒▒▒▒▒▒▒▒                 ░░░░░░░░░░░░   
\t\t\t\t\t                 █▒▒▒▒▒▒▒▒▒▒▒▓          ░░░░░░░░░░░░░█   
\t\t\t\t\t                    █▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒░░░░░░░░░░░░░░░    
\t\t\t\t\t                       █▒▒░░░▒▒▒▒░▒▒▒░░░░░░░░░░░░░░▒     
\t\t\t\t\t                          █▒▒▒░░░░░░░░░░░░░░░░░░░░       
\t\t\t\t\t                              █▒▒▒▒░░░░▒░░░░░░░░         
\t\t\t\t\t                                     ██▓▒██              """+Fore.RESET,"Dratini", "Dragón", "Dragón", "Primera", "Zona 2", "Río", "Peces y algas", "Envolvente"),
            Pokemon(Fore.LIGHTBLUE_EX+"""\t\t\t\t\t                                 █                       
\t\t\t\t\t                    █            ░█                      
\t\t\t\t\t                     █░         █░░                      
\t\t\t\t\t                      ▓░        ░█░░                     
\t\t\t\t\t                      █░░░░▒▒▒▒░░░░▒                     
\t\t\t\t\t                      █░▒▒▒▒▒▒░░░░▓                      
\t\t\t\t\t                       ░░░▒▒▒█▒░░▓                       
\t\t\t\t\t                        ▒▒▒▒ █▒▒▒                        
\t\t\t\t\t                        █▒▒▒█▒▒▓█                        
\t\t\t\t\t                        ▒░▒▒▒▒▒▒                         
\t\t\t\t\t                           █▒▒▒                          
\t\t\t\t\t                          ▓▓▓▒                           
\t\t\t\t\t                          ░░▒▓                           
\t\t\t\t\t                         ░░▒▒                            
\t\t\t\t\t       ▓                ░░▒▒                             
\t\t\t\t\t     ▓▒█              █░░░▒█                             
\t\t\t\t\t    ░▒▓              ░░░░▒▒                              
\t\t\t\t\t    ▒▓▒             ░░░░░▒                               
\t\t\t\t\t    ██             ░░░░░▒▒             █▒▒▒▒▒▒▒          
\t\t\t\t\t     ▒            █░░░░░▒▒         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       
\t\t\t\t\t     ▓█           ░░░░░░▒▒     █▒▒▒▒▒▒▒▒▒▒▒▒▒█░░▒▒▒      
\t\t\t\t\t      ▓▓          ░░░░░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒█░░░░▒▒░░      
\t\t\t\t\t       ░▓▓▓█      ░░░░░░░▒▒▒▓▓▓▓▓▓▓▓▓▓█░░░░░░▒▒░░░░      
\t\t\t\t\t         █░▓▓▓▓▓▓▓░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░      
\t\t\t\t\t               █░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░       
\t\t\t\t\t                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░█         
\t\t\t\t\t                     █░░░░░░░░░░░░░░░░░█                 
\t\t\t\t\t                         █▓░░░░░▓                        """+Fore.RESET,"Dragonair", "Dragón", "Dragón", "Primera", "Zona 2", "Río", "Peces y algas", "Envolvente"),
            Pokemon(Fore.LIGHTYELLOW_EX+"""\t\t\t\t\t                                  █                      
\t\t\t\t\t             ░                    ░                      
\t\t\t\t\t            ▒         ▓▒█ ░   ██                         
\t\t\t\t\t             █ █░█ ░█░░░▒▒▒▒                             
\t\t\t\t\t                    ░▒▒▒▒░▒░▒                            
\t\t\t\t\t                    ▒▒▒▒▒█▓▒▒         █▓░                
\t\t\t\t\t                    ░░░▒▒▒▒▒▒▒       ▒▒▓▓▓▒              
\t\t\t\t\t                    ░░▒▒▒▒▒▓▒▒      ▒▒▒▓▒▒▒▒             
\t\t\t\t\t                   █▓▒▒▒▒░░█▒▒▒    ▒▒▒▒█▒▒▒▒█            
\t\t\t\t\t           ░░░░▓█ ▒▓▓▓▓░░░░░▒▒▒░ ▒▓▓▒▒▒█▒▒▒▒▒▒           
\t\t\t\t\t            ▒▒▒▒▒▒▒▒▒▒░▒░▒▓▒▒░░▒▒▓▓▓▓▒▒▓▓▒██▒▓           
\t\t\t\t\t             ▒▒▒▒▒▒▒▒░░░░░░░▒░░░▒▒     ▓      █          
\t\t\t\t\t                █▒▓█░░░░░░░▒▒█▒░░▒░█                     
\t\t\t\t\t                   ░░░░░░░░░▒▒░▒░░░▒░                    
\t\t\t\t\t                  ░░░░░░▒░░▒░▒▒▒▒▒▒▒▒▒            █      
\t\t\t\t\t                 ░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒█          ▒▒      
\t\t\t\t\t                ░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░        ▒▒▒▓      
\t\t\t\t\t               ░░░░░░░░░░░░░░▒░░░░▒▒░      █▒▒▒▒▒▒       
\t\t\t\t\t              █░░░░░░░░░░░░░░░░░░░░▒▒█▒▒▒▒▒▒▒▒▒▒█        
\t\t\t\t\t              █░░░░░░░░░░░▒░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒          
\t\t\t\t\t               ░▒▒▒░░░░░░░░░█░░░▒░▒▒▒▒▒▒▒▒▒▒▒█           
\t\t\t\t\t                ▒▒▒▒▒▒░░░░░░▒█▒▒▒▒▒▒▒▒▒▒▒▓▓              
\t\t\t\t\t                   ▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒                 
\t\t\t\t\t              █░░▒▒▒▒▒▒      ████▒▒▒▒                    
\t\t\t\t\t             ░░░█░▒▒▒            ▒▒▒▒▒                   
\t\t\t\t\t                                ▒░▒▒▒▒▒                  
\t\t\t\t\t                                ▒░█░░▒░                  
\t\t\t\t\t                                  █ ░ █                  """+Fore.RESET,"Dragonite", "Dragón", "Dragón", "Primera", "Zona 2", "Río", "Peces y algas", "Envolvente"),
            Pokemon(Fore.LIGHTMAGENTA_EX+"""\t\t\t\t\t                             █░░    ▓                    
\t\t\t\t\t                              ░░░░█░░░                   
\t\t\t\t\t                             ░░░░░░░░▒                   
\t\t\t\t\t                            ░░░░░░░░░▒                   
\t\t\t\t\t                            ░░░░▓░░░░░                   
\t\t\t\t\t                    ░░░      ▒▒░░░░░░                    
\t\t\t\t\t                     ▒▒▒░█  ▒▒ ▒▒▒▒▒░                    
\t\t\t\t\t                     ░░▒▒▒░▒░░▒░░░░░                     
\t\t\t\t\t                 ░░▒▒▒▒▒▒░░░█▒▒█░░░▒▒                    
\t\t\t\t\t          ▒▒▒▒▒▒             ░░▒░░▒▒▒▒█                  
\t\t\t\t\t         ▒▓   ▒▒▒█             ░░▒▒▒  ▒▒░▒               
\t\t\t\t\t         ▓█     ▒▒▒             ▒▒▒▒░    ░░              
\t\t\t\t\t         ▓▓      ▒▒▒           ░░▒▒▒▒▒    ▒░█            
\t\t\t\t\t         ▒▓      █▒▒▒█       ░░░░░▒▒▒▒▒▒   ░░░           
\t\t\t\t\t          ▓▓      ▒▒▒▒▒▒   ░░░░░░░█▒▒▒▒▒░ ▓▒ ░█░         
\t\t\t\t\t           ▓▒█     ▒▒▒▒▒▒▒█░░░░░░░▓▒▒▒▒▒░▒ █ ▒█▒         
\t\t\t\t\t            ▒▒▒▒    ▒▒▒▒▒▒░░░░░░░▒▒▒▒▒▒▒▒█               
\t\t\t\t\t             ▒▒▒▒▒   █▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒                
\t\t\t\t\t              ▒▒▒▒▒▒   █▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒█                 
\t\t\t\t\t                ▒▒▒▒     █▒▒       ▓░▒                   
\t\t\t\t\t                        ▒░░        ░░█                   
\t\t\t\t\t                       ░░░        ▓▒▒░                   
\t\t\t\t\t                      █░░▓       ░░▒▒▒▒▒                 
\t\t\t\t\t                     ▓░░▒▓           ▓▒▒▒░░█░            
\t\t\t\t\t                    ░░░░░░░                              
\t\t\t\t\t                   ░░░▓  ▒█                              """+Fore.RESET,"Mewtwo", "Psíquico", "Genético", "Primera", "Zona 2", "Montaña", "ADN", "Presión"),
            Pokemon(Fore.LIGHTMAGENTA_EX+"""\t\t\t\t\t                     ▒░░█                                
\t\t\t\t\t                  █░░░░░                                 
\t\t\t\t\t                ▒░░░░▒█                                  
\t\t\t\t\t              ▒▒▒▒▒▒▒  █░░░░░░░█                         
\t\t\t\t\t            ▒▒▒▒░░░░░░░░░░░░░░▒▒                         
\t\t\t\t\t          ▒▒▒▒▒▒░░░░░░░░░░░░░░░░█                        
\t\t\t\t\t         ▒▒█    ░░░░░░░░░░░░░█░░░                        
\t\t\t\t\t       ▒▒       █░▒░░░░░░░░░▓▓█░░                        
\t\t\t\t\t      ▒█        ░░░░▓▒░░░░░░░░░░    █▒▒▒▒▒▒▓████▒▒▒█     
\t\t\t\t\t     ▒           ░░░░█░░░░░░▒▒▒▒▒█                  ▒    
\t\t\t\t\t    ██              ▓█░░░░░▒▒▒▒▒░░░░░░             ▒     
\t\t\t\t\t    ██            ▒▒▒  ▒▒▒▒▒▒▒░░░    ▓           ▒▒      
\t\t\t\t\t      █▒▒▒▒▒▒▒▒█     ░░░▒  ░░░░░░░             ▒▒        
\t\t\t\t\t                           ░░░░░░░░░░        ▒▒          
\t\t\t\t\t                           ░░░░░░░░░░░░   ▓▓             
\t\t\t\t\t                          ░░░░░░░░░░░░░░▓▓               
\t\t\t\t\t                          ░░░░░░░░░░░░░░█                
\t\t\t\t\t                          ░░░░░░░░▒▒░░▒▒█                
\t\t\t\t\t                          ▒▒░▒▒▒▒▒▒▒█  ▒▒▒               
\t\t\t\t\t                          ▒▒▒█         █▒▒█              
\t\t\t\t\t                          █▒░░          ░░░▓             
\t\t\t\t\t                           ░░░░         ░░░░             
\t\t\t\t\t                            ░░░░        █░░░░            
\t\t\t\t\t                             ▒▒█         ░░░░░           
\t\t\t\t\t                                         ░░░░░           
\t\t\t\t\t                                          ░░░▒           """+Fore.RESET,"Mew", "Psíquico", "Nuevo", "Primera", "Zona 1", "Bosque", "ADN", "Sincronización")
        ]

zona_1 = Instalaciones("Safari de Kanto", "Zona 1", "Abierto", pokemon_primera_generacion)
zona_2 = Instalaciones("Safari de Kanto", "Zona 2", "Abierto", pokemon_primera_generacion)
zona_3 = Instalaciones("Safari de Kanto", "Zona 3", "Abierto", pokemon_primera_generacion)

pokedex = Instalaciones("Safari de Kanto", "Zona 1", "Abierto", pokemon_primera_generacion)

instalacion = Instalaciones("Zona Safari", AREAS, "Limpio", pokemon_primera_generacion)

os.system("cls")

while True:
    os.system("cls")
    pygame.mixer.music.load(safari)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.5)
    pokemon_menu = random.choice(pokemon_primera_generacion)
    print(logo)
    opcion = input("\t\t\t\t\tIntroduce la opcion a la que quieras acceder, usa el numero correspondiente: ")
    if opcion == "1":
        while True:
          os.system("cls")
          print(buscar_imagen)
          print("\t\t\t\t\t1. Ver por areas.")
          print("\t\t\t\t\t2. Ver Introduciendo su numero de Pokedex.")
          print(Fore.LIGHTRED_EX +"\t\t\t\t\t0. Volver."+Fore.RESET)
          opcion = input("\t\t\t\t\tIntroduce la opcion a la que quieras acceder, usa el numero correspondiente: ")
          if opcion == "1":
              os.system("cls")
              print(buscar_imagen)
              opcion = input("\t\t\t\t\tIntroduce el número de la zona para ver los Pokémon que viven ahí: \n\t\t\t\t\t1. Zona 1\n\t\t\t\t\t2. Zona 2\n\t\t\t\t\t3. Zona 3\n\t\t\t\t\t->")
              if opcion == "1":
                  os.system("cls")
                  print(buscar_imagen)
                  zona_1.mostrar_pokemon_area("Zona 1")
                  print("\t\t\t\t\tPulsa enter para continuar.")
                  input()
                  os.system("cls")
              elif opcion == "2":
                  os.system("cls")
                  print(buscar_imagen)
                  zona_2.mostrar_pokemon_area("Zona 2")
                  print("\t\t\t\t\tPulsa enter para continuar.")
                  input()
                  os.system("cls")
              elif opcion == "3":
                  os.system("cls")
                  print(buscar_imagen)
                  zona_3.mostrar_pokemon_area("Zona 3")
                  print("\t\t\t\t\tPulsa enter para continuar.")
                  input()
                  os.system("cls")
              else:
                  print("\t\t\t\t\tOpción no válida.")
                  input("\t\t\t\t\tPulsa ENTER para continuar.")

          elif opcion == "2":
              os.system("cls")
              pokedex.mostrar_pokemon_por_numero_usuario()
              os.system("cls")
          elif opcion == "0":
              os.system("cls")
              break
          else:
              print("\t\t\t\t\tPor favor, introduce un número válido.")
              input("\t\t\t\t\tPulsa ENTER para continuar.")

        
    elif opcion == "2":
        while True:
            os.system("cls")
            print(empleados_imagen)
            print("\t\t\t\t\t1. Añadir nuevos empleados.")
            print("\t\t\t\t\t2. Modificar o eliminar trabajadores.")
            print("\t\t\t\t\t3. Ver trabajadores.")
            print(Fore.LIGHTRED_EX +"\t\t\t\t\t0. Volver."+Fore.RESET)
            opcion = input("\t\t\t\t\tIntroduce la opcion a la que quieras acceder, usa el numero correspondiente: ")
            if opcion == "1":
                while True:
                    os.system("cls")
                    print(empleados_imagen)
                    print("\t\t\t\t\t¿En que zona trabajara el nuevo empleado?\n\t\t\t\t\t1. Zona 1\n\t\t\t\t\t2. Zona 2\n\t\t\t\t\t3. Zona 3\n\t\t\t\t\t0. Volver")
                    opcion = input("\t\t\t\t\tIntroduce el número de la zona: ")
                    if opcion == "1":
                        agregar_trabajador(zona_1) 
                    elif opcion == "2":
                        agregar_trabajador(zona_2) 
                    elif opcion == "3":
                        agregar_trabajador(zona_3) 
                    elif opcion == "0":
                        break
                    else:
                        print("\t\t\t\t\tIntroduce una opcion correcta. Pulsa enter para continuar.")
                        input()
                    os.system("cls")
            elif opcion == "0":
                os.system("cls")
                break
            elif opcion == "3":
                  os.system("cls")
                  print(empleados_imagen)
                  print("\t\t\t\t\tTrabajadores por zona:")
                  print("\t\t\t\t\tZona 1:")
                  for trabajador in zona_1.trabajadores:
                      print(f"\t\t\t\t\tNombre: {trabajador.nombre}, Edad: {trabajador.edad}")
                  print("\t\t\t\t\tZona 2:")
                  for trabajador in zona_2.trabajadores:
                      print(f"\t\t\t\t\tNombre: {trabajador.nombre}, Edad: {trabajador.edad}")
                  print("\t\t\t\t\tZona 3:")
                  for trabajador in zona_3.trabajadores:
                      print(f"\t\t\t\t\tNombre: {trabajador.nombre}, Edad: {trabajador.edad}")
                  print("\t\t\t\t\tPulsa enter para continuar.")
                  input()
                  os.system("cls")
        
            elif opcion == "2":
                while True:
                    os.system("cls")
                    print(empleados_imagen)
                    print("\t\t\t\t\tIntroduce el número de la zona para modificar o eliminar trabajadores: ")
                    print("\t\t\t\t\t1. Zona 1")
                    print("\t\t\t\t\t2. Zona 2")
                    print("\t\t\t\t\t3. Zona 3")
                    print("\t\t\t\t\t0. Volver")
                    
                    zona = input("\t\t\t\t\t-> ")
                    if zona == '0':
                        os.system("cls")
                        break
                    elif zona.isdigit():
                        zona = int(zona)
                        if zona == 1:
                            os.system("cls")
                            print(empleados_imagen)
                            zona_1.mostrar_trabajadores("Zona 1")
                            opcion_trabajador = input("\t\t\t\t\tIntroduce el número del trabajador que desea modificar o eliminar (0 para volver): ")
                            if opcion_trabajador == '0':
                                break
                            elif opcion_trabajador.isdigit():
                                opcion_trabajador = int(opcion_trabajador)
                                if opcion_trabajador <= len(zona_1.trabajadores):
                                    accion = input("\t\t\t\t\t¿Desea modificar (M) o eliminar (E) el trabajador? (0 para volver) ")
                                    if accion.upper() == "M":
                                        nuevo_nombre = input("\t\t\t\t\tIntroduce el nuevo nombre del trabajador: ")
                                        nueva_edad = int(input("\t\t\t\t\tIntroduce la nueva edad del trabajador: "))
                                        zona_1.modificar_trabajador("Zona 1", opcion_trabajador, nuevo_nombre, nueva_edad)
                                    elif accion.upper() == "E":
                                        zona_1.eliminar_trabajador("Zona 1", opcion_trabajador)
                                    elif accion == '0':
                                        break
                                    else:
                                        print("\t\t\t\t\tOpción no válida.")
                                        input("\t\t\t\t\tPulsa ENTER para continuar.")
                                else:
                                    print("\t\t\t\t\tNúmero de trabajador no válido.")
                                    input("\t\t\t\t\tPulsa ENTER para continuar.")
                            else:
                                print("\t\t\t\t\tPor favor, introduce un número válido.")
                                input("\t\t\t\t\tPulsa ENTER para continuar.")
                        elif zona == 2:
                            os.system("cls")
                            print(empleados_imagen)
                            zona_2.mostrar_trabajadores("Zona 2")
                            opcion_trabajador = input("\t\t\t\t\tIntroduce el número del trabajador que desea modificar o eliminar (0 para volver): ")
                            if opcion_trabajador == '0':
                                break
                            elif opcion_trabajador.isdigit():
                                opcion_trabajador = int(opcion_trabajador)
                                if opcion_trabajador <= len(zona_2.trabajadores):
                                    accion = input("\t\t\t\t\t¿Desea modificar (M) o eliminar (E) el trabajador? (0 para volver) ")
                                    if accion.upper() == "M":
                                        nuevo_nombre = input("\t\t\t\t\tIntroduce el nuevo nombre del trabajador: ")
                                        nueva_edad = int(input("\t\t\t\t\tIntroduce la nueva edad del trabajador: "))
                                        zona_2.modificar_trabajador("Zona 2", opcion_trabajador, nuevo_nombre, nueva_edad)
                                    elif accion.upper() == "E":
                                        zona_2.eliminar_trabajador("Zona 2", opcion_trabajador)
                                    elif accion == '0':
                                        break
                                    else:
                                        print("\t\t\t\t\tOpción no válida.")
                                        input("\t\t\t\t\tPulsa enter para continuar.")
                                else:
                                    print("\t\t\t\t\tNúmero de trabajador no válido.")
                                    input("\t\t\t\t\tPulsa enter para continuar.")
                            else:
                                print("\t\t\t\t\tPor favor, introduce un número válido.")
                                input("\t\t\t\t\tPulsa enter para continuar.")
                        elif zona == 3:
                            os.system("cls")
                            print(empleados_imagen)
                            zona_3.mostrar_trabajadores("Zona 3")
                            opcion_trabajador = input("\t\t\t\t\tIntroduce el número del trabajador que desea modificar o eliminar (0 para volver): ")
                            if opcion_trabajador == '0':
                                os.system("cls")
                                break
                            elif opcion_trabajador.isdigit():
                                opcion_trabajador = int(opcion_trabajador)
                                if opcion_trabajador <= len(zona_3.trabajadores):
                                    accion = input("\t\t\t\t\t¿Desea modificar (M) o eliminar (E) el trabajador? (0 para volver) ")
                                    if accion.upper() == "M":
                                        nuevo_nombre = input("\t\t\t\t\tIntroduce el nuevo nombre del trabajador: ")
                                        nueva_edad = int(input("\t\t\t\t\tIntroduce la nueva edad del trabajador: "))
                                        zona_3.modificar_trabajador("Zona 3", opcion_trabajador, nuevo_nombre, nueva_edad)
                                    elif accion.upper() == "E":
                                        zona_3.eliminar_trabajador("Zona 3", opcion_trabajador)
                                    elif accion == '0':
                                        os.system("cls")
                                        break
                                    else:
                                        print("\t\t\t\t\tOpción no válida.")
                                        input("\t\t\t\t\tPulsa enter para continuar.")
                                else:
                                    print("\t\t\t\t\tNúmero de trabajador no válido.")
                                    input("\t\t\t\t\tPulsa enter para continuar.")
                            else:
                                print("\t\t\t\t\tPor favor, introduce un número válido.")
                                input("\t\t\t\t\tPulsa enter para continuar.")
                        else:
                            print("\t\t\t\t\tZona no válida.")
                            input("\t\t\t\t\tPulsa enter para continuar.")
                    else:
                        print("\t\t\t\t\tPor favor, introduce un número válido para la zona.")
                        input("\t\t\t\t\tPulsa enter para continuar.")
            else:
                print("\t\t\t\t\tPor favor, introduce un número válido.")
                input("\t\t\t\t\tPulsa enter para continuar.")

    elif opcion == "3":
        while True:
            os.system("cls")
            print(clientes_imagen)
            print("\t\t\t\t\t1. Vender entradas")
            print("\t\t\t\t\t2. Ver ganancias totales")
            print(Fore.LIGHTRED_EX +"\t\t\t\t\t0. Volver."+Fore.RESET)
            subopcion = input("\t\t\t\t\tSelecciona una opción: ")
            if subopcion == '0':
                os.system("cls")
                break
            elif subopcion == '1':
                os.system("cls")
                print(clientes_imagen)
                ganancias_totales = vender_entradas()
                input("\t\t\t\t\tPulsa ENTER para continuar.")
                os.system("cls")
            elif subopcion == '2':
                os.system("cls")
                print(clientes_imagen)
                print(Fore.LIGHTYELLOW_EX+f"\t\t\t\t\tGanancias totales: {ganancias_totales}€"+Fore.RESET)
                print("\n\t\t\t\t\tLista de clientes y si son entrenadores:")
                for venta in lista_ventas:
                    cliente, precio = venta
                    print(Fore.LIGHTMAGENTA_EX+f"\t\t\t\t\tCliente: {cliente.nombre}, Precio entrada: €{precio}, Entrenador: {'Sí' if cliente.es_entrenador else 'No'}"+Fore.RESET)
                input("\n\t\t\t\t\tPulsa ENTER para continuar.")

    elif opcion == "4":
        while True:
            os.system("cls")
            print(minijuego_imagen)
            print("\t\t\t\t\t1. Atrapalos a todos!")
            print("\t\t\t\t\t2. Mostrar Pokémon atrapados")
            print(Fore.LIGHTRED_EX +"\t\t\t\t\t0. Volver."+Fore.RESET)
            subopcion = input("\t\t\t\t\tSelecciona una opción: ")
            if subopcion == '0':
                break
            elif subopcion.isdigit():
                subopcion = int(subopcion)
                if subopcion == 1:
                    while True:
                      pygame.mixer.music.load(minijuego)
                      pygame.mixer.music.play()
                      pygame.mixer.music.set_volume(0.5)
                      os.system("cls")
                      print(minijuego_imagen)
                      print("\t\t\t\t\tÁreas disponibles:")
                      for i, area in enumerate(AREAS, start=1):
                          print(f"\t\t\t\t\t{i}. {area}")
                      opcion_area = input("\t\t\t\t\t¿En qué área deseas atrapar Pokémon? (0 para salir): ")
                      if opcion_area == '0':
                          os.system("cls")
                          break
                      elif opcion_area.isdigit():
                          opcion_area = int(opcion_area)
                          if 1 <= opcion_area <= len(AREAS):
                              instalacion.atrapar_pokemon(AREAS[opcion_area - 1])
                          else:
                              print("\t\t\t\t\tOpción no válida.")
                      else:
                          print("\t\t\t\t\tPor favor, introduce un número válido.")
                          input("\t\t\t\t\tPulsa ENTER para continuar.")
                elif subopcion == 2:
                    instalacion.mostrar_pokemon_atrapados()
                else:
                    print("\t\t\t\t\tOpción no válida. Por favor, selecciona una opción válida.")
            else:
                print("\t\t\t\t\tPor favor, introduce un número válido.")
                input("\t\t\t\t\tPulsa ENTER para continuar.")
            
                

    elif opcion == "0":
        print("\t\t\t\t\tGracias por usar la aplicacion.")
        input()
        break

    else:
        print("\t\t\t\t\tPor favor, introduce un número válido.")
        input("\t\t\t\t\tPulsa ENTER para continuar.")
        os.system("cls")
