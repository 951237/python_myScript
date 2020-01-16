from PIL import ImageGrab as IG
import pyautogui as pa
import sys
import os
import time
import re


pa.FAILSAFE = True

#스크린샷
def screenGrab():
    box = ()
    im = IG.grab(box)
    im.save(os.getcwd() + '\\img\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def waitWindow(p_x, p_y, p_r, p_g, p_b):
    i = 1
    while True:
        if pa.pixelMatchesColor(p_x, p_y, (p_r, p_g, p_b)) == True:  # 수덕원 예약 아이콘 좌표 및 색상코드
            break
        print('%s번째 시도중...' %(i))
        i += 1
        time.sleep(1)

#윈도우 창찾기
def findWindow():
    all = pa.getWindows()
    for i in all:
        if 'http://bms.ken.go.kr/?USERID=driver' in i:
            r_window = i
        else:
            continue
    return r_window

#윈도우창 위치 찾기
def getPosition(p_win):
    pa.getWindow(p_win).set_foreground()
    result = pa.getWindow(p_win).get_position()
    return result

#윈도우내에서 일치하는 이미지 검색
def imgSearchClick(p_imgName):
    v_imgLocation = pa.locateOnScreen(p_imgName)
    imgLocationX, imgLocationY = pa.center(v_imgLocation)
    pa.click(imgLocationX, imgLocationY, interval=0.5, pause=0.5)

print('결재창 찾는중...')
waitWindow(662,315,240,240,240)

#창의 색깔이 바뀜
print('결재정보를 찾는 중...')
p_win = findWindow()
r_region = getPosition(p_win)

print('창의 좌표 : %s' %(str(r_region)))

#창의 좌측 상단의 X좌표와 Y좌표를 변수로 지정
leftX, leftY = r_region[0:2]

def clickIwant(_x,_y):
    pa.click(leftX + _x,leftY + _y,clicks=1,interval=0.25)
    time.sleep(0.75)

print('결재정보 선택... ')
clickIwant(67,124)

#창의 색이 바뀜
print('과제카드 찾는 중....')
print('돋보기 선택....')
clickIwant(784,251)
print('정보 단위과제 선택....')
clickIwant(302,284)
print('확인 클릭....')
clickIwant(682,98)

#창의 색이 바뀜.
print('문서처리 선택....')
clickIwant(412,93)

print('문서처리창 기다리는 중....')
waitWindow(637,502,248,248,248)
time.sleep(2)
print('확인 클릭....')
clickIwant(781,255)
for i in range(2):
    time.sleep(2)
    pa.hotkey('enter')
#
# print('결재 완료')



