def predict(sepalL, sepalW, petalL, petalW):
	dataset = pd.read_csv('Irisasli.csv')
	dataset.drop("no", axis=1, inplace=True)
	train, test = train_test_split(dataset, test_size=0.2)
	headerCol=list(dataset.columns.values)
	meanbyclass = train.groupby([headerCol[-1]]).mean()
	meanDataset = pd.DataFrame(meanbyclass)
	dTest = pd.DataFrame(test)
	dTest_pred = dTest[headerCol[-1]]
	dTest.drop(headerCol[-1], axis=1, inplace=True)
	def calculate(meanDataset,dTest) :
		i=0
		j=0
		o = [[] for i in range(len(meanDataset))]
		for i in range (len(meanDataset)):
			for j in range (len(dTest)):
				sumValue = sum(meanDataset.iloc[i] + dTest.iloc[j])
				absValue = sum(abs(meanDataset.iloc[i] - dTest.iloc[j]))
				o[i].append(1-(absValue/sumValue))
		return o

	datax = {'sepal length in cm':[sepalL],
        'sepal width in cm':[sepalW] ,
        'petal length in cm':[petalL],
        'petal width in cm':[petalW]
        }
	df = pd.DataFrame(datax, columns = ['sepal length in cm', 'sepal width in cm', 'petal length in cm', 'petal width in cm'])
	compareDf2=(pd.DataFrame(calculate(meanDataset,df))).T
	compareDf2['Predict Class'] = compareDf.idxmax(axis = 1)
	x=compareDf2['Predict Class'][0]
	return x