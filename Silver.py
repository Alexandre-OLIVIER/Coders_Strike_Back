import sys
import math

x = 0
y = 0

while True:
    
    previousX = x
    previousY = y

    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    
    if prevX == 0:
        previousX = x
        previousY = y
    if next_checkpoint_dist < 1500: 
        thrust = 30
    if next_checkpoint_dist < 650: 
        thrust = 20
    else:
        thrust = 100
    if abs(next_checkpoint_angle) > 90:
        thrust = 0
    if next_checkpoint_dist > 5000 and abs(next_checkpoint_angle) < 5: 
        thrust = "BOOST"
    if next_checkpoint_dist < 500 and math.hypot(abs(x - x_opponent),abs(y - y_opponent)) < 850:
        thrust = "SHIELD"

    print(str(next_checkpoint_x - (x - previousX)*3)+ " " + str(next_checkpoint_y - (y - previousY)*3) + " " + str(thrust))
