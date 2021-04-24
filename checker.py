import requests
import time
import os
import datetime
import pprint
import traceback
import sys
import json
import urllib.error
import urllib.request
import colorama
from colorama import Fore, Back, Style


if True: #Functions
    def now() -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d")

colorama.init(autoreset=True)
os.system(
    "TITLE ---- Fortnite Eazy Check ---- (仮名)/ Created by: Twitter @ZenomBot")

# Defines update mode
def Fortnite_check():

    print(Fore.GREEN+'\nプレイヤーの名前を入力してください')
    ask = input()
    print(Fore.GREEN+f'>> {ask} を検索中です. . .')
    time.sleep(1)

    response = requests.get(f'https://fortnite-api.com/v1/stats/br/v2?name={ask}')

    print('')
    try:
        data = response.json()['data']
        print(Fore.CYAN+f'{ask} の戦績取得に成功しました')
        time.sleep(1)
    except:
        error = response.json()['error']
        print(Fore.RED+f'{ask} の戦績取得に失敗しました')
        print('')
        time.sleep(0.5)
        error_info = error.replace(f"the requested account's stats are not public",f"詳細: {ask} はプライベートになっています\n\n>>>対処法: 設定の項目から「アカウントとプライバシー」に移動し、「キャリアランキングに表示」をオンにしてください").replace("the requested account does not exist","詳細: アカウントが存在しません")
        print(Fore.YELLOW+ error_info)
        time.sleep(4)
        print('もう一度正しいプレイヤー名を入力してください', f"\n前回の入力: {ask}")
        Fortnite_check()

    id = data["account"]["id"]
    name = data["account"]["name"]
    level = response.json()['data']['battlePass']['level']

    print(Fore.GREEN+'')
    print('---- プレイヤー詳細 ----')                                                 #プレイヤー情報
    print('――――――――――――')
    print('・ＩＤ　　　　|', id)
    print('――――――――――――')
    print('・名前　　　　|', name)
    print('――――――――――――')
    print('・レベル　　　|', level)
    print('――――――――――――')

    all = response.json()['data']['stats']['all']['overall']

    win_all = all['wins']             #勝利数
    top3_all = all['top3']            #トップ３
    top5_all = all['top5']            #トップ５
    kill_all = all['kills']           #キル数
    killa_all = all['killsPerMin']    #キル/分
    killb_all = all['killsPerMatch']  #平均キル
    die_all = all['deaths']           #死亡数
    kd_all = all['kd']                #キルデス比
    match_all = all['matches']        #試合数
    winrate_all = all['winRate']      #勝率

    print('')
    print('--------- 全体 --------- (ソロ+デュオ+トリオ+スクワッド)')                  #全体の戦績
    print('――――――――――――')
    print('・試合数　　　|', match_all)
    print('――――――――――――')
    print('・勝利数　　　|', win_all)
    print('――――――――――――')
    print('・勝率　　　　|', winrate_all)
    print('――――――――――――')
    print('・トップ３　　|', top3_all)
    print('――――――――――――')
    print('・トップ５　　|', top5_all)
    print('――――――――――――')
    print('・キル数　　　|', kill_all)
    print('――――――――――――')
    print('・キル％分　　|', killa_all)
    print('――――――――――――')
    print('・平均キル数　|', killb_all)
    print('――――――――――――')
    print('・ダウン数　　|', die_all)
    print('――――――――――――')
    print('・キルデス比　|', kd_all)
    print('――――――――――――')

    solo_all = response.json()['data']['stats']['all']['solo']

    win_solo_all = solo_all['wins']             #勝利数
    kill_solo_all = solo_all['kills']           #キル数
    killa_solo_all = solo_all['killsPerMin']    #キル/分
    killb_solo_all = solo_all['killsPerMatch']  #平均キル
    die_solo_all = solo_all['deaths']           #死亡数
    kd_solo_all = solo_all['kd']                #キルデス比
    match_solo_all = solo_all['matches']        #試合数
    winrate_solo_all = solo_all['winRate']      #勝率

    print('')
    print('------- 全体ソロ -------')                                                #全体の戦績：ソロ
    print('――――――――――――')
    print('・試合数　　　|', match_solo_all)
    print('――――――――――――')
    print('・勝利数　　　|', win_solo_all)
    print('――――――――――――')
    print('・勝率　　　　|', winrate_solo_all)
    print('――――――――――――')
    print('・キル数　　　|', kill_solo_all)
    print('――――――――――――')
    print('・キル％分　　|', killa_solo_all)
    print('――――――――――――')
    print('・平均キル数　|', killb_solo_all)
    print('――――――――――――')
    print('・ダウン数　　|', die_solo_all)
    print('――――――――――――')
    print('・キルデス比　|', kd_solo_all)
    print('――――――――――――')

    duo_all = response.json()['data']['stats']['all']['duo']

    win_duo_all = duo_all['wins']             #勝利数
    kill_duo_all = duo_all['kills']           #キル数
    killa_duo_all = duo_all['killsPerMin']    #キル/分
    killb_duo_all = duo_all['killsPerMatch']  #平均キル
    die_duo_all = duo_all['deaths']           #死亡数
    kd_duo_all = duo_all['kd']                #キルデス比
    match_duo_all = duo_all['matches']        #試合数
    winrate_duo_all = duo_all['winRate']      #勝率

    print('')
    print('------ 全体デュオ ------')                                                #全体の戦績：デュオ
    print('――――――――――――')
    print('・試合数　　　|', match_duo_all)
    print('――――――――――――')
    print('・勝利数　　　|', win_duo_all)
    print('――――――――――――')
    print('・勝率　　　　|', winrate_duo_all)
    print('――――――――――――')
    print('・キル数　　　|', kill_duo_all)
    print('――――――――――――')
    print('・キル％分　　|', killa_duo_all)
    print('――――――――――――')
    print('・平均キル数　|', killb_duo_all)
    print('――――――――――――')
    print('・ダウン数　　|', die_duo_all)
    print('――――――――――――')
    print('・キルデス比　|', kd_duo_all)
    print('――――――――――――')

    trio_all = response.json()['data']['stats']['all']['trio']

    win_trio_all = trio_all['wins']             #勝利数
    kill_trio_all = trio_all['kills']           #キル数
    killa_trio_all = trio_all['killsPerMin']    #キル/分
    killb_trio_all = trio_all['killsPerMatch']  #平均キル
    die_trio_all = trio_all['deaths']           #死亡数
    kd_trio_all = trio_all['kd']                #キルデス比
    match_trio_all = trio_all['matches']        #試合数
    winrate_trio_all = trio_all['winRate']      #勝率

    print('')
    print('------ 全体トリオ ------')                                                #全体の戦績：トリオ
    print('――――――――――――')
    print('・試合数　　　|', match_trio_all)
    print('――――――――――――')
    print('・勝利数　　　|', win_trio_all)
    print('――――――――――――')
    print('・勝率　　　　|', winrate_trio_all)
    print('――――――――――――')
    print('・キル数　　　|', kill_trio_all)
    print('――――――――――――')
    print('・キル％分　　|', killa_trio_all)
    print('――――――――――――')
    print('・平均キル数　|', killb_trio_all)
    print('――――――――――――')
    print('・ダウン数　　|', die_trio_all)
    print('――――――――――――')
    print('・キルデス比　|', kd_trio_all)
    print('――――――――――――')

    squad_all = response.json()['data']['stats']['all']['squad']

    win_squad_all = squad_all['wins']             #勝利数
    kill_squad_all = squad_all['kills']           #キル数
    killa_squad_all = squad_all['killsPerMin']    #キル/分
    killb_squad_all = squad_all['killsPerMatch']  #平均キル
    die_squad_all = squad_all['deaths']           #死亡数
    kd_squad_all = squad_all['kd']                #キルデス比
    match_squad_all = squad_all['matches']        #試合数
    winrate_squad_all = squad_all['winRate']      #勝率

    print('')
    print('---- 全体スクワッド ----')                                                 #全体の戦績：スクワッド
    print('――――――――――――')
    print('・試合数　　　|', match_squad_all)
    print('――――――――――――')
    print('・勝利数　　　|', win_squad_all)
    print('――――――――――――')
    print('・勝率　　　　|', winrate_squad_all)
    print('――――――――――――')
    print('・キル数　　　|', kill_squad_all)
    print('――――――――――――')
    print('・キル％分　　|', killa_squad_all)
    print('――――――――――――')
    print('・平均キル数　|', killb_squad_all)
    print('――――――――――――')
    print('・ダウン数　　|', die_squad_all)
    print('――――――――――――')
    print('・キルデス比　|', kd_squad_all)
    print('――――――――――――')

    try:
        key = response.json()['data']['stats']['keyboardMouse']['overall']

        win_key = key['wins']             #勝利数
        top3_key = key['top3']            #トップ３
        top5_key = key['top5']            #トップ５
        kill_key = key['kills']           #キル数
        killa_key = key['killsPerMin']    #キル/分
        killb_key = key['killsPerMatch']  #平均キル
        die_key = key['deaths']           #死亡数
        kd_key = key['kd']                #キルデス比
        match_key = key['matches']        #試合数
        winrate_key = key['winRate']      #勝率

        print('')
        print('--- キーボード --- (ソロ+デュオ+トリオ+スクワッド)')                     #キーボードの戦績
        print('――――――――――――')
        print('・試合数　　　|', match_key)
        print('――――――――――――')
        print('・勝利数　　　|', win_key)
        print('――――――――――――')
        print('・勝率　　　　|', winrate_key)
        print('――――――――――――')
        print('・トップ３　　|', top3_key)
        print('――――――――――――')
        print('・トップ５　　|', top5_key)
        print('――――――――――――')
        print('・キル数　　　|', kill_key)
        print('――――――――――――')
        print('・キル％分　　|', killa_key)
        print('――――――――――――')
        print('・平均キル数　|', killb_key)
        print('――――――――――――')
        print('・ダウン数　　|', die_key)
        print('――――――――――――')
        print('・キルデス比　|', kd_key)
        print('――――――――――――')

        solo_key = response.json()['data']['stats']['keyboardMouse']['solo']

        win_solo_key = solo_key['wins']             #勝利数
        kill_solo_key = solo_key['kills']           #キル数
        killa_solo_key = solo_key['killsPerMin']    #キル/分
        killb_solo_key = solo_key['killsPerMatch']  #平均キル
        die_solo_key = solo_key['deaths']           #死亡数
        kd_solo_key = solo_key['kd']                #キルデス比
        match_solo_key = solo_key['matches']        #試合数
        winrate_solo_key = solo_key['winRate']      #勝率

        print('')
        print('---- キーボードソロ ----')                                         #キーボードの戦績：ソロ
        print('――――――――――――')
        print('・試合数　　　|', match_solo_key)
        print('――――――――――――')
        print('・勝利数　　　|', win_solo_key)
        print('――――――――――――')
        print('・勝率　　　　|', winrate_solo_key)
        print('――――――――――――')
        print('・キル数　　　|', kill_solo_key)
        print('――――――――――――')
        print('・キル％分　　|', killa_solo_key)
        print('――――――――――――')
        print('・平均キル数　|', killb_solo_key)
        print('――――――――――――')
        print('・ダウン数　　|', die_solo_key)
        print('――――――――――――')
        print('・キルデス比　|', kd_solo_key)
        print('――――――――――――')

        duo_key = response.json()['data']['stats']['keyboardMouse']['duo']

        win_duo_key = duo_key['wins']             #勝利数
        kill_duo_key = duo_key['kills']           #キル数
        killa_duo_key = duo_key['killsPerMin']    #キル/分
        killb_duo_key = duo_key['killsPerMatch']  #平均キル
        die_duo_key = duo_key['deaths']           #死亡数
        kd_duo_key = duo_key['kd']                #キルデス比
        match_duo_key = duo_key['matches']        #試合数
        winrate_duo_key = duo_key['winRate']      #勝率

        print('')
        print('--- キーボードデュオ ---')                                             #キーボードの戦績：デュオ
        print('――――――――――――')
        print('・試合数　　　|', match_duo_key)
        print('――――――――――――')
        print('・勝利数　　　|', win_duo_key)
        print('――――――――――――')
        print('・勝率　　　　|', winrate_duo_key)
        print('――――――――――――')
        print('・キル数　　　|', kill_duo_key)
        print('――――――――――――')
        print('・キル％分　　|', killa_duo_key)
        print('――――――――――――')
        print('・平均キル数　|', killb_duo_key)
        print('――――――――――――')
        print('・ダウン数　　|', die_duo_key)
        print('――――――――――――')
        print('・キルデス比　|', kd_duo_key)
        print('――――――――――――')

        trio_key = response.json()['data']['stats']['keyboardMouse']['trio']

        win_trio_key = trio_key['wins']             #勝利数
        kill_trio_key = trio_key['kills']           #キル数
        killa_trio_key = trio_key['killsPerMin']    #キル/分
        killb_trio_key = trio_key['killsPerMatch']  #平均キル
        die_trio_key = trio_key['deaths']           #死亡数
        kd_trio_key = trio_key['kd']                #キルデス比
        match_trio_key = trio_key['matches']        #試合数
        winrate_trio_key = trio_key['winRate']      #勝率

        print('')
        print('--- キーボードトリオ ---')                                             #キーボードの戦績：トリオ
        print('――――――――――――')
        print('・試合数　　　|', match_trio_key)
        print('――――――――――――')
        print('・勝利数　　　|', win_trio_key)
        print('――――――――――――')
        print('・勝率　　　　|', winrate_trio_key)
        print('――――――――――――')
        print('・キル数　　　|', kill_trio_key)
        print('――――――――――――')
        print('・キル％分　　|', killa_trio_key)
        print('――――――――――――')
        print('・平均キル数　|', killb_trio_key)
        print('――――――――――――')
        print('・ダウン数　　|', die_trio_key)
        print('――――――――――――')
        print('・キルデス比　|', kd_trio_key)
        print('――――――――――――')

        squad_key = response.json()['data']['stats']['keyboardMouse']['squad']

        win_squad_key = squad_key['wins']             #勝利数
        kill_squad_key = squad_key['kills']           #キル数
        killa_squad_key = squad_key['killsPerMin']    #キル/分
        killb_squad_key = squad_key['killsPerMatch']  #平均キル
        die_squad_key = squad_key['deaths']           #死亡数
        kd_squad_key = squad_key['kd']                #キルデス比
        match_squad_key = squad_key['matches']        #試合数
        winrate_squad_key = squad_key['winRate']      #勝率

        print('')
        print('- キーボードスクワッド -')                                             #キーボードの戦績：スクワッド
        print('――――――――――――')
        print('・試合数　　　|', match_squad_key)
        print('――――――――――――')
        print('・勝利数　　　|', win_squad_key)
        print('――――――――――――')
        print('・勝率　　　　|', winrate_squad_key)
        print('――――――――――――')
        print('・キル数　　　|', kill_squad_key)
        print('――――――――――――')
        print('・キル％分　　|', killa_squad_key)
        print('――――――――――――')
        print('・平均キル数　|', killb_squad_key)
        print('――――――――――――')
        print('・ダウン数　　|', die_squad_key)
        print('――――――――――――')
        print('・キルデス比　|', kd_squad_key)
        print('――――――――――――')

    except:
        print('')
        print(Fore.YELLOW+'｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜')
        print(Fore.YELLOW+'｜キーボードマウスの戦績はありません｜')
        print(Fore.YELLOW+'｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜'+Fore.GREEN)
    try:
        pad = response.json()['data']['stats']['gamepad']['overall']

        win_pad = pad['wins']             #勝利数
        top3_pad = pad['top3']            #トップ３
        top5_pad = pad['top5']            #トップ５
        kill_pad = pad['kills']           #キル数
        killa_pad = pad['killsPerMin']    #キル/分
        killb_pad = pad['killsPerMatch']  #平均キル
        die_pad = pad['deaths']           #死亡数
        kd_pad = pad['kd']                #キルデス比
        match_pad = pad['matches']        #試合数
        winrate_pad = pad['winRate']      #勝率

        print(Fore.GREEN+'')
        print('----- パッド ----- (ソロ+デュオ+トリオ+スクワッド)')                    #パッドの戦績
        print('――――――――――――')
        print('・試合数　　　|', match_pad)
        print('――――――――――――')
        print('・勝利数　　　|', win_pad)
        print('――――――――――――')
        print('・勝率　　　　|', winrate_pad)
        print('――――――――――――')
        print('・トップ３　　|', top3_pad)
        print('――――――――――――')
        print('・トップ５　　|', top5_pad)
        print('――――――――――――')
        print('・キル数　　　|', kill_pad)
        print('――――――――――――')
        print('・キル％分　　|', killa_pad)
        print('――――――――――――')
        print('・平均キル数　|', killb_pad)
        print('――――――――――――')
        print('・ダウン数　　|', die_pad)
        print('――――――――――――')
        print('・キルデス比　|', kd_pad)
        print('――――――――――――')

        solo_pad = response.json()['data']['stats']['gamepad']['solo']

        win_solo_pad = solo_pad['wins']             #勝利数
        kill_solo_pad = solo_pad['kills']           #キル数
        killa_solo_pad = solo_pad['killsPerMin']    #キル/分
        killb_solo_pad = solo_pad['killsPerMatch']  #平均キル
        die_solo_pad = solo_pad['deaths']           #死亡数
        kd_solo_pad = solo_pad['kd']                #キルデス比
        match_solo_pad = solo_pad['matches']        #試合数
        winrate_solo_pad = solo_pad['winRate']      #勝率

        print('')
        print('------ パッドソロ ------')                                            #パッドの戦績：ソロ
        print('――――――――――――')
        print('・試合数　　　|', match_solo_pad)
        print('――――――――――――')
        print('・勝利数　　　|', win_solo_pad)
        print('――――――――――――')
        print('・勝率　　　　|', winrate_solo_pad)
        print('――――――――――――')
        print('・キル数　　　|', kill_solo_pad)
        print('――――――――――――')
        print('・キル％分　　|', killa_solo_pad)
        print('――――――――――――')
        print('・平均キル数　|', killb_solo_pad)
        print('――――――――――――')
        print('・ダウン数　　|', die_solo_pad)
        print('――――――――――――')
        print('・キルデス比　|', kd_solo_pad)
        print('――――――――――――')

        duo_pad = response.json()['data']['stats']['gamepad']['duo']

        win_duo_pad = duo_pad['wins']             #勝利数
        kill_duo_pad = duo_pad['kills']           #キル数
        killa_duo_pad = duo_pad['killsPerMin']    #キル/分
        killb_duo_pad = duo_pad['killsPerMatch']  #平均キル
        die_duo_pad = duo_pad['deaths']           #死亡数
        kd_duo_pad = duo_pad['kd']                #キルデス比
        match_duo_pad = duo_pad['matches']        #試合数
        winrate_duo_pad = duo_pad['winRate']      #勝率

        print('')
        print('----- パッドデュオ -----')                                            #パッドの戦績：デュオ
        print('――――――――――――')
        print('・試合数　　　|', match_duo_pad)
        print('――――――――――――')
        print('・勝利数　　　|', win_duo_pad)
        print('――――――――――――')
        print('・勝率　　　　|', winrate_duo_pad)
        print('――――――――――――')
        print('・キル数　　　|', kill_duo_pad)
        print('――――――――――――')
        print('・キル％分　　|', killa_duo_pad)
        print('――――――――――――')
        print('・平均キル数　|', killb_duo_pad)
        print('――――――――――――')
        print('・ダウン数　　|', die_duo_pad)
        print('――――――――――――')
        print('・キルデス比　|', kd_duo_pad)
        print('――――――――――――')

        trio_pad = response.json()['data']['stats']['gamepad']['trio']

        win_trio_pad = trio_pad['wins']             #勝利数
        kill_trio_pad = trio_pad['kills']           #キル数
        killa_trio_pad = trio_pad['killsPerMin']    #キル/分
        killb_trio_pad = trio_pad['killsPerMatch']  #平均キル
        die_trio_pad = trio_pad['deaths']           #死亡数
        kd_trio_pad = trio_pad['kd']                #キルデス比
        match_trio_pad = trio_pad['matches']        #試合数
        winrate_trio_pad = trio_pad['winRate']      #勝率

        print('')
        print('----- パッドトリオ -----')                                            #パッドの戦績：トリオ
        print('――――――――――――')
        print('・試合数　　　|', match_trio_pad)
        print('――――――――――――')
        print('・勝利数　　　|', win_trio_pad)
        print('――――――――――――')
        print('・勝率　　　　|', winrate_trio_pad)
        print('――――――――――――')
        print('・キル数　　　|', kill_trio_pad)
        print('――――――――――――')
        print('・キル％分　　|', killa_trio_pad)
        print('――――――――――――')
        print('・平均キル数　|', killb_trio_pad)
        print('――――――――――――')
        print('・ダウン数　　|', die_trio_pad)
        print('――――――――――――')
        print('・キルデス比　|', kd_trio_pad)
        print('――――――――――――')

        squad_pad = response.json()['data']['stats']['gamepad']['squad']

        win_squad_pad = squad_pad['wins']             #勝利数
        kill_squad_pad = squad_pad['kills']           #キル数
        killa_squad_pad = squad_pad['killsPerMin']    #キル/分
        killb_squad_pad = squad_pad['killsPerMatch']  #平均キル
        die_squad_pad = squad_pad['deaths']           #死亡数
        kd_squad_pad = squad_pad['kd']                #キルデス比
        match_squad_pad = squad_pad['matches']        #試合数
        winrate_squad_pad = squad_pad['winRate']      #勝率

        print('')
        print('--- パッドスクワッド ---')                                             #パッドの戦績：スクワッド
        print('――――――――――――')
        print('・試合数　　　|', match_squad_pad)
        print('――――――――――――')
        print('・勝利数　　　|', win_squad_pad)
        print('――――――――――――')
        print('・勝率　　　　|', winrate_squad_pad)
        print('――――――――――――')
        print('・キル数　　　|', kill_squad_pad)
        print('――――――――――――')
        print('・キル％分　　|', killa_squad_pad)
        print('――――――――――――')
        print('・平均キル数　|', killb_squad_pad)
        print('――――――――――――')
        print('・ダウン数　　|', die_squad_pad)
        print('――――――――――――')
        print('・キルデス比　|', kd_squad_pad)
        print('――――――――――――')
    except:
        print('')
        print(Fore.YELLOW+'｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜')
        print(Fore.YELLOW+'｜ゲームパッドの戦績はありません｜')
        print(Fore.YELLOW+'｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜'+Fore.GREEN)
    time.sleep(5)
    Fortnite_check()


