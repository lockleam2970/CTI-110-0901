# CTI-110 
# M3HW2 - Software Sales
# Mitchell Locklear 
# 09/16/2017

def main():
    
    import time
    starttime=time.time()
    while True:
        Quantity = int(input('How many packages were ordered? '))
        packagePrice = 99
        
        if Quantity <= 9:
            discount = 0 
           
        elif Quantity < 20: 
            discount = .10 
            
        elif Quantity <50:
            discount = .20 
            
        elif Quantity < 100:
            discount = .30
         
        else: 
            discount = .40

        subtotal=Quantity * packagePrice
        discountAmount= subtotal * discount
        total=subtotal - discountAmount
        print('The amount of your discount is $'+ format(discountAmount, ",.2f"),'and the total cost is $'+format(total, ",.2f")+'.')
                   
        time.sleep(10.0 - ((time.time() - starttime) % 10.0))

       

              
#program start           
main()
