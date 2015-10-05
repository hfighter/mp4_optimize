import sys, os

if (len(sys.argv) > 1):
	mov = open(sys.argv[1])
	path = os.path.abspath(sys.argv[1])
	print path + '\n'

	head = mov.read(50)
	if 'moov' in head:
		print 'The file is optimized.'
	else:
		response = raw_input('The file is not optimized, optimize? (y/n): ')
		if response == 'y':
			os.system('/usr/local/bin/SublerCLI -dest "' + path + '" -optimize')
else:
	print 'No argument supplied'
