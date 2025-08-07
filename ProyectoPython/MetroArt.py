from apiClass import ApiClass
from obra import Obra   
from departamento import Departamento


class MetroArt:
    """Clase principal para interactuar con la API del Metropolitan Museum of Art."""
    def __init__(self,api):
        self.api = api

    def start(self):
        """Inicia la aplicación."""
        print("Bienvenido a MetroArt")
        while True:
            print("1. Ver obra por ID")
            print("2. Ver lista de obras por departamento")
            print("2. Buscar obras por departamento")
            print("3. Buscar obras por nacionalidad")
            print("4. Buscar obras por autor")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
        
            if opcion == '1':
                self.ver_obra_por_id()

            elif opcion == '2':
                self.ver_lista_de_obras_por_departamento()

            elif opcion == '3':
                pass  

            elif opcion == '4':
                print("Opción 4 seleccionada")        

            elif opcion == '5':
                print("Finalizando el programa")
                break     
            else:
                print("Opción no válida, intente de nuevo.") 


    

    def ver_obra_por_id(self):
        """Muestra los detalles de una obra por su ID."""

        obra_id = int(input("Ingrese el ID de la obra para ver su informacion: "))
        datos_obra = self.api.obtener_obra_por_id(obra_id)
        
        obra = Obra(datos_obra['objectID'],datos_obra['title'],datos_obra['artistDisplayName'],datos_obra['artistNationality'],datos_obra['artistBeginDate'],datos_obra['artistEndDate'],datos_obra['classification'],datos_obra['objectDate'],datos_obra['primaryImage'])
   
        print(f"ID: {obra.id_obra}")
        print(f"Título: {obra.titulo}")
        print(f"Artista: {obra.artista}")
        print(f"Nacionalidad: {obra.nacionalidad}")
        print(f"Nacimiento: {obra.nacimiento}")
        print(f"Muerte: {obra.muerte}")
        print(f"Tipo: {obra.tipo}")
        print(f"Año de creación: {obra.anio_creacion}")
        print(f"Imagen: {obra.imagen}")
   
           

    def ver_lista_de_obras_por_departamento(self):
        """Muestra una lista de obras por departamento."""
        departamentos = self.api.obtener_departamentos()
        for dpto in departamentos['departments']:
                departamento = Departamento(dpto['departmentId'], dpto['displayName'])
                print(f"Departamento ID: {departamento.id_departamento}, Nombre: {departamento.nombre}")
        
        departamento_id = int(input("Ingrese el ID del departamento para ver sus obras: "))
        obras = self.api.obtener_obras_por_departamento(departamento_id)
        for obra in obras['objectIDs'][:40]:#Muestra solo las primeras 40 obras para evitar errores y bloqueo de peticiones de la API
            datos_de_obrita = self.api.obtener_obra_por_id(obra)
            if datos_de_obrita:    #Esta verificacion es por si la API no devuelve datos para algun ID
              obrita = Obra(datos_de_obrita['objectID'],datos_de_obrita['title'],datos_de_obrita['artistDisplayName'],datos_de_obrita['artistNationality'],datos_de_obrita['artistBeginDate'],datos_de_obrita['artistEndDate'],datos_de_obrita['classification'],datos_de_obrita['objectDate'],datos_de_obrita['primaryImage'])
              print(f"{obrita.id_obra}-{obrita.titulo}-({obrita.artista})")
            else:
                print(f"Error al obtener datos de la obra con ID {obra}")  







