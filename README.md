pip freeze > requirements.txt

source venv/bin/activate

./venv/scripts/activate

pip install django

./venv/scripts/deactivate

pip install -r requirements.txt
