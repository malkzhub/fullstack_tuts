# ##### File Objects

# import os


# # print(os.listdir(os.getcwd()))

#### Reading a file

# # ### Method for opening files non-context manager

# # f = open('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts/FileObjects_Reading_Writing_to_Files/test.txt', 'r')

# # print(f.name)
# # print(f.mode)

# # f.close()


# ### Opening file using a context manager

# with open('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts/FileObjects_Reading_Writing_to_Files/test.txt', 'r') as f:
#     # # # f_contents = f.read() # good for reading small files
#     # # # f_contents = f.readlines() 

    
#     # # # Without newlines
#     # # f_contents = f.readline() 
#     # # print(f_contents, end='')

#     # # f_contents = f.readline() 
#     # # print(f_contents, end='')

#     # # # With newlines
#     # # f_contents = f.readline() 
#     # # print(f_contents)

#     # # f_contents = f.readline() 
#     # # print(f_contents)

#     # ## Reading Extra large files
#     # for line in f:
#     #     print(line, end='')

#     ## Reading specific number of characters

#     ## Reading extra large files using loop

#     # size_to_read = 10
    
#     # f_contents = f.read(size_to_read)

#     # while len(f_contents) > 0:
#     #     print(f_contents, end='*')

#     #     f_contents = f.read(size_to_read) # will loop until it returns an empty string

    
#     ## f.seek()

#     size_to_read = 10

#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')

#     f.seek(0)

#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')

#     # print(f.tell())

# # print(f.closed) # True
# # print(f.read()) # ValueError



# ###### Writing a file

# with open('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts/FileObjects_Reading_Writing_to_Files/test2.txt', 'w') as f:
#     # f.write('Test')
#     # f.seek(0)
#     # f.write('R')



##### Using read and write methods

# # # Working with files

# with open('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts/FileObjects_Reading_Writing_to_Files/test.txt', 'r') as rf:
#     with open('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts/FileObjects_Reading_Writing_to_Files/test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)


## Working with images

# Using binary mode - add (b)

# with open('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts/FileObjects_Reading_Writing_to_Files/KratosHera.jpg', 'rb') as rf:
#     with open('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts/FileObjects_Reading_Writing_to_Files/KratosHera_Copy.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)


## Chunk
with open('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts/FileObjects_Reading_Writing_to_Files/KratosHera.jpg', 'rb') as rf:
    with open('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts/FileObjects_Reading_Writing_to_Files/KratosHera_Copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


    