# Import necessary libraries
from textblob import TextBlob

# Define a function to get sentiment from user input
def get_sentiment(text):
    analysis = TextBlob(text)
    # Get polarity (-1 = negative, 1 = positive)
    return analysis.sentiment.polarity

# Define a function to recommend music based on sentiment
def recommend_music(sentiment_score):
    if sentiment_score > 0.5:
        return "You're feeling great! How about some upbeat pop or electronic music?"
    elif 0 < sentiment_score <= 0.5:
        return "You're in a positive mood. Indie rock or jazz might be nice."
    elif -0.5 <= sentiment_score <= 0:
        return "It seems like you're feeling a bit down. Maybe try some soothing classical or lo-fi music."
    else:
        return "You're feeling really low. Some slow, mellow tunes like acoustic or blues could help."

# Main program
if __name__ == "__main__":
    print("Welcome to the Mood-based Music Recommendation System!")
    user_input = input("How are you feeling today? Describe your mood in a sentence: ")
    
    # Get the sentiment score
    sentiment_score = get_sentiment(user_input)
    
    # Recommend music based on sentiment
    music_recommendation = recommend_music(sentiment_score)
    
    # Print the recommendation
    print(f"\nMood Analysis: {sentiment_score:.2f}")
    print(music_recommendation)