def Fortnite_item():
    print(Fore.GREEN+'\nアイテム名を入力してください')
    item = input()
    print(f'>> {item} を検索中です. . .')
    time.sleep(1)

    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?searchlanguage=ja&language=ja&name={item}')
    print('')
    try:
        data = response.json()['data']['name']
        print(Fore.CYAN+f'{data} のデータ取得に成功しました')
        time.sleep(1)
    except:
        error = response.json()['error']
        print(Fore.RED+f'{item} のデータ取得に失敗しました')
        print('')
        time.sleep(0.7)
        error_info = error.replace(f"no cosmetic matching the search parameters was found",f"詳細: {item} が見つかりませんでした\n\n>>>対処法: 正しいアイテム名が入力されているかご確認ください\nアイテムは名は完全一致している必要があります")
        print(Fore.YELLOW+ error_info)
        time.sleep(4)
        print('もう一度正しいアイテム名を入力してください', f"\n前回の入力: {item}\n")
        Fortnite_item()

    i = response.json()['data']
    id = i['id']
    name = i['name']
    desc = i['description']
    type = i['type']['displayValue']
    rarity = i['rarity']['displayValue']
    try:
        set = i['set']['text']
    except:
        set = 'なし'
    info = i['introduction']['text']


    print('\n')
    print(Fore.YELLOW+'ＩＤ　　|', Fore.YELLOW+id)
    print('――――――――――――')
    print('タイプ　|', type)
    print('――――――――――――')
    print('名前　　|', name)
    print('――――――――――――')
    print('説明　　|', desc)
    print('――――――――――――')
    print('レア度　|', rarity)
    print('――――――――――――')
    print('セット　|', set)
    print('――――――――――――')
    print('導入　　|', info)
    print('――――――――――――')
    print('')
    time.sleep(1)
    print(Fore.YELLOW+f"{type}: {name}"+Fore.GREEN+" の画像を保存しますか？ \n'yes' or 'no' を入力してください")
    option_choice = input(Fore.GREEN+">> "+Fore.RESET)
    if option_choice == "yes":
        def download_file(url, dst_path):
            try:
                print('画像を保存しています')
                with urllib.request.urlopen(url) as web_file:
                    data = web_file.read()
                    with open(dst_path, mode='wb') as local_file:
                        local_file.write(data)
            except urllib.error.URLError as e:
                print(e)
        try:
            image = response.json()['data']['images']['icon']
            url = f'{image}'
            dst_path = f'icons/{name}.png'
            download_file(url, dst_path)
            print('')
            print(Fore.CYAN+'iconsフォルダーに'+Fore.YELLOW+f' {name}.png '+Fore.CYAN+'の画像を保存しました'+Fore.RESET+f'')
            print('')
            time.sleep(6)
            Fortnite_item()
        except:
            print(Fore.RED+'iconsフォルダーがありません...')
            time.sleep(1)
            os.mkdir('icons')
            print(Fore.CYAN+'iconsフォルダーを作成しました')
            print('もう一度やり直してください')
            Fortnite_item()



    elif option_choice == "no":
        print(Fore.YELLOW+f'{name}'+Fore.RESET+' の画像を保存しませんでした')
        time.sleep(2)
        Fortnite_item()
    else:
        print('')
        print(Fore.RED+"'yes' or 'no'の入力が確認できなかったためアイテム検索に戻ります")
        time.sleep(3)
        Fortnite_item()

