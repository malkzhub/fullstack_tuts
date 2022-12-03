import os
import csv


os.chdir('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts/ParsingCSV_to_HTML_List')

# print(os.getcwd())

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    # csv_data = csv.reader(data_file)

    ## Using Dictionary Reader
    csv_data = csv.DictReader(data_file)

    # ## Showing output using dictionary reader
    # for item in csv_data:
    #     print(item)

    # print(list(csv_data))

    ## We don't want headers of first line of bad data
    ## We don't first line of bad data
    next(csv_data)
    # next(csv_data)

    for line in csv_data:
        ## break out in "No Reward Description"

        # ## Using csv.reader()
        # if line[0] == 'No Reward':
        #     break
        # names.append(f"{line[0]} {line[1]}")


        ## Using Dictionary Reader
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")


# for name in names:
#     print(name)

## Identifying number of contributors

html_output += f'<p>There currently {len(names)} public contributors. Thank you!</p>'

## Add unordered list in html output

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)

