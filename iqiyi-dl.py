import requests
import json
import os
from time import sleep

os.system('cls') if os.sys.platform == 'win32' else os.system('clear')

print("*******************************************************************")
print("                iQIYI DASH Video Downloader ")
print("*******************************************************************")
print(" > Works only with iq.com/iqiyi.com dash url.")
print(" > Enter the Episode Name.")
print(" > The Episode Name will also be the File Name.")
print("*******************************************************************")

epname = input("Enter the Episode Name: ")

x = input("Want to enter a cookie?\nY/Yes = Yes\nM/Maybe = Unsure (Will use a pre-set cookie)\nAnything else = No Cookie\nChoice: ")

if  any(word in x for word in ['y', 'yes', 'YES', 'Y']):
    cookie = input("Enter the cookie (no need to add surrounding quotes): ")
    header = {'cookie': cookie, 'user-agent': 'Mozilla/5.0'}
    ucookie = 'True'
elif any(word in x for word in ['m', 'maybe', 'M', 'MAYBE']):
    cookie = 'lang=en_us; mod=in; QC005=48cd0d1239284a42ec29df9da8e1fc5b; QC006=cwzzs2aegif5xmttyd1nk5gz; I00019=1; QC173=0; I00002={"msg":"","code":"A00000","data":{"birthday":"912729600","uid":"30100935853","nickname":"sohail0098","icon":"http://www.iqiyipic.com/common/fix/headicons/male-130.png"}}; _ga=GA1.2.1957024672.1625770773; __gads=ID=f8ecc793e7ea5b36:T=1625770830:S=ALNI_MZg8TaET4ItXjd8qIM4dal90vTEyg; intl_audioguide=1; b_ext_ip=43.249.227.178; showMainlandPop=true; _scid=5bc4c27a-9ba6-4d2d-a5de-e8c411e09317; _gcl_au=1.1.1684019488.1626896060; _fbp=fb.1.1626896059968.1649284677; _sctr=1|1626892200000; I00001=f9ncQJPQM1sn1Lf31bhHtRcMNcEcy3F3m1HAuueHLzRvSZEydoim1m3d7GwL24GjYF1Tv46; cloudmode_msg_sended=1; _abck=0190FDD2074DCCB28FF75D730E28A3BA~-1~YAAQPv3UF1BRYbF6AQAAyt404gaOl08huVxQhw1MSZK2y0S7t2apngsOVu74/YODenlR1DuDb/aEWywdvbkVa0PxKTtpVMof+d+f8V6PTYTUBwFWJ6ShTA7/Qh6aH5pFz2FBl+W0R6Y6Nv9+8uJ4IEbQc2qqiVfiO+5uKBPShc8o9zCcglE7z/Fb8+1/HVT26qXHw11HkilpXduGY2CiUoT+uiJuxAuLyY9nojUbLcQs05IM/4GIVAIIXDh6qiFaQKopLwH/wq5ynQW1MJa3pcILFKX4W7ecdlx3GLQgRgQvmdTMO+CNFEBwau2zWSzz/fxbaHQP+9HLQOkSxJ6BfQG9EzVRCuY25LOW/rykhWbqeQ1ki9CuUppvpcvQaJ1OKcYKjkx6~-1~-1~-1; ak_bmsc=EF75334E310D8F4B050216C62E34AD57~000000000000000000000000000000~YAAQPv3UF1FRYbF6AQAAyt404gx/Gbpk1NERSOn+doI56B+87KeNWiH3CiN9q6/cNyFmYcIjZRYvJ48aZjsN1xBfzMJTevF3E6LafaM4p1af1PBd+9P3afDjJRUdQlJG5aKpfuwLl8dv2XC/h2pyqsRj8IwEe2xX5Ke9292Gl9M7Io2ehjVaWQ9FWSnNxr+k0y7fc6dywx8h1E5/TIFnhrATPIGCmnYfrH+0kBJJPl2+e2TwBkoMwN1OYUVOc4eCYsa+XmPnJHmLX1QpuVGypX35jMVcQPj7dzpQaQJSGFg6yY0eCNEzrVj77cIGNBt3iFym19L3nykknjIvQgO5H885YfcQ1orsdfIfWx4pmV81V3z8VwXogw/98wY41GY3+97TCf/oEA==; bm_sz=8C765AA21BEA96677EC038DF6F3C0CFD~YAAQPv3UF1JRYbF6AQAAyt404gxa+RT/TbUZLUphATtgT1WQwPE/duseQ6DbpG2adzXduV2iWLU5fFvR+3B9HG9vJnyvu60aMUUqtIOqBJ6HYVq38c008L+/06jowlPi1eKiVMUOTjvUOetc50VlvIr0cKLE6zkPL6u9kK6c5bBTPmIbTYsAA5R40A0+yzOvvI/p9fwa0WlAwx+t9jl0yZKIyTGQVtNZsJKVzJ3+oLDChSKha1UOMjCJ7R9s9s9HNxP+m2gMTd3N5Zoxb1ZKbc99i3unmVUHqMs4w3uuBg==~4470070~3294514; IQC163=1; QC008=1625505277.1627164063.1627292756.38; QC007=DIRECT; nu=0; __dfp=a12297ab113e935187bc0025b7374c6416442de50a1b96f726b011c3fde725912b@1628178434447@1626882435447; bm_mi=92843C11F5C6BC9A58C0FAC2DF59146A~+8o/xmKl42QHcv0eInYaIKueKQCuzUEswwR3QGi7+GR28CVmA8k5YlBhiJl0aznrEr4XdC4K7NRujtcYiujETaINrPp0wsEdyey642Y4aD6YxP9FgA/lFNoiJHTtUkJK+n33dawMQOTxqgZ7qe9t+XVWb/esn6KgYQe9lI0MLtdXV5tCxVTdQb5OyRn07GRAkotpArGizYdyX0J54TWPSWK+tOQAhQhKSje5ggHdqMRQDwAEftZEtiZ85cz2QPM/; QC010=91300638; bm_sv=FB09575D13122B38706BE420104EA355~MQKwDTlMo4qAmHx9Z9k7ruIvdxcAubmLQ/5LROtmnqXWME58VDAYeNMx3xTyX3GALq8FegZefj8N/v8APkyZDldWYtXbpqylpMzDKbAke/4J2sWdS7nJZw7q2jNADwDtLpCexCaSgj7KfsXCfh1HKg=='
    header = {'cookie': cookie, 'user-agent': 'Mozilla/5.0'}
    ucookie = 'True'
