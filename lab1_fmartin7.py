""" Geometry calculator
 F Martin
 Making a geometry calculator
 10/04/2026 """

from circle import calc_area as circ_calc_area, calc_circumference 
from rectangle import calc_area as rect_calc_area, calc_perimeter 





def display_menu():
    print ("1.calculate circle area")
    print ("2.calculate circle circumference")
    print ("3.calculate rectangle area")
    print ("4.calculate rectangle perimeter")
    print ("5.exit")





def select_users_choice (user_choice):
    """user chooses what options they want to calculate"""
    if user_choice == "1":
        print ("1.calculate circle area")
        radius = float(input ("Enter the radius of the circle: "))
        print ("The area of the circle is: ", circ_calc_area(radius))
    elif user_choice == "2":
        print ("2.calculate circle circumference")
        radius = float(input ("Enter the radius of the circle: "))
        print ("The circumference of the circle is: ", calc_circumference(radius))
       
    elif user_choice == "3":
        print ("3.calculate rectangle area")
        length = float(input ("Enter the length of the rectangle: "))
        width = float(input ("Enter the width of the rectangle: "))
        print ("The area of the rectangle is: ", rect_calc_area(length, width))

    elif user_choice == "4":
        print ("4.calculate rectangle perimeter")
        length= float(input ("Enter the length of the rectangle: "))
        width = float(input ("Enter the width of the rectangle: "))
        print ("The perimeter of the rectangle is: ", calc_perimeter(length, width))
    elif user_choice == "5":
        print ("5.exit")
        
    
   






if __name__ == "__main__":
    print ("Geometry Calculator")
    display_menu()
    while True:   
        user_choice = input ("Enter your choice (1-5) or 6 to quit: ")
        if user_choice == "6":
            print ("Exiting the program.")
            break
        select_users_choice (user_choice)
    
  
