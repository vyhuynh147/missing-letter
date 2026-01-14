import os
import random
os.system('cls||clear')


#print brief welcome 
print("Welcome to the find missing words.\n")
print(" Let's try to complete full sentences.")

#list of the words for the user
words = [" chair", "phone", " enough ", " rough", " five"]

# list of sentences for random
sentences = [" The cat sat in the ___.",
 " I have ___ cookies to share with my friends.",
   " I have ___ fingers on one hand", 
   " I need a ___ to make a call.",
   " "]

# use dictionary 
sentence_word = {
    sentences[0]: "chair",
    sentences[1]: "phone",
    sentences[2]: "enough",
    sentences[3]: "rough",
    sentences[4]: "five "
}

#use def 
def start_game():
    while True:
        sentence = random.choice(sentences)
        correct_word = sentence_word[sentence]

        print("\nHere is the sentence:")
        print(sentence)
        print("Word list:", words)

        user = input("Fill the blank: ").strip().lower()

        if user == correct_word:
            print("Yes! You got it!!")
        else:
            print(" You wrong:( ")
            print(" The correct answer was", words)

# ask the user want another statement or not
more = input (" Do you want another sentences? (yes/no)").lower().strip()
if more != "yes":
    print(" Thank you for playing.")
 #   break



