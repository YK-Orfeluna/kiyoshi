# -*- coding: utf-8 -*
"""ズン　ズンズン　ズンドコ　キ・ヨ・シ！！"""
import numpy as np
import cv2
import time, random, sys

flag1 = 0						# ズン判定に使用
flag2 = 0						# ドコ判定に使用	

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
doko = np.array([doko0, doko1, doko2, doko3, doko4])

kiyoshi = cv2.imread("image/kiyoshi.png")

def image(img, fps=33) :
	cv2.imshow("img", img)
	key = cv2.waitKey(fps)
	if key == 27 :			# push esc
		cv2.destroyAllWindows()
		sys.exit()
	time.sleep(0.1)

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
		image(zun[flag1 - 1])
	elif flag2 == 1 :
		image(doko[flag1])
		if flag1 != 4 :
			flag1 = 0
		else :
			print ("キ・ヨ・シ！！")
			image(kiyoshi, fps=0)