def Fortnite_news():
    print('最新のニュースを取得しています...')
    print('')
    response = requests.get(f'https://fortnite-api.com/v2/news?language=ja')
    try:
        data = response.json()['data']
        print(Fore.CYAN+'取得に成功しました'+Fore.RESET+'\n画像を保存しています')
    except:
        print('取得に失敗しました\n6秒後に再取得を開始します')
        time.sleep(6)
        Fortnite_news()

    def download_file(url, dst_path):
        try:
            with urllib.request.urlopen(url) as web_file:
                data = web_file.read()
                with open(dst_path, mode='wb') as local_file:
                    local_file.write(data)
        except urllib.error.URLError as e:
            print(e)

    try:
        image = response.json()['data']['br']['image']
        url = f'{image}'
        dst_path = f'news/{now()}news.gif'
        download_file(url, dst_path)
        print('')
        print(Fore.CYAN+'newsフォルダーに'+Fore.YELLOW+f' {now()}news.gif '+Fore.CYAN+'の画像を保存しました'+Fore.RESET+f'')
        print('')
        print('6秒後にメニューへ移動します')
        time.sleep(6)
        print('')
        print('')
        remenu()
    except:
        print('')
        print(Fore.RED+'newsフォルダーが存在しません。')
        os.mkdir('news')
        time.sleep(1)
        print(Fore.CYAN+'newsフォルダーを作成しました')
        print('')
        print('再取得を開始します')
        time.sleep(3)
        Fortnite_news()



