# -*- coding:utf-8 -*-
import os
os.makedirs('glance1/api')
os.makedirs('glance1/cmd')
os.makedirs('glance1/db')
l = []
l.append(open('glance1/__init__.py','w'))
l.append(open('glance1/api/__init__.py','w'))
l.append(open('glance1/api/policy.py','w'))
l.append(open('glance1/api/versions.py','w'))
l.append(open('glance1/cmd/__init__.py','w'))
l.append(open('glance1/cmd/manage.py','w'))
l.append(open('glance1/db/models.py','w'))
map(lambda f:f.close(),l)
