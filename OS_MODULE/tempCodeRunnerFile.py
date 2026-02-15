import os

os.chdir('C:/Users/ACER/Downloads/C_CODES')
print(os.getcwd())

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    file_name = file_name.strip().zfill(3)
    new_name = file_name + file_ext
    print(new_name)
