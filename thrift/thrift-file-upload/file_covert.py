

file_path = "./test.jpg"
file_output = "./output.jpg"
with open(file_path, 'rb') as f:
	buff = f.read()
	with open(file_output, 'wb') as f2:
		f2.write(buff)
		f2.close
	f.close


