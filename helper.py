import pandas as pd
import random
from datetime import date, timedelta

today = date.today()

def make_new():
    df = pd.DataFrame({'date': [today],
                        'weight': [None]})
    return df

def get_csv(file):
    df = pd.read_csv(file,  sep=';')
    return df

def sample_weight_sim(weight, minweight, maxweight):
    weight_increment = 2.0
    weight_change = round(random.uniform(-weight_increment, weight_increment), 2)
    if weight > maxweight:
        weight = weight - abs(weight_change)
    elif weight < minweight:
        weight = weight + abs(weight_change)
    else:
        weight = weight + weight_change
    return weight


def sample_weight(minweight, maxweight, age):
    weight = round(random.uniform(minweight, maxweight), 2)
    day = date.today() + timedelta(days = -age)
    df = pd.DataFrame({'date' : [day] , 'weight': weight})
    r = 0
    while day != date.today():
        day = day + timedelta(days = + 1)
        weight = sample_weight_sim(df.iloc[r,1], minweight, maxweight)
        #df.append([day,weight])
        curr_row = pd.DataFrame({'date' : [day] , 'weight': weight})
        df = pd.concat([df, curr_row])
        r += 1
    return df