import pandas as pd
import os

def read_spam():
    category = 'spam'
    directory = './enron1/spam'
    return read_category(category, directory)

def read_ham():
    category = 'ham'
    directory = './enron1/ham'
    return read_category(category, directory)

def read_category(category, directory):
    emails = []
    for filename in os.listdir(directory):
        if not filename.endswith(".txt"):
            continue
        with open(os.path.join(directory, filename), 'r') as fp:
            try:
                content = fp.read()
                emails.append({'name': filename, 'content': content, 'category': category})
            except:
                print(f'skipped {filename}')
    return emails

# spam = read_spam()
ham = read_ham()

df = pd.DataFrame.from_records(spam)
df = df.append(pd.DataFrame.from_records(ham))

# import re

# def preprocessor(email):
#     # Remove HTML tags
#     email = re.sub('<[^>]*>', '', email)
    
#     # Remove URLs
#     email = re.sub(r'http\S+', '', email)
    
#     # Remove non-alphanumeric characters and convert to lowercase
#     email = re.sub(r'[^a-zA-Z0-9\s]', '', email).lower()
    
#     # Remove extra whitespaces
#     email = re.sub(r'\s+', ' ', email).strip()
    
#     return email
