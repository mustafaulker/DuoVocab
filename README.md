# DuoVocab

## Duolingo Vocabulary Trainer

Gathers users' Duolingo profile and language information.  
Lists users' learned words by selected language.

Study feature (Word repetition) will be added.

## Execution

`$ docker compose up`

### UI

[`localhost:8000`](http://localhost:8000/)

#### Admin Panel

Run following command to create an admin account.  
`$ docker exec -it duovocab bash -c "python manage.py createsuperuser --noinput; python manage.py migrate"`

Panel  
[`localhost:8000/admin`](http://localhost:8000/admin)

Authentication
> Username: `admin`  
> Password: `pass`

## License

**DuoVocab** is licensed under [MIT License](https://github.com/mustafaulker/DuoVocab/blob/master/LICENSE).