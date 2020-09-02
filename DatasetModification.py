import pandas as pd

files = ["AAPL.csv","AMZN.csv","BABA.csv","GOOG.csv","HPQ.csv","IBM.csv","INTC.csv","MSFT.csv","ORCL.csv","LNVGY.csv","^IXIC.csv"]
finals = ["apple.csv","amazon.csv","alibaba.csv","google.csv","hp.csv","ibm.csv","intel.csv","microsoft.csv","oracle.csv","lenovo.csv","nasdaq.csv"]

for n in range(len(files)):
	file = files[n]
	xl = pd.read_csv(file)
	date =  xl['Date']
	Close = xl['Close']
	AD_Position  = Close.copy()
	Change = [0]*len(date)
	Momentum = [0]*len(date)
	dates = date
	reference =  dates[0]
	for i in range(1,len(date)):
		if Close[i]>Close[i-1]:
			Momentum[i] = "1"
			Change[i] = (Close[i]-Close[i-1])/Close[i-1]
		else:
			Momentum[i] = "-1"
			Change[i] = (Close[i-1]-Close[i])/Close[i-1]

	xl = pd.DataFrame({'Date':date,'Close':Close,'Change':Change,'Momentum':Momentum})
	xl.to_csv(finals[n],index = False,header = True)

