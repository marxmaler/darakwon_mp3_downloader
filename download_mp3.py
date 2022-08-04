import requests

def download_mp3():
    default_url = "http://pds.darakwon.co.kr/5/3501/"
    file_extension = ".mp3"
    for i in range(1,3): #cd1, cd2
        default_file_name = f"다락원중국어마스터Step4 CD{i}_A0"
        file_number = "00"
        for j in range(1, 38):
            if j < 10:
                file_number=f"0{j}"
            else:
                file_number =f"{j}"
            url = f"{default_url}{default_file_name}{file_number}{file_extension}"
            res = requests.get(url)
            open(f'{default_file_name}{file_number}{file_extension}', "wb").write(res.content)