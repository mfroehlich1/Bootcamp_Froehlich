import datetime


with open('crime_incident_data_2014.csv') as f:

	rows = f.readlines()

	col_list = []
	csv_list = []
	for row in rows:
		if not col_list:
			col_list = row.split(',')
			continue
		row_list = row.split(',')
		date = datetime.datetime.strptime(row_list[1], '"%m/%d/%Y"')
		row_list[1] = date
		row_dict = dict(zip(col_list, row_list))
		csv_list.append(row_dict)

	offense_dict = {}
	for row in csv_list:
		offense = {row['"Major Offense Type"']: 0}
		offense_dict.update(offense)

	for row in csv_list:
		offense_dict[row['"Major Offense Type"']] += 1

	most_common_crime = ''
	crime_count = 0
	for k, v in offense_dict.items():
		if v > crime_count:
			most_common_crime = k
			crime_count = v

	least_common_crime = ''
	least_crime_count = crime_count
	for k, v in offense_dict.items():
		if v < crime_count:
			least_common_crime = k
			least_crime_count = v

	year_dict = {}
	for row in csv_list:
		crime_year = {row['"Report Date"'].year: 0}
		year_dict.update(crime_year)

	for row in csv_list:
		year_dict[row['"Report Date"'].year] += 1

	most_crime_year = ''
	most_crime_year_count = 0
	for k, v in year_dict.items():
		if v > most_crime_year_count:
			most_crime_year = k
			most_crime_year_count = v

	print(f'\nMost common crime: {most_common_crime}\nCount: {crime_count}\n')
	print(f'Least common crime: {least_common_crime}\nCount: {least_crime_count}\n')
	print(f'Year with most crime: {most_crime_year}\nCount: {most_crime_year_count}')
