# Custom Functions:

function stopwatch() {
    prev=$(pwd)
    source ~/.virtualenvs/calendar-stopwatch/bin/activate
    cd ~/Projects/calendar-stopwatch/src/
    python run.py "$1" -d "$2"
    cd $prev
    deactivate
}