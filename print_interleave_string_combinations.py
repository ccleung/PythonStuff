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
              e       w           h       o
            /   \   /   \       /   \   /   \
           l     w e     o     e     o h     r 
         / \   / \  /\   /\    /\   /\  /\   /\        

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
	#print "STRING1 %s and STRING2 %s" % (string_1, string_2)
	# really only two possibilities here:
	# 1.) we take the first character of the first string
	# 2.) we take the first character of the second string
	print "RESULT: %s %s" % (concatonated_results, len(results.keys()))
	string_1_truncated = string_1[1:] if len(string_1[1:]) > 1 else ""
	string_2_truncated = string_2[1:] if len(string_2[1:]) > 1 else ""
	print_all_combinations(concatonated_results, string_1[:1], string_1_truncated, string_2)
	print_all_combinations(concatonated_results, string_2[:1], string_1, string_2_truncated)


print_all_combinations("", "", string_1, string_2)

# check for duplicates
for key, value in results.iteritems():
	if value > 1:
		print "DUPLICATE ITEM: %s %s" % (key, value)
print len(results.keys())

# not correct since our number of combinations is more complex than 
# just the depth of the binary tree of choices
max_possiblities = math.pow(2, max(len(string_1), len(string_2))+1) - 1
print "MAXIMUM NUMBER OF POSSIBILITIES SHOULD BE: %s" % max_possiblities


