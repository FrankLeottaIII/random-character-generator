#Character combination generator
#Author: Frank R. Leotta III
# date started: 2/12/2024

#discription: This program will take a certain number of characters and generate all possible combinations of those characters from a list of characters.

#Warning: This program is to be used for educational purposes only.Its original funtion was to generate combinations for youtube Ids. It is not to be used for any illegal activities. The author is not responsible for any illegal activities that may be conducted with this program.

import string
import time
import json
import random
import copy
from random import shuffle
acceptable_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_']

def two_varible_combinations():
    """Summery:
    Print all the possible combinations of 2 varibles, each varible can be filled with 64 different characters. 
    Combinations: 4096
    Execution time(with print): 0.5050396919250488 seconds
    Execution time (without print): 0.0 seconds
    """
    # start_time = time.time()
    # mega_list = []
    alphanum = string.ascii_lowercase + string.digits + string.ascii_uppercase + '-_'
    combs = [val1+val2 for val1 in alphanum for val2 in alphanum]
    # print(len(combs))
    # print(combs)
    # end_time = time.time()
    # execution_time = end_time - start_time
    # print("Execution time (without print):", execution_time, "seconds")
    return combs
# two_varible_combinations()

def three_varible_combinations():
    """Summery:
    Print all the possible combinations of 3 varibles, each varible can be filled with 64 different characters. 
    Combinations: 262144
    Execution time: Execution time (with print): 1.6041204929351807 seconds
    Execution time (without print): 0.04998922348022461 seconds
    """
    start_time = time.time()
    mega_list = []
    alphanum = string.ascii_lowercase + string.digits + string.ascii_uppercase + '-_'
    combs = [val1+val2+val3 for val1 in alphanum for val2 in alphanum for val3 in alphanum]
    # print(len(combs))
    # print(combs)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
    return combs

# three_varible_combinations()

def four_varible_combinations():
    """Summery:
    Print all the possible combinations of 4 varibles, each varible can be filled with 64 different characters. 
    Combinations: 16777216
    Execution time: Execution time (with print): 264.750097990036 second, or 4.156310081481934 minutes
    Execution time (without print): 4.156310081481934 seconds
    """
    start_time = time.time()
    mega_list = []
    alphanum = string.ascii_lowercase + string.digits + string.ascii_uppercase + '-_'
    combs = [val1+val2+val3+val4 for val1 in alphanum for val2 in alphanum for val3 in alphanum for val4 in alphanum]
    # print(len(combs))
    # print(combs)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
    return combs

# four_varible_list =  four_varible_combinations()

def five_varible_combinations_BROKEN():
    """Summery:
    MemoryError: 
    Print all the possible combinations of 5 varibles, each varible can be filled with 64 different characters. 
    Combinations: 1073741824
    Execution time: Execution time (with print): estimated 16836.0 seconds, or 4.676666666666667 hours (estimated, i refuse to waste my time on this)
    Execution time (without print): 267.0 seconds, or 4.45 minutes (estimated, MemoryError may occur)
    """
    start_time = time.time()
    mega_list = []
    alphanum = string.ascii_lowercase + string.digits + string.ascii_uppercase + '-_'
    combs = [val1+val2+val3+val4+val5 for val1 in alphanum for val2 in alphanum for val3 in alphanum for val4 in alphanum for val5 in alphanum]
    # print(len(combs))
    # print(combs)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
    return combs

def five_varible_combinations():
    """Summary:
    Apparently this is a yield funtion... I don't know what that means, but it works.
    Generate all the possible combinations of 5 variables, each variable can be filled with 64 different characters. 
    Combinations: 1073741824
    """
    alphanum = string.ascii_lowercase + string.digits + string.ascii_uppercase + '-_'
    for val1 in alphanum:
        for val2 in alphanum:
            for val3 in alphanum:
                for val4 in alphanum:
                    for val5 in alphanum:
                        yield val1 + val2 + val3 + val4 + val5
                        #so its just like my other funtions... ok not helping
# Example usage:
# for combination in five_varible_combinations():
#      print(combination)

def add_two_lists_elements(list1, list2):  
    """Summary:
    Add two lists elements together.
    """
    return [x + y for x, y in zip(list1, list2)]

def add_1_big_list_to_small_listBROKEN(big_list, small_list):
    """Summary:
    Add a big list to a small list.  You will have the same memeory issues as five_varible_combinations() if you try to do this with 5 varibles.
    """
    return [x + y for x in big_list for y in small_list]
    start_time = time.time()
    mega_list = [x + y for x in four_varible_list for y in acceptable_characters]
    start_time = time.time()
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
    json_data = json.dumps(mega_list)
    with open('mega_list.json', 'w') as file: file.write(json_data)
    print("Done")
