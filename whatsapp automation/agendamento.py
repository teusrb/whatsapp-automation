from apscheduler.schedulers.blocking import BlockingScheduler
from whatsapp import send_message


sched = BlockingScheduler()

# Schedule send_message to be called every twelve hours
sched.add_job(send_message, 'interval', hours=12)

sched.start()