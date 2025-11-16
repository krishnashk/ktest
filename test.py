import os
print("this is run by jenkins")

name = os.getenv('my_name')
print("this is my",name)
