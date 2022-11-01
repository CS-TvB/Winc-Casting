# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
print (f"Leek is " + str(leek_price) + " euro per kilo.")
leek_4 = ('We got an order for four leeks!')
#print (leek_4)

obj = leek_4.split()
new_obj = obj[5]
#print (new_obj)
number_len_obj = len(new_obj)
#print (number_len_obj)
sum_total = number_len_obj * leek_price
print (sum_total)

broccoli = 2.34
order = 1.6
total_order = order * broccoli

zin = ('1.6kg broccoli costs {}e').format(round(total_order, 2))
print(zin)