#I just need 5 varibles and 6 varibles lists and combine them a leasure to get 11 varibles list.
    
#need to break up list into smaller lists to avoid memory error
def cut_list_in_half(big_list): #tested and it works
    """Summary:
    Cut a list in half, putting one list in 2 dictionary keys
    """
    half = len(big_list)//2
    return {'first_half': big_list[:half], 'second_half': big_list[half:]}
    
#using the cut_list_in_half funtion, you can cut the list generated by four_varible_combinations() in half, cut that in helf, until you have 2 dictionaries with 2 lists each. 
# you save all 4 of the lists to json, restart it, and just add more varibles to one of the lists so you do not have memory issues


def cut_in_half_json():
    """Summary:
    Cut the list in half and save it to a json file
    """
    json_data = json.dumps(cut_list_in_half(four_varible_list))
    with open('cut_list_in_half.json', 'w') as file: file.write(json_data)
    print("Done")


def random_eleven_varible_combinationsNOT_WORKING():
    """Summary: 
    Makes a list of random combinations of 11 varibles
    """
    start_time = time.time()
    mega_list = [] 
    alphanum = string.ascii_lowercase + string.digits + string.ascii_uppercase + '-_'
    combs = [val1+val2+val3 for val1 in alphanum for val2 in alphanum for val3 in alphanum]
    combs1 = [val1+val2 for val1 in alphanum for val2 in alphanum ]
    print("this is combs1")
    print(combs1)
    random.shuffle(combs)   
    random.shuffle(combs1)  
    #add random element of combs1 to each element of combs, stopping when there are no more elements in combs
    for i in range(len(combs)):
        random.shuffle(combs1)
        billy = combs[i] + combs1[1]
        "".join(billy)
        mega_list.append(billy)
        print (mega_list)
        time.sleep(5)
  

    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
    return combo

def write_list_to_json(data, filename):
    """Summary:
    Write a list to a JSON file.
    """
    json_data = json.dumps(data)
    with open(filename, 'w') as file:
        file.write(json_data)
    print("Done")

# seven_var_random_list = random_eleven_varible_combinations()
# # Example usage:
# write_list_to_json(seven_var_random_list, 'four_variable_list.json')

# the_file = random_eleven_varible_combinations()
# write_list_to_json(the_file, 'eleven_variable_list.json')
    



# for i in list2: Not what i am lookinf for
#     for j in acceptable_characters:
#         print(i + j)
#         time.sleep(0.5)


def even_out_list():
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8]

    if len(list1) > len(list2):
        list2.extend(list1[len(list2):])
    else:
        list1.extend(list2[len(list1):])

    print(list1)
    print(list2)





def add_list_elements_together_example():
    """Summary:
    Example funtion: Add two lists elements together.
    """
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    list2 = ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
    list3 = []
    for i in range(0, len(list1)):
        print(list1[i] + list2[i])
        list3.append(list1[i] + list2[i])

def add_list_elements_together(list1, list2):
    """Summary:
    Add two lists elements together.
    """
    list3 = []
    for i in range(0, len(list1)):
        print(list1[i] + list2[i])
        list3.append(list1[i] + list2[i])
    return list3

def random_youtube_id_generator()->str:
    """Summary:
    Generate a random youtube id.
    
    
    """
    acceptable_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_']
    random.shuffle(acceptable_characters)
    list2 = copy.deepcopy(acceptable_characters)
    shuffle(list2)
    list3 = add_list_elements_together(acceptable_characters, list2)
    shuffle(acceptable_characters)
    shuffle(list3)
    list4 = add_list_elements_together(acceptable_characters, list3)
    shuffle(acceptable_characters)
    shuffle(list4)
    list5 = add_list_elements_together(acceptable_characters, list4)
    shuffle(acceptable_characters)
    shuffle(list5)
    list6 = add_list_elements_together(acceptable_characters, list5)
    shuffle(acceptable_characters)
    shuffle(list6)
    list7 = add_list_elements_together(acceptable_characters, list6)
    shuffle(acceptable_characters)
    shuffle(list7)
    list8 = add_list_elements_together(acceptable_characters, list7)
    shuffle(acceptable_characters)
    shuffle(list8)
    list9 = add_list_elements_together(acceptable_characters, list8)
    shuffle(acceptable_characters)
    shuffle(list9)
    list10 = add_list_elements_together(acceptable_characters, list9)
    shuffle(acceptable_characters)
    shuffle(list10)
    list11 = add_list_elements_together(acceptable_characters, list10)
    return list11

print(random_youtube_id_generator())
