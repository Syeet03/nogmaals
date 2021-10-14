# name of student: Lucas van Pelt
# number of student: 99057303 

toPay = int(float(input('Te betalen bedrag: '))* 100) #
paid = int(float(input('Betaalt bedrag: ')) * 100) #
change = paid - toPay #

if change > 0: #
  coinValue = 50 #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('Maximaal ', nrCoins, ' munten van ', coinValue, ' cent terug' ) #
      nrCoinsReturned = int(input('Hoeveel munten van ' + str(coinValue) +  ' heb je terug gekregen? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: 
    if coinValue == 500:
          coinValue = 300
    elif coinValue == 300:
          coinValue = 200 
    elif coinValue == 200:
          coinValue = 100
    elif coinValue == 100:
          coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: 
  if change >= 100:
    fullchange = change % 100
    if change % 100 == 0:
          print('Niet teruggekregen: ', str(change/100) + ' euros')
    else:
          print('Niet teruggekregen: ', str((change - fullchange)/100) + ' euros and ', str(fullchange)+ ' cents')
  else:
        print('Niet teruggekregen: ', str(change) + ' cents')
else:
  print('Afgerond')