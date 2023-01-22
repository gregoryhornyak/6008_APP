"""
Read the text into Python and store as a list of words.
You should be able to solve the following tasks in Python without using loops or recursion,
you only need the higher order functions.

T1.  Calculate the average number of letters in these words.

T2.  Calculate the average number of letters in just the words beginning with letter y.

T3.  Identify the most common letter for every word to start with.  

Use only MAP, FILTER, and REDUCE functions

-----------

T1: average number of letters
- get each word
- store into a list every_word
- get length of each word
- store into a list every_word_length
- add up the list every_word_length
- divide by the length of list every_word

-----------

T2: average number of letters if word[0] == "y"
- same but filter before getting length of each word

-----------

T3: most common first letter
- get each word
- store into a list every_word
- slice the first letter of each
- store first letters 
- max count

"""

from functools import reduce


def sliceFirstLetter(word:str)->str:
    return word[0]

def startsWithY(word:str)->bool:
    """passes if initial is a 'y' """
    return word[0]=="y"

def addThem(acc:int,n:int)->int:
    """adds up two numbers and returns them"""
    return acc+n

def lenOfWords(word:str)->int:
    """return length of arg"""
    l = len(word)
    return l

def openFile(filename:str)->list:
    """Opens the given file and returns its content after formatting [slicing/stripping/etc]"""
    with open(filename,"r") as f:
        all_lines = f.read().split("\n")
    return all_lines

def task1(filename:str):
    every_word=openFile(filename)
    len_of_each_word = list(map(lenOfWords,every_word))
    # sum up the list
    summa = reduce(addThem,len_of_each_word)
    # the return value is float or int?
    average = summa//len(len_of_each_word)
    return average

def task2(filename:str):
    every_word=openFile(filename)
    # filter the 'y' initial
    every_word_start_with_y = list(filter(startsWithY,every_word))
    len_of_each_word = list(map(lenOfWords,every_word_start_with_y))
    summa = reduce(addThem,len_of_each_word)
    # the return value is float or int?
    average = round(summa/len(len_of_each_word))
    return average
    
def task3(filename:str):
    every_word=openFile(filename)
    # slice first letter
    every_word_first_letter = list(map(sliceFirstLetter,every_word))
    # get max occurance of a letter
    out = max(every_word_first_letter,key=every_word_first_letter.count)
    return out


if __name__ == "__main__":
    file_path_and_name = "../src/words.txt"
    print("average number of letters:",task1(file_path_and_name))
    print("average number of letters if first letter is 'y':",task2(file_path_and_name))
    print("most common first letter:",task3(file_path_and_name))