import threading
import pandas
import urllib.request
import schedule
import time
import ssl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt
from scipy.optimize import curve_fit
import matplotlib.ticker as ticker
 
 
# print('Вводи по английский с большой буквы')
# country = input()
def plot(country):
    date_interval = 5
    
    
    #считываем данные
    data = pandas.read_csv('covid_data.csv')
    data.head()
    
    data['date'] = pandas.to_datetime(data['date'])
    data['date']
    
    #преобразуем даты к божескому виду
    
    
    # для поиска нужной страны в списке
    def get_coordinates(country):
        amount = 0
        for i in range(len(data)):
            if data.iloc[i,1] == country:
                amount += 1
                if amount == 1:
                    start = i
                end = start + amount
            else:
                pass
        return [start, end, amount]
    
    
    # Получили координаты страны : индекс начала, индекс конца и длинна этого списка
    coordinates = get_coordinates(country)
    coordinates
    start = coordinates[0]
    end = coordinates[1]
    amount = coordinates[2]
    
    
    # функция апроксимации
    def f(x, a, b, c):
        return np.exp(a*x + b) + c
    
    
    # Определили списки количества зараженных
    Infected = np.array(data['total_cases'].iloc[start:end])
    days = np.arange(1,amount+1)
    
    
    # Отсеиваем хламную информацию, будем строить минимум от 100 заболевших
    def find_new_start(Infected):
        Infected_2 = []
        n = 0
        for i in range(len(Infected)):
            if Infected[i] > 100:
                n += 1
                if n == 1:
                    start_new = i
                Infected_2.append(Infected[i])
        Infected_2 = np.array(Infected_2)
        return (Infected_2, start_new)
    
    
    
    start_new = find_new_start(Infected)[1]
    Infected_2 = find_new_start(Infected)[0]
    days1 = np.arange(1,amount-start_new+1)
    
    
#Апроксимация


#коэффициенты
    try:
        beta_opt1, beta_cov1 = curve_fit(f, days1, Infected_2)
        a = beta_opt1[0]
        b = beta_opt1[1]
        c = beta_opt1[2]

        #получим погрешности для коэффициентов
        sigma_a = np.sqrt(beta_cov1[0,0])
        sigma_b = np.sqrt(beta_cov1[1,1])
        sigma_c = np.sqrt(beta_cov1[2,2])

        residuals1 = Infected_2 - f(days1,*beta_opt1)
        fres1 = sum(residuals1**2)
        Stand_error = np.sqrt(fres1/len(days1))

        fig, ax = plt.subplots(figsize=(15, 12))

        past = min(data['date'].iloc[start+start_new:end])
        now = max(data['date'].iloc[start+start_new:end]) + dt.timedelta(days=1)
        days2 = mdates.drange(past,now,dt.timedelta(days=1))


        delta = days2[0] - 1
        beta_opt2 = np.array([a,b-delta * a,c])

        ax.plot(days2, f(days2, *beta_opt2), 'coral', lw=2)

        lgnd = ax.legend(['~(˘▾˘~) Аппроксимация экспонентой дает ошибку $\pm$ %d людей' % Stand_error ], loc='upper left', shadow=True)

        ax.set_title('Infected in %s (date)      from %s to %s' % (country, min(data['date'].iloc[start+start_new:end]).strftime("%d.%m"), max(data['date'].iloc[start+start_new:end]).strftime("%d.%m")))
        ax.set_ylabel('Infected')
        ax.set_xlabel('Date (day.month)')

        ax.grid(which='major',
        color = 'k')

        ax.minorticks_on()

        ax.grid(which='minor',
        color = 'gray',
        linestyle = ':', linewidth = 0.5)

        ax.grid(which='major', linewidth = 0.5)


        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=date_interval))
        plt.errorbar(days2, Infected_2, fmt = 'ro', markersize = '2', yerr = Stand_error, capsize = 2, elinewidth = 2, capthick = 1, ecolor = 'violet')

        plt.gcf().autofmt_xdate()
        plt.savefig('%splot.png' % country, dpi=400, quality=100)
        plt.show()

    except RuntimeError:

        fig, ax = plt.subplots(figsize=(15, 12))

        past = min(data['date'].iloc[start+start_new:end])
        now = max(data['date'].iloc[start+start_new:end]) + dt.timedelta(days=1)
        days2 = mdates.drange(past,now,dt.timedelta(days=1))


        delta = days2[0] - 1

        ax.set_title('Infected in %s (date)      from %s to %s' % (country, min(data['date'].iloc[start+start_new:end]).strftime("%d.%m"), max(data['date'].iloc[start+start_new:end]).strftime("%d.%m")))
        ax.set_ylabel('Infected')
        ax.set_xlabel('Date (day.month)')

        ax.grid(which='major',
                color = 'k')

        ax.minorticks_on()

        ax.grid(which='minor',
                color = 'gray',
                linestyle = ':', linewidth = 0.5)

        ax.grid(which='major', linewidth = 0.5)


        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=date_interval))
        plt.errorbar(days2, Infected_2, fmt = 'ro', markersize = '2', yerr = 0, capsize = 2, elinewidth = 2, capthick = 1, ecolor = 'violet')
        ax.plot(days2, Infected_2, 'coral', lw=2)
        plt.gcf().autofmt_xdate()
        plt.savefig('%splot.png' % country, dpi=400, quality=100)
        plt.show()

 