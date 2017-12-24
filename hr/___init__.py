#!/usr/bin/python
# vim: noet sw=4 ts=4

import	sys
import	os
import	argparse

try:
	from version import Version
except:
	Version = 'WTF'

class	HR( object ):

	PROG = 'hr'

	def	__init__( self ):
		pass

	def	main( self ):
		p = argparse.ArgumentParser(
			prog = HR.PROG,
			description = '''
				Repeat a pattern enough times to fill out a line on a
				terminal screen.
			''',
			epilog = '''
				You were expecting, maybe, Valerie Perrine?
			'''
		)
		default = os.getenv( 'COLUMNS' )
		if default and default.isdigit():
			default = int(default)
		else:
			default = 80
		p.add_argument(
			'-w',
			'--width',
			metavar = 'N',
			type    = int,
			dest    = 'width',
			default = default,
			help    = 'width of screen if not {0}'.format( default ),
		)
		p.add_argument(
			'-v',
			'--version',
			action  = 'version',
			version = Version,
			help    = 'program version',
		)
		default = [ '-' ]
		p.add_argument(
			dest    = 'patterns',
			metavar = 'STR',
			default = default,
			nargs   = '*',
			help    = 'patterns to use if not {0}'.format( default ),
		)
		self.opts = p.parse_args()
		for pattern in self.opts.patterns:
			reps = int(
				self.opts.width / len( pattern )
			)
			line = pattern * (reps + 1)
			print line[:self.opts.width]
		return 0

if __name__ == '__main__':
	sys.exit( HR().main() )
