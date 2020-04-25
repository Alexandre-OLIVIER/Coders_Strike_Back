import sys
import math

while True:
   
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    thrust = 0
    if next_checkpoint_angle > 90 or next_checkpoint_angle < -90: 
        thrust = str(30)
    else:
        if thrust < 50 and next_checkpoint_dist > 2500:
            thrust = "BOOST"
        else:
            thrust = str(100)

    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + thrust)