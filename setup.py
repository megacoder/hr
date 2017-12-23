#!/usr/bin/env python

from distutils.core import setup, Extension

Name    = 'hr'
Version = '0.0.0'

with open( '{0}/version.py'.format( Name ), 'wt' ) as f:
    print >>f, 'Version = "{0}"'.format( Version )

setup(
    name         = Name,
    version      = Version,
    description  = 'Horizontal rules for your terminal',
    url          = 'http://www.megacoder.com',
    author       = 'Tommy Reynolds',
    author_email = 'oldest.software.guy@gmail.com',
    packages     = [ Name ],
)

