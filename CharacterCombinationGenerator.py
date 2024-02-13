#Character combination generator
#Author: Frank R. Leotta III
# date started: 2/12/2024

#discription: This program will take a certain number of characters and generate all possible combinations of those characters from a list of characters.

#Warning: This program is to be used for educational purposes only.Its original funtion was to generate combinations for youtube Ids. It is not to be used for any illegal activities. The author is not responsible for any illegal activities that may be conducted with this program.

import string
import time
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

four_varible_list =  four_varible_combinations()

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