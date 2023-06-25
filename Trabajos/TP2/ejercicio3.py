import re

youtube_id_regex = r'^[a-zA-Z0-9_-]{11}$'

while True:
    youtube_id = input("Ingrese el ID de un video de YouTube (o escriba 'salir' para terminar): ")
    
    if youtube_id.lower() == "salir":
        break
    
    if re.match(youtube_id_regex, youtube_id):
        print(f"{youtube_id} es un ID de video válido de YouTube.")
    else:
        print(f"{youtube_id} no es un ID de video válido de YouTube.")