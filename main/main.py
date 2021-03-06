import datetime as datetime
import pandas as pd
import pathlib
from os import path
from new_request import new_request_row


# every day, run this script and read in csv, and if it has been one week since
# last check in

tracker_sheet_file = pathlib.Path("tracker-sheet/foia_track_sheet.csv")

initial_column_names = ['agency', 'date_requested', 'tracking_num', 'request_subject', 'followup_interval', 'required_response_time']
# might want to add custom columns like contact at agency, state of agency like CA, OR, etc]

def setup():
    # if tracker-sheet directory is empty, makes new dataframe to use
    # TODO: if directory contains any kind of existing csv or excel, read that in - let people using existing foia sheets
    if not tracker_sheet_file.exists():
    #if not str(path.isfile('../tracker-sheet/foia_track_sheet.csv')):
        print("It looks like you don't have a tracker spreadsheet yet. Setting up...")
        tracker = pd.DataFrame(columns = initial_column_names)
    if tracker_sheet_file.exists():
        print("It looks like you aready have a tracker spreadsheet. Reading it in...")
        tracker = pd.read_csv('tracker-sheet/foia_track_sheet.csv')
    return tracker


if __name__ == '__main__':
    tracker = setup()
    print("Entering add new request mode... \n")
    new_row = new_request_row()
    tracker = tracker.append(new_row, ignore_index=True)
    print(tracker)
    tracker.to_csv('tracker-sheet/foia_track_sheet.csv', index=False)