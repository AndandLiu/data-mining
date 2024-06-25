import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats
from statsmodels.stats import multicomp
import statsmodels.api as sm

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler, FunctionTransformer
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import  DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

import sys


def len( list ):
	return list.__len__()

def outlier_remove (data, target): # actual handler
	mean = data[target].mean()
	std = data[target].std()
	upper = mean + std * 3
	lower = mean - std * 3

	data = data[data[target]>=lower]
	data = data[data[target]<=upper]

	return data

if __name__ == '__main__':
	col = ["bathrooms","bedrooms","building_id","created", 
			"description","display_address","features",
			"latitude","listing_id","longitude","manager_id",
			"photos","price","street_address","interest_level"]
	
	data = data = pd.read_json ("data/train.json")
	
	print ("counting missing values: ")
	# Missing value count handling=====================
	for i in range (15):
		# groupby cannot handle list type: fetures and photes (exception)
		if i == 6 or i == 11:
			continue
		result = ( data.groupby( data[col[i]]  ).count() )
		result.to_csv("missing_count_result/"+col[i]+"_missing_count_result.csv")


	# handle list type: features and photos sapretely
	list_len_operator = np.vectorize(len)

	data["features_count"] = list_len_operator(data["features"])
	data["photos_count"] = list_len_operator(data["photos"])
	

	result = ( data.groupby( data["features_count"]  ).count() )
	result.to_csv("missing_count_result/features_missing_count_result.csv")

	result = ( data.groupby( data["photos_count"]  ).count() )
	result.to_csv("missing_count_result/photos_missing_count_result.csv")

	Oulier handling =================================
	
	print ("counting outliers for each: ")
	for target in ["price","latitude","longitude"]:
		count_before = data[target].count()
		print (target, ": ")
		print ("before:", count_before)

		temp = data
		result = outlier_remove(temp, target)

		count_after = result[target].count()
		print ("after: ", count_after)
		print ("difference: ", count_before-count_after)
		print ("proportion: ", (count_before-count_after)/count_before,"\n")


	print ("handling outliers: ")
	for target in ["price","latitude","longitude"]:
		count_before = data[target].count()
		print ("after ", target, ": ")
		print ("before:", count_before)

		data = outlier_remove(data, target)

		count_after = data[target].count()
		print ("after: ", count_after)
		print ("difference: ", count_before-count_after)
		print ("proportion: ", (count_before-count_after)/count_before,"\n")
