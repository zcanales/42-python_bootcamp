class CsvReader():
    def __init__(self, filename, sep=", ", header=False, skip_top=0, skip_bottom=0):
        print("Init function called")
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_bottom = skip_bottom
        self.skip_top = skip_top
        self.fulldata = []

    def __enter__(self):
        print("Enter function called")
        try:
            self.fd = open(self.filename, "r")
        except:
            exit("File not found")
        return self

    def __exit__(self, exec_type, exe_val, exec_tabe):
        print("Exit function called")
        self.fd.close()
    
    def getdata(self):
        self.fd.seek(self.skip_top)
        lines = self.fd.readlines()
        #if self.skip_bottom != 0:
        lines = lines[:len(lines) - self.skip_bottom - 1]
        print(lines)
        lst = []
        for line in lines:
            line = line.rstrip("\n")
            l = []
            for ls in line.split(","):
                ls = ls.rstrip()
                l.append(ls)
            lst.append(l)
        return lst

    def getheader(sef):
        self.fd.seek(0)
        if self.header is True:
            return (self.fd.readline())
        return None

if __name__ == "__main__":
    with CsvReader('good.csv', skip_top=3, skip_bottom=0) as file:
        data = file.getdata()
        print(data)
