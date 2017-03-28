import csv

def iter_csv_file(csv_file):
    with open(csv_file) as csvfile_obj:
        reader = csv.DictReader(csvfile_obj)
        for row_dict in reader:
            yield dict((k.lower(), v) for k,v in row_dict.items())
