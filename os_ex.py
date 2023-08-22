import os

# print(os.name())

# os.makedirs('d:\\makedir_test')
print(os.getcwd()) #returns the current working directory(CWD) of the file.
os.chdir('d:\\work related\\Shivani')
print(os.listdir()) #list files and sub directories 

cwd_path = os.getcwd()
# new_dir = 'test_path'

# path_to_create = os.path.join(cwd_path,new_dir)
# print(path_to_create)

# os.makedirs(path_to_create) #makedirs()-->it will create the parent dir also if is not present. 
                            #makedir() -> it will create the durectory only 
                            #without any parent directory creation if it's not present

#os.rmdir() --> delete an empty dir 
#os.remove() --> remove file 

# for root, dirs, files in os.walk(cwd_path):
#     for file in files :
#         print(os.path.join(root, file))
    
#     for dir in dirs :
#         print("----------------------#####################-----------------------")
#         print(os.path.join(root, dir))


result = os.path.exists("a.txt") #giving the name of the file as a parameter.
  
print(result)

print(os.path.basename('D:\Work related\Shivani\Python\os_ex.py'))  #returns os_ex.py

print(os.path.split('D:\Work related\Shivani\Python\os_ex.py'))  #('D:\\Work related\\Shivani\\Python', 'os_ex.py')

print(os.path.dirname('D:\Work related\Shivani\Python\os_ex.py'))  #D:\Work related\Shivani\Python

print(os.path.commonprefix(['/home/webadmin/shivani/a.txt', '/home/temp/a.txt', '/home/www/a/b.txt', '/home/bbb/a/b.txt']))   #/home , returns the longest path prefix 
                                                                                                                              #which is a prefix for all the paths in the specified list.

print(os.path.isfile('D:\Work related\Shivani\Python\os_ex.py'))  #True

print(os.path.isdir('D:\Work related\Shivani\Python\os_ex.py')) #False

print(os.path.isdir('D:\Work related\Shivani\Python'))  #True

print(os.path.isabs('D:\Work related\Shivani\Python\os_ex.py'))  #True

print(os.path.isabs('os_ex.py'))  #False