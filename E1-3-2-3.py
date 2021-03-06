﻿# -*- coding: utf-8 -*-
"""
新北市公共自行車即時資訊主要欄位說明： sno：站點代號、 sna：場站名稱(中文)、 tot：場站總停車格、 
sbi：場站目前車輛數量、 sarea：場站區域(中文)、 mday：資料更新時間、 lat：緯度、 lng：經度、 
ar：地址(中文)、 sareaen：場站區域(英文)、 snaen：場站名稱(英文)、 aren：地址(英文)、 
bemp：空位數量、 act：全站禁用狀態 
"""
import json
with open("E1-3-2-3-input.json",encoding = 'utf8') as file:
    data = json.load(file)
    for item in data:
        print([item['sno'], item['sna'],item['tot']])
#把python轉換成json，上面的print就是你要怎麼呈現你的資料，後面的item就是你要呈現的是哪一項title的資料
