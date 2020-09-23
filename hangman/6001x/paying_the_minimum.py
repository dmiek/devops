balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

aIR = annualInterestRate
mPR = monthlyPaymentRate
tot = 0

for time in range(12):
    print 'Month:' + str(time+1)
    mMP = balance * mPR
    print 'Minimum monthly payment: ' + str(round(mMP, 2))
    tot += mMP
    uB = (balance - mMP) * (1 + aIR / 12)
    print 'Remaining balance: ' + str(round(uB, 2))
    balance = uB

print 'Total paid: ' + str(round(tot, 2))
print 'Remaning balance: ' + str(round(balance, 2))
    
