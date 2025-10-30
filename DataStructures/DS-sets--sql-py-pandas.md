1️⃣ SQL — Using DISTINCT
SELECT DISTINCT customer_name
FROM customers;


✅ Output:

Asma
John
Riya
Ravi


👉 DISTINCT removes duplicate rows from that column.

🐍 2️⃣ Python — Using Set
customers = ['Asma', 'John', 'Asma', 'Riya', 'Ravi', 'John']
unique_customers = set(customers)
print(unique_customers)


✅ Output:

{'Asma', 'John', 'Riya', 'Ravi'}


👉 set() automatically removes duplicates.

🧮 3️⃣ Pandas — Using unique() and nunique()
import pandas as pd

data = pd.DataFrame({'Customer': ['Asma', 'John', 'Asma', 'Riya', 'Ravi', 'John']})

print(data['Customer'].unique())    # Shows unique values
print(data['Customer'].nunique())   # Shows count of unique values


✅ Output:

['Asma' 'John' 'Riya' 'Ravi']
4


👉 .unique() gives list of unique names
👉 .nunique() gives how many unique names (4)

💡 So to remember easily:

SQL → DISTINCT
Python → set()
Pandas → unique() / nunique()

🌍 1️⃣ Removing Duplicates

Sets automatically store unique elements.
✅ Example: You have a list of customer emails, and some are repeated.
You can use a set to keep only unique emails:

unique_emails = set(email_list)


💡 Used in: Data cleaning, CRM systems, lead management.
📋 2️⃣ Checking Membership Quickly

Sets are super fast for checking if an item exists (faster than lists).
✅ Example:

if "India" in countries_set:
    print("Yes, data available")

💡 Used in: Validations, searching keywords, checking registered users.

💼 3️⃣ Comparing Data Between Groups

You can find common or different elements easily using set operations.
✅ Example:

Students enrolled in Python vs. SQL course

Products sold last month vs. this month

common = python_set.intersection(sql_set)
only_python = python_set.difference(sql_set)


💡 Used in: Reporting, HR analysis, comparing datasets.

📊 4️⃣ Data Analysis & Filtering

In analytics or Power BI-like tasks, sets can be used in Python scripts to:

Filter out repeated data

Compare category lists

Find missing IDs between two files

💡 Used in: Data preprocessing before visualization or modeling.

🧠 5️⃣ Mathematical or Logical Problems

Sets directly support union, intersection, difference — used in:

Probability and statistics

Graph theory

Recommendation systems (common interests, mutual friends)

💬 In simple words:

Lists are for ordered data,
Dictionaries are for key-value pairs,
Sets are for unique, unordered, and mathematical operations.