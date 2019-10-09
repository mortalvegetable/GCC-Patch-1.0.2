def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    interestPercentage /= 100
    repaymentPercentage /= 100
    totalCost = .1 * initialLevelOfDebt
    initialLevelOfDebt -= totalCost
    repaymentCost = repaymentPercentage * initialLevelOfDebt
    if repaymentCost < 50:
        repaymentCost = 50
    while initialLevelOfDebt > 0:
        totalDebt = initialLevelOfDebt + (initialLevelOfDebt * interestPercentage)
        totalCost += repaymentCost
        totalDebt -= repaymentCost
        print("total cost is: ", totalCost)
        initialLevelOfDebt = totalDebt
        print("initial debt is ", initialLevelOfDebt)
    totalCost += repaymentCost
    return totalCost
