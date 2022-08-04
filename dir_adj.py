import os
from download_mp3 import download_mp3 as dm

book_name = "다락원중국어마스터 Step4"
cwd = os.getcwd() #현재 작업 경로(폴더)

directory = f"{cwd}/{book_name}"
if not os.path.exists(directory):
    os.makedirs(directory)

os.chdir(directory) #경로 변경
dm()

