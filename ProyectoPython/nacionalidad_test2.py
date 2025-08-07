#PARTE ANDRÉS SANTANA, NO SE HA IMPLEMENTADO AL MAIN 
import requests
def obt_ids():
    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
    
    respuesta = requests.get(url, timeout=100)
    if respuesta.status_code == 200:
        data = respuesta.json()
        return data.get('objectIDs', [])
    else:
        print(f"Error: {respuesta.status_code}")
        return []
    
def obt_obra_id(object_id):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None
    
def filtrar_nacionalidad(nacionalidad, max_resultados=5):
    
    resultados = []
    
    url_busqueda = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nacionalidad}"
    
    respuesta = requests.get(url_busqueda, timeout=10)
    
    if respuesta.status_code == 200:
        data = respuesta.json()
        object_ids = data.get('objectIDs', [])
        
        print(f"Se encontraron {len(object_ids)} obras para la nacionalidad '{nacionalidad}'.")

        for i, object_id in enumerate(object_ids):
            if len(resultados) >= max_resultados:
                break
                
            obra = obt_obra_id(object_id) 
            if obra:
                resultados.append({
                    "titulo": obra.get("title"),
                    "artista": obra.get("artistDisplayName"),
                    "nacionalidad": obra.get("artistNationality"),
                    "fecha": obra.get("objectDate"),
                    "departamento": obra.get("department"),
                    "url_imagen": obra.get("primaryImageSmall")
                })
                
    else:
        print(f"Error en la búsqueda: {respuesta.status_code}")
        
    return resultados
    

def mostrar_resultados(obras):
    for obra in obras:
        print(f"Título: {obra['titulo']}")
        print(f"Artista: {obra['artista']}")
        print(f"Nacionalidad: {obra['nacionalidad']}")
        print(f"Fecha: {obra['fecha']}")
        print(f"Departamento: {obra['departamento']}")
        print(f"Imagen: {obra['url_imagen']}")
        print("-" * 40)


nacionalidad = input("Ingresa la nacionalidad del autor (en inglés):")
obras_encontradas = filtrar_nacionalidad(nacionalidad)
mostrar_resultados(obras_encontradas)