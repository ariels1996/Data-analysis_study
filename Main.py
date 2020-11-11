# this code using data from https://www.kaggle.com/unsdsn/world-happiness


# for data operations
import pandas as pd

# for providing the path
import os
print(os.listdir('./data'))

# import myModule
from Dataframe import Dataframe

class Main :

    def __init__(self):
        
        try:
            self.data_arr = []
            self.data_2015 = pd.read_csv('./data/2015.csv')
            self.data_2016 = pd.read_csv('./data/2016.csv')
            self.data_2017 = pd.read_csv('./data/2017.csv')
            self.data_arr.append(self.data_2015)
            self.data_arr.append(self.data_2016)
            self.data_arr.append(self.data_2017)
        except:
            print("Error opening file")
            return

        self.dataframe = Dataframe(self.data_arr)
        self.dataframe.spearman_correlation()
        print(self.dataframe.df.head())

def main():
    Main()

main()