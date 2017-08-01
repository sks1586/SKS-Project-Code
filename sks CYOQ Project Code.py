# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!
# -*- coding: utf-8 -*-

print "_________________________________________________________________________________"
print
print "Welcome to my game. You will fill blank spaces, theme is...Human Body!"
print "_________________________________________________________________________________"
print
print

#Texts to be used in easy mode.
text_easy = '''Central organ in chest is ___1___, whose function is circulation.
Second organ on sides of central organ is ___2___, which is light due to air.
Third organ above central organ inside head is ___3___, whose function is controlling nervous system.
Fourth organ below central organ is ___4___, whose function is controlling urinary system.'''

answers_easy = ["Heart", "Lungs", "Brain", "Kidneys"]

#Texts to be used in medium mode.
text_medium = '''Human body has many organs. Heart distributes nutrition to entire body via ___1___.
Lungs provide ___2___ to entire body to make it function. Brain helps entire body by connecting with it via ___3___.
Kidneys help the body by eliminating toxins in ___4___.'''

answers_medium = ["Blood", "Oxygen", "Nerves", "Urine"]

#Texts to be used in hard mode.
text_hard = '''Cardiac arrest can be helped by anyone (non-MD) by ___1___.
Lungs can be used by anyone to treat hypertension by breathing exercises, which is a type of ___2___.
Brain operation can be learned to benefit humans of the universe by anyone by Udacity Nanodegree known as ___3___.
Permanent Kidney damage can be helped by donating kidneys at death, by surgery known as ___4___.'''

answers_hard = ["Chest Compression", "Yoga", "Artificial Intelligence", "Kidney Transplant"]

#spaces to be filed by the user with correct answer.
fill_spaces = ["___1___", "___2___","___3___","___4___"]

#User inputs the number of lives that he can use before before game over.
def tryout():
    try_input = raw_input("Please input the number of lives, i: ")
    min_attempts = 1
    max_attempts = 10
    for i in range (min_attempts,max_attempts):
        print i
    if int(try_input) in range(min_attempts,max_attempts):
        return "\n"+str(try_input) + "- thank you!\n"
    else:
        return None

print tryout()


#User can choose the difficulty of the game, that uses different texts and answers.
def difficulty():
    user_dif = raw_input("Please choose the game's difficulty: \nEasy \nMedium \nHard \n")
    if user_dif == "Easy":
        print "\nLet's begin!!\n"
        print text_easy
        return game(text_easy, answers_easy) #game inputs are set on easy mode.
    elif user_dif == "Medium":
        print "\nLet's begin!!\n"
        print text_medium
        return game(text_medium, answers_medium) #game inputs are set on medium mode.
    elif user_dif == "Hard":
        print "\nLet's begin!!\n"
        print text_hard
        return game(text_hard, answers_hard) #game inputs are set on hard mode.
    else:
        return difficulty()



#The game funciotn where user fills the blank spaces.
def game(text, answers):
    index = 0 #used to loop around answers
    tries = 5 # number of lives
    while index < len(answers):
        print "\nNumber of tries left: " + str(tries) + "!\n"
        user_input = raw_input("Please, insert the right word for: " + str(fill_spaces[index]))
        if user_input == answers[index]:
            text = text.replace(fill_spaces[index], answers[index])
            index = index +1
            if index == len(answers): #game is won
                return "\nCONGRATULATIONS, You are Winner!!\n"
            print "\nNice try! It's right!! Go to the next one.\n"
            print text
        else:
            remaining_attempts = 1
            if tries == remaining_attempts:
                return "\nGAME OVER ! HAHA\n"
            else:
                tries = tries -1
                print "\nOps.. Try again. You still have " + str(tries) + " lives left.\n"


print difficulty()








# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/
