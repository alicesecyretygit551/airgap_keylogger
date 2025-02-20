#!/usr/bin/env python3
import argparse
import sys
import time
import sounddevice as sd
import numpy as np

print("Starting up...\n")
time.sleep(0.5)
print("There you go.\n\n")

# Функция для декодирования аудио в текст
def decode_audio(audio_data):
    # Здесь используем очень упрощенную логику
    # Преобразуем аудио обратно в символы на основе частоты
    sample_rate = 44100
    duration = 0.5
    message = ""
    
    for i in range(0, len(audio_data), int(sample_rate * duration)):
        segment = audio_data[i:i+int(sample_rate * duration)]
        frequency = np.argmax(np.abs(np.fft.fft(segment)))  # Преобразуем частоту в символ
        char = chr(frequency // 10)
        message += char
    
    return message

# Функция для прослушивания аудио данных
def listen_for_audio():
    while True:
        try:
            # Захватываем аудио с микрофона
            audio_data = sd.rec(int(44100 * 0.5), samplerate=44100, channels=1, dtype='float64')
            sd.wait()

            # Декодируем аудио в сообщение
            message = decode_audio(audio_data.flatten())
            print("Received:", message)
            with open("log.txt", 'a') as f:
                f.write(message)

        except Exception as e:
            print(f"Error: {e}")
            continue

# Главная функция
def main():
    listen_for_audio()

if __name__ == '__main__':
    main()

