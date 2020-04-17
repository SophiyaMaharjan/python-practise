hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
total_min = mins+dura

lastmin = total_min%60
result2 = int(total_min/60)
lasthour = (hour+result2)%24
print ("last time = ",lasthour,":",lastmin)
