##OPCION 4
"""De la misma manera que en el archivo referente a buscar obras por nacionalidad, se inicia pidiéndole a la api que nos de un id dentro de los parámetros artistOrCulture
estas IDs se guardan en una lista, para que luego con la función detalles_obra se obtengan los datos requeridos de la id, con lo cual se creará un diccionario con cada ID
"""
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
"""En base a las IDs obtenidas da detalles escenciales pertenecientes a las IDs"""
def detalles_obra(object_id):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None
"""
en base al diccionario obtenido anteriormente se hace print con un bucle para cada ID
"""

def mostrar_results(obras):
  for obra in obras:
    print("<----------------------------------------------->")
    print(f"ID: {obra["ID"]}")
    print(f"Título: {obra["titulo"]}")
    print(f"Artista: {obra["artista"]}")
    print("<----------------------------------------------->")

"""
Se hace un menú con el que el usuario podrá interactuar
"""

def interfaz_user():
    while True:
        elecc = str(input("""1. Escriba el nombre del autor que quiera buscar (ejemplo: "Leonardo da Vinci"):
2. Escriba "Salir" para salir
-------------------------->
"""))
        if elecc == "2" or elecc == "salir" or elecc == "Salir":
           print("Ha salido de la herramienta")
           break
        elif elecc != "2" or elecc != "salir" or elecc != "Salir":
            obras_autor = filt_autor(elecc)
            mostrar_results(obras_autor)

    
  
