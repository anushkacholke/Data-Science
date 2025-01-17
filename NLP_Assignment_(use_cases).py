# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 19:22:01 2024
"""
###########################################################
'''Objective:
    Need to understand customer feedback by analyzingreviews using text
    mining and sentiment analysis. 
'''
##############################################################
'''
Task 1:
    1.	Extract reviews of any product from e-commerce website Amazon.
    2.	Perform sentiment analysis on this extracted data and build
    aunigram and bigram word cloud.
'''
# Import required libraries
from bs4 import BeautifulSoup as bs
import requests


# Define the link to the specific Amazon review
link = "https://www.amazon.in/gp/customer-reviews/R2K9HGFU0XYEEL/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&ASIN=B0D3FG6HW9"


# Fetch the page
page = requests.get(link)

# Check if the connection is successfully established (status code 200)
if page.status_code == 200:
    print("Connection Successful!")
else:
    print(f"Failed to connect. Status code: {page.status_code}")

# Extract the content of the page
page_content = page.content

# Parse the page content using BeautifulSoup and HTML parser
soup = bs(page_content, 'html.parser')

# Apply the prettify method to clean the output
print(soup.prettify())


# Now Extracting the Actual Review Text

# Extract the review text using HTML tag and class(find correct class by inspecting page)
review = soup.find('span', {'data-hook': 'review-body'}).get_text(strip=True)

# Print the extracted review
print("Review Text:", review)

#########################################

#Clean the Text Data
import re
import nltk
from nltk.corpus import stopwords

# Function to clean the review text
def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation and numbers
    text = re.sub(r'[^\w\s]', '', text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

# Example to cleaned above review
review_cleaned = clean_text(review)
print("Cleaned Review:", review_cleaned)

#Perform Sentiment Analysis
from textblob import TextBlob

# Function to perform sentiment analysis using TextBlob
def get_sentiment(text):
    analysis = TextBlob(text)
    # Get the sentiment polarity (-1 to 1)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Example 
sentiment = get_sentiment(review_cleaned)
print("Sentiment of the Review:", sentiment)

#Build Word Clouds
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Function to generate a unigram word cloud
def generate_unigram_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Example for unigram word cloud
generate_unigram_wordcloud(review_cleaned)

###############################################################################
###############################################################################
'''
Task 2:
    1.	Extract reviews for any movie from IMDB and perform sentiment analysis.
'''
#import required libraries
import requests
from bs4 import BeautifulSoup

# Example IMDB movie review page link 
url = "https://www.imdb.com/title/tt16141116/reviews/"  # Example movie:2024 (I) (2021)

# Send a GET request to the page
response = requests.get(url)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract reviews
reviews = soup.find_all('div', class_='text show-more__control')

# Example: Print first 5 reviews
for i, review in enumerate(reviews[:5], 1):
    print(f"Review {i}: {review.get_text(strip=True)}\n")

# Clean the reviews
cleaned_reviews = [clean_text(review.get_text(strip=True)) for review in reviews]
print(cleaned_reviews[:5])  # Print cleaned versions of the first 5 reviews
 
#Perform Sentiment Analysis on IMDB Reviews
from textblob import TextBlob

# Perform sentiment analysis on the cleaned reviews
for i, review in enumerate(cleaned_reviews[:5], 1):  # First 5 reviews
    sentiment = TextBlob(review).sentiment.polarity
    print(f"Review {i}: Sentiment Polarity = {sentiment}")
    if sentiment > 0:
        print("Sentiment: Positive\n")
    elif sentiment < 0:
        print("Sentiment: Negative\n")
    else:
        print("Sentiment: Neutral\n")

###############################################################################
###############################################################################
'''
Task 3: 
    1.	Choose any other websiteon the internet and do some research on how 
    to extract text and perform sentiment analysis
'''
     
#import required libraries
import requests
from bs4 import BeautifulSoup

#review page link 
url = "https://www.shopify.com/in/free-trial/3-steps?term=shopify&adid=566014743975&campaignid=15433369407&branded_enterprise=1&BOID=brand&utm_medium=cpc&utm_source=google&gad_source=1&gclid=Cj0KCQjwi5q3BhCiARIsAJCfuZm8fH9LWgBZdUE-FAYkmB6TSttC54py4Z_-k2jpnqYbDZhTZCKMPl4aAk7IEALw_wcB&cmadid=516585705;cmadvertiserid=10730501;cmcampaignid=26990768;cmplacementid=324494758;cmcreativeid=163722649;cmsiteid=5500011"  # shopicy

# Send a GET request to the page
response = requests.get(url)
response
# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract headline
reviews = soup.find_all('h2', class_='richtext text-t5')

# Example: Print 
for i, review in enumerate(reviews[:5], 1):
    print(f"head {i}: {review.get_text(strip=True)}\n")

# Clean the reviews
cleaned_reviews = [clean_text(review.get_text(strip=True)) for review in reviews]
print(cleaned_reviews[:5])  # Print cleaned versions 
 
#Perform Sentiment Analysis 
from textblob import TextBlob

# Perform sentiment analysis on the cleaned reviews
for i, review in enumerate(cleaned_reviews[:5], 1):  
    sentiment = TextBlob(review).sentiment.polarity
    print(f"Review {i}: Sentiment Polarity = {sentiment}")
    if sentiment > 0:
        print("Sentiment: Positive\n")
    elif sentiment < 0:
        print("Sentiment: Negative\n")
    else:
        print("Sentiment: Neutral\n")