import _csv
import csv

with open("data.csv", 'r') as f :
    wines =list(csv.reader(f,delimiter=";"))
print(wines[:3])    