def Update():
    def CheckUpdate(filename: str, githuburl: str, overwrite: bool = False) -> bool:
        print(f'{filename} の更新ファイルがあるかチェックします')
        try:
            if "/" in filename:
                os.makedirs("/".join(filename.split("/")[:-1]), exist_ok=True)
            for count, text in enumerate(filename[::-1]):
                if text == ".":
                    filename_ = filename[:len(filename)-count-1]
                    extension = filename[-count-1:]
                    break
            else:
                extension = ""
            if extension in [".py", ".bat", ".txt", ".md", ".html", ".exe", ""]:
                if os.path.isfile(filename):
                    with open(filename, "r", encoding='utf-8') as f:
                        current = f.read()
                else:
                    github = requests.get(githuburl + filename)
                    if github.status_code != 200:
                        print(Fore.RED+f'{filename} ファイルが見つかりませんでした')
                        return None
                    github.encoding = github.apparent_encoding
                    github = github.text.encode(encoding='utf-8')
                    with open(filename, "wb") as f:
                        f.write(github)
                    with open(filename, "r", encoding='utf-8') as f:
                        current = f.read()
                github = requests.get(githuburl + filename)
                if github.status_code != 200:
                    print(Fore.RED+f'{filename} ファイルが見つかりませんでした')
                    return None
                github.encoding = github.apparent_encoding
                github = github.text.encode(encoding='utf-8')
                if current.replace('\n','').replace('\r','').encode(encoding='utf-8') != github.decode().replace('\n','').replace('\r','').encode(encoding='utf-8'):
                    print(Fore.CYAN+f'{filename} の更新ファイルが見つかりました')
                    print(f'{filename} のバックアップを作成します')
                    if os.path.isfile(f'old-{filename_}{extension}'):
                        try:
                            os.remove(f'old-{filename_}{extension}')
                        except PermissionError:
                            print(Fore.RED+f'{filename} の古いファイルを削除できませんでした')
                            print(traceback.format_exc())
                    try:
                        os.rename(filename, f'old-{filename_}{extension}')
                    except PermissionError:
                        print(Fore.RED+f'{filename} ファイルのバックアップに失敗しました')
                        print(traceback.format_exc())
                    else:
                        with open(filename, "wb") as f:
                            f.write(github)
                        print(Fore.CYAN+f'{filename} の更新ファイルのインストールに成功しました')
                        return True
                else:
                    print(Fore.RED+f'{filename} ファイルが見つかりませんでした')
                    return False
            elif extension == ".json":
                if os.path.isfile(filename):
                    with open(filename, "r", encoding='utf-8') as f:
                        current = json.load(f)
                else:
                    github = requests.get(githuburl + filename)
                    if github.status_code != 200:
                        print(Fore.RED+f'{filename} ファイルが見つかりませんでした')
                        return None
                    github.encoding = github.apparent_encoding
                    github = github.text.encode(encoding='utf-8')
                    with open(filename, "wb") as f:
                        f.write(github)
                    try:
                        with open(filename, "r", encoding='utf-8') as f:
                            current = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open(filename, "r", encoding='utf-8-sig') as f:
                            current = json.load(f)
                github = requests.get(githuburl + filename)
                if github.status_code != 200:
                    print(Fore.RED+f'{filename} ファイルが見つかりませんでした')
                    return None
                github.encoding = github.apparent_encoding
                github = github.text
                github = json.loads(github)

                if overwrite:
                    if current != github:
                        print(Fore.CYAN+f'{filename} の更新ファイルが見つかりました')
                        print(f'{filename} をバックアップしています')
                        if os.path.isfile(f'old-{filename_}{extension}'):
                            try:
                                os.remove(f'old-{filename_}{extension}')
                            except PermissionError:
                                print(Fore.RED+f'{filename} の古いファイルを削除できませんでした')
                                print(traceback.format_exc())
                        try:
                            os.rename(filename, f'{filename_}_old{extension}')
                        except PermissionError:
                            print(Fore.RED+f'{filename} ファイルのバックアップに失敗しました')
                            print(traceback.format_exc())
                        else:
                            with open(filename, "w", encoding="utf-8") as f:
                                json.dump(github, f, indent=4, ensure_ascii=False)
                            print(Fore.CYAN+f'{filename} の更新ファイルのインストールに成功しました')
                            return True
                    else:
                        print(Fore.YELLOW+f'{filename} の更新は見つかりませんでした')
                        return False
                else:
                    new = AddNewKey(current, github)
                    if current != new:
                        print(Fore.CYAN+f'{filename} の更新ファイルが見つかりました')
                        print(f'{filename} のバックアップを作成しています')
                        try:
                            if os.path.isfile(f'old-{filename_}{extension}'):
                                try:
                                    os.remove(f'old-{filename_}{extension}')
                                except PermissionError:
                                    print(Fore.RED+f'old-{filename_}{extension} ファイルを削除できませんでした')
                                    print(Fore.RED+f'{traceback.format_exc()}\n')
                            os.rename(filename, f'old-{filename_}{extension}')
                        except PermissionError:
                            print(Fore.RED+f'{filename} ファイルのバックアップに失敗しました')
                            print(Fore.RED+f'{traceback.format_exc()}\n')
                            return None
                        else:
                            with open(filename, 'w', encoding="utf-8") as f:
                                json.dump(new, f, indent=4, ensure_ascii=False)
                            print(Fore.CYAN+f'{filename} の更新ファイルのインストールに成功しました')
                            return True
                    else:
                        print(Fore.YELLOW+f'{filename} の更新は見つかりませんでした')
                        return False
            elif extension == ".png":
                if os.path.isfile(filename):
                    with open(filename, "rb") as f:
                        current = f.read()
                else:
                    github = requests.get(githuburl + filename)
                    if github.status_code != 200:
                        print(Fore.RED+f'{filename} ファイルが見つかりませんでした')
                        return None
                    github = github.content
                    with open(filename, "wb") as f:
                        f.write(github)
                    with open(filename, "rb") as f:
                        current = f.read()
                github = requests.get(githuburl + filename)
                if github.status_code != 200:
                    print(Fore.RED+f'{filename} のファイルが見つかりませんでした')
                    return None
                github = github.content
                if current != github:
                    print(Fore.CYAN+f'{filename} の更新ファイルが見つかりました')
                    print(f'{filename} をバックアップしています')
                    if os.path.isfile(f'old-{filename_}{extension}'):
                        try:
                            os.remove(f'old-{filename_}{extension}')
                        except PermissionError:
                            print(Fore.RED+f'{filename} の古いファイルを削除できませんでした')
                            print(traceback.format_exc())
                    try:
                        os.rename(filename, f'old-{filename_}{extension}')
                    except PermissionError:
                        print(f'{filename} ファイルのバックアップに失敗しました')
                        print(traceback.format_exc())
                    else:
                        with open(filename, "wb") as f:
                            f.write(github)
                        print(f'{filename} の更新ファイルのインストールに成功しました')
                        return True
                else:
                    print(Fore.YELOOW+f'{filename} の更新は見つかりませんでした')
                    return False
            else:
                print(Fore.RED+f'{extension} は無効な拡張子です')
                return None
        except Exception:
            print(Fore.RED+"更新に失敗しました")
            print(f'{traceback.format_exc()}\n')
            return None
    if "-dev" in sys.argv:
        githuburl = "https://raw.githubusercontent.com/Zenom-Git/Fortnite-C/Dev/"
    else:
        githuburl = "https://raw.githubusercontent.com/Zenom-Git/Fortnite-C/master/"

    if CheckUpdate("checker.py", githuburl):
        print(Fore.CYAN+"checker.py の更新ファイルが見つかりました。"+Fore.YELLOW+"再起動してください")
        time.sleep(6)
        exit()

