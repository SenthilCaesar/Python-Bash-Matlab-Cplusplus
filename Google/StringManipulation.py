import re
import itertools

def removeWhitespace(string):
    return re.sub(r'\s+', '', string)

def palindrome(x):
    j = len(x)
    for i in range(0, j//2):
        if x[i] != x[j-1]:
            return False
        j -= 1
    return True

def PowerSet(given):
    '''Function prints all subsequences or Power set '''
    str_list = list(given)
    combos = []
    powerset = []
    for i in range(0, len(str_list)+1):
        ''' itertools returns an iterable object of tuples '''
        combos.append(itertools.combinations(str_list, i))

    for iterable in combos:
        for combinations in iterable:
            combined = ''.join(str(x) for x in combinations)
            ''' All Non-empty Subsequences '''
            if combined != '':
                powerset.append(int(combined))
    print("All subsequences of", given)
    print(powerset)
    
def Longest_common_prefix(given):
    prefix = {}
    for string in given:
        length = len(string)
        for i in range(0, length):
            key = string[0:i+1]
            if key in prefix:
                prefix[key] += 1
            else:
                prefix[key] = 1
            
    longest_common_p = ''
    for key in prefix:
       longest = 0   
       if prefix[key] == len(given):
           if len(key) > longest:
               longest = len(key)
               longest_common_p = key
            
    if len(longest_common_p) > 0:
        print("Longest common prefix in", given, " = ", longest_common_p)
    else:
        print("There is no common prefix among the input strings")  
        
def startEnd(string, substring):
    count = 0
    l = len(string)
    for i in range(0, l):
        for j in range(i, l):
            substring.append(string[i:j+1])
    for sub in substring:
        if len(sub) > 1 and sub[0] == '1' and sub[len(sub)-1] == '1':
            count += 1
    return count    
    
def lenghtofLongsubstring(string, substring):
    longest = 0
    l = len(string)
    string = string.lower()
    for i in range(0, l):
        for j in range(i, l):
            substring.append(string[i:j+1])
            
    for sub in substring:
        if palindrome(sub) == True:
            if len(sub) > longest:
                longest = len(sub)
                longest_palindrome = sub
    print(longest_palindrome, "is the longest substring which is palindrome")
    substring = []
    
def lenghtofLongsubsequence(string):
    longest = 0
    str_list = removeWhitespace(string)   
    str_list = str_list.lower()
    str_list = list(str_list)
    combos = []
    for i in range(0, len(str_list)+1):
        ''' itertools returns an iterable object of tuples '''
        combos.append(itertools.combinations(str_list, i))

    for iterable in combos:
        for combinations in iterable:
            combined = ''.join(str(x) for x in combinations)
            ''' All Non-empty Subsequences '''
            if combined != '':

                if palindrome(combined) == True:
                    if len(combined) > longest:
                        longest = len(combined)
                        longest_palindrome = combined
    if len(longest_palindrome) == 1:
        print("No Plaindrome found in subequences of string", string)
    else:
        print(longest_palindrome, "is the longest subsequence which is palindrome found in string", string)

def highestConcat(arr):
    combinations = itertools.permutations(arr)
    maximum = 0
    for tup in combinations:
        concat = ''.join(str(x) for x in tup)
        if int(concat) > maximum:
            maximum = int(concat)
            combo = tup
    return list(combo)

def seenSubstring(string):
    substring = {}
    l = len(string)
    for i in range(0, l):
        for j in range(i+1, l):
            sub = string[i:j+1] 
            if sub in substring:
                substring[sub] += 1
                print("Substring that has been seen previously in", string, "= ", string[i:j+2])
                break
            else:
                substring[sub] = 1
            
def RemoveAlternativeDuplicate(string):
    seen = {}
    given = string.lower()
    given = list(given)
    for i in range(0, len(given)):
        c = given[i]
        if c in seen:
            seen[c] += 1
            given[i] = "$"            
            del seen[c]
        else:
            seen[c] = 1
            
    concat = ''.join(x for x in given)
    concat = concat.replace("$", "")
    return concat

def string2Words(given, my_dict):
    length = len(given)
    given = given.lower()
    for i in range(0, length):
        word1 = given[0:i+1]
        word2 = given[i+1:length]
        ''' Print if both the words are in dictionary '''
        if word1 in iter(my_dict.values()) \
            and word2 in iter(my_dict.values()):
                print(word1, word2)
                
def combinations(string, size):
    lst = list(string)
    combinations = set(itertools.permutations(lst, size))
    combos = []
    for tup in combinations:
        combine = ''.join(tup)
        combos.append(combine)
        
    for combined in combos:
        if palindrome(combined) == True:
           print(combined + ' ', end="")

#----------------------------------Test---------------------------------------#    
x = 'malayalam rotator'
substring = []
string = x.lower()
string = removeWhitespace(string)
ans = palindrome(string)
if ans == True:
    print(string, "is a Palindrome")
else:
    print(string, "is not a Palindrome")

print()
lenghtofLongsubstring(string, substring)
print()
print("Combinations of size 4 of", string, "which are also palindromes:")
combinations(string, 4)

num='0010110010'
count = startEnd(num, substring)
print("\n")
print("Number of substrings in", num,"which starts and end with a 1 = ", count)
print()
arr=[9, 93, 24, 6]
output = highestConcat(arr)
print("Highest number formed by concatening elements in", arr,"=", output)
print()
given = "you got beautiful eyes"
output_string = RemoveAlternativeDuplicate(given)
print("Removed alternate characters from", given, " = ", output_string)
print()
seenSubstring(x)
print()
given = ["flower","flow","flight"]  
Longest_common_prefix(given)
print()
my_dict = {1:'flip', 2:'is', 3:'easy', 4:'with', 5:'shop', 6:'shopping', 7:'flipkart',
           8:'ping', 9:'hop', 10:'hopping', 11:'lip', 12:'art', 13:'sea', 14:'car',
           15:'cart', 16:'map', 17:'mapping', 18:'app', 19:'a', 20:'man', 21:'an',
           22:'water', 23:'melon', 24:'am'}
given = 'WaterMelon'
string2Words(given, my_dict)
print()
given = '1234'
PowerSet(given)
print()
given = 'under qualified'
lenghtofLongsubsequence(given)
