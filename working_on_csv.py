# import csv

# with open('test.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count=0
#     for row in csv_reader:
#         if line_count == 0:
#             print("columns are \n", ",".join(row))
#             line_count += 1
#         else:
#             print(",".join(row))
#             line_count += 1

#     print("processng completed it")


##Writing into csv 

# import csv

# with open('employee_file.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


#using pandas 

import pandas as pd
df = pd.read_csv('test.csv')
print(df)
print(df['name'])
