import numpy as np
from sklearn import cross_validation
from sklearn import svm
import sys

f = open('ml-ratings.txt')
# Map<UserID, Map<ItemID, Rating>>
all_data = dict()
for line in f:
	columns = line.split(',')
	if columns[0] in all_data:
		curr = all_data[columns[0]]
		curr[columns[1]] = columns[2]
		all_data[columns[0]] = curr
	else:
		curr = dict()
		curr[columns[1]] = columns[2]
		all_data[columns[0]] = curr
f.close()
# Map<UserID, NumRatings>
userid_to_numratings = dict()
for key in all_data:
	userid_to_numratings[key] = len(all_data[key])
output_file = open('X_train_1_out.txt')
counter = 0
summation = 0
new_sum = 0
user_gain = 0
threshold = 4 #for calculating user gain, this assumes that users want items that have at least a [threshold] star rating
for line in output_file:
	results = line.split('\t')
	curr_user_dict = all_data[results[0]] #this is the original ratings
	ratings = results[1].split(',')
	ratings2 = ratings[1:]
	ratings3 = ratings2[:len(ratings2)-1]
	checker = 0
	for r in ratings3:
		split_rating = r.split(':')
		itemid = split_rating[0]
		# If there's a rating that we find in the user's original ratings, we want to compare how close our prediction is
		if itemid in curr_user_dict:
			#Mean Absolute Value Computation
			counter +=1
			summation += abs(float(split_rating[1]) - float(curr_user_dict[itemid]))
			new_sum += float(split_rating[1])
			#Mean User Gain Computation
			if split_rating[1] >= threshold:
				user_gain += float(curr_user_dict[itemid]) - float(threshold)
			else:
				user_gain += float(threshold) - float(curr_user_dict[itemid])
			# For Testing
			#print "User ID: " + results[0]
			#print "Movie ID: " + itemid
			#print "Predicted Rating: " + split_rating[1]
			#print "Actual Rating: " + curr_user_dict[itemid]
			checker += 1
		rating = split_rating[1]
		#print itemid + ":" + rating
	print checker
print "Mean Absolute Error: " + str((1/float(counter)) * summation)
print "Mean User Gain: " + str((1/float(counter)) * user_gain)
print "Average Predicted Rating: " + str((1/float(counter)) * new_sum)
output_file.close()
#print counter