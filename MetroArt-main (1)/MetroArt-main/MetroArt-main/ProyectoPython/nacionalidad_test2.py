#PARTE ANDRÉS SANTANA, IMPLEMENTADO AL MAIN 
import requests
"""
COMUNICACIÓN CON LA API, le decimos a la api que busque dentro del parámetro artisOrCulture e insertamos la nacionalidad que buscamos, se guardan IDs en una lista de resultados
Creamos un diccionario con los resultados arrojados por la función obt_obra_id
"""
def filtrar_nacionalidad(nacionalidad, max_resultados=5):
    
    resultados = []
    
    url_busqueda = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nacionalidad}"
    
    respuesta = requests.get(url_busqueda)
    
    if respuesta.status_code == 200:
        data = respuesta.json()
        object_ids = data.get('objectIDs', [])
        
        print(f"Se encontraron obras para la nacionalidad {nacionalidad}")

        for i, object_id in enumerate(object_ids):
            if len(resultados) >= max_resultados:
                break
                
            obra = obt_obra_id(object_id) 
            if obra:
                resultados.append({
                    "ID": obra.get("objectID"),
                    "titulo": obra.get("title"),
                    "artista": obra.get("artistDisplayName"),
                    "nacionalidad": obra.get("artistNationality"),
                })
                
    else:
        print(f"Error en la búsqueda: {respuesta.status_code}")
        
    return resultados
"""
Obtenemos más detalles de la obra en particular
"""
def obt_obra_id(object_id):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None  
"""Imprimimos los resultados obtenidos en base al diccionario creado anteriormente, si no se imprime nada en algunos parámetros, es que no están registrados dentro de la API """
def mostrar_resultados(obras):
    for obra in obras:
        print("<----------------------------------------------->")
        print(f"ID : {obra["ID"]}")
        print(f"Título: {obra["titulo"]}")
        print(f"Artista: {obra["artista"]}")
        print(f"Nacionalidad: {obra["nacionalidad"]}")
        print("<----------------------------------------------->")
