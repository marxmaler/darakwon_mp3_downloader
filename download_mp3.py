import requests

def download_mp3(cdNumber): #cd 갯수
    # 개별 파일의 url은 script의 javascript 코드를 뜯어보면 zip 파일을 만들기 위해 생성한 array에 들어있음.
    # default_url = "http://pds.darakwon.co.kr/5/3501/" #다락원 중국어 마스터 Step 4
    # default_url = "https://pds.darakwon.co.kr/5/2108/" #신공략 중국어 독해 초급에서 중급으로
    default_url = "http://pds.darakwon.co.kr/5/5198/" #내게는 특별한 프랑스어 어휘를 부탁해
    file_extension = ".mp3"
    for i in range(1,cdNumber+1): #cd1, cd2...
        # default_file_name = f"다락원중국어마스터Step4 CD{i}_A0"
        # default_file_name = f"신공략중국어독해_초급에서중급으로_"
        default_file_name = f"내게는특별한프랑스어어휘_"
        file_number = ""
        for j in range(1, 54): #file 숫자만큼 반복
            if j < 10:
                file_number=f"00{j}"
            else:
                file_number =f"0{j}"
            url = f"{default_url}{default_file_name}{file_number}{file_extension}"
            res = requests.get(url)
            open(f'{default_file_name}{file_number}{file_extension}', "wb").write(res.content)