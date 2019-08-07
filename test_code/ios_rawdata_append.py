import requests
import json
import os
#from pandas.io.json import json_normalize
import datetime
#import pandas as pd
import sys

fileObject = open('ios_test.txt', 'a')
for row in sys.stdin:
    fileObject.write(row)
    fileObject.write("\n")