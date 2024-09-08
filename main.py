meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo",
    "CHILL": "Estar relajado"
}

print("Hola, este programa te ayudará a entender las siguientes palabras:")
print(meme_dict.keys())
print("Escribe 'SALIR' para terminar el programa.")

while True:            
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word == "SALIR":
        print("¡Adiós!")
        break
    elif word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Esa palabra no está registrada, lee las instrucciones")
