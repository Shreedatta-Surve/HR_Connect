class HandleCSV:
    filename="E:\PYTHON DEVELOPER\HR Connect\employees.csv"

    @classmethod
    def read_entire_csv(cls):
        with open(cls.filename, "r") as foo:
            return foo.readlines()

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as foo:
            for line_number, line in enumerate(foo.readlines()):
                if line_number >= 0:
                    yield line
                    line_number = line_number + 1


csvobj = HandleCSV()
result = csvobj.read_entire_csv()
print(result)
next(csvobj.read_csv_line_by_line())
