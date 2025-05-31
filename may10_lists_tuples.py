Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x=[]
type(x)
<class 'list'>
list
<class 'list'>
list()
[]
num=[1,2,3,4,5,6,7]
num
[1, 2, 3, 4, 5, 6, 7]
type(num)
<class 'list'>
names=['einstein','tesla','faraday','ramanujan']
names
['einstein', 'tesla', 'faraday', 'ramanujan']

len(names)
4
len(num)
7
names[0]
'einstein'
names[1]
'tesla'
names[3]
'ramanujan'
names[4]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    names[4]
IndexError: list index out of range
names[2]
'faraday'
names[-1]
'ramanujan'
names[-2]
'faraday'
names[-3]
'tesla'
names[-4]
'einstein'

dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']



y='einstein'
y
'einstein'
y.strip()
'einstein'
y.rsplit()
['einstein']
y='    einstein'
y.strip()
'einstein'
y.rsplit()
['einstein']
y='einstein     '"
SyntaxError: unterminated string literal (detected at line 1)
y='einstein   '
y.rstrip()
'einstein'
'einstein    '.rstrip()
'einstein'
'asma shaik   '.rstrip()
'asma shaik'
'asma shaik'.rstrip()
'asma shaik'
'   asma shaik'.lstrip()
'asma shaik'
len(y)
11
y
'einstein   '
len(y)+1
12
len(y)+20
31
len(names)
4


#mutable
#add /remove values
a=[]
names
['einstein', 'tesla', 'faraday', 'ramanujan']
names.append['asma']
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    names.append['asma']
TypeError: 'builtin_function_or_method' object is not subscriptable
names.append('asma')
names
['einstein', 'tesla', 'faraday', 'ramanujan', 'asma']
a.append('apple')
a
['apple']
a.append('banana','water melon')
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.append('banana','water melon')
TypeError: list.append() takes exactly one argument (2 given)
a.append('banana'
         )
a
['apple', 'banana']
a.append('water melon')
a.append('cherry')
a
['apple', 'banana', 'water melon', 'cherry']
a.append('pine apple')
a
['apple', 'banana', 'water melon', 'cherry', 'pine apple']
veg=['brinjal','okra','bottle guard','kothmir']
veg
['brinjal', 'okra', 'bottle guard', 'kothmir']
len(veg)
4
len(a)
5
a.append(veg)
a
['apple', 'banana', 'water melon', 'cherry', 'pine apple', ['brinjal', 'okra', 'bottle guard', 'kothmir']]
len(a)
6
# here its taking entire veg as a single string as its places in a [], its considered as one.
#it counts strings which are sepearted by , in len ()
a[]-1
SyntaxError: invalid syntax
a[-1]
['brinjal', 'okra', 'bottle guard', 'kothmir']
a[0]
'apple'
a[0].upper()
'APPLE'
a[1].isupper()
False
a[2]
'water melon'
a[3]
'cherry'
a[4]
'pine apple'
a[5]
['brinjal', 'okra', 'bottle guard', 'kothmir']
a[5].isupper()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a[5].isupper()
AttributeError: 'list' object has no attribute 'isupper'
len(a)
6
#it cant give len to a[5]
len(a[5])
4
len(a[0])
5
len(a[1])
6
a
['apple', 'banana', 'water melon', 'cherry', 'pine apple', ['brinjal', 'okra', 'bottle guard', 'kothmir']]
b='asma'
len(b)
4
c="asma shaik"
len(c)
10
a
['apple', 'banana', 'water melon', 'cherry', 'pine apple', ['brinjal', 'okra', 'bottle guard', 'kothmir']]
a.upper()
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a.upper()
AttributeError: 'list' object has no attribute 'upper'
a[1].upper()
'BANANA'
a[2].isupper()
False



