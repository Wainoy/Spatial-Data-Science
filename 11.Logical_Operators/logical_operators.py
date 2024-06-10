#Logical operators AND, OR and NOT
a = 3
b = 4
c = 5
if b > a and c >b:
    print('both conditions are true')
if a>b or a<c:
    print('one of the conditions is true')

#Sample Exercise 5. if a buyer has good credit, they are required to pay 10% downpayment
# for a product worth $1M, and 20% if they have bad credit
has_good_credit = True
price = 1000000
if has_good_credit:
    print(f'Your down payment is {price*0.1}')
elif not has_good_credit:
    print(f'Your down payment is {pricce*0.2}')
print('Thank you for shopping with us.')

#exercise
has_good_credit = True
has_criminal_records = True
has_unpaid_loan = False
if not has_criminal_records and not has_unpaid_loan and has_good_credit:
    print('Customer is eligible for a loan')
else:
    print('Customer is not eligible for a loan') #returne this as the result