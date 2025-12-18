from openpyxl import load_workbook
from datetime import datetime

today_date = datetime.today().strftime('%d-%m-%Y')
CODE = ""
PATH = 'C:/Users/0034DK744/Documents/Development/Hospital Project/Hospital.xlsx'
IMAGE_1 = 'C:/Users/0034DK744/Documents/Development/Hospital Project/h11.png'
IMAGE_2 = 'C:/Users/0034DK744/Documents/Development/Hospital Project/t11.png'

wb = load_workbook(PATH)

local_data_list = []

get_clear_response = False


therapy_name= [
    "Hot Water Treatment",
    "Abhyangam",
    "Shiro DHara  + Oil Fees",
    "Vashpa Snan",
    "Sarvang Mitti Lep",
    "Pedu Mitti Lep",
    "Sampoorna Badan Mitti Lep",
    "Pet Garam Thanda Sek",
    "Pairon ka Garam Snan",
    "Thanda Garam Kati Snan",
    "Kidney Pack",
    "Potali Sek",
    "Jaanu Vasti + Oil Fees",
    "Kati Vasti + Oil Fees",
    "Greeva Vasti + Oil fees",
    "Jal Neti",
    "Rubber Neti",
    "Kunjal",
    "OsteoTherapy",
    "Physio Therapy",
    "Neuropathy",
    "Zero Volte Therapy",
    "Yogasan",
    "Eye Wash",
    "Chiro Practice - Full",
    "Chiro Practice - Half",
    "Homeo Quantam Test",
    "Ooni Sooti Patti"]

therapy_list_price = {
    1: 750.00,
    2: 500.00,
    3: 800.00,
    4: 200.00,
    5: 250.00,
    6: 100.00,
    7: 250,
    8: 100.00,
    9: 150.00,
    10: 250.00,
    11: 150.00,
    12: 200.00,
    13: 800.00,
    14: 800.00,
    15: 800.00,
    16: 100.00,
    17: 100.00,
    18: 100.00,
    19: 200.00,
    20: 150.00,
    21: 200.00,
    22: 100.00,
    23: 500.00,
    24: 100.00,
    25: 750.00,
    26: 350.00,
    27: 200.00,
    28: 100.00,
    }

gender = ['F', 'M', 'O']


states = [
    'Andhra Pradesh',
    'Arunachal Pradesh','Assam', 'Bihar', 'Chhattisgarh',
    'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir',
    'Jharkhand','Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra',
    'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
    'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
    'Uttarakhand', 'West Bengal', 'Andaman and Nicobar Islands', 'Chandigarh',
    'Dadra-Nagar Haveli & Daman-Diu', 'Lakshadweep', 'National Capital Territory of Delhi',
    'Puducherry', 'Ladakh'
          ]


#var = []
KEY = 0
#therapies = []

