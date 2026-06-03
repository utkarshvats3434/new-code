import time
timestamp = time.strftime("%H:%M:%S")
# print(timestamp)
hour = int(time.strftime("%H"))
hour = int(input("Enter the hour: "))
print(hour)
# minute = time.strftime("%M")
# print(minute)
# second = time.strftime("%S")
# print(second)
if(hour>=0 and hour<12):
    print("Good morning")
elif(hour>=12 and hour<18):
    print("Good afternoon")
elif(hour>=18 and hour<21):
    print("Good evening")
elif(hour>24):
    print("Invalid hour")
else:    
    print("Good night")