def renumber():
    print("")
    option_choice = input(Fore.GREEN+">> "+Fore.RESET)
    if option_choice == "1":
        Fortnite_check()
    elif option_choice == "2":
        Fortnite_item()
    elif option_choice == "3":
        Fortnite_news()
    elif option_choice == "4":
        Update()
    else:
        print(Fore.RED+"1～4 の中から半角数字を入力してください")
        renumber()

def remenu():
    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTYELLOW_EX+"\n   - - - - メニュー一覧 - - - -   "+Back.RESET)
    time.sleep(0.1)
    print(Back.LIGHTYELLOW_EX+"      　 　　　　　　　　　　　 　"+Back.RESET)
    time.sleep(0.1)
    print(Fore.BLACK+Back.LIGHTYELLOW_EX+" (1) - フォートナイトの戦績を見る "+Back.RESET)
    time.sleep(0.1)
    print(Fore.BLACK+Back.LIGHTYELLOW_EX+" (2) - アイテムを検索する　　　　 "+Back.RESET)
    time.sleep(0.1)
    print(Fore.BLACK+Back.LIGHTYELLOW_EX+" (3) - 最新のニュースを取得する　 "+Back.RESET)
    time.sleep(0.1)
    print(Fore.BLACK+Back.LIGHTYELLOW_EX+" (4) - アップデートを確認する　　 "+Back.RESET)
    print(Back.LIGHTYELLOW_EX+"      　　　　 　　　　　　　　　 "+Back.RESET)
    time.sleep(0.1)
    print(Fore.BLUE+Back.LIGHTYELLOW_EX+"　- 製作者: Twitter @ZenomBot -　 "+Back.RESET)
    time.sleep(0.1)
    print(Fore.BLACK+Back.LIGHTYELLOW_EX+" バグなどがありましたらTwitterへ  "+Back.RESET)
    time.sleep(0.1)
    print(Fore.BLACK+Back.LIGHTYELLOW_EX+" ご連絡お願いします　　　　　　　 "+Back.RESET)
    time.sleep(0.1)
    print(Back.LIGHTYELLOW_EX+"      　　　　 　　　　　　　　　 "+Back.RESET)
    time.sleep(0.2)
    print(Fore.GREEN+"\n上記のメニューの中から数字を選択してください")
    option_choice = input(Fore.GREEN+">> "+Fore.RESET)
    if option_choice == "1":
        Fortnite_check()
    elif option_choice == "2":
        Fortnite_item()
    elif option_choice == "3":
        Fortnite_news()
    elif option_choice == "4":
        Update()
    else:
        print(Fore.RED+"1～4 の中から半角数字を入力してください")
        renumber()

