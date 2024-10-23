from datetime import datetime

import time

inp = input("Input no. of seconds: ")
print()
print("Date and Time for the following " + str(inp) + " seconds:")
i=0
while i < int(inp):

    now = datetime.now()
    mm = str(now.month)
    dd = str(now.day)
    yyyy = str(now.year)
    hour = str(now.hour)
    mi = str(now.minute)
    ss = str(now.second)

    print(dd + "/" + mm + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)
    time.sleep(1)
    i+=1
    
print()
print("Ends.")
