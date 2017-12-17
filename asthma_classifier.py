# Author: Alvaro Esperanca
from os import listdir
from SVM import SVM
from PreProcessor import PreProcessor
from GaussianKernel import GaussianKernel

def main():
    dirList = list()

    temp = listdir("./data/Asthma/2010/")
    dirList.append(temp)
    temp = listdir("./data/Asthma/2011/")
    dirList.append(temp)
    temp = listdir("./data/Asthma/2012/")
    dirList.append(temp)
    temp = listdir("./data/Asthma/2013/")
    dirList.append(temp)
    temp = listdir("./data/Asthma/2014/")
    dirList.append(temp)

    pre = PreProcessor()
    clf = SVM(kernel=GaussianKernel(5.0), C=1.0)

    X_train, y_train = pre.loadTrainingSet("training_data/Asthma_Sample_Tokenized.csv")    
    clf.fit(X_train, y_train)

if __name__ == '__main__':
    main()