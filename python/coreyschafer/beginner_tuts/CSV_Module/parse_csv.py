import os
import csv

'''Change current working directory first for code runner compile'''

os.chdir('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts/CSV_Module')

# # print(os.getcwd())

# cur_dir = os.getcwd()

# def filename(filename):
#     file_path = os.path.join(cur_dir, filename)

#     return file_path

# print(filename('file.txt'))


# ## Reading CSV Files

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     next(csv_reader)

#     for line in csv_reader:
#         # print(line)

#         ## Printing indexes
#         print(line[2])



#     # print(csv_reader) # returns object


# ## Writing CSV Files
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     # next(csv_reader)

#     with open('new_names.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')

#         for line in csv_reader:
#             # print(line)

#             ## Printing indexes
#             csv_writer.writerow(line)


# ## Read CSV with wrong delimiter
# with open('new_names.csv', 'r') as csv_file:
#     # csv_reader = csv.reader(csv_file)

#     ## Result
#     # ['Dave\tSmith\tdavesmith@bogusemail.com']
#     # ['Jane\tStuart\tjanestuart@bogusemail.com']

#     ## To correct this code
#     csv_reader = csv.reader(csv_file, delimiter='\t')

#     for line in csv_reader:
#         print(line)



#     # with open('new_names.csv', 'w') as new_file:
#     #     csv_writer = csv.writer(new_file, delimiter='\t')

#     #     for line in csv_reader:
#     #         # print(line)

#     #         ## Printing indexes
#     #         csv_writer.writerow(line)



### CSV data using dictionary reader and dictionary writer

with open('names.csv', 'r') as csv_file:

    ## Dictionary Reader
    # csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line['email'])


    ## Dictionary Writer
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:

            del line['email']
            csv_writer.writerow(line)