# CTI-110 
# QUESTION M3Q2_A-N
# Mitchell Locklear 
# 09/20/2017

def main():

    while True:
        
        SampleTemp = int(input('What is the temperature of the sample in Fahrenheit? '))

        if SampleTemp <= 32:
            print('Solid.')
        elif SampleTemp > 32 and SampleTemp <= 212:
            print('Liquid.')
        else:
            SampleTemp < 212
            print('Gas.')

   

              
#program start           
main()
