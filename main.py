from time import sleep

import schedule

from app.main import task

if __name__ == "__main__":
    schedule.every(5).minutes.do(task)

    while True:
        schedule.run_pending()
        sleep(1)
