flag = "\x17'_4&)E uhh<&hW?5/\x11:'r\x11\x16\x1f\x07Jc2qTkbq\x02c`z\x03kaz\x05e0|\x012g~Ujm-\x06bd|T2mz\x02ca*\x04."

def do_xor(text, key):
	r = ''
	lk = len(key)
	for i in range(len(text)):
		#print "'" + text[i] + "' ^ '" + key[i % lk] + "'"
		r += chr(ord(text[i]) ^ ord(key[i % lk]))
	return r

for i1 in xrange(0,127):
	for i2 in xrange(0,127):
		for i3 in xrange(0,127):
			for i4 in xrange(0,127):
				key = chr(i1) + chr(i2) + chr(i3) + chr(i4)
				result = do_xor(flag, key)
				if 'EKO{' in result:
					print key, result