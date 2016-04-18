# -*- coding: utf-8 -*-
## for LOL実験 Histgram
from __future__ import division
import pandas as pd
import numpy as np
from datetime import datetime as dt
import os.path     # ファイルパス用
import glob    # 指定フォルダ内のファイルを取得
import sys
import matplotlib.pyplot as plt

print("##### HistGen forLoL:Start")

# const
match1=dt.strptime("2016-02-12 14:22:00",'%Y-%m-%d %H:%M:%S')
match2=dt.strptime("2016-02-12 15:33:00",'%Y-%m-%d %H:%M:%S')
match3=dt.strptime("2016-02-12 16:44:00",'%Y-%m-%d %H:%M:%S')

#指定フォルダ一括処理
target_path="/Users/jins/Downloads/hist/"
files= glob.glob(target_path + '*.csv')
for file in files:
    fname = file
    # 処理済のファイルが存在する場合スキップ
    if os.path.exists(fname.replace(".csv","_fixed.csv")): continue
    if os.path.exists(fname.replace(".csv","_fixed.csv")): continue
    if "_fixed.csv" in fname: continue

    # ファイル読み込み
    print("processing:%s" % fname)
    df=pd.read_csv(file,header=0,index_col=None,delimiter=',',parse_dates=[9])

    # ファイル名の3文字目から試合No抽出
    match_no=os.path.basename(fname)[2]

    # 試合開始時間セット
    if match_no=="1":ttime=match1
    elif match_no=="2":ttime=match2
    elif match_no=="3":ttime=match3

    # 試合開始以降のデータを抽出
    t=[x for x in df['time'] if x>=ttime]
    df2=df.iloc[(len(df)-len(t)):,:]

    # 不要データ削除
    del df,t

    # CZoneRT = (focus+calm)/2
    cz=[(x+y)/2.0 for x,y in zip(df2[u'focus'],df2[u'calm'])]

    # ヒストグラム生成:CZoneRT'
    fig1 = plt.figure(1)
    ax = fig1.add_subplot(1,1,1)
    ax.hist(cz, bins=16, range=(np.round(np.min(cz)), np.round(np.max(cz))))
    ax.set_title(os.path.basename(fname)[:3]+"_CZone_new", size=16)
    ax.set_xlabel('Score', size=14)
    ax.set_ylabel('Frequency', size=14)
    ax.text(np.round(np.min(cz)), 2000, r'''
        med=%.1f
        Std=%.2f''' % (np.median(cz),np.std(cz)))
    ax.grid(True)
    fig1.tight_layout
    plt.savefig(fname.replace(".csv","_CZone_new.png"))

    # ヒストグラム生成:roll
    fig2=plt.figure(2)
    ax1=fig2.add_subplot(2,3,1)
    ax1.hist(df2['roll'].values, bins=16, range=(np.round(np.min(df2['roll'])), np.round(np.max(df2['roll']))))
    ax1.set_title(os.path.basename(fname)[:3]+"_roll",size=16)
    ax1.set_xlabel('Score', size=14)
    ax1.set_ylabel('Frequency', size=14)
    ax1.text(np.round(np.min(df2['roll'])), 2000, r'''
        med=%.1f
        Std=%.2f''' % (np.median(df2['roll']),np.std(df2['roll'])))
    ax1.grid(True)
