def collect_principal_time_rate ():   
# This first 3 lines are provided for yougetACompoundInterest()
# This first 3 lines are provided for you
    client_principal = float(input("Principle (amount): "))
    client_time =      float(input("Time:               "))
    client_rate =      float(input("Rate:               "))
 
    return client_principal, client_time, client_rate

def compoundInterestcalc(client_principal, client_time, client_rate):
    
    amount = client_principal * (1 + (client_rate/100))**client_time
    compoundInterest = str(round(amount - client_principal, 2))

    print ('Compound Interest: ' + compoundInterest)
    
def calculateCompoundInterest():

    line_break = "---"

    client_one_principle, client_one_time, client_one_rate = collect_principal_time_rate()
    compoundInterestcalc(client_one_principle, client_one_time, client_one_rate)
    
    print(line_break)
    
    client_two_principle, client_two_time, client_two_rate = collect_principal_time_rate()
    compoundInterestcalc(client_two_principle, client_two_time, client_two_rate)

    print(line_break)

    client_three_principle, client_three_time, client_three_rate = collect_principal_time_rate()
    compoundInterestcalc(client_three_principle, client_three_time, client_three_rate)

 
 
 #print("Compound Interest: "+str(intrest))

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
