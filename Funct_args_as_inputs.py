def interview2(name,yob,city,edu,gender,contact):
    details=dict()
    current_year = 2025

    #transforamtion
    details['name']=name.upper()
    details['gender']=gender[0].upper()
    details['eduaction']=edu.capitalize()
    details['contact']=+91+int(contact)
    details['age']=current_year-int(yob)        
    return details
    
interview2('sri',2010,'wgl','bsc','male',1234567)
interview2('asma',2011,'kgm','bsc','female',456738)
interview2('manha',2012,'bdcr kgm','mba','female',4534538)
interview2('danish',2013,'hyd','mca','male',99894538)


