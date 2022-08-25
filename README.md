# Teleminder (Telegram reminder)

Telegram bot setup that sends a message every x time (according to the desired cron job).
<br>
The cron job is defined via Github actions and being executed every time through the Github CI/CD pipeline.

I created this mini project to remind myself once in 4 hours (between 8AM to 8PM) to do a specific task. 

Be aware that Github actions cron jobs are free and not guaranteed to run at the exact time you set them (depends on the loads of Github).