import re
import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud

# Download necessary resources (only required once)
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Step 1: Read the exported WhatsApp chat file
with open("chat.txt", "r", encoding="utf-8") as file:
    chat_data = file.read()

# Step 2: Preprocess the text (Remove timestamps, special characters, and tokenize)
chat_data = re.sub(r'\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2} - ', '', chat_data)  # Remove timestamps
chat_data = re.sub(r'[^A-Za-z\s]', '', chat_data)  # Remove special characters

# Tokenize sentences
sentences = sent_tokenize(chat_data)

# Print tokenized sentences
print("\nTokenized Sentences:")
for sent in sentences[:10]:  # Display first 10 sentences
    print(sent)

# Step 3: Tokenize words, remove stopwords, and perform lemmatization
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

words = word_tokenize(chat_data.lower())  # Tokenize words
filtered_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]

# Step 4: Generate WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(filtered_words))

# Plot WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of WhatsApp Chat")
plt.show()

