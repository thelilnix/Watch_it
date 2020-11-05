#!/bin/bash

echo -n "Enter your MySQL server IP> "
read ip
echo -n "Enter your MySQL username(non-root recommended)> "
read username
echo -n "Enter your MySQL password> "
read password
echo -n "Enter new admin panel page username> "
read panel_username
echo -n "Enter new password for admin page> "
read panel_password

cp src/Watch_it/db_config.py.sample src/Watch_it/db_config.py

echo -n "MYSQL_HOST = \"$ip\"
MYSQL_USER = \"$username\"
MYSQL_PASSWORD = \"$password\"
DB_NAME = \"Watch_it\"

# Admin panel
PANEL_USERNAME = \"$panel_username\"
PANEL_PASSWORD = \"$panel_password\"
" > src/Watch_it/db_config.py

echo -e "[\033[1;32m+\033[0m] DONE! Now just run './run.sh'"
