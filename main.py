import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import json
import csv


def read():
    print("Reading File")
    # Opening JSON file
    f = open('data.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Closing file
    f.close()

    return data


def make_json():
    # Function to convert a CSV to JSON
    # Takes the file paths as arguments
    csvFilePath = r'data.csv'
    jsonFilePath = r'data.json'

    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        key = 0
        for rows in csvReader:
            # Assuming a column named 'No' to
            # be the primary key
            # key = rows['user_name']
            data[key] = rows
            key += 1

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


def handle_user_input(input):

    data = read()

    if input == 1:
        most_retweeted(data)

    if input == 2:
        users(data)

    if input == 3:
        days(data)

    if input == 4:
        hashtags(data)


def most_retweeted(data):
    print("\n El top 10 de tweets con mas retweet es:")
    i = 0
    while i < 4:
        print(data[str(i)])
        i += 1


def users(data):
    print("\n El top 10 de usuarios con mas tweets es:")


def days(data):
    print("\n El top 10 de dias con mas tweets:")


def hashtags(data):
    print("\n El top 10 de hashtags mas usados:")


def main_menu():
    print("-----------------------------------------")
    print("Hola! ¿Que quieres saber? (1,2,3,4)")
    print("1. Top 10 tweets con mas retweet.")
    print("2. Top 10 usuarios en función a la cantidad de tweets que emitieron.")
    print("3. Top 10 días donde hay más tweets.")
    print("4. Top 10 hashtags más usados.")
    print("-----------------------------------------")


def run():
    main_menu()
    user_input = int(input())
    make_json()
    handle_user_input(user_input)


def main():
    run()


if __name__ == "__main__":
    main()
