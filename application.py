import os
import nbformat
import subprocess
from nbformat.v4 import new_notebook , new_code_cell

directory = os.path.join(os.getcwd())
def create_branch_and_commit(branch_name, function_to_run, commit_message):
    subprocess.run(["git", "checkout", "-b", branch_name])
    function_to_run()
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "checkout", "main"])

def create_project_structure():

    directory = os.path.join(os.getcwd())
    folders = ["data/raw", "data/cleaned", "docs",
               "models", "notebooks", "reports", "src"]


    for folder in folders:
            
            folder_path = os.path.join(directory, folder)
            os.makedirs(folder_path, exist_ok=True)
            # Crée un fichier .gitkeep dans les dossiers vides pour qu'ils soient suivis
            with open(os.path.join(folder_path, ".gitkeep"), 'w') as f:
                pass

def create_initial_files():

    files = ["LICENSE", "Makefile", "README.md", ".gitignore",
             "requirements.txt"]

    for file in files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'w') as f:
            file_content = ''
            f.write(file_content)


def add_specific_files():

    # verifiez si les dossiers existe deja 
    os.makedirs('notebooks', exist_ok=True)
    # Ajoutez une cellule de code au notebook et remplissage du fichier mains.ipynb du notebook
    notebook = new_notebook()
    code_source = "print('Hello, world!')"
    cell = new_code_cell(source=code_source)
    notebook.cells.append(cell)
    main_notebook_path = os.path.join(directory, "notebooks/main.ipynb")
    if not os.path.exists(main_notebook_path):
    
        with open(main_notebook_path, "w") as main_notebook_file:
            nbformat.write(notebook,main_notebook_file)
    # ajout du fichier utils.py
    if not os.path.exists("src/utils.py"):
        with open("src/utils.py", "w") as readme_file:
            readme_file.write("")


def main():
   
    create_branch_and_commit("ticket1", create_project_structure, "Ajout de la structure de base du projet. Closes #1")
    create_branch_and_commit("ticket2", create_initial_files, "Ajout des fichiers initiaux. Closes #2")
    create_branch_and_commit("ticket3", add_specific_files, "Ajout des fichiers spécifiques. Closes #3")
main()