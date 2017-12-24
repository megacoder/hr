#!/usr/bin/python
# vim: noet sw=4 ts=4

import	sys
import	os
import	argparse

try:
	from version import Version
except:
	Version = 'WTF'

PROG = 'hr'

def	main( ):
	p = argparse.ArgumentParser(
		prog = PROG,
		description = '''
			Repeat a pattern enough times to fill out a line on a
			terminal screen.
		''',
		epilog = '''
			You were expecting, maybe, Valerie Perrine?
		'''
	)
	default = None
	p.add_argument(
		'-o',
		'--out',
		dest    = 'out',
		metavar = 'FILE',
		default = default,
		help    = 'write here if not stdout',
	)
	#
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
	opts = p.parse_args()
	if opts.out:
		try:
			sys.stdout = open( opts.out, 'wt' )
		except Exception, e:
			print >>sys.stderr, 'Cannot redirect output to "{0}".'.format(
				opts.out
			)
			raise e
	for pattern in opts.patterns:
		reps = int(
			opts.width / len( pattern )
		)
		line = pattern * (reps + 1)
		print line[:opts.width]
	return 0

if __name__ == '__main__':
	sys.exit( main() )
