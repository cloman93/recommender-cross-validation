import numpy as np
from sklearn import cross_validation
from sklearn import svm
import sys

def write_file(array, filename):
	f = open(filename, 'r+')
	for i in xrange(len(array)):
		f.write(str(array[i,0]) + ',' + str(array[i,1]) + ',' + str(array[i,2]) + '\n')


def kfold_cv(data, K):
	#putting the data into a numpy array
	raw_data = open(data)
	data_entries = 0
	for line in raw_data:
		data_entries+=1
	X = np.arange(data_entries*3).reshape(data_entries,3)
	raw_data_again = open(data)
	counter = 0
	for line in raw_data_again:
		columns = line.split(",")
		X[counter,0] = columns[0] #userid
		X[counter,1] = columns[1] #itemid
		X[counter,2] = columns[2] #user's rating for item
		counter+=1
	X_train, X_test = cross_validation.train_test_split(X, test_size=(1/float(K)), random_state=0)

	write_file(X_train, 'X_train_1.csv')
	write_file(X_test, 'X_test_1.csv')

def main():
	data = sys.argv[1]
	K = 3
	kfold_cv(data, K)

main()

