# Custom Scripts:
stopwatch() {
    cd
    source .virtualenvs/google-stopwatch/bin/activate
    cd Projects/google-stopwatch/google-stopwatch/
    ./run.py "$1" -d "$2"
    cd
    deactivate
}