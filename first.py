import pandas as pd

mydataset = {
    'name' : ['shivam','ved','bhayani'],
    'marks' : [90, 89, 98],
    'roll no' : [62, 34, 20]
}

# myvar = pd.DataFrame(mydataset) #this is like exelsheet
myvar = pd.Series(mydataset)  #this is like normal string type but in one line like that
print(myvar[0])
print(myvar)