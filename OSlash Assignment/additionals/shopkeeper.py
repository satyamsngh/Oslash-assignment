Clothing = "Clothing"
Stationery = "Stationery"
ClothingMaxQuantity = 2
StationeryMaxQuantity = 3

InventoryList = "TSHIRT Clothing 1000 10\nJACKET Clothing 2000 5\nCAP Clothing 50 20\nNOTEBOOK Stationery 200 20\nPENS Stationery 300 10\nMARKERS Stationery 500 5"

empty = 0
maxDiscount = 100
extraDiscountThreshold = 3000
extraDiscount = 0.05
taxPercentage = 0.10
minDiscountThreshold = 1000

addItem = "ADD_ITEM"
error = "ERROR_QUANTITY_EXCEEDED\n"
success = "ITEM_ADDED\n"
discountText = "TOTAL_DISCOUNT "
finalAmountText = "TOTAL_AMOUNT_TO_PAY "
newLine = "\n"
formatSpecifier = '%.2f'

def billFormatter(discount, total):
    bill = discountText + str(formatSpecifier % discount) + newLine
    bill += finalAmountText + str(formatSpecifier % total) + newLine
    return bill
