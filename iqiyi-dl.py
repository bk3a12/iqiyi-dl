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
header = {'user-agent': 'Mozilla/5.0'}
ucookie = 'True'

x = input("Want to enter a cookie?\nY/Yes = Yes (Copy cookie value from dash url request headers)\nAnything else = No Cookie\nChoice: ")

if x.lower()[0] == 'y':
    cookie = input("Enter the cookie (no need to add surrounding quotes): ")
    header = {'cookie': cookie, 'user-agent': 'Mozilla/5.0'}
    ucookie = 'True'
else:
    ucookie = 'False'

os.system('cls') if os.sys.platform == 'win32' else os.system('clear')

print('*'*20)
print("Episode Name:", epname)
print("Using Cookie:", ucookie)
print('*'*20)

url = requests.get(input("Enter an iqiyi dash url: "), headers=header).content

try:
    data = json.loads(url)
except:
    data = json.loads(url[38:-16])

m3u8 = next(filter(lambda x: 'm3u8' in x,
            data['data']['program']['video']))['m3u8']

if not os.path.exists(epname):
    os.mkdir(epname)

with open(f"{epname}/file.m3u8", "w+") as file:
    file.write(m3u8)

subsbase = data['data']['dm']
stl = data['data']['program']['stl']
subs = []

for i in range(len(stl)):
    subs.append(stl[i]['_name'])
    os.system(
        f"ffmpeg -loglevel quiet -nostats -hide_banner -y -stats -i \"{subsbase + stl[i]['srt']}\" \"{epname}/{stl[i]['_name']}.srt\"")

alang = data['data']['program']['audio'][0]['name']
print('Downloading:', epname)
os.system(f'dl "{epname}/file.m3u8" --saveName "{epname}" --workDir "."')
sleep(5)

mkvcmd = f'mkvmerge -q -o "{epname}.mkv" --language 0:und --default-track 0:yes --default-track 1:yes '
mkvcmd += f'--language 0:zh --track-name 1:Mandarin "{epname}.mp4" ' if alang == 'Mandarin' else f'--language 0:ko --track-name 1:Korean "{epname}.mp4" '

audios = {'Spanish': 'es', 'Simplified Chinese': 'zh-Hans', 'Traditional Chinese': 'zh-Hant', 'Thai': 'th', 'Bahasa Indonesia': 'id',
          'Bahasa Malaysia': 'ms', 'Arabic': 'ar', 'Korean': 'ko', 'Vietnamese': 'vi', 'Turkish': 'tr', 'Hindi': 'hi', 'Urdu': 'ur'}

for lang in subs:
    if lang == 'English':
        mkvcmd += f'--default-track 0:yes --language 0:en --track-name "0:{lang}" "{epname}/{lang}.srt" '

    for audio, short in audios.items():
        if lang == audio:
            mkvcmd += f'--language 0:{short} --track-name "0:{lang}" "{epname}/{lang}.srt" '

mkvcmd += f'--title "{epname}"'
print("Merging Files...")
os.system(mkvcmd)
print("Cleaning Up...")
os.system(f'rmdir /S /Q "{epname}" && del "{epname}.mp4"')
print("Finished Downloading:", epname)
