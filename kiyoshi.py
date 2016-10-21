# -*- coding: utf-8 -*
"""ズン　ズンズン　ズンドコ　キ・ヨ・シ！！"""
import numpy as np
import time
import cv2, random, sys

flag1 = 0						# ズン判定に使用
flag2 = 0						# ドコ判定に使用	
cnt = time.clock()

zun1 = cv2.imread("image/zun1.png")
zun2 = cv2.imread("image/zun2.png")
zun3 = cv2.imread("image/zun3.png")
zun4 = cv2.imread("image/zun4.png")
zun = np.array([zun1, zun2, zun3, zun4])

doko0 = cv2.imread("image/doko0.png")
doko1 = cv2.imread("image/doko1.png")
doko2 = cv2.imread("image/doko2.png")
doko3 = cv2.imread("image/doko3.png")
doko4 = cv2.imread("image/doko4.png")

kiyoshi = cv2.imread("image/kiyoshi.png")

def image(img, fps=33) :
	cv2.imshow("img", img)
	key = cv2.waitKey(fps)
	if key == 27 :			# push esc
		cv2.destroyAllWindows()
		sys.exit()

while True :					# 無限ループ
	a = random.randint(1,2)		# ランダムで()内の範囲の数値をint型で代入

	if a == 1 :
		print ("ズン")
		flag1 += 1
		if flag1 > 4 :
			flag1 = 1
		flag2 = 0
	else :
		print ("ドコ")
		flag2 = 1

	if flag2 == 0 :
		image(zun[l])

	elif flag2 == 1 :
		if flag1 == 0 :
			image(doko0)
		elif flag1 == 1 :
			image(doko1)
		elif flag1 == 2 :
			image(doko2)
		elif flag1 == 3 :
			image(doko3)
		if flag1 < 4 :
			flag1 = 0
	time.sleep(0.05)

	if flag1 == 4 and flag2 == 1 :			# ズンが４回連続した後にドコが来た場合，キ・ヨ・シ！！と出力
			print ("キ・ヨ・シ！！")
			image(kiyoshi, fps=0)