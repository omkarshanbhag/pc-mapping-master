import pandas as pd

df = pd.read_csv(r'/Users/omkarshanbhag/Desktop/Pierce_final.csv', encoding = 'latin-1')
df_1 = pd.read_csv(r'/Users/omkarshanbhag/Desktop/iso_3166_2_countries.csv', encoding = 'latin-1')


country_list_prelim = df['Country'].tolist()
chicken = df['Occupation'].tolist()
other_chicken = df['Geolocation'].tolist()
other_chicken = df['Author'].tolist()

country_list = []

for country in country_list_prelim:
    if country == 'Australien':
        country_list.append('Australia')
    else:
        country_list.append(country)

country_comp = df_1['Common Name'].tolist()
letter_code = df_1['ISO 3166-1 2 Letter Code'].tolist()

final_code_list = []
index_list = []

y = 0
for country in country_list:
    x = 0
    for c in country_comp:
        if c == country:
            final_code_list.append(letter_code[x])
            index_list.append(y)
        x += 1
    y += 1

while len(final_code_list) < len(chicken):
    final_code_list.append(0)

ne = pd.Series(final_code_list)
df['Country Code'] = ne.values

df.to_csv('Final_input.csv')
