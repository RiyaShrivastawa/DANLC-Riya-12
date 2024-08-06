def calculate_salary(basic_salary, experience):
    # Calculate allowances and deductions
    da = 0.05 * basic_salary
    ta = 0.065 * basic_salary
    cca = 0.08 * basic_salary
    hra = 0.10 * basic_salary
    pf = 0.125 * basic_salary

    # Calculate bonus based on experience
    if experience > 25:
        bonus = 0.25 * basic_salary
    elif experience > 20:
        bonus = 0.20 * basic_salary
    elif experience > 15:
        bonus = 0.15 * basic_salary
    else:
        bonus = 0.10 * basic_salary

    # Calculate total and net salary
    total_salary = basic_salary + da + ta + cca + hra + bonus
    net_salary = total_salary - pf

    return da, ta, cca, hra, pf, bonus, total_salary, net_salary

def generate_payslip(name, experience, basic_salary):
    da, ta, cca, hra, pf, bonus, total_salary, net_salary = calculate_salary(basic_salary, experience)

    print("--------------------------------------------------------------------------------------------------------")
    print(" " * 100 + "Pay Slip")
    print("--------------------------------------------------------------------------------------------------------")
    print(f"Name: {name}")
    print(f"Experience: {experience} years")
    print(f"Basic Salary: {basic_salary}")
    print("--------------------------------------------------------------------------------------------------------")
    print(f"DA: {da}")
    print(f"TA: {ta}")
    print(f"CCA: {cca}")
    print(f"HRA: {hra}")
    print(f"PF: {pf}")
    print(f"BONUS: {bonus}")
    print(f"TOTAL SALARY: {total_salary}")
    print(f"NET SALARY: {net_salary}")
    print("--------------------------------------------------------------------------------------------------------")

# Main function to get input and generate payslip
def main():
    name = input("Enter name: ")
    experience = int(input("Enter Experience (in years): "))
    basic_salary = float(input("Enter Basic salary: "))

    generate_payslip(name, experience, basic_salary)

if __name__ == "__main__":
    main()