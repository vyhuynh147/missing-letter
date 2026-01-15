import os
import random
import time 
os.system('cls||clear')


#print brief welcome 
print("Welcome to the find missing words. ^--^\n")
print(" Let's try to complete full sentences.")

#list of the words
words = [" chair", "phone", "enough", "rough", " five", "very", "hair", "kite", "park","leaf","routine"]

# list of sentences for random
sentences = ["The cat sat in the _____.",
             "I need a _____ to make a call.",
             "I have ______ cookies to share with my friends.",
             "The bumpy road was very _____.",
             "I have ____ fingers on one hand.",
             "He was ____ upset and cried. ",
             "Can you tie your ____?",
             "I saw a ____ fly across the sky.",
             "Let's go for a walk in the ____.",
             "The ____ on the tree as bright red.",
             "When she woke up, she did her morning ______."
]

# use dictionary 
sentence_word = {
    sentences[0]: "chair",
    sentences[1]: "phone",
    sentences[2]: "enough",
    sentences[3]: "rough",
    sentences[4]: "five",
    sentences[5]: "very",
    sentences[6]: "hair",
    sentences[7]: "kite",
    sentences[8]: "park",
    sentences[9]: "leaf",
    sentences[10]:"routine"
}

#use def to play game
def start_game():
    while True:
        sentence = random.choice(sentences)
        correct_word = sentence_word[sentence]

        print("Word list:", words)
        print("\nHere is the sentence:")
        print(sentence)
        

        user = input("Fill the blank: ").strip().lower()

        if user == correct_word:
            print("Yes! You got it!!")
            time.sleep(2.5)
            os.system('cls||clear')
        else:
            print(" You wrong:( ")
            print ("The correct answer was:", correct_word)
            time.sleep(2.5)
            os.system('cls||clear')

# ask the user want another sentences or not
        more = input (" Do you want another sentences? (yes/no): ").lower().strip()
        if more != "yes":
            print(" Thank you for playing.")
            break 
        else:
            time.sleep(1.0)
            os.system('cls||clear')
start_game()



