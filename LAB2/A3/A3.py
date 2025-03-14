from textblob import TextBlob

# Given review messages
reviews = [
    "I purchased headphones online. I am very happy with the product.",
    "I saw the movie yesterday. The animation was really good but the script was ok.",
    "I enjoy listening to music",
    "I take a walk in the park everyday"
]

# Perform sentiment analysis
for review in reviews:
    sentiment = TextBlob(review).sentiment
    polarity = sentiment.polarity  # Sentiment score (-1 to 1)
    subjectivity = sentiment.subjectivity  # Subjectivity score (0 to 1)
    
    # Categorize sentiment
    if polarity > 0:
        sentiment_label = "Positive"
    elif polarity < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    
    # Print results
    print(f"Review: {review}")
    print(f"Sentiment: {sentiment_label} (Polarity: {polarity:.2f}, Subjectivity: {subjectivity:.2f})\n")

