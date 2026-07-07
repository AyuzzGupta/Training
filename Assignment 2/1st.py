from abc import ABC, abstractmethod
import csv


class ReportFile(ABC):
    @abstractmethod
    def save(self, name, marks):
        pass

    @abstractmethod
    def read(self):
        pass


class TextReport(ReportFile):
    def save(self, name, marks):
        f = open("students.txt", "a")
        f.write(name + "," + str(marks) + "\n")
        f.close()

    def read(self):
        f = open("students.txt", "r")
        print("Text File Records:")
        for line in f:
            d = line.strip().split(",")
            print("Name:", d[0], "| Marks:", d[1])
        f.close()


class CSVReport(ReportFile):
    def save(self, name, marks):
        f = open("students.csv", "a", newline="")
        w = csv.writer(f)
        w.writerow([name, marks])
        f.close()

    def read(self):
        f = open("students.csv", "r")
        r = csv.reader(f)
        print("CSV File Records:")
        for row in r:
            print("Name:", row[0], "| Marks:", row[1])
        f.close()


# Using polymorphism
reports = [TextReport(), CSVReport()]

students = [
    ("Ayush", 92),
    ("Priya", 88),
    ("Rahul", 75),
    ("Sneha", 95),
    ("Vikram", 81),
]

for r in reports:
    for s in students:
        r.save(s[0], s[1])
    r.read()
    print()
