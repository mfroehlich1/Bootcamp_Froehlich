import datetime
import matplotlib.pyplot as plt

with open('rain.txt') as f:

    rows = f.readlines()

    line_count = 0
    for row in rows:
        line_count += 1
        if set(row.strip()) == set('-'):
            break

    file_list = []
    for row in rows[line_count:]:
        col_list = ['Date', 'Daily Total']
        row_list = row.split()[:2]
        date = datetime.datetime.strptime(row_list[0], '%d-%b-%Y')
        row_list[0] = date
        if row_list[1].isdigit():
            row_list[1] = int(row_list[1])
        row_dict = dict(zip(col_list, row_list))
        file_list.append(row_dict)

    highest_rain = 0
    annual_rain = {}
    for row in file_list:
        row_rain = row['Daily Total']
        annual_rain[(row['Date']).year] = 0
        try:
            if row['Daily Total'] > highest_rain:
                row_rain = row['Daily Total']
                highest_rain = row['Daily Total']
                highest_rain_date = row['Date']
        except TypeError:
            row['Daily Total'] = 0
            continue
    date_list = []
    inch_list = []
    for row in file_list:
        row_rain = row['Daily Total']
        date_list.append(row['Date'])
        inch_list.append(row['Daily Total'] * .01)
        try:
            annual_rain[(row['Date']).year] += (row_rain * .01)
        except TypeError:
            continue

    plt.plot(date_list, inch_list)
    plt.show()
