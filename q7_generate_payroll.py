#Payroll

name= input("Enter name:")
hours=int(input("Enter number of hours worked weekly:"))
pay_rate=float(input("Enter hourly pay rate:"))
CPF_rate=int(input("Enter CPF contribution rate(%):"))
CPF=CPF_rate/100*pay_rate*hours

print("Payroll statement for {0}".format(name))
print("Number of hours worked weekly:",hours)
print("Hourly pay rate: ${0}".format(pay_rate))
print("Gross pay = ${0:.2f}".format((hours*pay_rate)))
print("CPF contribution at {0}% = ${1:.2f}".format(CPF_rate,CPF))
print("Net pay = ${0:.2f}".format(pay_rate*hours-CPF))
