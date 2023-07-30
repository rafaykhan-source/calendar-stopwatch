# Custom Scripts:
stopwatch() {
    cd
    source .virtualenvs/google-stopwatch/bin/activate
    cd Projects/google-stopwatch/
    ./run.py -t "$1" -d "$2"
    cd
    deactivate
}