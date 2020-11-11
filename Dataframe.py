# for data operations
import pandas as pd

# for visualization
import matplotlib.pyplot as plt
import seaborn as sns

targets = ['Low', 'Low-Mid', 'Top-Mid', 'Top']
h_cols = ['Country', 'GDP', 'Family', 'Life', 'Freedom', 'Generosity', 'Trust']


class Dataframe :
    
    def __init__(self, data_arr):
        self.data_arr = data_arr

        self.df = self.prep_frame(data_arr[0], 2015)
        self.df = self.df.append(self.prep_frame(data_arr[1], 2016), sort=False)
        self.df = self.df.append(self.prep_frame(data_arr[2], 2017), sort=False)
        
    
    def prep_frame(self, data, year):
        df = pd.DataFrame()
        target_cols = []
        for col in h_cols:
            target_cols.extend([x for x in data.columns if col in x])
        df[h_cols] = data[target_cols]
        df['Happiness Score'] = data[[x for x in data.columns if 'Score' in x]]
        df['Target'] = pd.qcut(df[df.columns[-1]], len(targets), labels=targets)
        df["target_n"] = pd.qcut(df[df.columns[-2]], len(targets), labels=range(len(targets)))
    # Append year and assign to multi-index
        df['Year'] = year
        df = df.set_index(['Country', 'Year'])
        return df

    def spearman_correlation (self):
        spearman_cormatrix = self.df.corr(method='spearman')
        fig, ax = plt.subplots(ncols=2,figsize=(24, 8))
        sns.heatmap(spearman_cormatrix, vmin=-1, vmax=1, ax=ax[0], center=0, cmap="viridis", annot=True)
        sns.heatmap(spearman_cormatrix, vmin=-.25, vmax=1, ax=ax[1], center=0, cmap="Accent", annot=True)
        plt.show()

  