"""
FINALMENTE CREAMOS UN MENÚ CON EL QUE EL USUARIO PODRÁ BUSCAR OBRAS CON LAS NACIONALIDADES REGISTRADAS
"""
def metod_nac():
    while True:
        
        op = str(input("""¿A cuál continente pertenece el país en el que el autor nació?
    1. África
    2. América 
    3. Asia
    4. Europa 
    5. Oceanía
    6. Salir
    ----------->
    """))

        if op == "África" or op == "1" or op == "Africa" or op == "africa" or op == "áfrica":
            op_af = str(input("""Elija la nacionalidad del autor (debe escribir la opción exactamente igual a como aparece en la lista)
    Argelia: Algerian
    Angola: Angolan
    Benín: Beninese
    Botsuana: Botswanan
    Burkina Faso: Burkinan
    Burundi: Burundian
    Cabo Verde: Cape Verdean
    Camerún: Cameroonian
    Chad: Chadian
    Comoras: Comoran
    Congo (Brazzaville): Congolese (Congo)
    Congo (RDC): Congolese (DRC)
    Costa de Marfil: Ivorian
    Djibouti: Djiboutian
    Egipto: Egyptian
    Eritrea: Eritrean
    Etiopía: Ethiopian
    Gabón: Gabonese
    Gambia: Gambian
    Ghana: Ghanaian
    Guinea: Guinean
    Guinea-Bissau: Citizen of Guinea-Bissau
    Guinea Ecuatorial: Equatorial Guinean
    Kenia: Kenyan
    Lesoto: Mosotho
    Liberia: Liberian
    Libia: Libyan
    Madagascar: Malagasy
    Malaui: Malawian
    Mali: Malian
    Marruecos: Moroccan
    Mauricio: Mauritian
    Mauritania: Mauritanian
    Mozambique: Mozambican
    Namibia: Namibian
    Níger: Nigerien
    Nigeria: Nigerian
    República Centroafricana: Central African
    Ruanda: Rwandan
    Santo Tomé y Príncipe: Sao Tomean
    Senegal: Senegalese
    Seychelles: Citizen of Seychelles
    Sierra Leona: Sierra Leonean
    Somalia: Somali
    Sudáfrica: South African
    Sudán: Sudanese
    Sudán del Sur: South Sudanese
    Suazilandia (Esuatini): Swazi
    Tanzania: Tanzanian
    Togo: Togolese
    Túnez: Tunisian
    Uganda: Ugandan
    Yibuti: Djiboutian
    Zambia: Zambian
    Zimbabue: Zimbabwean
    ---------------------> 
    """))
            obras_encontradas = filtrar_nacionalidad(op_af)
            mostrar_resultados(obras_encontradas)

        elif op == "América" or op == "2" or op == "America" or op == "america" or op == "américa":
            op_am = str(input("""Elija la nacionalidad del autor (debe escribir la opción exactamente igual a como aparece en la lista)
    Anguila: Anguillan
    Antigua y Barbuda: Citizen of Antigua and Barbuda
    Argentina: Argentine
    Bahamas: Bahamian
    Barbados: Barbadian
    Belice: Belizean
    Bermudas: Bermudian
    Bolivia: Bolivian
    Brasil: Brazilian
    Canadá: Canadian
    Chile: Chilean
    Colombia: Colombian
    Costa Rica: Costa Rican
    Cuba: Cuban
    Dominica: Dominican
    Ecuador: Ecuadorean
    El Salvador: Salvadorean
    Estados Unidos: American
    Granada: Grenadian
    Groenlandia: Greenlandic
    Guatemala: Guatemalan
    Guayana: Guyanese
    Haití: Haitian
    Honduras: Honduran
    Islas Caimán: Cayman Islander
    Islas Turcas y Caicos: Turks and Caicos Islander
    Islas Vírgenes Británicas: British Virgin Islander
    Jamaica: Jamaican
    Martinica: Martiniquais
    México: Mexican
    Montserrat: Montserratian
    Nicaragua: Nicaraguan
    Panamá: Panamanian
    Paraguay: Paraguayan
    Perú: Peruvian
    Puerto Rico: Puerto Rican
    República Dominicana: Citizen of the Dominican Republic
    San Cristóbal y Nieves: Kittitian
    San Vicente y las Granadinas: Vincentian
    Santa Elena: St Helenian
    Santa Lucía: St Lucian
    Surinam: Surinamese
    Trinidad y Tobago: Trinidadian
    Uruguay: Uruguayan
    Venezuela: Venezuelan
    ------------------>
    """))
            obras_encontradas = filtrar_nacionalidad(op_am)
            mostrar_resultados(obras_encontradas)

        elif op == "Asia" or op == "3" or op == "asia":
            op_as = str(input("""Elija la nacionalidad del autor (debe escribir la opción exactamente igual a como aparece en la lista)
    Afganistán: Afghan
    Arabia Saudí: Saudi Arabian
    Armenia: Armenian
    Azerbaiyán: Azerbaijani
    Baréin: Bahraini
    Bangladés: Bangladeshi
    Bhután: Bhutanese
    Brunéi: Bruneian
    Birmania (Myanmar): Burmese
    Camboya: Cambodian
    China: Chinese
    Corea del Norte: North Korean
    Corea del Sur: South Korean
    Emiratos Árabes Unidos: Emirati
    Filipinas: Filipino
    Georgia: Georgian
    Hong Kong: Hong Konger
    India: Indian
    Indonesia: Indonesian
    Irak: Iraqi
    Irán: Iranian
    Israel: Israeli
    Japón: Japanese
    Jordania: Jordanian
    Kazajistán: Kazakh
    Kirguistán: Kyrgyz
    Kuwait: Kuwaiti
    Laos: Lao
    Líbano: Lebanese
    Macao: Macanese
    Malasia: Malaysian
    Maldivas: Maldivian
    Mongolia: Mongolian
    Nepal: Nepalese
    Omán: Omani
    Pakistán: Pakistani
    Palestina: Palestinian
    Catar: Qatari
    Singapur: Singaporean
    Sri Lanka: Sri Lankan
    Siria: Syrian
    Taiwán: Taiwanese
    Tayikistán: Tajik
    Tailandia: Thai
    Timor Oriental: East Timorese
    Turkmenistán: Turkmen
    Turquía: Turkish
    Uzbekistán: Uzbek
    Vietnam: Vietnamese
    Yemen: Yemeni
    ------------->
    """))
            obras_encontradas = filtrar_nacionalidad(op_as)
            mostrar_resultados(obras_encontradas)
        elif op == "Europa" or op == "4" or op == "europa":
            op_eu = str(input("""Elija la nacionalidad del autor (debe escribir la opción exactamente igual a como aparece en la lista)
    Alemania: German
    Andorra: Andorran
    Austria: Austrian
    Bielorrusia: Belarusian
    Bélgica: Belgian
    Bosnia y Herzegovina: Citizen of Bosnia and Herzegovina
    Bulgaria: Bulgarian
    Chipre: Cypriot
    Ciudad del Vaticano: Vatican citizen
    Croacia: Croatian
    Dinamarca: Danish
    Escocia: Scottish
    Eslovaquia: Slovak
    Eslovenia: Slovenian
    España: Spanish
    Estonia: Estonian
    Finlandia: Finnish
    Francia: French
    Gales: Welsh, Cymro, Cymraes
    Gibraltar: Gibraltarian
    Grecia: Greek
    Holanda: Dutch
    Hungría: Hungarian
    Inglaterra: English
    Irlanda: Irish
    Irlanda del Norte: Northern Irish
    Islandia: Icelandic
    Italia: Italian
    Kosovo: Kosovan
    Letonia: Latvian
    Liechtenstein: Liechtenstein citizen
    Lituania: Lithuanian
    Luxemburgo: Luxembourger
    Macedonia del Norte: Macedonian
    Malta: Maltese
    Moldavia: Moldovan
    Mónaco: Monegasque
    Montenegro: Montenegrin
    Noruega: Norwegian
    Polonia: Polish
    Portugal: Portuguese
    Reino Unido: British, Prydeinig
    República Checa: Czech
    Rumanía: Romanian
    Rusia: Russian
    San Marino: Sammarinese
    Serbia: Serbian
    Suecia: Swedish
    Suiza: Swiss
    Ucrania: Ukrainian
    -------------------->
    """))
            obras_encontradas = filtrar_nacionalidad(op_eu)
            mostrar_resultados(obras_encontradas)
        elif op == "Oceanía" or op =="5" or op =="Oceania" or op == "oceania" or op == "oceanía":
            op_oc = str(input("""Elija la nacionalidad del autor (debe escribir la opción exactamente igual a como aparece en la lista)
    Australia: Australian
    Fiyi: Fijian
    Islas Cook: Cook Islander
    Islas Feroe: Faroese
    Islas Marshall: Marshallese
    Islas Pitcairn: Pitcairn Islander
    Islas Salomón: Solomon Islander
    Kiribati: Citizen of Kiribati
    Micronesia: Micronesian
    Nauru: Nauruan
    Niue: Niuean
    Nueva Zelanda: New Zealander
    Palaos: Palauan
    Papúa Nueva Guinea: Papua New Guinean
    Samoa: Samoan
    Tokelau: Tokelauan
    Tonga: Tongan
    Tristán de Acuña: Tristanian
    Tuvalu: Tuvaluan
    Vanuatu: Citizen of Vanuatu
    Wallis y Futuna: Wallisian
    __---------------------->
    """))
            obras_encontradas = filtrar_nacionalidad(op_oc)
            mostrar_resultados(obras_encontradas)
        elif op == "Salir" or op == "6" or op == "salir":
            print("Ha salido de la opción")
            break








