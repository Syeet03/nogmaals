from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
for y in range(1,5):
    for x in range(y):
        robotArm.grab()

        for i in range(6):
            robotArm.moveRight()

        robotArm.drop()

        for i in range(6):
            robotArm.moveLeft()

    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()