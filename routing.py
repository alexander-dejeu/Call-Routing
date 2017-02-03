import sys
from datetime import datetime

_end = '_end_'


def route_cost_check(filename, number):
    open_file = open(filename, 'r')
    data = open_file.readlines()

    number_cost = []
    for line in data:
        print line
        for i in range(0, len(line)):
            if line[i] == ',':
                print i
                number = line[0:i]
                price = line[i+1:-1]
                number_cost.append((number, price))

    print number_cost
    trie = make_dictionary_trie(number_cost)

    open_file.close()

    print (search_trie_for(trie, number))


def make_dictionary_trie(all_tups):
    trie_root = dict()

    for tup in all_tups:
        current_node = trie_root
        number = tup[0]
        price = tup[1]

        for letter in number:
            current_node = current_node.setdefault(letter, {})
        current_node[_end] = price
    # print trie_root
    return trie_root


def search_trie_for(trie, prefix):
    current_node = trie
    for letter in prefix:
        if letter in current_node:
            current_node = current_node[letter]
        else:
            return False
    else:
        if _end in current_node:
            return current_node[_end]
        else:
            return False


def autocomplete_for(trie, prefix):
    current_node = trie
    for letter in prefix:
        if letter in current_node:
            current_node = current_node[letter]
        else:
            return False
    # print current_node
    print_trie(current_node, prefix)


def print_trie(trie, prefix):
    current_node = trie
    word = prefix
    for key in current_node:
        if key == _end:
            # print 'we reached the end'
            print str(word)
        else:
            word = prefix + key
            print_trie(current_node[key], word)

route_cost_check('route-costs-100.txt', '+3363349')
