# bluealsaautofix

## Installation

- copy bluealsaautofix.py to /usr/sbin with the name bluealsaautofix
- make the script executable: chmod +x /usr/sbin/bluealsaautofix
- copy bluealsaautofix.service to /etc/systemd/system/
- reload systemd units: systemctl daemon-reload
- install service: systemctl enable bluealsaautofix
- start service: systemctl start bluealsaautofix