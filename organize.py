import os #biblioteca de comandos sistema operacional#
import shutil #é usado para copiar e colar um arquivo de um lugar para outro#

#predefinido
#from_dir = "C:/Users/gustavo/Desktop/ggu/coisas/VSCode/[B]aula 102/imagens2"
#to_dir = "C:/Users/gustavo/Desktop/ggu/coisas/VSCode/[B]aula 102/imagens"

#input
from_dir = input("insira o caminho da pasta de onde os arquivos serão enviados: ")
to_dir = input("insira o caminho da pasta para onde os arquivos serão enviados: ")

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    
    name, extension = os.path.splitext(file_name)
                                       
    if extension == '':
        continue
    if extension  in['.gif', '.png', '.jpg', '.jpeg', '.jfif']:

        path1 = from_dir + '/' + file_name
        path2 = to_dir 
        path3 = to_dir + '/' + file_name

        if os.path.exists(path2):
            print("Movendo " + file_name + "....")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Movendo" + file_name + "....")
            shutil.move(path1, path2)