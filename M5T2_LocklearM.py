#Mitchell Locklear
#M5T2: Bug Collector
#CTI 110
#10/15/2017

#Initialize the accumulator
total=0
#Get the bugs collected for each day
for day in range(1,8):
    print('Enter the bugs collected on day', day)
    bugs=int(input())

    total=bugs+total
    
#Display total bugs

print('You collected a total of', total, 'bugs.')
