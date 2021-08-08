# scraping-tools

This repository contains 2 folders - HP and DELL. <br>
Folders were named according to manufactures of servers for that we wanted to gain information about original processor's configuration.<br>

I needed to distrubute the tools somehow among my teammates and therefore I created exe.files by using <i>PyInstaller</i>. PyInstaller bundles a Python application and all its dependencies into a single package. The user can run the packaged app without installing a Python interpreter or any modules. Thanks it each user could easily use the app. <br>

The steps were following:
* Paste required serial numbers into file Input_HPC.txt/Input_Dell.txt
* Run HPC_1.exe/Dell_1.2.exe application (in folder dist)
* Have a look at output.txt. There should be information that were found on web pages for required serial numbres.  





