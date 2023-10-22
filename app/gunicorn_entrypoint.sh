echo "starting server"

cd $HOME_PROJECT

bind = '0.0.0.0:8000'

gunicorn ${DJANGO_WSGI_MODULE}:application \
    --log-level=info \
    --workers $NUM_WORKERS \
    --bind=$BIND