#CTI-110
#M3LAB Debugging
#Mitchell Locklear
#09/13/2017

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
  
    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    elif score >= 80:
        print('Your grade is: B')
    elif score >= 70:
        print('Your grade is: C')
    elif score >= 60:
        print('Your grade is: D')
    elif score <= 59:
        print('Your grade is: F')
   





# program start
main()
