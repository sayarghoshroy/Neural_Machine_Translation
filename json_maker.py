import json

tokenized_stores = {'en_train': [], 'en_dev': [], 'en_test': [], 'bn_train': [], 'bn_dev': [], 'bn_test': []}

for key in tokenized_stores:
    file_name = "./" + str(key)[3:] + "." + str(key)[0:2]
    load = open(file_name)
    sentences = load.read().lower().split('\n')
    
    for sentence in sentences:
        token_store = sentence.lower().split(' ')
        tokenized_stores[key].append(token_store)

def build(src_string, trg_string, target_file):
	index = 0
	size = len(tokenized_stores[src_string])
	
	built_set = []
	while index < size:
		dump_stuff = {"src": tokenized_stores[src_string][index], "trg": tokenized_stores[trg_string][index]}
		built_set.append(dump_stuff)
		index += 1

	with open(target_file, "w") as file:
		for pair in built_set:
			json.dump(pair, file, ensure_ascii = False)
			file.write("\n")

build("en_train", "bn_train", "./train.json")
build("en_dev", "bn_dev", "./dev.json")
build("en_test", "bn_test", "./test.json")