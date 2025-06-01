import csv

with open("data.csv", "r") as c:
    myreader = csv.reader(c)
    headers = next(myreader)
    for row in myreader:
        print(row["name"])
