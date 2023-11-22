import random
import statistics


def main():
    print("Hello User, Welcome To Higher Or Lower")
    preferences = simulationAsk()
    player = preferences[0]
    numberOfSims = preferences[1]
    simulations(player, numberOfSims)


def game():
    # deck = ["H1", "C1", "S1","D1", "H2", "C2", "S2","D2", "H3", "C3", "S3", "D3",]
    deck = ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8",
            "H9", "H10", "H11", "H12", "H13", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8",
            "S9", "S10", "S11", "S12", "S13", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8",
            "D9", "D10", "D11", "D12", "D13", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8",
            "C9", "C10", "C11", "C12", "C13", ]

    deckLength = len(deck)
    shuffledDeck = []

    while deckLength > 0:
        location = random.randint(0, deckLength - 1)
        loc1 = deck[location]
        deck.pop(location)
        shuffledDeck.append(loc1)
        deckLength = len(deck)

    firstCard = shuffledDeck[0]

    firstCardVal = int(firstCard[1:])

    secondCard = shuffledDeck[1]

    secondCardVal = int(secondCard[1:])

    return ([firstCardVal, secondCardVal, firstCard, secondCard])


def userSelection():
    userGuess = input("Guess H or L: ")
    if userGuess in ["H", "L"]:
        return (userGuess)
    else:
        print("Input is invalid, Try again!")
        return userSelection()


def comparing(streakCounter, player):
    values = game()
    firstCardVal = values[0]
    secondCardVal = values[1]

    if firstCardVal != secondCardVal:
        if firstCardVal > secondCardVal:
            correctAns = "L"
        elif firstCardVal < secondCardVal:
            correctAns = "H"

        print("the first card is", values[2])
        ###############################################################################
        ##########This Code Gets the user choice, from either human, or computer ######
        ###############################################################################

        if player == 1:
            userGuess = userSelection()
        elif player == 2:
            userGuess = stupidComputerPlayer()
        elif player == 3:
            userGuess = smarterComputerPlayer(values[2])

        print("the next card is", values[3])
        if userGuess == correctAns:
            streakCounter = streakCounter + 1
            print("Correct, streak so far is", streakCounter)
            winLog = open("winLog.csv", "a")
            winLog.write("1 \n")
            winLog.close()
            comparing(streakCounter, player)

        elif userGuess != correctAns:
            print("Wrong")
            print("Your total streak is:", streakCounter)

            # Each Player Type gets their own Files#

            if player == 1:
                streakLog = open("streakLogHuman.csv", "a")
                streakLog.write(str(streakCounter) + " \n")
                streakLog.close()
                winLog = open("winLogHuman.csv", "a")
                winLog.write("0 \n")
                winLog.close()
                with open('streakLogHuman.csv', 'r') as f:
                    data = [float(x) for x in f.read().split()]
                    mean = sum(data) / len(data)
                    print(f"The mean streak length is {mean}")


            elif player == 2:
                streakLog = open("streakLogStupid.csv", "a")
                streakLog.write(str(streakCounter) + " \n")
                streakLog.close()
                winLog = open("winLogStupid.csv", "a")
                winLog.write("0 \n")
                winLog.close()
                with open('streakLogStupid.csv', 'r') as f:
                    data = [float(x) for x in f.read().split()]
                    mean = sum(data) / len(data)
                    print(f"The mean streak length is {mean}")


            elif player == 3:
                streakLog = open("streakLogSmart.csv", "a")
                streakLog.write(str(streakCounter) + " \n")
                streakLog.close()
                winLog = open("winLogsmart.csv", "a")
                winLog.write("0 \n")
                winLog.close()
                with open('streakLogSmart.csv', 'r') as f:
                    data = [float(x) for x in f.read().split()]
                    mean = sum(data) / len(data)
                    print(f"The mean streak length is : {mean}")

        else:
            goAgain = input("It will be a draw, Go Again Y/N; ")
            if goAgain == "Y":
                comparing(streakCounter, player)
            else:
                return


def stupidComputerPlayer():
    choiceNum = random.randint(0, 1)
    hAndL = ["H", "L"]
    choice = hAndL[choiceNum]
    print("User Chose " + choice)
    return (choice)


def smarterComputerPlayer(compareWithThis):
    compareWithThis = int(compareWithThis[1:])

    if compareWithThis < 7:
        print("User Guessed H")
        return ("H")
    else:
        print("User Guessed L")
        return ("L")


def gameMode():
    ques = int(
        input("Which mode would you like to play? \n 1 Singleplayer \n 2 Stupid Simulation \n 3 Smart Simulation \n> "))
    if ques == 1:
        return (1)
    elif ques == 2:
        return (2)
    elif ques == 3:
        return (3)
    else:
        print("invalid input, go again")
        return (gameMode())


def simulationAsk():
    ques = input("Do you want to run Simulations[1] or SinglePlayerGame[2]? 1/2; ")
    if ques == "2":
        return (1, 1)
    elif ques == "1":
        numberOfTurns = int(input("Please enter the number of games you want to simulate; "))
        botType = int(input("Chose the bot you want: \n 1 Stupid Bot \n 2 Smart Bot \n > "))
        if botType == 1:

            return ([2, numberOfTurns])

        elif botType == 2:
            return ([3, numberOfTurns])
        else:
            print("invalid input, please chose again")
            simulationAsk()


def simulations(player, numberOfSims):
    for i in range(numberOfSims):
        comparing(0, player)


main()

