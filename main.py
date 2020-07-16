import time
from datetime import datetime as dt

REDIRECT = '127.0.0.1'
HOST_PATH = '/etc/hosts'


def run():

    from_hour = 8
    to_hour = 19

    web_sites = [
        'www.facebook.com',
        'facebook.com',
        'www.instagram.com'
    ]

    while True:
        if from_hour < dt.now().hour < to_hour:
            lock(web_sites)

        else:
            unlock(web_sites)
        time.sleep(10)


def lock(sites_list):
    print('Ponte a trabajar .... :)')
    with open(HOST_PATH, 'r+') as f:
        content = f.read()
        for web_site in sites_list:
            if web_site in content:
                pass
            else:
                f.write(('{} {}\n').format(REDIRECT, web_site))


def unlock(sites_list):
    with open(HOST_PATH, 'r+') as f:
        content = f.readlines()
        f.seek(0)
        for line in content:
            if not any(web_site in line for web_site in sites_list):
                f.write(line)
        f.truncate()
    print('diviertete')


if __name__ == '__main__':
    run()
