from __future__ import print_function
import pickle
import os.path
# from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import csv, io
from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse
from django.contrib import messages
from .models import FormData, DataSchema
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
import os
from PIL import Image


# Create your views here.
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1buqR2OkUJdPA63NYh2WZWRoCQ4-P_8JP-7vogko3oYA'
SAMPLE_RANGE_NAME = 'A3:F'
SAMPLE_RANGE_GREG = 'G3:L'
SAMPLE_RANGE_KEVIN = 'M3:R'
SAMPLE_RANGE_MATT = 'S3:X'
SAMPLE_RANGE_ORG = 'Y3:AD'
SAMPLE_RANGE_ECLIENTS = 'AE3:AF'


def index(request):
    return render(request)


def create(request):
    if request.method == "POST":
        corpus = []
        input_text = request.POST['search']

        response1 = "30% progress is done by the manufacturing team in this project. You can go to the link for the AR tutorial.  "
        response2 = "Its a docking system which is very useful for hold"
        response3 = "Protect data stored and shared in public cloud storage. Yet, as convenient as they are, public cloud storage serviceshave also introduced a huge data security gap. As soonas users save files in a public cloud, IT immediately—andirretrievably—loses control over data security. From thatpoint forward, users can share that data with whomeverthey want, whenever they want. In these all too common scenarios, data securitysuddenly relies on the tenuous hope that data will remainprotected. When combined with Mobile Edition, the solutions helpkeep data protected when it is accessed on Androidand iOS smartphones and tablets, both personally andcompany owned. Together, they enable end users towork when, where, and how they want while IT remains incontrol of data and compliance. CloudEdition provides an additional encryption key, stored on yournetwork and owned by you, so data is guarded even fromthe storage provider itself."
        response4 = "To be more specific, we look for keys with a crisp action that quickly rebound when a finger is removed. Alternatives are acceptable if their quality holds up. Multi-touch gestures should be included, and we look for them to operate without a jerky or uncertain feel. Using the laptop naturally reveals the quality of the display, but there are also tests used to provide a measurable impression. Audio quality is judged by a number of subjective tests. A typical benchmark includes YouTube HD, podcasts, and streaming music. Peacekeeper, a web browser benchmark, is our most demanding test. We test systems using Chrome. Next up, we have our iMacro test. A pause between each load provides downtime. This tends to be the least demanding test in our suite. We also run these tests on MacOS systems, but we use Mac default applications (like Safari). With ChromeOS, we only conduct the Peacekeeper and iMacro tests. The results are often referenced in our reviews. We also measure fan noise during our temperature tests. Noise is measured during idle, at full CPU load, and at full GPU load. Competition must also be considered. Even if you don’t agree with our final verdict, the information."
    # --------------------------------------------------
        if input_text == 'quit' or input_text == 'Quit':
            exit()
        else:
            title = re.sub('[^a-zA-Z]', ' ', input_text)
            title = title.lower()
            title = title.split()
            ps = PorterStemmer()
            title = [ps.stem(word) for word in title if not word in set(stopwords.words('english'))]
            title = ' '.join(title)
            corpus.append(title)

        if title.find(' progress monitor stand') != -1 or title.find('monitor stand') != -1 or title.find(
                ' status monitor stand') != -1:
            print("30% progress is done by the manufacturing team in this project. You can go to the link_"
                  "for the AR tutorial.  ")
            return TemplateResponse(request, 'home.html', {'data1': response1})

        elif title.find(' dell dock system') != -1 or title.find('dock system') != -1:
            print("Its a docking system which is very useful for hold")
            return TemplateResponse(request, 'home.html', {'data2': response2})

        elif title.find(' cloud storage') != -1 or title.find('cloud') != -1:
            print("Its a docking system which is very useful for hold")
            return TemplateResponse(request, 'home.html', {'data2': response3})

        elif title.find('Alienware') != -1 or title.find('game laptop') != -1:
            # print(
                # "The latest version of alienware is Dell Alienware 17 Area 51 9thGeneration Corei9-9900K,32GB RAM,1TB+512GB SSD,8GB RTX 2080 Graphics 17.3  FHD Display Gaming Laptop")

            return TemplateResponse(request, 'home.html', {'data3': response4})
            # --------------------------------------------------



        value_text = request.POST['prodId']
        all_data = DataSchema.objects.filter(company_name__icontains=input_text).values('company_name', 'company_url', 'company_email', 'f_name', 'l_name', 'city_name')
        if all_data:
            return TemplateResponse(request, 'home.html', {'data': all_data})
        else:
            return TemplateResponse(request, 'home.html', {'data_value': value_text})


