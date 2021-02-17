# copy this file to a 'run.sh' file to make it easier to start the website
# replace '1234' with the port you'd like to run the website on
# omit the '&' if you don't want to run it in the background
# you may in some instances need to prepend "sudo" to the start of the command
gunicorn -b "127.0.0.1:1234" app:app &