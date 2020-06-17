def new_request_row():
    """ Get all user input necessary for a new request, make a dictionary of that user input, and append a new row to tracking spreadsheet """
    new_request_dict = {
        'agency': get_agency(),
        'date_requested': get_date_requested(),
        'tracking_num': get_tracking_num(),
        'followup_interval': get_followup_interval(),
        'required_response_time': get_required_response_time(),
        'request_description': get_request_subject()
    }
    return new_request_dict


def get_agency():
    """ Get the name of the agency for the relevant request and save it """
    # TODO: confirm the agency
    agency = str(input("To which agency did you make your request? \n"))
    #confirm_agency = str(input("You entered %s, enter space to confirm or any other key to start over " % agency))
    #while confirm_agency != ' ':
    #    get_agency()
    #print("Confirmed: " + agency)
    return agency


def get_required_response_time():
    """ Get the number of days in which the agency must respond to the request """
    while True:
        try:
            response_time = int(input("Please enter the number of days (i.e. '5' or '20' ) in which the agency must initially respond to requests: "))
        except ValueError:
            print("Please enter the number of days as integer (i.e. '5' instead of 'five'")
            continue
        else:
            # days parsed successfully
            break
    return response_time


def get_date_requested():
    """ Get the year, month, and day of initial request """
    while True:
        try:
            year = int(input("In what year did you make the initial request? "))
            month  = int(input("In what month did you make the initual request (as two numbers, i.e. 05 for May)? "))
            day = int(input("What day did you make the initial request (as two numbers, i.e. 23 for the 23rd)? "))
        except ValueError:
            print("Enter as an integer (i.e. 2020, or 05)")
            continue
        else:
            break
    return str(year) + '-' + str(month) + '-' + str(day)


def get_followup_interval():
    """ Get the interval for how often to prompt user to follow up """
    while True:
        try:
            followup_days = int(input("How often would you like to follow up with this agency, in days? (i.e. enter 14 for 2 weeks "))
        except ValueError:
            print("Did you enter the interval in days as an integer?")
            continue
        else:
            break
    return followup_days


def get_request_subject():
    """ Get a short description from user about the request """
    description = str(input("Enter a short description or summary of this request, i.e. police officer roster, or N95 mask purchase orders \n"))
    return description
    

def get_tracking_num():
    """ Get a tracking number for the user, if applicable (entry is optional) """ 
    answer = str(input("Would you like to enter a tracking number? Type y for yes, or n for no \n"))
    if answer.lower() == 'n':
        # we don't need to do anything
        return None
    if answer.lower != 'n' or 'y':
        print("Enter y or n")
        get_tracking_num()
    if answer == 'y':
        tracking_num = str(input("Enter tracking number, i.e. P50728 \n"))
        return tracking_num