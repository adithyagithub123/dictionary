dictionary1 = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}
print(dictionary1['India'])
print(dictionary1.get('India','not found'))
print(dictionary1.get('Australia' , 'not found'))
print(dictionary1.get('America' , 'not found'))