# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ipFoSieAGCXJnyQhJit5i60KEpN6C7Wx

# **NEXT_WORD_PREDICTION**
"""

data='''Children are not things to be molded, but are people to be unfolded.
A child is a beam of sunlight from the Infinite and Eternal, with possibilities of virtue and vice, but as yet unstained.
Children are our most valuable resource.
Children are the living messages we send to a time we will not see.
Children see magic because they look for it.
Old men can make war, but it is children who will make history.
I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin, but by the content of their character.
The soul is healed by being with children.
Children are a gift from the Lord, the fruit of the womb a reward.
And He took the children in his arms, placed his hands on them and blessed them.
Children are a heritage from the LORD, offspring a reward from him.
Children’s children are a crown to the aged, and parents are the pride of their children.
Start children off on the way they should go, and even when they are old they will not turn from it.
Every child you encounter is a divine appointment.
Children are like wet cement: whatever falls on them makes an impression.
Children are the hands by which we take hold of heaven.
You have to love your children unselfishly. That is hard. But it is the only way.
Children make your life important.
Hugs can do great amounts of good, especially for children.
The best inheritance a parent can give his children is a few minutes of his time each day.
Always kiss your children goodnight, even if they’re already asleep.
Children are not casual guests in our home. They have been loaned to us temporarily for the purpose of loving them and instilling a foundation of values on which their future lives will be built.
Children have never been very good at listening to their elders, but they have never failed to imitate them.
The potential possibilities of any child are the most intriguing and stimulating in all creation.
The best way to make children good is to make them happy.
When I approach a child, he inspires in me two sentiments – tenderness for what he is and respect for what he may become.
The greatest gifts you can give your children are the roots of responsibility and the wings of independence.
At every step the child should be allowed to meet the real experience of life; the thorns should never be plucked from his roses.
You can learn many things from children. How much patience you have, for instance.
Children seldom misquote. In fact, they usually repeat word for word what you shouldn’t have said.
A child is a curly dimpled lunatic.
Children are a great comfort to us in our old age, and they help us reach it faster too.
I have found the best way to give advice to your children is to find out what they want and then advise them to do it.
Cleaning your house while your kids are still growing up is like shoveling the sidewalk before it stops snowing.
Children are likely to live up to what you believe of them.
Children must be taught how to think, not what to think.
Each day of our lives we make deposits in the memory banks of our children.
Children need models rather than critics.
Children are great imitators. So give them something great to imitate.
While we try to teach our children all about life, Our children teach us what life is all about.
Play is often talked about as if it were a relief from serious learning. But for children play is serious learning. Play is really the work of childhood.
Our heritage and ideals, our code and standards – the things we live by and teach our children – are preserved or diminished by how freely we exchange ideas and feelings'''

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer()

tokenizer.fit_on_texts([data])

len(tokenizer.word_index)

input_sequences = []
for sentence in data.split('\n'):
  tokenized_sentence = tokenizer.texts_to_sequences([sentence])[0]

  for i in range(1,len(tokenized_sentence)):
    input_sequences.append(tokenized_sentence[:i+1])

input_sequences

max_len = max([len(x) for x in input_sequences])

from tensorflow.keras.preprocessing.sequence import pad_sequences
padded_input_sequences = pad_sequences(input_sequences, maxlen = max_len, padding='pre')

padded_input_sequences

X = padded_input_sequences[:,:-1]

y = padded_input_sequences[:,-1]

X.shape

y.shape

from tensorflow.keras.utils import to_categorical
y = to_categorical(y,num_classes=285)

y.shape

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

model = Sequential()
model.add(Embedding(285, 100, input_length=34))
model.add(LSTM(150))
model.add(Dense(285, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])

model.summary()

model.fit(X,y,epochs=100)

import time
import numpy as np
text = "Children need"

for i in range(4):
  # tokenize
  token_text = tokenizer.texts_to_sequences([text])[0]
  # padding
  padded_token_text = pad_sequences([token_text], maxlen=34, padding='pre')
  # predict
  pos = np.argmax(model.predict(padded_token_text))

  for word,index in tokenizer.word_index.items():
    if index == pos:
      text = text + " " + word
      print(text)
      time.sleep(2)



