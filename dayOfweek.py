from utilitylogic import generallogic
obj= generallogic()


date=int(input("Enter the date:"))
month=int(input("Enter the month in form of 1-12 :"))
year=int(input("Enter the year :"))
days=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


dayofweek = obj.day_of_week(date, month, year, days)