def savedata(request):
    if request.method == "POST":

        form_data_obj = FormData()
        dataschema_obj = DataSchema()

        datafield1 = request.POST['data1']
        datafield2 = request.POST['data2']
        datafield3 = request.POST['data3']
        datafield4 = request.POST['data4']
        datafield5 = request.POST['data5']
        datafield6 = request.POST['data6']
        datafield7 = request.POST['data7']
        datafield8 = request.POST['data8']
        datafield9 = request.POST['data9']
        datafield10 = request.POST['data10']
        datafield11 = request.POST['data11']
        datafield12 = request.POST['data12']
        datafield13 = request.POST['data13']
        datafield14 = request.POST['data14']
        datafield15 = request.POST['data15']
        datafield16 = request.POST['data16']

        # Form info save to users_formdata DB

        form_data_obj.lead_gen = datafield1
        form_data_obj.company_name = datafield2
        form_data_obj.company_address = datafield3
        form_data_obj.company_city = datafield4
        form_data_obj.company_state = datafield5
        form_data_obj.company_country = datafield6
        form_data_obj.company_url = datafield7
        form_data_obj.company_linkedin = datafield8
        form_data_obj.company_phone = datafield9
        form_data_obj.company_email = datafield10
        form_data_obj.f_name = datafield11
        form_data_obj.l_name = datafield12
        form_data_obj.owner_linkedin = datafield13
        form_data_obj.owner_title = datafield14

        # Form info save to users_formdata DB
        dataschema_obj.company_name = datafield2
        dataschema_obj.company_url = datafield7
        dataschema_obj.company_email = datafield10
        dataschema_obj.f_name = datafield11
        dataschema_obj.l_name = datafield12
        dataschema_obj.city_name = datafield4


        form_data_obj.save()
        dataschema_obj.save()
        messages.success(request, 'Form submitted successfully')

        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

        client = gspread.authorize(creds)

        sheet = client.open("info")
        worksheet = sheet.worksheet('ashwin')

        data = worksheet.get_all_records()

        # numRows = sheet.row_count
        data_len = len(data)


        insertRow = [datafield1, datafield2, datafield4]
        worksheet.insert_row(insertRow, data_len + 2)

        # pprint(data)
        # print(numRows)
        print(len(data))



        return TemplateResponse(request, 'home.html')


