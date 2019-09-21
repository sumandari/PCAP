digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]

def print_number(num):
    # failsafe
    try:
        num = int(num)
    except ValueError:
        print("Error: angka yang dimasukan tidak valid")
        return None
    


print_number(int(input("Enter the number you wish to display: ")
