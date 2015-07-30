def pre_fork(server, worker):
    f = '/tmp/app-initialized'
    open(f, 'w').close()

bind = 'unix:///tmp/nginx.socket'
