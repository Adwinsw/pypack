#!/usr/bin/env python
import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
# APPS_DIR = os.path.join(BASE_DIR, 'src') etc: python3 -m django startapp src/
# {'cmd': cmd, 'cwd': APPS_DIR}

HTTP_HOST = '0.0.0.0'
HTTP_PORT = '8000'

def main():
    print("Start Gunicorn WSGI HTTP Server")
    bind = '{}:{}'.format(HTTP_HOST, HTTP_PORT)
    log_format = '%(h)s %(t)s %(L)ss "%(r)s" %(s)s %(b)s '

    cmd = [
        'python3', '-m',
        'gunicorn', 'djangor.wsgi',
        '-b', bind,
        '-k', 'gthread',
        '--threads', '2',
        '-w', '2',
        '--max-requests', '1024',
        '--access-logformat', log_format,
        '--access-logfile', '-'
    ]
    subprocess.call(cmd)

if __name__ == "__main__":
    main()
