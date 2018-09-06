# Birthday reminder

author: Patrick Stetz ([Github](https://github.com/pstetz))

### Summary

This repo reminds me if someone's birthday is today!  Create your own `birthdays.csv` file to customize to yourself.  Alerts are sent to Finder at 8am every morning as long as today or tomorrow is someone's birthday.

### Install

To use just run `sh main.sh` after downloading the repo!

### Note

You will probably need to change a few directories, I've marked them below

- alert.sh
	- Change the commands on line 1 and 9 to your Python directionory.
	- Change the paths on line 1 and 9 to the paths of check_today.py and organize.py respectively.
- main.sh
	- Change the command to the path of the alert.sh file.
- check_today.py
  - Change the PATH variable (line 9) to the directory of this repo.
- organize.py
	- Change the PATH variable (line 4) to the directory of this repo.