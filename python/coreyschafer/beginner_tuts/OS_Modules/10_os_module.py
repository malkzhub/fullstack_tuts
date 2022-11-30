# #### OS Module - Use Underlying Operating System Functionality

# import os

# from datetime import datetime

# # print(dir(os)) # shows all attributes and methods in this module

# ## Printing current working directory getcwd()
# # print(os.getcwd())

# # # Changing the current working directory
# # os.chdir('/var/www/html/fullstack_tuts/python/coreyschafer/')

# # print(os.getcwd()) # prints out the changed current directory

# # # Creating a folder in the working directory
# # os.mkdir('OS-Demo-2')
# # os.makedirs('OS-Demo-2/Sub-Dir-1') # recommended for inter-level directories

# # # Deleting folders
# # os.rmdir('OS-Demo-2') # good for deleting empty folders
# # os.removedirs('OS-Demo-2/Sub-Dir-1') # good for deleting non-empty folders

# # # Renaming fils and/or folders
# # os.rename('demo', 'demo.txt')

# ## Looking information about files
# # print(os.stat('demo.txt').st_size)
# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))

# # ## Listing files and folders in the working directory
# # print(os.listdir())


import os

from datetime import datetime

os.chdir('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts')

# for dirpath, dirnames, filenames in os.walk('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts'):
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()

# ## Environment variables
# print(os.environ.get('HOME'))

# 'text.txt'

# # file_path = os.environ.get('HOME') + 'test.txt' # problems with slashes in directories

# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)

## Other methods

print(os.path.basename('/tmp/test.txt')) # grab a filename on any type working on
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt')) # false since no filename is in that folder
print(os.path.isdir('/tmp/dsdssd')) # check if directory
print(os.path.isfile('/tmp/f01a6549-5adf-460b-9d66-6415b0bb4d5a')) # check if file
print(os.path.splitext('/tmp/test.txt'))

print()

print(dir(os.path))