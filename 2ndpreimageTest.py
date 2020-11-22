from hashtable import *
import hashlib
import random
import string
import matplotlib.pyplot as plt


# --- SECOND PRE-IMAGE RESISTANCE TEST ---


def sec_preimage_blake2b():
	trials = 0
	while True:

		randstr1 = '54321'
		randstr2 = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = 5))

		if randstr1 == randstr2:
			continue
		else:
			hash_obj_1 = hashlib.blake2b(randstr1.encode()).hexdigest()
			hash_obj_2 = hashlib.blake2b(randstr2.encode()).hexdigest()

			trials += 1

			if hash_obj_1[0:2] == hash_obj_2[0:2]:
				break
	
	return trials


def sec_preimage_hash():
	trials = 0
	while True:

		randstr1 = '54321'
		randstr2 = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = 5))

		if randstr1 == randstr2:
			continue
		else:
			h1 = Hashtable(10000)
			hash_obj_1 = h1.hashfunction(randstr1.encode())
			try:
				hash_obj_1 = hash_obj_1.hexdigest()
			except:
				hash_obj_1 = str(hash_obj_1)

			h2 = Hashtable(100000)
			hash_obj_2 = h2.hashfunction(randstr2.encode())
			try:
				hash_obj_2 = hash_obj_2.hexdigest()
			except:
				hash_obj_2 = str(hash_obj_2)

			trials += 1

			if hash_obj_1[0:2] == hash_obj_2[0:2]:
				break
	
	return trials


# Storing number of trials in a list
li_b = []
for i in range(100):
	li_b.append(sec_preimage_blake2b())

li_h = []
for i in range(100):
	li_h.append(sec_preimage_hash())

# Plotting
plt.hist(li_b, alpha=0.8, width=100, label='Blake2b')
plt.hist(li_h, alpha=0.8, width=100, label='Hash')
plt.legend(loc='upper right')
plt.title('Second pre-image resistance')
plt.xlabel('Trials')
plt.ylabel('Frequency')
plt.show()

print("Average blake2b = ", sum(li_b)/len(li_b))
print("Average hash = ", sum(li_h)/len(li_h))

