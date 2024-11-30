from itertools import count
import math
from typing import List

def zcount(data: List[float]) -> float :
    return len(data)

def zmean(data: List[float]) -> float :
    return sum(data) / len(data)

def zmode(data: List[float]) -> float :
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1
    mode = max(frequency, key=frequency.get)
    return mode 

def zmedian(data: List[float]) -> float :
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[n // 2 -1 ] + sorted_data[n // 2]) /2

def zvariance(data: List[float]) -> float :
    mean = zmean(data)
    return sum ((x - mean) ** 2 for x in data) / (len(data) - 1)
	
def zstddev(data: List[float]) -> float :
    # sqrt of variance
    return math.sqrt(zvariance(data))

def zstderr(data: List[float]) -> float :
    return zstddev(data) / math.sqrt(len(data))

def cov(a, b):
    if len(a) != len(b):
        raise ValueError("The lists must have the same length.")
    
    mean_a = sum(a) / len(a)
    mean_b = sum(b) / len(b)
    
    return sum((x - mean_a) * (y - mean_b) for x, y in zip(a, b)) / (len(a) - 1)


def zcorr(datax: List[float], datay: List[float]) -> float :
    mean_x = zmean(datax)
    mean_y = zmean(datay)
    covariance = sum((x - mean_x) * (y - mean_y) for x,y in zip(datax, datay)) / (len(datax) - 1)
    return covariance / (zstddev(datax) * zstddev(datay))

def readDataFile(file):
    x,y = [], []
    with open(file) as f:
        first_line = f.readline() # consume headers
        for l in f:
            row = l.split(',')
            #print(row, type(row))
            x.append(float(row[0]))
            y.append(float(row[1]))
    return (x,y)

def readDataSets(files):
    data = {}
    for file in files:
        twoLists = readDataFile(file)
        data[file] = twoLists
    return data
