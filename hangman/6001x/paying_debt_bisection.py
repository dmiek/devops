balance = 39260
annualInterestRate = 0.18
aIR = annualInterestRate
time = 12                   # Months
precision = 0.01            # Cents



def Payment(balance, aIR, time, precision):
    start = balance / time
    slut = (balance * (1+aIR)**time) / time
    payment = 0
    testBalance = balance
    while testBalance > 0:
        payment = (slut - start)/2 + start
        for months in range(time):
            testBalance = (testBalance - payment)*(1+aIR/time)
        if testBalance > 0:
            testBalance = balance
            start = payment
##            print payment
        elif testBalance < -precision:
            testBalance = balance
            slut = payment
##            print payment
        else:
            break
    return round(payment, 2)
    
lowestPayment = Payment(balance, aIR, time, precision)

print 'Lowest Payment: ' + str(lowestPayment)


