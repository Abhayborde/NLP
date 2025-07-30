import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

example_string = """
Sagar (PRN: UIT22M1019) is pursuing B.Tech in Information Technology at Sanjivani College of Engineering.
He is passionate about AI and machine learning.
Recently, he started learning Natural Language Processing (NLP).
He enjoys working on Python projects in his free time.
His favorite subjects are Data Structures, Algorithms, and Cloud Computing.
"""

sentences = sent_tokenize(example_string)
print(sentences)

words = word_tokenize(example_string)

words = [word for word in words if word.isalnum()]

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

print(filtered_words)
print(stemmed_words)
print(lemmatized_words)
