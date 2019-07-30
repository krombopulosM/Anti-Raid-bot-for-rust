import os
import os.path
from os import path
import numpy as np
from PIL import ImageGrab
import cv2
import pytesseract
import pyautogui
import discord
from discord.ext import commands
import asyncio

description = '''Rust Anti-Raid Bot made by Randolf, Version 1.1.0'''
bot = commands.Bot(command_prefix='!', description=description)
bot.raid_bot_channel = ''

# setting up OCR
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe"


home = os.path.expanduser('~')
home
print('checking for token file...')
try:
    with open(home +'\KEEP-ME.txt') as file_in:
        token = file_in.readline()
except FileNotFoundError:
    token = input('Enter your discord bot token > ')
    with open(home +'\KEEP-ME.txt', 'w') as file_out:
        file_out.write(token)


@bot.event
async def on_ready():
    print("Started Rust Anti-Raid Bot")
    print ("Version 1.1.0 by Randolf")


@bot.command(name="archannel", pass_context=True)
async def archannel(ctx):
    """Changes notification channel to current channel"""
    await bot.say('Successfully changed notification channel to #' + ctx.message.channel.name)
    bot.raid_bot_channel = ctx.message.channel.id


@bot.command(name="arstart", pass_context=True)
async def arstart(ctx):
    """Starts Rust Anti-Raid Bot"""
    if bot.get_channel(bot.raid_bot_channel) is None:
        await bot.say('A notification channel has not been set. Please first set your notification channel with '
                      '"!archannel" in the channel you would like.')
        return
    await bot.say('Successfully started Rust Anti-Raid Bot')
    bot.loop.create_task(main())


@bot.command(name="arscreenshot", pass_context=True)
async def arscreenshot(ctx):
    """Takes a screenshot"""
    screenshot = ImageGrab.grab()
    screenshot.save('screenshot.png')
    await bot.send_file(ctx.message.channel, 'screenshot.png')


# sending message to discord
async def raid(message, channel):
    await bot.send_message(bot.get_channel(channel), message)


# checking if image text = 'respawn' with OCR
def process_img(grey_img):
    txt = pytesseract.image_to_string(grey_img)
    if txt == "RESPAWN":
        return True
    return False


# start rust anti-raid bot
async def main():
    await bot.wait_until_ready()

    food_counter = 0

    while True:
        # processing image to convert to different format, make it more readable for OCR and display the image
        img = ImageGrab.grab(bbox=(1420, 935, 1600, 970))
        img = np.array(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('window', img)

        # if image text = 'respawn' call raid() function and end script
        if process_img(img):
            bot.loop.create_task(raid("@everyone You're being raided!", bot.raid_bot_channel))
            cv2.destroyAllWindows()
            await asyncio.sleep(3)
            continue

        # end script if 'q' is pressed in cv2 window
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        food_counter += 1
        if food_counter == 720:
            pyautogui.keyDown('6')
            pyautogui.keyUp('6')
            food_counter = 0

        asyncio.sleep(5)
#Enter your discord bot token here
bot.run(token)
