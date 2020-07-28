from crontab import CronTab

cron = CronTab(user='ec2-user')
job = cron.new(command='python CRONjob2.py')
job.minute.every(1)

cron.write()

