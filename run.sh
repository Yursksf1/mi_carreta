#!/bin/bash
# init
function pause(){
   read -p "$*"
}

function run_mc(){
   for /f "tokens=2 delims=:" %i  in ('ipconfig ^| findstr "IPv4" ^| findstr [0-9]') do echo %i && venv\Scripts\activate && python manage.py runserver 0.0.0.0:8000
}
run_mc

# ...
# call it
pause 'Press [Enter] key to continue...'
# rest of the script