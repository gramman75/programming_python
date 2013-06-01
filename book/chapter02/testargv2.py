def getopts(argv):
	opts = {}
	while argv:
		if argv[0][0] == '-':
			opts[argv[0]] = argv[1]
			argv = argv[2:]
		else:
			argv = argv[1:]
	return opts

if __name__ == '__main__':
	import sys
	argv = sys.argv
	print(argv)
	opts = getopts(argv)
	print(opts)

	