import discord
from discord.ext import commands
import csv
from csv import DictReader
import random

roomNameWordFile = 'lamoJuanYouGay.csv'

bot = commands.Bot(command_prefix = '.')

# parses csv file for genRoomName function
def loadRoomName(filename):
    from csv import DictReader
    with open(filename, newline='') as csvfile:
        csvReader = csv.reader(csvfile)
        wordDict = {}
        for line in csvReader:
            wordList = []
            for word in line:
                if len(word)>1:
                    wordList.append(word)
            wordDict[line[0]] = (wordList)
    return wordDict
            

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command(name = 'grn')
async def genRoomName(ctx, arg):
    roomCode = str(arg).strip().upper()
    if len(roomCode) == 4 and roomCode.isalpha():
        await ctx.send("Success")
        roomPhrase = ''
        roomNameDict = loadRoomName(roomNameWordFile)
        for char in roomCode:
            listLen = len(roomNameDict[char])
            randNum = random.randint(0,listLen-1)
            roomPhrase += roomNameDict[char][randNum] + ' '
        await ctx.send('The room code is '+ roomPhrase)
        
    else:
        await ctx.send("Room Code must be exactly 4 letters (no letters/special characters)")
        

bot.run('NzUxNjIwNzk1NjE2NDYwODYw.X1Lvag.aRIKMXBmgQbrqQDIhchtaSort_0')