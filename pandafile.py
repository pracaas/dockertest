import pandas as pd

def getpandas():
    lst = ['Geeks', 'For', 'Geeks', 'is',
       'portal', 'for', 'Geeks']
    df = pd.DataFrame(lst)
    print(df)

if __name__ == "__main__":
    getpandas()
