import kaggle
import pandas as pd
import re

print("hello1")
akg = kaggle.KaggleApi()
akg.authenticate()
adatasetloc = 'paultimothymooney/denver-crime-data'
adataset = akg.dataset_view(adatasetloc)
adataset.files
print("hello")
akg.dataset_download_cli(adatasetloc, unzip=True, force=True)


myds = pd.read_csv('offense_codes.csv', header=0, names=['off_code','offcode_ext','offtype_id','offtype_name','offcategory_id','offcategory_name','crime','traffic'],sep=',',engine='c')
