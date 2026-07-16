from textblob import TextBlob

sentence = TextBlob(input("Sentence - "))

e2e = {
    "sad": "😞",
    "happy": "😄",
    "dissatisfaction": "😕",
    "satisfaction": "🙂",
    "neutral":"😐"
}

senti = sentence.sentiment.polarity
if senti >= 0.6:
  emo = "happy"
elif senti >= 0.2:
  emo = "satisfaction"
elif senti >= -0.2:
  emo = "neutral"
elif senti >= -0.6:
  emo = "dissatisfaction"
else:
  emo = "sad"

keywords = {
    "love": "🥰",
    "angry": "😡",
    "betrayed": "😡",
    "tired": "😩",
    "lazy": "😩"
}
e2e.update(keywords)
for k in keywords:
  if k in sentence.string.lower() and "I" in sentence.string.split():
    emo = k

if sentence.sentiment.subjectivity < 0.3:
  e2e["objective"] = "🧠"
  emo = "objective"

print(e2e[emo])
