from itertools import zip_longest
from collections import defaultdict
from itertools import islice
from collections import defaultdict, OrderedDict
import copy

def calculate_checksum(representation):
    checksum = 0
    for i in range(len(representation)):
        if isinstance(representation[i], int):
            checksum+= representation[i]*i
    return checksum

def parse_input():
    with open("input.txt", "r") as file:
        disk_input = list(file.read().strip())
    return list(map(int, disk_input))

def get_dot_representation(disk_input):
    blocks = []
    spaces = []
    for i in range(len(disk_input)):
        if i%2==0:
            blocks.append(disk_input[i])
        else:
            spaces.append(disk_input[i])
    representation = []
    empty_indices = []
    empty_indices_two = defaultdict(int, OrderedDict())  #keep track of index of where empty spaces are in representation {begining_index:how many empty space till next block}

    for idx, (block, space) in enumerate(zip_longest(blocks, spaces, fillvalue=0)):
        start_index = len(representation) + block
        empty_indices += [start_index+i for i in range(space)]
        if space !=0:
            empty_indices_two[start_index] = space
        representation += [idx]*block
        representation += ["."]*space
    representation2 = copy.deepcopy(representation)
    return representation, representation2, empty_indices, empty_indices_two



def get_representation_dict(representation, empty_indices_two):
    representation_dict = defaultdict(list)
    l_representation = len(representation)
    for k in range(l_representation, 0, -1):
        if isinstance(representation[k-1], int):
            representation_dict[representation[k-1]] += [k-1]
    items = list(empty_indices_two.items())
    return representation_dict, items

def move_file_part1(representation, empty_indices):
    l_representation = len(representation)
    l_empty_indices = len(empty_indices)
    j = 0
    for k in range(l_representation, 0, -1):
        if l_representation-k >= l_empty_indices:
            break
        if isinstance(representation[k-1], int):
            tmp = representation[k-1]
            representation[k-1] = "."
            loc = empty_indices[j]
            representation[loc] = tmp
            j+=1
    return representation

def move_file_part2(representation, representation_part2, items):
    for idx, (k1, v1) in enumerate(representation_part2.items()):
        for idy, (k2, v2) in enumerate(items):
            if len(v1) <=v2 and k2 < v1[0]:
                j = 0
                for v in v1:
                    new_dict = OrderedDict()
                    representation[v] = "."
                    representation[k2+j] = k1
                    tmpk, tmpv = items[idy]
                    new_key = tmpk+1
                    new_value = tmpv-1
                    items[idy] = (new_key, new_value)
                    j+=1
                break
    return representation

def main():
    disk_input = parse_input()
    representation1, representation2, empty_indices, empty_indices_two = get_dot_representation(disk_input)

    updated_representation1 = move_file_part1(representation1, empty_indices)
    checksum1 = calculate_checksum(updated_representation1)
    print(checksum1)

    representation_dict, items = get_representation_dict(representation2, empty_indices_two)
    updated_representation2 = move_file_part2(representation2, representation_dict, items)
    checksum2 = calculate_checksum(updated_representation2)
    print(checksum2)

if __name__ == "__main__":
    main()
            
    
    
        
