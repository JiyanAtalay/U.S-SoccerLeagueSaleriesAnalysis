import numpy as np
import pandas as pd

dataset = pd.read_csv("mls-salaries-2017.csv")
# İlk 10 veriyi okuma
# reading the first 10 data
"""
print(dataset.head(n = 10))
"""
# Ortalama bulma
# Find mean
"""
arr = np.array(dataset["base_salary"])
print(arr.mean())
"""
# En yüksek maaş bulma
# Find max salary
"""
print(dataset["base_salary"].max())
"""
# En yüksek tazminata sahip oyuncu
# Find max compensation
"""
print(dataset[dataset["guaranteed_compensation"].max() == dataset["guaranteed_compensation"]])
"""
# Gonzalez Pirez mevki bulma
# Find Gonzalez Pirez position
"""
print(dataset[dataset["last_name"] == "Gonzalez Pirez"]["position"].iloc[0])
"""
# Mevkilere göre futbolcuları gruplayarak mevkilerde ortalama maaşları bulun
# Group football players according to positions and find the average salaries in each position
"""
print(dataset.groupby("position").mean())
"""
# Kaç farklı mevki olduğunu bulma
# Find the number of positions
"""
print(dataset["position"].nunique())
print(dataset["position"].nunique())
"""
# Her mevkide kaç oyuncu olduğunu hesaplama
# Calculate the number of players in each position
"""
print(dataset["position"].value_counts())
"""
# Her takımda kaç kişinin oynadığını hesaplayınız
# Calculate the number of players in each team
"""
print(dataset["club"].value_counts())
"""
# Soyadında 'son' olanları bulma
# Find those with the last name containing 'son'
"""
def findson(last_name):
    if "son" in last_name.lower():
        return True
    return False

print(dataset[dataset["last_name"].apply(findson)])
"""