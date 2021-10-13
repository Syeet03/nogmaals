dagdeel = input('Wil je te tijd van AM of PM zien?: ')

i = 0
if dagdeel == "AM":
    while i < 13:
        print(i,': 00 AM')
        i = i + 1

elif dagdeel == "PM":
    while i < 13:
        print(i,': 00 PM')
        i = i + 1