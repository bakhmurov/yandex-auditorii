import csv
import re


def csv_writer(data, file):
    with open(file, "w", newline='') as csv_file:
        fieldnames = ['\ufeffname', 'group', 'code', 'parentCode', 'measureName', 'tax', 'allowToSell', 'description', 'articleNumber', 'type', 'price', 'costPrice', 'quantity', 'barCodes', 'alcoCodes', 'alcoholByVolume', 'alcoholProductKindCode', 'tareVolume']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        # pattern = re.compile("(Германия|Италия|Франция)")
        for row in data:
            if "Австрия" in row['\ufeffname']:
                writer.writerow(row)


def csv_reader(file):
    with open(file, mode='r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        data = []
        for row in reader:
            data.append(row)
        return data


if __name__ == "__main__":
    file = 'samson.csv'
    csv_writer(csv_reader(file), 'austria.csv')
    # print(csv_reader(file))


