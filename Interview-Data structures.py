# ✅ *Top Python Data Structure Interview Questions & Answers [Part-2]* 🧠🐍

# *1️⃣ Reverse a List in Python*  
# # *Answer:*  
# # ```python
my_list = [1, 2, 3, 4]
reversed_list = my_list[::-1]
print(reversed_list)
# OR
# my_list.reverse()

# *2️⃣ Find the Maximum Value in a List*  
# *Answer:*  
# ```python
nums = [4, 7, 1, 9]
max_val = max(nums)
print("max value is:",max_val)

# *3️⃣ Remove Duplicates from a List*  
# *Answer:*  
# ```python
unique = list(set([1, 2, 2, 3]))
print("unique are:",unique)
# ```

# *4️⃣ Check if Two Strings are Anagrams*  
# *Answer:*  
# ```python
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
a=is_anagram("asma","shaik")
print(a)
# ```

# *5️⃣ Count Frequency of Elements in List*  
# *Answer:*  
# ```python
from collections import Counter
Counter(['a', 'b', 'a', 'c'])
print("Count Frequency of Elements in List:", Counter)
# ```

# *6️⃣ Merge Two Lists Without Duplicates*  
# *Answer:*  
# ```python
list1 = [1, 2, 3]
list2 = [3, 4]
merged = list(set(list1 + list2))
print("merged lists without duplicates:",merged)
# ```

# *7️⃣ Find Missing Number from List (1 to N)*  
# *Answer:*  
# ```python
# def missing_number(arr, n):
#     return n*(n+1)//2 - sum(arr)
# a=missing_number([1,2,3,4,6],6)
# ```

# *8️⃣ Check for Palindrome String*  
# *Answer:*  
# ```python
def is_palindrome(s):
    return s == s[::-1]
q="asa"
p=is_palindrome(q)
print(q,"palindrome:",p)
# ```

# *9️⃣ Find the First Non-Repeating Character*  
# *Answer:*  
# ```python
from collections import Counter
def first_unique(s):
    count = Counter(s)
    for ch in s:
        if count[ch] == 1:
            return ch
s="asma shaik"
for each in s:
    c=first_unique(s)
print(c)
# ```

# *🔟 Sort Dictionary by Value*  
# *Answer:*  
# ```python
data = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(data.items(), key=lambda x: x[1]))
print("sorted dict is :",sorted_dict)