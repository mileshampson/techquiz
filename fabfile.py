from __future__ import with_statement
from fabric.api import *
from fabric.contrib.files import exists

env.hosts = ['prodbox']
# env.password = 'your password goes here'
project_tgz = 'techquiz.tgz'
install_path = '/srv/techquiz/'
apache2_config = 'techquiz.aptive.net'
cron_file = 'techquiz'
awstats_config = 'awstats.techquiz.aptive.net.conf'
logrotate_config = 'techquiz.aptive.net'

def deploy():
    local('tar czf '+project_tgz+' src config static djangosite')
    put(project_tgz, '/tmp/')
    local('rm '+project_tgz)
    if not exists(install_path):
        sudo("mkdir -p "+install_path)
        sudo("chown www-data "+install_path)
    with cd(install_path):
        sudo("tar xzf /tmp/"+project_tgz, user="www-data")
        if not exists("log"):
            sudo("mkdir log", user="www-data")
        run("rm /tmp/"+project_tgz)
        sudo("cp config/apache/"+apache2_config+" /etc/apache2/sites-available")
        sudo("a2ensite "+apache2_config)
        sudo("apache2ctl restart")
        sudo("cp config/cron/"+cron_file+" /etc/cron.d")
        sudo("cp config/awstats/"+awstats_config+" /etc/awstats")
        sudo("cp config/logrotate/"+logrotate_config+" /etc/logrotate.d")
        
