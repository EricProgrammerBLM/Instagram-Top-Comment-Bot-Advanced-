import os
from Google import Create_Service

#Code to connect to Google Cloud API
#FOLDER_PATH = (r"C:\Users\John Doe\Desktop\Google") // All doctuments in the same path
CLIENT_SECRET_FILE = os.path.join('client_secret.json') #deleted FOLDER_PATH from arguement because we no longer needed it
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
 
service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

sheetId = '1ussOkI20ZwdbNP-cVwDPCoV7B5xP3O5PiYvk7R8uRtE' #Google Sheets ID - Found in the Google Sheets Link; Also can't be from an Uploaded Document
#                                                                                                             Create new excel sheet then extract the id code

test = []

def ConnectToAPI(ColLetter, thelist):
	response = service.spreadsheets().values().get(
		spreadsheetId=sheetId, 
		majorDimension='COLUMNS', 
		range='Sheet1!'+ColLetter+'2:'+ColLetter+'40'
		).execute()
	#print (response)
	comments = response['values'][0] #Pull the values from the Google Sheets dictionary thats responded back to you
	for cell in comments:
		thelist.append(cell)
	
