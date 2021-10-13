# export records webpublicatie = 'europeana' uit adlib naar csv

import pandas as pd

df = pd.read_csv("Europeana_ttt.csv", delimiter=',')
print(df)

# read kolommen
#print(df.columns)

# read 1 kolom
#print(df['production.date.start'][200:208])

# read meerdere kolommen
#df2 =  (df[["object_name", "object_number"]])
#print(df2)

# read 1 of meerdere rijen
#print(df.iloc[0:21])

# read specifieke locatie
#print(df.iloc[1:10, 9:11])

#wijzigen nam kolommen
#df = df.rename(columns={"object_number": "objectnummer", "object_name": "objectnaam"})

# delete kolom
#df3 = df.drop(['object_number', 'objectnaam'], 1)
#print(df3)

#toevoegen kolom
#df["test"] = df["object_number"] + df["institution.name"]
#print(df)

#verplaatsen kolom
#df = df[['institution.name', 'collection', 'object_number', 'object_category',

#cols = list(df.colums.values)
#print(cols)
#df = df[cols[0:3] + [cols[-1]] + cols [4:26]]
#print(df)

df = df.sort_values("object_category", ascending=False)
print(df)

#filteren op een voorwwaarde

df4 = df.sort_values(['creator', 'object_category'], ascending=[1,0])

df5 = df.loc[df['production.place'] == 'Gent']
print(df5)

#filteren op meerdre voorwaarden

df6 = df.loc[(df['production.place'] == 'Gent') & (df['creator.role'] == "ontwerper")]
print(df6)

#csv opslaan

df6.to_csv('Gentseontwerpers.csv')

#waarden tellen

aantal_records = df["institution.name"].count()
print(aantal_records)

beschrijving = df["description"].count()
print(beschrijving)

filterplaatsenGent = df.loc[df['production.place'] == 'Gent']

records_vervaardigdinGent = filterplaatsenGent['production.place'].count()
print(records_vervaardigdinGent)

#visualiseren met matplotlib
from matplotlib import pyplot as plt

vervaardigdingent = [aantal_records-records_vervaardigdinGent, records_vervaardigdinGent]
plt.pie(vervaardigdingent)
plt.show()