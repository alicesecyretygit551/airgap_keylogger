![My keylogger](logo.jpg)

# Description
A simple keylogger that can bridge an airgapped system over near-ultrasonic frequencies using soundwaves to transmit data. The keylogger captures keystrokes on the target machine and transmits them via inaudible audio signals. The receiving machine only needs a microphone to capture and decode these signals.

This project is intended for educational purposes, demonstrating how an airgap attack can be carried out using an acoustic channel.

# Setup
Install the necessary dependencies on both computers:

` pip3 install pynput sounddevice numpy `

` apt install python3-dev python3-setuptools libsndfile1 ` 
# Usage
## Victim Machine:

Place and run the keylog.py script.
The script will capture keystrokes and transmit them over the audio channel as sound signals.
## Attacker Machine:

Run the listener.py script to receive and decode the transmitted audio signals.
The received keystrokes will be displayed on the terminal and logged into a file.
