#dictionaries
customer = {
    "Name": 'Eve',
    "Age":20,
"is_verified": True,
1:3
}
print(customer)
print(customer.get('Name','Not found')) #'Not found' is a default value to be printed incase there is no key called 'Name'
#print(customer[0]) #returns a key error
#print(customer["name"]) #returns a key error
customer["birthdate"] = '18 June 2001'
print(customer)

#Sample Exercise
phone = input('Phone: ')
digits = {
    "1":'One',
    "2":'Two',
    "3":'Three',
    "4":"Four"
}
output=""
for ch in phone:
    output += digits.get(ch,'!') + " "
print(output)

#emoji converter
message = input("> ")
words = message.split(" ")
emojis= {
    ":)":'😊',
    ":(":'😞',
    ";)":'😉'
}
output = ""
for word in words:
    output += emojis.get(word,word) + " "
print(output)