import csv

dt = (('temperatura', '25.0', 'C', '11:40', '2024-12-11'),
      ('peso', 60.0, 'kg', '11:40', '2024-12-11'))


with open('dt.csv', 'w+', encoding='utf-8') as file:
    
    out = csv.writer(file)
    out.writerows(dt)

    file.seek(0)

    data = csv.reader(file)
    for reg in data:
        print(reg)
