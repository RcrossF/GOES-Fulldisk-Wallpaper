# GOES-Fulldisk-Wallpaper

Updates your (Windows) wallpaper witht the latest fulldisk satellite image from NOAA GOES automatically every set period (down to 10 minutes).

# Install
1. Clone the repo
2. Create a new scheduled task in Windows task scheduler to run on logon and every `x` minutes after that
3. Run it manually if you don't want to wait for the task

# Config
GOES offers quite a few satellites, image bands, and qualities. These can all be set in the config file. Check em out [here](https://www.star.nesdis.noaa.gov/GOES/fulldisk.php?sat=G16)
