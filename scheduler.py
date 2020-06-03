from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    print("Hello World")

def job_function_2():
    print("Hello World - 45")

sched = BlockingScheduler()

sched.add_job(job_function, 'cron', second='30')
sched.add_job(job_function_2, 'cron', second='45')
sched.start()