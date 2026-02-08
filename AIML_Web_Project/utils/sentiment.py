from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive Sentiment 😊"
    elif polarity < 0:
        return "Negative Sentiment 😞"
    else:
        return "Neutral Sentiment 😐"
