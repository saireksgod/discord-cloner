from os import system
system("title Discord Cloner by SaiDark")
import discord
import asyncio
from colorama import Fore, init, Style
import platform
from serverclone import Clone
from winotify import Notification, audio
import requests, tempfile, os

ava = requests.get('https://i.pinimg.com/736x/25/8d/da/258ddaf94b61e57dd0e79d37bf47321e.jpg')
ava = ava.content
img_path = os.path.join(tempfile.gettempdir(),'sairekscloner.jpg')
with open(img_path, 'wb') as f:
    f.write(ava)
notif = Notification(app_id='Server Cloner by SaiDark',
                    title='',
                    msg="",
                    duration='short',
                    icon=img_path)
notif.set_audio(audio.Default, loop=False)

try:
    client = discord.Client()
    os = platform.system()
    if os == "Windows":
        system("cls")
    print(f"""{Fore.LIGHTMAGENTA_EX}
                         
            ██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░  ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
            ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
            ██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║  ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
            ██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║  ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
            ██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝  ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
            ╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
    {Style.RESET_ALL}
                                                  {Fore.YELLOW}   Cоздатель: saireks.{Style.RESET_ALL}
    """)
    token = input(f'{Fore.YELLOW} 1. Введите токен аккаунта:\n >>')
    input_guild_id = input(f'{Fore.YELLOW} 2. Id сервера который нужно скопировать:\n >>')
    output_guild_id = input(f'{Fore.YELLOW} 3. Id сервера куда нужно вставить:\n >>')
    if os == "Windows":
        system("cls")
    @client.event
    async def on_ready():
        notif.msg = '🎢 Клонирование началось!'
        notif.show()
        print(f"{Fore.CYAN}                 Вход с аккаунта : {client.user}")
        print(f"{Fore.CYAN}                 Клонирование началось\n\n")
        guild_from = client.get_guild(int(input_guild_id))
        guild_to = client.get_guild(int(output_guild_id))
        await Clone.guild_edit(guild_to, guild_from)
        await Clone.roles_delete(guild_to)
        await Clone.channels_delete(guild_to)
        await Clone.roles_create(guild_to, guild_from)
        await Clone.categories_create(guild_to, guild_from)
        await Clone.channels_create(guild_to, guild_from)
        notif.msg = '✅ Клонирование успешно окончено!'
        notif.duration = 'long'
        notif.show()
        print(f"""{Fore.BLUE}


                                ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██║░░██║
                                ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██║░░██║
                                ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██████╔╝
                                ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░

        {Style.RESET_ALL}""")
        await asyncio.sleep(20)
        await client.close()
    try:
        client.run(token, bot=False)
    except Exception as e:
        notif.msg = '❌ Возникла ошибка!'
        notif.show()
        print(f"{Fore.RED}Возникли проблемы с ТОКЕНОМ аккаунта") 
        print(f"{Fore.RED}Попробуйте его заменить")
        input(f"{Fore.RED}Нажмите Enter для продолжения...")
except:
    notif.msg = '❌ Возникла ошибка!'
    notif.show()
    print(f"{Fore.RED}Похоже у вас стоит не та версия discord.py, нужна 1.7.3")
    input(f"{Fore.RED}Нажмите Enter для продолжения...")
