# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2020 gomashio1596

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
try:
    import asyncio
    import copy
    import datetime
    import json
    import logging
    import os
    import platform
    import random
    import re
    import socket
    import string
    import sys
    import time
    import traceback
    import unicodedata
    import webbrowser
    from collections import defaultdict
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from functools import partial, wraps
    from glob import glob
    from threading import Thread, Timer
    from typing import Any, Callable, List, Optional, Type, Union
except ModuleNotFoundError as e:
    import traceback
    print(traceback.format_exc())
    import platform
    print(f'Python {platform.python_version()}\n')
    print('標準ライブラリの読み込みに失敗しました。Pythonのバージョンが間違っている可能性があります。Pythonの再インストールなどを試してみてください。問題が修正されない場合は\nTwitter @gomashio1596\nDiscord gomashio#4335\nこちらか\nhttps://discord.gg/NEnka5N\nDiscordのサーバーまでお願いします')
    print('Failed to load basic library. Python version maybe wrong. Try reinstall Python. If the issue is not resolved, contact me\nTwitter @gomashio1596\nDiscord gomashio#4335\nor please join support Discord server\nhttps://discord.gg/NEnka5N')
    sys.exit(1)

try:
    import aiohttp
    import discord
    import fortnitepy
    import jaconv
    import requests
    import sanic.exceptions
    import sanic.response
    from bs4 import BeautifulSoup
    from aioconsole import ainput
    from crayons import cyan, green, magenta, red, yellow
    from fortnitepy import ClientPartyMember, Enum
    from jinja2 import Environment, FileSystemLoader
    from sanic import Sanic
    from sanic.request import Request
    from colorama import Fore, Back, Style
except ModuleNotFoundError as e:
    print(traceback.format_exc())
    print(f'Python {platform.python_version()}\n')
    print('サードパーティーライブラリの読み込みに失敗しました。INSTALL.bat を実行してください。問題が修正されない場合は\nTwitter @gomashio1596\nDiscord gomashio#4335\nこちらか\nhttps://discord.gg/NEnka5N\nDiscordのサーバーまでお願いします')
    print('Failed to load third party library. Please run INSTALL.bat. If the issue is not resolved, contact me\nTwitter @gomashio1596\nDiscord gomashio#4335\nor please join support Discord server\nhttps://discord.gg/NEnka5N')
    sys.exit(1)

try:
    import modules
except ModuleNotFoundError:
    print(traceback.format_exc())
    print(f'Python {platform.python_version()}\n')
    print(
        'モジュールの読み込みに失敗しました。Check Update.bat を実行してください。問題が修正されない場合は\n'
        'Twitter @gomashio1596\n'
        'Discord gomashio#4335\n'
        'こちらか\n'
        'https://discord.gg/NEnka5N\n'
        'Discordのサーバーまでお願いします'
    )
    print(
        'Failed to module. Please run Check Update.bat. If the issue is not resolved, contact me\n'
        'Twitter @gomashio1596\n'
        'Discord gomashio#4335\n'
        'or please join support Discord server\n'
        'https://discord.gg/NEnka5N'
    )
    sys.exit(1)

if sys.platform == 'win32':
    asyncio.set_event_loop(asyncio.ProactorEventLoop())
else:
    try:
        import uvloop
    except ModuleNotFoundError:
        pass
    else:
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

        loop = asyncio.get_event_loop()
        bot = modules.Bot(mode, loop=loop, dev='-dev' in sys.argv)
        bot.setup()
        loop.run_until_complete(bot.start())

