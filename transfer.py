import csv

f = open('new_contact.csv', 'r')
data = f.readlines()
for line in data:
    print(line.strip().split(';'))

with open('data_base.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerows(data)
