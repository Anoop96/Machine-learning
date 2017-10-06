import json, math, pickle, time, re
from textblob import TextBlob as tb

#Calculate Term Frequency
def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

#Calculate words in blobs
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

#Inverse Doc Freq
def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

#TF-IDF
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

'''
#Remove Commonly Used Words
def rmv_stpwrds(string):
	stop_words=['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'you']
	string = string.lower()
	for ch in stop_words:
		if ch in string:
			string = string.replace(' '+ch+' ',' ')
	return string
'''
#Herbs Dataset
start = time.time()
herb_data=[]
with open('data.json', 'r') as fx:
    herb_data = json.loads(fx.read())

#List of blobs containing eng name, botanical name, properties
properties=[]
for i in herb_data:
	line = '"""'+' '+i['botanical_name']+' '+' '.join(i['places'])+' '+re.sub(r'[\s]disorder[s]?','',' '.join(i['properties']))+'"""'
	properties.append(tb(line))
#print(properties[:10])

#TF-IDF scores of each blob
scores=[]
for i, blob in enumerate(properties):
    scores.append({word: tfidf(word, blob, properties) for word in blob.words})

#Save Trained Model
with open('model.sav','wb') as mod:
	pickle.dump(scores, mod, protocol=pickle.HIGHEST_PROTOCOL)

#Save Data
with open('data.sav','wb') as data:
	pickle.dump(herb_data, data, protocol=pickle.HIGHEST_PROTOCOL)
print('Trained in: '+str(time.time()-start))
