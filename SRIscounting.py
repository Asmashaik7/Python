# counting letters S,R,I,s from a list
count_S=0
count_R=0
count_I=0
count_s=0
count_others=0
count_all=0
list1=list("""This is even considering spaces in the sentence and splitting. 
SRI,SIR,Sri,sri, sir,IISSSS sissSS sharp.iceage2 Remember Rose, Sid Sick Rich Idle IDLI II shahrukh salman SREE ShahI srk sk asma.""")
for letter in list1:
    count_all=count_all+1
    if letter=='S':
        count_S+=1
    elif letter=='R':
        count_R=count_R+1
    elif letter=='I':
        count_I=count_I+1
    elif letter=='s':
        count_s=count_s+1
    else:
        count_others+=1
print("S letters =",count_S,"\n" "R letters =",count_R,"\n" "I letters =",count_I,"\n" "s letters =",count_s,"\n" "Other letters =",count_others,"\n""All letters =",count_all)
