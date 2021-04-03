import pandas as pd
import sys, json, numpy as np
import csv
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def main():
    lines = sys.stdin.readlines()
    lines = json.loads(lines[0])
    filePath = lines["filePath"]

    df = pd.read_csv(filePath)
    df = df.select_dtypes(include=np.number)

    sc = StandardScaler()
    df = sc.fit_transform(df)

    pca = PCA()
    newData = pca.fit_transform(df)

    perVar = np.round(pca.explained_variance_ratio_ * 100, decimals=1)

    columnNames = ["PC" + str(x) for x in range(1, len(perVar) + 1)]

    newDf = pd.DataFrame(newData, columns=columnNames)

    newDf.to_csv(filePath, index=False)

    perVar = perVar.tolist()

    output = {"columnNames": columnNames, "values": perVar}
    output = json.dumps(output)

    print(output)


# start process
if __name__ == "__main__":
    main()