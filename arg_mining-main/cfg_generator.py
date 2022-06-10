import random as rd

# Example Grammar rules
rules = [
        {
        "S":[ 
            ["a", "S", "a"] ,
            ["b", "S", "b"] ,
            ["S_bar"],
            ["S_bar"]
        ], 
        "S_bar":[
            ["c"]
        ]
    }, 
        {
        "S":[ 
            ["A", "c", "B"],
            ["A", "c", "B"],
            ["A", "c", "B"]
        ], 
        "A": [
            ["a", "A"] ,
            ["A_bar"],
            ["A_bar"]
        ],
        "A_bar": [
            ["a"]
        ],
        "B": [
            ["b", "B"] ,
            ["B_bar"],
            ["B_bar"]
        ],
        "B_bar": [
            ["b"]
        ]
    },
        {
        "S":[ 
            ["A", "c", "B"],
            ["A", "c", "B"],
            ["A", "c", "B"]
        ], 
        "A": [
            ["a", "A"] ,
            ["b", "A"],
            ["A_bar"] ,
            ["A_bar"]
        ],
        "A_bar": [
            ["a"],
            ["b"]
        ],
        "B": [
            ["a", "B"] ,
            ["b", "B"] ,
            ["B_bar"],
            ["B_bar"]
        ],
        "B_bar": [
            ["a"],
            ["b"]
        ]
    }

]


# Contributed by Tiger Sachase
# Used to parse any list of strings and insert them in place in a list 
def generate_items(items):
    for item in items:
        if isinstance(item, list):
            for subitem in generate_items(item):
                yield subitem
        else:
            yield item       

# Our expansion algo
def expansion(start, len_max, last_ind, ind_rule):
    for element in start:
        if element in rules[ind_rule]:
            loc = start.index(element)
            # print(start)
            if(len(start) > len_max):
                start[loc] = rd.choice(rules[ind_rule][element])
            else:
                start[loc] = rd.choice(rules[ind_rule][element][:-last_ind])
        result = [item for item in generate_items(start)]
    
    for item in result:
        if not isinstance(item, list):
            if item in rules[ind_rule]:
                result = expansion(result, len_max, last_ind, ind_rule)
    
    return result


def to_string(result):
    return ' '.join(result)

from tqdm import tqdm
def generate_dataset(total_size, len_of_cfg):
    
    train_data = []
    train_label = []
    test_data = []
    test_label = []

    for i in tqdm(range(total_size)):
        for j in range(3):
            train_data.append(to_string(expansion(["S"], len_of_cfg, 2, j)))
            train_label.append(j)
            test_data.append(to_string(expansion(["S"], len_of_cfg, 2, j)))
            test_label.append(j)
    temp =  list(zip(train_data, train_label))
    rd.shuffle(temp)
    train_data, train_label = zip(*temp)
    train_data, train_label = list(train_data), list(train_label)

    temp =  list(zip(test_data, test_label))
    rd.shuffle(temp)
    test_data, test_label = zip(*temp)
    test_data, test_label = list(test_data), list(test_label)
    

    return (train_data, train_label), (test_data, test_label)

# # An example test you can run to see it at work
# result = ["S"]
# print(result) # Print our starting result
# result = expansion(result, 200, 2, 2) # Expand our starting list 
# final = to_string(result)
(train_data, train_label), (test_data, test_label) = generate_dataset(5000, 200)
import pickle
data_path = "data.pkl"
with open(data_path, "wb") as f:
  pickle.dump(zip((train_data, train_label), (test_data, test_label)), f)