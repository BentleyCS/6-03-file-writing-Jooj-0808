import random
#You need to create your own test file for this assignment.
#Because we are dealing with both reading and writing to files. Your test file will be more complicated than it has been.

def writeFile(inputList, fileName):
    #Creates a file of the given name and adds each value from the list to said file with each line being an index from the list.
    with open(fileName, 'w') as file:
        for item in inputList:
            file.write(f"{item}\n")

def sortNames(fileName, targetFile):
            with open(fileName, 'r') as f:
                names = [line.strip() for line in f.readlines()]

            names.sort()

            with open(targetFile, 'w') as f:
                for name in names:
                    f.write(name + '\n')

            print(f"sorted '{fileName}' into '{targetFile}'.")



def highScore( newScore: int):
    with open("scores.txt", "a") as f:
        f.write(f"{newScore}\n")

    with open("scores.txt", "r") as f:
        scores = [int(line.strip()) for line in f if line.strip()]

    return sum(scores) / len(scores) if scores else 0
highScore(random.randint(1,100))

