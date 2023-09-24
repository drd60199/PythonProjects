print("---Time Calculator---")

seconds = int(input("Enter a number of seconds: "))

minutes = seconds / 60
hours = seconds / 3600
days = seconds / 86400

secondsRemainder = seconds % 60
minutesRemainder = minutes % 60
hoursRemainder = hours % 24



if seconds >= 60 and seconds < 3600:
    print(f"{minutes:.0f} minutes:{secondsRemainder:.0f} seconds")
elif seconds >= 3600 and seconds < 86400:  
    print(f"{hours:.0f} hours:{minutesRemainder:.0f} minutes:{secondsRemainder:.0f} seconds")
elif seconds >= 86400:
    print(f"{days:.0f} days:{hoursRemainder:.0f} hours:{minutesRemainder:.0f} minutes:{secondsRemainder:.0f} seconds")  
else:
    print(seconds,"seconds")
