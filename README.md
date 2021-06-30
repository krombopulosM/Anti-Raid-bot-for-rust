# Rust Anti-Raid bot

Rust Anti-raid bot for detecting intruders and reporting back to your discord server. Made in Python 3.6 and Tesseract-OCR, it monitors if the "Respawn" button is located in the bottom right (indicating death) and will then @everyone in the channel specified every X seconds (default is 3).


# Usage

The Discord bot comes with several commands, which are used to control how to bot works.

!help | Displays the list of commands<br>
!archannel | Sets the channel for alerts to the current<br>
!arscreenshot | Takes a screenshot of the bots screen and publishes it to the channel<br>
!arstart | Starts monitoring for the "Respawn" button in order to alert your channel<br>

once !arstart has been initilized a new window will appear with the contents of the bottom right screen, indicating monitor-mode, once it reads "Respawn" it will alert the channel, you can stop Monitoring by closing down the application.

![Discord Commands](https://i.imgur.com/f0q68if.png)

# Pre-compiled

you can download the compiled file [here](https://anonfile.com/s5569b19nd/Anti-Raid_exe), it's still required you install [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract/wiki/4.0-with-LSTM#400-alpha-for-windows) to your C:\Program Files (x86)\Tesseract-OCR.
once installed open the file and it will begin checking for an existing discord bot token, if one is not found you can create one from [here](https://discordapp.com/developers/applications/) and paste it in, The token is then saved and memorized for the next time you boot the program.

# Setup

The script was made using Python 3.6, Tesseract-OCR and Discord.py version 0.6. To modify/compile you will need the following Modules:

pip install discord.py==1.7.3<br>
pip install numpy<br>
pip install pillow<br>
pip install opencv-python<br>
pip install pytesseract<br>
pip install autogui<br>
pip install async.io<br>

At the bottom of the script is where you should place your discord bot token, and then compile.

# Tesseract-OCR

Tesseract is the program that is used to monitor for "respawn" and report back. By default the bot searches for the file in C:\Program Files (x86)\Tesseract-OCR. So when installing make sure you have your file paths the same as the bot script.

You can download Tesseract-OCR from here:<br>
https://github.com/tesseract-ocr/tesseract/wiki/4.0-with-LSTM#400-alpha-for-windows
