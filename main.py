import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import json
 


def read():
    # Opening JSON file
    f = open('data.json')
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    for i in data['emp_details']:
        print(i)
    
    # Closing file
    f.close()

def run():
    print("Hola! ¿Que quieres saber? (1,2,3,4)")
    print("1. Top 10 tweets con mas retweet.")
    print("2. Top 10 usuarios en función a la cantidad de tweets que emitieron.")
    print("3. Top 10 días donde hay más tweets.")
    print("4. Top 10 hashtags más usados.")


def main():
    run()

if __name__ == "__main__":
    main()