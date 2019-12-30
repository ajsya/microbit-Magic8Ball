# Shake the micro:bit for a fortune from "the magic 8-Ball".
from microbit import *
import random


fortunes = [
    "Better not tell you now!",
    "Outcome Likly",
    "Outlook not so good",
    "Very Dobtful",
    "Yes",
    "No",
    "Ask again later",
    "Consitrate and ask again",
    "My reply is no",
    "Maybe",
    "It is certain",
    "You may rely on it",
    ]


while True:
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(500)
        chosenFortune = random.choice(fortunes)
        display.scroll(chosenFortune)
