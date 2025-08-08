
from apiClass import ApiClass
from obra import Obra   
from departamento import Departamento
import requests
from nacionalidad_test2 import metod_nac, mostrar_resultados, filtrar_nacionalidad, obt_obra_id
from list_nom_autor import filt_autor, detalles_obra, mostrar_results, interfaz_user  
from PIL import Image


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
                metod_nac()  

            elif opcion == '4':
                print("Opción 4 seleccionada")        

            elif opcion == '5':
                print("Finalizando el programa")
                break     
            else:
                print("Opción no válida, intente de nuevo.") 


    


    def ver_obra_por_id(self):  #ejecuta la opción 1 del menu
        """Muestra los detalles de una obra por su ID."""
        obra_id = int(input("Ingrese el ID de la obra para ver su informacion: "))
        datos_obra = self.api.obtener_obra_por_id(obra_id)
        obra = Obra(datos_obra['objectID'],datos_obra['title'],datos_obra['artistDisplayName'],datos_obra['artistNationality'],datos_obra['artistBeginDate'],datos_obra['artistEndDate'],datos_obra['classification'],datos_obra['objectDate'],datos_obra['primaryImage'])

        #Validaciones para mostrar la informacion de la obra si existe
        if obra.titulo:
            print(f"Título: {obra.titulo}")
        else:
            print("Título: No existe información en la API")
        if obra.artista:
            print(f"Artista: {obra.artista}")
        else:
            print("Artista: No existe información en la API")
        if obra.nacionalidad:
            print(f"Nacionalidad: {obra.nacionalidad}")
        else:
            print("Nacionalidad: No existe información en la API")
        if obra.nacimiento:
            print(f"Nacimiento: {obra.nacimiento}")
        else:
            print("Nacimiento: No existe información en la API")
        if obra.muerte:
            print(f"Muerte: {obra.muerte}")
        else:
            print("Muerte: No existe información en la API")
        if obra.tipo:
            print(f"Tipo: {obra.tipo}")
        else:
            print("Tipo: No existe información en la API")
        if obra.anio_creacion:
            print(f"Año de creación: {obra.anio_creacion}")
        else:
            print("Año de creación: No existe información en la API")
        if obra.imagen:
            print(f"Imagen: {obra.imagen}")
        else:
            print("Imagen: No existe información en la API")

        # Guarda y muestra la imagen si hay URL
        if obra.imagen:
            nombre_archivo = f"obra_{obra.id_obra}"
            archivo_guardado = self.guardar_imagen_desde_url(obra.imagen, nombre_archivo)
            if archivo_guardado:
                try:
                    img = Image.open(archivo_guardado)
                    img.show()
                except Exception as e:
                    print(f"No se pudo mostrar la imagen: {e}")
        else:
            print("No hay imagen disponible para esta obra.")



    def guardar_imagen_desde_url(self,url, nombre_archivo):
        """ Descarga una imagen desde una URL y la guarda en un archivo"""
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status() # Lanza una excepción para códigos de estado de error (4xx o 5xx)
            content_type = response.headers.get('Content-Type')
            extension = '.png' # Valor por defecto
            if content_type:
                if 'image/png' in content_type:
                    extension = '.png'
                elif 'image/jpeg' in content_type:
                    extension = '.jpg'
                elif 'image/svg+xml' in content_type:
                    extension = '.svg'

            nombre_archivo_final = f"{nombre_archivo}{extension}"

            with open(nombre_archivo_final, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Imagen guardada exitosamente como '{nombre_archivo_final}'")
        except requests.exceptions.RequestException as e:
            print(f"Error al hacer el request: {e}")
            return None
        except IOError as e:
            print(f"Error al escribir el archivo: {e}")
            return None
        return nombre_archivo_final
    

    def ver_lista_de_obras_por_departamento(self):   #ejecuta la opcion 2 del menu
        """Muestra una lista de obras por departamento."""
        departamentos = self.api.obtener_departamentos()
        for dpto in departamentos['departments']:
                departamento = Departamento(dpto['departmentId'], dpto['displayName'])
                print(f"Departamento ID: {departamento.id_departamento}, Nombre: {departamento.nombre}")
        
        
        while True:
            departamento_id = int(input("Ingrese el ID del departamento para ver sus obras (INGRESE UN NUMERO): "))
            if departamento_id < 0 or departamento_id >21 or departamento_id == 20:
                print("ID de departamento no válido. Por favor, intente de nuevo.")
                
            else:    
                obras = self.api.obtener_obras_por_departamento(departamento_id)

                cont = 0  #auxiliar para controlar las obras que se muestran con cada "si"
                while True:

                    continuar = input(" CONSIDERE LOS ERRORES AL REALIZAR MUCHAS SOLICITUDES A LA API \n ¿Desea ver las 20 siguientes obras de este departamento? (si/no): ").lower()

                    if continuar == 'si':
                        for obra in obras['objectIDs'][cont : cont+20]:#Muestra solo las primeras 20 obras para evitar errores y bloqueo de peticiones de la API
                            datos_de_obrita = self.api.obtener_obra_por_id(obra)
                            if datos_de_obrita:    #Esta verificacion es por si la API no devuelve datos para algun ID
                              obrita = Obra(datos_de_obrita['objectID'],datos_de_obrita['title'],datos_de_obrita['artistDisplayName'],datos_de_obrita['artistNationality'],datos_de_obrita['artistBeginDate'],datos_de_obrita['artistEndDate'],datos_de_obrita['classification'],datos_de_obrita['objectDate'],datos_de_obrita['primaryImage'])
                              print(f"{obrita.id_obra}-{obrita.titulo}-({obrita.artista})")
                            else:
                                print(f"Error al obtener datos de la obra con ID {obra}")  
                        cont += 20        

                    elif continuar == 'no':    
                        print("Saliendo de la lista de obras.")
                        cont = 0 #reiniciar el contador para la proxima vez que se use esta funcion
                        break
                    else:
                        print("Opcion no válida. Responda 'si' o 'no'.")
                break
                        










