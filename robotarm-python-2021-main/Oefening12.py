from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
x = 0

for i in range(9):
    robotArm.grab()
    scanResult = robotArm.scan()
    
    if scanResult != 'red':
        robotArm.drop()
        
    else:
        for i in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(9-x):
            robotArm.moveLeft()

    robotArm.moveRight()

    x+=1 

# Na jouw code wachten tot het sluiten van de window: 
robotArm.wait()