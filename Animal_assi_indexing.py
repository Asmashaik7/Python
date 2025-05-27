#animal assignment using indexing
import requests
url="https://raw.githubusercontent.com/srisreedhar/DataSets/refs/heads/master/animal_sleeptime_ggplot2.csv"
resp=requests.get(url)
resp
txt=resp.text
spt=txt.split("\n")
spt=txt.split("'")
spt=txt.split(",")
spt=txt.lower()
print("number of lines=",len(spt),"\n")
print(spt)

count_c=0
count_r=0
count_p=0
for everyword in spt.split(","):
    if everyword=='carnivora':
        count_c+=1
    elif everyword=='rodentia':
        count_r+=1
    elif everyword=='primates':
        count_p+=1

print("Carnivora =",count_c,"\n" "Rodentia =",count_r,"\n" "primates=",count_p)

