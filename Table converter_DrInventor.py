import json
import pandas as pd
import ast

precision_data = []
recall_data = []
f1_data = []
support_data = []
micro_avg_data = []
macro_avg_data = []
weighted_avg_data = []

keys = ["Technique and metric Name", "supports", "contradicts", "parts_of_same" ]
data_1 = pd.DataFrame(columns = keys)
keys_2 = ["Technique and metric Name", "precision", "recall", "f1", "support" ]
data_2 = pd.DataFrame(columns = keys_2)
def add_data(name, data, df):
	df.append([name] + [i[1] for i in data])
	return df;

while True:
	print("Enter data name (-1) to exit) :")
	data_name = input()
	if(data_name == "-1"):
		break
	print("Enter data")
	technique_name = data_name
	data = input()
	data = data.replace('\'', '\"')
	data_dict = ast.literal_eval(data)

	data_prec = data_dict["precision"]
	temp = []
	for i in data_prec:
		temp.append((i, data_prec[i]))
	precision_data.append((data_name, temp))

	data_recall = data_dict["recall"]
	temp = []
	for i in data_recall:
		temp.append((i, data_recall[i]))
	recall_data.append((data_name, temp))

	data_support = data_dict['support']
	temp = []
	for i in data_support:
		temp.append((i, data_support[i]))
	support_data.append((data_name, temp))

	data_f1 = data_dict['f1']
	temp = []
	for i in data_f1:
		temp.append((i, data_f1[i]))
	f1_data.append((data_name, temp))

	data_micro_avg = data_dict['micro_avg']
	temp = []
	for i in data_micro_avg:
		temp.append((i, data_micro_avg[i]))
	micro_avg_data.append((data_name, temp))

	data_macro_avg = data_dict['macro_avg']
	temp = []
	for i in data_macro_avg:
		temp.append((i, data_macro_avg[i]))
	macro_avg_data.append((data_name, temp))

	data_weighted = data_dict['weighted_avg']
	temp = []
	for i in data_weighted:
		temp.append((i, data_weighted[i]))
	weighted_avg_data.append((data_name, temp))

def convert_dict(keys, data):
	dict1 = {}
	for ind, key in enumerate(keys):
		print(key, dict1)
		dict1[key] = data[ind]
	return dict1
for i in precision_data:
	technique_name = i[0]
	data = i[1]
	data_1 = data_1.append(convert_dict(keys, ["precision - " + technique_name] + [i[1] for i in data]), ignore_index = True)

for i in recall_data:
	technique_name = i[0]
	data = i[1]
	data_1 = data_1.append(convert_dict(keys, ["recall - " + technique_name] + [i[1] for i in data]), ignore_index = True)

for i in f1_data:
	technique_name = i[0]
	data = i[1]
	data_1 = data_1.append(convert_dict(keys, ["f1 - " + technique_name] + [i[1] for i in data]), ignore_index = True)

for i in support_data:
	technique_name = i[0]
	data = i[1]
	data_1 = data_1.append(convert_dict(keys, ["support - " + technique_name] + [i[1] for i in data]), ignore_index = True)

for i in micro_avg_data:
	technique_name = i[0]
	data = i[1]
	data_2 = data_2.append(convert_dict(keys_2, ["micro_avg - " + technique_name] + [i[1] for i in data]), ignore_index = True)

for i in macro_avg_data:
	technique_name = i[0]
	data = i[1]
	data_2 = data_2.append(convert_dict(keys_2, ["macro_avg - " + technique_name] + [i[1] for i in data]), ignore_index = True)

for i in weighted_avg_data:
	technique_name = i[0]
	data = i[1]
	data_2 = data_2.append(convert_dict(keys_2, ["weighted_avg - " + technique_name] + [i[1] for i in data]), ignore_index = True)
print(data_1)
print(data_2)

data_1.to_csv("Classwise Results.csv")
data_2.to_csv("Total Results.csv")