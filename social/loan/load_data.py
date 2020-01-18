import csv
from models import User

with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = User.objects.get_or_create(
            name=row[0],
            item=row[1],
            value=row[2],
            )
