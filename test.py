
import pandas as pd

if __name__ == '__main__':
    data1 = {
        "a": ['1', '2', '3'],
        "b": ['4', '5', '6'],
        "c": ['7', '8', '9']
    }

    df1 = pd.DataFrame(data1)



    df1["a"].apply( lambda x : float(x))

    print(df1)
