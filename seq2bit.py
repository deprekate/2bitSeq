import sys

def encode(string):
	result = 1
	for char in string:
		result = (result << 2) | ((ord(char) >> 1) & 3)
	return result

def decode(bits):
	result = ''
	enc = bits
	while enc > 1:
		byte = enc & 3
		if byte == 0:
			result += 'A'
		elif byte == 1:
			result += 'C'
		elif byte == 2:
			result += 'T'
		elif byte == 3:
			result += 'G'
		enc = enc >> 2
	return result[::-1]

seq = 'CGATCGTAGCTAGCTAGCTAGCTAGCTAGATAAAATATTATTATATTTAGGCGGCCTAGCTAGCTAGCTAGCTAGCTGACTGATCGATGCATGCTAGCTAGCTAGCTAGCTGACTGATCGATGCTAGCTAGCTAGCTAGCTAGCTAGCATCGATCG'
print(seq)
print('sizeofseq: ', sys.getsizeof(seq))
e = encode(seq)
print('sizeofbits: ', sys.getsizeof(e))
#print(e)
d = decode(e)
print(d)
