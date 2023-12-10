import math as math

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def arg(real,imaginary):
    angle = math.degrees(math.atan(imaginary/real))
    #Because if a number in the division is negative the angle will be negative,hate negative angles
    if angle<0: positive_angle = angle+360
    else: positive_angle=angle
    
    #Real and imaginary comparison for angle veracity
    if real>0 and imaginary>0: quadrant_1 = True
    else: quadrant_1 = False
    if real<0 and imaginary>0: quadrant_2 = True
    else: quadrant_2 = False
    if real<0 and imaginary<0: quadrant_3 = True
    else: quadrant_3 = False
    if real>0 and imaginary<0: quadrant_4 = True
    else: quadrant_4 = False
    
    #To check in what quadrant is positive_angle 
    if 90<positive_angle<0: angled_1_quadrant = True
    else: angled_1_quadrant = False
    if 180<positive_angle<90: angled_2_quadrant = True
    else: angled_2_quadrant = False
    if 270<positive_angle<180: angled_3_quadrant = True
    else: angled_3_quadrant = False
    if 360<positive_angle<270: angled_4_quadrant = True
    else: angled_4_quadrant = False
    
    #Checks if both quadrants (the expected and the returned) are the same, 
    #if they aren't, adds 180º to translate to the other quadrant. Meaning the conjugate angle
    if quadrant_1 and angled_1_quadrant is True: return positive_angle
    elif quadrant_2 and angled_2_quadrant is True: return positive_angle
    elif quadrant_3 and angled_3_quadrant is True: return positive_angle
    elif quadrant_4 and angled_4_quadrant is True: return positive_angle
    else: real_angle = positive_angle+180
    
    if real_angle>360: simplified_real_angle = real_angle-360
    else: return real_angle
    return simplified_real_angle

print()
parameter_a = int(input("   The first parameter of the second-order polynomial equation is: "))
print()
parameter_b = int(input("   The second parameter of the second-order polynomial equation is: "))
print()
parameter_c = int(input("   The third parameter of the second-order polynomial equation is: "))
print()

#imaginary checker
rooted_equation = ((parameter_b)**2)-(4*parameter_a*parameter_c)

#Complex Number operations
first_real_part= -(parameter_b)/(2*parameter_a)
first_imaginary_part= (math.sqrt(abs(rooted_equation)))/(2*parameter_a)
second_real_part= -(parameter_b)/(2*parameter_a)
second_imaginary_part= -(math.sqrt(abs(rooted_equation)))/(2*parameter_a)
absolute_second_imaginary_part= abs(second_imaginary_part)
first_z= f"{first_real_part} + {first_imaginary_part}"
second_z= f"{second_real_part} - {absolute_second_imaginary_part}"

# Polar Form operations
absolute_z = round(math.sqrt(((first_real_part)**2)+((first_imaginary_part)**2)),3)
argument1 = round(arg(first_real_part,first_imaginary_part),3)
stringed_argument_1 = str(argument1)
argument2 = round(arg(second_real_part,second_imaginary_part),3)
stringed_argument_2 = str(argument2)

if rooted_equation<0:
    print()
    print("   The equation being rooted is negative with the given parameters")
    print()
    imaginary_calculation_request_checker = input("   Do you want to calculate the imaginary solution? (y/n)  ")
    print()
    if imaginary_calculation_request_checker == "y":
        imaginary_expression_question = input("   Do you prefer polar, complex number or both? (polar/complex/both)  ")
        print()
        if imaginary_expression_question == "complex":
            print("===================================================================================================================")
            print()
            print(f" 𝟙   The first solutions complex number is expressed as {first_z}i")
            print()
            print(f" 𝟚   The second solutions complex number is expressed as {second_z}i")
            print()
            print("===================================================================================================================")
        if imaginary_expression_question == "polar":
            print("===================================================================================================================")
            print()
            print(f" 𝟙   Hence, the first solution, which is a complex number, in the polar form can")
            print(f"     be expressed as this: {absolute_z} {stringed_argument_1.translate(SUB)}")
            print()
            print(f" 𝟚   The second solution, which is also a complex number, represented in a polar")
            print(f"     form can be expressed as this: {absolute_z} {stringed_argument_2.translate(SUB)}")
            print()
            print("===================================================================================================================")
        if imaginary_expression_question == "both":
            print("===================================================================================================================")
            print()
            print(f" 𝟙   Therefore, the first solution expressed as a complex number is [ {first_z}i ]. The polar form of")
            print(f"     the first solution is represented as {absolute_z} {stringed_argument_1.translate(SUB)}")
            print()
            print(f" 𝟚   Consequently, the second solution is another complex number, and it is depicted as [ {second_z}i ].")
            print(f"     When translating the complex number to the polar form it is expressed as {absolute_z} {stringed_argument_2.translate(SUB)}")
            print()
            print("===================================================================================================================")
    else:
        print()
        print("   The solutions of the equation you are solving are imaginary,")
        print("   meaning that the solutions are inexistent in the real world")
        print()


if rooted_equation > 0:
    solution_a = ((-parameter_b+math.sqrt(rooted_equation))/(2*parameter_a))
    solution_b = ((-parameter_b-math.sqrt(rooted_equation))/(2*parameter_a))
    print_solution_a=f"   The first solution gives {solution_a}"
    print_solution_b=f"   The second solution gives {solution_b}"
    print("===================================================================================================================")
    print()
    print(print_solution_a)
    print()
    print(print_solution_b)
    print()
    print("===================================================================================================================")