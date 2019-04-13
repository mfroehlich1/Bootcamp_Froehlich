import datetime

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
            continue
    for row in file_list:
        row_rain = row['Daily Total']
        try:
            annual_rain[(row['Date']).year] += (row_rain * .01)
        except TypeError:
            continue

    most_rain = 0
    for year, rain_inches in annual_rain.items():
        if rain_inches > most_rain:
            highest_year = year
            most_rain = rain_inches

    inches = highest_rain * 0.01

    print(f'\nThe highest rainfall date was {highest_rain_date.month}\\{highest_rain_date.day}\\{highest_rain_date.year} with {inches} inches of rainfall.\n')
    print(f'{highest_year} had the most rain with {most_rain} inches of rain total\n')
