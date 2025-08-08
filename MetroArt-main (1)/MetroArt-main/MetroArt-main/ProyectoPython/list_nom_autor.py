##OPCION 4 NO SE HA IMPLEMENTADO AL MAIN
import requests
def filt_autor(autor, max_res = 10):
  resultados = []
  url_busq = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={autor}"
  respuesta = requests.get(url_busq)

  if respuesta.status_code == 200:
    data = respuesta.json()
    object_ids = data.get("objectIDs", [])
    print(f"Se encontraron obras para el nombre {autor}")

    for i, object_id in enumerate(object_ids):
      if len(resultados) >= max_res:
        break
      obra = detalles_obra(object_id)
      if obra:
        resultados.append({
          "ID": obra.get("objectID"),
          "titulo": obra.get("title"),
          "artista": obra.get("artistDisplayName")
        })
  else:
    print(f"Error en la búsqueda: {respuesta.status_code}")
  return resultados
def detalles_obra(object_id):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None
def mostrar_results(obras):
  for obra in obras:
    print(f"ID: {obra["ID"]}")
    print(f"Título: {obra["titulo"]}")
    print(f"Artista: {obra["artista"]}")

def interfaz_user():
  elecc = str(input("Escriba el nombre del autor que quiera buscar: "))
  obras_autor = filt_autor(elecc)
  mostrar_results(obras_autor)
    
  
