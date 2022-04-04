import pandas as pd
import json
import csv

from operator import itemgetter


def read_json():
    print("Procesando informacion. Paciencia :) ")
    # Opening JSON file
    f = open('data.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Closing file
    f.close()

    return data


def make_json():
    print('Lectura inicial de datos. Puede que tarde un poco.')
    # Function to convert a CSV to JSON
    # Takes the file paths as arguments
    csvFilePath = r'data.csv'
    jsonFilePath = r'data.json'

    # create a dictionary
    data = []

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

            number_followers = int(rows["user_followers"])
            number_friends = int(rows["user_friends"])
            number_favourites = int(rows["user_favourites"])

            rows["user_followers"] = number_followers
            rows["user_friends"] = number_friends
            rows["user_favourites"] = number_favourites

            data.append(rows)
            key += 1

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


def handle_user_input(input):

    data = read_json()

    if input == 1:
        most_followers(data)

    if input == 2:
        most_friends(data)

    if input == 3:
        most_favorites(data)


def most_followers(data):
    print("\n El top 10 de tweets con mas followers es:")

    users = sorted(data, key=itemgetter('user_followers'), reverse=True)[:10]
    counter = 1
    for user in users:
        name = user['user_name']
        number = user['user_followers']
        tweet = user['text']

        print(f'{counter}. USER: {name} \n  TWEET: {tweet} \n  TOTAL FOLLOWERS: {number}')
        print('________')
        counter += 1


def most_friends(data):
    print("\n El top 10 de usuarios con mas tweets es:")


def most_favorites(data):
    print("\n El top 10 de dias con mas tweets:")


def main_menu():
    print("-----------------------------------------")
    print("Hola! ¿Que quieres saber? (1,2,3)")
    print("1. Top 10 de tweets con mas followers.")
    print("2. Top 10 users con mas amigos.")
    print("3. Top 10 users con mas cantidad de cuentas favoritas.")
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
