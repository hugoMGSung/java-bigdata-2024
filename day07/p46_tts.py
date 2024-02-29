# file : p46_tts.py
# desc : Text To Speech

# pip install gTTS
# pip install pygame
from gtts import gTTS
import pygame

text = input('소리로 바꿀 텍스트 입력 > ')

speech = gTTS(text=text, lang='ko')
speech.save('./day07/tts.mp3')

pygame.mixer.init()
pygame.mixer.music.load('./day07/tts.mp3')
pygame.mixer.music.play()