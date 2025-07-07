import os
import requests
import time

# === CONFIGURATION ===

# Dossier contenant tes .luac
input_folder = r"C:\Users\tezst\Desktop\BYTECODE DECOMPILER\BOULOT"

# Dossier où seront enregistrés les .lua
output_folder = r"C:\Users\tezst\Desktop\BYTECODE DECOMPILER\SAVE"

# Lien de l'API
api_url = "http://api.plusgiant5.com/konstant/decompile"

# Délai entre chaque requête (en secondes)
request_delay = 0.05

# === SCRIPT ===

os.makedirs(output_folder, exist_ok=True)

total_files = 0
success_count = 0
fail_count = 0

for filename in os.listdir(input_folder):
    if filename.endswith(".luac"):
        total_files += 1
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".luac", ".lua"))

        print(f"[{total_files}] Décompilation de {filename}...")

        with open(input_path, "rb") as f:
            bytecode = f.read()

        try:
            response = requests.post(api_url, headers={"Content-Type": "text/plain"}, data=bytecode)
            
            if response.status_code == 200:
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(response.text)
                print(f"✔ Sauvegardé dans {output_path}\n")
                success_count += 1
            else:
                print(f"✖ Erreur {response.status_code} pour {filename} : {response.text}\n")
                fail_count += 1

        except Exception as e:
            print(f"✖ Requête échouée pour {filename} : {e}\n")
            fail_count += 1

        time.sleep(request_delay)

print(f"\n=== Terminé : {total_files} fichiers traités | {success_count} réussis | {fail_count} échoués ===")