def main(request):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()

    # for greg
    result2 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_GREG).execute()

    # for kevin
    result3 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_KEVIN).execute()

    # for matt
    result4 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range=SAMPLE_RANGE_MATT).execute()

    # for organizations
    result5 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range=SAMPLE_RANGE_ORG).execute()

    # for existing clients
    result6 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range=SAMPLE_RANGE_ECLIENTS).execute()

    values = result.get('values', [])
    values_greg = result2.get('values', [])
    values_kevin = result3.get('values', [])
    values_matt = result4.get('values', [])
    values_org = result5.get('values', [])
    values_eclients = result6.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Fetching Data of GABE from DB')

        for row in values:
            sheetdata_obj = DataSchema()
            try:
                if row:
                    sheetdata_obj.company_name = row[0]
                    sheetdata_obj.company_url = row[1]
                    sheetdata_obj.company_email = row[2]
                    sheetdata_obj.f_name = row[3]
                    sheetdata_obj.l_name = row[4]
                    sheetdata_obj.city_name = row[5]
            except IndexError:
                pass

            sheetdata_obj.save()

    if not values_kevin:
        print('No data found.')
    else:
        print('Fetching Data of GREG from DB')

        for row in values_kevin:
            sheetdata_obj = DataSchema()
            try:
                if row:
                    sheetdata_obj.company_name = row[0]
                    sheetdata_obj.company_url = row[1]
                    sheetdata_obj.company_email = row[2]
                    sheetdata_obj.f_name = row[3]
                    sheetdata_obj.l_name = row[4]
                    sheetdata_obj.city_name = row[5]
            except IndexError:
                pass

            sheetdata_obj.save()

    if not values_greg:
        print('No data found.')
    else:
        print('Fetching Data of KEVIN from DB')

        for row in values_greg:
            sheetdata_obj = DataSchema()
            try:
                if row:
                    sheetdata_obj.company_name = row[0]
                    sheetdata_obj.company_url = row[1]
                    sheetdata_obj.company_email = row[2]
                    sheetdata_obj.f_name = row[3]
                    sheetdata_obj.l_name = row[4]
                    sheetdata_obj.city_name = row[5]
            except IndexError:
                pass

            sheetdata_obj.save()

    if not values_matt:
        print('No data found.')
    else:
        print('Fetching Data of MATT from DB')

        for row in values_matt:
            sheetdata_obj = DataSchema()
            try:
                if row:
                    sheetdata_obj.company_name = row[0]
                    sheetdata_obj.company_url = row[1]
                    sheetdata_obj.company_email = row[2]
                    sheetdata_obj.f_name = row[3]
                    sheetdata_obj.l_name = row[4]
                    sheetdata_obj.city_name = row[5]
            except IndexError:
                pass

            sheetdata_obj.save()

    if not values_org:
        print('No data found.')
    else:
        print('Fetching Data of ORGANIZATIONS from DB')

        for row in values_org:
            sheetdata_obj = DataSchema()
            try:
                if row:
                    sheetdata_obj.company_name = row[0]
                    sheetdata_obj.company_url = row[1]
                    sheetdata_obj.company_email = row[2]
                    sheetdata_obj.f_name = row[3]
                    sheetdata_obj.l_name = row[4]
                    sheetdata_obj.city_name = row[5]
            except IndexError:
                pass

            sheetdata_obj.save()

    if not values_eclients:
        print('No data found.')
    else:
        print('Fetching Data of EXISTING CLIENTS from DB')

        for row in values_eclients:
            sheetdata_obj = DataSchema()
            try:
                if row:
                    sheetdata_obj.company_name = row[0]
                    sheetdata_obj.company_email = row[1]
            except IndexError:
                pass

            sheetdata_obj.save()

    return TemplateResponse(request, 'home.html', {'info': values_greg})


def update_sheet(request):

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()

    num_rows = len(result)
    print(num_rows)

    allData = DataSchema.objects.all()


    for company in allData:
        googlesheet = []
        googlesheet = company.company_name
        googlesheet = company.company_name
        googlesheet = company.company_name
        googlesheet = company.company_name

        print(googlesheet)

    return HttpResponse("hello cow")


def contact_upload(request):
    template = "contact_upload.html"

    prompt = {
        'order': 'Order of CSV should be company_name, company_url, company_email, f_name, l_name, city_name'
    }

    if request.method == "GET":
        return render(request, template, prompt)
    # empty_lines = 0

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        if not column:
            continue
        else:

            _, created = DataSchema.objects.update_or_create(
                company_name = column[0],
                company_url = column[1],
                company_email = column[2],
                f_name = column[3],
                l_name = column[4],
                city_name = column[5]
            )

    messages.success(request, 'File Uploaded')
    context = {}

    return render(request, template, context)






