# GOES-Fulldisk-Wallpaper

Updates your (Windows) wallpaper witht the latest fulldisk satellite image from NOAA GOES automatically every set period (down to 10 minutes).

# Install
1. Clone the repo
2. Create a new scheduled task in Windows task scheduler to run on startup and every `x` minutes after that
    - Set the action to "Start a program"
    - The program should be `pythonw.exe`, usually found in `C:\Users\{NAME}\AppData\Local\Programs\Python\Python37\pythonw.exe`
    - Set the command line argument to be the path to `update_wallpaper.pyw`, eg. `C:\Stuff\...\...\GOES-Fulldisk-Wallpaper\update_wallpaper.pyw`
    - Start in should be the repo folder, eg. `C:\Stuff\...\...\GOES-Fulldisk-Wallpaper`
    - Set timeout to 1 minute
3. If the wallpaper is stretched or tiled go into desktop settings and set the image to "Fit", my personal favourite
4. Run it manually if you don't want to wait for the task

# Config
GOES offers quite a few satellites, image bands, and qualities. These can all be set in the config file. Check em out [here](https://www.star.nesdis.noaa.gov/GOES/fulldisk.php?sat=G16)

# Warning
If using the max (10848x10848) resolution it will consume ~80MB of data each time an image is fetched, this can add up quickly running it many times a day over weeks. Beware if you have a data cap on your internet. All other resolutions are much smaller and should use negligible data
