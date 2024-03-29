#!/usr/bin/env python
import datetime
import pathlib
import os
from os import path
from new_request import new_request_row
from track_requests import track_requests
import sqlite3


# might want to add custom columns like contact at agency, state of agency like CA, OR, etc]


def determine_track(cursor):
    """ Determine whether to create a new request or track existing requests """
    action = str(input("What would you like to do?\nEnter 1 to get today's requests to follow up on\n Enter 2 to add a new request\n"))
    if action == '1':
        track_requests(cursor)
    if action == '2':
        print('true')
        print("Entering add new request mode... \n")
        new_row = new_request_row()
        cursor.execute("insert into requests (requesttitle, agency, date_requested, tracking_num, followup_interval, required_response_time, days_to_followup, request_description) values (?, ?, ?, ?, ?, ?, ?, ?)", new_row)


if __name__ == '__main__':
    connection = sqlite3.connect("foiatrack.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS requests (requesttitle TEXT, agency TEXT, date_requested TEXT, tracking_num TEXT, followup_interval INTEGER, required_response_time INTEGER, days_to_followup INTEGER, request_description TEXT)")
    determine_track(cursor)