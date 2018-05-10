""" Main application entry point.

    python -m pomodoro  ...

"""

from datetime import datetime, timedelta
from time import sleep

def main():
    """ Execute the application.

    """

    remain = 25 * 60
    current = 25
    start = datetime.now()
    end = start + timedelta(seconds=1500)
    print(f'Start:{start}')
    print(f'End:{end}')

    while remain != 0:
        remaining = end - datetime.now()
        current_remaining_time = int(remaining.seconds / 60)

        if current != current_remaining_time:
            print(f"\n{current_remaining_time}", end='', flush=True)
            current = current_remaining_time

        sleep(1)
        print('🍅 ', end='', flush=True)
        remain -= 1

# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
