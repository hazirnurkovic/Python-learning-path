#declare empty list with name empty_list
empty_list = []

#declare list with more than 5 elements
list_5 = [1,2,3,4,5,6,7,8,9,10]

#find the length of list
print(len(list_5))

#get the first item, the middle item and the last item of the list
print(list_5[0])
print(list_5[4])
print(list_5[-1])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Hazir', 25, 184, 'Married', 'Podgorica, Montenegro']

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#print the list using print()
print(it_companies)

#print number of companies in the list
print(len(it_companies))

#print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

#Print the list after modifying one of the companies
it_companies[0] = 'Instagram'
print(it_companies)

#Add an IT company to it_companies
it_companies.append('Twitter')

#Change one of the it_companies names to uppercase (IBM excluded!)
for i in range(len(it_companies)):
    if it_companies[i] != 'IBM' :
        it_companies[i] = it_companies[i].upper()
print(it_companies)

#Join the it_companies with a string '#;  '
joined_it_companies = '#; '.join(it_companies)
print(joined_it_companies)

#Check if a certain company exists in the it_companies list
print('Facebook' in it_companies)

#Sort the list using sort() method
it_companies.sort()
print(it_companies)

#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#Slice out the first 3 companies from the list
first_3_companies = it_companies[:3]
print(first_3_companies)

#Slice out the last 3 companies from the list
last_3_companies = it_companies[-3:]
print(last_3_companies)

#Slice out the middle IT company or companies from the list
middle_company = it_companies[len(it_companies)//2]
print(middle_company)

#Remove the first IT company from the list
    #it_companies.pop(0)
    #it_companies.remove(it_companies[0])
    #del it_companies[0]
it_companies = it_companies[1:]
print(it_companies)

#Remove the middle IT company or companies from the list
    #it_companies.pop(len(it_companies)//2)
    #it_companies.remove(it_companies[len(it_companies)//2])
    #del it_companies[len(it_companies)//2]
it_companies.pop(len(it_companies)//2)
print(it_companies)

#Remove the last IT company from the list
    #it_companies.pop(-1)
    #it_companies.remove(it_companies[-1])
    #del it_companies[-1]
it_companies = it_companies[:-1]
print(it_companies)

#Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#Destroy the it_companies list
del it_companies
#print(it_companies)

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
    #joined_list = front_end + back_end
    #front_end.extend(back_end)
    #back_end.extend(front_end)
joined_list = front_end + back_end
print(front_end + back_end)

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = joined_list.copy()
full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack.insert(full_stack.index('Python')+1, 'SQL')
print(full_stack)

#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages.sort()
min = ages[0]
max = ages[-1]
print(min)
print(max)

#Add the min age and the max age again to the list
ages.append(min)
ages.append(max)
print(ages)

#Find the median age (one middle item or two middle items divided by two)
median = ages[len(ages)//2]
print(median)

#Find the average age (sum of all items divided by their number )
sum = sum(ages)
average = sum/len(ages)
print(average)

#Find the range of the ages (max minus min)
range = max - min
print(range)

#Compare the value of (min - average) and (max - average), use abs() method
print(abs(min - average))
print(abs(max - average))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

#Find the middle country(ies) in the country list
if(len(countries) % 2 == 0):
    middle_country = countries[len(countries)//2-1:len(countries)//2+1]
else:
    middle_country = countries[len(countries)//2]

print(middle_country)

#  Divide the countries list into two equal lists if it is even if not one more country for the first half.
if(len(countries) % 2 == 0):
    first_half = countries[:len(countries)//2]
    second_half = countries[len(countries)//2:]
else:
    first_half = countries[:len(countries)//2+1]
    second_half = countries[len(countries)//2+1:]

print(first_half)
print(second_half)

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
first_country, second_country, third_country, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(scandic_countries)