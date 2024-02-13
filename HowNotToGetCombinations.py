# random character generator
#Author: Frank R. Leotta III
# date started: 2/12/2024

# Discription:  This program contain funtions that will seriously mess you up.  I mean like your computer will be running for a while, you will be wasting so much time, and you will not be happy.  This is an example of why you need to do mini tests before running a big program.
#1st attempt for: youtube IDs random generator
from copy import deepcopy
import csv
import json
import json

acceptable_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_']

#psudo code:
"""
Goal: there are 11 different varibles that can be filled with 64 different characters.  The goal is to fill each varible with a random character from the list of acceptable characters.  The varibles will be combined to create a string of 11 characters.  This will create a mega list of all the acceptable combinations, and save it to a cvs file, then a text file.  


Future goal: Indexing:  
finding out the names and other infomration about the video with each of those combinations using pytube and perhaps beautiful soup.  Then saving the names to a text file

"""
mega_list = []

#Convert the mega_list to JSON format
json_data = json.dumps(mega_list)

#Write the JSON data to a file
                    #with open('mega_list.json', 'w') as file: file.write(json_data)  #if you are crazy enough to run any of these funtions(besides the explination), you will need to comment this out.  It will start a series of events that will be of your own doing, and waste massive amounts of time and energy.  You have been warned.

# #save the list to a text file
# with open('mega_list.txt', 'w') as file:
#     for item in mega_list:
#         file.write("%s\n" % item)

# with open('The_mega_list.txt', 'w') as file:
#     for item in mega_list:
#         file.write("%s\n" % item)


def print_combination_explanation():
    "Summery:  This function will print the explanation of why loops to get all the combinations of 11 varibles is a bad idea."

    print("each character added on multiplies the number of combinations by 64. \n This is because there are 64 different characters that can be added to each varible.\n  This is why the number of combinations grows so quickly.")
    print("Here are some examples of the number of combinations for each number of characters added on:")
    print("64**2 =", 64**2)
    print("64**3 =", 64**3)
    print("64**4 =", 64**4)
    print("64**5 =", 64**5)
    print("64**6 =", 64**6)
    print("64**7 =", 64**7)
    print("64**8 =", 64**8)
    print("64**9 =", 64**9)
    print("64**10 =", 64**10)
    print("64**11 =", 64**11)
    print( "Now here is the amount of time it takes to get all the combinations for each number of characters added on:")
    print("\nIn seconds:")
    print("two_char =", 0.5050396919250488)
    print("three_char =", 32.322540283203125)
    print ("\nIn minutes:")
    print("four_char =", 34.477376302083336)
    #then HOURS...
    print("\nTHEN hours...")
    # five_char = 36.775868055555556
    print("five_char =", 36.775868055555556)
    print("\nTHEN days...")
    print("five_char =", 1.5323278356481482)
    print("six_char =", 98.06898148148149)
    print("seven_char =", 6276.414814814815)
    print("eight_char =", 401690.54814814817)
    print("nine_char =", 25708195.081481483)
    print("ten_char =", 1645324485.214815)
    print("eleven_char =", 105300767053.74815)
    print("This is why you should not run the loops to get characterd combinations for 11 varibles in loops.\n It exponentially increases in time.  I will show you a diffrerent way to do this.")



print_combination_explanation()


def two_varible_combinations_savepoint():
    """Summery:
    Print  and save to .json all the possible combinations of 2 varibles, each varible can be filled with 64 different characters.  This is save as you print version (savepoint). 
    Combinations: 4096, 
    Execution time: 62.57057309150696 seconds
    """
    acceptable_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_']

    start_time = time.time()
    mega_list = []
    for a in acceptable_characters:
        for b in acceptable_characters:
                print(a + b )
                mega_list.append(a + b)
                json_data = json.dumps(mega_list)
                with open('mega_list.json', 'w') as file: file.write(json_data)
    end_time = time.time()
    execution_time = end_time - start_time

    print("Execution time:", execution_time, "seconds")



def two_varible_combinations_SA():
    """Summery:
    Print  and save to .json all the possible combinations of 2 varibles, each varible can be filled with 64 different characters.  This is save after goin through all combinations style. Combinations: 4096, Execution time: 62.57057309150696 seconds
    Combinations: 4096
    Execution time: 0.5050396919250488 seconds


    """
    acceptable_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_']

    start_time = time.time()
    mega_list = []
    for a in acceptable_characters:
        for b in acceptable_characters:
                print(a + b )
                mega_list.append(a + b)

    json_data = json.dumps(mega_list)
    with open('mega_list.json', 'w') as file: file.write(json_data)
    end_time = time.time()
    execution_time = end_time - start_time

    print("Execution time:", execution_time, "seconds")




def eleven_varible_combinations_DONT_USE():
    """Summery:
    This function will create a list of all the possible combinations of 11 varibles, each varible can be filled with 64 different characters.  The list will be saved to a cvs file and a text file.  The function will return the list of combinations.
    WARNING:  This function will take a long time to run, and will create a very large file.  It is not recommended to run this function.  It is only here for reference.
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

                                                # Convert the mega_list to JSON format
                                                json_data = json.dumps(mega_list)

                                                # Write the JSON data to a file

                                                with open('mega_list.json', 'r') as file:
                                                    data = json.load(file)  # Load the existing JSON data

                                                    data.extend(mega_list)  # Add each element to the existing data

                                                    with open('mega_list.json', 'w') as file:
                                                        json.dump(data, file)  # Write the updated JSON data back to the file
                                                    print(a + b + c + d + e + f + g + h + i + j + k)
                                                    print('mega_list.json has been updated')


    #Convert the mega_list to JSON format
    json_data = json.dumps(mega_list)

    #Write the JSON data to a file
    with open('mega_list.json', 'w') as file: file.write(json_data)


    #save the list to a text file
    with open('The_mega_list.txt', 'a') as file:
        for item in mega_list:
            file.write("%s,\n" % item)
                                                
    return mega_list



