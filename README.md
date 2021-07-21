## iQIYI Video Downloader using dash link
1. You need to get the dash link from iq/iqiyi from the browser's network tab.
2. The script takes 3 inputs
```
a. Episode Name (Will also be the File Name)
b. Cookie option
> ( Y -> Allows adding a cookie )
> ( M -> Uses a pre-set premium cookie )
> ( N -> Does not use any cookie )
c. Dash Link from iQIYI (from browser network tab)
```
3. The script will then download the given episode link with the given episode/file name to the current directory.
4. **Currently hardcoded for WINDOWS usage only.**
5. You need to have the following .exe files either in the same folder as the script or set in the PATH environment variable.
> dl.exe (n_m3u8DL_cli.exe renamed as dl.exe)<br>
> ffmpeg.exe<br>
> mkvmerge.exe<br>
