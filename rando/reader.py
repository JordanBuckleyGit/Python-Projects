
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

def q3():
    inFile = open("lab5/debanks.txt", "r")

    lines = inFile.readlines()

    for line_number, line in enumerate(lines, start=1):
        print(f"Line {line_number}: {line.strip()}")

    inFile.close()
q3()

def q4():
    inFile = open("lab5/debanks.txt", "r")

    with open("lab5/debanks.txt", "r") as inFile:
        for line_number, line in enumerate(inFile, start=1):
            print(f"Line {line_number}: {line.strip()}")

    inFile.close()
q4()

def q5():
    with open("lab5/dna.txt", "r") as inFile:
        content = inFile.read()

    dna_sequences = content.split("\n")

    for person_id, dna in enumerate(dna_sequences):
        print(f"{person_id}: {dna.strip()}")

    inFile.close()
q5()