print('')
print(Fore.LIGHTRED_EX+'ここへアップデート内容が記載されます')
time.sleep(0.5)
print(Fore.LIGHTMAGENTA_EX+Back.LIGHTYELLOW_EX+"\n   - - - - メニュー一覧 - - - -   ")
time.sleep(0.1)
print(Back.LIGHTYELLOW_EX+"      　 　　　　　　　　　　　 　")
time.sleep(0.1)
print(Fore.BLACK+Back.LIGHTYELLOW_EX+" (1) - フォートナイトの戦績を見る ")
time.sleep(0.1)
print(Fore.BLACK+Back.LIGHTYELLOW_EX+" (2) - アイテムを検索する　　　　 ")
time.sleep(0.1)
print(Fore.BLACK+Back.LIGHTYELLOW_EX+" (3) - 最新のニュースを取得する　 ")
time.sleep(0.1)
print(Fore.BLACK+Back.LIGHTYELLOW_EX+" (4) - アップデートを確認する　　 ")
print(Back.LIGHTYELLOW_EX+"      　　　　 　　　　　　　　　 ")
time.sleep(0.1)
print(Fore.BLUE+Back.LIGHTYELLOW_EX+"　- 製作者: Twitter @ZenomBot -　 ")
time.sleep(0.1)
print(Fore.BLACK+Back.LIGHTYELLOW_EX+" バグなどがありましたらTwitterへ  ")
time.sleep(0.1)
print(Fore.BLACK+Back.LIGHTYELLOW_EX+" ご連絡お願いします　　　　　　　 ")
time.sleep(0.1)
print(Back.LIGHTYELLOW_EX+"      　　　　 　　　　　　　　　 ")
time.sleep(0.2)
print(Fore.GREEN+"\n上記のメニューの中から数字を選択してください")
option_choice = input(Fore.GREEN+">> "+Fore.RESET)
if option_choice == "1":
    Fortnite_check()
elif option_choice == "2":
    Fortnite_item()
elif option_choice == "3":
    Fortnite_news()
elif option_choice == "4":
    Update()
else:
    print(Fore.RED+"1～4 の中から半角数字を入力してください")
    renumber()
