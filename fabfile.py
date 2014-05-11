from fabric.api import local, cd, env, run
import os.path

env.hosts = ['localhost']
env.use_ssh_config = True

def test():
    local('coverage run manage.py test -v 2')
    local('coverage report --include=food/*,pyfood/* --omit=food/migrations/*')
    local('coverage html --include=food/*,pyfood/* --omit=food/migrations/*')

def prepare_deployment():
    local('python manage.py test pyfood')
    local('git add -p && git commit')

def update_database():
    local('python manage.py syncdb')
    local('python manage.py schemamigration food --auto')
    local('python manage.py migrate food')

def deploy():
    with cd('/srv/pyfood/'):

        # get git directory
        git = os.path.dirname(os.path.realpath(__file__))
        try:
            run('git pull {0}'.format(git))
        except Exception as e:
            print 'here'
            print e
            raise e
        env.warn_only = False

        run('python manage.py migrate pyfood')
        run('python manage.py test pyfood')
        run('/srv/pyfood/manage.py runserver 0.0.0.0')
