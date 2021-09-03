# get today's requests and print/format them nicely

def track_requests(df):
    df.to_sql('requests', conn, if_exists='append', index = False)
    pass