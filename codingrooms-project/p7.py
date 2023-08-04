import csv
from collections import Counter
import statistics as st
import matplotlib.pyplot as plt
# Write your functions here


def load_data(file_name: str, types: dict): #this function loads the data in from the titanic file
    name = []
    newTypes = []
    for key, value in types.items():
        name.append(key)
        newTypes.append(value)
    info = {(col_name, col_type): [] for col_name, col_type in zip(name, newTypes)}
    with open(file_name, 'r') as f:
        next(f)
        for line in f:
            line = line.strip()
            inf = line.split(',')
            for x in range(0, len(info), 1):
                info[(name[x], newTypes[x])].append(newTypes[x](inf[x]))
    return info


def summarize(data: dict): #this function summarizes the data and calculates the different min, max, etc.
    daKey = []
    daVal = []
    for key, val in data.items():
        daKey.append(key)
        daVal.append(val)

    for i in range(0, len(daKey), 1):
        print("Statistics for " + daKey[i][0])
        if daKey[i][1] == int or daKey[i][1] == float:
            print("    min:" + (" " * (7 - len(str(round(float(max(daVal[i])), 1))))) + str(round(float(min(daVal[i])), 1)))
            print("    max:" + (" " * (7 - len(str(round(float(max(daVal[i])), 1))))) + str(round(float(max(daVal[i])), 1)))
            print("   mean:" + (" " * (7 - len(str(round(float(st.mean(daVal[i])), 1)))) + str(round(float(st.mean(daVal[i])), 1))))
            print("  stdev:" + (" " * (7 - len(str(round(st.stdev(daVal[i]), 1))))) + str(round(st.stdev(daVal[i]), 1)))
            print("   mode:" + (" " * (7 - len(str(round(float(st.mode(daVal[i])), 1)))) + str(round(float(st.mode(daVal[i])), 1))))
        else:
            print("Number of unique values: " + str(len(set(daVal[i]))))
            print("      Most common value: " + Counter(daVal[i]).most_common(1)[0][0])


def pearson_corr(x: list, y: list): #this function finds important correlations in the data and recognizes means and standard deviations for the graph
    xBar = st.mean(x)
    yBar = st.mean(y)
    xStd = st.stdev(x)
    yStd = st.stdev(y)
    num = 0.0
    for i in range(len(x)):
        num = num + (x[i] - xBar) * (y[i] - yBar)
    return num / ((len(x) - 1) * xStd * yStd)


def survivor_vis(data: dict, col1: tuple, col2: tuple): #this function outputs the data in graph form
    xName = col1[0]
    yName = col2[0]
    eleX = 0
    eleY = 0
    daKey = []
    daVal = []
    aliveE = []
    deadE = []
    aliveX = []
    deadX = []
    aliveY = []
    deadY = []
    for key, val in data.items():
        daKey.append(key)
        daVal.append(val)
    for x in range(0, len(daKey), 1):
        if (xName == daKey[x][0]):
            eleX = x
    for y in range(0, len(daKey), 1):
        if (yName == daKey[y][0]):
            eleY = y
    for i in range(0, len(daVal[1]), 1):
        if (daVal[1][i] == 1):
            aliveE.append(i)
        if (daVal[1][i] == 0):
            deadE.append(i)
    for r in range(0, len(aliveE), 1):
        aliveX.append(daVal[eleX][aliveE[r]])
        aliveY.append(daVal[eleY][aliveE[r]])
    for t in range(0, len(deadE), 1):
        deadX.append(daVal[eleX][deadE[t]])
        deadY.append(daVal[eleY][deadE[t]])
    plt.scatter(aliveX, aliveY, c='green')
    plt.scatter(deadX, deadY, c='red')
    plt.title("Survival of Titanic Passengers")
    plt.xlabel(xName)
    plt.ylabel(yName)
    plt.savefig(f'scatter-{xName}-{yName}.png')
    #plt.scatter(daVal[eleX], daVal[eleY])
    #plt.show()
# ------ You shouldn't have to modify main --------


def main():
    """Main program driver for Project 7."""

    # 7.1 Load the dataset
    TITANIC_TYPES = {'PassengerId': int, 'Survived': int, 'Pclass': int,
                     'Sex': str, 'Age': float, 'SibSp': int, 'Parch': int,
                     'Fare': float, 'Embarked': str, 'FamilySize': int,
                     'age_group': str}
    data = load_data('Titanic-clean.csv', TITANIC_TYPES)



    # 7.4 Visualize results
    fig = survivor_vis(data, ('Age', float), ('Fare', float))
    fig = survivor_vis(data, ('Age', float), ('Pclass', int))
    fig = survivor_vis(data, ('Age', float), ('Parch', int))


if __name__ == "__main__":
    main()