else:
    header = {'user-agent': 'Mozilla/5.0'}
    ucookie = 'False'

os.system('cls') if os.sys.platform == 'win32' else os.system('clear')

print('*'*20)
print("Episode Name:", epname)
print("Using Cookie:", ucookie)
print('*'*20)

url = requests.get(input("Enter an iqiyi dash url: "), headers = header).content

try:
    data = json.loads(url)
except:
    data = json.loads(url[38:-16])

m3u8 = next(filter(lambda x: 'm3u8' in x, data['data']['program']['video']))['m3u8']

if not os.path.exists(epname):
    os.mkdir(epname)

with open(f"{epname}/file.m3u8", "w+") as file:
    file.write(m3u8)

subsbase = data['data']['dm']
stl = data['data']['program']['stl']
subs = []
for i in range(len(stl)):
    subs.append(stl[i]['_name'])
    os.system(f"ffmpeg -loglevel quiet -nostats -hide_banner -y -stats -i \"{subsbase + stl[i]['srt']}\" \"{epname}/{stl[i]['_name']}.srt\"")
alang = data['data']['program']['audio'][0]['name']
print('Downloading:', epname)
os.system(f'dl "{epname}/file.m3u8" --saveName "{epname}" --workDir "."')
print("Finished Downloading:", epname)
sleep(5)
mkvcmd = f'mkvmerge -q -o "{epname}.mkv" --language 0:und --default-track 0:yes --default-track 1:yes '
mkvcmd += f'--language 0:zh --track-name 1:Mandarin "{epname}.mp4" ' if alang == 'Mandarin' else f'--language 0:ko --track-name 1:Korean "{epname}.mp4" '
for lang in subs:
    if lang == 'English':
        mkvcmd += f'--default-track 0:yes --language 0:en --track-name "0:{lang}" "{epname}/{lang}.srt" '
    if lang == 'Spanish':
        mkvcmd += f'--language 0:es --track-name "0:{lang}" "{epname}/{lang}.srt" '
    if lang == 'Simplified Chinese':
        mkvcmd += f'--language 0:zh-Hans --track-name "0:{lang}" "{epname}/{lang}.srt" '
    if lang == 'Traditional Chinese':
        mkvcmd += f'--language 0:zh-Hant --track-name "0:{lang}" "{epname}/{lang}.srt" '
    if lang == 'Thai':
        mkvcmd += f'--language 0:th --track-name "0:{lang}" "{epname}/{lang}.srt" '
    if lang == 'Bahasa Indonesia':
        mkvcmd += f'--language 0:id --track-name "0:{lang}" "{epname}/{lang}.srt" '
    if lang == 'Bahasa Malaysia':
        mkvcmd += f'--language 0:ms --track-name "0:{lang}" "{epname}/{lang}.srt" '
    if lang == 'Arabic':
        mkvcmd += f'--language 0:ar --track-name "0:{lang}" "{epname}/{lang}.srt" '
    if lang == 'Korean':
        mkvcmd += f'--language 0:ko --track-name "0:{lang}" "{epname}/{lang}.srt" '
    if lang == 'Vietnamese':
        mkvcmd += f'--language 0:vi --track-name "0:{lang}" "{epname}/{lang}.srt" '
    if lang == 'Turkish':
        mkvcmd += f'--language 0:tr --track-name "0:{lang}" "{epname}/{lang}.srt" '
    if lang == 'Hindi':
        mkvcmd += f'--language 0:hi --track-name "0:{lang}" "{epname}/{lang}.srt" '
    if lang == 'Urdu':
        mkvcmd += f'--language 0:ur --track-name "0:{lang}" "{epname}/{lang}.srt" '
mkvcmd += f'--title "{epname}"'
print("Merging Files...")
os.system(mkvcmd)
print("Cleaning Up...")
os.system(f'rmdir /S /Q "{epname}" && del "{epname}.mp4"')
print("Finished Downloading:", epname)
