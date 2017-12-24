#!/usr/bin/env python
# vim: nonu noet ai sm ts=4 sw=4

from setuptools import setup

Name    = 'hr'
Version = '0.0.0'
CLI     = Name.lower()

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
	long_description = open( 'README.md' ).read(),
	zip_safe         = True,
	entry_points = {
		'console_scripts' : [
			'{0} = {1}:main'.format(
				CLI,
				Name,
			),
		],
	},
)

