# This program reads the input from the user on salary & number of dependents to calculate and print out the following:
# 1. State income tax
# 2. Federal income tax
# 3. Dependents tax
# 4. Salary
# 5. Take-Home Pay (Net Pay)

# Read input from User
Salary = float(input( "Enter your salary: "))
NumDependents = float(input( "Enter the number of dependents: "))
# Declare values of state income tax, federal income tax, and dependents tax
StatePer = 0.065
FederalPer = 0.28
DependentPer = 0.025
# Calculate state income tax, federal income tax, and dependents tax
StateTax = (Salary * StatePer)
FederalTax = (Salary * FederalPer)
DependentDeduction = (NumDependents * DependentPer * Salary)
# Calculate TotalWithholding & Net Pay
TotalWithholding = (StateTax + FederalTax + DependentDeduction)
TakeHomePay = (Salary - TotalWithholding)
# Print out the results
print("StateTax: $" + str(StateTax))
print("FederalTax: $" + str(FederalTax))
print("Dependents: $" + str(DependentDeduction))
print("Salary: $" + str(Salary))
print("Take-Home Pay: $" + str(TakeHomePay))