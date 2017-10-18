#Mitchell Locklear
#M5HW1
#CTI-110
#10/17/2017

#distance=speed*time

m = 'L'

while m == 'L':
    speed = int(input('Enter the mph: '))
    time = int(input('Enter the hours: '))
    print("Hour" '\t', "Distance Traveled")
    print("----------------------------")

    if time <= 0 or speed <= 0:
        print('Hours and mph must be greater than 0!!!')
    else:
        for t in range(0,time):
            distance = speed * (t+1)
            print(t+1, '\t' , distance)
            
        
print('End')
