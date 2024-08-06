basic_salary = float(input("Enter your basic salary:"))
da = 0.02 * basic_salary

Ta = 0.03 * basic_salary

hra = 0.1 * basic_salary

pf = 0.15 * basic_salary
total_salary = basic_salary + da + Ta + hra + pf
net_salary = total_salary - pf

bonus = 0.25 *basic_salary    #calculate bonus
print(f"Basic Salary : {basic_salary}")
print(f"DA           : {da}")
print(f"TA           : {Ta}")
print(f"HRA          : {hra}")
print(f"PF           : {pf}")
print(f"Total Salary : {total_salary}")
print(f"Net Salary   : {net_salary}")
print(f"Bonus        : {bonus}")


