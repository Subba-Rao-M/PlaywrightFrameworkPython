import csv
import os

csv_file_path = os.path.join(os.path.dirname(__file__), 'utilities', 'loanapp.csv')

#newline is used to avoid blank lines
with open(csv_file_path, newline='') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',') # has all rows from file
    print(csvReader)
    print(list(csvReader)) # convert into list format
    names = []
    stats = []
    for row in csvReader:
        if len(row) < 2:
            continue
        names.append(row[0])
        stats.append(row[1])

print(names)
print(stats)

index_value = names.index('Joe')
loan_status = stats[index_value]
print('loan status is '+loan_status)

# a in below refers to append the data to existing file data
with open(csv_file_path, 'a', newline='') as wFile:
    write = csv.writer(wFile)
    write.writerow(["Bob","rejected"])

# every row is list in csv file