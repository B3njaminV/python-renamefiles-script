import os

remove_str = " " # Remplacer par la chaîne de caractères que vous voulez supprimer

directory = os.getcwd() # Récupère le répertoire courant

for filename in os.listdir(directory):
    if remove_str in filename:
        new_name = filename.replace(remove_str, "")

        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)

        os.rename(old_file, new_file)

        print(f'Renamed: "{filename}" to "{new_name}"')

print("Renaming complete.")

