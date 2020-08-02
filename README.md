# dj_test
Test django project was given by Svyatoslav Navytka.
The source [Djinni Pages](https://djinni.co/my/inbox/3650817/).
The [Task](https://docs.google.com/document/d/1Mamfic4pUb3rrfGKzwaUEE2pKFx1Vn1BDNgVODZ1meM/edit).
The initial [data](https://docs.google.com/spreadsheets/d/1o2s6z705b0MpNsNPMoXI5yYnOrJDmwHZFx2ltFFrzlY/edit#gid=1013141086).

This project supposed to run on `python3`


## Location
This site locate [GitHub Pages](https://github.com/miha-pavel/dj_test)


## Before first launch
```
1. python3 -m venv env
2. . env/bin/activate
3. pip install -r requirements.txt
4. Configure project using `local_setings.dev.py` as example. Your local settings should be written in `local_setings.py`
5. python manage.py migrate
```


## Run Django project
```
python manage.py runserver
```
Or use makefile guide


## Makefile guide
* ```make run``` - will run Django developer server at 8000 port
* ```make test``` - will test the project with --keepdb option
* ```make pep8``` - will check the code with pylint
* ```make sh_p``` - will run django shell_plus
* ```make migrate``` - will run django "./manage.py migrate" command

## Default super user
* Username: admin
* Email address: admin@admin.com
* Password: admin
