#1
import sys
print (sys.getdefaultencoding())

print (ord ('a'))

print (chr(97))
print (chr(198))

s = 'hello'

enc_ascii = s.encode('ascii')
enc_utf8 = s.encode('utf8')
enc_utf16 = s.encode('utf16')

print (type(enc_ascii))
print (enc_ascii)
print (enc_utf8)
print (enc_utf16)

print (len(enc_ascii))
print (len(enc_utf8))
print (len(enc_utf16))

#2
str_in_bytes = b'hello'
str_in_bytes2 = s.encode('utf8')

str_in_text = 'hello'

print (type(str_in_bytes))
print (type(str_in_bytes2))
print (type(str_in_text))

print ('bytes'.encode('utf8'))
print ('байты'.encode('utf8'))

print (str_in_bytes[0])
print (str_in_text[0])

#3
ba = bytearray (b'hello')
ba[0] = 87
print (ba)

result = str(str_in_bytes)
print (result)
print(len(result))

result = str_in_bytes.decode('utf8')
print (result)

#4
jpeg = [120, 3, 255, 100]
with open (r'e:\Python3\btest.bin', 'w+b') as file:
	file.write(bytes(jpeg))

with open (r'e:\Python3\btest.bin', 'rb') as file:
	date = file.read()
	for b in date:
		print (int(b))



