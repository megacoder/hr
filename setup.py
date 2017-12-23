#!/usr/bin/env python
# vim: nonu noet ai sm ts=4 sw=4

from distutils.core import setup, Extension

Name    = 'horizontal_ruler'
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
    scripts      = [
        'horizontal_ruler/scripts/hr',
    ]
)

