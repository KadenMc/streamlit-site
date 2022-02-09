import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import os

def join(a, b):
    """
    A custom path join function which replaces "\\" with "/". Otherwise,
    os.path.join may cause problems with filepaths (especially on Windows).

    Parameters:
        a (str): Start of file path.
        b (str): End of file path.
    
    Returns:
        (str): The joined path of a and b.
    """
    return os.path.join(a, b).replace("\\", "/")


CUR_PATH = str(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/")
MODEL_PATH = join(CUR_PATH, 'models')

def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def load():
    # Load model - can't cache with Streamlit, unfortunately
    return load_model(join(MODEL_PATH, 'model.h5'))

@st.cache
def load_aux():
    # Define other necessary information
    max_length = 100
    chars = [' ', '!', "'", ',', '-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '?', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    char_indices = {' ': 0, '!': 1, "'": 2, ',': 3, '-': 4, '.': 5, '0': 6, '1': 7, '2': 8, '3': 9, '4': 10, '5': 11, '6': 12, '7': 13, '8': 14, '9': 15, '?': 16, 'a': 17, 'b': 18, 'c': 19, 'd': 20, 'e': 21, 'f': 22, 'g': 23, 'h': 24, 'i': 25, 'j': 26, 'k': 27, 'l': 28, 'm': 29, 'n': 30, 'o': 31, 'p': 32, 'q': 33, 'r': 34, 's': 35, 't': 36, 'u': 37, 'v': 38, 'w': 39, 'x': 40, 'y': 41, 'z': 42}
    indices_char = {0: ' ', 1: '!', 2: "'", 3: ',', 4: '-', 5: '.', 6: '0', 7: '1', 8: '2', 9: '3', 10: '4', 11: '5', 12: '6', 13: '7', 14: '8', 15: '9', 16: '?', 17: 'a', 18: 'b', 19: 'c', 20: 'd', 21: 'e', 22: 'f', 23: 'g', 24: 'h', 25: 'i', 26: 'j', 27: 'k', 28: 'l', 29: 'm', 30: 'n', 31: 'o', 32: 'p', 33: 'q', 34: 'r', 35: 's', 36: 't', 37: 'u', 38: 'v', 39: 'w', 40: 'x', 41: 'y', 42: 'z'}
    return max_length, chars, char_indices, indices_char


def demo(text_in, length, diversity):
    # Load model and other necessary information
    model = load()
    max_length, chars, char_indices, indices_char = load_aux()
    
    # Process the input string
    text_in = text_in.lower()
    text_in = ''.join([s for s in text_in if s in chars])
    
    # Crop the prompt to the relevant max_length
    if len(text_in) <= max_length:
        prompt = ' '*(max_length-len(text_in)) + text_in
    else:
        prompt = text_in[-max_length:]

    sentence = prompt
    result = []
    for i in range(length):
        x_pred = np.zeros((1, max_length, len(chars)))
        for t, char in enumerate(sentence):
            x_pred[0, t, char_indices[char]] = 1.

        preds = model.predict(x_pred, verbose=0)[0]
        next_index = sample(preds, diversity)
        next_char = indices_char[next_index]
        sentence = sentence[1:] + next_char

        result.append(next_char)
    
    return text_in + ''.join(result)