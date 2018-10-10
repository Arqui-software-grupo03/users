to run:

    docker-compose build && docker-compose up

    docker exec -it app3 ./manage.py makemigrations mysite

    docker exec -it app3 ./manage.py migrate

    docker exec -it app3 python ./manage.py runserver 0.0.0.0:8000

    try it:
        http://localhost:8000/admin