a
['apple', 'banana', 'water melon', 'cherry', 'pine apple', ['brinjal', 'okra', 'bottle guard', 'kothmir']]
a.remove(a[5])
a
['apple', 'banana', 'water melon', 'cherry', 'pine apple']
a.remove('gulab jamun')
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    a.remove('gulab jamun')
ValueError: list.remove(x): x not in list
a.remove('pine apple')
a
['apple', 'banana', 'water melon', 'cherry']
a.append('pine apple')
a
['apple', 'banana', 'water melon', 'cherry', 'pine apple']
a.pop()
'pine apple'
a
['apple', 'banana', 'water melon', 'cherry']
a.append('pine apple')
a
['apple', 'banana', 'water melon', 'cherry', 'pine apple']
a.pop('pine apple')
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a.pop('pine apple')
TypeError: 'str' object cannot be interpreted as an integer
a.pop(a[4])
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    a.pop(a[4])
TypeError: 'str' object cannot be interpreted as an integer
# pop removes values from end/tail-LIFO
a
['apple', 'banana', 'water melon', 'cherry', 'pine apple']
a.pop()
'pine apple'
a.remove()
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
a
['apple', 'banana', 'water melon', 'cherry']
a.remove('water melon')
a
['apple', 'banana', 'cherry']
a.pop(2)
'cherry'
a
['apple', 'banana']
a.append['water melon','cherry','pine apple']
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    a.append['water melon','cherry','pine apple']
TypeError: 'builtin_function_or_method' object is not subscriptable
a.append('water melon','cherry','pine apple')
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    a.append('water melon','cherry','pine apple')
TypeError: list.append() takes exactly one argument (3 given)
a=['apple', 'banana', 'water melon', 'cherry', 'pine apple']
a
['apple', 'banana', 'water melon', 'cherry', 'pine apple']
fruits=['apple', 'banana', 'water melon', 'cherry', 'pine apple','mango']
veg
['brinjal', 'okra', 'bottle guard', 'kothmir']


#listname.extend(another_list)
fruits.extend(veg)
fruits
['apple', 'banana', 'water melon', 'cherry', 'pine apple', 'mango', 'brinjal', 'okra', 'bottle guard', 'kothmir']
#Here we can observe that [] are missing unlike before ['apple', 'banana', 'water melon', 'cherry', 'pine apple', ['brinjal', 'okra', 'bottle guard', 'kothmir']]
fruits
['apple', 'banana', 'water melon', 'cherry', 'pine apple', 'mango', 'brinjal', 'okra', 'bottle guard', 'kothmir']
#fruits.extend(veg)- here list has been unpacked and values of another list are added
#a.append(veg)
#a
#['apple', 'banana', 'water melon', 'cherry', 'pine apple', ['brinjal', 'okra', 'bottle guard', 'kothmir']]
#a.append(veg)
#a
#['apple', 'banana', 'water melon', 'cherry', 'pine apple', ['brinjal', 'okra', 'bottle guard', 'kothmir']]



#TUPLE:
#TUPLES are immutable. they r opp of lists
#we create a tuple using a ()
#tuple, tuple() r keywords
#len and indexing r applicable
#no methods


t=()
t
()
t=('userid','password')
t
('userid', 'password')
type(t)
<class 'tuple'>
s=[]
type(s)
<class 'list'>
t.append(1)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    t.append(1)
AttributeError: 'tuple' object has no attribute 'append'
# mutable=[], immutable=()
t[0]
'userid'
t[1]
'password'
a
['apple', 'banana', 'water melon', 'cherry', 'pine apple']
1=2
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1==2
False
>>> 1+2
3
>>> 1+'2'
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    1+'2'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> #covnvert all the values in veg list into upper and add to a separate list
>>> veg
['brinjal', 'okra', 'bottle guard', 'kothmir']
>>> veg_upper=[]
>>> veg_upper=veg.upper()
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    veg_upper=veg.upper()
AttributeError: 'list' object has no attribute 'upper'
>>> veg[0]
'brinjal'
>>> veg[0].upper()
'BRINJAL'
>>> #we can assign a new var to above
>>> temp=veg[0].upper()
>>> veg[0]
'brinjal'
>>> temp
'BRINJAL'
>>> #new memory assigned to temp
>>> veg_upper.append(veg[0].upper())
>>> veg_upper
['BRINJAL']
>>> veg_upper.append('asmaveg')
>>> veg_upper
['BRINJAL', 'asmaveg']
>>> veg_upper.pop()
'asmaveg'
>>> veg_upper
['BRINJAL']
>>> veg_upper.append(veg[1].upper())
>>> veg_upper.append(veg[2].upper())
>>> veg_upper.append(veg[3].upper())
>>> veg_upper
['BRINJAL', 'OKRA', 'BOTTLE GUARD', 'KOTHMIR']
>>> veg_upper[]
SyntaxError: invalid syntax
