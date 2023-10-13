import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print('Excecao: ' + str(e))


def run_discord_bot():
    intentions = discord.Intents.default()
    intentions.message_content = True

    TOKEN = ''
    client = discord.Client(intents= intentions)

    @client.event
    async def on_ready(): #chamado quando o bot é iniciado
        print(f'{client.user} ta rodando')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} disse: {user_message} em {channel}')

        if user_message == '&npc':
            await send_message(message, user_message, is_private=True)
        elif user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)



    client.run(TOKEN)
