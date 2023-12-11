import pandas as pd

file_path = 'Question2/titles.csv'

df = pd.read_csv(file_path)

def countvowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count+=1

    return count

df['Vowels'] = df['title'].astype(str).apply(countvowels)

print(df.head(30))