#!/usr/bin/python3
# usage: ./*.py [json]

import re, sys, json
from datetime import datetime

header = "バージョン,タイトル,ジャンル,アーティスト,プレー回数,BEGINNER 難易度,BEGINNER EXスコア,BEGINNER PGreat,BEGINNER Great,BEGINNER ミスカウント,BEGINNER クリアタイプ,BEGINNER DJ LEVEL,NORMAL 難易度,NORMAL EXスコア,NORMAL PGreat,NORMAL Great,NORMAL ミスカウント,NORMAL クリアタイプ,NORMAL DJ LEVEL,HYPER 難易度,HYPER EXスコア,HYPER PGreat,HYPER Great,HYPER ミスカウント,HYPER クリアタイプ,HYPER DJ LEVEL,ANOTHER 難易度,ANOTHER EXスコア,ANOTHER PGreat,ANOTHER Great,ANOTHER ミスカウント,ANOTHER クリアタイプ,ANOTHER DJ LEVEL,BEGINNER 難易度,BEGINNER EXスコア,BEGINNER PGreat,BEGINNER Great,BEGINNER ミスカウント,BEGINNER クリアタイプ,BEGINNER DJ LEVEL,最終プレー日時"
dummy = '0,0,0,0,---,NO PLAY,---,'
clear = ('FAILED','ASSIST CLEAR','EASY CLEAR','CLEAR','HARD CLEAR','EX HARD CLEAR','FULLCOMBO CLEAR')

#dat = open(sys.argv[1]).readlines()[0]
dat = open('bpim_sample.txt').readlines()[0]
#dat = sys.argv[1]
all = json.loads(dat)

out = open('out.csv', 'w')
out.write(header+'\n')

d = datetime.now()
date_str = f"{d.year}/{d.month}/{d.day} {d.hour}:{d.minute}"

def write_one_song(out, song):
    if song['difficulty'] == 'hyper': # レベルを全部12とする都合上、灰11の譜面をここで弾く
        if song['title'] not in ('gigadelic', 'Innocent Walls'):
            return
    out.write(f"-,{song['title']},-,-,1,")
    out.write(dummy+dummy) # beginner, normal
    if song['difficulty'] == 'hyper':
        out.write(f"12,{song['score']},1,1,1,{clear[song['clear']]},A,{dummy}{dummy}")
    elif song['difficulty'] == 'another':
        out.write(f"{dummy}12,{song['score']},1,1,1,{clear[song['clear']]},A,{dummy}")
    else:
        out.write(f"{dummy}{dummy}12,{song['score']},1,1,1,{clear[song['clear']]},A,")
    out.write(date_str+'\n')


for song in all:
    write_one_song(out,song)