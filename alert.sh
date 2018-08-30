info=`python3 check_today.py`

# check if info is not blank
if [ "$info" != "None" ]; then
    osascript -e "tell app \"Finder\" to display dialog \"$info\""
fi

