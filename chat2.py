#Line對話紀錄
# 讀取檔案
def read_file(filename):
	chat = []
	with open(filename, 'r',encoding = 'utf-8-sig') as f:
		for line in f :
			chat.append(line.strip())
	return chat

#格式轉換
def convert(chat):
	person = None #預設值"無"
	allen_word_count = 0
	viki_word_count = 0 
	allen_sticker_count = 0 # allen 貼圖數
	viki_sticker_count = 0 # viki 貼圖數
	allen_image_count = 0 # allen 圖片數
	viki_image_count = 0 # viki 圖片數
	for line in chat: #變成清單後將一行一行用迴圈印出來
		s = line.split(' ') #切割完會變成清單
		#print(line)
		time = s[0]
		name = s[1]
		if name =='Allen': # 如果對話的人是 Allen 的時候
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]: #把每一個子清單 s[2] 之後的字用 for 迴圈拿出來存成 m 做累加 #s[2:] 從S裡的清單 2~底
					allen_word_count = allen_word_count + len(m)
					#print('Allen', allen_word_count)
		elif name =='Viki': # 如果對話的人是 Viki 的時候
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]: #把每一個子清單 s[2] 之後的字用 for 迴圈拿出來存成 m 做累加 #s[2:] 從S裡的清單 2~底
					viki_word_count = viki_word_count + len(m)
					#print('Viki', viki_word_count)
	print('Allen 的對話總字數是', allen_word_count)
	print('Viki 的對話總字數是', viki_word_count)
	print('Allen 傳了', allen_sticker_count, '個貼圖')
	print('Viki 傳了', viki_sticker_count, '個貼圖')
	print('Allen 傳了', allen_image_count, '張圖片')
	print('Viki 傳了', viki_image_count, '張圖片')

#寫入檔案
def write_file(filename, chat):
	with open(filename, 'w') as f:
		for line in chat:
			f.write(line + '\n')

#主程式
def main():
	chat = read_file('LINE-Viki.txt')
	chat = convert(chat)
	# write_file('output.txt',chat)

main()