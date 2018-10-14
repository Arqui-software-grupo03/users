to run:

## Step1: 
- clone the mongodb repo from https://github.com/Arqui-software-grupo03/mongodb.git
- `cd mongodb`
- `docker-compose up`

## Step 2
- Open a new terminal
- go to the users repo 
- `cd users`
- `docker-compose build` && `docker-compose up`
- `docker exec -it appUsers ./manage.py migrate`
- `docker exec -it appUsers python ./manage.py runserver 0.0.0.0:8000`
- try it:
        http://localhost:8000/admin
