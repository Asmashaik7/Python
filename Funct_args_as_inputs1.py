#create a funtion that collects name, age, add, pin, phone num without collecting from the user
#transformation
#return a dictionary of values collected

def interview2(name,yob,city,edu,gender,contact):
    details={}
    current_year = 2025
    #transforamtion
    details['name']=name.upper()
    details['gender']=gender[0].upper()
    details['eduaction']=edu.capitalize()
    details['contact']=+91+int(contact)
    details['age']=current_year-int(yob)
    return details  
details=interview2('sri',2010,'wgl','bsc','male',1234567)
print("details are :",details)
