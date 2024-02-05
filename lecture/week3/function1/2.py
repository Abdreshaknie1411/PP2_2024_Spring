def fahrenhit_to_formula(fahrenhit):
    celsius=(5/9)*(fahrenhit-32)
    return celsius

fahrenhit_temperature=float(input())
celsius_temperature=fahrenhit_to_formula(fahrenhit_temperature)
print(celsius_temperature)