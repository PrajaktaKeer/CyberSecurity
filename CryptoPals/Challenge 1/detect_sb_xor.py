file1 = open('crypto.txt', 'r') 
Lines = file1.read().splitlines() 
possible_messages = []

def get_english_score(input_bytes):
    # From https://en.wikipedia.org/wiki/Letter_frequency
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])

def xor(str, val):
	output = b''
	for byte in str:
		output += bytes([byte ^ val])
	return output

for line in Lines:
	for i in range(256):
		pt = xor(bytes.fromhex(line), i)#plaintext for key = 88
		score = get_english_score(pt)
		data = {'PlainText': pt, 'score': score, 'key': i}
		possible_messages.append(data)
best_score = sorted(possible_messages, key = lambda x: x['score'], reverse=True)[0]
for item in best_score:
	print("{}: {}".format(item.title(), best_score[item]))