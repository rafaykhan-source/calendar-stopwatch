# Custom Scripts:
stopwatch() {
    cd
    source .virtualenvs/google-stopwatch/bin/activate
    cd Projects/calendar-stopwatch/src/
    ./run.py "$1" -d "$2"
    cd
    deactivate
}