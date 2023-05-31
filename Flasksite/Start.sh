# Start Gunicorn with the desired configuration
/home/pi/.local/bin/gunicorn --chdir "/home/pi/Desktop/T1_TableCast/Flasksite" -b 127.0.0.1:5000 main:app

