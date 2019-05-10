import keras
import numpy as np
from keras.models import Sequential,Model
from keras.layers import Dense,Dropout,Input,Activation
from keras import metrics,models,layers

train_data = np.loadtxt(open("train.csv","rb"),delimiter=",",skiprows=0)
train_target = np.loadtxt(open("target.csv","rb"),delimiter=",",skiprows=0)
test_data = np.loadtxt(open("test.csv","rb"),delimiter=",",skiprows=0)
mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std
test_data -= mean
test_data /= std

def build_model():
    model = Sequential()
    model.add(Dense(90,activation='tanh',input_shape=(train_data.shape[1],)))
    model.add(Dropout(0.1))
    model.add(Dense(50,activation='tanh'))
    model.add(Dropout(0.1))
    model.add(Dense(1,activation=None))
    model.compile(loss='mean_squared_error',optimizer='adam',metrics=['mae'])
    return model

num_epochs = 3500
model = build_model()
history = model.fit(train_data,train_target,epochs=num_epochs,batch_size=1,verbose=1)
result = model.predict(test_data)
np.savetxt('result_3500',result,delimiter=',')
print('It is done.')