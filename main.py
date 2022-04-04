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

def handle_user_input(input):

    if input == 1:
        most_retweeted()
    
    if input == 2:
        users()
    
    if input == 3:
        days()
    
    if input == 4:
        hashtags()

def most_retweeted():
    print("\n El top 10 de tweets con mas retweet es:")
    
def users():
    print("\n El top 10 de usuarios con mas tweets es:")

def days():
    print("\n El top 10 de dias con mas tweets:")
    
def hashtags():
    print("\n El top 10 de hashtags mas usados:")

def main_menu():
    print("Hola! ¿Que quieres saber? (1,2,3,4)")
    print("1. Top 10 tweets con mas retweet.")
    print("2. Top 10 usuarios en función a la cantidad de tweets que emitieron.")
    print("3. Top 10 días donde hay más tweets.")
    print("4. Top 10 hashtags más usados.")

def run():
    main_menu()
    user_input = int(input())
    handle_user_input(user_input)

def main():
    run()

if __name__ == "__main__":
    main()