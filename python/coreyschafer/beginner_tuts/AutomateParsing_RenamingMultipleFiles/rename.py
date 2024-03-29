import os

os.chdir('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts/AutomateParsing_RenamingMultipleFiles/files')

for f in os.listdir():
    # print(f)

    ## Spliting extension from a filename

    # print(os.path.splitext(f))

    f_name, f_ext = os.path.splitext(f)

    # print(file_name.split('-'))

    f_title, f_course, f_num = f_name.split('-')

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)

    new_name = f'{f_num}-{f_title}{f_ext}'

    os.rename(f, new_name)