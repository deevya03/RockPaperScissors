from random import randint
import time

choice = ["rock", "scissors", "paper"]

def rpsRules():
    print("-------------------------------------------------")
    print("|Rock Paper Scissors Rules:                      |")
    print("|* Scissors beats paper(it cuts)                 |")
    print("|* Paper beats rock.(it wraps)                   |")
    print("|* Rock beats scissors.(it crushes)              |")
    print("-------------------------------------------------")
    

def userRSPinput():
    inputBool=True
    while inputBool:
        try:
            userRSP=int(input('press \'1\' to choose rock\npress \'2\' to choose scissor\npress \'3\' to choose paper\n'))-1
            userChoice=choice[userRSP]
            if userRSP<0 or userRSP>2:
                print("input value is not valid")
                print("please select following")
            else:
                inputBool=False
                print("******************************")
                print(f"Your Choice: {userChoice} ")
                return userRSP
        except:
                print("invalid input! Please try again")

def computerRSPguess():
    computerRSP = randint(0, 2) 
    computerChoice=choice[computerRSP]
    print(f"Computer Choice: {computerChoice}")
    print("******************************")
    return computerRSP

def decideWinner(userChoice,computerChoice):
  rpsDatabase={
        'rock': {'scissors':1, 'rock':0.5, 'paper':0},
        'paper': {'rock':1, 'paper':0.5, 'scissors':0},
        'scissors': {'paper':1,'scissors': 0.5, 'rock':0}
    }
  yourScore =rpsDatabase[userChoice][computerChoice]
  computerScore =rpsDatabase[computerChoice][userChoice]
  return yourScore,computerScore


def finalMessage(yourScore,computerScore):

  print("Cheking results...")
  if yourScore == 0:
    time.sleep(1)
    print('Ohhh....You lost!')
  elif yourScore == 0.5:
    time.sleep(1)
    print('Oops..You tied!')
  elif yourScore==1:
    time.sleep(1)
    print('Yaaay!! You won!')
  

def main():
  rpsRules()
  userRSP=userRSPinput()
  computerRSP=computerRSPguess()
  yourScore,myScore=decideWinner(choice[userRSP],choice[computerRSP])
  finalMessage(yourScore,myScore)
  
main()

repeat=True
while repeat:
      repeatRSP=input("\nEnter Y to continue and N to exit:")
      if not repeatRSP:
        print("Please enter any value!")
        continue
      elif repeatRSP.upper() == "Y":
        print("Here we go again!!")
        time.sleep(2)
        main()
      elif repeatRSP.upper()=="N":
        print("--- Thank you for playing ---")
        repeat=False
        break      
      else:
        print("Please only enter the value \'Y\' or \'N\'") 
        continue


