balance = 39260
annualInterestRate = 0.2
aIR = annualInterestRate
inc = 10

def Payment(balance, aIR, inc):
    payment = 0
    testBalance = balance
    while testBalance > 0:
        payment += inc
        for time in range(12):
            testBalance = (testBalance - payment)*(1+aIR/12)
            print 'Payment: ' + str(payment)
        if testBalance > 0:
            testBalance = balance            
    return payment
    
lowestPayment = Payment(balance, aIR, inc)

print 'Lowest Payment: ' + str(lowestPayment)
