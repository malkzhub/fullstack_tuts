
# # try:
# #     f = open('test_file.txt')
# #     # var = bad_var
# # # except Exception:
# # #     print('Sorry. This file does not exist')
# # # except FileNotFoundError:
# # #     print('Sorry. This file does not exist')
# # # except Exception:
# # #     print('Sorry. Something went wrong')
# # except FileNotFoundError as e:
# #     print(e)
# # except Exception as e:
# #     print(e)
# # else:
# #     pass
# # # finally:
# # #     pass

import os

os.chdir('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts/Exceptions')


# try:
#     f = open('test_file.txt')
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     f.close()
# finally:
#     print("Excecuting Finally...")

# ## else clause - runs if no error was thrown in the exception
# ## finally - runs no matter what happens. Successful or not


### Corrupt File

try:
    f = open('corrupt_file.txt')
    # if f.name == 'corrupt_file.txt':
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print('Excecuting Finally...')
