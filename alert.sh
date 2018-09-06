info=`/anaconda3/bin/python3 ~/git/Birthdays/check_today.py`

# check if info is not blank
if [ "$info" != "None" ]; then
	osascript -e "tell app \"Finder\" to display dialog \"$info\""
fi

# Organize birthday file
/anaconda3/bin/python3 ~/git/Birthdays/organize.py
echo "Ran Birthdays script"
