set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
            
# Linha mágica para o plano Free:
python setup_admin.py || true