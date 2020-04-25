import sys
import math

laps = int(input())
checkpoint_count = int(input())
checkpoints = []
for i in range(checkpoint_count):
    checkpoint_x, checkpoint_y = [int(j) for j in input().split()]
    checkpoints.append((checkpoint_x, checkpoint_y))

while True:
    for i in range(2):
        
        x, y, vx, vy, angle, next_check_point_id = [int(j) for j in input().split()]
        
        print(checkpoints[next_check_point_id],file=sys.stderr)
        next_checkpoint_x = checkpoints[next_check_point_id][0]
        next_checkpoint_y = checkpoints[next_check_point_id][1]
                
        next_checkpoint_dist = math.hypot(abs(x - next_checkpoint_x), abs(y - next_checkpoint_y))
        print(next_checkpoint_dist,file=sys.stderr)
        if next_checkpoint_dist < 1500: 
            thrust = 30
        if next_checkpoint_dist < 1050: 
            thrust = 20
        if next_checkpoint_dist > 4000: 
            thrust = "BOOST"
        else:
            thrust = 100
            
    coord_ennemies = []
    for i in range(2):
        
        x_2, y_2, vx_2, vy_2, angle_2, next_check_point_id_2 = [int(j) for j in input().split()]
        coord_ennemies.append((x_2, y_2))
    
        X_ennemy = coord_ennemies[0][0]
        Y_ennemy = coord_ennemies[0][1]
        
        dist_between_ennemy = math.hypot(abs(x-x_2), abs(y - y_2))
        if dist_between_ennemy < 1200:
            thurst = "SHIELD"
                
    print(str(X_ennemy - 3*vx)+ " " + str(Y_ennemy - 3*vy) + " " + str(thrust))
    
    print(str(next_checkpoint_x - 3*vx)+ " " + str(next_checkpoint_y - 3*vy) + " " + str(thrust))