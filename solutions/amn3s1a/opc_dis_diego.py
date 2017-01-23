import binascii

password = [919161, 1859495, 985017, 1377995, 1659485, 1068148, 1599708, 738095, 525756, 1332298, 1274390, 1926028, 1462800, 157737, 1144861, 460670, 411631, 1531994, 1992766, 197800, 349871, 2033064, 852423, 23667, 1211575, 1771461, 1727029, 86621, 805407, 616682, 279968, 675489]

chars = []
index = []
for e in password:
	c = chr(int("{0:b}".format(e).zfill(32)[-16:-8], 2) ^ 55)
	i = int("{0:b}".format(e).zfill(32)[:-16], 2) ^ 19
	index.append(i)
	chars.append(c)

pwd = []
for i in range(len(index)):
	pwd.append(chars[index.index(i)])

print "".join(pwd)
