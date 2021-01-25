import shutil,os

os.chdir(r'C:\Users\Administrator\Desktop\wdl\WordToExcel')
print(os.getcwd())

for file in os.listdir():
    if '.xlsx' in file and '~$' not in file:
        print(file)
        shutil.move(file,
                    r'C:\Users\Administrator\Desktop\wdl\Excel')

# for file in os.open('Excel'):
#     shutil.move(file,r'C:\Users\Administrator\Desktop\wdl\WordToExcel')