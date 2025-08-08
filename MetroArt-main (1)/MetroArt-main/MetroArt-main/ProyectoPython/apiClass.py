import requests

#ApiClass es una clase la cual contiene funciones que extraeran la informacion solicitada de la Api mediante Url
#Cada funcion devuelve json (formato diccionario)

class ApiClass:
    def obtener_obra_por_id(obra_id):
        """Devuelve toda la información de una obra por su ID."""
        respuesta = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obra_id}")
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            print(f"Error al obtener obra: {respuesta.status_code}")
            return None

    def obtener_departamentos():
        """Devuelve la lista de departamentos del museo."""
        respuesta = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
        if respuesta.status_code == 200:
            print("Departamentos obtenidos correctamente.")
            departamentos_json = respuesta.json()
            return departamentos_json
        else:
            print(f"Error al obtener departamentos: {respuesta.status_code}")
            return None
        
    def obtener_obras_por_departamento(departamento_id):
        """Devuelve los IDs de obras de un departamento."""
        respuesta = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={departamento_id}")
        if respuesta.status_code == 200:
            print("IDs de obras obtenidos correctamente.")
            obras_json = respuesta.json()
            return obras_json
        else:
            print(f"Error al obtener IDs de obras en departamento {departamento_id}: {respuesta.status_code}")
            return None
    #nacionalidades update
    def obt_obra_id(object_id):
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            return None
        
    def obtener_obras_por_autor(nombreAutor):
        """Devuelve los IDs de obras según el nombre del autor."""
        respuesta = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombreAutor}")   
        if respuesta.status_code == 200:
            print("Obras por autor obtenidas correctamente.")
            obras_json = respuesta.json()
            return obras_json
        else:
            print(f"Error al obtener obras por autor: {respuesta.status_code}")
            return None 

