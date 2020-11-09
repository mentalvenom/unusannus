import praw
import random
from os import getenv
from discord.ext import commands

bot = commands.Bot(description="Unus Annus", command_prefix="!")

reddit = praw.Reddit(client_id=getenv('CLIENTID'), client_secret=getenv('CLIENTSECRET'), user_agent='UnusAnnus 1.0 by /u/Odd-Ant-5614 https://repl.it/@replitcode/UnusAnnusBot')

@bot.command()
async def meme():
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await bot.say(submission.url)
async def fiftyfifty():
    fiftyfifty_submissions = reddit.subreddit('FiftyFifty').hot()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in fiftyfifty_submissions if not x.stickied)

    await bot.say(submission.url)

print("bot online")

bot.run(getenv('TOKEN'))
