def runningMed(seq):
    num = 0
    sum = 0
    for item in seq:
        num += 1
        sum += item
        print(sum/num)
    
runningMed([2, 1, 5, 7, 2, 0, 5])