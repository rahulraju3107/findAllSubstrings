word = input("Please type in a word: ")
char = input("Please type in a character: ")

index = 0
while index < len(word):
    if word[index] == char and index + 2 < len(word):
        print(word[index:index + 3])
    index += 1

"""

Please make an extended version of the previous program, which prints out all the substrings which are at least three characters long, 
and which begin with the character specified by the user. You may assume the input string is at least three characters long.

Sample output

Please type in a word: mammoth
Please type in a character: m
mam
mmo
mot

"""