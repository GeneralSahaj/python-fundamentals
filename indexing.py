#indexing = accessing elements of a sequence using [] (indexing operator)
#           [start:stop:step] (slicing operator)
# start = inclusive
# stop = exclusive
# step = how many to jump

#Some examples of indexing and slicing:

#print(index[0]) #first element
#print(index[:4]) #first 4 elements
#print(index[5:9]) #elements from index 5 to 8
#print(index[5:]) #elements from index 5 to the end
#print(index[-1]) #last element
#print(index[::3]) #every 3rd element

#lets take a practical example of indexing and slicing:

credit_card_number = "1234 5678 9012 3456"

#lets say we want to mask the credit card number except for the last 4 digits

last_four_digits = credit_card_number[-4:]

print(f"Your credit card number is : **** **** **** {last_four_digits}")

#lets say we want to reverse the credit card number

#reversed_credit_card_number = credit_card_number[::-1]

#print(f"Your reversed credit card number is {reversed_credit_card_number}")