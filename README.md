
# getting started

virtualenv -p python3  --no-site-packages env
source env/bin/activate
pip install -r go/requirements
cd go
./manage.py makemigrations
./manage.py migrate
./manage.py runserver 0.0.0.0:8000


# Create a user

./manage.py shell
from django.contrib.auth.models import User
User.objects.create_user('lilaoshi', '40089056@qq.com', '123')

