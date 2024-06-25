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


def outlier_remove ( data, target):
	mean = data[target].mean()
	std = data[target].std()
	upper = mean + std * 3
	lower = mean - std * 3

	data = data[data[target]>=lower]
	data = data[data[target]<=upper]

	return data

def outlier_remove_2 (data, target):
	df = data[target]
	df = df[df.between(df.quantile(0.1), df.quantile(0.9))]

if __name__ == '__main__':
	data = pd.read_json ("data/train.json")

	# target = 'price'
	# data = outlier_remove( data, target)
	# plt.title (target)
	# plt.hist(data[target], bins=50)
	# plt.savefig("hist - outliers/"+target+"_his.png")

	# target = "latitude"
	# data = outlier_remove( data, target)
	# plt.title (target)
	# plt.hist(data[target], bins=50)
	# plt.savefig("hist - outliers/"+target+"_his.png")

	target = "longitude"
	data = outlier_remove( data, target)
	plt.title (target)
	plt.hist(data[target], bins=50)
	plt.savefig("hist - outliers/"+target+"_his.png")
