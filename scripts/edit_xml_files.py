import os
import glob

fpath = 'car/'
files = os.listdir(fpath)

xml_list = []
for xml_file in glob.glob(fpath + '*.xml'):
	#print(xml_file)

	num = xml_file.split('.')[0][5:]
	#print(num)

	name = num + '.png'
	print(name)

	file_r = open(xml_file, 'r')
	file_w = open('new' + fpath + 'c' + num + '.xml', 'w')
	while True:
		line = file_r.readline()
		if not line:
			break

		if line.find(name) > 0:
			line = line.replace(name, 'c' + name)
			print(line)
		else:
			pass

		file_w.write(line)
