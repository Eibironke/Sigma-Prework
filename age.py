from datetime import datetime


def age_finder():
  now =  datetime.now() 
  year = int(input("Year of birth:") ) 
  month = int (input("Month of birth:"))  
  day = int(input("Day of birth:"))
  dob = datetime(year, month, day)
  age = now - dob
  age_years = int(age.total_seconds() // 31557600)
  return f"You are {age_years} years old!"

print(age_finder())