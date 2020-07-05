# GOES-Fulldisk-Wallpaper

Updates your (Windows) wallpaper witht the latest fulldisk satellite image from NOAA GOES automatically every set period (down to 10 minutes).

# Install
1. Clone the repo
2. You might have to associate `.pyw` files with `pythonw.exe`. To do this double click `update_wallpaper.pyw` and find `pythonw.exe` to always open it
3. Create a new scheduled task in Windows task scheduler to run on logon and every `x` minutes after that
4. If the wallpaper is stretched or tiled go into desktop settings and set the image to "Fit", my personal favourite
4. Run it manually if you don't want to wait for the task

# Config
GOES offers quite a few satellites, image bands, and qualities. These can all be set in the config file. Check em out [here](https://www.star.nesdis.noaa.gov/GOES/fulldisk.php?sat=G16)

# Warning
If using the max (10848x10848) resolution it will consume ~80MB of data each time an image is fetched, this can add up quickly running it many times a day over weeks. Beware if you have a data cap on your internet. All other resolutions are much smaller and should use negligible data
