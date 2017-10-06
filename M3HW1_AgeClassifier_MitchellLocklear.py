# CTI-110 
# M3HW1 - Age Classifier 
# Mitchell Locklear 
# 09/13/2017

def main():

    import time
    starttime=time.time()
    while True:
        adult = 20

        age = int(input('What is the age of the person? '))

        if age >= adult:
            print('He or she is an ADULT.')
        elif age >= 13 and age < 20:
            print('He or she is a TEENAGER.')
        elif age >= 1 and age < 13:
            print('He or she is a CHILD.')
        else:
            print('He or she is an INFANT.') 
        time.sleep(10.0 - ((time.time() - starttime) % 10.0))

   

              
#program start           
main()
