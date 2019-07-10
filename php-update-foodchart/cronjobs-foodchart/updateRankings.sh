#!/bin/sh

# Update rankings every 30 minutes
*/30 * * * * python3 /etc/cron.d/updateRankings.py update

# RUN once at midnight everyday
0 0 * * * python3 /etc/cron.d/updateRankings.py wipe daily
# Run once every week ( at 00:00 every Sunday )
0 0 * * 0 python3 /etc/cron.d/updateRankings.py wipe weekly
# Run once every month
0 0 1 * * python3 /etc/cron.d/updateRankings.py wipe monthly
