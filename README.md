# Hyperion

Hyperion is a simple web password manager write using Python, Django and DRF and Swagger for documentation.

  - store all user accounts
  - using encryption to store passwords in database
  - rest api with JWT autorizatrion

### Demo

...

### Installation

Clone github repo:
```sh
$ git clone git://github.com/vThaian/hyperion-django.git
$ cd hyperion-django
```

Create virtualenv for project:
```sh
$ virtualenv ~/virtualenvs/hyperion
```

Run virtualenv and install packages from requiremnts.txt:
```sh
$ source ~/virtualenvs/hyperion/bin/activate
$ pip install -r ~/PycharmProjects/hyperion-django/requirements.txt
```

Run server:
```sh
$ ~/virtualenvs/hyperionbin/python PycharmProjects/hyperion-django/manage.py runserver
```

Run tests:
```sh
$ ~/virtualenvs/hyperionbin/python PycharmProjects/hyperion-django/manage.py test
```