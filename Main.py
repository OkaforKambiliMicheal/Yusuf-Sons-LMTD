print("welcome to Yusuf & Sons ")
initial_principal = float(input("Enter initial amount: "))
interest_rate = float(input("Enter interest rate: "))
N = int(input("number of times interest applied per time period: "))
T = float(input("number of times period elapsed: "))
Simple_Interest = initial_principal*(1+interest_rate*T)
Compound_Interest = initial_principal*(1+interest_rate/N)**N*T
print("Simple interest = " + str(Simple_Interest))
print("Compound interest = " + str(Compound_Interest))
