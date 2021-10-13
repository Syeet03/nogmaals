time = 0
weekDag = ("Maandag","Dinsdag","Woensdag","Donderdag","Vrijdag","Zaterdag","Zondag")
while True:
    dag =input('Dag van de week: ')
    if dag in weekDag:
        break
  
while True:
    if dag != weekDag(time):
        print(weekDag(time))

    else:
        print(weekDag(time))
        break  
    time+=1