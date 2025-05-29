#create a funtion that collects name, age, add, pin, phone num from the user
#transformation
#return a dictionary of values collected
def interview():
    details=dict()
    #or details={}
    name = input("Please Enter your Name : ")
    yob = input("Please enter the year of your birth :")
    city = input("Please Enter your City : ")
    edu = input("Please Enter your Qualification : ")
    gender = input("Please Enter your Gender : ")
    phone_number = input("Please Enter your PhoneNumber : ")
    current_year = 2025
    #transforamtion
    details['name']=name.upper()
    details['gender']=gender[0].upper()
    details['eduaction']=edu.capitalize()
    details['contact']="+91"+phone_number
    details['age']=current_year-int(yob)
    return details
interview()
