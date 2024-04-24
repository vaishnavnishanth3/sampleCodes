
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

def encode():
	message = input("Enter the Message: ")
	shift_num = int(input("Enter the Shift number: "))
	ind = []
	encode_message=""
	for i in message:
		ind.append(alph.index(i))		
	for i in ind:
		if i == 26:
			i = i + 0				
		elif i != 26:			
			if i + shift_num < 26:
				i = i + shift_num			
			elif i + shift_num > 26:
				i = i + shift_num - 26				
		encode_message= encode_message+alph[i]		
	print(encode_message)
	continue_opt()

def decode():
	encode_message = input("Enter the encoded message: ")	
	shif_num = int(input("Enter the Shift number: "))	
	ind = []
	decode_message=""	
	for i in encode_message:
		ind.append(alph.index(i))		
	for i in ind:
		if i == 26:
			i = i + 0				
		elif i != 26:			
			if i + shif_num > 26:
				i = i - shif_num				
			elif i + shif_num > 26:
				i = 26 - (i + shif_num)
		decode_message= decode_message+alph[i]
		
	print(encode_message)
	continue_opt()
	
def option():
	option = input("Enter your Option [Encode | Decode]: ").lower()
	if option == "encode":
		encode()
	elif option == "decode":
		decode()
	else:
		print("Invalid Option")

def continue_opt():
	continue_opt = input("Enter your continue option [Continue | Stop]: ").lower()
	if continue_opt == "continue":
		option()
		
option()