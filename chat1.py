# 讀取檔案
def read_file(filename):
	chat = []
	with open(filename, 'r',encoding = 'utf-8-sig') as f:
		for line in f :
			# if 'Allen' in line: 
			# 	continue # 迴圈裡的限定功能, 如果有'Allen'跳到下一回, 但仍在迴圈內
			# elif 'Tom' in line: 
			# 	continue # 迴圈裡的限定功能, 如果有'Tom'跳到下一回, 但仍在迴圈內
			chat.append(line.strip())
	return chat

#格式轉換
def convert(chat):
	new = [] #新清單
	person = None #預設值"無"
	for line in chat:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:  #如果 person 有值的話
			new.append(person + ": " + line) # 形成一個新的字串
	return new


#寫入檔案
def write_file(filename, chat):
	with open(filename, 'w') as f:
		for line in chat:
			f.write(line + '\n')

#主程式
def main():
	chat = read_file('input.txt')
	chat = convert(chat)
	write_file('output.txt',chat)

main()
# 想辦法把對話與姓名分開
# 姓名存成 c[0], 對話存成 c[1]


# 寫入成新的檔案
# with open('output.txt','w',encoding = 'utf-8-sig') as f:
# 	for chat in output:
# 		f.write(c[0] + ':' + c[1] + '\n')