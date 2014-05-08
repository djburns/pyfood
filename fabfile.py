from fabric.api import local, lcd

def prepare_deployment():
    local('python manage.py test pyfood')
    local('git add -p && git commit')

def deploy():
    with lcd('/srv/pyfood/'):

        local('git pull ~/src/pyfood/')

        local('python manage.py migrate pyfood')
        local('python manage.py test pyfood')
        local('/srv/pyfood/manage.py runserver 0.0.0.0')
