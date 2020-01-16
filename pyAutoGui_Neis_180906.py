from PIL import ImageGrab as IG
import pyautogui as pa
import sys
import os
import time
import re


pa.FAILSAFE = True
sec_between_keys = 0.25
sec_between_term = 3
sec_sleep = 0.25

#스크린샷
def screenGrab():
    box = ()
    im = IG.grab(box)
    im.save(os.getcwd() + '\\img\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

#나이스 화면 띄우기에서 비밀번호 입력전까지

#나이스 사이트 접속, 상용구 이
pa.typewrite(',skdl', interval=0.15, pause=7) #상용구로 나이스접속
while True : #경기도마크 붉은색이 아니면 기다리기
    if pa.pixelMatchesColor(1143, 307, (251, 15, 12)) == True:
        break

#나이스 로그인 - 아이디 입력
pa.typewrite('driver1', interval=0.15) #아이디 입력
pa.hotkey('tab', interval=0.02) #탭키 누르기
pa.hotkey('enter', interval=0.02) #엔터키 입력

while True : #인증서화면이 나올때 까지 기다리기
    if pa.pixelMatchesColor(1038, 706, (14, 110, 166)) == True: #확인의 파란색 색깔 확인
        break

pa.click(x=874, y=339, interval=0.02, pause=0.5) #이동식디스크 아이콘 클릭
pa.click(x=912, y=398, interval=0.02) #D드라이브 선택
pa.click(x=1000, y=622, interval=0.02) #비번 입력칸 선택
pa.click(x=1000, y=622, interval=0.02) #비번 입력칸 선택

