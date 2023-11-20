import os
import requests
import zipfile

os.makedirs('resources', exist_ok=True)
os.makedirs('exports', exist_ok=True)

url = 'https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/parcours-data-scientist/P2/fr.openfoodfacts.org.products.csv.zip'  # check if already exist and don't change

temp_zip_path = os.path.join('resources', 'temp.zip')

response = requests.get(url)
if response.status_code == 200:

    with open(temp_zip_path, 'wb') as temp_zip:
        temp_zip.write(response.content)

    with zipfile.ZipFile(temp_zip_path, 'r') as zip_ref:

        for file in zip_ref.namelist():
            if file.endswith('.csv'):
                zip_ref.extract(file, 'resources')
                print(f"Fichier CSV extrait : {file}")

    os.remove(temp_zip_path)
else:
    print("Erreur lors du téléchargement. Code d'état:", response.status_code)