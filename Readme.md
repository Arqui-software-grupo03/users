to run:

## Step1:
- clone the mongodb repo from https://github.com/Arqui-software-grupo03/mongodb.git
- `cd mongodb`
- `docker-compose up`

## Step 2
- Open a new terminal
- go to the users repo
- `cd users`
- in settings.py comment this line --> 'django.contrib.admin',
- `docker-compose build` && `docker-compose up`
- in settings.py uncomment this line --> 'django.contrib.admin',
- `docker-compose build` && `docker-compose up`
