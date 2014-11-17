import math

string_1 = "hello"
string_2 = "world"
'''
prints all the combinations between two strings that are serially sent to a server 
(example sequence: 'h', 'w', 'hw', 'hwe'....etc)

assume starting character is empty ('')

                           ''
                   /                 \
                  h                   w
               /     \             /     \
              e       o           e       o
            /   \   /   \       /   \   /   \
           l     r l     r     l     r l     r 
          / \   / \  

There should be at most 2^h - 1 nodes, or combinations
'''

results = {}

def print_all_combinations(concatonated_results, chosen_char, string_1, string_2):
	global results
	if len(string_1) == 0 or len(string_2) == 0:
		return
	concatonated_results = concatonated_results + chosen_char
	# sanity check, capture histogram of results to ensure we didn't get any duplicates
	if concatonated_results not in results:
		results[concatonated_results] = 1
	else:
		print "WHOAAAA WE GOT A DUPLICATE"
		results[concatonated_results] += 1
	print concatonated_results
	# really only two possibilities here:
	# 1.) we take the first character of the first string
	# 2.) we take the first character of the second string
	print_all_combinations(concatonated_results, string_1[:1], string_1[1:], string_2)
	print_all_combinations(concatonated_results, string_2[:1], string_1, string_2[1:])


print_all_combinations("", "", string_1, string_2)

for key, value in results.iteritems():
	if value > 1:
		print "DUPLICATE ITEM: %s %s" % (key, value)
print len(results.keys())

max_possiblities = math.pow(2, max(len(string_1), len(string_2))+1) - 1
print "MAXIMUM NUMBER OF POSSIBILITIES SHOULD BE: %s" % max_possiblities


