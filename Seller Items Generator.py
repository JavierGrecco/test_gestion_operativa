from pip._vendor import requests
import json

#Test ID: seller_id = 179571326
site_id = "MLA"
print(f"Este script escribirá los items del sitio {site_id} como resultado.")

seller_id = input("Ingrese el id del usuario con el que desea realizar la consulta: ")
request_api = f"https://api.mercadolibre.com/sites/{site_id}/search?seller_id={seller_id}"
file_name = f"{site_id}_{seller_id}.txt"

try:
    results = requests.get(request_api).json()['results']
    with open(file_name, "w") as file:
        file.write(f"Items de site_id = '{site_id}':\n\n")
        for item in results:
            item_data = [f"ID: {item['id']}",
                         f"Título: {item['title']}",
                         f"ID de la categoria: {item['category_id']}",
                         f"Nombre de la categoría: {item['domain_id']}"]
            file.writelines("%s\n" % data for data in item_data)
            file.write("\n")
        print(f"El archivo {file_name} se ha creado correctamente en la misma ubicacion que el script.")
except:
    print("Error: El archivo no se ha guardado correctamente.")
input("Pulse alguna tecla para finalizar.")
