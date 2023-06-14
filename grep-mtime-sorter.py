import re, sys
from datetime import datetime
from pathlib import Path

#We will use the coloring to get the filename and line number
#This is likely not very portable but will solve my immediate needs
line_re = re.compile('^\x1b\[35m\x1b\[K(.*?)\x1b.*$')
line_buffer = tuple(sys.stdin)

def iso_format(timestamp):
	if timestamp:
		return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M')
	else:
		return 'Unknown'

def get_mtime(line):
	[filename] = line_re.match(line).groups()
	try:
		return Path(filename).stat().st_mtime
	except:
		return 0

for time, index in sorted((get_mtime(line), index) for index, line in enumerate(line_buffer)):
	print(f'\x1b[34m{iso_format(time):>16}\x1b[0m', line_buffer[index], end='')
