import csv
import datetime

with open ("employees.csv","r") as foo:
    file=csv.DictReader(foo)

    for line in file:
        first_name=line.get("FIRST_NAME")
        last_name=line.get("LAST_NAME")

        date=line.get("HIRE_DATE")
        dept_id=int(line.get("DEPARTMENT_ID"))

        salary=line.get("SALARY")
        salary=int(salary)

        date=datetime.datetime.strptime(date,"%d-%b-%y")

        if dept_id > 30 and dept_id <110 and salary > 4200:
            print(date,"\n",first_name,last_name)


