# Problem Set 1: Indexing and Slicing Strings

##group members: Esteban Galvan, Ryan Ostrowski, Lance Espino##

# Basic Indexing:
# Given the string 
magic ="abracadabra"
# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find("c"))
# Advanced Slicing:
# Given the string 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
print(alphabet.find("hij"))
print(alphabet[7:10])
# it's 7 through 10

# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet.find("m"))
print(alphabet[0:12:2])
#reminder: we count FROM 0, not from 1, computers are weird

# c. Reverse the entire string using slicing.
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote2 ="Ask not what your country can do for you — ask what you can do for y-our country. - John F. Kennedy"
print(quote2.find("John"))
print(quote2[83:98])
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
string1 = "Python is fun. Fun is good. Good is subjective."
string1list = ["Python", "is", "fun", "Fun", "is", "good", "Good", "is", "subjective."]
# a. Extract the word 'subjective' without knowing its exact position.
print(string1.find("subjective"))
print(string1[36:-1])
# b. Extract every third word.
print(string1[0:0:3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.

print(str(string1list.reverse()))

####how on earth do you reverse it like this

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
sentence2 =  "MAY THE FORCE BE WITH YOU."
print(sentence2.lower())
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
wordlist = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
single_string = " ".join(wordlist)
# b. Now, split the string at every occurrence of the letter 'a'.

# Replacing Words:
sentence = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
print(sentence.replace("busy", "distracted").replace("plans", "mistakes"))
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:

# Concatenate the word "Iteration" 7 times.
print("Iteration " * 7)

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
quote = "With freedom, books, flowers, and the moon, who could not be happy?"
hasMoon = quote.find("Moonlight")
if hasMoon == -1:
    print("the word 'moonlight' is not in the poem")
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: 
phrase = "Supercalifragilisticexpialidocious."
print(len(phrase))
# b. Count the number of times the letter 'i' appears in the same word/phrase.
print(phrase.count("i"))
