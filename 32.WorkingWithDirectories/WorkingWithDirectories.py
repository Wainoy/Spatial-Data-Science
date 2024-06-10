#paths and directories
from pathlib import Path
path = Path('ecommerce')
#path.mkdir('ecommerce')
print(path.exists())
print(Path().absolute()) #returns the current working directory
#print(path.rmdir())


#to iterate over all the paths in a directory.
from pathlib import Path
path = Path()
for file in path.glob('*'): #getting all the files in the curret dir
    print(file)

