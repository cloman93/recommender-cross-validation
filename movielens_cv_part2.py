import numpy as np
from sklearn import cross_validation
from sklearn import svm
import sys

f = open('ml-ratings.txt')
# Map<UserID, Map<ItemID, Rating>>
d = dict()
for line in f:
	columns = line.split(',')
	if columns[0] in d:
		curr = d[columns[0]]
		curr[columns[1]] = columns[2]
		d[columns[0]] = curr
	else:
		curr = dict()
		curr[columns[1]] = columns[2]
		d[columns[0]] = curr
f.close()
output_file = open('sample_output.txt')
#counter = 0
for line in output_file:
	results = line.split('\t')
	curr_user_dict = d[results[0]] #this is the original ratings
	ratings = results[1].split(',')
	ratings2 = ratings[1:]
	ratings3 = ratings2[:len(ratings2)-1]
	for r in ratings3:
		split_rating = r.split(':')
		itemid = split_rating[0]
		# If there's a rating that we find in the user's original ratings, we want to compare how close our prediction is
		if itemid in curr_user_dict:
			#print "User ID: " + results[0]
			#print "Movie ID: " + itemid
			#print "Predicted Rating: " + split_rating[1]
			#print "Actual Rating: " + curr_user_dict[itemid]
			#counter +=1
		rating = split_rating[1]
		#print itemid + ":" + rating
output_file.close()
#print counter