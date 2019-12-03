# Save-Yaplog-Images
Python scripts to scrape Yaplog.jp blogs for images before they turn off in January 2020. 

WARNING! Using the script may get your IP blacklisted by Yaplog. Use VPN !  

This script for Python 3 downloads full images
from entered Yaplog.jp blog, for blogs where /image/       
folder is available. The images will be saved              
into script's folder in image<post>-<num>-big.<ext> 
format. Please set up the script's variables before you
run the script. 

1. install Python 3
1. download the .py script
2. put the script into folder where you want the images to be saved
3. edit the script to enter required information:
     * blog    : link to the yaplog blog in the given format
     * postMin : first post to scrape. usually 1, or if the script crashed (e.g. you lost internet connection) 
                 check last saved image and rewrite it to continue where it ended
     * postMax : last post to scrape +1. When you click on the newest post of the blog, 
                 its the /archive/postMax number
4. run the script.
   if you are running the script first time:
   you need to install required python packages. 
   If you do not know which packages you need, just try to run the script
   through command line, and it will tell you what you are missing.
     
The script will open itself its own browser and start its work.
It is using selenium browser, and will make slow but steady progress.               
                                                                
