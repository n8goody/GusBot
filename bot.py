import discord
from discord.ext import commands
import random

adjectivesFile = 'rcAdjectives.txt'
nounsFile = 'rcNouns.txt'
verbsFile = 'rcVerbs.txt'

isTTSon = True

bot = commands.Bot(command_prefix = 'g!')

# creates dictionary of lists, each list a different letter, for genRoomName from csv file
def fileToDict(filename):
    wordDict = {}
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        wordDict[letter] = []
    with open(filename, newline='') as txtfile:
        reader = txtfile.read().splitlines()
        for line in reader:
            if line[0] not in wordDict:
                wordDict[line[0]] = [line]
            else:
                wordDict[line[0].upper()].append(line.capitalize())
    return wordDict
            

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command()
async def addWords(ctx, type, *words):
    if (len(words)<1):
        ctx.send("Please include words you wish to add.")
    t = str(type).strip().upper()
    if t =='N':
        typeFile = 'rcNouns.txt'
    elif t == 'A':
        typeFile ='rcAdjectives.txt'
    elif t == 'V':
        typeFile = 'rcVerbs.txt'
    else:
        await ctx.send("Invalid Type. Valid types: N = nouns; A = Adjectives; V = Verbs")
        return
    with open(typeFile, "a") as txtfile:
        for word in words:
            txtfile.write('\n' + word.capitalize())
    await ctx.send("Words succesfully added")
    


@bot.command()
async def toggleTTS(ctx):
    global isTTSon
    if isTTSon:
        isTTSon = False
        await ctx.send('TTS is OFF')
    else:
        isTTSon = True
        await ctx.send('TTS is ON')

@bot.command()
async def wordList(ctx, type, letter):
    l = str(letter).strip().upper()
    t = str(type).strip().upper()
    wordType = ''
    if t =='N':
        typeFile = 'rcNouns.txt'
        wordType = "Nouns"
    elif t == 'A':
        typeFile ='rcAdjectives.txt'
        wordType = "Adjectives"
    elif t == 'V':
        typeFile = 'rcVerbs.txt'
        wordType = "Verbs"
    else:
        await ctx.send("Invalid Type. Valid types: N = nouns; A = Adjectives; V = Verbs")
        return

    if (not l.isalpha() and  not l =='%'):
        await ctx.send("Invalid letter. Must be a letter or '%'. '%' = all letters. No special characters/numbers")
        return
    if l == '%':
        typeDict = fileToDict(typeFile)
        output = wordType + ":\n"
        for key in typeDict:
            output += key + ': '
            for word in typeDict[key]:
                output += word + ' '
            output += '\n'
        await ctx.send(output) 
    else:
        typeDict =fileToDict(typeFile)
        output = l + ': '
        for word in typeDict[l]:
            output += word + ' '
        await ctx.send(output) 

@bot.command()
async def shitpost(ctx, arg):
    spCode = str(arg.strip().upper())
    if not spCode.isalpha:
        await ctx.send("Must be letters. No special characters/numbers")
        return
    adjDict = fileToDict(adjectivesFile)
    nounDict = fileToDict(nounsFile)
    verbDict = fileToDict(verbsFile)
    spPhrase = ''
    i = 0
    for char in spCode:
        if i % 3 == 0: #adj
            listLen = len(adjDict[char])
            randNum = random.randint(0,listLen-1)
            spPhrase += adjDict[char][randNum] + ' '
        if i % 3 == 1: #noun
            listLen = len(nounDict[char])
            randNum = random.randint(0,listLen-1)
            spPhrase += nounDict[char][randNum] + ' '
        if i % 3 == 2: #verb
            listLen = len(verbDict[char])
            randNum = random.randint(0,listLen-1)
            spPhrase += verbDict[char][randNum] + ' '
        i += 1
    await ctx.send(spPhrase, tts=isTTSon)

@bot.command(name = 'grn')
async def genRoomName(ctx, arg):
    roomCode = str(arg).strip().upper()
    if len(roomCode) == 4 and roomCode.isalpha():
        roomPhrase = ''
        adjDict = fileToDict(adjectivesFile)
        nounDict = fileToDict(nounsFile)
        verbDict = fileToDict(verbsFile)

        #noun
        char = roomCode[0]
        listLen = len(nounDict[char])
        randNum = random.randint(0,listLen-1)
        roomPhrase += nounDict[char][randNum] + ' '

        #verb
        char = roomCode[1]
        listLen = len(verbDict[char])
        randNum = random.randint(0,listLen-1)
        roomPhrase += verbDict[char][randNum] + ' '

        #adj
        char = roomCode[2]
        listLen = len(adjDict[char])
        randNum = random.randint(0,listLen-1)
        roomPhrase += adjDict[char][randNum] + ' '

        #noun
        char = roomCode[3]
        listLen = len(nounDict[char])
        randNum = random.randint(0,listLen-1)
        roomPhrase += nounDict[char][randNum] + ' '

        await ctx.send('The room code is '+ roomPhrase, tts=isTTSon)
        
    else:
        await ctx.send("Room Code must be exactly 4 letters (no numbers/special characters)")
        

bot.run('NzUxNjIwNzk1NjE2NDYwODYw.X1Lvag.aRIKMXBmgQbrqQDIhchtaSort_0')