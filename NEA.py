
import random
#import the random module
from anytree import Node, RenderTree
#imports the Node and RenderTree 
print ("Welcome to Life Learning!\nA game filled with scenarios to help you learn life skills and morals.")
#prints the welcome message
qna = []
#creates an empty list to store the questions and answers
storefile = []
#where each line of the text file is stored
answers = []
#create an empty list
File = open("questionlist.txt", "r")
counter = 1
for x in File:
    storefile.append(x)
def Game():
    print("Welcome to the Motivational Maze! \n /\/\/\/\/\/\/\/\/\//\/\/\/\/\/\//\/\/\/\/\ \n")
    print("Pick an option:\n(Start)\n(Exit)")

Game()

print(storefile)
#creates an empty list for temporary holding of a string
temp = []
for x in storefile:
    #for each value within storefile
    print(counter,x.strip())
    #print the value of counter aswell as the current value it is looping through within storefile but stripping the value
    if counter % 4 != 0:
        #if the value of counter is not a number divisble by 4: appends the string (an answer) into the temporary list:
        temp.append(x.strip())
    else:
        #shuffles the values within temp
        random.shuffle(temp)
        #restates the value within temp to be the questions as long with the question and is perceived as one value
        temp = [x.strip(), temp]
        #then appends that current value within temp as a value within qna
        qna.append(temp)
        #and then clear the list again
        temp = []
    counter += 1

#to eventually create the qna list 
print (qna)

#perhaps create the menu now

#now I need to implement the tree part of the code
#think of more questions and answers so that I can use that as the foundation for the tree so at least I have something to use when constructing it
#think about how I am going to give a response depending on the specific answer chosen
#the type of questions which are going to be asked are open-ended, ambiguous question; essentially there are no wrong answers
#use these questions as mainly testing so that i know how to manipulate certain things when I make the actual code
#It doesn’t necessarily have an exact end: if the user wants to leave, there should be an option to end the code and then print all of the ‘morals’ whichwere outputed whilst the user was playing all at once.


#perhaps make answering the question one separate function and make another function/loop that links all the different questions and answers within a loop
#however perhaps I should link them within a tree in a specific way
#perhaps make one scenario but depending on your answer: determine which way the scenario plays out
#Target Attack: The Game, no escape game






        

