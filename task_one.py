import csv

with open ("employees.csv","r")as foo:
    file= csv.DictReader(foo)
    for line in file :
        bar=int(line.get("SALARY"))
        foo=line.get("PHONE_NUMBER")
        foo=foo.replace(".","")
        if bar >=9000:

            print("F_NAME:",line["FIRST_NAME"],"L_NAME:",line["LAST_NAME"],"EMAIL",line["EMAIL"],"P_NO",foo)

