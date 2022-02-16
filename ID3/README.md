# ID3

This is my implementation of the ID3 decision tree algorithm. In the id3.py file you can specify a path to your training dataset and your testing dataset. Included in this implementation are 3 datasets: lakesDiscreteFold1.arff, lakesDiscreteFold2.arff, and Table4-3.arff. 


## Usage

Be sure that python 3 is installed on your machine. Using a command line interface, browse to the directory where the DataReader.py file lives. Use the following command to run the script.

```
 python3 DataReader.py
```
The script will build a decision tree using the data from the training set and use that decision tree to predict the target values of the testing set. It will then print out the accuracy of its predictions.