# Save-Yaplog-Images
Python scripts to scrape Yaplog.jp blogs for images before they turn off in January 2020. 

<b> WARNING! Using the script may get your IP blacklisted by Yaplog. Use VPN ! </b>  

This script for Python 3 downloads full images from entered Yaplog.jp blog, </br>
for blogs where image folder is available. The images will be saved </br>
into script's folder in imagePost-num-big.ext format. </br>
Please set up the script's variables before you run the script. 

1. install Python 3
1. download the .py script
2. put the script into folder where you want the images to be saved
3. edit the script to enter required information:
     * blog    : link to the yaplog blog in the given format
     * postMin : first post to scrape. Usually 1, or if the script crashed </br>
       (e.g. you lost internet connection) check last saved image </br> 
       and rewrite it to continue where it ended
     * postMax : last post to scrape +1. When you click on the newest post of the blog, </br>
       its the /archive/postMax number
4. run the script. </br>
   if you are running the script first time: </br>
   you need to install required python packages. </br>
   If you do not know which packages you need, just try to run the script
   through command line, and it will tell you what you are missing.
     
The script will open itself its own browser and start its work.
It is using selenium browser, and will make slow but steady progress.               
                                                                
<b>Common problems</b>

I closed the script before it finished. What now?
Look at the index of last saved image and insert the number into script as postMin variable. E.g. for image1331-18-big.jpg, write postMin = 1331. The script will continue from this point onward.

The script immediately ended with a message: "Session not created: This version of ChromeDriver only supports Chrome version.."!
Check what is your version of Chrome and get the correct ChromeDriver from https://chromedriver.chromium.org/downloads and put it into C:/Windows (if you're running Windows).
