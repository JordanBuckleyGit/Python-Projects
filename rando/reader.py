
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

def q2():
    inFile = open("lab5/debanks.txt", "r")


    content = inFile.read()
    lines = content.split("\n")

    for line_number, line in enumerate(lines, start=1):
        print(f"Line {line_number}: {line}")

    inFile.close()
q2()


