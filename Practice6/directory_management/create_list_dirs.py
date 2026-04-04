import os

#ex1 создает папку
os.mkdir("test1_fol")

#ex2  создает вложенные папки
os.makedirs("lv1/lv2/lv3")

#or 

os.makedirs("parent/child", exist_ok = True)

#ex3 список папок 

files = os.listdir()
print(files)
#ex 4 открывает папки, ".." выход в папку на уровень выше
os.chdir("parent/child")
os.chdir("..")
#ex5 указывает путь
a = os.getcwd()
print(a)
#ex6 удаление пустой папки, в ином случае ошибка
os.rmdir("child")