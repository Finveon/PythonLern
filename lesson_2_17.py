file = open ('sample.txt')
data = file.read()
print (data)

print (file.read())

# после прочтения файла необходимо возвращать 
# каретку в начало файла командой file.seek(0)

file.seek(0)
print (file.read())

file.seek(0)
data = file.read()
print(type(data))
print (data)

file.seek(0)
lines = file.readlines()
print (type(lines))
print (lines)

print (len(lines))

#закрытие файлов
sample_file = open ('e:\\Python3\\sample.txt')
print (sample_file)
file.close()
sample_file.close()

# проверяем закрытие файлов с помощью функции .closed
print (file.closed)
print (sample_file.closed)


# по завершению блока with файл будет автоматически закрыт
# это поможет не забыть закрыть файл после обработки.
with open('sample.txt') as sample_file:
	sample_data = sample_file.read()

print (sample_data)

#with open ('sample.txt', mode = 'r+') as sample_file:
#	data = sample_file.read()


with open('sample.txt', mode = 'a') as sample_file:
	sample_file.write ('\nEric;7639')

with open('sample.txt', mode = 'r') as sample_file:
	print (sample_file.read())


# добавляем строку в существующий файл.
with open ('sample.txt', mode = 'r+') as sample_file:
	sample_file.seek(0, 2)
	sample_file.write('\nToub;5627')
	sample_file.seek(0)
	print(sample_file.read())

# создаем новый файл и добавляем в ненго строку.
with open ('abracadabra.txt', mode='w+') as spell_file:
	spell_file.write('abra-abra-abra-cadabra')
	spell_file.seek(0)
	print (spell_file.read())

