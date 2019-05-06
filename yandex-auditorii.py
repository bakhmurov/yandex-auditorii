import csv
import re


def is_not_blank(s):
    return bool(s and s.strip())


def csv_writer(data, file):
    with open(file, "w", newline='') as csv_file:
        fieldnames = ['external_id', 'phone', 'email']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        for row in data:
            if (is_not_blank(row.get('phone')) & (is_not_blank(row.get('email'))) & re.sub('\ |\+|\[|\]|\(|\)|\-', '', row.get('phone'))[0:11].isdigit()):
                a = re.sub('\ |\+|\[|\]|\(|\)|\-', '', row.get('phone'))[0:11]
                b = '7' + a[1:11]
                del row['phone']
                row['phone'] = b
                writer.writerow(row)


def csv_reader(file):
    with open(file, mode='r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        data = []
        for row in reader:
            data.append(row)
        return data


def main():
    file = 'customers.csv'
    csv_writer(csv_reader(file), 'auditorii.csv')


if __name__ == "__main__":
    main()



