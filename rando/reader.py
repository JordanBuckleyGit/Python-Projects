
def q1():
    inFile = open("lab5/debanks.txt", "r")

    line_number = 1
    line = inFile.readline()

    while line:
        print(f"Line {line_number}: {line.strip()}")
        line_number += 1
        line = inFile.readline()

    inFile.close()
q1()
