import pickle

# from keras.datasets.mnist import load_data
# from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
# from keras.models import Sequential
# from keras.utils import to_categorical
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical


def create_model(n_filters, n_hidden, n_classes=10):
    model = Sequential()
    model.add(Conv2D(n_filters, (3, 3), padding='same',input_shape=(28, 28, 1), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(n_filters, (3, 3), padding='same', activation='relu'))
    model.add(Flatten())
    model.add(Dense(n_hidden, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(n_classes, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def train(model, x_train, y_train):
    x_train = x_train/255.0
    x_train = x_train.reshape(x_train.shape[0],
                              x_train.shape[1],
                              x_train.shape[2],
                              1)
    y_train = to_categorical(y_train)
    model.fit(x_train, y_train, batch_size=64, epochs=1, validation_split=0.2)
    return model


if __name__ == '__main__':
    n_filters = 32
    n_hidden = 256
    (x_train, y_train), (x_test, y_test) = load_data()

    model = create_model(n_filters, n_hidden)
    trained_model = train(model, x_train, y_train)
    trained_model.save('model.h5')
    # tf.saved_model.save(pretrained_model, "/tmp/mobilenet/1/")
    # with open('model.pkl', 'wb') as f:
    #     pickle.dump(trained_model, f)
    print("model saved")
