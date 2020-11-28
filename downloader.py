import threading
import urllib.request
import schedule
import time
import ssl
import os

def first_run():
    check_file = os.path.exists('сovid_data1.csv')
    if check_file == True:
        print('covid_data1 exist')
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'covid_data1.csv')
        os.remove(path)
    else: 
        print('covid_data1 doesnt exist')
    print('Beginning file download')
    url = 'https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.csv'
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib.request.urlretrieve(url, 'covid_data1.csv')
    print('downloaded covid_data1')
    check_file = os.path.exists('covid_data.csv')
    if check_file == True:
        print('covid_data exist, I will delete it')
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'covid_data.csv')
        os.remove(path)
    else: 
        print('covid_data doesnt exist')
    print('I will rename')
    os.rename('covid_data1.csv', 'covid_data.csv')
    print('cool')


def update():
    def downloading():
        check_file = os.path.exists('сovid_data1.csv')
        if check_file == True:
            print('covid_data1 exist')
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'covid_data1.csv')
            os.remove(path)
        else: 
            print('covid_data1 doesnt exist')
        print('Beginning file download')
        url = 'https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.csv'
        ssl._create_default_https_context = ssl._create_unverified_context
        urllib.request.urlretrieve(url, 'covid_data1.csv')
        print('downloaded covid_data1')
        check_file = os.path.exists('covid_data.csv')
        if check_file == True:
            print('covid_data exist, I will delete it')
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'covid_data.csv')
            os.remove(path)
        else: 
            print('covid_data doesnt exist')
        print('I will rename')
        os.rename('covid_data1.csv', 'covid_data.csv')
        print('cool')



    schedule.every().day.at("08:00").do(downloading)
    schedule.every().day.at("09:00").do(downloading)
    schedule.every().day.at("10:00").do(downloading)
    schedule.every().day.at("11:00").do(downloading)
    schedule.every().day.at("12:00").do(downloading)
    schedule.every().day.at("13:00").do(downloading)
    schedule.every().day.at("14:00").do(downloading)
    schedule.every().day.at("15:00").do(downloading)
    schedule.every().day.at("16:00").do(downloading)
    schedule.every().day.at("17:00").do(downloading)
    schedule.every().day.at("18:00").do(downloading)
    schedule.every().day.at("19:00").do(downloading)
    schedule.every().day.at("20:00").do(downloading)
    schedule.every().day.at("21:00").do(downloading)
    schedule.every().day.at("22:00").do(downloading)
    schedule.every().day.at("23:00").do(downloading)
    schedule.every().day.at("00:00").do(downloading)


    while True:
        schedule.run_pending()
        time.sleep(1)
