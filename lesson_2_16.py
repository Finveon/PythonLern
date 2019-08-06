#1
print ("1) " + str(2>1))

#2
result = 2>1
print ("2)", type(result))

#3
print ("3) ")
print (2 > 2)
print (2 >= 2)
print (3 >= 2)
print (3 >= 4)

#4
print ("4) ")
print (2 < 3)
print (3 < 2)
print (3 <= 3)
print (3 <= 2)
print (3 <= 4)

#5
print ("5)", 1 == 1)
#1 = 1
print (1 != 1)
print (2 != 1)

#6
print ("6)")
print ("string" == "string")
print ("string" == "another_string")
print ("string" == "String")

x = "string"
y = "String"
print (x.lower() == y.lower())

#7
print ("7)")
print (1 < 2)
print (2 < 3)
print (1 < 2 < 3)
print (1 < 2 and 2 < 3)
print (1 > 2 and 2 < 3)
print (1 > 2 or 2 < 3)
print (1 > 2 or 2 > 3)

#8
print ("8)")

is_admin = True
file_exists = True

should_open_file = is_admin and file_exists
print (should_open_file)

#9
print ("9)")

is_admin = False
if not is_admin:
	print ('not an admin')

if is_admin == False:
	print ('not an admin')


