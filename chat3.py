lines =[]
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	print(s)
	#清單分割法
	time = s[0][:5] #S[0]裡面的前5個字
	name = s[0][5:]
	print(time)
	print(name)