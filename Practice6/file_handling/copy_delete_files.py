import os

#EX1
f = open("sample.txt", "x")
f.write("Hello")
f.close()
os.remove("sample.txt")

#EX2
if os.path.exists("sample.txt"):
  os.remove("sample.txt")
else:
  print("The file does not exist") 


#EX3
os.rmdir("testfolder") 

#EX4
import shutil
shutil.copy("test.txt", "copy_of_file.txt")   # копирует файл
shutil.copy2("test.txt", "copy_of_file.txt")  # копирует + сохраняет метаданные(время создания и изменения)