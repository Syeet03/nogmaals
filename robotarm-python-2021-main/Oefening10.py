from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
for i in range(5):
    robotArm.grab()

    for i in range(5):
        robotArm.moveRight()

    robotArm.drop()

    for i in range(4):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()