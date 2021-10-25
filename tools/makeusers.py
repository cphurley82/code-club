# -*- coding: utf-8 -*-
"""Generates a csv file with usenames and passowrds for a Scratch classroom."""
import csv
import random

states_and_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}


def get_random_color():
    """Generates a random color."""
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    import random
    return random.choice(colors)


def fixup_name(name):
    """Fixes up the name."""
    name = name.replace(' ', '-')
    return name.lower()


def main():
    """ Generates a csv file with usenames and passowrds."""

    rows = []
    for state, capital in states_and_capitals.items():
        username = get_random_color() + '-' + fixup_name(state)
        password = fixup_name(states_and_capitals[state]) + str(
            random.randint(10, 99))
        rows.append([username, password])
    rows.sort(key=lambda s: len(s[0]) + len(s[1]))

    with open('student-upload.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        for row in rows:
            csvwriter.writerow(row)


if __name__ == '__main__':
    main()
