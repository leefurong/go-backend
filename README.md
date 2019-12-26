
# getting started

virtualenv -p python3  --no-site-packages env
source env/bin/activate
pip install -r go/requirements
cd go
./manage.py makemigrations
./manage.py migrate
./manage.py runserver 0.0.0.0:8000
