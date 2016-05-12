from collections import Counter
from nltk.corpus import twitter_samples, stopwords
from nltk import bigrams
from nltk import trigrams


tokenizedWordsFromTwitter = twitter_samples.tokenized('tweets.20150430-223406.json')
tokenizedWordsFromTwitter += twitter_samples.tokenized('negative_tweets.json')
tokenizedWordsFromTwitter += twitter_samples.tokenized('positive_tweets.json')
#tokenizedWordsFromTwitter = twitter_samples.tokenized('positive_tweets.json')

for tweetIndex in range(len(tokenizedWordsFromTwitter)):
    tokenizedWordsFromTwitter[tweetIndex] = [item for item in tokenizedWordsFromTwitter[tweetIndex] if item not in [".",",",":",";","!","?","(",")"]]
    tokenizedWordsFromTwitter[tweetIndex] = [item for item in tokenizedWordsFromTwitter[tweetIndex] if item not in stopwords.words('english')]

print("Number of Tweets: " + str(len(tokenizedWordsFromTwitter)))

twitter_unigrams = Counter({})
twitter_bigrams = Counter({})
twitter_trigrams = Counter({})

for i in tokenizedWordsFromTwitter:

    twitter_unigrams += Counter(i)

    individual_bigrams = bigrams(i)
    twitter_bigrams += Counter(individual_bigrams)

    individual_trigrams = trigrams(i)
    twitter_trigrams += Counter(individual_trigrams)

print("Unigrams: ")
print(twitter_unigrams.most_common(10))
print("Bigrams: ")
print(twitter_bigrams.most_common(10))
print("trigrams: ")
print(twitter_trigrams.most_common(10))