if True: #Classes
    class PartyPrivacy(Enum):
        PUBLIC = {
            'partyType': 'Public',
            'inviteRestriction': 'AnyMember',
            'onlyLeaderFriendsCanJoin': False,
            'presencePermission': 'Anyone',
            'invitePermission': 'Anyone',
            'acceptingMembers': True,
        }
        FRIENDS_ALLOW_FRIENDS_OF_FRIENDS = {
            'partyType': 'FriendsOnly',
            'inviteRestriction': 'LeaderOnly',
            'onlyLeaderFriendsCanJoin': False,
            'presencePermission': 'Anyone',
            'invitePermission': 'Anyone',
            'acceptingMembers': True,
        }
        FRIENDS = {
            'partyType': 'FriendsOnly',
            'inviteRestriction': 'LeaderOnly',
            'onlyLeaderFriendsCanJoin': True,
            'presencePermission': 'Leader',
            'invitePermission': 'Leader',
            'acceptingMembers': False,
        }
        PRIVATE_ALLOW_FRIENDS_OF_FRIENDS = {
            'partyType': 'Private',
            'inviteRestriction': 'LeaderOnly',
            'onlyLeaderFriendsCanJoin': False,
            'presencePermission': 'Noone',
            'invitePermission': 'Anyone',
            'acceptingMembers': False,
        }
        PRIVATE = {
            'partyType': 'Private',
            'inviteRestriction': 'LeaderOnly',
            'onlyLeaderFriendsCanJoin': True,
            'presencePermission': 'Noone',
            'invitePermission': 'Leader',
            'acceptingMembers': False,
        }

    class bool_:
        @classmethod
        def create(cls, content: str) -> bool:
            d = {"false": False, "true": True}
            return d.get(content.lower(), False)

    class bool_none:
        @classmethod
        def create(cls, content: str) -> bool:
            d = {"false": False, "true": True, "none": None}
            return d.get(content.lower(), False)

    class select:
        def __init__(self, content: List[dict]) -> None:
            self.content = content

    class Red:
        pass

    class FixRequired:
        pass

    class CanLinebreak:
        pass

    class LoginManager:
        def __init__(self) -> None:
            self.id_len = 64
            self.expire_time = datetime.timedelta(minutes=10)
            self.expires = {}
            self.cookie_key = "X-SessionId"
            self.no_auth_handler_ = sanic.response.html("Unauthorized")

        def generate_id(self, request: Request) -> str:
            Id = "".join(random.choices(string.ascii_letters + string.digits, k=self.id_len))
            while Id in self.expires.keys():
                Id = "".join(random.choices(string.ascii_letters + string.digits, k=self.id_len))
            return Id

        def authenticated(self, request: Request) -> bool:
            if data["web"]["login_required"]:
                Id = request.cookies.get(self.cookie_key)
                if not Id:
                    return False
                elif Id in self.expires.keys():
                    return True
                else:
                    return False
            else:
                return True

        def login_user(self, request: Request, response: Type[sanic.response.BaseHTTPResponse]) -> None:
            Id = self.generate_id(request)
            response.cookies[self.cookie_key] = Id
            self.expires[Id] = datetime.datetime.utcnow() + self.expire_time

        def logout_user(self, request: Request, response: Type[sanic.response.BaseHTTPResponse]) -> None:
            Id = request.cookies.get(self.cookie_key)
            if Id:
                del response.cookies[self.cookie_key]
                self.expires[Id] = datetime.datetime.utcnow() + self.expire_time

        def login_required(self, func: Callable):
            @wraps(func)
            def deco(*args: Any, **kwargs: Any):
                request = args[0]
                if self.authenticated(request):
                    return func(*args, **kwargs)
                elif isinstance(self.no_auth_handler_, sanic.response.BaseHTTPResponse):
                    return self.no_auth_handler_
                elif callable(self.no_auth_handler_):
                    return self.no_auth_handler_(*args, **kwargs)
            return deco

        def no_auth_handler(self, func: Callable):
            if asyncio.iscoroutinefunction(func) is False:
                raise ValueError("Function must be a coroutine")
            self.no_auth_handler_ = func
            @wraps(func)
            def deco(*args: Any, **kwargs: Any):
                return func(*args, **kwargs)
            return deco

    class WebUser:
        def __init__(self, sessionId: str) -> None:
            self._id = sessionId

        @property
        def display_name(self) -> None:
            return "WebUser"

        @property
        def id(self) -> None:
            return self._id

    class WebMessage:
        def __init__(self, content: str, sessionId: str, client: fortnitepy.Client) -> None:
            self._sessionId = sessionId
            self._content = content
            self._client = client
            self._author = WebUser(self._sessionId)
            self._messages = []

        @property
        def author(self) -> WebUser:
            return self._author

        @property
        def content(self) -> str:
            return self._content

        @property
        def client(self) -> Type[fortnitepy.Client]:
            return self._client

        @property
        def result(self) -> str:
            return self._messages

        def reply(self, content: str) -> None:
            self._messages.append(content)

    class AllMessage:
        def __init__(self,
                     content: str,
                     author: Union[fortnitepy.user.UserBase, discord.abc.User, WebUser],
                     client: fortnitepy.Client,
                     base: Union[fortnitepy.message.MessageBase, discord.Message, WebMessage]
                    ) -> None:
            self._content = content
            self._author = author
            self._client = client
            self._base = base
            self._messages = {}

        @property
        def author(self) -> WebUser:
            return self._author

        @property
        def content(self) -> str:
            return self._content

        @property
        def client(self) -> fortnitepy.Client:
            return self._client

        @property
        def base(self) -> Union[fortnitepy.message.MessageBase, discord.Message, WebMessage]:
            return self._base

        @property
        def result(self) -> str:
            return self._messages

        def reply(self, content: str, client: fortnitepy.Client) -> None:
            if not self._messages.get(client.user.id):
                self._messages[client.user.id] = []
            self._messages[client.user.id].append(content)

    class CanBeMultiple:
        pass

    class Client(fortnitepy.Client):
        def __init__(self, emote: str, **kwargs: Any) -> None:
            self.email  =  email
            self.status_ = data['fortnite']['status']
            self.eid = emote
            self.boot_time = None
            self.booted_utc = None
            self.isready = False
            self.booting = False
            self.timer = None
            self.acceptinvite_interval = True
            self.stopcheck = False
            self.outfitlock = False
            self.backpacklock = False
            self.pickaxelock = False
            self.emotelock = False
            self.owner = []
            self.prevmessage = {}
            self.select = {}
            self.visual_members = []
            self.invitelist = []
            self.whisper = data['fortnite']['whisper']
            self.partychat = data['fortnite']['partychat']
            self.discord = data['discord']['discord']
            self.web = data['web']['web']
            self.whisperperfect = data['fortnite']['disablewhisperperfectly']
            self.partychatperfect = data['fortnite']['disablepartychatperfectly']
            self.discordperfect = data['discord']['disablediscordperfectly']
            self.joinmessageenable = data['fortnite']['joinmessageenable']
            self.randommessageenable = data['fortnite']['randommessageenable']
            self.outfitmimic = data['fortnite']['outfitmimic']
            self.backpackmimic = data['fortnite']['backpackmimic']
            self.pickaxemimic = data['fortnite']['pickaxemimic']
            self.emotemimic = data['fortnite']['emotemimic']
            self.outfitlock = data['fortnite']['outfitlock']
            self.backpacklock = data['fortnite']['backpacklock']
            self.pickaxelock = data['fortnite']['pickaxelock']
            self.emotelock = data['fortnite']['emotelock']
            self.acceptinvite = data['fortnite']['acceptinvite']
            self.acceptfriend = data['fortnite']['acceptfriend']

            super().__init__(**kwargs)

        def get_cache_user(self, user: str) -> Optional[fortnitepy.User]:
            if self.is_id(user):
                users = {i.id: i for i in cache_users.values()}
            else:
                users = cache_users
            return users.get(user)

        def add_cache(self, user: fortnitepy.user.UserBase) -> None:
            try:
                if isinstance(user, fortnitepy.user.UserBase) and user.id:
                    if isinstance(user, fortnitepy.User):
                        if user.display_name:
                            cache_users[user.display_name] = user
                    else:
                        user = self.get_user(user.id)
                        if user and user.display_name:
                            cache_users[user.display_name] = user
            except Exception:
                send(l('bot'),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        def inviteaccept(self) -> None:
            send(name(self.user),l("inviteaccept"),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            self.acceptinvite = True

        def inviteinterval(self) -> None:
            send(name(self.user),l("inviteinterval"),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            self.acceptinvite_interval = True

        def lock_check(self, author_id: str) -> bool:
            if author_id in [client.user.id for client in loadedclients]:
                return False
            elif author_id in [owner.id for owner in self.owner]:
                return False
            elif data['fortnite']['whitelist-ignorelock'] and author_id in whitelist:
                return False
            elif author_id in [owner.id for owner in dclient.owner]:
                return False
            elif data['discord']['whitelist-ignorelock'] and author_id in whitelist_:
                return False
            return True

        def is_most(self) -> None:
            name = self.user.display_name
            member_joined_at_most = [self.user.id, getattr(getattr(self.party,"me",None),"joined_at",datetime.datetime.now())]
            for member_ in self.party.members:
                self.add_cache(member_)
                if member_.id in [i.user.id for i in loadedclients]:
                    if member_.id != self.user.id:
                        name += f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most = [member_.id, getattr(member_, "joined_at", datetime.datetime.now())]
            if self.user.id == member_joined_at_most[0]:
                return name
            return None

        def get_client_data(self) -> defaultdict:
            var = defaultdict(lambda: None)
            if not self.isready:
                return var
            party = getattr(self,"party",None)
            if party:
                config = party.config
                var.update(
                    {
                        "party_id": party.id,
                        "party_size": party.member_count,
                        "party_max_size": config["max_size"]
                    }
                )
            var.update(
                {
                    "friend_count": len(self.friends),
                    "pending_count": len(self.pending_friends),
                    "incoming_pending_count": len(self.incoming_pending_friends),
                    "outgoing_pending_count": len(self.outgoing_pending_friends),
                    "block_count": len(self.blocked_users),
                    "display_name": self.user.display_name,
                    "id": self.user.id,
                    "boot_time": int(time.time() - self.boot_time),
                    "client": self,
                    "whitelist": whitelist,
                    "whitelist_": whitelist_,
                    "blacklist": blacklist,
                    "blacklist_": blacklist_
                }
            )
            return var

        async def change_status(self) -> None:
            var = defaultdict(lambda: None)

            var.update(self.get_client_data())
            var.update(
                {
                    "get_client_data": get_client_data,
                    "all_friend_count": sum([len(client_.friends) for client_ in clients]),
                    "all_pending_count": sum([len(client_.pending_friends) for client_ in clients]),
                    "all_incoming_pending_count": sum([len(client_.incoming_pending_friends) for client_ in clients]),
                    "all_outgoing_pending_count": sum([len(client_.outgoing_pending_friends) for client_ in clients]),
                    "all_block_count": sum([len(client_.blocked_users) for client_ in clients])
                }
            )

            if data['discord']['enabled'] and dclient.isready:
                var.update(
                    {
                        "guild_count": len(dclient.guilds),
                        "get_guild_member_count": get_guild_member_count,
                        "dclient": dclient
                    }
                )

            party = getattr(self,"party",None)
            if party:
                status = eval_format(self.status_,var)
                self.status = status
                status = self.party.construct_presence(status)
                try:
                    await self.send_presence(status)
                except Exception:
                    if data['loglevel'] == 'debug':
                        send(self.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            else:
                status = eval_format(self.status_,var)
                self.status = status
                try:
                    await self.send_presence(status)
                except Exception:
                    if data['loglevel'] == 'debug':
                        send(self.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def status_loop(self) -> None:
            while True:
                try:
                    await self.change_status()
                except Exception:
                    send(self.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await asyncio.sleep(30)

        async def invitation_accept(self, invitation: fortnitepy.ReceivedPartyInvitation) -> None:
            try:
                await invitation.accept()
            except fortnitepy.PartyError:
                if data['ingame-error']:
                    await invitation.sender.send(l("error_already_member_of_party"))
                if data['loglevel'] == 'debug':
                    send(name(self.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(name(self.user),l("already_member_of_party"),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
            except fortnitepy.HTTPException:
                if data['ingame-error']:
                    await invitation.sender.send(l("user_notfound"))
                if data['loglevel'] == 'debug':
                    send(self.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(self.user.display_name,l("user_notfound"),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
            except fortnitepy.Forbidden:
                if data['ingame-error']:
                    await invitation.sender.send(l("error_private_party"))
                if data['loglevel'] == 'debug':
                    send(self.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(self.user.display_name,l("error_private_party"),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
            except fortnitepy.HTTPException:
                if data['ingame-error']:
                    await invitation.sender.send(l("error_while_accepting_partyinvite"))
                if data['loglevel'] == 'debug':
                    send(self.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(self.user.display_name,l("error_while_accepting_partyinvite"),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                self.acceptinvite_interval = False
            except Exception:
                if data['ingame-error']:
                    await invitation.sender.send(l("error"))
                send(self.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if data['fortnite']['inviteinterval']:
                try:
                    self.timer.cancel()
                except Exception:
                    pass
                self.acceptinvite_interval = False
                self.timer = Timer(data['fortnite']['interval'], self.inviteinterval)
                self.timer.start()
            if data['loglevel'] == 'normal':
                send(name(self.user),l("accepted_invite_from", name(invitation.sender)),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            else:
                send(name(self.user),f'{l("accepted_invite_from2", f"{name(invitation.sender)} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id)}',add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')

        async def invitation_decline(self, invitation: fortnitepy.ReceivedPartyInvitation) -> None:
            if data['loglevel'] == 'normal':
                send(self.user.display_name,l("declined_invite_from", str(invitation.sender.display_name)),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            else:
                send(self.user.display_name,l("declined_invite_from2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            try:
                await invitation.decline()
            except fortnitepy.PartyError:
                if data['ingame-error']:
                    await invitation.sender.send(l("error_netcl_does_not_match"))
                if data['loglevel'] == 'debug':
                    send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(client.user.display_name,l("error_netcl_does_not_match"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
            except fortnitepy.HTTPException:
                if data['ingame-error']:
                    await invitation.sender.send(l("error_while_declining_invite"))
                if data['loglevel'] == 'debug':
                    send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(client.user.display_name,l("error_while_declining_invite"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
            except Exception:
                if data['ingame-error']:
                    await invitation.sender.send(l("error"))
                send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def invitation_decline_interval(self, invitation: fortnitepy.ReceivedPartyInvitation) -> None:
            await invitation.sender.send(l("declined_invite_interval3", str(data["fortnite"]["interval"])))
            if data['loglevel'] == 'normal':
                send(self.user.display_name,l("declined_invite_interval", str(invitation.sender.display_name), str(data["fortnite"]["interval"])),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            else:
                send(self.user.display_name,l("declined_invite_interval2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id, str(data["fortnite"]["interval"])),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            try:
                await invitation.decline()
            except fortnitepy.PartyError:
                if data['ingame-error']:
                    await invitation.sender.send(l("error_netcl_does_not_match"))
                if data['loglevel'] == 'debug':
                    send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(client.user.display_name,l("error_netcl_does_not_match"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
            except fortnitepy.HTTPException:
                if data['ingame-error']:
                    await invitation.sender.send(l("error_while_declining_invite"))
                if data['loglevel'] == 'debug':
                    send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(client.user.display_name,l("error_while_declining_invite"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
            except Exception:
                if data['ingame-error']:
                    await invitation.sender.send(l("error"))
                send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def invitation_decline_owner(self, invitation: fortnitepy.ReceivedPartyInvitation) -> None:
            await invitation.sender.send(l("declined_invite_owner3"))
            if data['loglevel'] == 'normal':
                send(self.user.display_name,l("declined_invite_owner", str(invitation.sender.display_name)),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            else:
                send(self.user.display_name,l("declined_invite_owner2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            try:
                await invitation.decline()
            except fortnitepy.PartyError:
                if data['ingame-error']:
                    await invitation.sender.send(l("error_netcl_does_not_match"))
                if data['loglevel'] == 'debug':
                    send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(client.user.display_name,l("error_netcl_does_not_match"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
            except fortnitepy.HTTPException:
                if data['ingame-error']:
                    await invitation.sender.send(l("error_while_declining_invite"))
                if data['loglevel'] == 'debug':
                    send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(client.user.display_name,l("error_while_declining_invite"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
            except Exception:
                if data['ingame-error']:
                    await invitation.sender.send(l("error"))
                send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def invitation_decline_whitelist(self, invitation: fortnitepy.ReceivedPartyInvitation) -> None:
            await invitation.sender.send(l("declined_invite_whitelist3"))
            if data['loglevel'] == 'normal':
                send(self.user.display_name,l("declined_invite_whitelist", str(invitation.sender.display_name)),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            else:
                send(self.user.display_name,l("declined_invite_whitelist2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            try:
                await invitation.decline()
            except fortnitepy.PartyError:
                if data['ingame-error']:
                    await invitation.sender.send(l("error_netcl_does_not_match"))
                if data['loglevel'] == 'debug':
                    send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(client.user.display_name,l("error_netcl_does_not_match"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
            except fortnitepy.HTTPException:
                if data['ingame-error']:
                    await invitation.sender.send(l("error_while_declining_invite"))
                if data['loglevel'] == 'debug':
                    send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(client.user.display_name,l("error_while_declining_invite"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
            except Exception:
                if data['ingame-error']:
                    await invitation.sender.send(l("error"))
                send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def change_asset(self, author_id: str, type_: str, id_: str, variants: Optional[list] = [], enlightenment: Optional[Union[tuple, list]] = None) -> None:
            if not enlightenment:
                enlightenment = None
            if type_ == "Outfit":
                if self.outfitlock and self.lock_check(author_id):
                    return False
                else:
                    if 'banner' in id_:
                        variants += self.party.me.create_variants(item="AthenaCharacter", profile_banner='ProfileBanner', enlightenment=enlightenment)
                    if not variants:
                        variants = None
                    await self.party.me.edit_and_keep(partial(self.party.me.set_outfit, asset=id_, variants=variants))
                    try:
                        if data['fortnite']['avatar_id'] == "{bot}":
                            self.set_avatar(fortnitepy.Avatar(asset=self.party.me.outfit, background_colors=data['fortnite']['avatar_color']))
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(name(self.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            elif type_ == "Back Bling":
                if self.backpacklock and self.lock_check(author_id):
                    return False
                else:
                    if 'banner' in id_:
                        variants += self.party.me.create_variants(item="AthenaBackpack", profile_banner='ProfileBanner', enlightenment=enlightenment)
                    await self.party.me.edit_and_keep(partial(self.party.me.set_backpack, asset=id_, variants=variants))
            elif type_ == "Pet":
                if self.backpacklock and self.lock_check(author_id):
                    return False
                else:
                    if 'banner' in id_:
                        variants += self.party.me.create_variants(item="AthenaBackpack", profile_banner='ProfileBanner', enlightenment=enlightenment)
                    await self.party.me.edit_and_keep(partial(self.party.me.set_pet, asset=id_, variants=variants))
            elif type_ == "Harvesting Tool":
                if self.pickaxelock and self.lock_check(author_id):
                    return False
                else:
                    if 'banner' in id_:
                        variants += self.party.me.create_variants(item="AthenaPickaxe", profile_banner='ProfileBanner', enlightenment=enlightenment)
                    await self.party.me.edit_and_keep(partial(self.party.me.set_pickaxe, asset=id_, variants=variants))
                    await self.party.me.set_emote("EID_IceKing")
            elif type_ == "Emote":
                if self.emotelock and self.lock_check(author_id):
                    return False
                else:
                    if member_asset(self.party.me, "emote") and member_asset(self.party.me, "emote").lower() == id_.lower():
                        await self.party.me.clear_emote()
                    if "holidaycracker" in id_.lower():
                        if id_ != '' and '.' not in id_:
                            id_ = ("AthenaDanceItemDefinition'/Game/Athena/Items/"
                                 "Cosmetics/Dances/HolidayCracker/{0}.{0}'".format(id_))
                        await self.party.me.set_emote(asset=id_)
                        self.eid = id_
                    elif id_.lower().endswith("papayacomms"):
                        if id_ != '' and '.' not in id_:
                            id_ = ("AthenaDanceItemDefinition'/Game/Athena/Items/"
                                 "Cosmetics/Dances/PapayaComms/{0}.{0}'".format(id_))
                        await self.party.me.set_emote(asset=id_)
                        self.eid = id_
                    else:
                        await self.party.me.set_emote(asset=id_)
                        self.eid = id_
            elif type_ == "Emoticon":
                if self.emotelock and self.lock_check(author_id):
                    return False
                else:
                    if member_asset(self.party.me, "emote") and member_asset(self.party.me, "emote").lower() == id_.lower():
                        await self.party.me.clear_emote()
                    id_ = f"/Game/Athena/Items/Cosmetics/Dances/Emoji/{id_}.{id_}"
                    await self.party.me.set_emote(asset=id_)
                    self.eid = id_
            elif type_ == "Toy":
                if self.emotelock and self.lock_check(author_id):
                    return False
                else:
                    if member_asset(self.party.me, "emote") and member_asset(self.party.me, "emote").lower() == id_.lower():
                        await self.party.me.clear_emote()
                    id_ = f"/Game/Athena/Items/Cosmetics/Toys/{id_}.{id_}"
                    await self.party.me.set_emote(asset=id_)
                    self.eid = id_
            return True

        async def disable_voice(self) -> None:
            if not self.party.me.leader:
                raise fortnitepy.Forbidden("You must be the party leader to perform this action.")
            prop = self.party.meta.set_voicechat_implementation('None')
            await client.party.patch(updated=prop)

        async def enable_voice(self) -> None:
            if not self.party.me.leader:
                raise fortnitepy.Forbidden("You must be the party leader to perform this action.")
            prop = self.party.meta.set_voicechat_implementation('VivoxVoiceChat')
            await client.party.patch(updated=prop)

        async def hide(self, member_id: Optional[str] = None) -> None:
            if not self.party.me.leader:
                raise fortnitepy.Forbidden("You must be the party leader to perform this action.")
            real_members = self.party.meta.squad_assignments
            if not member_id:
                num = 0
                squad_assignments = [{"memberId": self.user.id, "absoluteMemberIdx": num}]
                num += 1
                if data['fortnite']['show-owner']:
                    for owner in self.owner:
                        if self.party.get_member(owner.id):
                            squad_assignments.append({"memberId": owner.id, "absoluteMemberIdx": num})
                            num += 1
                if data['fortnite']['show-whitelist']:
                    for whitelistuser in whitelist:
                        if self.party.get_member(whitelistuser):
                            squad_assignments.append({"memberId": whitelistuser, "absoluteMemberIdx": num})
                            num += 1
                if data['fortnite']['show-bot']:
                    for botuser in (otherbotlist + [i.user.id for i in loadedclients]):
                        if self.party.get_member(botuser):
                            squad_assignments.append({"memberId": botuser, "absoluteMemberIdx": num})
                            num += 1
            else:
                member = self.party.get_member(member_id)
                if not member:
                    raise fortnitepy.NotFound("This member is not a part of this party.")
                squad_assignments = self.visual_members
                for squad in squad_assignments:
                    if squad["memberId"] == member.id:
                        squad_assignments.remove(squad)
            self.visual_members = squad_assignments
            prop = self.party.meta.set_squad_assignments(squad_assignments)
            await self.party.patch(updated=prop)
            self.party.meta.set_squad_assignments(real_members)

        async def show(self, member_id: Optional[str] = None) -> None:
            if not self.party.me.leader:
                raise fortnitepy.Forbidden("You must be the party leader to perform this action.")
            real_members = self.party.meta.squad_assignments
            if not member_id:
                member_indexes = [member.position for member in self.party.members if isinstance(member.position,int)]
                available_indexes = [num for num in range(15) if num not in member_indexes]

                num = 0
                squad_assignments = []
                for member in self.party.members:
                    if isinstance(member.position,int):
                        squad_assignments.append(
                            {
                                "memberId": member.id,
                                "absoluteMemberIdx": member.position
                            }
                        )
                    else:
                        squad_assignments.append(
                            {
                                "memberId": member.id,
                                "absoluteMemberIdx": available_indexes[num]
                            }
                        )
                        num += 1
            else:
                squad_assignments = self.visual_members
                squad_members = [member["memberId"] for member in squad_assignments]
                member_indexes = [member["absoluteMemberIdx"] for member in squad_assignments]
                available_indexes = [num for num in range(15) if num not in member_indexes]
                member = self.party.get_member(member_id)
                if not member:
                    raise fortnitepy.NotFound("This member is not a part of this party.")
                if member.id not in squad_members:
                    squad_assignments.append({"memberId": member.id, "absoluteMemberIdx": available_indexes[0]})
            self.visual_members = squad_assignments
            prop = self.party.meta.set_squad_assignments(squad_assignments)
            await self.party.patch(updated=prop)
            self.party.meta.set_squad_assignments(real_members)

        async def party_member_outfit_change(self, member: fortnitepy.PartyMember) -> None:
            display_name = name(self.user)
            if member.id == self.user.id:
                return
            flag = False
            if isinstance(self.outfitmimic,bool) and self.outfitmimic:
                if (member.id in (otherbotlist + [i.user.id for i in loadedclients]) and data['fortnite']['mimic-ignorebot']):
                    return
                flag = True
            elif isinstance(self.outfitmimic,str) and member.id == self.outfitmimic:
                flag = True
            display_name_ = self.is_most()
            if display_name_ and member_asset(member,"outfit"):
                send(display_name_,f"CID: {member_asset(member,'outfit')}")
            if flag:
                if not member_asset(member,"outfit"):
                    try:
                        await self.change_asset(self.user.id, "Outfit", "")
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                else:
                    try:
                        await self.change_asset(self.user.id, "Outfit", member_asset(member,"outfit"), member.outfit_variants, member.enlightenments)
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def party_member_backpack_change(self, member: fortnitepy.PartyMember) -> None:
            display_name = name(self.user)
            if member.id == self.user.id:
                return
            flag = False
            if isinstance(self.backpackmimic,bool) and self.backpackmimic:
                if (member.id in (otherbotlist + [i.user.id for i in loadedclients]) and data['fortnite']['mimic-ignorebot']):
                    return
                flag = True
            elif isinstance(self.backpackmimic,str) and member.id == self.backpackmimic:
                flag = True
            display_name_ = self.is_most()
            if display_name_ and member_asset(member,"backpack"):
                send(display_name_,f"BID: {member_asset(member,'backpack')}")
            if flag:
                if not member_asset(member,"backpack"):
                    try:
                        await self.change_asset(self.user.id, "Back Bling", "")
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                else:
                    try:
                        type_ = convert_to_type(member_asset(member,'backpack'))
                        await self.change_asset(self.user.id, type_, member_asset(member,"backpack"), member.backpack_variants, member.enlightenments)
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def party_member_pickaxe_change(self, member: fortnitepy.PartyMember) -> None:
            display_name = name(self.user)
            if member.id == self.user.id:
                return
            flag = False
            if isinstance(self.pickaxemimic,bool) and self.pickaxemimic:
                if (member.id in (otherbotlist + [i.user.id for i in loadedclients]) and data['fortnite']['mimic-ignorebot']):
                    return
                flag = True
            elif isinstance(self.pickaxemimic,str) and member.id == self.pickaxemimic:
                flag = True
            display_name_ = self.is_most()
            if display_name_ and member_asset(member,"pickaxe"):
                send(display_name_,f"Pickaxe_ID: {member_asset(member,'pickaxe')}")
            if flag:
                if not member_asset(member,"pickaxe"):
                    try:
                        await self.change_asset(self.user.id, "Harvesting Tool", "")
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                else:
                    try:
                        await self.change_asset(self.user.id, "Harvesting Tool", member_asset(member,"pickaxe"), member.pickaxe_variants)
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def party_member_emote_change(self, member: fortnitepy.PartyMember) -> None:
            display_name = name(self.user)
            if member.id == self.user.id:
                return
            flag = False
            if isinstance(self.emotemimic,bool) and self.emotemimic:
                if (member.id in (otherbotlist + [i.user.id for i in loadedclients]) and data['fortnite']['mimic-ignorebot']):
                    return
                flag = True
            elif isinstance(self.emotemimic,str) and member.id == self.emotemimic:
                flag = True
            display_name_ = self.is_most()
            if display_name_ and member_asset(member,"emote"):
                send(display_name_,f"EID: {member_asset(member,'emote')}")
            if flag:
                if not member_asset(member,"emote"):
                    try:
                        await self.change_asset(self.user.id, "Emote", "")
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                else:
                    try:
                        type_ = convert_to_type(member_asset(member,"emote"))
                        await self.change_asset(self.user.id, type_, member_asset(member,"emote"))
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        #Events
        async def event_device_auth_generate(self, details: dict, email: str) -> None:
            store_device_auth_details(email, details)

        async def event_ready(self) -> None:
            global first_boot

            loop = asyncio.get_event_loop()
            self.boot_time = time.time()
            self.booted_utc = datetime.datetime.utcnow()
            display_name = name(self.user)
            send(display_name,f'{l("login")}: {display_name}',green,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            flag = False
            if first_boot:
                first_boot = False
                flag = True
            self.isready = True
            self.booting = False
            if not self.visual_members:
                if self.party:
                    self.visual_members = self.party.meta.squad_assignments
                else:
                    self.visual_members = [{"memberId": self.user.id, "absoluteMemberIdx": 0}]
            loadedclients.append(self)
            client_name[self.user.display_name] = self
            self.add_cache(self.user)
            for user in [list(self.friends) + list(self.pending_friends) + list(self.blocked_users)]:
                self.add_cache(user)
            loop.create_task(self.status_loop())
            try:
                if data['fortnite']['avatar_id'] == "{bot}":
                    self.set_avatar(fortnitepy.Avatar(asset=self.party.me.outfit, background_colors=data['fortnite']['avatar_color']))
                else:
                    self.set_avatar(fortnitepy.Avatar(asset=data['fortnite']['avatar_id'].format(bot=self.party.me.outfit), background_colors=data['fortnite']['avatar_color']))
            except Exception:
                if data['loglevel'] == 'debug':
                    send(name(self.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

            self.owner = []
            for owner in data['fortnite']['owner']:
                user = self.get_user(owner) or self.get_cache_user(owner)
                if not user:
                    try:
                        user = await self.fetch_user(owner)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    except Exception:
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                if not user:
                    send(display_name,l("owner_notfound",owner),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                else:
                    self.add_cache(user)
                    friend = self.get_friend(user.id)
                    if not friend:
                        send(display_name,l("not_friend_with_owner",commands["reload"]),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        if data['fortnite']['addfriend'] and not self.is_pending(user.id):
                            try:
                                await self.add_friend(user.id)
                            except fortnitepy.HTTPException:
                                if data['loglevel'] == 'debug':
                                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                                send(display_name,l("error_while_sending_friendrequest"),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                            except Exception:
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    else:
                        self.owner.append(friend)
                        send(display_name,f'{l("owner")}: {name(friend)}',green,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            if self.owner and data['fortnite']['click_invite']:
                for owner in self.owner:
                    await owner.send(l("click_invite"))

            async def _(listuser: str) -> None:
                user = self.get_user(listuser) or self.get_cache_user(listuser)
                if not user:
                    try:
                        user = await self.fetch_user(listuser)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                if not user:
                    send(display_name,l("invitelist_user_notfound",listuser),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                else:
                    self.add_cache(user)
                    friend = self.get_friend(user.id)
                    if not friend:
                        send(display_name,l("not_friend_with_inviteuser",listuser,commands["reload"]),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        if data['fortnite']['addfriend'] and not self.is_pending(user.id) and user.id != self.user.id:
                            try:
                                await self.add_friend(user.id)
                            except fortnitepy.HTTPException:
                                if data['loglevel'] == 'debug':
                                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                                send(display_name,l("error_while_sending_friendrequest"),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    else:
                        self.invitelist.append(friend.id)
            try:
                await asyncio.gather(*[_(listuser) for listuser in data['fortnite']['invitelist']])
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if data['loglevel'] == "debug":
                send(display_name,f'invitelist {self.invitelist}',yellow,add_d=lambda x:f'```\n{x}\n```')

            if data['fortnite']['acceptfriend']:
                async def _(pending: fortnitepy.IncomingPendingFriend) -> None:
                    if self.acceptfriend is True:
                        try:
                            await pending.accept()
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            try:
                                await pending.decline()
                            except fortnitepy.HTTPException:
                                if data['loglevel'] == 'debug':
                                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    elif self.acceptfriend is False:
                        try:
                            await pending.decline()
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                try:
                    await asyncio.gather(*[_(pending) for pending in client.incoming_pending_friends])
                except Exception:
                    data["discord"]["enabled"] = False
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

            if flag:
                lists = {
                    "blacklist": "blacklist",
                    "whitelist": "whitelist",
                    "otherbotlist": "botlist"
                }
                async def _(listuser: str) -> None:
                    user = self.get_user(listuser) or self.get_cache_user(listuser)
                    if not user:
                        try:
                            user = await self.fetch_user(listuser)
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        except Exception:
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    if not user:
                        send(display_name,l(f"{data_}_user_notfound",listuser),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    else:
                        self.add_cache(user)
                        if data_ == "blacklist" and data["fortnite"]["blacklist-autoblock"]:
                            try:
                                await user.block()
                            except Exception:
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        globals()[list_].append(user.id)

                for list_,data_ in lists.items():
                    try:
                        await asyncio.gather(*[_(listuser) for listuser in data['fortnite'][list_]])
                    except Exception:
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    if data['loglevel'] == "debug":
                        send(display_name,f"fortnite {data_}list {globals()[list_]}",yellow,add_d=lambda x:f'```\n{x}\n```')

                lists = [
                    "outfitmimic",
                    "backpackmimic",
                    "pickaxemimic",
                    "emotemimic"
                ]
                async def _(mimic: str) -> None:
                    if isinstance(data['fortnite'][mimic],str):
                        user = self.get_user(mimic) or self.get_cache_user(mimic)
                        if not user:
                            try:
                                user = await self.fetch_user(data['fortnite'][mimic])
                            except fortnitepy.HTTPException:
                                if data['loglevel'] == 'debug':
                                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                                send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                            except Exception:
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        if not user:
                            send(display_name,l(f"{mimic}_user_notfound",data['fortnite'][mimic]),red,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        else:
                            self.add_cache(user)
                            setattr(self,mimic,user.id)
                            if data['loglevel'] == "debug":
                                send(display_name,f"{mimic} {getattr(self,mimic)}",yellow,add_d=lambda x:f'```\n{x}\n```')
                try:
                    await asyncio.gather(*[_(mimic) for mimic in lists])
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

                if data['discord']['enabled']:
                    try:
                        await dclient.start(data['discord']['token'])
                    except Exception:
                        data["discord"]["enabled"] = False
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def event_before_close(self) -> None:
            self.isready = False
            self.boot_time = None
            send(name(self.user),f'{l("closing")}: {self.user.display_name}',green,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')

        async def event_restart(self) -> None:
            self.boot_time = time.time()
            send(name(self.user),l("relogin", self.user.display_name),green,add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')

        async def event_party_invite(self, invitation: fortnitepy.ReceivedPartyInvitation) -> None:
            if not self.isready or not invitation:
                return
            display_name = name(self.user)
            self.add_cache(invitation.sender)
            if invitation.sender.id in blacklist and data['fortnite']['blacklist-declineinvite']:
                return
            if invitation.sender.id in [owner.id for owner in self.owner]:
                await self.invitation_accept(invitation)
                return
            if invitation.sender.id in whitelist and data['fortnite']['whitelist-allowinvite']:
                await self.invitation_accept(invitation)
                return
            if data['loglevel'] == 'normal':
                send(display_name,l("invite_from",name(invitation.sender)),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            else:
                send(display_name,l("invite_from2",f'{name(invitation.sender)} [{platform_to_str(invitation.sender.platform)}]',invitation.party.id),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            for owner in self.owner:
                if self.party.get_member(owner.id) and data['fortnite']['invite-ownerdecline']:
                    await self.invitation_decline_owner(invitation)
                    return
            if True in [member.id in whitelist for member in self.party.members] and data['fortnite']['whitelist-declineinvite']:
                await self.invitation_decline_whitelist(invitation)
            elif not self.acceptinvite:
                await self.invitation_decline(invitation)
            elif not self.acceptinvite_interval:
                await self.invitation_decline_interval(invitation)
            else:
                await self.invitation_accept(invitation)

        async def event_friend_request(self, request: Union[fortnitepy.IncomingPendingFriend, fortnitepy.OutgoingPendingFriend]) -> None:
            if not self.isready or not request:
                return
            display_name = name(self.user)
            self.add_cache(request)
            if request.outgoing:
                send(display_name,l("friend_request_to",name(request)),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
                return
            send(display_name,l("friend_request_from",name(request)),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            if self.acceptfriend is True:
                try:
                    await request.accept()
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(display_name,l("error_while_accepting_friendrequest"),red,add_d=lambda x:f'>>> {x}')
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            elif self.acceptfriend is False:
                try:
                    await request.decline()
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(display_name,l("error_while_declining_friendrequest"),red,add_d=lambda x:f'>>> {x}')
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(display_name,l("friend_request_decline",name(request)),red,add_d=lambda x:f'>>> {x}')

        async def event_friend_add(self, friend: fortnitepy.Friend) -> None:
            if not self.isready or not friend:
                return
            display_name = name(self.user)
            self.add_cache(friend)
            if friend.outgoing:
                send(display_name,l("friend_accept",name(friend)),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            else:
                send(display_name,l("friend_add",name(friend)),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')

        async def event_friend_remove(self, friend: fortnitepy.Friend) -> None:
            if not self.isready or not friend:
                return
            display_name = name(self.user)
            self.add_cache(friend)
            if data['loglevel'] == 'normal':
                send(display_name,l("friend_remove",name(friend)),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
            else:
                send(display_name,l("friend_remove",f'{name(friend)} [{platform_to_str(friend.platform)}]'),add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')

        async def event_party_member_join(self, member: fortnitepy.PartyMember) -> None:
            try:
                if member.id == self.user.id:
                    self.visual_members = self.party.meta.squad_assignments
                else:
                    self.visual_members.append({"memberId": member.id, "absoluteMemberIdx": member.position})
            except Exception:
                if data['loglevel'] == 'debug':
                    send(name(self.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if not self.isready or not member:
                return
            self.add_cache(member)
            display_name = name(self.user)
            display_name_ = self.is_most()
            loop = asyncio.get_event_loop()
            loop.create_task(self.change_status())

            if self.party.me.leader and (data['fortnite']['hide-user'] or data['fortnite']['hide-blacklist']):
                async def _() -> None:
                    nonlocal member
                    try:
                        await asyncio.sleep(0.5)
                        if data['fortnite']['hide-user']:
                            if (not member.id in [owner.id for owner in self.owner] and data['fortnite']['show-owner']
                                and not (member.id in whitelist and data['fortnite']['show-whitelist'])
                                and not (member.id in (otherbotlist + [i.user.id for i in loadedclients]) and data['fortnite']['show-bot'])
                                and member.id != self.user.id):
                                for squad in self.visual_members:
                                    if squad["memberId"] == member.id:
                                        self.visual_members.remove(squad)
                        elif data['fortnite']['hide-blacklist']:
                            if member.id in blacklist:
                                for squad in self.visual_members:
                                    if squad["memberId"] == member.id:
                                        self.visual_members.remove(squad)
                        real_members = self.party.meta.squad_assignments
                        prop = self.party.meta.set_squad_assignments(self.visual_members)
                        await self.party.patch(updated=prop)
                        self.party.meta.set_squad_assignments(real_members)
                        await asyncio.sleep(2)
                        self.party.meta.set_squad_assignments(real_members)
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(name(self.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                loop.create_task(_())
            if display_name_:
                if data['loglevel'] == 'normal':
                    send(display_name_,l('party_member_joined',name(member),member.party.member_count),magenta,add_p=lambda x:f'[{now()}] [{l("party")}] [{display_name_}] {x}')
                else:
                    send(display_name_,l('party_member_joined',f'{name(member)} [{platform_to_str(member.platform)}/{member.input}]',member.party.member_count),magenta,add_p=lambda x:f'[{now()}] [{l("party")}/{self.party.id}] [{display_name_}] {x}')
            if member.id in blacklist and self.party.me.leader:
                if data['fortnite']['blacklist-autokick']:
                    try:
                        await member.kick()
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                elif data['fortnite']['blacklist-autochatban']:
                    try:
                        await member.chatban()
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

            if data['fortnite']['addfriend']:
                for member_ in member.party.members:
                    try:
                        if not self.has_friend(member_.id) and not self.is_pending(member_.id) and not self.is_blocked(member_.id) and member_.id != self.user.id:
                            await self.add_friend(member_.id)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

            if self.joinmessageenable:
                var = defaultdict(lambda: None)
                var.update(self.get_client_data())
                var.update(
                    {
                        "get_client_data": get_client_data,
                        "all_friend_count": sum([len(client_.friends) for client_ in clients]),
                        "all_pending_count": sum([len(client_.pending_friends) for client_ in clients]),
                        "all_block_count": sum([len(client_.blocked_users) for client_ in clients]),
                        "member_display_name": member.display_name,
                        "member_id": member.id,
                        "member": member
                    }
                )
                try:
                    mes = eval_format(data['fortnite']['joinmessage'],var)
                    await self.party.send(mes)
                except Exception:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if self.randommessageenable:
                var = defaultdict(lambda: None)
                var.update(self.get_client_data())
                var.update(
                    {
                        "get_client_data": get_client_data,
                        "all_friend_count": sum([len(client_.friends) for client_ in clients]),
                        "all_pending_count": sum([len(client_.pending_friends) for client_ in clients]),
                        "all_block_count": sum([len(client_.blocked_users) for client_ in clients]),
                        "member_display_name": member.display_name,
                        "member_id": member.id,
                        "member": member
                    }
                )
                try:
                    randommessage = random.choice(data['fortnite']['randommessage'])
                    mes = mes = eval_format(randommessage,var)
                    send(display_name,f'{l("random_message")}: {mes}',add_p=lambda x:f'[{now()}] [{self.user.display_name}] {x}')
                    await self.party.send(mes)
                except Exception:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

            await asyncio.sleep(0.1)

            if data["fortnite"]["joinemote"]:
                try:
                    await self.change_asset(self.user.id, "Emote", self.eid)
                except Exception:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

            if self.party.leader.id == self.user.id:
                try:
                    await self.party.set_playlist(data['fortnite']['playlist'])
                    await self.party.set_privacy(data['fortnite']['privacy'].value)
                    if data["fortnite"]["disable_voice"]:
                        await self.disable_voice()
                except fortnitepy.Forbidden:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def event_party_member_leave(self, member: fortnitepy.PartyMember) -> None:
            try:
                if member.id == self.user.id:
                    self.visual_members = []
                else:
                    for squad in self.visual_members:
                        if squad["memberId"] == member.id:
                            self.visual_members.remove(squad)
            except Exception:
                if data['loglevel'] == 'debug':
                    send(name(self.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if not self.isready or not member:
                return
            self.add_cache(member)
            display_name = name(self.user)
            display_name_ = self.is_most()
            loop = asyncio.get_event_loop()
            loop.create_task(self.change_status())

            if self.party.me.leader and (data['fortnite']['hide-user'] or data['fortnite']['hide-blacklist']):
                async def _() -> None:
                    nonlocal member
                    try:
                        await asyncio.sleep(0.5)
                        real_members = self.party.meta.squad_assignments
                        prop = self.party.meta.set_squad_assignments(self.visual_members)
                        await self.party.patch(updated=prop)
                        self.party.meta.set_squad_assignments(real_members)
                        await asyncio.sleep(2)
                        self.party.meta.set_squad_assignments(real_members)
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(name(self.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                loop.create_task(_())
            if display_name_:
                if data['loglevel'] == 'normal':
                    send(display_name_,l("party_member_left",name(member),member.party.member_count),magenta,lambda x:f'[{now()}] [{l("party")}] [{display_name_}] {x}')
                else:
                    send(display_name_,l("party_member_left",f'{name(member)} [{platform_to_str(member.platform)}/{member.input}]',member.party.member_count),magenta,lambda x:f'[{now()}] [{l("party")}] [{display_name_}] {x}')

            if data['fortnite']['addfriend']:
                for member in member.party.members:
                    if not self.has_friend(member.id) and not self.is_pending(member.id) and not self.is_blocked(member.id) and member.id != self.user.id:
                        try:
                            await self.add_friend(member.id)
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            continue
                        except Exception:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def event_party_member_confirm(self, confirmation: fortnitepy.PartyJoinConfirmation) -> None:
            if not self.isready or not confirmation:
                return
            self.add_cache(confirmation.user)
            display_name = name(self.user)
            display_name_ = self.is_most()
            if display_name_ and data['loglevel'] != 'normal':
                send(display_name_,l("party_member_request",name(confirmation.user)),magenta,add_p=lambda x:f'[{now()}] [{l("party")}/{self.party.id}] [{display_name_}] {x}')

            if data['fortnite']['blacklist-autokick'] and confirmation.user.id in blacklist:
                try:
                    await confirmation.reject()
                except fortnitepy.HTTPException:
                    if data['loglevel'] == "debug":
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(display_name,l("error_while_declining_partyrequest"),red,add_d=lambda x:f'>>> {x}')
            else:
                try:
                    await confirmation.confirm()
                except fortnitepy.HTTPException:
                    if data['loglevel'] == "debug":
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(display_name,l("error_while_accepting_partyrequest"),red,add_d=lambda x:f'>>> {x}')

        async def event_party_member_kick(self, member: fortnitepy.PartyMember) -> None:
            try:
                if member.id == self.user.id:
                    self.visual_members = []
                else:
                    for squad in self.visual_members:
                        if squad["memberId"] == member.id:
                            self.visual_members.remove(squad)
            except Exception:
                if data['loglevel'] == 'debug':
                    send(name(self.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if not self.isready or not member:
                return
            self.add_cache(member)
            if self.party.me.leader and member.id != self.user.id and (data['fortnite']['hide-user'] or data['fortnite']['hide-blacklist']):
                async def _() -> None:
                    nonlocal member
                    try:
                        await asyncio.sleep(0.5)
                        real_members = self.party.meta.squad_assignments
                        prop = self.party.meta.set_squad_assignments(self.visual_members)
                        await self.party.patch(updated=prop)
                        self.party.meta.set_squad_assignments(real_members)
                        await asyncio.sleep(2)
                        self.party.meta.set_squad_assignments(real_members)
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(name(self.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                loop.create_task(_())
            display_name_ = self.is_most()
            if display_name_:
                if data['loglevel'] == 'normal':
                    send(display_name_,l("party_member_kick",name(member.party.leader),name(member),member.party.member_count),magenta,add_p=lambda x:f'[{now()}] [{l("party")}] [{display_name_}] {x}')
                else:
                    send(display_name_,l("party_member_kick",f'{name(member.party.leader)} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}]',f'{name(member)} [{platform_to_str(member.platform)}/{member.input}]',member.party.member_count),magenta,add_p=lambda x:f'[{now()}] [{l("party")}/{self.party.id}] [{display_name_}] {x}')

        async def event_party_member_promote(self, old_leader: fortnitepy.PartyMember, new_leader: fortnitepy.PartyMember) -> None:
            if not self.isready or not old_leader or not new_leader:
                return
            self.add_cache(old_leader)
            self.add_cache(new_leader)
            display_name = name(self.user)
            display_name_ = self.is_most()
            try:
                if new_leader.id == self.user.id:
                    if data['fortnite']['hide-user']:
                        await self.hide()
            except Exception:
                if data['loglevel'] == 'debug':
                    send(name(self.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if display_name_:
                if data['loglevel'] == 'normal':
                    send(display_name_,l("party_member_promote",name(old_leader),name(new_leader)),magenta,add_p=lambda x:f'[{now()}] [{l("party")}] [{display_name_}] {x}')
                else:
                    send(display_name_,l("party_member_promote",f'{name(old_leader)} [{platform_to_str(old_leader.platform)}/{old_leader.input}]',f'{name(new_leader)} [{platform_to_str(new_leader.platform)}/{new_leader.input}]'),magenta,add_p=lambda x:f'[{now()}] [{l("party")}/{self.party.id}] [{display_name_}] {x}')

            if new_leader.id == self.user.id:
                try:
                    await self.party.set_playlist(data['fortnite']['playlist'])
                    await client.party.set_privacy(data['fortnite']['privacy'].value)
                    if data["fortnite"]["disable_voice"]:
                        await self.disable_voice()
                    for member in self.party.members:
                        if member.id in blacklist:
                            if data['fortnite']['blacklist-autokick']:
                                try:
                                    await member.kick()
                                except Exception:
                                    if data['loglevel'] == 'debug':
                                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            elif data['fortnite']['blacklist-autochatban']:
                                try:
                                    await member.chatban()
                                except Exception:
                                    if data['loglevel'] == 'debug':
                                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                except fortnitepy.Forbidden:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def event_party_playlist_change(self, party: fortnitepy.ClientParty, before: tuple, after: tuple) -> None:
            display_name_ = self.is_most()
            if display_name_ and data['loglevel'] != 'normal':
                send(display_name_,after[0])

        async def event_party_member_update(self, member: fortnitepy.PartyMember) -> None:
            if not self.isready or not member:
                return
            self.add_cache(member)
            display_name = name(self.user)
            display_name_ = self.is_most()
            if display_name_ and data['loglevel'] != 'normal':
                send(display_name_,l("party_member_update", f"{name(member)} [{platform_to_str(member.platform)}/{member.input}]"),magenta,add_p=lambda x:f'[{now()}] [{l("party")}/{self.party.id}] [{display_name_}] {x}')
            if member.id == self.user.id:
                return
            if member.id in blacklist and self.party.me.leader:
                if data['fortnite']['blacklist-autokick']:
                    try:
                        await member.kick()
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                elif data['fortnite']['blacklist-autochatban']:
                    try:
                        await member.chatban()
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def event_party_member_outfit_change(self, member: fortnitepy.PartyMember, before: str, after: str) -> None:
            if not self.isready or not member:
                return
            await self.party_member_outfit_change(member)

        async def event_party_member_backpack_change(self, member: fortnitepy.PartyMember, before: str, after: str) -> None:
            if not self.isready or not member:
                return
            await self.party_member_backpack_change(member)

        async def event_party_member_pet_change(self, member: fortnitepy.PartyMember, before: str, after: str) -> None:
            if not self.isready or not member:
                return
            await self.party_member_backpack_change(member)

        async def event_party_member_pickaxe_change(self, member: fortnitepy.PartyMember, before: str, after: str) -> None:
            if not self.isready or not member:
                return
            await self.party_member_pickaxe_change(member)

        async def event_party_member_emote_change(self, member: fortnitepy.PartyMember, before: str, after: str) -> None:
            if not self.isready or not member:
                return
            await self.party_member_emote_change(member)

        async def event_party_member_emoji_change(self, member: fortnitepy.PartyMember, before: str, after: str) -> None:
            if not self.isready or not member:
                return
            await self.party_member_emote_change(member)

        async def event_party_member_zombie(self, member: fortnitepy.PartyMember) -> None:
            if not self.isready or not member:
                return
            self.add_cache(member)
            display_name = name(self.user)
            display_name_ = self.is_most()
            if display_name_:
                if data['loglevel'] == 'normal':
                    send(display_name_,l("party_member_disconnect",name(member)),magenta,add_p=lambda x:f'[{now()}] [{l("party")}] [{display_name_}] {x}')
                else:
                    send(display_name_,l("party_member_disconnect",f'{name(member)} [{platform_to_str(member.platform)}/{member.input}]'),magenta,add_p=lambda x:f'[{now()}] [{l("party")}/{self.party.id}] [{display_name_}] {x}')

            if self.party.me.leader:
                try:
                    await member.kick()
                except Exception:
                    if data['loglevel'] == "debug":
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def event_party_member_chatban(self, member: fortnitepy.PartyMember, reason: Optional[str]) -> None:
            if not self.isready or not member:
                return
            self.add_cache(member)
            display_name_ = self.is_most()
            if display_name_:
                if data['loglevel'] == 'normal':
                    if not reason:
                        send(display_name_,l("party_member_chatban",name(member.party.leader),name(member)),magenta,add_p=lambda x:f'[{now()}] [{l("party")}] [{display_name_}] {x}')
                    else:
                        send(display_name_,l("party_member_chatban2",name(member.party.leader),name(member),reason),magenta,add_p=lambda x:f'[{now()}] [{l("party")}] [{display_name_}] {x}')
                else:
                    if not reason:
                        send(display_name_,l("party_member_chatban",name(member.party.leader),name(member)),magenta,add_p=lambda x:f'[{now()}] [{l("party")}/{self.party.id}] [{display_name_}] {x}')
                    else:
                        send(display_name_,l("party_member_chatban2",f'{name(member.party.leader)} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}]',f'{name(member)} [{platform_to_str(member.platform)}/{member.input}]',reason),magenta,add_p=lambda x:f'[{now()}] [{l("party")}/{self.party.id}] [{display_name_}] {x}')

        async def event_party_update(self, party: fortnitepy.Party) -> None:
            if not self.isready or not party:
                return
            display_name_ = self.is_most()
            if display_name_ and data['loglevel'] != 'normal':
                send(display_name_,l("party_update"),magenta,add_p=lambda x:f'[{now()}] [{l("party")}/{self.party.id}] [{display_name_}] {x}')

        async def event_friend_message(self, message: fortnitepy.FriendMessage) -> None:
            await process_command(message)

        async def event_party_message(self, message: fortnitepy.PartyMessage) -> None:
            await process_command(message)


if True: #Functions
    def now() -> str:
        return datetime.datetime.now().strftime("%H:%M:%S")


if True: #Functions
    def now1() -> str:
        return datetime.datetime.now().strftime("%Y")

if True: #Functions
    def now2() -> str:
        return datetime.datetime.now().strftime("%m")

if True: #Functions
    def now3() -> str:
        return datetime.datetime.now().strftime("%d")

if True: #Functions
    def now4() -> str:
        return datetime.datetime.now().strftime("%H")

if True: #Functions
    def now5() -> str:
        return datetime.datetime.now().strftime("%M")

if True: #Functions
    def now6() -> str:
        return datetime.datetime.now().strftime("%S")

if True: #Functions
    def now7() -> str:
        return datetime.datetime.now().strftime("%A") #Monday(月曜日)

if True: #Functions
    def now8() -> str:
        return datetime.datetime.now().strftime("%a") #Mon(月曜日)


    def l(key: str, *args: Any, **kwargs: Any) -> Optional[str]:
        text = localize.get(key)
        if text:
            return text.format(*args, **kwargs)
        else:
            return None

    def name(user: Union[fortnitepy.user.UserBase, discord.user.User, WebUser]) -> str:
        if data['loglevel'] == 'normal':
            return user.display_name
        else:
            return f"{user.display_name} / {user.id}"

    def render_template(file_: str, **kwargs: Any) -> str:
        template = env.get_template(file_)
        return sanic.response.html(template.render(**kwargs))

    def dprint() -> None:
        text_max = 1990
        while True:
            if data['discord-log']:
                if data['skip-if-overflow'] and len(storedlogs) >= 50:
                    storedlogs.clear()
                for num,log in enumerate(storedlogs):
                    try:
                        username = list(log.keys())[0]
                        content = list(log.values())[0]
                        if len(content) > text_max:
                            if data["omit-over2000"]:
                                text = content[:text_max] + "..."
                                res = requests.post(
                                    data['webhook'],
                                    json={
                                        'username': username,
                                        'content': text
                                    }
                                )
                            else:
                                text = [content[i:i+text_max] for i in range(0, len(content), text_max)]
                                for text_ in text:
                                    res = requests.post(
                                        data['webhook'],
                                        json={
                                            'username': username,
                                            'content': text_
                                        }
                                    )
                                    if res.status_code == 429:
                                        break
                                else:
                                    continue
                                break
                        else:
                            res = requests.post(
                                data['webhook'],
                                json={
                                    'username': username,
                                    'content': content
                                }
                            )
                        if res.status_code == 204:
                            storedlogs.pop(num)
                        if res.status_code == 429:
                            break
                    except TypeError:
                        if data['loglevel'] =='debug':
                            print(red(traceback.format_exc()))
                        try:
                            storedlogs.pop(num)
                        except Exception:
                            pass
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        print(red(f"{username}: {content} の送信中にエラーが発生しました"))
                        continue
                time.sleep(5)

    def dstore(username: str, content: Any) -> None:
        if data['discord-log']:
            if data['hide-email']:
                for email in data['fortnite']['email']:
                    content = content.replace(email,len(email)*"X")
            if data['hide-token']:
                for token in data['discord']['token'].split(','):
                    content = content.replace(token,len(token)*"X")
            if data['hide-webhook']:
                for webhook in data['webhook'].split(','):
                    content = content.replace(webhook,len(webhook)*"X")
            if len(storedlogs) > 0:
                if list(storedlogs[len(storedlogs)-1].keys())[0] == username:
                    storedlogs[len(storedlogs)-1][username] += f'\n{content}'
                else:
                    storedlogs.append({username: content})
            else:
                storedlogs.append({username: content})

    def send(user_name: str, content: Any, color: Optional[Callable] = None, add_p: Optional[Callable] = None, add_d: Optional[Callable] = None) -> Optional[str]:
        content = str(content)
        if not data['no-logs'] or color is red:
            if not color:
                if not add_p:
                    print(content)
                else:
                    print(add_p(content))
            else:
                if not add_p:
                    print(color(content))
                else:
                    print(color(add_p(content)))
        content = discord.utils.escape_markdown(content)
        if not add_d:
            dstore(user_name,content)
        else:
            dstore(user_name,add_d(content))

    def split_ignore(text: str, ignore: Optional[str] = None) -> list:
        temp = ""
        text_list = []
        for char in text:
            if char.split() != []:
                temp += char
            elif char != ignore:
                if temp != "":
                    text_list.append(temp)
                    temp = ""
                text_list.append("")
        if temp != "":
            text_list.append(temp)
        return text_list

    def eval_format(text: str, variables: dict = {}) -> str:
        for match in format_pattern.finditer(text):
            match_text = match.group()
            eval_text = match_text.replace("{","",1)[::-1].replace("}","",1)[::-1]
            result = eval(eval_text,globals(),variables)
            text = text.replace(match_text,str(result),1)
        return text

    def get_client_data(id_: str) -> defaultdict:
        var = defaultdict(lambda: None)
        for client in clients:
            if not client.isready:
                continue
            if client.user.id == id_:
                break
        else:
            return var
        party = getattr(client,"party",None)
        if party:
            config = party.config
            var.update(
                {
                    "party_id": party.id,
                    "party_size": party.member_count,
                    "party_max_size": config["max_size"]
                }
            )
        var.update(
            {
                "friend_count": len(client.friends),
                "pending_count": len(client.pending_friends),
                "incoming_pending_count": len(client.incoming_pending_friends),
                "outgoing_pending_count": len(client.outgoing_pending_friends),
                "block_count": len(client.blocked_users),
                "display_name": client.user.display_name,
                "id": client.user.id,
                "boot_time": int(time.time() - dclient.boot_time)
            }
        )
        return var

    def get_guild_member_count(id_: Union[str]) -> Optional[int]:
        if isinstance(id_,str):
            id_ = int(id_)
        guild = dclient.get_guild(id_)
        if guild is None:
            return None
        return guild.member_count

    def platform_to_str(platform: fortnitepy.Platform) -> Optional[str]:
        converter = {
            fortnitepy.Platform.WINDOWS: "Windows",
            fortnitepy.Platform.MAC: "Mac",
            fortnitepy.Platform.PLAYSTATION: "PlayStation",
            fortnitepy.Platform.XBOX: "Xbox",
            fortnitepy.Platform.SWITCH: "Switch",
            fortnitepy.Platform.IOS: "IOS",
            fortnitepy.Platform.ANDROID: "Android"
        }
        return converter.get(platform)

    def convert_to_type(text: str) -> Optional[str]:
        if True in [text.lower() in commands[key] for key in outfit_keys] or text.lower().startswith("cid_"):
            return "Outfit"
        elif True in [text.lower() in commands[key] for key in backpack_keys] or text.lower().startswith("bid_"):
            return "Back Bling"
        elif True in [text.lower() in commands[key] for key in pet_keys] or text.lower().startswith("petcarrier_"):
            return "Pet"
        elif True in [text.lower() in commands[key] for key in pickaxe_keys] or text.lower().startswith("pickaxe_id"):
            return "Harvesting Tool"
        elif True in [text.lower() in commands[key] for key in emote_keys] or text.lower().startswith("eid_"):
            return "Emote"
        elif True in [text.lower() in commands[key] for key in emoji_keys] or text.lower().startswith("emoji_"):
            return "Emoticon"
        elif True in [text.lower() in commands[key] for key in toy_keys] or text.lower().startswith("toy_"):
            return "Toy"
        elif True in [text.lower() in commands[key] for key in item_keys]:
            return "Item"

    def convert_to_asset(text: str) -> Optional[str]:
        if True in [text.lower() in commands[key] for key in outfit_keys] or text.lower().startswith("cid_"):
            return "outfit"
        elif True in [text.lower() in commands[key] for key in backpack_keys] or text.lower().startswith("bid_"):
            return "backpack"
        elif True in [text.lower() in commands[key] for key in pet_keys] or text.lower().startswith("petcarrier_"):
            return "backpack"
        elif True in [text.lower() in commands[key] for key in pickaxe_keys] or text.lower().startswith("pickaxe_id"):
            return "pickaxe"
        elif True in [text.lower() in commands[key] for key in emote_keys] or text.lower().startswith("eid_"):
            return "emote"
        elif True in [text.lower() in commands[key] for key in emoji_keys] or text.lower().startswith("emoji_"):
            return "emote"
        elif True in [text.lower() in commands[key] for key in toy_keys] or text.lower().startswith("toy_"):
            return "emote"

    def convert_to_id(text: str) -> Optional[str]:
        if True in [text.lower() in commands[key] for key in outfit_keys] or text.lower().startswith("cid_"):
            return "cid"
        elif True in [text.lower() in commands[key] for key in backpack_keys] or text.lower().startswith("bid_"):
            return "bid"
        elif True in [text.lower() in commands[key] for key in pet_keys] or text.lower().startswith("petcarrier_"):
            return "petcarrier"
        elif True in [text.lower() in commands[key] for key in pickaxe_keys] or text.lower().startswith("pickaxe_id"):
            return "pickaxe_id"
        elif True in [text.lower() in commands[key] for key in emote_keys] or text.lower().startswith("eid_"):
            return "eid"
        elif True in [text.lower() in commands[key] for key in emoji_keys] or text.lower().startswith("emoji_"):
            return "emoji_id"
        elif True in [text.lower() in commands[key] for key in toy_keys] or text.lower().startswith("toy_"):
            return "toy_id"
        elif True in [text.lower() in commands[key] for key in item_keys]:
            return "id"

    def convert_to_old_type(text: str) -> Optional[str]:
        converter = {
            "outfit": "outfit",
            "back bling": "backpack",
            "pet": "pet",
            "harvesting tool": "pickaxe",
            "emote": "emote",
            "emoticon":" emoji",
            "toy": "toy",
            "item": "item"
        }
        return converter.get(text.lower())

    def convert_to_new_type(text: str) -> Optional[str]:
        converter = {
            "outfit": "Outfit",
            "backpack": "Back Bling",
            "pet": "Pet",
            "pickaxe": "Harvesting Tool",
            "emote": "Emote",
            "emoji": "Emoticon",
            "toy": "Toy",
            "item": "Item"
        }
        return converter.get(text.lower())

    def convert_backend_type(backendType: str) -> str:
        converter = {
            "AthenaBackpack": "Back Bling",
            "AthenaPickaxe": "Harvesting Tool",
            "AthenaItemWrap": "Wrap",
            "AthenaGlider": "Glider",
            "AthenaCharacter": "Outfit",
            "AthenaPet": "Pet",
            "AthenaMusicPack": "Music",
            "AthenaLoadingScreen": "Loading Screen",
            "AthenaDance": "Emote",
            "AthenaSpray": "Spray",
            "AthenaEmoji": "Emoticon",
            "AthenaSkyDiveContrail": "Contrail",
            "AthenaPetCarrier": "Pet",
            "AthenaToy": "Toy",
            "AthenaConsumableEmote": "Emote",
            "AthenaBattleBus": "Battle Bus",
            "AthenaRewardEventGraphCosmetic": "Outfit",
            "AthenaVictoryPose": "Emote"
        }
        return converter.get(backendType)

    def convert_variant(type_: str, variants: dict) -> List[dict]:
        result = []
        for variant in variants:
            for option in variant['options']:
                result.append(
                    {
                        "name": option['name'],
                        'variants': [
                            {
                                'c': variant['channel'],
                                'v': option['tag'],
                                'dE': 0
                            }
                        ]
                    }
                )
        return result

    def get_device_auth_details() -> None:
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                return json.load(f)
        return {}

    def store_device_auth_details(email: str, details: dict) -> None:
        existing = get_device_auth_details()
        existing[email.lower()] = details
        with open(filename, 'w') as f:
            json.dump(existing, f)

    def load_json(filename: str) -> Union[list,dict]:
        try:
            with open(filename,encoding='utf-8') as f:
                data = json.load(f)
        except (json.decoder.JSONDecodeError, UnicodeDecodeError):
            try:
                with open(filename,encoding='utf-8-sig') as f:
                    data = json.load(f)
            except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                with open(filename,encoding='shift_jis') as f:
                    data = json.load(f)
        return data

    def load_config(client: Optional[fortnitepy.Client] = None) -> bool:
        global data
        global commands
        global replies
        try:
            data = load_json("config.json")
        except json.decoder.JSONDecodeError as e:
            send('ボット',f'{traceback.format_exc()}\n{e}',red,add_d=lambda x:f'>>> {x}')
            send('ボット','config.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください',red,add_d=lambda x:f'>>> {x}')
            send('Bot','Failed to load config.json file. Make sure you wrote correctly',red,add_d=lambda x:f'>>> {x}')
            return False
        except FileNotFoundError:
            send('ボット',traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send('ボット','config.json ファイルが存在しません',red,add_d=lambda x:f'>>> {x}')
            send('Bot','config.json file does not exist',red,add_d=lambda x:f'>>> {x}')
            return False
        if data.get('loglevel','normal') == 'debug':
            send('ボット',f'\n{json.dumps(data,ensure_ascii=False,indent=4)}\n',yellow,add_d=lambda x:f'\n```{x}```\n')
        for key,tags in config_tags_raw.items():
            try:
                value = eval(f"data{key}")
            except KeyError:
                error_config.append(key)
            else:
                if isinstance(value,dict):
                    continue
                if bool_ in tags:
                    if not isinstance(value,bool):
                        error_config.append(key)
                elif bool_none in tags:
                    if not isinstance(value,(bool,None.__class__)):
                        error_config.append(key)
                elif "can_be_multiple" in tags:
                    if not isinstance(value,list):
                        if str in tags:
                            error_config.append(key)
                            try:
                                exec(f"data{key} = value.split(',')")
                            except Exception:
                                if data.get('loglevel','normal') == 'debug':
                                    send('ボット',traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        elif int in tags:
                            error_config.append(key)
                            try:
                                exec(f"data{key} = [value]")
                            except Exception:
                                if data.get('loglevel','normal') == 'debug':
                                    send('ボット',traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                else:
                    if not isinstance(value,tags[0]):
                        error_config.append(key)
                        try:
                            exec(f"data{key} = tags[0](value)")
                        except Exception:
                            if data.get('loglevel','normal') == 'debug':
                                send('ボット',traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
        checks = [
            ['fortnite','owner'],
            ['fortnite','blacklist'],
            ['fortnite','whitelist'],
            ['fortnite','invitelist'],
            ['fortnite','otherbotlist'],
            ['discord','owner'],
            ['discord','blacklist'],
            ['discord','whitelist']
        ]
        for check in checks:
            k,k2 = check
            try:
                for value in data.get(k,{}).get(k2,[]).copy():
                    if len(str(value)) == 0:
                        data.get(k,{}).get(k2,[]).remove(value)
            except Exception:
                if data.get('loglevel','normal') == 'debug':
                    send('ボット',traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
        with open("config.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        def set_default(keys: list, default: Any, func: Optional[Callable] = None) -> None:
            text = ""
            text2 = ""
            for nest,key in enumerate(keys,1):
                text += f"['{key}']"
                if nest == len(keys):
                    if isinstance(default,str):
                        text2 += f".get('''{key}''','''{default}''')"
                    else:
                        text2 += f".get('''{key}''',{default})"
                else:
                    text2 += f"['''{key}''']"
            if func:
                var = func(eval(f"data{text2}"))
                exec(f"data{text} = var")
            else:
                exec(f"data{text} = data{text2}")
        set_default(['fortnite'],{})
        set_default(['fortnite','outfit'],"")
        set_default(['fortnite','outfit_style'],"")
        set_default(['fortnite','backpack'],"")
        set_default(['fortnite','backpack_style'],"")
        set_default(['fortnite','pickaxe'],"")
        set_default(['fortnite','pickaxe_style'],"")
        set_default(['fortnite','emote'],"")
        try:
            set_default(['fortnite','privacy'],'public',lambda x: getattr(PartyPrivacy,x.upper()))
        except AttributeError:
            send('ボット',traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            error_config.append("['fortnite']['privacy']")
        set_default(['fortnite','avatar_color'],'#ffffff,#ffffff,#ffffff')
        set_default(['discord','channels'],['{name}-command-channel'],lambda x: [i.replace(" ","-").replace(".","-").replace(",","-").replace("--","-").lower() for i in x])
        try:
            set_default(['discord','status_type'],'playing',lambda x: getattr(discord.ActivityType,x.lower()))
        except AttributeError:
            send('ボット',traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            error_config.append("['discord']['status_type']")
        set_default(['web'],{})
        set_default(['web','ip'],'{ip}')
        set_default(['web','port'],8080)
        set_default(['web','login_required'],False)
        set_default(['lang'],'en')
        set_default(['caseinsensitive'],False)
        set_default(['no-logs'],False)
        set_default(['discord-log'],False)
        set_default(['search_max'],60)
        set_default(['omit-over2000'],False)
        set_default(['skip-if-overflow'],False)
        set_default(['hide-email'],False)
        set_default(['hide-token'],False)
        set_default(['hide-webhook'],False)
        set_default(['loglevel'],'normal')
        if data.get("status",1) == 0:
            config_tags["['fortnite']['email']"].append("red")
            config_tags["['lang']"].append("red")
        if os.getcwd().startswith('/app') or os.getcwd().startswith('/home/runner'):
            data['web']['ip']="0.0.0.0"
        else:
            data['web']['ip'] = data['web']['ip'].format(ip=socket.gethostbyname(socket.gethostname()))
        if client:
            client.status_ = data['fortnite']['status']
            client.whisper = data['fortnite']['whisper']
            client.partychat = data['fortnite']['partychat']
            client.discord = data['discord']['discord']
            client.web = data['web']['web']
            client.whisperperfect = data['fortnite']['disablewhisperperfectly']
            client.partychatperfect = data['fortnite']['disablepartychatperfectly']
            client.discordperfect = data['discord']['disablediscordperfectly']
            client.joinmessageenable = data['fortnite']['joinmessageenable']
            client.randommessageenable = data['fortnite']['randommessageenable']
            client.outfitmimic = data['fortnite']['outfitmimic']
            client.backpackmimic = data['fortnite']['backpackmimic']
            client.pickaxemimic = data['fortnite']['pickaxemimic']
            client.emotemimic = data['fortnite']['emotemimic']
            client.outfitlock = data['fortnite']['outfitlock']
            client.backpacklock = data['fortnite']['backpacklock']
            client.pickaxelock = data['fortnite']['pickaxelock']
            client.emotelock = data['fortnite']['emotelock']
            client.acceptinvite = data['fortnite']['acceptinvite']
            client.acceptfriend = data['fortnite']['acceptfriend']

        if error_config:
            send('ボット',f'config.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください。アップデート後の場合は、最新のconfig.jsonファイルを確認してください\n{", ".join(error_config)} がありません',red,add_d=lambda x:f'>>> {x}')
            send('Bot',f'Failed to load config.json file. Make sure key name is correct. If this after update, plase check latest config.json file\n{", ".join(error_config)} is missing',red,add_d=lambda x:f'>>> {x}')
        os.makedirs("items/", exist_ok=True)

        def load_lang(lang: str) -> None:
            global localize
            try:
                localize = load_json(f"lang/{lang}.json")
            except json.decoder.JSONDecodeError as e:
                send('ボット',f'{traceback.format_exc()}\n{e}',red,add_d=lambda x:f'>>> {x}')
                send('ボット',f'{data["lang"]}.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください\n',red,add_d=lambda x:f'>>> {x}')
                send('Bot',f'Failed to load {data["lang"]}.json file. Make sure you wrote correctly',red,add_d=lambda x:f'>>> {x}')
                return False
            except FileNotFoundError:
                send('ボット',f'{traceback.format_exc()}\n{e}',red,add_d=lambda x:f'>>> {x}')
                send('ボット',f'{data["lang"]}.json ファイルが存在しません',red,add_d=lambda x:f'>>> {x}')
                send('Bot',f'{data["lang"]}.json file does not exist',red,add_d=lambda x:f'>>> {x}')
                return False
            return True

        if os.path.isfile(f"lang/{data['lang']}.json"):
            if not load_lang(data['lang']):
                return False
        else:
            if not load_lang("en"):
                return False

        color = data['fortnite']['avatar_color'].split(',') if data['fortnite']['avatar_color'] else ""
        if len(color) > 2:
            background_colors = [color[0], color[1], color[2]]
        elif len(color) == 1:
            try:
                background_colors = eval(f"fortnitepy.KairosBackgroundColorPreset.{color[0]}")
            except (AttributeError, SyntaxError):
                send(l('bot'),l('color_must_be'))
                error_config.append("['fortnite']['avatar_color']")
                background_colors = ["#ffffff","#ffffff","#ffffff"]
        else:
            background_colors = None
        data['fortnite']['avatar_color'] = background_colors

        try:
            commands = load_json("commands.json")
        except json.decoder.JSONDecodeError as e:
            send(l('bot'),f'{traceback.format_exc()}\n{e}',red,add_d=lambda x:f'>>> {x}')
            send(l('bot'),l("load_failed_json", "commands.json"),red,add_d=lambda x:f'>>> {x}')
            return False
        except FileNotFoundError:
            send(l('bot'),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(l('bot'),l("load_failed_notfound", "commands.json"),red,add_d=lambda x:f'>>> {x}')
            return False
        if data['loglevel'] == 'debug':
            send(l('bot'),f'\n{json.dumps(commands,ensure_ascii=False,indent=4)}\n',yellow,add_d=lambda x:f'\n```{x}```\n')
        for key,tags in commands_tags.items():
            try:
                value = eval(f"commands{key}")
            except KeyError:
                error_commands.append(key)
            else:
                if not isinstance(value,list):
                    try:
                        exec(f"commands{key} = value.split(',')")
                    except Exception:
                        if data["loglevel"] == 'debug':
                            send('ボット',traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    error_commands.append(key)
        with open("commands.json", 'w', encoding='utf-8') as f:
            json.dump(commands, f, ensure_ascii=False, indent=4)

        def set_default_(key: str, default: Any, func: Optional[Callable] = None) -> None:
            text = f"['{key}']"
            text2 = f".get('{key}','{default}')"
            if func:
                exec(f"commands{text} = {func}(commands{text2})")
            else:
                exec(f"commands{text} = commands{text2}")
        set_default_("usercommands","")

        if error_commands:
            send(l('bot'),f'{l("load_failed_keyerror", "commands.json")}\n{l("is_missing", ", ".join(error_commands))}',red,add_d=lambda x:f'>>> {x}')
        if data['caseinsensitive']:
            commands = {k.lower(): [jaconv.kata2hira(c.lower()) for c in v] for k,v in commands.items()}

        flag = True
        commands['ownercommands'] = []
        if "{all}" in commands['usercommands']:
            for command in (list(commands_tags.keys()) + ["cid_","bid_","petcarrier_","pickaxe_id_","eid_","emoji_","toy_","item-search"]):
                command = command.replace("['","",1).replace("']","",1)
                if command in ["usercommands","true","false","me","privacy_public","privacy_friends_allow_friends_of_friends","privacy_friends","privacy_private_allow_friends_of_friends","privacy_private","info_party"]:
                    continue
                if command in [i.lower() for i in commands['usercommands']]:
                    commands['ownercommands'].append(command)
        else:
            for command in (list(commands_tags.keys()) + ["cid_","bid_","petcarrier_","pickaxe_id_","eid_","emoji_","toy_","item-search"]):
                command = command.replace("['","",1).replace("']","",1)
                if command in ["usercommands","true","false","me","privacy_public","privacy_friends_allow_friends_of_friends","privacy_friends","privacy_private_allow_friends_of_friends","privacy_private","info_party"]:
                    continue
                if command not in [i.lower() for i in commands['usercommands']]:
                    commands['ownercommands'].append(command)

        try:
            replies = load_json("replies.json")
        except json.decoder.JSONDecodeError as e:
            send(l('bot'),f'{traceback.format_exc()}\n{e}',red,add_d=lambda x:f'>>> {x}')
            send(l('bot'),l("load_failed_json", "replies.json"),red,add_d=lambda x:f'>>> {x}')
            return False
        except FileNotFoundError:
            send(l('bot'),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(l('bot'),l("load_failed_notfound", "replies.json"),red,add_d=lambda x:f'>>> {x}')
            return False
        return True

    def get_item_data(lang: str) -> dict:
        res = requests.get("https://benbotfn.tk/api/v1/cosmetics/br", params={"lang": lang})
        if res.status_code == 200:
            return res.json()
        return None

    def store_item_data(langs: list) -> None:
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(get_item_data,lang): lang for lang in langs}
            for future in as_completed(futures):
                lang = futures[future]
                result = future.result()
                data_ = {}
                if data["loglevel"] == "debug":
                    send(l("bot"),f"Saving {lang} items",yellow)
                for item in result:
                    type_ = convert_backend_type(item["backendType"])
                    if type_ in ignoretype:
                        continue
                    if not data_.get(type_):
                        data_[type_] = []
                    data_[type_].append(item)
                for type_,items in data_.items():
                    with open(f"items/{type_}_{lang}.json","w",encoding="utf-8") as f:
                        json.dump(items,f,ensure_ascii=False,indent=4)
                if data["loglevel"] == "debug":
                    send(l("bot"),f"Saved {lang} items",yellow)

    def partymember_backpack(member: fortnitepy.party.PartyMemberBase) -> str:
        asset = member.meta.backpack
        result = re.search(r".*\.([^\'\"]*)", asset.strip("'"))
        if result and result.group(1) != 'None':
            return result.group(1)

    def partymember_emote(member: fortnitepy.party.PartyMemberBase) -> str:
        asset = member.meta.emote
        result = re.search(r".*\.([^\'\"]*)", asset.strip("'"))
        if result and result.group(1) != 'None':
            return result.group(1)

    def member_asset(member: fortnitepy.party.PartyMemberBase, asset: str) -> str:
        if asset in ("backpack", "pet"):
            return partymember_backpack(member)
        elif asset in ("emote", "emoji", "toy"):
            return partymember_emote(member)
        else:
            return getattr(member, asset, None)

    def search_item(lang: str, mode: str, text: str, type_: Optional[str] = None, cache: Optional[bool] = True) -> Optional[List[dict]]:
        itemlist = []
        if not cache_items.get(lang):
            cache_items[lang] = []
        if cache:
            if mode == 'set':
                data_ = cache_items[lang]
            else:
                data_ = [i for i in cache_items[lang] if convert_backend_type(i["backendType"]) in type_.split(',')]
        else:
            data_ = []
            if type_ not in ["Item", None]:
                with ThreadPoolExecutor() as executor:
                    def _open_file(filename: str) -> Union[list, dict]:
                        with open(filename, 'r', encoding='utf-8') as f:
                            d = json.load(f)
                        return d
                    futures = [executor.submit(_open_file,f'items/{i}_{lang}.json') for i in type_.split(',')]
                for future in futures:
                    data_.extend(future.result())
            else:
                with ThreadPoolExecutor() as executor:
                    def _open_file(filename: str) -> Union[list, dict]:
                        with open(filename, 'r', encoding='utf-8') as f:
                            d = json.load(f)
                        return d
                    def _(text: str) -> str:
                        return re.sub(r"items(\\|/)","",text).replace(f"_{lang}.json","")
                    futures = [executor.submit(_open_file,f'items/{_(i)}_{lang}.json') for i in glob(f"items/*_{lang}.json") if _(i)[0].isupper()]
                for future in futures:
                    data_.extend(future.result())
        for item in data_:
            try:
                if convert_backend_type(item["backendType"]) in ignoretype or item in itemlist or item.get("name") is None:
                    continue
                if mode == "name":
                    if data['caseinsensitive']:
                        text_ = jaconv.hira2kata(text.lower())
                        name = jaconv.hira2kata(item['name'].lower())
                    else:
                        text_ = text
                        name = item['name']
                    if text_ in name:
                        itemlist.append(item)
                elif mode == "id":
                    text_ = text
                    if text_.lower() in item['id'].lower():
                        itemlist.append(item)
                elif mode == "set":
                    if not item.get('set'):
                        continue
                    if data['caseinsensitive']:
                        text_ = jaconv.hira2kata(text.lower())
                        name = jaconv.hira2kata(item['set'].lower())
                    else:
                        text_ = text
                        name = item['set']
                    if text_ in name:
                        itemlist.append(item)
            except Exception:
                send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(l("bot"),item,red,add_d=lambda x:f'>>> {x}')
        if len(itemlist) == 0:
            if cache:
                return search_item(lang=lang, mode=mode, text=text, type_=type_, cache=False)
            else:
                return None
        else:
            if not cache:
                for item in itemlist:
                    if item not in cache_items[lang]:
                        cache_items[lang].append(item)
            return itemlist

    def search_style(lang: str, id_: str, type_: str, cache: Optional[bool] = True) -> Optional[List[dict]]:
        if not cache_items.get(lang):
            cache_items[lang] = []
        if cache:
            data_ = cache_items[lang]
        else:
            data_ = []
            if type_ != "Item":
                with ThreadPoolExecutor() as executor:
                    futures = [executor.submit(load_json,f'items/{i}_{lang}.json') for i in type_.split(',')]
                for future in futures:
                    data_.extend(future.result())
            else:
                with ThreadPoolExecutor() as executor:
                    def _(text: str) -> str:
                        return re.sub(r"items(\\|/)","",text).replace(f"_{lang}.json","")
                    futures = [executor.submit(load_json,f'items/{_(i)}_{lang}.json') for i in glob(f"items/*_{lang}.json") if _(i)[0].isupper()]
                for future in futures:
                    data_.extend(future.result())
        variants = None
        for item in data_:
            if item['id'].lower() == id_.lower():
                if item['variants']:
                    variants = convert_variant(item['backendType'], item['variants'])
                    break
        if not variants:
            if cache:
                return search_style(lang=lang, id_=id_, type_=type_, cache=False)
            else:
                return None
        else:
            if not cache:
                if item not in cache_items[lang]:
                    cache_items[lang].append(item)
            return variants

    def get_banner_data() -> dict:
        res = requests.get("https://benbotfn.tk/api/v1/exportAsset?path=FortniteGame/Content/Banners/BannerIcons")
        if res.status_code == 200:
            return res.json()
        return None

    def store_banner_data() -> None:
        data = get_banner_data()
        with open("items/banners.json","w",encoding="utf-8") as f:
            json.dump(data,f,indent=4,ensure_ascii=False)

    def restart(sleep_time: Optional[Union[int,float]] = 0) -> None:
        if sleep_time > 0:
            time.sleep(sleep_time)
        os.chdir(os.getcwd())
        os.execv(os.sys.executable,['python', *sys.argv])

if True: #Asynchronous functions
    async def reply(message: Union[fortnitepy.message.MessageBase, discord.Message, WebMessage], client: fortnitepy.Client, content: str) -> None:
        if isinstance(message, fortnitepy.message.MessageBase):
            await message.reply(content)
        elif isinstance(message, discord.Message):
            if len(content) > 1990:
                text = discord.utils.escape_markdown(content).split("\n")
                for txt in text:
                    if len(txt) > 1990:
                        text = [txt[i:i+1990] for i in range(0, len(txt), 1990)]
                        for t in text:
                            await message.channel.send(t)
                    else:
                        await message.channel.send(content)
            else:
                await message.channel.send(content)
        elif isinstance(message, WebMessage):
            message.reply(content)
        elif isinstance(message, AllMessage):
            message.reply(content, client)

    async def aexec(code: str, variable: dict) -> Any:
        def _(text) -> str:
            return re.match(r"(\u0020|\u3000)*", text).end() * u"\u0020"
        scode = code.split('\n')
        delete = len(_(scode[0]))
        lines = [i.replace(u"\u0020", "", delete) for i in scode]
        exc = (
            f'async def __ex(var):'
            + '\n for v in var:'
            + '\n     v = var[v]'
            + ''.join(f'\n {l}' for l in lines)
            + '\n for v in locals():'
            + '\n     var[v] = locals()[v]'
        )
        if data['loglevel'] == 'debug':
            send(l('bot'),exc,yellow,add_d=lambda x:f'```\n{x}\n```')
        exec(exc)
        variable_before = variable.copy()
        result = await locals()['__ex'](variable)
        variable_after = variable.copy()
        newvar = {k: v for k,v in variable_after.items() if (k not in variable_before.keys() or v != variable_before.get(k)) and "_" not in k and k not in ("k", "v") and isinstance(k, str)}
        for k in newvar:
            exc = (
                f"global {k}"
                + f"\n{k} = newvar['{k}']"
            )
            exec(exc)
        return result

    async def generate_device_auth_and_store(email: str) -> str:
        global web_text

        while True:
            send(l('bot'),l('get_code', email))
            web_text = l('get_code2', email)
            response = await ainput("Data: \n")
            if "redirectUrl" in response:
                response = json.loads(response)
                if "?code" not in response["redirectUrl"]:
                    send(l('bot'),l('unauthorized'))
                    continue
                code = response["redirectUrl"].split("?code=")[1]
            else:
                if "https://accounts.epicgames.com/fnauth" in response:
                    if "?code" not in response:
                        send(l('bot'),l('unauthorized'))
                        continue
                    code = response.split("?code=")[1]
                else:
                    code = response
            data = await authorization_code_auth(code)
            try:
                access_token = data["access_token"]
                in_app_id = data["in_app_id"]
            except KeyError:
                send(l('bot'),l('authorization_expired'))
                continue
            fortnite_access_token, fortnite_expires_at = await get_fortnite_token(access_token)
            user = await lookup_user(in_app_id, fortnite_access_token)
            if user["email"].lower() == email.lower():
                break
            else:
                send(l('bot'),l('account_incorrect', user["email"], email))
                continue
        exchange_code = await exchange(access_token)
        launcher_access_token, client_id = await exchange_code_auth(exchange_code)
        details = await generate_device_auth(client_id, launcher_access_token)
        store_device_auth_details(email.lower(), details)
        web_text = ""
        return details

    async def get_token() -> tuple:
        async with aiohttp.ClientSession() as session:
            data = await session.post(
                oauth_url,
                headers={
                    "Authorization": f"basic {launcher_token}"
                },
                data={
                    "grant_type": "client_credentials",
                    "token_type": "eg1"
                }
            )
            data = await data.json()
            return data["access_token"], datetime.datetime.fromisoformat(data["expires_at"].replace("Z",""))

    async def get_fortnite_token(access_token: str) -> tuple:
        exchange_code = await exchange(access_token)
        async with aiohttp.ClientSession() as session:
            data = await session.post(
                fortnite_token_url,
                headers={
                    "Authorization": f"basic {fortnite_token}"
                },
                data={
                    "grant_type": "exchange_code",
                    "token_type": "eg1",
                    "exchange_code": exchange_code
                }
            )
            data = await data.json()
            return data["access_token"], datetime.datetime.fromisoformat(data["expires_at"].replace("Z",""))

    async def authorization_code_auth(authorization_code: str) -> Optional[tuple]:
        async with aiohttp.ClientSession() as session:
            data = await session.post(
                oauth_url,
                headers={
                    "Authorization": f"basic {launcher_token}"
                },
                data={
                    "grant_type": "authorization_code",
                    "code": authorization_code,
                    "token_type": "eg1"
                }
            )
            return await data.json()

    async def exchange_code_auth(exchange_code: str) -> tuple:
        async with aiohttp.ClientSession() as session:
            data = await session.post(
                exchange_auth_url,
                headers={
                    "Authorization": f"basic {launcher_token}"
                },
                data={
                    "grant_type": "exchange_code",
                    "exchange_code": exchange_code,
                    "token_type": "eg1"
                }
            )
            data = await data.json()
            return data["access_token"], data["account_id"]

    async def exchange(access_token: str) -> str:
        async with aiohttp.ClientSession() as session:
            data = await session.get(
                exchange_url,
                headers={
                    "Authorization": f"bearer {access_token}"
                }
            )
            data = await data.json()
            return data["code"]

    async def lookup_user(user_id: str, fortnite_access_token: str) -> dict:
        async with aiohttp.ClientSession() as session:
            data = await session.get(
                user_lookup_url.format(user_id=user_id),
                headers={
                    "Authorization": f"bearer {fortnite_access_token}"
                }
            )
            data = await data.json()
            return data

    async def generate_device_auth(client_id: str, access_token: str) -> dict:
        async with aiohttp.ClientSession() as session:
            data = await session.post(
                f"https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{client_id}/deviceAuth",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/json"
                }
            )
            data = await data.json()
            return {"device_id": data["deviceId"], "account_id": data["accountId"], "secret": data["secret"]}

    async def run_bot() -> None:
        for client in clients:
            client.booting = True
        if data.get('restart_in') not in [None, 0]:
            Timer(data.get('restart_in'), restart).start()
        try:
            await fortnitepy.start_multiple(
                clients,
                all_ready_callback=lambda: send(l("bot"),l("all_login"),green,add_p=lambda x:f'[{now()}] {x}') if len(clients) > 1 else print('')
            )
        except fortnitepy.AuthException as e:
            if data["loglevel"] == "debug":
                send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if "errors.com.epicgames.account.oauth.exchange_code_not_found" in e.args[0]:
                send(l("bot"),l("exchange_code_error"),red,add_p=lambda x:f'[{now()}] {x}',add_d=lambda x:f'>>> {x}')
            elif "Invalid device auth details passed." in e.args[0]:
                some_detail = e.args[0].split("-")[0].strip()
                device_auth_details = get_device_auth_details()
                for email,details in device_auth_details.items():
                    for detail in details.values():
                        if detail == some_detail:
                            break
                    else:
                        continue
                    break
                else:
                    email = some_detail
                device_auth_details.pop(email.lower())
                with open(filename, 'w') as f:
                    json.dump(device_auth_details, f)
                restart()
            else:
                send(l("bot"),l("login_failed"),red,add_p=lambda x:f'[{now()}] {x}',add_d=lambda x:f'>>> {x}')
            sys.exit(1)
        except fortnitepy.HTTPException as e:
            if data["loglevel"] == "debug":
                send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if "reset" in e.args[0]:
                send(l("bot"),l("password_reset_error"),red,add_p=lambda x:f'[{now()}] {x}',add_d=lambda x:f'>>> {x}')
            else:
                send(l("bot"),l("login_failed"),red,add_p=lambda x:f'[{now()}] {x}',add_d=lambda x:f'>>> {x}')
            sys.exit(1)
        except KeyboardInterrupt:
            sys.exit(1)
        except Exception:
            send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(l("bot"),l("failed_to_load_account"),red,add_p=lambda x:f'[{now()}] {x}',add_d=lambda x:f'>>> {x}')
            sys.exit(1)

    async def run_app() -> None:
        try:
            await app.create_server(host=data['web']['ip'], port=data['web']['port'], return_asyncio_server=True, access_log=data['web']['log'])
        except OSError:
            if data["loglevel"] == "debug":
                send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(l("bot"),l("web_already_running"),red,add_p=lambda x:f'[{now()}] {x}',add_d=lambda x:f'>>> {x}')
        except Exception:
            send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
        else:
            if data["status"] == 0 or bot_ready is False:
                webbrowser.open(f"http://{data['web']['ip']}:{data['web']['port']}")
            send(l("bot"),l("web_running",f"http://{data['web']['ip']}:{data['web']['port']}"),add_p=lambda x:f'[{now()}] {x}')

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

async def process_command(message: Union[fortnitepy.FriendMessage, fortnitepy.PartyMessage, discord.Message, WebMessage, AllMessage]):
    global blacklist
    global whitelist
    global blacklist_
    global whitelist_
    global otherbotlist
    if not message or not message.content:
        return
    loop = asyncio.get_event_loop()
    content = message.content
    con = content.split("\n")
    if data['caseinsensitive']:
        args = jaconv.kata2hira(content.lower()).split()
    else:
        args = content.split()
    content_ = ' '.join(args[1:])
    content2_ = ' '.join(args[2:])
    rawargs = content.split()
    rawcontent = ' '.join(rawargs[1:])
    rawcontent2 = ' '.join(rawargs[2:])
    check_ownercommand = True
    check_ng = True
    if len(args) < 1:
        return
    if isinstance(message, fortnitepy.message.MessageBase):
        client = message.client
        client.add_cache(message.author)
        if ((data['discord']['enabled'] and not dclient.isready)
            or (message.author.id in blacklist and data['fortnite']['blacklist-ignorecommand'])
            or (message.author.id in (otherbotlist + [i.user.id for i in loadedclients]) and data['fortnite']['ignorebot'])):
            return

        if ((len(con) > 1)
            and not (args[0] in commands['eval'])
            and not (args[0] in commands['exec'])):
            tasks = []
            for c in con:
                mes = AllMessage(c, message.author, client, message)
                task = loop.create_task(process_command(mes))
                tasks.append([task,mes])
            await asyncio.gather(*[task[0] for task in tasks])
            for mes in [task[1] for task in tasks]:
                result = mes.result.get(client.user.id)
                if result:
                    await reply(message, client, '\n'.join(result))
            return

        if isinstance(message, fortnitepy.FriendMessage):
            if not client.whisper:
                if client.whisperperfect:
                    return
                elif message.author.id not in [owner.id for owner in client.owner] and message.author.id not in whitelist:
                    return
            if data['loglevel'] == 'normal':
                send(name(message.author),content,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {name(message.author)} | {x}',add_d=lambda x:f'[{client.user.display_name}] {x}')
            else:
                send(f'{name(message.author)} [{platform_to_str(message.author.platform)}]',content,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {name(message.author)} [{platform_to_str(message.author.platform)}] | {x}',add_d=lambda x:f'[{client.user.display_name}] {x}')
        elif isinstance(message, fortnitepy.PartyMessage):
            if not client.partychat:
                if client.partychatperfect:
                    return
                elif message.author.id not in [owner.id for owner in client.owner] and message.author.id not in whitelist:
                    return
            display_name_ = client.is_most()
            if display_name_:
                if data['loglevel'] == 'normal':
                    send(name(message.author),content,add_p=lambda x:f'[{now()}] [{l("party")}] [{display_name_}] {name(message.author)} | {x}',add_d=lambda x:f'[{l("party")}] [{display_name_}] {x}')
                else:
                    send(f'{name(message.author)} [{platform_to_str(message.author.platform)}/{message.author.input}]',content,add_p=lambda x:f'[{now()}] [{l("party")}/{client.party.id}] [{display_name_}] {name(message.author)} [{platform_to_str(message.author.platform)}/{message.author.input}] | {x}',add_d=lambda x:f'[{l("party")}/{client.party.id}] [{display_name_}] {x}')

        if content_ in commands['me']:
            rawcontent = message.author.id
            content_ = message.author.id

        if ((message.author.id in [owner.id for owner in client.owner])
            or (message.author.id in whitelist and data['fortnite']['whitelist-ownercommand'])):
            check_ownercommand = False
        if ((message.author.id in [owner.id for owner in client.owner])
            or (message.author.id in whitelist and data['fortnite']['whitelist-ignoreng'])):
            check_ng = False
    elif isinstance(message, discord.Message):
        if ((not isinstance(message.channel, discord.TextChannel))
            or (message.author.id == dclient.user.id)
            or (message.author.id in blacklist_ and data['discord']['blacklist-ignorecommand'])
            or (message.author.bot and data['discord']['ignorebot'])):
            return
        if True in [True for i in data['discord']['channels'] if "{name}" not in i and "{id}" not in i and message.channel.name == i]:
            tasks = {}
            for client_ in loadedclients:
                mes = AllMessage(content, message.author, client_, message)
                task = loop.create_task(process_command(mes))
                tasks[client_] = [task, mes]
            await asyncio.gather(*[i[0] for i in tasks.values()])
            for client_,list_ in tasks.items():
                result = list_[1].result.get(client_.user.id)
                if result:
                    results = '\n'.join(result)
                    await reply(message, client_, f"[{name(client_.user)}] {results}")
            return
        else:
            for clientname, client in client_name.items():
                if not client.isready:
                    continue

                if message.channel.name in [i.format(name=clientname, id=client.user.id).replace(" ","-").replace(".","-").replace(",","-").replace("--","-").lower() for i in data["discord"]["channels"]]:
                    break
            else:
                return
        if not client.discord:
            if client.discordperfect:
                return
            elif message.author.id not in [owner.id for owner in client.owner] and message.author.id not in whitelist_:
                return

        if (len(con) > 1
            and not (args[0] in commands['eval'])
            and not (args[0] in commands['exec'])):
            tasks = []
            for c in con:
                mes = AllMessage(c, message.author, client, message)
                task = loop.create_task(process_command(mes))
                tasks.append([task,mes])
            await asyncio.gather(*[task[0] for task in tasks])
            for mes in [task[1] for task in tasks]:
                result = mes.result.get(client.user.id)
                if result:
                    await reply(message, client, '\n'.join(result))
            return

        send(name(message.author),content,add_p=lambda x:f'[{now()}] [{client.user.display_name}({dclient.user})] {name(message.author)} | {x}',add_d=lambda x:f'[{client.user.display_name}({dclient.user})] {x}')

        if ((message.author.id in [owner.id for owner in dclient.owner])
            or (message.author.id in whitelist_ and data['discord']['whitelist-ownercommand'])):
            check_ownercommand = False
        if ((message.author.id in [owner.id for owner in dclient.owner])
            or (message.author.id in whitelist_ and data['discord']['whitelist-ignoreng'])):
            check_ng = False
    elif isinstance(message, WebMessage):
        client = message.client
        if ((data['discord']['enabled'] and not dclient.isready)
            or (not client.web)):
            return

        if (len(con) > 1
            and not (args[0] in commands['eval'])
            and not (args[0] in commands['exec'])):
            tasks = []
            for c in con:
                mes = AllMessage(c, message.author, client, message)
                task = loop.create_task(process_command(mes))
                tasks.append([task,mes])
            await asyncio.gather(*[task[0] for task in tasks])
            for mes in [task[1] for task in tasks]:
                result = mes.result.get(client.user.id)
                if result:
                    await reply(message, client, '\n'.join(result))
            return

        check_ownercommand = False
        check_ng = False
        send(name(message.author),content,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {name(message.author)} | {x}',add_d=lambda x:f'[{client.user.display_name}] {x}')
    elif isinstance(message, AllMessage):
        client = message.client
        if data['discord']['enabled'] and not dclient.isready:
            return

        if (len(con) > 1
            and not (args[0] in commands['eval'])
            and not (args[0] in commands['exec'])):
            tasks = []
            for c in con:
                mes = AllMessage(c, message.author, client, message)
                task = loop.create_task(process_command(mes))
                tasks.append([task,mes])
            await asyncio.gather(*[task[0] for task in tasks])
            for mes in [task[1] for task in tasks]:
                result = mes.result.get(client.user.id)
                if result:
                    await reply(message, client, '\n'.join(result))
            return

        base = message.base
        while isinstance(base, AllMessage):
            base = base.base

        if isinstance(base, fortnitepy.message.MessageBase):
            client.add_cache(message.author)
            if ((message.author.id in blacklist and data['fortnite']['blacklist-ignorecommand'])
                or (message.author.id in (otherbotlist + [i.user.id for i in loadedclients]) and data['fortnite']['ignorebot'])):
                return
            if isinstance(base, fortnitepy.FriendMessage):
                if not client.whisper:
                    if client.whisperperfect:
                        return
                    elif message.author.id not in [owner.id for owner in client.owner] and message.author.id not in whitelist:
                        return
                if data['loglevel'] == 'normal':
                    send(name(message.author),content,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {name(message.author)} | {x}',add_d=lambda x:f'[{client.user.display_name}] {x}')
                else:
                    send(f'{name(message.author)} [{platform_to_str(message.author.platform)}]',content,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {name(message.author)} | {x}',add_d=lambda x:f'[{client.user.display_name}] {x}')
            elif isinstance(base, fortnitepy.PartyMessage):
                if not client.partychat:
                    if client.partychatperfect:
                        return
                    elif message.author.id not in [owner.id for owner in client.owner] and message.author.id not in whitelist:
                        return
                display_name = client.is_most()
                if display_name:
                    if data['loglevel'] == 'normal':
                        send(name(message.author),content,add_p=lambda x:f'[{now()}] [{l("party")}] [{display_name}] {name(message.author)} | {x}',add_d=lambda x:f'[{l("party")}] [{display_name}] {x}')
                    else:
                        send(f'{name(message.author)} [{platform_to_str(message.author.platform)}/{message.author.input}]',content,add_p=lambda x:f'[{now()}] [{l("party")}/{client.party.id}] [{display_name}] {name(message.author)} [{platform_to_str(message.author.platform)}/{message.author.input}] | {x}',add_d=lambda x:f'[{l("party")}/{client.party.id}] [{display_name}] {x}')
            if rawcontent in commands['me']:
                rawcontent = message.author.id
                content_ = message.author.id

            if ((message.author.id in [owner.id for owner in client.owner])
                or (message.author.id in whitelist and data['fortnite']['whitelist-ownercommand'])):
                check_ownercommand = False
            if ((message.author.id in [owner.id for owner in client.owner])
                or (message.author.id in whitelist and data['fortnite']['whitelist-ignoreng'])):
                check_ng = False
        elif isinstance(base, discord.message.Message):
            if ((message.author.id == dclient.user.id)
                or (message.author.id in blacklist_ and data['discord']['blacklist-ignorecommand'])
                or (message.author.bot and data['discord']['ignorebot'])):
                return
            if not client.discord:
                if client.discordperfect:
                    return
                elif message.author.id not in [owner.id for owner in dclient.owner] and message.author.id not in whitelist_:
                    return
            send(name(message.author),content,add_p=lambda x:f'[{now()}] [{client.user.display_name}({dclient.user})] {name(message.author)} | {x}',add_d=lambda x:f'[{client.user.display_name}({dclient.user})] {x}')

            if ((message.author.id in [owner.id for owner in dclient.owner])
                or (message.author.id in whitelist_ and data['discord']['whitelist-ownercommand'])):
                check_ownercommand = False
            if ((message.author.id in [owner.id for owner in dclient.owner])
                or (message.author.id in whitelist_ and data['discord']['whitelist-ignoreng'])):
                check_ng = False
        elif isinstance(base, WebMessage):
            if ((data['discord']['enabled'] and not dclient.isready)
                or (not client.web)):
                return
            check_ownercommand = False
            check_ng = False
            send(name(message.author),content,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {name(message.author)} | {x}',add_d=lambda x:f'[{client.user.display_name}] {x}')

    if not client.isready:
        return
    display_name = name(client.user)

    do_itemsearch = True
    if check_ownercommand:
        for command in commands['ownercommands']:
            if command in ("cid_", "bid_", "petcarrier_", "pickaxe_id_", "eid_", "emoji_", "toy_"):
                if args[0].startswith(command):
                    await reply(message, client, l("this_command_owneronly"))
                    return
            elif command == "item-search":
                do_itemsearch = False
            elif args[0] in commands[command]:
                await reply(message, client, l("this_command_owneronly"))
                return

    reply_flag = False
    for key,value in replies.items():
        reply_flag_ = False

        if data["replies-matchmethod"] == "contains":
            if [k for k in key.split(',') if k in content]:
                reply_flag_ = True
        elif data["replies-matchmethod"] == "full":
            if [k for k in key.split(',') if k == content]:
                reply_flag_ = True
        elif data["replies-matchmethod"] == "starts":
            if [k for k in key.split(',') if content.startswith(k)]:
                reply_flag_ = True
        elif data["replies-matchmethod"] == "ends":
            if [k for k in key.split(',') if content.endswith(k)]:
                reply_flag_ = True
        if reply_flag_:
            reply_flag = True
            var = defaultdict(lambda: None)
            var.update(client.get_client_data())
            var.update(
                {
                    "get_client_data": get_client_data,
                    "all_friend_count": sum([len(client_.friends) for client_ in clients]),
                    "all_pending_count": sum([len(client_.pending_friends) for client_ in clients]),
                    "all_block_count": sum([len(client_.blocked_users) for client_ in clients]),
                    "author_display_name": message.author.display_name,
                    "author_id": message.author.id
                }
            )
            mes = eval_format(value,var)
            await reply(message, client, mes)

    if check_ng:
        flag = False
        if data["ng-word-matchmethod"] == "contains":
            if [ng for ng in data["ng-words"] if ng in content]:
                flag = True
        elif data["ng-word-matchmethod"] == "full":
            if [ng for ng in data["ng-words"] if ng == content]:
                flag = True
        elif data["ng-word-matchmethod"] == "starts":
            if [ng for ng in data["ng-words"] if content.startswith(ng)]:
                flag = True
        elif data["ng-word-matchmethod"] == "ends":
            if [ng for ng in data["ng-words"] if content.endswith(ng)]:
                flag = True
        if flag:
            if data["ng-word-blacklist"]:
                if isinstance(message, fortnitepy.message.MessageBase):
                    blacklist.append(message.author.id)
                    data_ = load_json("config.json")
                    data_["fortnite"]["blacklist"].append(message.author.id)
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                elif isinstance(message, discord.Message):
                    blacklist_.append(message.author.id)
                    data_ = load_json("config.json")
                    data_["discord"]["blacklist"].append(message.author.id)
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            member = client.party.get_member(message.author.id)
            if member and client.party.me.leader:
                if data["ng-word-kick"]:
                    try:
                        await member.kick()
                    except Exception as e:
                        if data["loglevel"] == "debug":
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            await reply(message, client, f"{l('error')}\n{traceback.format_exc()}")
                elif data["ng-word-chatban"]:
                    try:
                        await member.chatban()
                    except Exception as e:
                        if data["loglevel"] == "debug":
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            await reply(message, client, f"{l('error')}\n{traceback.format_exc()}")
            return
    if reply_flag:
        return

    if args[0] in commands['prev']:
        c = client.prevmessage.get(message.author.id)
        if c:
            mes = AllMessage(c, message.author, client, message)
            task = loop.create_task(process_command(mes))
            await task
            result = mes.result
            if result:
                await reply(message, client, '\n'.join(result))
        return
    client.prevmessage[message.author.id] = content

    if args[0] in commands['eval']:
        try:
            if rawcontent == "":
                await reply(message, client, f"[! (計算式)]のように入力してください\n例) ! 123+456")
                return
            variable = globals()
            variable.update(locals())
            if rawcontent.startswith("await "):
                if data['loglevel'] == "debug":
                    send(display_name,f"await eval({rawcontent.replace('await ','',1)})",yellow,add_d=lambda x:f'```\n{x}\n```')
                result = await eval(rawcontent.replace("await ","",1), variable)
                send(display_name,str(result))
                await reply(message, client, str(result))
            else:
                if data['loglevel'] == "debug":
                    send(display_name,f"eval {rawcontent}",yellow,add_d=lambda x:f'```\n{x}\n```')
                result = eval(rawcontent, variable)
                send(display_name,str(result))
                await reply(message, client, str(result))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"{l('eval_error')}")

    elif args[0] in commands['exec']:
        try:
            if rawcontent == "":
                await reply(message, client, f"[{commands['exec']}] [{l('exec')}]")
                return
            variable = globals()
            variable.update(locals())
            result = await aexec(content.replace(f"{args[0]} ","",1), variable)
            await reply(message, client, str(result))
        except Exception as e:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"{l('error')}\n{traceback.format_exc()}")

    if data['discord']['enabled']:
        if args[0] in commands['addblacklist_discord']:
            try:
                if rawcontent == '' or not args[1].isdigit():
                    await reply(message, client, f"[{commands['addblacklist_discord']}] [{l('userid')}]")
                    return
                user = dclient.get_user(int(args[1]))
                if not user:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id not in blacklist_:
                    blacklist_.append(user.id)
                    data_ = load_json("config.json")
                    data_["discord"]["blacklist"].append(user.id)
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    send(display_name,l('add_to_list', f'{name(user)}', l('discord_blacklist')),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('add_to_list', f'{name(user)}', l('discord_blacklist')))
                else:
                    await reply(message, client, l('already_list', f'{name(user)}', l('discord_blacklist')))
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('user_notfound'))
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['removeblacklist_discord']:
            try:
                if rawcontent == '' or not args[1].isdigit():
                    await reply(message, client, f"[{commands['removeblacklist_discord']}] [{l('userid')}]")
                    return
                user = dclient.get_user(int(args[1]))
                if not user:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id in blacklist_:
                    blacklist_.remove(user.id)
                    data_ = load_json("config.json")
                    data_["discord"]["blacklist"].remove(user.id)
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    send(display_name,l('remove_from_list', f'{name(user)}', l('discord_blacklist')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('remove_from_list', f'{name(user)}', l('discord_blacklist')))
                else:
                    await reply(message, client, l('not_list', f'{name(user)}', l('discord_blacklist')))
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(display_name,l('user_notfound'),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('user_notfound'))
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(display_name,traceback.format_exc(),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['addwhitelist_discord']:
            try:
                if rawcontent == '' or not args[1].isdigit():
                    await reply(message, client, f"[{commands['addwhitelist_discord']}] [{l('userid')}]")
                    return
                user = dclient.get_user(int(args[1]))
                if not user:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id not in whitelist_:
                    whitelist_.append(user.id)
                    data_ = load_json("config.json")
                    data_["discord"]["whitelist"].append(user.id)
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    send(display_name,l('remove_from_list', f'{name(user)}', l('discord_whitelist')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('add_from_list', f'{name(user)}', l('discord_whitelist')))
                else:
                    await reply(message, client, l('already_list', f'{name(user)}', l('discord_whitelist')))
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('user_notfound'))
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['removewhitelist_discord']:
            try:
                if rawcontent == '' or not args[1].isdigit():
                    await reply(message, client, f"[{commands['removewhitelist_discord']}] [{l('userid')}]")
                    return
                user = dclient.get_user(int(args[1]))
                if not user:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id in whitelist_:
                    whitelist_.remove(user.id)
                    data_ = load_json("config.json")
                    data_["discord"]["whitelist"].remove(user.id)
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    send(display_name,l('remove_from_list', f'{name(user)}', l('discord_whitelist')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('remove_list', f'{name(user)}', l('discord_whitelist')))
                else:
                    await reply(message, client, l('not_list', f'{name(user)}', l('discord_whitelist')))
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('user_notfound'))
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

    if args[0] in commands['restart']:
        try:
            if not client.acceptinvite:
                if isinstance(message, fortnitepy.message.MessageBase) or isinstance(getattr(message,"base",None), fortnitepy.message.MessageBase):
                    if (not (message.author.id in [owner.id for owner in client.owner])
                        and not (message.author.id in whitelist and data['fortnite']['whitelist-ownercommand'])
                        and not (message.author.id in [owner.id for owner in dclient.owner])
                        and not (message.author.id in whitelist_ and data['discord']['whitelist-ownercommand'])):
                        await reply(message, client, l('invite_is_decline'))
                        return
            await reply(message, client, l('restarting'))
            Thread(target=restart,args=(0.5,)).start()
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['relogin']:
        try:
            if client.acceptinvite is False:
                if isinstance(message, fortnitepy.message.MessageBase) or isinstance(getattr(message,"base",None), fortnitepy.message.MessageBase):
                    if (not (message.author.id in [owner.id for owner in client.owner])
                        and not (message.author.id in whitelist and data['fortnite']['whitelist-ownercommand'])
                        and not (message.author.id in [owner.id for owner in dclient.owner])
                        and not (message.author.id in whitelist_ and data['discord']['whitelist-ownercommand'])):
                        await reply(message, client, l('invite_is_decline'))
                        return
            await reply(message, client, l('relogining'))
            await client.restart()
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['reload']:
        success = load_config(client)
        try:
            if success:
                await reply(message, client, l('success'))
            else:
                await reply(message, client, l('error'))
                return
            try:
                if data['fortnite']['avatar_id'] == "{bot}":
                    client.set_avatar(fortnitepy.Avatar(asset=client.party.me.outfit, background_colors=data['fortnite']['avatar_color']))
                else:
                    client.set_avatar(fortnitepy.Avatar(asset=data['fortnite']['avatar_id'].format(bot=client.party.me.outfit), background_colors=data['fortnite']['avatar_color']))
            except Exception:
                if data['loglevel'] == 'debug':
                    send(name(client.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

            client.owner = []
            for owner in data['fortnite']['owner']:
                user = client.get_user(owner) or client.get_cache_user(owner)
                if not user:
                    try:
                        user = await client.fetch_user(owner)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    except Exception:
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                if not user:
                    send(display_name,l("owner_notfound",owner),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                else:
                    client.add_cache(user)
                    friend = client.get_friend(user.id)
                    if not friend:
                        send(display_name,l("not_friend_with_owner",commands["reload"]),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        if data['fortnite']['addfriend'] and not client.is_pending(user.id):
                            try:
                                await client.add_friend(user.id)
                            except fortnitepy.HTTPException:
                                if data['loglevel'] == 'debug':
                                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                                send(display_name,l("error_while_sending_friendrequest"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                            except Exception:
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    else:
                        client.owner.append(friend)
                        send(display_name,f'{l("owner")}: {name(friend)}',green,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
            if client.owner and data['fortnite']['click_invite']:
                for owner in client.owner:
                    await owner.send(l("click_invite"))

            lists = {
                "blacklist": "blacklist",
                "whitelist": "whitelist",
                "otherbotlist": "botlist"
            }
            async def _(listuser: str) -> None:
                user = client.get_user(listuser) or client.get_cache_user(listuser)
                if not user:
                    try:
                        user = await client.fetch_user(listuser)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    except Exception:
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                if not user:
                    send(display_name,l(f"{data_}_user_notfound",listuser),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                else:
                    client.add_cache(user)
                    if data_ == "blacklist" and data["fortnite"]["blacklist-autoblock"]:
                        try:
                            await user.block()
                        except Exception:
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    globals()[list_].append(user.id)

            for list_,data_ in lists.items():
                try:
                    await asyncio.gather(*[_(listuser) for listuser in data['fortnite'][list_]])
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                if data['loglevel'] == "debug":
                    send(display_name,f"fortnite {data_}list {globals()[list_]}",yellow,add_d=lambda x:f'```\n{x}\n```')

            lists = [
                "outfitmimic",
                "backpackmimic",
                "pickaxemimic",
                "emotemimic"
            ]
            async def _(mimic: str) -> None:
                if isinstance(data['fortnite'][mimic],str):
                    user = client.get_user(mimic) or client.get_cache_user(mimic)
                    if not user:
                        try:
                            user = await client.fetch_user(data['fortnite'][mimic])
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        except Exception:
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    if not user:
                        send(display_name,l(f"{mimic}_user_notfound",data['fortnite'][mimic]),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    else:
                        client.add_cache(user)
                        setattr(client,mimic,user.id)
                        if data['loglevel'] == "debug":
                            send(display_name,f"{mimic} {getattr(client,mimic)}",yellow,add_d=lambda x:f'```\n{x}\n```')
            try:
                await asyncio.gather(*[_(mimic) for mimic in lists])
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

            async def _(listuser: str) -> None:
                user = client.get_user(listuser) or client.get_cache_user(listuser)
                if not user:
                    try:
                        user = await client.fetch_user(listuser)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                if not user:
                    send(display_name,l("invitelist_user_notfound",listuser),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                else:
                    client.add_cache(user)
                    friend = client.get_friend(user.id)
                    if not friend:
                        send(display_name,l("not_friend_with_inviteuser",listuser,commands["reload"]),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        if data['fortnite']['addfriend'] and not client.is_pending(user.id) and user.id != client.user.id:
                            try:
                                await client.add_friend(user.id)
                            except fortnitepy.HTTPException:
                                if data['loglevel'] == 'debug':
                                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                                send(display_name,l("error_while_sending_friendrequest"),red,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    else:
                        client.invitelist.append(friend.id)
            try:
                await asyncio.gather(*[_(listuser) for listuser in data['fortnite']['invitelist']])
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if data['loglevel'] == "debug":
                send(display_name,f'invitelist {client.invitelist}',yellow,add_d=lambda x:f'```\n{x}\n```')

            if data['fortnite']['acceptfriend']:
                async def _(pending: fortnitepy.IncomingPendingFriend) -> None:
                    if client.acceptfriend is True:
                        try:
                            await pending.accept()
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            try:
                                await pending.decline()
                            except fortnitepy.HTTPException:
                                if data['loglevel'] == 'debug':
                                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    elif client.acceptfriend is False:
                        try:
                            await pending.decline()
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                try:
                    await asyncio.gather(*[_(pending) for pending in client.incoming_pending_friends])
                except Exception:
                    data["discord"]["enabled"] = False
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

            if data['discord']['enabled'] and dclient.isready:
                dclient_user = name(dclient.user)

                dclient.owner = []
                for owner in data['discord']['owner']:
                    user = dclient.get_user(owner)
                    if not user:
                        try:
                            user = await dclient.fetch_user(owner)
                        except discord.NotFound:
                            if data['loglevel'] == "debug":
                                send(dclient_user,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        except discord.HTTPException:
                            if data['loglevel'] == 'debug':
                                send(dclient_user,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            send(dclient_user,l('error_while_requesting_userinfo'),red,add_p=lambda x:f'[{now()}] [{dclient_user}] {x}',add_d=lambda x:f'>>> {x}')
                    if not user:
                        send(dclient_user,l('discord_owner_notfound',owner),red,add_p=lambda x:f'[{now()}] [{dclient_user}] {x}',add_d=lambda x:f'>>> {x}')
                    else:
                        dclient.owner.append(user)
                        send(dclient_user,f"{l('owner')}: {name(user)}",green,add_p=lambda x:f'[{now()}] [{dclient_user}] {x}')

                lists = {
                    "blacklist_": "blacklist",
                    "whitelist_": "whitelist"
                }
                async def _(listuser: str) -> None:
                    listuser = int(listuser)
                    user = dclient.get_user(listuser)
                    if not user:
                        try:
                            user = await dclient.fetch_user(listuser)
                        except discord.NotFound:
                            if data['loglevel'] == "debug":
                                send(dclient_user,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            send(dclient_user,l(f'discord_{data_}_user_notfound', listuser),red,add_p=lambda x:f'[{now()}] [{dclient_user}] {x}',add_d=lambda x:f'>>> {x}')
                            return
                    globals()[list_].append(user.id)

                for list_,data_ in lists.items():
                    await asyncio.gather(*[_(listuser) for listuser in data['discord'][data_]])
                    if data['loglevel'] == "debug":
                        send(dclient_user,f"discord {data_}list {globals()[list_]}",yellow,add_d=lambda x:f'```\n{x}\n```')
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['addblacklist']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['addblacklist']}] [{l('name_or_id')}]")
                return
            if data["caseinsensitive"]:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(name).lower()) and user.id != client.user.id and user.id not in blacklist}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(name) and user.id != client.user.id and user.id not in blacklist}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if user.id not in blacklist:
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', len(users)))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                if user.id not in blacklist:
                    blacklist.append(user.id)
                    if user.display_name:
                        data["fortnite"]["blacklist"].append(user.display_name)
                    else:
                        data["fortnite"]["blacklist"].append(user.id)
                    data_ = load_json("config.json")
                    data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    send(display_name,l('add_to_list', f'{name(user)}', l('blacklist')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('add_to_list', f'{name(user)}', l('blacklist')))
                else:
                    await reply(message, client, l('already_in_list', f'{name(user)}', l('blacklist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
            if user.id not in blacklist:
                blacklist.append(user.id)
                if user.display_name:
                    data["fortnite"]["blacklist"].append(user.display_name)
                else:
                    data["fortnite"]["blacklist"].append(user.id)
                data_ = load_json("config.json")
                data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                send(display_name,l('add_to_list', f'{name(user)}', l('blacklist')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                await reply(message, client, l('add_to_list', f'{name(user)}', l('blacklist')))
            else:
                await reply(message, client, l('already_in_list', f'{name(user)}', l('blacklist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {name(user)}"
                text += f"\n{l('enter_to_add_to_list', l('blacklist'))}"
                await reply(message, client, text)
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['removeblacklist']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['removeblacklist']}] [{l('name_or_id')}]")
                return
            if data["caseinsensitive"]:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and user.id in blacklist}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and user.id in blacklist}
            try:
                user = await client.fetch_user(rawcontent)
                if not user:
                    if user.id in blacklist:
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                if user.id in blacklist:
                    blacklist.remove(user.id)
                    try:
                        data["fortnite"]["blacklist"].remove(str(user.display_name))
                    except ValueError:
                        data["fortnite"]["blacklist"].remove(user.id)
                    data_ = load_json("config.json")
                    data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    send(display_name,l('remove_from_list', name(user), l('blacklist')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('remove_from_list', name(user), l('blacklist')))
                else:
                    await reply(message, client, l('not_list', name(user), l('blacklist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id in blacklist:
            blacklist.remove(user.id)
            try:
                data["fortnite"]["blacklist"].remove(str(user.display_name))
            except ValueError:
                data["fortnite"]["blacklist"].remove(user.id)
            data_ = load_json("config.json")
            data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            send(display_name,l('remove_from_list', name(user), l('blacklist')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
            await reply(message, client, l('remove_from_list', name(user), l('blacklist')))
        else:
            await reply(message, client, l('not_list', name(user), l('blacklist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {name(user)}"
                text += f"\n{l('enter_to_remove_from_list', l('blacklist'))}"
                await reply(message, client, text)
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['addwhitelist']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['addwhitelist']}] [{l('name_or_id')}]")
                return
            if data["caseinsensitive"]:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and user.id not in whitelist}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and user.id not in whitelist}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if user.id not in whitelist:
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                if user.id not in whitelist:
                    whitelist.append(user.id)
                    if user.display_name:
                        data["fortnite"]["whitelist"].append(str(user.display_name))
                    else:
                        data["fortnite"]["whitelist"].append(user.id)
                    data_ = load_json("config.json")
                    data_["fortnite"]["whitelist"] = data["fortnite"]["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    send(display_name,l("add_to_list",name(user),l('whitelist')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l("add_to_list", name(user), l('whitelist')))
                else:
                    await reply(message, client, l("already_list", name(user), l('whitelist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
            if user.id not in whitelist:
                whitelist.append(user.id)
                if user.display_name:
                    data["fortnite"]["whitelist"].append(str(user.display_name))
                else:
                    data["fortnite"]["whitelist"].append(user.id)
                data_ = load_json("config.json")
                data_["fortnite"]["whitelist"] = data["fortnite"]["whitelist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                send(display_name,l("add_to_list",name(user),l('whitelist')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                await reply(message, client, l("add_to_list", name(user), l('whitelist')))
            else:
                await reply(message, client, l("already_list", name(user), l('whitelist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {name(user)}"
                text += f"\n{l('enter_to_add_to_list', l('whitelist'))}"
                await reply(message, client, text)
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['removewhitelist']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['removewhitelist']}] [{l('name_or_id')}]")
                return
            if data["caseinsensitive"]:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and user.id in whitelist}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and user.id in whitelist}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if user.id in whitelist:
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l("too_many_users", str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                if user.id in whitelist:
                    whitelist.remove(user.id)
                    try:
                        data["whitelist"].remove(str(user.display_name))
                    except ValueError:
                        data["whitelist"].remove(user.id)
                    data_ = load_json("config.json")
                    data_["whitelist"] = data["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    send(display_name,l("remove_from_list",name(user),l("whitelist")),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l("remove_from_list", name(user), l('whitelist')))
                else:
                    await reply(message, client, l("not_list", name(user), l('whitelist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id in whitelist:
            whitelist.remove(user.id)
            try:
                data["whitelist"].remove(str(user.display_name))
            except ValueError:
                data["whitelist"].remove(user.id)
            data_ = load_json("config.json")
            data_["whitelist"] = data["whitelist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            send(display_name,l("remove_from_list",name(user),l("whitelist")),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
            await reply(message, client, l("remove_from_list", name(user), l('whitelist')))
        else:
            await reply(message, client, l("not_list", name(user), l('whitelist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {name(user)}"
                text += f"\n{l('enter_to_remove_from_list', l('whitelist'))}"
                await reply(message, client, text)
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['addinvitelist']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['addinvitelist']}] [{l('name_or_id')}]")
                return
            if data["caseinsensitive"]:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and user.id not in client.invitelist}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and user.id not in client.invitelist}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if user.id not in client.invitelist:
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l("too_many_users", str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                if user.id not in client.invitelist:
                    client.invitelist.append(user.id)
                    if user.display_name:
                        data["fortnite"]["invitelist"].append(str(user.display_name))
                    else:
                        data["fortnite"]["invitelist"].append(user.id)
                    data_ = load_json("config.json")
                    data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    send(display_name,l("add_to_list",name(user),l("invitelist")),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l("add_to_list", name(user), l('invitelist')))
                else:
                    await reply(message, client, l("already_list", name(user), l('invitelist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id not in client.invitelist:
            client.invitelist.append(user.id)
            if user.display_name:
                data["fortnite"]["invitelist"].append(str(user.display_name))
            else:
                data["fortnite"]["invitelist"].append(user.id)
            data_ = load_json("config.json")
            data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            send(display_name,l("add_to_list",name(user),l("invitelist")),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
            await reply(message, client, l("add_to_list", name(user), l('invitelist')))
        else:
            await reply(message, client, l("already_list", name(user), l('invitelist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {name(user)}"
                text += f"\n{l('enter_to_add_to_list', l('invitelist'))}"
                await reply(message, client, text)
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['removeinvitelist']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['removeinvitelist']}] [{l('name_or_id')}]")
                return
            if data["caseinsensitive"]:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and user.id in client.invitelist}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and user.id in client.invitelist}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if user.id in client.invitelist:
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l("too_many_users", str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                if user.id in client.invitelist:
                    client.invitelist.remove(user.id)
                    try:
                        data["fortnite"]["invitelist"].remove(str(user.display_name))
                    except ValueError:
                        data["fortnite"]["invitelist"].remove(user.id)
                    data_ = load_json("config.json")
                    data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    send(display_name,l("remove_from_list",name(user),l("invitelist")),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l("remove_from_list", name(user), l('invitelist')))
                else:
                    await reply(message, client, l("not_list", name(user), l('invitelist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id in client.invitelist:
            client.invitelist.remove(user.id)
            try:
                data["fortnite"]["invitelist"].remove(str(user.display_name))
            except ValueError:
                data["fortnite"]["invitelist"].remove(user.id)
            data_ = load_json("config.json")
            data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            send(display_name,l("remove_from_list",name(user),l("invitelist")),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
            await reply(message, client, l("remove_from_list", name(user), l('invitelist')))
        else:
            await reply(message, client, l("not_list", name(user), l('invitelist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {name(user)}"
                text += f"\n{l('enter_to_remove_from_list', l('invitelist'))}"
                await reply(message, client, text)
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['get']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['get']}] [{l('name_or_id')}]")
                return
            if data["caseinsensitive"]:
                users = {str(member.display_name): member for member in client.party.members if content_ in jaconv.kata2hira(str(member.display_name).lower())}
            else:
                users = {str(member.display_name): member for member in client.party.members if content_ in str(member.display_name)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if client.party.get_member(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l("too_many_users", str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                member = client.party.get_member(user.id)
                if not member:
                    await reply(message, client, l("user_not_in_party"))
                    return
                send(display_name,f'{name(member)}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}',add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                if data['loglevel'] == 'debug':
                    send(display_name,json.dumps(member.meta.schema, indent=2),yellow,add_d=lambda x:f'```\n{x}\n```',add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                await reply(message, client, f'{name(member)}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        member = client.party.get_member(user.id)
        if not member:
            await reply(message, client, l("user_not_in_party"))
            return
        send(display_name,f'{name(member)}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}',add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
        if data['loglevel'] == 'debug':
            send(display_name,json.dumps(member.meta.schema, indent=2),yellow,add_d=lambda x:f'>>> {x}',add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
        await reply(message, client, f'{name(member)}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {name(user)}"
                text += f"\n{l('enter_to_get_userinfo')}"
                await reply(message, client, text)
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['friendcount']:
        try:
            send(display_name,f"{l('friendcount')}: {len(client.friends)}",add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
            await reply(message, client, f"{l('friendcount')}: {len(client.friends)}")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['pendingcount']:
        try:
            send(display_name,f"{l('pendingcount')}: {len(client.pending_friends)}\n{l('outbound')}: {len(client.outgoing_pending_friends)}\n{l('inbound')}: {len(client.incoming_pending_friends)}",add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
            await reply(message, client, f"{l('pendingcount')}: {len(client.pending_friends)}\n{l('outbound')}: {len(client.outgoing_pending_friends)}\n{l('inbound')}: {len(client.incoming_pending_friends)}")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['blockcount']:
        try:
            send(display_name,f"{l('blockcount')}: {len(client.blocked_users)}",add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
            await reply(message, client, f"{l('blockcount')}: {len(client.blocked_users)}")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['friendlist']:
        try:
            text = ''
            for friend in client.friends:
                client.add_cache(friend)
                text += f'\n{name(friend)}'
            send(display_name,text,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
            await reply(message, client, f'{text}')
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['pendinglist']:
        try:
            outgoing = ''
            incoming = ''
            for pending in client.pending_friends:
                client.add_cache(pending)
                if pending.outgoing:
                    outgoing += f'\n{name(pending)}'
                elif pending.incoming:
                    incoming += f'\n{name(pending)}'
            send(display_name,f"{l('outbound')}: {outgoing}\n{l('inbound')}: {incoming}",add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
            await reply(message, client, f"{l('outbound')}: {outgoing}\n{l('inbound')}: {incoming}")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['blocklist']:
        try:
            text = ''
            for block in client.blocked_users:
                client.add_cache(block)
                text += f'\n{name(block)}'
            send(display_name,text,add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
            await reply(message, client, f'{text}')
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['wait']:
        try:
            if not client.acceptinvite:
                if isinstance(message, fortnitepy.message.MessageBase) or isinstance(getattr(message,"base",None), fortnitepy.message.MessageBase):
                    if (not (message.author.id in [owner.id for owner in client.owner])
                        and not (message.author.id in whitelist and data['fortnite']['whitelist-ownercommand'])
                        and not (message.author.id in [owner.id for owner in dclient.owner])
                        and not (message.author.id in whitelist_ and data['discord']['whitelist-ownercommand'])):
                        await reply(message, client, l('invite_is_decline'))
                        return
            client.acceptinvite = False
            try:
                client.timer_.cancel()
            except AttributeError:
                pass
            client.timer_ = Timer(data['fortnite']['waitinterval'], client.inviteaccept)
            client.timer_.start()
            await reply(message, client, l('decline_invite_for', str(data['fortnite']['waitinterval'])))
        except Exception:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['join']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['join']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.has_friend(user.id)}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if client.has_friend(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                friend = client.get_friend(user.id)
                if not friend:
                    await reply(message, client, l('not_friend_with_user'))
                else:
                    await friend.join_party()
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            friend = client.get_friend(user.id)
            if not friend:
                await reply(message, client, l('not_friend_with_user'))
            else:
                await friend.join_party()
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('party_full_or_already_or_offline'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('party_notfound'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('party_private'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_joining_to_party'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {name(user)}"
                text += f"{l('enter_to_join_party')}"
                await reply(message, client, text)
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('party_full_or_already_or_offline'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('party_notfound'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('party_private'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_joining_to_party'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['joinid']:
        try:
            await client.join_party(party_id=args[1])
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('party_full_or_already'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('party_notfound'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('party_private'))
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"[{commands['join']}] [{l('party_id')}]")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['leave']:
        try:
            await client.party.me.leave()
            await reply(message, client, l('party_leave', client.party_id))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_leaving_party'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['invite']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['invite']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.has_friend(user.id)}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if client.has_friend(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                friend = client.get_friend(user.id)
                if not friend:
                    await reply(message, client, l('not_friend_with_user'))
                    return
                await friend.invite()
                await reply(message, client, l('user_invited', name(friend), client.party.id))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            friend = client.get_friend(user.id)
            if not friend:
                await reply(message, client, l('not_friend_with_user'))
                return
            await friend.invite()
            await reply(message, client, l('user_invited', name(friend), client.party.id))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('party_full_or_already'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_sending_partyinvite'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {name(user)}"
                text += f"\n{l('enter_to_invite_user')}"
                await reply(message, client, text)
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('party_full_or_already'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_sending_partyinvite'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['inviteall']:
        try:
            [loop.create_task(client.party.invite(inviteuser)) for inviteuser in client.invitelist]
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['message']:
        try:
            text = rawcontent.split(' : ')
            if data['caseinsensitive']:
                users = {str(user.display_name): user for user in cache_users.values() if text[0] in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.has_friend(user.id)}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if text[0] in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id)}
            try:
                user = await client.fetch_user(text[0])
                if user:
                    if client.has_friend(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                friend = client.get_friend(user.id)
                if not friend:
                    await reply(message, client, l('not_friend_with_user'))
                    return
                await friend.send(text[1])
                await reply(message, client, l('user_sent', name(friend), text[1]))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            friend = client.get_friend(user.id)
            if not friend:
                await reply(message, client, l('not_friend_with_user'))
                return
            await friend.send(text[1])
            await reply(message, client, l('user_sent', name(friend), text[1]))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l("error_while_requesting_userinfo"))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user, "text": text} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {name(user)}"
                text += f"\n{l('enter_to_send')}"
                await reply(message, client, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l("error_while_requesting_userinfo"))
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"[{commands['message']}] [{l('name_or_id')}] : [{l('content')}]")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['now_day']:
            await reply(message, client, f"今日は {int(now1())}年 - {int(now2())}月 / {int(now3())}日 です")

    elif args[0] in commands['now_time']:
            await reply(message, client, f"只今の時刻は {int(now4())}時 : {int(now5())}分 : {int(now6())}秒 です")


    elif args[0] in commands['i_news']:
            # WebサイトのURLを指定
            url = "https://news.infoseek.co.jp/g/"
            # Requestsを利用してWebページを取得する
            r = requests.get(url)

            # BeautifulSoupを利用してWebページを解析する
            soup = BeautifulSoup(r.text, 'html.parser')

            # soup.find_allを利用して、見出しのタイトルを取得する
            elems = soup.find_all("a", class_="news-flash-list__title")
            for e in elems:
             await reply(message, client, f"{e.getText()}")


    elif args[0] in commands['y_news']:
            # WebサイトのURLを指定
            url = "https://news.yahoo.co.jp"
            # Requestsを利用してWebページを取得する
            r = requests.get(url)

            # BeautifulSoupを利用してWebページを解析する
            soup = BeautifulSoup(r.text, 'html.parser')

            # soup.find_allを利用して、見出しのタイトルを取得する
            elems = soup.find_all("a", class_="sc-kIPQKe eMCmdt")
            for e in elems:
             await reply(message, client, f"{e.getText()}")


    elif args[0] in commands['y_news_f']:
            # WebサイトのURLを指定
            url = "https://news.yahoo.co.jp/flash"
            # Requestsを利用してWebページを取得する
            r = requests.get(url)

            # BeautifulSoupを利用してWebページを解析する
            soup = BeautifulSoup(r.text, 'html.parser')

            # soup.find_allを利用して、見出しのタイトルを取得する
            elems = soup.find_all("p", class_="sc-iysEgW clKYKn")
            for e in elems:
             await reply(message, client, f"{e.getText()}")


    elif args[0] in commands['quake']:
            # WebサイトのURLを指定
            url = "https://weather.goo.ne.jp/earthquake/"
            # Requestsを利用してWebページを取得する
            r = requests.get(url)

            # BeautifulSoupを利用してWebページを解析する
            soup = BeautifulSoup(r.text, 'html.parser')

            # soup.find_allを利用して、見出しのタイトルを取得する
            elems = soup.find_all("dd", class_="w75")

            for e in elems:
              await reply(message, client, f"地震情報: {e.getText()}")


    elif args[0] in commands['tokushima']:
            # WebサイトのURLを指定
            url = "https://weather.yahoo.co.jp/weather/36/"
            # Requestsを利用してWebページを取得する
            r = requests.get(url)

            # BeautifulSoupを利用してWebページを解析する
            soup = BeautifulSoup(r.text, 'html.parser')

            # soup.find_allを利用して、見出しのタイトルを取得する
            elems = soup.find_all("p", class_="text")

            for e in elems:
                await reply(message, client, f"{e.getText()}")





    elif args[0] in commands['partymessage']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['partymessage']}] [{l('content')}]")
                return
            await client.party.send(rawcontent)
            await reply(message, client, l('party_sent', client.party.id, rawcontent))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['sendall']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['sendall']}] [{l('content')}]")
                return
            tasks = {}
            for client_ in loadedclients:
                mes = AllMessage(rawcontent, message.author, client_, message)
                task = loop.create_task(process_command(mes))
                tasks[client_] = [task, mes]
            await asyncio.gather(*[i[0] for i in tasks.values()])
            for client_,list_ in tasks.items():
                result = list_[1].result
                if result.get(client_.user.id):
                    results = '\n'.join(result[client_.user.id])
                    await reply(message, client, f"[{name(client_.user)}] {results}")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['status']:
        try:
            client.status_ = rawcontent
            await client.change_status()
            await reply(message, client, l('set_to', l('status'), rawcontent))
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"[{commands['status']}] [{l('content')}]")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['avatar']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['avatar']}] [ID]")
                return
            if len(args) > 4:
                background_colors = [args[2], args[3], args[4]]
            elif len(args) == 2:
                background_colors = None
            else:
                background_colors = getattr(fortnitepy.KairosBackgroundColorPreset, args[2])
            avatar = fortnitepy.Avatar(asset=args[1], background_colors=background_colors)
            client.set_avatar(avatar)
            await reply(message, client, l('set_to', l('avatar'), f"{args[1]}, {background_colors}"))
        except AttributeError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('color_must_be'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['banner']:
        try:
            await client.party.me.edit_and_keep(partial(client.party.me.set_banner,args[1],args[2],client.party.me.banner[2]))
            await reply(message, client, l('set_to', l('banner'), f"{args[1]}, {args[2]}"))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_changing_asset'))
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"[{commands['banner']}] [{l('bannerid')}] [{l('color')}]")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['level']:
        try:
            await client.party.me.edit_and_keep(partial(client.party.me.set_banner,client.party.me.banner[0],client.party.me.banner[1],int(args[1])))
            await reply(message, client, l('set_to', l('level'), args[1]))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_changing_asset'))
        except ValueError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('must_be_int'))
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"[{commands['level']}] [{l('level')}]")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['bp']:
        try:
            await client.party.me.edit_and_keep(partial(client.party.me.set_battlepass_info,True,args[1],args[2],args[3]))
            await reply(message, client, l('set_to', l('bpinfo'), f"{l('tier')}: {args[1]}, {l('xpboost')}: {args[2]}, {l('friendxpboost')}: {args[3]}"))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_changing_bpinfo'))
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"[{commands['bp']}] [{l('tier')}] [{l('xpboost')}] [{l('friendxpboost')}]")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['privacy']:
        try:
            privacies = [
                "privacy_public",
                "privacy_friends_allow_friends_of_friends",
                "privacy_friends",
                "privacy_private_allow_friends_of_friends",
                "privacy_private"
            ]
            for privacy in privacies:
                if args[1] in commands[privacy]:
                    priv = getattr(PartyPrivacy,privacy.replace("privacy_","",1).upper()).value
                    await client.party.set_privacy(priv)
                    await reply(message, client, l('set_to', l('privacy'), l(privacy.replace("privacy_","",1))))
                    break
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('not_party_leader'))
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"[{commands['privacy']}] [[{commands['privacy_public']}] / [{commands['privacy_friends_allow_friends_of_friends']}] / [{commands['privacy_friends']}] / [{commands['privacy_private_allow_friends_of_friends']}] / [{commands['privacy_private']}]]")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['getuser']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['getuser']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    users[str(user.display_name)] = user
                    client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            text = str()
            for user in users.values():
                text += f'\n{name(user)}'
            send(display_name,text)
            await reply(message, client, text)
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['getfriend']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['getfriend']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.has_friend(user.id)}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if client.has_friend(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            text = str()
            for user in users.values():
                friend = client.get_friend(user.id)
                if not friend:
                    return
                if not friend.nickname:
                    text += f'\n{str(friend.display_name)} / {friend.id}'
                else:
                    text += f'\n{friend.nickname}({str(friend.display_name)}) / {friend.id}'
                if friend.last_presence and friend.last_presence.avatar:
                    text += f"\n{l('avatar')}: {friend.last_presence.avatar.asset}"
                if friend.last_logout:
                    text += "\n{1}: {0.year}/{0.month}/{0.day} {0.hour}:{0.minute}:{0.second}".format(friend.last_logout, l('lastlogin'))
            send(display_name,text)
            await reply(message, client, text)
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['getpending']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['getpending']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.is_pending(user.id)}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if client.is_pending(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            text = str()
            for user in users.values():
                pending = client.get_pending_friend(user.id)
                if not pending:
                    return
                text += f'\n{str(pending.display_name)} / {pending.id}'
            send(display_name,text)
            await reply(message, client, text)
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['getblock']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['getblock']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.is_blocked(user.id)}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if client.is_blocked(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            text = str()
            for user in users.values():
                block = client.get_blocked_user(user.id)
                if not block:
                    return
                text += f'\n{str(block.display_name)} / {block.id}'
            send(display_name,text)
            await reply(message, client, text)
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['info']:
        try:
            if args[1] in commands['info_party']:
                text = str()
                text += f"\n{l('member_count')} {client.party.member_count} 人です"
                for member in client.party.members:
                    client.add_cache(member)
                    if data['loglevel'] == 'normal':
                        text += f'\n{str(member.display_name)}　 ({member.id})'
                    else:
                        text += f'\n{str(member.display_name)} / {member.id}'
                send(display_name,text)
                await reply(message, client, text)
                if data['loglevel'] == 'debug':
                    send(display_name,json.dumps(client.party.meta.schema,indent=4),yellow,add_d=lambda x:f'```\n{x}\n```')

            elif True in [args[1] in commands[key] for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "id")]:
                type_ = convert_to_type(args[1])
                if rawcontent2 == '':
                    await reply(message, client, f"[{commands[convert_to_old_type(type_)]}] [ID]")
                    return
                result = await loop.run_in_executor(None, search_item, data["search-lang"], "id", rawcontent2, type_)
                if not result and data["sub-search-lang"] != data["search-lang"]:
                    result = await loop.run_in_executor(None, search_item, data["sub-search-lang"], "id", rawcontent2, type_)
                if not result:
                    await reply(message, client, l('item_notfound'))
                else:
                    if len(result) > search_max:
                        await reply(message, client, l('too_many_items', str(len(result))))
                        return
                    if len(result) == 1:
                        await reply(message, client, f"{convert_backend_type(result[0]['backendType'])}: {result[0]['name']} | {result[0]['id']}\n{result[0]['description']}\n{result[0]['rarity']}\n{result[0]['set']}")
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {convert_backend_type(item['backendType'])}: {item['name']} | {item['id']}"
                        text += f"\n{l('enter_to_show_info')}"
                        await reply(message, client, text)
                        client.select[message.author.id] = {
                            "exec": [
                                """\
                                await reply(message, client, f"{convert_backend_type(item['backendType'])}: {item['name']} | {item['id']}\n{item['description']}\n{item['rarity']}\n{item['set']}")""" for item in result
                                ],
                                "variable": [
                                    {"item": item} for item in result
                                ]
                            }

            elif True in  [args[1] in commands[key] for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "item")]:
                type_ = convert_to_type(args[1])
                if rawcontent2 == '':
                    await reply(message, client, f"[{commands[convert_to_old_type(type_)]}] [{l('itemname')}]")
                    return
                result = await loop.run_in_executor(None, search_item, data["search-lang"], "name", rawcontent2, type_)
                if not result and data["sub-search-lang"] != data["search-lang"]:
                    result = await loop.run_in_executor(None, search_item, data["sub-search-lang"], "name", rawcontent2, type_)
                if not result:
                    await reply(message, client, l('item_notfound'))
                else:
                    if len(result) > search_max:
                        await reply(message, client, l('too_many_items', str(len(result))))
                        return
                    if len(result) == 1:
                        await reply(message, client, f"{convert_backend_type(result[0]['backendType'])}: {result[0]['name']} | {result[0]['id']}\n{result[0]['description']}\n{result[0]['rarity']}\n{result[0]['set']}")
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {convert_backend_type(item['backendType'])}: {item['name']} | {item['id']}"
                        text += f"\n{l('enter_to_show_info')}"
                        await reply(message, client, text)
                        client.select[message.author.id] = {
                            "exec": [
                                """\
                                await reply(message, client, f"{convert_backend_type(item['backendType'])}: {item['name']} | {item['id']}\n{item['description']}\n{item['rarity']}\n{item['set']}")""" for item in result
                            ],
                            "variable": [
                                {"item": item} for item in result
                            ]
                        }
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"[{commands['info']}] [[{commands['info_party']}] / [{commands['item']}] / [{commands['id']}] / [{commands['outfit']}] / [{commands['backpack']}] / [{commands['pickaxe']}] / [{commands['emote']}]]")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['pending']:
        try:
            pendings = []
            for pending in client.pending_friends:
                client.add_cache(pending)
                if pending.incoming:
                    pendings.append(pending)
            if args[1] in commands['true']:
                for pending in pendings:
                    try:
                        await pending.accept()
                        await reply(message, client, l('add_friend', f'{str(pending.display_name)} / {pending.id}'))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        await reply(message, client, l('error_while_sending_friendrequest'))
                        return
                    except Exception:
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        await reply(message, client, l('error'))
                        return
            elif args[1] in commands['false']:
                for pending in pendings:
                    try:
                        await pending.decline()
                        await reply(message, client, l('friend_request_decline', f'{str(pending.display_name)} / {pending.id}'))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        await reply(message, client, l('error_while_declining_friendrequest'))
                        return
                    except Exception:
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        await reply(message, client, l('error'))
                        return
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"[{commands['pending']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['removepending']:
        try:
            pendings = []
            for pending in client.pending_friends:
                client.add_cache(pending)
                if pending.outgoing:
                    pendings.append(pending)
            for pending in pendings:
                try:
                    await pending.cancel()
                    await reply(message, client, l('remove_pending', f'{str(pending.display_name)} / {pending.id}'))
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l('error_while_removing_friendrequest'))
                    return
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l('error'))
                    return
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['addfriend']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['addfriend']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and not client.has_friend(user.id)}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and not client.has_friend(user.id)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if not client.has_friend(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache( user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                if client.has_friend(user.id):
                    await reply(message, client, l('already_friend'))
                    return
                await client.add_friend(user.id)
                await reply(message, client, l('friend_request_to', f'{name(user)}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.has_friend(user.id):
                await reply(message, client, l('already_friend'))
                return
            await client.add_friend(user.id)
            await reply(message, client, l('friend_request_to', f'{name(user)}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_sending_friendrequest'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {name(user)}"
                text += f"\n{l('enter_to_send_friendrequest')}"
                await reply(message, client, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_sending_friendrequest'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['removefriend']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['removefriend']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.has_friend(user.id)}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if client.has_friend(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                if not client.has_friend(user.id):
                    await reply(message, client, l('not_friend_with_user'))
                    return
                await client.remove_or_decline_friend(user.id)
                await reply(message, client, l('remove_friend', f'{name(user)}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if not client.has_friend(user.id):
                await reply(message, client, l('not_friend_with_user'))
                return
            await client.remove_or_decline_friend(user.id)
            await reply(message, client, l('remove_friend', f'{name(user)}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_removing_friend')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {name(user)}"
                text += f"\n{l('enter_to_remove_friend')}"
                await reply(message, client, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_removing_friend'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['removeallfriend']:
        try:
            friend_count = len(client.friends)
            await client.remove_all_friends()
            await reply(message, client, l('remove_allfriend',friend_count))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_removing_friend'))
        except Exception:
            send(name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['remove_offline_for']:
        try:
            kwargs = {}
            kwargs["days"] = int(args[1])
            kwargs["hours"] = int(args[2]) if args[2:3] else 0
            kwargs["minutes"] = int(args[3]) if args[3:4] else 0
            offline_for = datetime.timedelta(**kwargs)
            utcnow = datetime.datetime.utcnow()
            event = asyncio.Event(loop=loop)
            removed = []

            async def _(friend: fortnitepy.Friend):
                last_logout = None
                if friend.last_logout:
                    last_logout = friend.last_logout
                elif friend.created_at > client.booted_utc:
                    last_logout = await friend.fetch_last_logout()
                if last_logout and ((utcnow - last_logout) > offline_for):
                    if event.is_set():
                        await event.wait()
                    try:
                        await friend.remove()
                    except fortnitepy.HTTPException as e:
                        if e.message_code != "errors.com.epicgames.common.throttled":
                            raise
                        if "Operation access is limited by throttling policy" not in e.message:
                            raise
                        event.set()
                        await asyncio.sleep(int(e.message_vars[0]) + 1)
                        await friend.remove()
                        event.clear()
                    removed.append(friend)
            max_worker = 5
            worker = 0
            def dec(*args):
                nonlocal worker
                worker -= 1

            tasks = []
            val = len(client.friends)
            for num,friend in enumerate(client.friends):
                if worker >= max_worker:
                    await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
                worker += 1
                task = loop.create_task(_(friend))
                task.add_done_callback(dec)
                tasks.append(task)
            await asyncio.gather(*tasks)
            await reply(message, client, l('remove_allfriend',len(removed)))
            await asyncio.sleep(2)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_removing_friend'))
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"[{commands['remove_offline_for']}] [{l('day')}] [{l('hour')}]({l('optional')}) [{l('minute')}]({l('optional')})")
        except Exception:
            send(name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['acceptpending']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['acceptpending']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.is_pending(user.id)}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if client.is_pending(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                if not client.is_pending(user.id):
                    await reply(message, client, l('not_pending_with_user'))
                    return
                await client.accept_friend(user.id)
                await reply(message, client, l('friend_add', f'{name(user)}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if not client.is_pending(user.id):
                await reply(message, client, l('not_pending_with_user'))
                return
            await client.accept_friend(user.id)
            await reply(message, client, l('friend_add', f'{name(user)}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_accepting_friendrequest'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {name(user)}"
                text += f"\n{l('enter_to_accept_pending')}"
                await reply(message, client, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_accepting_friendrequest'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['declinepending']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['declinepending']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.is_pending(user.id)}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if client.is_pending(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                if not client.is_pending(user.id):
                    await reply(message, client, l('nor_pending_with_user'))
                    return
                await client.remove_or_decline_friend(user.id)
                await reply(message, client, l('friend_request_decline', f'{name(user)}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if not client.is_pending(user.id):
                await reply(message, client, l('nor_pending_with_user'))
                return
            await client.remove_or_decline_friend(user.id)
            await reply(message, client, l('friend_request_decline', f'{name(user)}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_declining_friendrequest'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {name(user)}"
                text += f"\n{l('enter_to_decline_pending')}"
                await reply(message, client, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_declining_friendrequest'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['blockfriend']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['blockfriend']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and not client.is_blocked(user.id)}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and not client.is_blocked(user.id)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if not client.is_blocked(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                if client.is_blocked(user.id):
                    await reply(message, client, l('already_block'))
                    return
                await client.block_user(user.id)
                await reply(message, client, l('block_user', f'{name(user)}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_blocked(user.id):
                await reply(message, client, l('already_block'))
                return
            await client.block_user(user.id)
            await reply(message, client, l('block_user', f'{name(user)}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_blocking_user'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1}, {name(user)}"
                text += f"\n{l('enter_to_block_user')}"
                await reply(message, client, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_blocking_user'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['unblockfriend']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['unblockfriend']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.is_blocked(user.id)}
            else:
                users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if client.is_blocked(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                if not client.is_blocked(user.id):
                    await reply(message, client, l('not_block'))
                    return
                await client.unblock_user(user.id)
                await reply(message, client, l('unblock_user', f'{name(user)}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if not client.is_blocked(user.id):
                await reply(message, client, l('not_block'))
                return
            await client.unblock_user(user.id)
            await reply(message, client, l('unblock_user', f'{name(user)}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_unblocking_user'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1}, {name(user)}"
                text += f"\n{l('enter_to_unblock_user')}"
                await reply(message, client, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_unblocking_user'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['voice']:
        try:
            if args[1] in commands['true']:
                client.voice = True
                await client.enable_voice()
                send(display_name,l('set_to', 'voice', l('on')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                await reply(message, client, l('set_to', 'voice', l('on')))
            elif args[1] in commands['false']:
                client.voice = False
                await client.disable_voice()
                send(display_name,l('set_to', 'voice', l('off')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                await reply(message, client, l('set_to', 'voice', l('off')))
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"[{commands[key]}] [[{commands['true']}] / [{commands['false']}]]")
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('not_party_leader'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))
        return

    elif args[0] in commands['chatban']:
        try:
            reason = rawcontent.split(' : ')
            if rawcontent == '':
                await reply(message, client, f"[{commands['chatban']}] [{l('name_or_id')}] : [{l('reason')}({l('optional')})]")
                return
            if data['caseinsensitive']:
                users = {str(member.display_name): member for member in client.party.members if content_ in jaconv.kata2hira(str(member.display_name).lower())}
            else:
                users = {str(member.display_name): member for member in client.party.members if content_ in str(member.display_name)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if client.party.get_member(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                member = client.party.get_member(user.id)
                if not member:
                    await reply(message, client, l('user_not_in_party'))
                    return
                try:
                    await member.chatban(reason[1])
                except IndexError:
                    await member.chatban()
                await reply(message, client, l('chatban_user', f'{name(user)}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            member = client.party.get_member(user.id)
            if not member:
                await reply(message, client, l('user_not_in_party'))
                return
            try:
                await member.chatban(reason[1])
            except IndexError:
                await member.chatban()
            await reply(message, client, l('chatban_user', f'{name(user)}'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('not_party_leader'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('user_notfound'))
        except ValueError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('already_chatban'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user, "reason": reason} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1}, {name(user)}"
                text += f"\n{l('enter_to_chatban_user')}"
                await reply(message, client, text)
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('not_party_leader'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('user_notfound'))
        except ValueError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('already_chatban'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['promote']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['promote']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(member.display_name): member for member in client.party.members if content_ in jaconv.kata2hira(str(member.display_name).lower())}
            else:
                users = {str(member.display_name): member for member in client.party.members if content_ in str(member.display_name)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if client.party.get_member(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                member = client.party.get_member(user.id)
                if not member:
                    await reply(message, client, l('user_not_in_party'))
                    return
                await member.promote()
                await reply(message, client, l('promote_user', f'{name(user)}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            member = client.party.get_member(user.id)
            if not member:
                await reply(message, client, l('user_not_in_party'))
                return
            await member.promote()
            await reply(message, client, l('promote_user', f'{name(user)}'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('not_party_leader'))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('already_party_leader'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_promoting_party_leader'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1}, {name(user)}"
                text += f"\n{l('enter_to_promote_user')}"
                await reply(message, client, text)
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('not_party_leader'))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('already_party_leader'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_promoting_party_leader'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['kick']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['kick']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(member.display_name): member for member in client.party.members if content_ in jaconv.kata2hira(str(member.display_name).lower())}
            else:
                users = {str(member.display_name): member for member in client.party.members if content_ in str(member.display_name)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if client.party.get_member(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                member = client.party.get_member(user.id)
                if not member:
                    await reply(message, client, l('user_not_in_party'))
                    return
                await member.kick()
                await reply(message, client, l('kick_user', f'{name(user)}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            member = client.party.get_member(user.id)
            if not member:
                await reply(message, client, l('user_not_in_party'))
                return
            await member.kick()
            await reply(message, client, l('kick_user', f'{name(user)}'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('not_party_leader'))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('cant_kick_yourself'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_kicking_user'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1}, {name(user)}"
                text += f"\n{l('enter_to_kick_user')}"
                await reply(message, client, text)
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('not_party_leader'))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('cant_kick_yourself'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_kicking_user'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))





    elif args[0] in commands['test']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['test']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(member.id): member for member in client.party.members if content_ in jaconv.kata2hira(str(member.id).lower())}
            else:
                users = {str(member.id): member for member in client.party.members if content_ in str(member.id)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if client.party.get_member(user.id):
                        users[str(user.id)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('not_id'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                member = client.party.get_member(user.id)
                if not member:
                    await reply(message, client, l('user_not_in_party'))
                    return
                await member.kick()
                await reply(message, client, l('kick_user', f'{name(user)}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            member = client.party.get_member(user.id)
            if not member:
                await reply(message, client, l('not_id'))
                return
            await member.kick()
            await reply(message, client, l('kick_user', f'{name(user)}'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('not_party_leader'))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('cant_kick_yourself'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_kicking_user'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1}, {name(user)}"
                text += f"\n{l('enter_to_kick_user')}"
                await reply(message, client, text)
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('not_party_leader'))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('cant_kick_yourself'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_kicking_user'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))







    elif args[0] in commands['hide']:
        try:
            if rawcontent == '':
                await client.hide()
                await reply(message, client, l('hide_all_user'))
            else:
                if data['caseinsensitive']:
                    users = {str(member.display_name): member for member in client.party.members if content_ in jaconv.kata2hira(str(member.display_name).lower())}
                else:
                    users = {str(member.display_name): member for member in client.party.members if content_ in str(member.display_name)}
                try:
                    user = await client.fetch_user(rawcontent)
                    if user:
                        if client.party.get_member(user.id):
                            users[str(user.display_name)] = user
                            client.add_cache(user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > search_max:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    return
                if len(users) == 1:
                    user = tuple(users.values())[0]
                    member = client.party.get_member(user.id)
                    if not member:
                        await reply(message, client, l('user_not_in_party'))
                        return
                    await client.hide(member.id)
                    await reply(message, client, l('hide_user', f'{name(user)}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                member = client.party.get_member(user.id)
                if not member:
                    await reply(message, client, l('user_not_in_party'))
                    return
                await client.hide(member.id)
                await reply(message, client, l('hide_user', f'{name(user)}'))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('not_party_leader'))
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('user_not_in_party'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_hide_user')}"
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('not_party_leader'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('user_not_in_party'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['show']:
        try:
            if rawcontent == '':
                await client.show()
                await reply(message, client, l('show_all_user'))
            else:
                if data['caseinsensitive']:
                    users = {str(member.display_name): member for member in client.party.members if content_ in jaconv.kata2hira(str(member.display_name).lower())}
                else:
                    users = {str(member.display_name): member for member in client.party.members if content_ in str(member.display_name)}
                try:
                    user = await client.fetch_user(rawcontent)
                    if user:
                        if client.party.get_member(user.id):
                            users[str(user.display_name)] = user
                            client.add_cache(user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > search_max:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    return
                if len(users) == 1:
                    user = tuple(users.values())[0]
                    member = client.party.get_member(user.id)
                    if not member:
                        await reply(message, client, l('user_not_in_party'))
                        return
                    await client.show(member.id)
                    await reply(message, client, l('show_user', f'{name(user)}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                member = client.party.get_member(user.id)
                if not member:
                    await reply(message, client, l('user_not_in_party'))
                    return
                await client.show(member.id)
                await reply(message, client, l('show_user', f'{name(user)}'))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('not_party_leader'))
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('user_not_in_party'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_show_user')}"
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('not_party_leader'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('user_not_in_party'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['ready']:
        try:
            await client.party.me.set_ready(fortnitepy.ReadyState.READY)
            await reply(message, client, l('set_to', l('readystate'), l('ready')))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['unready']:
        try:
            await client.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
            await reply(message, client, l('set_to', l('readystate'), l('unready')))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['sitout']:
        try:
            await client.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
            await reply(message, client, l('set_to', l('readystate'), l('sitout')))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['match']:
        try:
            await client.party.me.set_in_match(players_left=int(args[1]) if args[1:2] else 100)
            await reply(message, client, l('set_to', l('matchstate'), l('remaining', args[1] if args[1:2] else "100")))
        except ValueError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('remaining_must_be_between_0_and_255'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['unmatch']:
        try:
            await client.party.me.clear_in_match()
            await reply(message, client, l('set_to', l('matchstate'), l('off')))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['swap']:
        try:
            if rawcontent == '':
                await reply(message, client, f"[{commands['swap']}] [{l('name_or_id')}]")
                return
            if data['caseinsensitive']:
                users = {str(member.display_name): member for member in client.party.members if content_ in jaconv.kata2hira(str(member.display_name).lower())}
            else:
                users = {str(member.display_name): member for member in client.party.members if content_ in str(member.display_name)}
            try:
                user = await client.fetch_user(rawcontent)
                if user:
                    if client.party.get_member(user.id):
                        users[str(user.display_name)] = user
                        client.add_cache(user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            if len(users) > search_max:
                await reply(message, client, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, client, l('user_notfound'))
                return
            if len(users) == 1:
                user = tuple(users.values())[0]
                member = client.party.get_member(user.id)
                if not member:
                    await reply(message, client, l('user_not_in_party'))
                    return
                real_members = client.party.meta.squad_assignments
                assignments = client.visual_members
                await member.swap_position()
                await reply(message, client, l('swap_user', f'{name(user)}'))
                if client.party.me.leader:
                    await asyncio.sleep(0.5)
                    prop = client.party.meta.set_squad_assignments(assignments)
                    await client.party.patch(updated=prop)
                    await asyncio.sleep(2)
                    client.party.meta.set_squad_assignments(real_members)
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            member = client.party.get_member(user.id)
            if not member:
                await reply(message, client, l('user_not_in_party'))
                return
            real_members = client.party.meta.squad_assignments
            assignments = client.visual_members
            await member.swap_position()
            await reply(message, client, l('swap_user', f'{name(user)}}'))
            if client.party.me.leader:
                await asyncio.sleep(0.5)
                prop = client.party.meta.set_squad_assignments(assignments)
                await client.party.patch(updated=prop)
                client.party.meta.set_squad_assignments(real_members)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_swapping_user'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {name(user)}"
                text += f"\n{l('enter_to_swap_user')}"
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_swapping_user'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['stop']:
        try:
            client.stopcheck = True
            if await client.change_asset(message.author.id, "Emote", ""):
                await reply(message, client, l('stopped'))
            else:
                await reply(message, client, l('locked'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['setenlightenment']:
        try:
            if await client.change_asset(message.author.id, "Outfit", client.party.me.outfit, client.party.me.outfit_variants,(args[1],args[2])) is True:
                await reply(message, client, l('set_to', 'enlightenment', f'{args[1]}, {args[2]}'))
            else:
                await reply(message, client, l('locked'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_changing_asset'))
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"[{commands['setenlightenment']}] [{l('number')}] [{l('number')}]")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['addeditems']:
        try:
            async with aiohttp.ClientSession() as session:
                res = await session.get("https://benbotfn.tk/api/v1/newCosmetics")
                res = await res.json()
            flag = False
            items = res["items"]
            for item in items:
                if client.stopcheck:
                    client.stopcheck = False
                    break
                if item["backendType"] in ignoretype:
                    continue
                if await client.change_asset(message.author.id, convert_backend_type(item["backendType"]), item["id"]):
                    if data['loglevel'] == 'normal':
                        await reply(message, client, f"new {item['shortDescription']} is {item['name']}")
                    else:
                        await reply(message, client, f"new {item['shortDescription']} is {item['name']}")
                    await asyncio.sleep(3)
            else:
                await reply(message, client, l('all_end', l('addeditem')))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['shopitems']:
        try:
            store = await client.fetch_item_shop()
            items = []
            for item in (store.featured_items
                         + store.daily_items
                         + store.special_featured_items
                         + store.special_daily_items):
                for grant in item.grants:
                    if convert_backend_type(grant["type"]) in ignoretype:
                        continue
                    item = {
                        "id": grant["asset"],
                        "type": convert_to_asset(convert_to_old_type(convert_backend_type(grant["type"]))),
                        "backendType": grant["type"]
                    }
                    items.append(item)
            for item in items:
                if client.stopcheck:
                    client.stopcheck = False
                    break
                if item["backendType"] in ignoretype:
                    continue
                if await client.change_asset(message.author.id, convert_backend_type(item["backendType"]), item["id"]):
                    i = await loop.run_in_executor(None,search_item,data["search-lang"],"id",item["id"],convert_backend_type(item["backendType"]))
                    if i:
                        i = i[0]
                        if data['loglevel'] == 'normal':
                            await reply(message, client, f"shop >> {i['shortDescription']}: {i['name']}")
                        else:
                            await reply(message, client, f"shop >> {i['shortDescription']}: {i['name']}")
                    else:
                        await reply(message, client, item["id"])
                    await asyncio.sleep(5)
            else:
                await reply(message, client, l('all_end', l('shopitem')))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif True in [args[0] in commands[key] for key in ("alloutfit", "allbackpack", "allpet", "allpickaxe", "allemote", "allemoji", "alltoy")]:
        type_ = convert_to_type(args[0])
        try:
            if getattr(client,f"{convert_to_old_type(type_)}lock") and client.lock_check(message.author.id):
                await reply(message, client, l('locked'))
                return
            with open(f'items/{type_}_{data["search-lang"]}.json', 'r', encoding='utf-8') as f:
                allitem = json.load(f)
            for item in allitem:
                if client.stopcheck:
                    client.stopcheck = False
                    break
                await client.change_asset(message.author.id, type_, item["id"])
                await asyncio.sleep(2)
            else:
                await reply(message, client, l('all_end', l(convert_to_old_type(type_))))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif True in [args[0] in commands[key] for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "id")]:
        type_ = convert_to_type(args[0])
        if rawcontent == '':
            await reply(message, client, f"[{commands[convert_to_old_type(type_)]}] [ID]")
            return
        try:
            result = await loop.run_in_executor(None, search_item, data["search-lang"], "id", rawcontent, type_)
            if result is None and data["sub-search-lang"] != data["search-lang"]:
                result = await loop.run_in_executor(None, search_item, data["sub-search-lang"], "id", rawcontent, type_)
            if result is None:
                await reply(message, client, l('item_notfound'))
            else:
                if len(result) > search_max:
                    await reply(message, client, l('too_many_items', str(len(result))))
                    return
                if len(result) == 1:
                    if await client.change_asset(message.author.id, convert_backend_type(result[0]['backendType']), result[0]['id']) is True:
                        if data['loglevel'] == 'normal':
                            await reply(message, client, f"{result[0]['shortDescription']}: {result[0]['name']}")
                        else:
                            await reply(message, client, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}")
                    else:
                        await reply(message, client, l('locked'))
                else:
                    text = str()
                    for count, item in enumerate(result):
                        if data['loglevel'] == 'normal':
                            text += f"\n{count+1} {item['shortDescription']}: {item['name']}"
                        else:
                            text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                    text += f"\n{l('enter_to_change_asset')}"
                    await reply(message, client, text)
                    client.select[message.author.id] = {
                        "exec": [
                            """\
                            if await client.change_asset(message.author.id, convert_backend_type(item['backendType']), item['id']) is True:
                                if data['loglevel'] == 'normal':
                                    await reply(message, client, f"{item['shortDescription']}: {item['name']}")
                                else:
                                    await reply(message, client, f"{item['shortDescription']}: {item['name']} | {item['id']}")
                            else:
                                await reply(message, client, l('locked'))""" for item in result
                        ],
                        "variable": [
                            {"item": item} for item in result
                        ]
                    }
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_changing_asset'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif True in [args[0] in commands[key] for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "item")]:
        type_ = convert_to_type(args[0])
        if rawcontent == '':
            await reply(message, client, f"[{commands[convert_to_old_type(type_)]}] [{l('itemname')}]")
            return
        try:
            result = await loop.run_in_executor(None, search_item, data["search-lang"], "name", rawcontent, type_)
            if result is None and data["sub-search-lang"] != data["search-lang"]:
                result = await loop.run_in_executor(None, search_item, data["sub-search-lang"], "name", rawcontent, type_)
            if result is None:
                await reply(message, client, l('item_notfound'))
            else:
                if len(result) > search_max:
                    await reply(message, client, l('too_many_items', str(len(result))))
                    return
                if len(result) == 1:
                    if await client.change_asset(message.author.id, convert_backend_type(result[0]['backendType']), result[0]['id']) is True:
                        if data['loglevel'] == 'normal':
                            await reply(message, client, f"{result[0]['shortDescription']}: {result[0]['name']}")
                        else:
                            await reply(message, client, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}")
                    else:
                        await reply(message, client, l('locked'))
                else:
                    text = str()
                    for count, item in enumerate(result):
                        if data['loglevel'] == 'normal':
                            text += f"\n{count+1} {item['shortDescription']}: {item['name']}"
                        else:
                            text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                    text += f"\n{l('enter_to_change_asset')}"
                    await reply(message, client, text)
                    client.select[message.author.id] = {
                        "exec": [
                            """\
                            if await client.change_asset(message.author.id, convert_backend_type(item['backendType']), item['id']) is True:
                                if data['loglevel'] == 'normal':
                                    await reply(message, client, f"{item['shortDescription']}: {item['name']}")
                                else:
                                    await reply(message, client, f"{item['shortDescription']}: {item['name']} | {item['id']}")
                            else:
                                await reply(message, client, l('locked'))""" for item in result
                        ],
                        "variable": [
                            {"item": item} for item in result
                        ]
                    }
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_changing_asset'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['set']:
        if rawcontent == '':
            await reply(message, client, f"[{commands['set']}] [{l('setname')}]")
            return
        try:
            result = await loop.run_in_executor(None, search_item, data["search-lang"], "set", rawcontent)
            if result is None and data["sub-search-lang"] != data["search-lang"]:
                result = await loop.run_in_executor(None, search_item, data["sub-search-lang"], "set", rawcontent)
            if result is None:
                await reply(message, client, l('item_notfound'))
            else:
                if len(result) > search_max:
                    await reply(message, client, l('too_many_items', str(len(result))))
                    return
                if len(result) == 1:
                    if await client.change_asset(message.author.id, convert_backend_type(result[0]["backendType"]), result[0]['id']) is True:
                        if data['loglevel'] == 'normal':
                            await reply(message, client, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['set']}")
                        else:
                            await reply(message, client, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}({result[0]['set']})")
                    else:
                        await reply(message, client, l('locked'))
                else:
                    text = str()
                    for count, item in enumerate(result):
                        if data['loglevel'] == 'normal':
                            text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {result[0]['set']}"
                        else:
                            text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}({result[0]['set']})"
                    text += f"\n{l('enter_to_change_asset')}"
                    await reply(message, client, text)
                    client.select[message.author.id] = {
                        "exec": [
                            """\
                            if await client.change_asset(message.author.id, convert_backend_type(item["backendType"]), item['id']) is True:
                                if data['loglevel'] == 'normal':
                                    await reply(message, client, f"{item['shortDescription']}: {item['name']} | {item['set']}")
                                else:
                                    await reply(message, client, f"{item['shortDescription']}: {item['name']} | {item['id']}({item['set']})")
                            else:
                                await reply(message, client, l('locked'))""" for item in result
                        ],
                        "variable": [
                            {"item": item}
                        ]
                    }
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_changing_asset'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['setstyle']:
        try:
            if True not in [args[1] in commands[key] for key in ("outfit", "backpack", "pickaxe")]:
                await reply(message, client, f"[{commands['setstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pickaxe']}]]")
                return
            type_ = convert_to_asset(args[1])
            id_ = member_asset(client.party.me, type_)
            type_ = convert_to_new_type(type_)
            if type_ == "Back Bling" and (id_.startswith("pet_carrier_") or id_.startswith("pet_")):
                type_ = "Pet"
            result = await loop.run_in_executor(None, search_style, data["search-lang"], id_, type_)
            if result is None:
                await reply(message, client, l('no_stylechange'))
            else:
                text = str()
                for count, item in enumerate(result):
                    text += f"\n{count+1}, スタイル : {item['name']}　　{count+1}←を入力"
                text += f"\n{l('enter_to_set_style')}"
                await reply(message, client, text)
                client.select[message.author.id] = {"exec": [f"await client.change_asset('{message.author.id}', '{type_}', '{id_}', {variants['variants']})" for variants in result]}
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"スタイルを変更するには[{commands['setstyle']}と入力した後に] \n[スキンの場合{commands['outfit']}] , [バッグの場合{commands['backpack']}] \n[ペットの場合{commands['pet']}] , [ツルハシの場合{commands['pickaxe']}] と入力してください。\n 例）スタイル a")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['addstyle']:
        try:
            if True not in [args[1] in commands[key] for key in ("outfit", "backpack", "pickaxe")]:
                await reply(message, client, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pickaxe']}]]")
                return
            type_ = convert_to_asset(args[1])
            id_ = member_asset(client.party.me, type_)
            variants_ = eval(f"client.party.me.{type_}_variants")
            type_ = convert_to_new_type(type_)
            if type_ == "Back Bling" and (id_.startswith("pet_carrier_") or id_.startswith("pet_")):
                type_ = "Pet"
            result = await loop.run_in_executor(None, search_style, data["search-lang"], id_, type_)
            if result is None:
                await reply(message, client, l('no_stylechange'))
            else:
                text = str()
                for count, item in enumerate(result):
                    text += f"\n{count+1} {item['name']}"
                text += f"\n{l('enter_to_set_style')}"
                await reply(message, client, text)
                client.select[message.author.id] = {"exec": [f"await client.change_asset('{message.author.id}', '{type_}', '{id_}', {variants_} + {variants['variants']})" for variants in result]}
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['setvariant']:
        try:
            if True not in [args[1] in commands[key] for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, client, f"[{commands['setvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            variantdict={}
            for count,text in enumerate(args[2:]):
                if count % 2 != 0:
                    continue
                try:
                    variantdict[text]=args[count+3]
                except IndexError:
                    break
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.party.me, convert_to_asset(args[1]))
            variants = client.party.me.create_variants(item='AthenaCharacter', enlightenment=enlightenment, **variantdict)
            type_ = convert_to_new_type(type_)
            if type_ == "Back Bling" and (id_.startswith("pet_carrier_") or id_.startswith("pet_")):
                type_ = "Pet"
            if await client.change_asset(message.author.id, type_, id_, variants, client.party.me.enlightenments) is False:
                await reply(message, client, l('locked'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_changing_asset'))
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"[{commands['setvariant']}] [ID] [variant] [{l('number')}]")
        except Exception:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0] in commands['addvariant']:
        try:
            if True not in [args[1] in commands[key] for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, client, f"[{commands['addvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            variantdict={}
            for count,text in enumerate(args[2:]):
                if count % 2 != 0:
                    continue
                try:
                    variantdict[text]=args[count+3]
                except IndexError:
                    break
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.party.me, convert_to_asset(args[1]))
            variants = client.party.me.create_variants(item='AthenaCharacter', enlightenment=enlightenment, **variantdict)
            variants += eval(f"client.party.me.{convert_to_asset(args[1])}_variants")
            type_ = convert_to_new_type(type_)
            if type_ == "Back Bling" and (id_.startswith("pet_carrier_") or id_.startswith("pet_")):
                type_ = "Pet"
            if await client.change_asset(message.author.id, type_, id_, variants, client.party.me.enlightenments) is False:
                await reply(message, client, l('locked'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_changing_asset'))
        except IndexError:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"[{commands['addvariant']}] [ID] [variant] [{l('number')}]")
        except Exception:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif True in [args[0].lower().startswith(id_) for id_ in ("cid_", "bid_", "petcarrier_", "pickaxe_id_", "eid_", "emoji_", "toy_")]:
        try:
            type_ = convert_to_type(args[0])
            if not await client.change_asset(message.author.id, type_, args[0]):
                await reply(message, client, l('locked'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error_while_changing_asset'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    elif args[0].lower().startswith('playlist_'):
        try:
            await client.party.set_playlist(args[0])
            await reply(message, client, l('set_playlist', args[0]))
            data['fortnite']['playlist']=args[0]
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('not_party_leader'))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, l('error'))

    else:
        keys = {
            "outfitmimic": ["outfitmimic", l('mimic', l("outfit"))],
            "backpackmimic": ["backpackmimic", l('mimic', l("backpack"))],
            "pickaxemimic": ["pickaxemimic", l('mimic', l("pickaxe"))],
            "emotemimic": ["emotemimic", l('mimic', l("emote"))]
        }
        for key,value in keys.items():
            if args[0] in commands[key]:
                try:
                    if args[1] in commands['true']:
                        setattr(client,value[0],True)
                        send(display_name,l('set_to', value[1], l('on')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                        await reply(message, client, l('set_to', value[1], l('on')))

                    elif args[1] in commands['false']:
                        setattr(client,value[0],False)
                        send(display_name,l('set_to', value[1], l('off')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                        await reply(message, client, l('set_to', value[1], l('off')))

                    else:
                        if data['caseinsensitive']:
                            users = {str(user.display_name): user for user in client.party.members if content_ in jaconv.kata2hira(str(user.display_name).lower())}
                        else:
                            users = {str(user.display_name): user for user in client.party.members if content_ in str(user.display_name)}
                        try:
                            user = await client.fetch_user(rawcontent)
                            if user:
                                users[str(user.display_name)] = user
                                client.add_cache(user)
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            await reply(message, client, l("error_while_requesting_userinfo"))
                        if len(users) > search_max:
                            await reply(message, client, l('too_many_users', str(len(users))))
                            return
                        if len(users) == 0:
                            await reply(message, client, l('user_notfound'))
                            return
                        if len(users) == 1:
                            user = tuple(users.values())[0]
                            setattr(client,value[0],user.id)
                            send(display_name,l('set_to', value[1], l('off')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                            await reply(message, client, l('set_to', value[1], name(user)))
                        else:
                            client.select[message.author.id] = {
                                "exec": [
                                    """\
                                        setattr(client,value[0],user.id)
                                        send(display_name,l('set_to', value[1], l('off')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                                        await reply(message, client, l('set_to', value[1], name(user)))""" for user in users.values()
                                ],
                                "variable": [
                                    {"user": user, "value": value} for user in users.values()
                                ]
                            }
                            text = str()
                            for count, user in enumerate(users.values()):
                                text += f"\n{count+1} {name(user)}"
                            text += f"\n{l('enter_to_mimic_user')}"
                            await reply(message, client, text)
                except IndexError:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, f"[{commands[key]}] [[{commands['true']}] / [{commands['false']}] / {l('name_or_id')}]")
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l('error'))
                return

        keys = {
            "outfitlock": ["outfitlock", l('lock', l("outfit"))],
            "backpacklock": ["backpacklock", l('lock', l("backpack"))],
            "pickaxelock": ["pickaxelock", l('lock', l("pickaxe"))],
            "emotelock": ["emotelock", l('lock', l("emote"))],
            "whisper": ["whisper", l('command_from', l('whisper'))],
            "partychat": ["partychat", l('command_from', l('partychat'))],
            "discord": ["discord", l('command_from', l('discord'))],
            "web": ["web", l('command_from', l('web'))],
            "disablewhisperperfectly": ["whisperperfect", l('disable_perfect', l('whisper'))],
            "disablepartychatperfectly": ["partychatperfect", l('disable_perfect', l('partychat'))],
            "disablediscordperfectly": ["discordperfect", l('disable_perfect', l('discord'))],
            "acceptinvite": ["acceptinvite", l('invite')],
            "acceptfriend": ["acceptfriend", l('friend_request')],
            "joinmessageenable": ["joinmessageenable", l('join_', l('message'))],
            "randommessageenable": ["randommessageenable", l('join_', l('randommessage'))]
        }
        for key,value in keys.items():
            if args[0] in commands[key]:
                try:
                    if args[1] in commands['true']:
                        setattr(client,value[0],True)
                        send(display_name,l('set_to', value[1], l('on')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                        await reply(message, client, l('set_to', value[1], l('on')))
                    elif args[1] in commands['false']:
                        setattr(client,value[0],False)
                        send(display_name,l('set_to', value[1], l('off')),add_p=lambda x:f'[{now()}] [{client.user.display_name}] {x}')
                        await reply(message, client, l('set_to', value[1], l('off')))
                except IndexError:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, f"[{commands[key]}] [[{commands['true']}] / [{commands['false']}]]")
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l('error'))
                return


        if ': ' in message.content:
            return
        if content.isdigit() and client.select.get(message.author.id):
            try:
                if int(args[0]) == 0:
                    await reply(message, client, l('please_enter_valid_number'))
                    return
                exec_ = client.select[message.author.id]["exec"][int(args[0])-1]
                variable = globals()
                variable.update(locals())
                if client.select[message.author.id].get("variable"):
                    variable.update(client.select[message.author.id]["variable"][int(args[0])-1])
                await aexec(exec_, variable)
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('please_enter_valid_number'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))
        else:
            if do_itemsearch:
                result = await loop.run_in_executor(None, search_item, data["search-lang"], "name", content, "Item")
                if not result and data["sub-search-lang"] != data["search-lang"]:
                    result = await loop.run_in_executor(None, search_item, data["sub-search-lang"], "name", content, "Item")
                if result:
                    if len(result) > search_max:
                        await reply(message, client, l('too_many_items', str(len(result))))
                        return
                    if len(result) == 1:
                        if await client.change_asset(message.author.id, convert_backend_type(result[0]["backendType"]), result[0]['id']) is True:
                            if data['loglevel'] == 'normal':
                                await reply(message, client, f"{result[0]['shortDescription']}を{result[0]['name']} に設定しました")
                            else:
                                await reply(message, client, f"{result[0]['shortDescription']}を{result[0]['name']} に設定しました")
                        else:
                            await reply(message, client, l('locked'))
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            if data['loglevel'] == 'normal':
                                text += f"\n{count+1}, {item['shortDescription']} / {item['name']}  {count+1}←を入力"
                            else:
                                text += f"\n{count+1}, {item['shortDescription']} / {item['name']}  {count+1}←を入力"
                        text += f"\n{l('enter_to_change_asset')}"
                        await reply(message, client, text)
                        client.select[message.author.id] = {
                            "exec": [
                                """\
                                    if await client.change_asset(message.author.id, convert_backend_type(item["backendType"]), item['id']) is True:
                                        if data['loglevel'] == 'normal':
                                            await reply(message, client, f"{item['shortDescription']}を{item['name']} に設定しました")
                                        else:
                                            await reply(message, client, f"{item['shortDescription']}: {item['name']} | {item['id']}")
                                    else:
                                        await reply(message, client, l('locked'))""" for item in result
                            ],
                            "variable": [
                                {"item": item} for item in result
                            ]
                        }

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

bot_ready = True
first_boot = True
filename = 'device_auths.json'
web_text = ''
cache_users = {}
cache_items = {}
cache_banners = {}
client_name = {}
ignoretype = [
    "Contrail",
    "Glider",
    "Wrap",
    "Loading Screen",
    "Music",
    "Spray",
    "Battle Bus"
]
clients = []
loadedclients = []
whitelist = []
whitelist_ = []
blacklist = []
blacklist_ = []
otherbotlist = []
storedlogs = []
format_pattern = re.compile(r"""\{(.*?)\}""")

config_tags={
    "['fortnite']": [dict],
    "['fortnite']['email']": [str,"can_be_multiple"],
    "['fortnite']['owner']": [str,"can_be_multiple"],
    "['fortnite']['platform']": [str,"select_platform"],
    "['fortnite']['outfit']": [str],
    "['fortnite']['outfit_style']": [str],
    "['fortnite']['backpack']": [str],
    "['fortnite']['backpack_style']": [str],
    "['fortnite']['pickaxe']": [str],
    "['fortnite']['pickaxe_style']": [str],
    "['fortnite']['emote']": [str],
    "['fortnite']['playlist']": [str],
    "['fortnite']['banner']": [str],
    "['fortnite']['banner_color']": [str],
    "['fortnite']['avatar_id']": [str],
    "['fortnite']['avatar_color']": [str,"can_linebreak"],
    "['fortnite']['level']": [int],
    "['fortnite']['tier']": [int],
    "['fortnite']['xpboost']": [int],
    "['fortnite']['friendxpboost']": [int],
    "['fortnite']['status']": [str],
    "['fortnite']['privacy']": [str,"select_privacy"],
    "['fortnite']['whisper']": [bool_,"select_bool"],
    "['fortnite']['partychat']": [bool_,"select_bool"],
    "['fortnite']['disablewhisperperfectly']": [bool_,"select_bool"],
    "['fortnite']['disablepartychatperfectly']": [bool_,"select_bool"],
    "['fortnite']['ignorebot']": [bool_,"select_bool"],
    "['fortnite']['joinmessage']": [str,"can_linebreak"],
    "['fortnite']['randommessage']": [str,"can_be_multiple"],
    "['fortnite']['joinmessageenable']": [bool_,"select_bool"],
    "['fortnite']['randommessageenable']": [bool_,"select_bool"],
    "['fortnite']['joinemote']": [bool_,"select_bool"],
    "['fortnite']['click_invite']": [bool_,"select_bool"],
    "['fortnite']['disable_voice']": [bool_,"select_bool"],
    "['fortnite']['outfitmimic']": [bool_,"select_bool"],
    "['fortnite']['backpackmimic']": [bool_,"select_bool"],
    "['fortnite']['pickaxemimic']": [bool_,"select_bool"],
    "['fortnite']['emotemimic']": [bool_,"select_bool"],
    "['fortnite']['mimic-ignorebot']": [bool_,"select_bool"],
    "['fortnite']['mimic-ignoreblacklist']": [bool_,"select_bool"],
    "['fortnite']['outfitlock']": [bool_,"select_bool"],
    "['fortnite']['backpacklock']": [bool_,"select_bool"],
    "['fortnite']['pickaxelock']": [bool_,"select_bool"],
    "['fortnite']['emotelock']": [bool_,"select_bool"],
    "['fortnite']['acceptinvite']": [bool_,"select_bool"],
    "['fortnite']['acceptfriend']": [bool_none,"select_bool_none"],
    "['fortnite']['addfriend']": [bool_,"select_bool"],
    "['fortnite']['invite-ownerdecline']": [bool_,"select_bool"],
    "['fortnite']['inviteinterval']": [bool_,"select_bool"],
    "['fortnite']['interval']": [int],
    "['fortnite']['waitinterval']": [int],
    "['fortnite']['hide-user']": [bool_,"select_bool"],
    "['fortnite']['hide-blacklist']": [bool_,"select_bool"],
    "['fortnite']['show-owner']": [bool_,"select_bool"],
    "['fortnite']['show-whitelist']": [bool_,"select_bool"],
    "['fortnite']['show-bot']": [bool_,"select_bool"],
    "['fortnite']['blacklist']": [str,"can_be_multiple"],
    "['fortnite']['blacklist-declineinvite']": [bool_,"select_bool"],
    "['fortnite']['blacklist-autoblock']": [bool_,"select_bool"],
    "['fortnite']['blacklist-autokick']": [bool_,"select_bool"],
    "['fortnite']['blacklist-autochatban']": [bool_,"select_bool"],
    "['fortnite']['blacklist-ignorecommand']": [bool_,"select_bool"],
    "['fortnite']['whitelist']": [str,"can_be_multiple"],
    "['fortnite']['whitelist-allowinvite']": [bool_,"select_bool"],
    "['fortnite']['whitelist-declineinvite']": [bool_,"select_bool"],
    "['fortnite']['whitelist-ignorelock']": [bool_,"select_bool"],
    "['fortnite']['whitelist-ownercommand']": [bool_,"select_bool"],
    "['fortnite']['whitelist-ignoreng']": [bool_,"select_bool"],
    "['fortnite']['invitelist']": [str,"can_be_multiple"],
    "['fortnite']['otherbotlist']": [str,"can_be_multiple"],
    "['discord']": [dict],
    "['discord']['enabled']": [bool_,"select_bool"],
    "['discord']['token']": [str],
    "['discord']['owner']": [int,"can_be_multiple"],
    "['discord']['channels']": [str,"can_be_multiple"],
    "['discord']['status']": [str],
    "['discord']['status_type']": [str,"select_status"],
    "['discord']['discord']": [bool_,"select_bool"],
    "['discord']['disablediscordperfectly']": [bool_,"select_bool"],
    "['discord']['ignorebot']": [bool_,"select_bool"],
    "['discord']['blacklist']": [str,"can_be_multiple"],
    "['discord']['blacklist-ignorecommand']": [bool_,"select_bool"],
    "['discord']['whitelist']": [str,"can_be_multiple"],
    "['discord']['whitelist-ignorelock']": [bool_,"select_bool"],
    "['discord']['whitelist-ownercommand']": [bool_,"select_bool"],
    "['discord']['whitelist-ignoreng']": [bool_,"select_bool"],
    "['web']": [dict],
    "['web']['enabled']": [bool_,"select_bool"],
    "['web']['ip']": [str],
    "['web']['port']": [int],
    "['web']['password']": [str],
    "['web']['login_required']": [bool_,"select_bool"],
    "['web']['web']": [bool_,"select_bool"],
    "['web']['log']": [bool_,"select_bool"],
    "['replies-matchmethod']": [str,"select_matchmethod"],
    "['ng-words']": [str,"can_be_multiple"],
    "['ng-word-matchmethod']": [str,"select_matchmethod"],
    "['ng-word-kick']": [bool_,"select_bool"],
    "['ng-word-chatban']": [bool_,"select_bool"],
    "['ng-word-blacklist']": [bool_,"select_bool"],
    "['restart_in']": [int],
    "['search_max']": [int],
    "['lang']": [str,"select_lang"],
    "['search-lang']": [str,"select_ben_lang"],
    "['sub-search-lang']": [str,"select_ben_lang"],
    "['no-logs']": [bool_,"select_bool"],
    "['ingame-error']": [bool_,"select_bool"],
    "['discord-log']": [bool_,"select_bool"],
    "['omit-over2000']": [bool_,"select_bool"],
    "['skip-if-overflow']": [bool_,"select_bool"],
    "['hide-email']": [bool_,"select_bool"],
    "['hide-token']": [bool_,"select_bool"],
    "['hide-webhook']": [bool_,"select_bool"],
    "['webhook']": [str],
    "['caseinsensitive']": [bool_,"select_bool"],
    "['loglevel']": [str,"select_loglevel"],
    "['debug']": [bool_,"select_bool"]
}
config_tags_raw = copy.deepcopy(config_tags)
commands_tags={
    "['usercommands']": [str,"can_be_multiple"],
    "['true']": [str,"can_be_multiple"],
    "['false']": [str,"can_be_multiple"],
    "['me']": [str,"can_be_multiple"],
    "['prev']": [str,"can_be_multiple"],
    "['eval']": [str,"can_be_multiple"],
    "['exec']": [str,"can_be_multiple"],
    "['restart']": [str,"can_be_multiple"],
    "['relogin']": [str,"can_be_multiple"],
    "['reload']": [str,"can_be_multiple"],
    "['addblacklist']": [str,"can_be_multiple"],
    "['removeblacklist']": [str,"can_be_multiple"],
    "['addwhitelist']": [str,"can_be_multiple"],
    "['removewhitelist']": [str,"can_be_multiple"],
    "['addblacklist_discord']": [str,"can_be_multiple"],
    "['removeblacklist_discord']": [str,"can_be_multiple"],
    "['addwhitelist_discord']": [str,"can_be_multiple"],
    "['removewhitelist_discord']": [str,"can_be_multiple"],
    "['addinvitelist']": [str,"can_be_multiple"],
    "['removeinvitelist']": [str,"can_be_multiple"],
    "['get']": [str,"can_be_multiple"],
    "['friendcount']": [str,"can_be_multiple"],
    "['pendingcount']": [str,"can_be_multiple"],
    "['blockcount']": [str,"can_be_multiple"],
    "['friendlist']": [str,"can_be_multiple"],
    "['pendinglist']": [str,"can_be_multiple"],
    "['blocklist']": [str,"can_be_multiple"],
    "['outfitmimic']": [str,"can_be_multiple"],
    "['backpackmimic']": [str,"can_be_multiple"],
    "['pickaxemimic']": [str,"can_be_multiple"],
    "['emotemimic']": [str,"can_be_multiple"],
    "['whisper']": [str,"can_be_multiple"],
    "['partychat']": [str,"can_be_multiple"],
    "['discord']": [str,"can_be_multiple"],
    "['web']": [str,"can_be_multiple"],
    "['disablewhisperperfectly']": [str,"can_be_multiple"],
    "['disablepartychatperfectly']": [str,"can_be_multiple"],
    "['disablediscordperfectly']": [str,"can_be_multiple"],
    "['acceptinvite']": [str,"can_be_multiple"],
    "['acceptfriend']": [str,"can_be_multiple"],
    "['joinmessageenable']": [str,"can_be_multiple"],
    "['randommessageenable']": [str,"can_be_multiple"],
    "['wait']": [str,"can_be_multiple"],
    "['join']": [str,"can_be_multiple"],
    "['joinid']": [str,"can_be_multiple"],
    "['leave']": [str,"can_be_multiple"],
    "['invite']": [str,"can_be_multiple"],
    "['inviteall']": [str,"can_be_multiple"],
    "['message']": [str,"can_be_multiple"],
    "['now_day']": [str,"can_be_multiple"],
    "['i_news']": [str,"can_be_multiple"],
    "['y_news']": [str,"can_be_multiple"],
    "['y_news_f']": [str,"can_be_multiple"],
    "['quake']": [str,"can_be_multiple"],
    "['tokushima']": [str,"can_be_multiple"],
    "['now_time']": [str,"can_be_multiple"],
    "['partymessage']": [str,"can_be_multiple"],
    "['sendall']": [str,"can_be_multiple"],
    "['status']": [str,"can_be_multiple"],
    "['avatar']": [str,"can_be_multiple"],
    "['banner']": [str,"can_be_multiple"],
    "['level']": [str,"can_be_multiple"],
    "['bp']": [str,"can_be_multiple"],
    "['privacy']": [str,"can_be_multiple"],
    "['privacy_public']": [str,"can_be_multiple"],
    "['privacy_friends_allow_friends_of_friends']": [str,"can_be_multiple"],
    "['privacy_friends']": [str,"can_be_multiple"],
    "['privacy_private_allow_friends_of_friends']": [str,"can_be_multiple"],
    "['privacy_private']": [str,"can_be_multiple"],
    "['senseki']": [str,"can_be_multiple"],
    "['getuser']": [str,"can_be_multiple"],
    "['getfriend']": [str,"can_be_multiple"],
    "['getpending']": [str,"can_be_multiple"],
    "['getblock']": [str,"can_be_multiple"],
    "['info']": [str,"can_be_multiple"],
    "['info_party']": [str,"can_be_multiple"],
    "['pending']": [str,"can_be_multiple"],
    "['removepending']": [str,"can_be_multiple"],
    "['addfriend']": [str,"can_be_multiple"],
    "['removefriend']": [str,"can_be_multiple"],
    "['removeallfriend']": [str,"can_be_multiple"],
    "['remove_offline_for']": [str,"can_be_multiple"],
    "['acceptpending']": [str,"can_be_multiple"],
    "['declinepending']": [str,"can_be_multiple"],
    "['blockfriend']": [str,"can_be_multiple"],
    "['unblockfriend']": [str,"can_be_multiple"],
    "['voice']": [str,"can_be_multiple"],
    "['chatban']": [str,"can_be_multiple"],
    "['promote']": [str,"can_be_multiple"],
    "['kick']": [str,"can_be_multiple"],
    "['test']": [str,"can_be_multiple"],
    "['hide']": [str,"can_be_multiple"],
    "['show']": [str,"can_be_multiple"],
    "['ready']": [str,"can_be_multiple"],
    "['unready']": [str,"can_be_multiple"],
    "['sitout']": [str,"can_be_multiple"],
    "['match']": [str,"can_be_multiple"],
    "['unmatch']": [str,"can_be_multiple"],
    "['swap']": [str,"can_be_multiple"],
    "['outfitlock']": [str,"can_be_multiple"],
    "['backpacklock']": [str,"can_be_multiple"],
    "['pickaxelock']": [str,"can_be_multiple"],
    "['emotelock']": [str,"can_be_multiple"],
    "['stop']": [str,"can_be_multiple"],
    "['addeditems']": [str,"can_be_multiple"],
    "['shopitems']": [str,"can_be_multiple"],
    "['alloutfit']": [str,"can_be_multiple"],
    "['allbackpack']": [str,"can_be_multiple"],
    "['allpet']": [str,"can_be_multiple"],
    "['allpickaxe']": [str,"can_be_multiple"],
    "['allemote']": [str,"can_be_multiple"],
    "['allemoji']": [str,"can_be_multiple"],
    "['alltoy']": [str,"can_be_multiple"],
    "['cid']": [str,"can_be_multiple"],
    "['bid']": [str,"can_be_multiple"],
    "['petcarrier']": [str,"can_be_multiple"],
    "['pickaxe_id']": [str,"can_be_multiple"],
    "['eid']": [str,"can_be_multiple"],
    "['emoji_id']": [str,"can_be_multiple"],
    "['toy_id']": [str,"can_be_multiple"],
    "['id']": [str,"can_be_multiple"],
    "['outfit']": [str,"can_be_multiple"],
    "['backpack']": [str,"can_be_multiple"],
    "['pet']": [str,"can_be_multiple"],
    "['pickaxe']": [str,"can_be_multiple"],
    "['emote']": [str,"can_be_multiple"],
    "['emoji']": [str,"can_be_multiple"],
    "['toy']": [str,"can_be_multiple"],
    "['item']": [str,"can_be_multiple"],
    "['set']": [str,"can_be_multiple"],
    "['setvariant']": [str,"can_be_multiple"],
    "['addvariant']": [str,"can_be_multiple"],
    "['setstyle']": [str,"can_be_multiple"],
    "['addstyle']": [str,"can_be_multiple"],
    "['setenlightenment']": [str,"can_be_multiple"]
}
error_config = []
error_commands = []

outfit_keys = ("cid", "outfit", "outfitmimic", "outfitlock", "alloutfit")
backpack_keys = ("bid", "backpack", "backpackmimic", "backpacklock", "allbackpack")
pet_keys = ("petcarrier", "pet", "allpet")
pickaxe_keys = ("pickaxe_id", "pickaxe", "pickaxemimic", "pickaxelock", "allpickaxe")
emote_keys = ("eid", "emote", "emotemimic", "emotelock", "allemote")
emoji_keys = ("emoji_id", "emoji", "allemoji")
toy_keys = ("toy_id", "toy", "alltoy")
item_keys = ("id", "item")

app = Sanic(__name__)
app.secret_key = os.urandom(32)
app.static('/images', './templates/images')
env = Environment(loader=FileSystemLoader('./templates', encoding='utf8'), extensions=['jinja2.ext.do'])
auth = LoginManager()

fortnitepy_auth = fortnitepy.Auth()
launcher_token = fortnitepy_auth.ios_token
fortnite_token = fortnitepy_auth.fortnite_token
oauth_url = "https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/token"
fortnite_token_url = "https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/token"
exchange_auth_url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"
device_auth_url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/deviceAuthorization"
exchange_url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/exchange"
user_lookup_url = "https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{user_id}"


if not load_config():
    sys.exit(1)
if error_config or error_commands:
    bot_ready = False
for key in error_config:
    config_tags[key].append("fix_required")
for key in error_commands:
    commands_tags[key].append("fix_required")
search_max = data["search_max"]

if data['debug']:
    logger = logging.getLogger('fortnitepy.auth')
    logger.setLevel(level=logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('\u001b[36m %(asctime)s:%(levelname)s:%(name)s: %(message)s \u001b[0m'))
    logger.addHandler(handler)

    logger = logging.getLogger('fortnitepy.http')
    logger.setLevel(level=logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('\u001b[36m %(asctime)s:%(levelname)s:%(name)s: %(message)s \u001b[0m'))
    logger.addHandler(handler)

    logger = logging.getLogger('fortnitepy.xmpp')
    logger.setLevel(level=logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('\u001b[35m %(asctime)s:%(levelname)s:%(name)s: %(message)s \u001b[0m'))
    logger.addHandler(handler)

if os.getcwd().startswith('/app') or os.getcwd().startswith('/home/runner'):
    data['web']['ip'] = "0.0.0.0"
else:
    data['web']['ip'] = data['web']['ip'].format(ip=socket.gethostbyname(socket.gethostname()))

if True:
    send(l('bot'),f'{l("lobbybot")}: gomashio\n{l("credit")}\n{l("library")}: Terbau',cyan)
    text = ""
    if data['loglevel'] == 'normal':
        text += f'\n{l("loglevel")}: {l("normal")}\n'
    elif data['loglevel'] == 'info':
        text += f'\n{l("loglevel")}: {l("info")}\n'
    elif data['loglevel'] == 'debug':
        text += f'\n{l("loglevel")}: {l("debug")}\n'
    if data.get('debug',False) is True:
        text += f'\n{l("debug")}: {l("on")}\n'
    else:
        text += f'\n{l("debug")}: {l("off")}\n'
    text += f'\nPython {platform.python_version()}\n'
    text += f'fortnitepy {fortnitepy.__version__}\n'
    text += f'discord.py {discord.__version__}\n'
    text += f'Sanic {sanic.__version__}\n'
    send(l('bot'),text,green)
    if data.get('debug',False) is True:
        send(l('bot'),f'[{now()}] {l("debug_is_on")}',red)
    send(l('bot'),l("booting"))

dclient = discord.Client()
dclient.owner = []
dclient.isready = False
dclient.boot_time = None
if True: #discord
    @dclient.event
    async def on_ready() -> None:
        loop = asyncio.get_event_loop()
        dclient.boot_time = time.time()
        dclient_user = name(dclient.user)
        send(dclient_user,f"{l('login')}: {dclient_user}",green,add_p=lambda x:f'[{now()}] [{dclient_user}] {x}')
        dclient.isready = True
        loop.create_task(status_loop())

        dclient.owner = []
        for owner in data['discord']['owner']:
            user = dclient.get_user(owner)
            if not user:
                try:
                    user = await dclient.fetch_user(owner)
                except discord.NotFound:
                    if data['loglevel'] == "debug":
                        send(dclient_user,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                except discord.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(dclient_user,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(dclient_user,l('error_while_requesting_userinfo'),red,add_p=lambda x:f'[{now()}] [{dclient_user}] {x}',add_d=lambda x:f'>>> {x}')
            if not user:
                send(dclient_user,l('discord_owner_notfound',owner),red,add_p=lambda x:f'[{now()}] [{dclient_user}] {x}',add_d=lambda x:f'>>> {x}')
            else:
                dclient.owner.append(user)
                send(dclient_user,f"{l('owner')}: {name(user)}",green,add_p=lambda x:f'[{now()}] [{dclient_user}] {x}')

        lists = {
            "blacklist_": "blacklist",
            "whitelist_": "whitelist"
        }
        async def _(listuser: str) -> None:
            listuser = int(listuser)
            user = dclient.get_user(listuser)
            if not user:
                try:
                    user = await dclient.fetch_user(listuser)
                except discord.NotFound:
                    if data['loglevel'] == "debug":
                        send(dclient_user,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(dclient_user,l(f'discord_{data_}_user_notfound', listuser),red,add_p=lambda x:f'[{now()}] [{dclient_user}] {x}',add_d=lambda x:f'>>> {x}')
                    return
            globals()[list_].append(user.id)

        for list_,data_ in lists.items():
            await asyncio.gather(*[_(listuser) for listuser in data['discord'][data_]])
            if data['loglevel'] == "debug":
                send(dclient_user,f"discord {data_}list {globals()[list_]}",yellow,add_d=lambda x:f'```\n{x}\n```')

    @dclient.event
    async def on_message(message: discord.Message) -> None:
        await process_command(message)

    async def change_status() -> None:
        var = defaultdict(lambda: None)

        var.update(
                {
                    "get_client_data": get_client_data,
                    "all_friend_count": sum([len(client_.friends) for client_ in clients]),
                    "all_pending_count": sum([len(client_.pending_friends) for client_ in clients]),
                    "all_block_count": sum([len(client_.blocked_users) for client_ in clients]),
                    "guild_count": len(dclient.guilds),
                    "get_guild_member_count": get_guild_member_count,
                    "boot_time": int(time.time() - dclient.boot_time)
                }
            )

        activity = discord.Activity(name=eval_format(data['discord']['status'],var),type=data['discord']['status_type'])
        await dclient.change_presence(activity=activity)

    async def status_loop() -> None:
        while True:
            try:
                await change_status()
            except Exception:
                send(dclient.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await asyncio.sleep(30)

select_bool = select(
    [
        {"value": "True","display_value": l('bool_true')},
        {"value": "False","display_value": l('bool_false')}
    ]
)
select_bool_none = select(
    [
        {"value": "True","display_value": l('bool_true')},
        {"value": "False","display_value": l('bool_false')},
        {"value": "None","display_value": l('bool_none')}
    ]
)
select_platform = select(
    [
        {"value": "WIN","display_value": "Windows"},
        {"value": "MAC","display_value": "Mac"},
        {"value": "PSN","display_value": "PlayStation"},
        {"value": "XBL","display_value": "Xbox"},
        {"value": "SWT","display_value": "Switch"},
        {"value": "IOS","display_value": "IOS"},
        {"value": "AND","display_value": "Android"}
    ]
)
select_privacy = select(
    [
        {"value": i,"display_value": l(i)} for i in ["public","friends_allow_friends_of_friends","friends","private_allow_friends_of_friends","private"]
    ]
)
select_status = select(
    [
        {"value": i,"display_value": l(i)} for i in ["playing","listening","watching"]
    ]
)
select_matchmethod = select(
    [
        {"value": i,"display_value": l(i)} for i in ["full","contains","starts","ends"]
    ]
)
select_loglevel = select(
    [
        {"value": "normal","display_value": l('normal')},
        {"value": "info","display_value": l('info')},
        {"value": "debug","display_value": l('debug')}
    ]
)
select_lang = select(
    [
        {"value": re.sub(r"lang(\\|/)","",i).replace(".json",""),"display_value": re.sub(r"lang(\\|/)","",i).replace(".json","")} for i in glob("lang/*.json") if "_old.json" not in i
    ]
)
select_ben_lang = select(
    [
        {"value": i,"display_value": i} for i in ["ar","de","en","es","es-419","fr","it","ja","ko","pl","pt-BR","ru","tr","zh-CN","zh-Hant"]
    ]
)

converter = {
    "can_be_multiple": CanBeMultiple,
    "can_linebreak": CanLinebreak,
    "select_bool": select_bool,
    "select_bool_none": select_bool_none,
    "select_platform": select_platform,
    "select_privacy" :select_privacy,
    "select_status": select_status,
    "select_loglevel": select_loglevel,
    "select_lang": select_lang,
    "select_ben_lang": select_ben_lang,
    "select_matchmethod": select_matchmethod,
    "red": Red,
    "fix_required": FixRequired
}
for key,value in config_tags.items():
    for count,tag in enumerate(value):
        config_tags[key][count] = converter.get(tag,tag)
for key,value in commands_tags.items():
    for count,tag in enumerate(value):
        commands_tags[key][count] = converter.get(tag,tag)

if True: #Web
    @app.route("/favicon.ico", methods=["GET"])
    async def favicon(request: Request):
        return sanic.response.redirect("/images/icon.png")

    if os.environ.get("FORTNITE_LOBBYBOT_STATUS") == "-1":
        @app.route("/", methods=["GET"])
        async def main(request: Request):
            return sanic.response.html(
                "<h2>Fortnite-LobbyBot<h2>"
                "<p>初めに<a href='https://github.com/gomashio1596/Fortnite-LobbyBot/blob/master/README.md' target='_blank'>README</a>をお読みください</p>"
                "<p>First, please read <a href='https://github.com/gomashio1596/Fortnite-LobbyBot/blob/master/README_EN.md' target='_blank'>README<a/></p>"
                "<p>質問などは私(Twitter @gomashio1596 Discord gomashio#4335)か<a href='https://discord.gg/NEnka5N' target='_blank'>Discordサーバー</a>まで</p>"
                "<p>For questions, Contact to me(Twitter @gomashio1596 Discord gomashio#4335) or ask in <a href='https://discord.gg/NEnka5N' target='_blank'>Discord server</a></p>"
                "<p><a href='https://glitch.com/edit/#!/remix/fortnite-lobbybot' target='_blank'>ここをクリック</a>してRemix</p>"
                "<p><a href='https://glitch.com/edit/#!/remix/fortnite-lobbybot' target='_blank'>Click here</a> to Remix</p>"
                "<a href='https://discord.gg/NEnka5N' target='_blank'><img src='https://discordapp.com/api/guilds/718709023427526697/widget.png?style=banner1'></img></a>"
            )
    elif data["status"] == 0:
        @app.route("/", methods=["GET", "POST"])
        async def main(request: Request):
            flash_messages = []
            flash_messages_red = []
            if request.method == "GET":
                data = load_json("config.json")
                return render_template(
                    "config_editor.html",
                    l=l,
                    data=data,
                    config_tags=config_tags,
                    len=len,
                    type=type,
                    can_be_multiple=CanBeMultiple,
                    can_linebreak=CanLinebreak,
                    select=select,
                    str=str,
                    int=int,
                    bool=bool,
                    list=list,
                    map=map,
                    red=Red,
                    fix_required=FixRequired,
                    flash_messages=flash_messages,
                    flash_messages_red=flash_messages_red
                )
            else:
                flag = False
                raw = request.form
                data = load_json("config.json")
                corrected = data
                for key_,tags in config_tags.items():
                    keys = key_.replace("'","").replace("[","").split("]")
                    key = keys[0]
                    nest = len(keys) - 1

                    if nest == 1:
                        if dict in tags:
                            if not corrected.get(key):
                                corrected[key] = {}
                        else:
                            value = raw.get(f"['{key}']")

                        if FixRequired in tags and value == corrected.get(key):
                            flash_messages_red.append(l('this_field_fix_required', key))
                            flag = True
                        if CanBeMultiple in tags:
                            if str in tags:
                                corrected[key] = re.split(r'\r\n|\n',value) if value else []
                            elif int in tags:
                                corrected[key] = [int(i) for i in re.split(r'\r\n|\n',value)] if value else []
                        elif str in tags:
                            corrected[key] = value.replace(r"\\n",r"\n").replace(r"\n","\n") if value else ""
                        elif int in tags:
                            corrected[key] = int(value) if value else 0
                        elif bool_ in tags:
                            corrected[key] = bool_.create(value)
                        elif bool_none in tags:
                            corrected[key] = bool_none.create(value)
                    elif nest == 2:
                        key2 = keys[1]

                        if dict in tags:
                            if not corrected.get(key):
                                if not corrected.get(key).get(key2):
                                    corrected[key][key2] = {}
                        else:
                            value2 = raw.get(f"['{key}']['{key2}']")

                        if FixRequired in tags and value2 == corrected.get(key,{}).get(key2):
                            flash_messages_red.append(l('this_field_fix_required', f"{key}: {key2}"))
                            flag = True
                        if CanBeMultiple in tags:
                            if str in tags:
                                corrected[key][key2] = re.split(r'\r\n|\n',value2) if value2 else []
                            elif int in tags:
                                corrected[key][key2]  = [int(i) for i in re.split(r'\r\n|\n',value2)] if value2 else []
                        elif str in tags:
                            corrected[key][key2]  = value2.replace(r"\\n",r"\n").replace(r"\n","\n") if value2 else ""
                        elif int in tags:
                            corrected[key][key2] = int(value2) if value2 else 0
                        elif bool_ in tags:
                            corrected[key][key2] = bool_.create(value2)
                        elif bool_none in tags:
                            corrected[key][key2] = bool_none.create(value2)
                if flag:
                    return render_template(
                        "config_editor.html",
                        l=l,
                        data=data,
                        config_tags=config_tags,
                        len=len,
                        type=type,
                        can_be_multiple=CanBeMultiple,
                        can_linebreak=CanLinebreak,
                        select=select,
                        str=str,
                        int=int,
                        bool=bool,
                        list=list,
                        map=map,
                        red=Red,
                        fix_required=FixRequired,
                        flash_messages=flash_messages,
                        flash_messages_red=flash_messages_red
                    )
                else:
                    corrected["status"] = 1
                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(corrected, f, ensure_ascii=False, indent=4, sort_keys=False)
                    Thread(target=restart,args=(1,)).start()
                    return sanic.response.redirect("/")
    else:
        @app.route("/", methods=["GET", "POST"])
        async def main(request: Request):
            if request.method == "GET":
                return render_template(
                    "main.html",
                    l=l,
                    authenticated=auth.authenticated(request),
                    data=data
                )
            elif request.method == "POST":
                if auth.authenticated(request):
                    Thread(target=restart,args=(1,)).start()
                return sanic.response.redirect("/")

        @app.route("/login", methods=["GET", "POST"])
        async def login(request: Request):
            if auth.authenticated(request):
                return sanic.response.redirect("/")
            else:
                flash_messages = []
                if request.method == "GET":
                    return render_template("login.html", l=l, flash_messages=flash_messages)
                elif request.method == "POST":
                    if request.form.get("password","") == data["web"]["password"]:
                        r = sanic.response.redirect("/")
                        auth.login_user(request, r)
                        return r
                    else:
                        flash_messages.append(l('invalid_password'))
                        return render_template("login.html", l=l, flash_messages=flash_messages)

        @app.route("/text")
        @auth.login_required
        async def web_text_(request: Request):
            return sanic.response.json(
                {
                    "text": web_text
                }
            )

        @app.route("/logout")
        @auth.login_required
        async def logout(request: Request):
            r = sanic.response.redirect("/")
            auth.logout_user(request, r)
            return r

        @app.route("/config_editor", methods=["GET", "POST"])
        @auth.login_required
        async def config_editor(request: Request):
            flash_messages = []
            flash_messages_red = []
            if request.method == "GET":
                data = load_json("config.json")
                return render_template(
                    "config_editor.html",
                    l=l,
                    data=data,
                    config_tags=config_tags,
                    len=len,
                    type=type,
                    can_be_multiple=CanBeMultiple,
                    can_linebreak=CanLinebreak,
                    select=select,
                    str=str,
                    int=int,
                    bool=bool,
                    list=list,
                    map=map,
                    red=Red,
                    fix_required=FixRequired,
                    flash_messages=flash_messages,
                    flash_messages_red=flash_messages_red
                )
            else:
                flag = False
                raw = request.form
                data = load_json("config.json")
                corrected = data
                for key_,tags in config_tags.items():
                    keys = key_.replace("'","").replace("[","").split("]")
                    key = keys[0]
                    nest = len(keys) - 1

                    if nest == 1:
                        if dict in tags:
                            if not corrected.get(key):
                                corrected[key] = {}
                        else:
                            value = raw.get(f"['{key}']")

                        if FixRequired in tags and value == corrected.get(key):
                            flash_messages_red.append(l('this_field_fix_required', key))
                            flag = True
                        if CanBeMultiple in tags:
                            if str in tags:
                                corrected[key] = re.split(r'\r\n|\n',value) if value else []
                            elif int in tags:
                                corrected[key] = [int(i) for i in re.split(r'\r\n|\n',value)] if value else []
                        elif str in tags:
                            corrected[key] = value.replace(r"\\n",r"\n").replace(r"\n","\n") if value else ""
                        elif int in tags:
                            corrected[key] = int(value) if value else 0
                        elif bool_ in tags:
                            corrected[key] = bool_.create(value)
                        elif bool_none in tags:
                            corrected[key] = bool_none.create(value)
                    elif nest == 2:
                        key2 = keys[1]

                        if dict in tags:
                            if not corrected.get(key):
                                if not corrected.get(key).get(key2):
                                    corrected[key][key2] = {}
                        else:
                            value2 = raw.get(f"['{key}']['{key2}']")

                        if FixRequired in tags and value2 == corrected.get(key,{}).get(key2):
                            flash_messages_red.append(l('this_field_fix_required', f"{key}: {key2}"))
                            flag = True
                        if CanBeMultiple in tags:
                            if str in tags:
                                corrected[key][key2] = re.split(r'\r\n|\n',value2) if value2 else []
                            elif int in tags:
                                corrected[key][key2]  = [int(i) for i in re.split(r'\r\n|\n',value2)] if value2 else []
                        elif str in tags:
                            corrected[key][key2]  = value2.replace(r"\\n",r"\n").replace(r"\n","\n") if value2 else ""
                        elif int in tags:
                            corrected[key][key2] = int(value2) if value2 else 0
                        elif bool_ in tags:
                            corrected[key][key2] = bool_.create(value2)
                        elif bool_none in tags:
                            corrected[key][key2] = bool_none.create(value2)
                if flag:
                    return render_template(
                        "config_editor.html",
                        l=l,
                        data=corrected,
                        config_tags=config_tags,
                        len=len,
                        type=type,
                        can_be_multiple=CanBeMultiple,
                        can_linebreak=CanLinebreak,
                        select=select,
                        str=str,
                        int=int,
                        bool=bool,
                        list=list,
                        map=map,
                        red=Red,
                        fix_required=FixRequired,
                        flash_messages=flash_messages,
                        flash_messages_red=flash_messages_red
                    )
                else:
                    corrected["status"] = 1
                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(corrected, f, ensure_ascii=False, indent=4, sort_keys=False)
                    if raw.get("reload"):
                        Thread(target=restart, args=(1,)).start()
                        return sanic.response.redirect("/")
                    else:
                        flash_messages.append(l('web_saved'))
                        return render_template(
                            "config_editor.html",
                            l=l,
                            data=corrected,
                            config_tags=config_tags,
                            len=len,
                            join=str.join,
                            split=str.split,
                            type=type,
                            can_be_multiple=CanBeMultiple,
                            can_linebreak=CanLinebreak,
                            select=select,
                            str=str,
                            int=int,
                            bool=bool,
                            list=list,
                            map=map,
                            red=Red,
                            fix_required=FixRequired,
                            flash_messages=flash_messages,
                            flash_messages_red=flash_messages_red
                        )

        @app.route("/commands_editor", methods=["GET", "POST"])
        @auth.login_required
        async def commands_editor(request: Request):
            flash_messages = []
            flash_messages_red = []
            if request.method == "GET":
                data = load_json("commands.json")
                return render_template(
                    "commands_editor.html",
                    l=l,
                    data=data,
                    commands_tags=commands_tags,
                    len=len,
                    join=str.join,
                    split=str.split,
                    type=type,
                    can_be_multiple=CanBeMultiple,
                    select=select,
                    str=str,
                    int=int,
                    bool=bool,
                    list=list,
                    red=Red,
                    fix_required=FixRequired,
                    flash_messages=flash_messages,
                    flash_messages_red=flash_messages_red
                )
            elif request.method == "POST":
                flag = False
                raw = request.form
                data = load_json("commands.json")
                corrected = data
                for key_,tags in commands_tags.items():
                    keys = key_.replace("'","").replace("[","").split("]")
                    key = keys[0]
                    nest = len(keys) - 1

                    if nest == 1:
                        if dict in tags:
                            if not corrected[key]:
                                corrected[key] = {}
                        else:
                            value = raw.get(f"['{key}']")

                        if FixRequired in tags and value == corrected.get(key):
                            flash_messages_red.append(l('this_field_fix_required', key))
                            flag = True
                        corrected[key] = re.split(r'\r\n|\n',value) if value else []
                if flag:
                    return render_template(
                        "commands_editor.html",
                        l=l,
                        data=corrected,
                        commands_tags=commands_tags,
                        len=len,
                        join=str.join,
                        split=str.split,
                        type=type,
                        can_be_multiple=CanBeMultiple,
                        select=select,
                        str=str,
                        int=int,
                        bool=bool,
                        list=list,
                        red=Red,
                        fix_required=FixRequired,
                        flash_messages=flash_messages,
                        flash_messages_red=flash_messages_red
                    )
                else:
                    with open('commands.json', 'w', encoding='utf-8') as f:
                        json.dump(corrected, f, ensure_ascii=False, indent=4, sort_keys=False)
                    if raw.get("reload"):
                        Thread(target=restart, args=(1,)).start()
                        return sanic.response.redirect("/")
                    else:
                        flash_messages.append(l('web_saved'))
                        return render_template(
                            "commands_editor.html",
                            l=l,
                            data=corrected,
                            commands_tags=commands_tags,
                            len=len,
                            type=type,
                            can_be_multiple=CanBeMultiple,
                            select=select,
                            str=str,
                            int=int,
                            bool=bool,
                            list=list,
                            red=Red,
                            fix_required=FixRequired,
                            flash_messages=flash_messages,
                            flash_messages_red=flash_messages_red
                        )

        @app.route("/replies_editor", methods=["GET", "POST"])
        @auth.login_required
        async def replies_editor(request: Request):
            flash_messages = []
            flash_messages_red = []
            if request.method == "GET":
                data = load_json("replies.json")
                return render_template(
                    "replies_editor.html",
                    l=l,
                    data=data,
                    flash_messages=flash_messages,
                    flash_messages_red=flash_messages_red,
                    len=len,
                    enumerate=enumerate,
                    str=str
                )
            elif request.method == "POST":
                raw = request.form
                corrected = {}
                for num in range(0,int(raw["number"][0])):
                    trigger = raw.get(f"trigger{str(num)}")
                    if not trigger:
                        flash_messages_red.append(l('cannot_be_empty'))
                        break
                    content = raw.get(f"content{str(num)}")
                    if not content:
                        flash_messages_red.append(l('cannot_be_empty'))
                        break
                    corrected[trigger] = content
                with open('replies.json', 'w', encoding='utf-8') as f:
                    json.dump(corrected, f, ensure_ascii=False, indent=4, sort_keys=False)
                if raw.get("reload"):
                    Thread(target=restart, args=(1,)).start()
                    return sanic.response.redirect("/")
                else:
                    flash_messages.append(l('web_saved'))
                    return render_template(
                        "replies_editor.html",
                        l=l,
                        data=corrected,
                        flash_messages=flash_messages,
                        flash_messages_red=flash_messages_red,
                        len=len,
                        enumerate=enumerate,
                        str=str
                    )

        @app.route("/party_viewer", methods=["GET"])
        @auth.login_required
        async def party_viewer(request: Request):
            return render_template(
                "party_viewer.html",
                l=l,
                clients=clients,
                enumerate=enumerate
            )

        @app.route("/clients<num>", methods=["GET", "POST"])
        @auth.login_required
        async def clients_viewer(request: Request, num: str):
            num = int(num)
            client = clients[num] if clients[num:num+1] else None

            if not client:
                sanic.exceptions.abort(404)
            flash_messages = []
            if request.method == "GET":
                return render_template(
                    "clients_viewer.html",
                    l=l,
                    client=client,
                    none=None,
                    len=len,
                    flash_messages=flash_messages
                )
            else:
                if request.form.get("command"):
                    content = request.form["command"][0] if isinstance(request.form["command"],list) else request.form["command"]
                    message = WebMessage(content, request.cookies.get(auth.cookie_key, 'NoID'), client)
                    await process_command(message)
                    result = message.result
                    if result:
                        for mes in message.result:
                            for m in mes.split('\n'):
                                flash_messages.append(m)

                    return render_template(
                        "clients_viewer.html",
                        l=l,
                        client=client,
                        none=None,
                        len=len,
                        flash_messages=flash_messages
                    )
                else:
                    return sanic.response.redirect(f"/clients{num}")

        @app.route("/clients_info/<num>", methods=["GET"])
        @auth.login_required
        async def clients_info(request: Request, num: str):
            num = int(num)
            client = clients[num] if len(clients[num:num+1]) == 1 else None

            if not client:
                return sanic.response.json(
                    {
                        "error": "account_not_exists"
                    }
                )
            elif not client.isready:
                return sanic.response.json(
                    {
                        "error": "account_not_loaded"
                    }
                )
            elif not client.party or not client.party.me:
                return sanic.response.json(
                    {
                        "error": "party_moving"
                    }
                )
            else:
                return sanic.response.json(
                    {
                        "display_name": client.user.display_name,
                        "id": client.user.id,
                        "leader": client.party.me.leader,
                        "level": client.party.me.banner[2],
                        "outfit": member_asset(client.party.me, "outfit"),
                        "outfit_variants": client.party.me.outfit_variants,
                        "backpack": member_asset(client.party.me, "backpack"),
                        "backpack_variants": client.party.me.backpack_variants,
                        "pickaxe": member_asset(client.party.me, "pickaxe"),
                        "pickaxe_variants": client.party.me.pickaxe_variants,
                        "contrail": member_asset(client.party.me, "contrail"),
                        "emote": member_asset(client.party.me, "emote"),
                        "party_id": client.party.id,
                        "members": [
                            {
                                "display_name": i.display_name,
                                "id": i.id,
                                "leader": i.leader,
                                "level": i.banner[2],
                                "outfit": member_asset(i, "outfit"),
                                "outfit_variants": i.outfit_variants,
                                "backpack": member_asset(i, "backpack"),
                                "backpack_variants": i.backpack_variants,
                                "pickaxe": member_asset(i, "pickaxe"),
                                "pickaxe_variants": i.pickaxe_variants,
                                "contrail": member_asset(i, "contrail"),
                                "emote": member_asset(i, "emote")
                            } for i in client.party.members
                        ]
                    }
                )

        @app.route("/boot_switch", methods=["GET", "POST"])
        @auth.login_required
        async def boot_switch(request: Request):
            if request.method == "GET":
                return render_template(
                    "boot_switch.html",
                    l=l,
                    len=len
                )
            elif request.method == "POST":
                raw = request.form
                for i in raw.keys():
                    if "on" in i or "off" in i:
                        break
                on_or_off = i
                num = int(re.sub(r"on|off","", on_or_off))
                on_or_off = i.replace(str(num),"")
                loop = asyncio.get_event_loop()
                if on_or_off == "on":
                    clients[num].booting = True
                    loop.create_task(clients[num].start())
                elif on_or_off == "off":
                    loop.create_task(clients[num].close())
                return sanic.response.redirect("/boot_switch")

        @app.route("/boot_info", methods=["GET"])
        @auth.login_required
        async def boot_info(request: Request):
            data = {}
            for client in clients:
                if not client.booting and not client.isready:
                    data[client.email] = {
                        "info": "info_closed",
                        "booting": client.booting,
                        "isready": client.isready
                    }
                elif client.booting:
                    data[client.email] = {
                        "info": "info_booting",
                        "booting": client.booting,
                        "isready": client.isready
                    }
                elif client.isready:
                    data[client.email] = {
                        "info": "info_ready",
                        "booting": client.booting,
                        "isready": client.isready
                    }
            return sanic.response.json(data)

        @app.exception(sanic.exceptions.NotFound)
        async def not_found(request: Request, exception: Exception):
            return render_template("not_found.html", l=l)

        @auth.no_auth_handler
        async def unauthorized(request: Request, *args, **kwargs):
            return sanic.response.redirect("/")

loop = asyncio.get_event_loop()
if data.get('web',{}).get('enabled',True) is True or data.get('status',1)  == 0:
    loop.create_task(run_app())

Thread(target=dprint,args=(),daemon=True).start()
Thread(target=store_banner_data).start()
if data.get("status",1) != 0:
    try:
        langs = [
            data["search-lang"],
            data["sub-search-lang"]
        ] if data["sub-search-lang"] and data["sub-search-lang"] != data["search-lang"] else [
            data["search-lang"]
        ]
        store_item_data(langs)
    except Exception:
        send(l('bot'),l('api_downing'),red)
    langs = [
        data["search-lang"],
        data["sub-search-lang"]
    ] if data["sub-search-lang"] and data["sub-search-lang"] != data["search-lang"] else [
        data["search-lang"]
    ]
    items = {}
    styles = {}
    with ThreadPoolExecutor() as executor:
        items_futures = {executor.submit(search_item,lang,mode,data['fortnite'][type_.split(',')[0]],",".join(convert_to_new_type(i) for i in type_.split(','))): type_.split(',')[0] for lang in langs for mode in ("name","id") for type_ in ("outfit","backpack,pet","pickaxe","emote,emoji,toy")}
    for future,type_ in items_futures.items():
        result = future.result()
        if result and not items.get(type_):
            items[type_] = result[0]
    with ThreadPoolExecutor() as executor:
        styles_futures = {executor.submit(search_style,data["search-lang"],items.get(type_.split(',')[0],{}).get("id"),",".join(convert_to_new_type(i) for i in type_.split(','))): type_.split(',')[0] for type_ in ("outfit","backpack,pet","pickaxe") if data["fortnite"][f"{type_.split(',')[0]}_style"]}
    for future,type_ in styles_futures.items():
        result = future.result()
        if result and not styles.get(type_):
            variants = [i["variants"] for i in result if data["fortnite"][f"{type_}_style"] in i["name"]]
            if variants:
                styles[type_] = variants[0]
    for email in data["fortnite"]["email"]:
        email = email.strip()
        try:
            device_auth_details = get_device_auth_details().get(email.lower(), {})
            if not device_auth_details:
                device_auth_details = loop.run_until_complete(generate_device_auth_and_store(email))
            client = Client(
                auth=fortnitepy.DeviceAuth(
                    **device_auth_details
                ),
                default_party_config=fortnitepy.DefaultPartyConfig(
                    privacy=data['fortnite']['privacy']
                ),
                default_party_member_config=fortnitepy.DefaultPartyMemberConfig(
                    meta=[
                        partial(ClientPartyMember.set_outfit, items.get("outfit",{}).get("id",data["fortnite"]["outfit"]), variants=styles.get("outfit")),
                        partial(ClientPartyMember.set_backpack, items.get("backpack",{}).get("id",data["fortnite"]["backpack"]), variants=styles.get("backpack")),
                        partial(ClientPartyMember.set_pickaxe, items.get("pickaxe",{}).get("id",data["fortnite"]["pickaxe"]), variants=styles.get("pickaxe")),
                        partial(ClientPartyMember.set_battlepass_info, has_purchased=True, level=data['fortnite']['tier'], self_boost_xp=data['fortnite']['xpboost'], friend_boost_xp=data['fortnite']['friendxpboost']),
                        partial(ClientPartyMember.set_banner, icon=data['fortnite']['banner'], color=data['fortnite']['banner_color'], season_level=data['fortnite']['level'])
                    ]
                ),
                platform=fortnitepy.Platform(data['fortnite']['platform'].upper()),
                emote=items.get("emote",{}).get("id",data["fortnite"]["emote"])
            )
        except ValueError:
            send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(l("bot"),l('error_while_setting_client'),red,add_d=lambda x:f'>>> {x}')
            continue
        clients.append(client)

if data.get('status',1) != 0 and bot_ready:
    loop.create_task(run_bot())
try:
    loop.run_forever()
except KeyboardInterrupt:
    sys.exit(1)
