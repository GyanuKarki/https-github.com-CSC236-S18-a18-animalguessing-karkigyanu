
#####Animal guessing game####
###THIS DOES not work, havent had time to work on it######
#####

import json

def playgame(data):

    if "Answer" in data:
        print(data["Answer"])

        correctguess=input("is our guessed animal correct?")
        if correctguess=="yes":
            print("Thank you for playing game!")
            return
        elif correctguess == "no":
            incorrect = data["Answer"]
            correct=input("Input your animal name: ")
            question=input("Enter a question to distinguish ")
            data["Q"]=question
            data["yes"]={"Answer":correct}
            data["no"]={"Answer": incorrect}
            del data["Answer"]

        return


    print(data["Q"])
    user=input("Answer yes or no")
    if user == "yes":
        return playgame(data["yes"])
    elif user =="no":
        return playgame(data["no"])



def main():

    datafile=open("ask.json","r")
    data=json.load(datafile)

    while True:
        playgame(data)

        datafile.close()

        writefile=open("ask.json", "w")
        json.dump(data, writefile)
        writefile.close()



main()
