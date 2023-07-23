import os
from download_mp3 import download_mp3 as dm

book_name = "내게는 특별한 프랑스어 어휘를 부탁해"
cwd = os.getcwd() #현재 작업 경로(폴더)

directory = f"{cwd}/{book_name}"
if not os.path.exists(directory):
    os.makedirs(directory)

os.chdir(directory) #경로 변경
dm(1) #cd가 하나인 경우 1로 설정

