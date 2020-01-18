import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '%')

@client.event
async def on_ready():
    print('Bot is ready.')

#User Join Event

@client.event
async def on_member_join(member):
    print(f'{member} has entered the Happy Sock Land')

@client.event
async def on_member_remove(member):
    print(f'{member} has created the Sad Sock Land')

#Command One, Ping test
@client.command()
async def ping(ctx):
    await ctx.send(f' Your Ping Is. {round(client.latency * 1000)}ms')
#Command Two. Eightball
@client.command(aliases=['8ball', '8Sock', 'eightball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes, Definitely.',
                 'You may rely on it',
                 'As I see it, Yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes',
                 'Signs point to yes.',
                 'Reply hazy, try again',
                 'Ask again later.',
                 'I will not tell you this now.',
                 'I cannot predict this at the moment',
                 'Concentrate and ask me again',
                 "Don't count on it",
                 'My reply is no!',
                 'My sources are pointing to no.',
                 'The outlook is not so good.',
                 'It is very doubtful.']
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

#Command Three. Clear command.
@client.command()
async def clear(ctx, amount=5):
    amount = amount + 1
    await ctx.channel.purge(limit=amount)


client.run('NjY4MTk3NjA3NDA3MDkxNzIy.XiOWsg.nmW99D7CBY8ssFTh8J7_AaszQKY')