##    fig2.tight_layout
##    plt.savefig(fname.replace(".csv","_roll.png"))

    # ヒストグラム生成:calibRoll
    ax2=fig2.add_subplot(2,3,4)
    ax2.hist(df2['calibRoll'].values, bins=16, range=(np.round(np.min(df2['calibRoll'])), np.round(np.max(df2['calibRoll']))))
    ax2.set_title(os.path.basename(fname)[:3]+"_calibRoll",size=16)
    ax2.set_xlabel('Score', size=14)
    ax2.set_ylabel('Frequency', size=14)
    ax2.text(np.round(np.min(df2['calibRoll'])), 2000, r'''
        med=%.1f
        Std=%.2f''' % (np.median(df2['calibRoll']),np.std(df2['calibRoll'])))
    ax2.grid(True)

    # ヒストグラム生成:pitch
    ax3=fig2.add_subplot(2,3,2)
    ax3.hist(df2['pitch'].values, bins=16, range=(np.round(np.min(df2['pitch'])), np.round(np.max(df2['pitch']))))
    ax3.set_title(os.path.basename(fname)[:3]+"_pitch",size=16)
    ax3.set_xlabel('Score', size=14)
    ax3.set_ylabel('Frequency', size=14)
    ax3.text(np.round(np.min(df2['pitch'])), 2000, r'''
        med=%.1f
        Std=%.2f''' % (np.median(df2['pitch']),np.std(df2['pitch'])))
    ax3.grid(True)

    # ヒストグラム生成:calibPitch
    ax4=fig2.add_subplot(2,3,5)
    ax4.hist(df2['calibPitch'].values, bins=16, range=(np.round(np.min(df2['calibPitch'])), np.round(np.max(df2['calibPitch']))))
    ax4.set_title(os.path.basename(fname)[:3]+"_calibPitch",size=16)
    ax4.set_xlabel('Score', size=14)
    ax4.set_ylabel('Frequency', size=14)
    ax4.text(np.round(np.min(df2['calibPitch'])), 2000, r'''
        med=%.1f
        Std=%.2f''' % (np.median(df2['calibPitch']),np.std(df2['calibPitch'])))
    ax4.grid(True)

    # ヒストグラム生成:yaw
    ax5=fig2.add_subplot(2,3,3)
    ax5.hist(df2['yaw'].values, bins=16, range=(np.round(np.min(df2['yaw'])), np.round(np.max(df2['yaw']))))
    ax5.set_title(os.path.basename(fname)[:3]+"_yaw",size=16)
    ax5.set_xlabel('Score', size=14)
    ax5.set_ylabel('Frequency', size=14)
    ax5.text(np.round(np.min(df2['yaw'])), 2000, r'''
        med=%.1f
        Std=%.2f''' % (np.median(df2['yaw']),np.std(df2['yaw'])))
    ax5.grid(True)

    # ヒストグラム生成:calibYaw
    ax6=fig2.add_subplot(2,3,6)
    ax6.hist(df2['calibYaw'].values, bins=16, range=(np.round(np.min(df2['calibYaw'])), np.round(np.max(df2['calibYaw']))))
    ax6.set_title(os.path.basename(fname)[:3]+"_calibYaw",size=16)
    ax6.set_xlabel('Score', size=14)
    ax6.set_ylabel('Frequency', size=14)
    ax6.text(np.round(np.min(df2['calibYaw'])), 2000, r'''
        med=%.1f
        Std=%.2f''' % (np.median(df2['calibYaw']),np.std(df2['calibYaw'])))
    ax6.grid(True)

    #figManager = plt.get_current_fig_manager()
    #figManager.window.showMaximized()
    fig2.tight_layout
    plt.savefig(fname.replace(".csv","_Euler.png"))
    plt.show()
    #figManager.window.close()
    #del fig1,fig2,figManager
    plt.close()
    plt.clf()

    # CSV出力
    out=pd.concat([df2['time'],df2['blinkSpeed'],df2['blinkStrength'],df2['roll'],df2['pitch'], df2['yaw'], \
                    df2['accX'],df2['accY'],df2['accZ'],df2['calibRoll'],df2['calibPitch'],df2['calibYaw'], \
                    df2['calibAccX'],df2['calibAccY'],df2['calibAccZ'],df2['CZoneRT'],pd.DataFrame(cz),df2['focus'],df2['calm'],#, \
                    df2['posture'],df2['param1'],df2['parama2'],df2['param3'],df2['param4'],df2['param5'], \
                    df2['leaveAlone'],df2['walking'],df2['isWalking']],ignore_index=True,axis=1, join_axes=[df2.index])
    out.columns=['time','blinkSpeed','blinkStrength','roll','pitch','yaw','accX','accY','accZ','calibRoll', \
                'calibPitch','calibYaw','calibAccX','calibAccY','calibAccZ','CZoneRT','CZoneRT_new','focus', \
                'calm','posture','param1','parama2','param3','param4','param5','leaveAlone','walking','isWalking']
    out.to_csv(fname.replace(".csv","_fixed.csv"), header=True,encoding='shift-jis')

print("##### forLoL HistGen:End")
