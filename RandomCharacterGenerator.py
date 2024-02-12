# random character generator
#Author: Frank R. Leotta III
# date started: 2/12/2024

# Discription:  This program contain funtions that will generate random characters and strings.  The user can specify the length of the string and the type of characters to be generated.  The user can also specify the number of strings to be generated.  The program will return the strings in a list.

#1st attempt for: youtube IDs random generator
from copy import deepcopy
import csv

acceptable_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_']

#psudo code:
"""
Goal: there are 11 different varibles that can be filled with 64 different characters.  The goal is to fill each varible with a random character from the list of acceptable characters.  The varibles will be combined to create a string of 11 characters.  This will create a mega list of all the acceptable combinations, and save it to a cvs file, then a text file.  


Future goal: Indexing:  
finding out the names and other infomration about the video with each of those combinations using pytube and perhaps beautiful soup.  Then saving the names to a text file

"""



def eleven_varible_combinations():
    """Summery:
    This function will create a list of all the possible combinations of 11 varibles, each varible can be filled with 64 different characters.  The list will be saved to a cvs file and a text file.  The function will return the list of combinations.
    """

    #create a list of all the possible combinations of 11 varibles, each varible can be filled with 64 different characters
    mega_list = []
    for a in acceptable_characters:
        for b in acceptable_characters:
            for c in acceptable_characters:
                for d in acceptable_characters:
                    for e in acceptable_characters:
                        for f in acceptable_characters:
                            for g in acceptable_characters:
                                for h in acceptable_characters:
                                    for i in acceptable_characters:
                                        for j in acceptable_characters:
                                            for k in acceptable_characters:
                                                mega_list.append(a + b + c + d + e + f + g + h + i + j + k)
    return mega_list
          
mega_list = eleven_varible_combinations()
#save the list to a cvs file
with open('mega_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(mega_list)

#save the list to a text file
with open('mega_list.txt', 'w') as file:
    for item in mega_list:
        file.write("%s\n" % item)
