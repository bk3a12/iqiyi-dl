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
    cookie = 'lang=en_us; mod=in; QC005=48cd0d1239284a42ec29df9da8e1fc5b; QC006=cwzzs2aegif5xmttyd1nk5gz; I00019=1; QC173=0; I00002={"msg":"","code":"A00000","data":{"birthday":"912729600","uid":"30100935853","nickname":"sohail0098","icon":"http://www.iqiyipic.com/common/fix/headicons/male-130.png"}}; _ga=GA1.2.1957024672.1625770773; __gads=ID=f8ecc793e7ea5b36:T=1625770830:S=ALNI_MZg8TaET4ItXjd8qIM4dal90vTEyg; intl_audioguide=1; intl_skipguide=1; b_ext_ip=43.249.227.178; showMainlandPop=true; cloudmode_msg_sended=1; I00001=0eULBkULihExOrLyInwm3fvHjkMBf0kdB8dKCF8kxjum1oONm1qGxqICZ13IVm32hXXuLk2b; QC142=8148ef42066eb475; IQC163=1; _abck=0190FDD2074DCCB28FF75D730E28A3BA~-1~YAAQZP3UF5auhJt6AQAAZYHUvgYJevYEjGu1VJiNG7/lcERmUCMC/v2kfA7YpmzoWBTBH25YO0sNUsocj6mw8QWN952wm1RAFxDY4GOHqrIkYyfbQSq4Bn8P0brZHMHzdaDJh0i5Y3NlBmSJajzyGfsoxpNv49llC8qQ8q79x04BtdFSnCqj5SUoyuxhyDcJxXiExpNMhMTE7XHXLD9dNO8wto5EH4qng3kyk+r3tJ6EUHXR/IsDxE/UzyDEKvOjvHJj66VqljNCaZZtGYyHWJikXVJBpNVCbLESrmlBPl10NGjLQNeacIYRl806NLZbOPRElfmXntIGuWs+TTA14SxaduGrUkp+q8EmF5WJUaEha/Y0wTvcNUsR58l7FPbK/YJXJ9Zt~-1~-1~-1; ak_bmsc=84C1CCEB011AE3D107BE936EB039BB6C~000000000000000000000000000000~YAAQZP3UF5euhJt6AQAAZYHUvgwgiUqEYY8Ht8jKNkijwzzYXoDRvvFYZWXQ/TwRe96lLKd/GjovswSmagQnI48IryTrEm3Ibj011dxpJsW9j1h9ONlEuEwaLQSSoGWMaH67DVTp+08BiBFLG3CZSyNRAsqfkb/9deN/XRjIOOpuBvHoYV8hNsw8qIGN8kj645J4qw8GxmHW0gtjIsNhY9MRH6lqUQ+retqGJr+WIl6qrby11MhrQ5KCZ3POlqpc/ypKvIM7ZEzwxHULE5XKCsZrIiVEp5xL5YQQlzVbPWdk9M8zAwk94j9PCz2NRrpwNXosXwgKO8At0ImWlfh4/uvnl0Dhi1BZeH0TSKf6TS6ZXolbcEVTgW68b/+JoFg9anqKPlazww==; bm_sz=8F4C1D2A57DEABFDC9A0D3F0E8AD8E9A~YAAQZP3UF5iuhJt6AQAAZYHUvgxg5ba96K7cQNbTapo5Ot0Wg064zN2Gb7A7+4zlnYPe9i0Te1WMIZubBKrlrYHmMrJ5LHnKmQl6B9/I2ZvVfJvefWk+XfxoBq9vBF+ToMXM9OMJP4L8MM1dMDceQQ5Juf6JNPF+FZpo6eW5UVEoRUfyDAktY33N1CQrQmXO0hEIDIS3R2qAtbNl+/lpmEg4HRzJzVZQcqxa2BSZccttKiQhaFr9IkoCA/lmRK4MPU44f2xdjlCYsC5UuZcIFieoXEAgpBgp8M6V8UAgAQ==~3617593~3618103; QC007=DIRECT; QC008=1625505277.1626671005.1626699236.26; nu=0; QC010=254266892; __dfp=a1bb49a22e9bda553793979dd7a61bbf5e865a55d64bb53ddf353b28a299e9bf15@1626801277799@1625505278799; bm_mi=AA1311E16D47AB4813DBF4C3C40A2F86~PtC52M1PB3LSoK/BhB9a9JXtgbrntrcf2JojEFn47UYZznEpAAwTJf4+svQUmGk48KV8yqCXAW1Eszo8KRHbPTXGX9DyS5uXAvpZQoO3mBfYyZmcttyZLP5ZSorHJi5nPZ2G+TNveWEZD8TWK3BpgMRs9H3goW/IiOsc2U2smDTqZ3Ndmmyfr9HNgknE+kAoXQ4TaS5k2zE4ZUAorUA/fLN61ckCw1NvtzP9x2Y2ifsaA3gA0NCAJHb6f8lbuM2A; bm_sv=C3235CA42BA0D3A477389947F44DF8E0~jDuiPDr0kKDrL+2BYHxH5Mp9kYz+jGBLuGL3v4WY0KwgPn55WUnWBJ9RvK0rqKAtcCCdzzNSr7+tw6HdvENH2AlUfTU1Fz3X+UaP/juxBuYGiVsB3nRcNMnZ1HX/NJJwGe1c1YTQ0xkQyhOrHRQOEQ=='
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
    data = json.loads()
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