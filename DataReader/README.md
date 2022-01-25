# DataReader

DataReader is a python script that asks a user for the filename of an arff file. It then reads the file and stores the features and instances in an ArffData object. It also outputs the min and max for each numerical feature and outputs the set of possible values for each discrete feature.


## Usage

Be sure that python 3 is installed on your machine. Using a command line interface, browse to the directory where the DataReader.py file lives. Use the following command to run the script.

```
 python3 DataReader.py
```
The script will ask for the path and name of the file. The files live in the includes directory so your response should look something like:

``` 
includes/lakes.arff
```
After that the script will print out the results of the min/max for each numerical feature and the set of possible values for the discrete features.