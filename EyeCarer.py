import os
from plyer import notification
import time
icon_path = os.path.abspath("Eye Carer/Eye Carer App Icon No Background.ico")
running = True
while running:
    time.sleep(1200)
    notification.notify(
        title='Time to rest your eyes!',
        message='Look away for 20 seconds at 6 meters distance.',
        app_name='Eye Carer',
        app_icon=icon_path,
        timeout= 1
    )
    time.sleep(22)
    notification.notify(
        title='Rest complete!',
        message='Now you can continue at your work',
        app_name='Eye Carer',
        app_icon=icon_path,
        timeout= 1
    )