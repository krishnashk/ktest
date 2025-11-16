import os
print("this is run by jenkins")

name = os.getenv('USERNAME')
print("this is my",name)
