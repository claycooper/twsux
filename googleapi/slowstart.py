#!/usr/bin/python3

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import pprint
import subprocess
import json
import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
#SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '13uqOmHFsZViGGkF13II2vbhBxrecWZ6Wy9RQxx2Tof8'
    rangeName = 'Sheet1!A:B'
    value_input_option = 'USER_ENTERED'

    """result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    """
    now = datetime.datetime.now()
    #trace = subprocess.check_output(['mtr', '--json', '-c1', '142.254.217.45'])
    trace = subprocess.check_output(['mtr', '--json', '-c10', '8.8.8.8'])
    traceStr = str(trace, 'utf-8')
    traceObj = json.loads(traceStr)
    print(traceObj['report'])
    print(now)


    #newvalues = []

    for hub in traceObj['report']['hubs']:
    #  print(' '.join([ hub['host'], str(hub['Avg']), str(hub['StDev']), str(hub['Loss%']) ]))
      newvalues = [[ now.strftime('%Y-%m-%d %H:%M:%S'), hub['host'], hub['Avg'], hub['StDev'], hub['Loss%'] ]]
      result = service.spreadsheets().values().get(
         spreadsheetId=spreadsheetId, range=rangeName).execute()

      body = { 'values': newvalues }

      writeResult = service.spreadsheets().values().append(
         spreadsheetId=spreadsheetId, range=rangeName,
         valueInputOption=value_input_option, body=body).execute()


    #newvalues = [
    #   [ 1, 2 ]
    #]


    """
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()


    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))
    """


if __name__ == '__main__':
    main()
