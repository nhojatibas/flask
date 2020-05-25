#!/bin/sh

env > _log.txt
echo "DB_INIT.....: $DB_INIT"  >> _log.txt
echo "DB_MIGRATE..: $DB_MIGRATE" >> _log.txt
echo "DB_UPGRATE.,: $DB_UPGRADE" >> _log.txt

[ "$DB_INIT" = 'True' ] && python3 run.py db init
[ "$DB_MIGRATE" = 'True' ] && python3 run.py db migrate
[ "$DB_UPGRADE" = 'True' ] && python3 run.py db upgrade

#python3 run.py runserver -h 0.0.0.0 -p 5000 -d
python3 run.py runserver -h 0.0.0.0 -p 5000
#python3 run.py runserver

#/bin/sh
