import os

def walk(dirname):
     list1=[]
     list2=[]
     for name in os.listdir(dirname):
         path=os.path.join(dirname,name)
         if os.path.isfile(path):
             list1.append(path)
             print(list1) 
         elif os.path.isdir(path):
             list2.append(path)
             print(list2)
         else:
             print("neither dir nor file")

walk(os.getcwd())
