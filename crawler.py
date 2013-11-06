import string
import pdb
# texto = "como uma onde no mar, como uma onda no mar."

def remove_punctuation(txt):
	return txt.translate(None, string.punctuation)

def remove_less_than_3(txt):
	i = 0;
	txt = txt.split(" ")
	# pdb.set_trace()
	while i < len(txt):
		if len(txt[i]) < 3:
			txt.remove(txt[i])
		i += 1
	txt = string.join(txt, " ")
	return txt


