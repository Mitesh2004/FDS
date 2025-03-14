import re
import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud

# Download stopwords (if not already available)
nltk.download('stopwords')
nltk.download('punkt')

# Sample paragraph
text = """Natural Language Processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence.
It focuses on the interaction between computers and humans through natural language.
The goal of NLP is to enable computers to understand, interpret, and generate human language."""

# Preprocessing: Remove special characters and digits
clean_text = re.sub(r'[^A-Za-z\s]', '', text)

# Tokenization
sentences = sent_tokenize(clean_text)
words = word_tokenize(clean_text.lower())

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Word frequency
word_freq = Counter(filtered_words)

# Display word frequency distribution
print("Word Frequency Distribution:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")

# Plot word frequency distribution
plt.figure(figsize=(10, 5))
plt.bar(word_freq.keys(), word_freq.values(), color='blue')
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Word Frequency Distribution")
plt.xticks(rotation=45)
plt.show()

# Generate WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(filtered_words))

# Plot WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud")
plt.show()

