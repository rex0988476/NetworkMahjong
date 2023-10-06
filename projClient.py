# import區
from glob import glob
import re
import pygame
import random
import os
from datetime import datetime
import sys
import socket
import time
import threading
from random import choice
from enum import Enum
#import projLib
# 全域變數區

# 基本設定
WIDTH = 1280  # 寬
HEIGHT = 720  # 高
FPS = 60
MAHJONG_WIDTH = 51
MAHJONG_HEIGHT = 68
SMALL_MAHJONG_WIDTH = 36
SMALL_MAHJONG_HEIGHT = 48
MANAGER_MODE = 0  # 自訂模式
BACK_OR_FRONT = True
if MANAGER_MODE == 1:
    BACK_OR_FRONT = False

# 顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 205, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GRAY = (88, 88, 88)
BROWN = (112, 66, 20)
INACTIVE_WHITE = (150, 150, 150)
USERID_ERROR = 0  # 登入偵錯訊息
CREATE_SUCCESS = 0  # 登入偵錯訊息
#遊戲初始化 and 創建視窗
pygame.init()  # 初始化
pygame.mixer.init()  # 初始化音效模組
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 傳入元組,表示畫面高度跟寬度
pygame.display.set_caption("網路程式設計專題")  # 設定視窗名稱
clock = pygame.time.Clock()

#載入音樂
click_sound = pygame.mixer.Sound(os.path.join("data","sound","click.wav"))
pygame.mixer.music.load(os.path.join("data","sound","bgm.ogg"))
pygame.mixer.music.set_volume(0.2)
#Man1_img = pygame.transform.scale(Man1_img, (60, 80))
#background_img = pygame.image.load(os.path.join("data","img","bg.png")).convert()
# .set_colorkey(BLACK)

# 無圖片物件的圖片
null_img = pygame.image.load(os.path.join(
    "data", "img", "null_img.png")).convert()

# 圖片
shadow_img_name_list = ["shadow1.png", "shadow2.png", "shadow3.png", "shadow4.png", "shadow5.png", "shadow6.png", "shadow7.png", "shadow8.png", "shadow9.png", "shadow10.png",
                        "shadow11.png", "shadow12.png", "shadow13.png", "shadow14.png", "shadow15.png", "shadow16.png", "shadow17.png", "shadow18.png", "shadow19.png", "shadow20.png", ]
i = random.randint(0, 19)

shadow_img = pygame.image.load(os.path.join(
    "data", "img", shadow_img_name_list[i])).convert()
shadow_img.set_colorkey(WHITE)

w = pygame.image.load(os.path.join(
    "data", "img", "waiting.png")).convert()
w1 = pygame.image.load(os.path.join(
    "data", "img", "wait_1.png")).convert()
w2 = pygame.image.load(os.path.join(
    "data", "img", "wait_2.png")).convert()
w3 = pygame.image.load(os.path.join(
    "data", "img", "wait_3.png")).convert()

wait_people_img_list = [w, w1, w2, w3]

ron_effect_img = pygame.image.load(os.path.join(
    "data", "img", "ron_effect.png")).convert()
ron_effect_img.set_colorkey(WHITE)
tsumo_effect_img = pygame.image.load(os.path.join(
    "data", "img", "tsumo_effect.png")).convert()
tsumo_effect_img.set_colorkey(BLACK)


login_img = pygame.image.load(os.path.join(
    "data", "img", "login.png")).convert()
login_init_img = pygame.image.load(os.path.join(
    "data", "img", "login_init.png")).convert()
register_img = pygame.image.load(os.path.join(
    "data", "img", "register.png")).convert()
single_mode_img = pygame.image.load(os.path.join(
    "data", "img", "single_mode.png")).convert()
multi_mode_img = pygame.image.load(os.path.join(
    "data", "img", "multi_mode.png")).convert()
end_img = pygame.image.load(os.path.join(
    "data", "img", "end.png")).convert()
chi_img = pygame.image.load(os.path.join(
    "data", "img", "chi.png")).convert()
pong_img = pygame.image.load(os.path.join(
    "data", "img", "pong.png")).convert()
kong_img = pygame.image.load(os.path.join(
    "data", "img", "kong.png")).convert()
ron_img = pygame.image.load(os.path.join(
    "data", "img", "ron.png")).convert()
tsumo_img = pygame.image.load(os.path.join(
    "data", "img", "tsumo.png")).convert()
cancel_img = pygame.image.load(os.path.join(
    "data", "img", "cancel.png")).convert()
vice_dews_choice_bg_img = pygame.image.load(os.path.join(
    "data", "img", "vice_dews_choice_bg.png")).convert()
end_background_img = pygame.image.load(os.path.join(
    "data", "img", "background_end.png")).convert()
background_img = pygame.image.load(os.path.join(
    "data", "img", "background_init.png")).convert()
# 麻將圖片
# 下
Man1_img = pygame.image.load(os.path.join("data", "img", "Man1.png")).convert()
Man2_img = pygame.image.load(os.path.join("data", "img", "Man2.png")).convert()
Man3_img = pygame.image.load(os.path.join("data", "img", "Man3.png")).convert()
Man4_img = pygame.image.load(os.path.join("data", "img", "Man4.png")).convert()
Man5_img = pygame.image.load(os.path.join("data", "img", "Man5.png")).convert()
Man6_img = pygame.image.load(os.path.join("data", "img", "Man6.png")).convert()
Man7_img = pygame.image.load(os.path.join("data", "img", "Man7.png")).convert()
Man8_img = pygame.image.load(os.path.join("data", "img", "Man8.png")).convert()
Man9_img = pygame.image.load(os.path.join("data", "img", "Man9.png")).convert()

Chun_img = pygame.image.load(os.path.join("data", "img", "Chun.png")).convert()
Hatsu_img = pygame.image.load(os.path.join(
    "data", "img", "Hatsu.png")).convert()
Haku_img = pygame.image.load(os.path.join("data", "img", "Haku.png")).convert()
Ton_img = pygame.image.load(os.path.join("data", "img", "Ton.png")).convert()
Nan_img = pygame.image.load(os.path.join("data", "img", "Nan.png")).convert()
Shaa_img = pygame.image.load(os.path.join("data", "img", "Shaa.png")).convert()
Pei_img = pygame.image.load(os.path.join("data", "img", "Pei.png")).convert()

Pin1_img = pygame.image.load(os.path.join("data", "img", "Pin1.png")).convert()
Pin2_img = pygame.image.load(os.path.join("data", "img", "Pin2.png")).convert()
Pin3_img = pygame.image.load(os.path.join("data", "img", "Pin3.png")).convert()
Pin4_img = pygame.image.load(os.path.join("data", "img", "Pin4.png")).convert()
Pin5_img = pygame.image.load(os.path.join("data", "img", "Pin5.png")).convert()
Pin6_img = pygame.image.load(os.path.join("data", "img", "Pin6.png")).convert()
Pin7_img = pygame.image.load(os.path.join("data", "img", "Pin7.png")).convert()
Pin8_img = pygame.image.load(os.path.join("data", "img", "Pin8.png")).convert()
Pin9_img = pygame.image.load(os.path.join("data", "img", "Pin9.png")).convert()

Sou1_img = pygame.image.load(os.path.join("data", "img", "Sou1.png")).convert()
Sou2_img = pygame.image.load(os.path.join("data", "img", "Sou2.png")).convert()
Sou3_img = pygame.image.load(os.path.join("data", "img", "Sou3.png")).convert()
Sou4_img = pygame.image.load(os.path.join("data", "img", "Sou4.png")).convert()
Sou5_img = pygame.image.load(os.path.join("data", "img", "Sou5.png")).convert()
Sou6_img = pygame.image.load(os.path.join("data", "img", "Sou6.png")).convert()
Sou7_img = pygame.image.load(os.path.join("data", "img", "Sou7.png")).convert()
Sou8_img = pygame.image.load(os.path.join("data", "img", "Sou8.png")).convert()
Sou9_img = pygame.image.load(os.path.join("data", "img", "Sou9.png")).convert()

Man5_red_img = pygame.image.load(os.path.join(
    "data", "img", "Man5_red.png")).convert()
Pin5_red_img = pygame.image.load(os.path.join(
    "data", "img", "Pin5_red.png")).convert()
Sou5_red_img = pygame.image.load(os.path.join(
    "data", "img", "Sou5_red.png")).convert()

small_Man1_img = pygame.image.load(os.path.join(
    "data", "img", "small_Man1.png")).convert()
small_Man2_img = pygame.image.load(os.path.join(
    "data", "img", "small_Man2.png")).convert()
small_Man3_img = pygame.image.load(os.path.join(
    "data", "img", "small_Man3.png")).convert()
small_Man4_img = pygame.image.load(os.path.join(
    "data", "img", "small_Man4.png")).convert()
small_Man5_img = pygame.image.load(os.path.join(
    "data", "img", "small_Man5.png")).convert()
small_Man6_img = pygame.image.load(os.path.join(
    "data", "img", "small_Man6.png")).convert()
small_Man7_img = pygame.image.load(os.path.join(
    "data", "img", "small_Man7.png")).convert()
small_Man8_img = pygame.image.load(os.path.join(
    "data", "img", "small_Man8.png")).convert()
small_Man9_img = pygame.image.load(os.path.join(
    "data", "img", "small_Man9.png")).convert()

small_Chun_img = pygame.image.load(os.path.join(
    "data", "img", "small_Chun.png")).convert()
small_Hatsu_img = pygame.image.load(os.path.join(
    "data", "img", "small_Hatsu.png")).convert()
small_Haku_img = pygame.image.load(os.path.join(
    "data", "img", "small_Haku.png")).convert()
small_Ton_img = pygame.image.load(os.path.join(
    "data", "img", "small_Ton.png")).convert()
small_Nan_img = pygame.image.load(os.path.join(
    "data", "img", "small_Nan.png")).convert()
small_Shaa_img = pygame.image.load(os.path.join(
    "data", "img", "small_Shaa.png")).convert()
small_Pei_img = pygame.image.load(os.path.join(
    "data", "img", "small_Pei.png")).convert()

small_Pin1_img = pygame.image.load(os.path.join(
    "data", "img", "small_Pin1.png")).convert()
small_Pin2_img = pygame.image.load(os.path.join(
    "data", "img", "small_Pin2.png")).convert()
small_Pin3_img = pygame.image.load(os.path.join(
    "data", "img", "small_Pin3.png")).convert()
small_Pin4_img = pygame.image.load(os.path.join(
    "data", "img", "small_Pin4.png")).convert()
small_Pin5_img = pygame.image.load(os.path.join(
    "data", "img", "small_Pin5.png")).convert()
small_Pin6_img = pygame.image.load(os.path.join(
    "data", "img", "small_Pin6.png")).convert()
small_Pin7_img = pygame.image.load(os.path.join(
    "data", "img", "small_Pin7.png")).convert()
small_Pin8_img = pygame.image.load(os.path.join(
    "data", "img", "small_Pin8.png")).convert()
small_Pin9_img = pygame.image.load(os.path.join(
    "data", "img", "small_Pin9.png")).convert()

small_Sou1_img = pygame.image.load(os.path.join(
    "data", "img", "small_Sou1.png")).convert()
small_Sou2_img = pygame.image.load(os.path.join(
    "data", "img", "small_Sou2.png")).convert()
small_Sou3_img = pygame.image.load(os.path.join(
    "data", "img", "small_Sou3.png")).convert()
small_Sou4_img = pygame.image.load(os.path.join(
    "data", "img", "small_Sou4.png")).convert()
small_Sou5_img = pygame.image.load(os.path.join(
    "data", "img", "small_Sou5.png")).convert()
small_Sou6_img = pygame.image.load(os.path.join(
    "data", "img", "small_Sou6.png")).convert()
small_Sou7_img = pygame.image.load(os.path.join(
    "data", "img", "small_Sou7.png")).convert()
small_Sou8_img = pygame.image.load(os.path.join(
    "data", "img", "small_Sou8.png")).convert()
small_Sou9_img = pygame.image.load(os.path.join(
    "data", "img", "small_Sou9.png")).convert()

small_Man5_red_img = pygame.image.load(os.path.join(
    "data", "img", "small_Man5_red.png")).convert()
small_Pin5_red_img = pygame.image.load(os.path.join(
    "data", "img", "small_Pin5_red.png")).convert()
small_Sou5_red_img = pygame.image.load(os.path.join(
    "data", "img", "small_Sou5_red.png")).convert()
# 右
small_right_Man1_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Man1.png")).convert()
small_right_Man2_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Man2.png")).convert()
small_right_Man3_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Man3.png")).convert()
small_right_Man4_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Man4.png")).convert()
small_right_Man5_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Man5.png")).convert()
small_right_Man6_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Man6.png")).convert()
small_right_Man7_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Man7.png")).convert()
small_right_Man8_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Man8.png")).convert()
small_right_Man9_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Man9.png")).convert()

small_right_Chun_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Chun.png")).convert()
small_right_Hatsu_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Hatsu.png")).convert()
small_right_Haku_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Haku.png")).convert()
small_right_Ton_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Ton.png")).convert()
small_right_Nan_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Nan.png")).convert()
small_right_Shaa_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Shaa.png")).convert()
small_right_Pei_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Pei.png")).convert()

small_right_Pin1_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Pin1.png")).convert()
small_right_Pin2_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Pin2.png")).convert()
small_right_Pin3_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Pin3.png")).convert()
small_right_Pin4_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Pin4.png")).convert()
small_right_Pin5_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Pin5.png")).convert()
small_right_Pin6_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Pin6.png")).convert()
small_right_Pin7_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Pin7.png")).convert()
small_right_Pin8_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Pin8.png")).convert()
small_right_Pin9_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Pin9.png")).convert()

small_right_Sou1_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Sou1.png")).convert()
small_right_Sou2_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Sou2.png")).convert()
small_right_Sou3_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Sou3.png")).convert()
small_right_Sou4_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Sou4.png")).convert()
small_right_Sou5_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Sou5.png")).convert()
small_right_Sou6_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Sou6.png")).convert()
small_right_Sou7_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Sou7.png")).convert()
small_right_Sou8_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Sou8.png")).convert()
small_right_Sou9_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Sou9.png")).convert()

small_right_Man5_red_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Man5_red.png")).convert()
small_right_Pin5_red_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Pin5_red.png")).convert()
small_right_Sou5_red_img = pygame.image.load(os.path.join(
    "data", "img", "small_right_Sou5_red.png")).convert()

# 上
small_up_Man1_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Man1.png")).convert()
small_up_Man2_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Man2.png")).convert()
small_up_Man3_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Man3.png")).convert()
small_up_Man4_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Man4.png")).convert()
small_up_Man5_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Man5.png")).convert()
small_up_Man6_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Man6.png")).convert()
small_up_Man7_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Man7.png")).convert()
small_up_Man8_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Man8.png")).convert()
small_up_Man9_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Man9.png")).convert()

small_up_Chun_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Chun.png")).convert()
small_up_Hatsu_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Hatsu.png")).convert()
small_up_Haku_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Haku.png")).convert()
small_up_Ton_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Ton.png")).convert()
small_up_Nan_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Nan.png")).convert()
small_up_Shaa_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Shaa.png")).convert()
small_up_Pei_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Pei.png")).convert()

small_up_Pin1_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Pin1.png")).convert()
small_up_Pin2_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Pin2.png")).convert()
small_up_Pin3_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Pin3.png")).convert()
small_up_Pin4_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Pin4.png")).convert()
small_up_Pin5_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Pin5.png")).convert()
small_up_Pin6_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Pin6.png")).convert()
small_up_Pin7_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Pin7.png")).convert()
small_up_Pin8_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Pin8.png")).convert()
small_up_Pin9_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Pin9.png")).convert()

small_up_Sou1_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Sou1.png")).convert()
small_up_Sou2_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Sou2.png")).convert()
small_up_Sou3_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Sou3.png")).convert()
small_up_Sou4_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Sou4.png")).convert()
small_up_Sou5_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Sou5.png")).convert()
small_up_Sou6_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Sou6.png")).convert()
small_up_Sou7_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Sou7.png")).convert()
small_up_Sou8_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Sou8.png")).convert()
small_up_Sou9_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Sou9.png")).convert()

small_up_Man5_red_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Man5_red.png")).convert()
small_up_Pin5_red_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Pin5_red.png")).convert()
small_up_Sou5_red_img = pygame.image.load(os.path.join(
    "data", "img", "small_up_Sou5_red.png")).convert()

# 左
small_left_Man1_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Man1.png")).convert()
small_left_Man2_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Man2.png")).convert()
small_left_Man3_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Man3.png")).convert()
small_left_Man4_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Man4.png")).convert()
small_left_Man5_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Man5.png")).convert()
small_left_Man6_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Man6.png")).convert()
small_left_Man7_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Man7.png")).convert()
small_left_Man8_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Man8.png")).convert()
small_left_Man9_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Man9.png")).convert()

small_left_Chun_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Chun.png")).convert()
small_left_Hatsu_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Hatsu.png")).convert()
small_left_Haku_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Haku.png")).convert()
small_left_Ton_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Ton.png")).convert()
small_left_Nan_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Nan.png")).convert()
small_left_Shaa_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Shaa.png")).convert()
small_left_Pei_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Pei.png")).convert()

small_left_Pin1_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Pin1.png")).convert()
small_left_Pin2_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Pin2.png")).convert()
small_left_Pin3_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Pin3.png")).convert()
small_left_Pin4_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Pin4.png")).convert()
small_left_Pin5_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Pin5.png")).convert()
small_left_Pin6_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Pin6.png")).convert()
small_left_Pin7_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Pin7.png")).convert()
small_left_Pin8_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Pin8.png")).convert()
small_left_Pin9_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Pin9.png")).convert()

small_left_Sou1_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Sou1.png")).convert()
small_left_Sou2_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Sou2.png")).convert()
small_left_Sou3_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Sou3.png")).convert()
small_left_Sou4_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Sou4.png")).convert()
small_left_Sou5_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Sou5.png")).convert()
small_left_Sou6_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Sou6.png")).convert()
small_left_Sou7_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Sou7.png")).convert()
small_left_Sou8_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Sou8.png")).convert()
small_left_Sou9_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Sou9.png")).convert()

small_left_Man5_red_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Man5_red.png")).convert()
small_left_Pin5_red_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Pin5_red.png")).convert()
small_left_Sou5_red_img = pygame.image.load(os.path.join(
    "data", "img", "small_left_Sou5_red.png")).convert()


back_img = pygame.image.load(os.path.join(
    "data", "img", "back.png")).convert()
back_right_img = pygame.image.load(os.path.join(
    "data", "img", "back_right.png")).convert()
back_up_img = pygame.image.load(os.path.join(
    "data", "img", "back_up.png")).convert()
back_left_img = pygame.image.load(os.path.join(
    "data", "img", "back_left.png")).convert()

# icon
icon_img = pygame.image.load(os.path.join("data", "img", "icon.ico")).convert()
icon_img.set_colorkey(BLACK)
pygame.display.set_icon(icon_img)  # 設定視窗icon

# 載入音樂
VOLUME = 50
#success_sound = pygame.mixer.Sound(os.path.join("data","sound","success.ogg"))
# success_sound.set_volume(VOLUME/100)#調整音量大小,介於1~0之間
#blue_sound = pygame.mixer.Sound(os.path.join("data","sound","blue.ogg"))
# blue_sound.set_volume(VOLUME/100)
# pygame.mixer.music.load(os.path.join("sound","background.ogg"))


#引入字體pygame.font.Font(None, size)
#font_name = pygame.font.match_font('arial')

# 字體全域變數
font_name = None
chinese_font_name = os.path.join("data", "font.ttf")

# 函式區


# pygame相關函式

def draw_text(surf, text, size, color, center_x, center_y):  # 將文字寫到畫面上
    font = pygame.font.Font(font_name, size)  # 文字物件,(字體,文字大小)
    # 渲染,(要渲染的文字,是(True)否(False)要用反鋸齒(使字體看起來比較滑順),文字顏色)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()  # 定位
    text_rect.centerx = center_x
    text_rect.centery = center_y
    surf.blit(text_surface, text_rect)


def draw_text_background(surf, texts, size, color, x, y):  # 將多行(列表)文字寫到畫面上
    font = pygame.font.Font(font_name, size)  # 文字物件,(字體,文字大小)
    # 渲染,(要渲染的文字,是(True)否(False)要用反鋸齒(使字體看起來比較滑順),文字顏色)
    text_surface = font.render(texts, True, color)
    text_rect = text_surface.get_rect()  # 定位
    text_rect.x = x
    text_rect.y = y
    fill_rect = pygame.Rect(0, 0, text_rect.width + 20, text_rect.height + 20)
    pygame.draw.rect(screen, WHITE, fill_rect)
    surf.blit(text_surface, text_rect)


def draw_texts(surf, texts, size, color, x, y):  # 將多行(列表)文字寫到畫面上
    i = 0
    while i < len(texts):
        font = pygame.font.Font(font_name, size)  # 文字物件,(字體,文字大小)
        # 渲染,(要渲染的文字,是(True)否(False)要用反鋸齒(使字體看起來比較滑順),文字顏色)
        text_surface = font.render(texts[i], True, color)
        text_rect = text_surface.get_rect()  # 定位
        text_rect.x = x
        text_rect.y = y + (i*size)
        surf.blit(text_surface, text_rect)
        i += 1


def draw_chinese_texts(surf, texts, size, color, x, y):  # 將文字寫到畫面上(中文字體)
    i = 0
    while i < len(texts):
        font = pygame.font.Font(chinese_font_name, size)  # 文字物件,(字體,文字大小)
        # 渲染,(要渲染的文字,是(True)否(False)要用反鋸齒(使字體看起來比較滑順),文字顏色)
        text_surface = font.render(texts[i], True, color)
        text_rect = text_surface.get_rect()  # 定位
        text_rect.x = x
        text_rect.y = y + (i*size)
        surf.blit(text_surface, text_rect)
        i += 1


def draw_text_init(surf, text, size, color, x, y):
    # 傳入要寫的文字 以及 字體大小
    font = pygame.font.Font(font_name, size)
    # 渲染要寫的文字 中間的布林值為啟用antialias(看起來較滑順) 字體顏色
    text_surface = font.render(text, True, color)
    # 定位 get_rect：獲得影像位置
    text_rect = text_surface.get_rect()
    text_rect.left = x
    text_rect.centery = y
    surf.blit(text_surface, text_rect)


# 登入介面顯示
outline_rect_ID = pygame.Rect(440, 145, 400, 50)
outline_rect_PASSWORD = pygame.Rect(440, 245, 400, 50)
USERNAME = ""
PASSWORD_TEXT = ""
PASSWORD_TEXT_HIDE = ""


def draw_white(surf):
    fill_rect = pygame.Rect(0, 0, 1280, 720)
    # 畫血條 因為沒有第四個參數，會將所圍面積填滿
    pygame.draw.rect(surf, WHITE, fill_rect)


login_cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
login_cSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
login_cSocket.connect(('127.0.0.1', 8884))
thread_flag = 0
login_register_flag = 0  # -1 login, 1 register


def init():
    global outline_rect_ID
    global outline_rect_PASSWORD
    global USERID_ERROR
    global CREATE_SUCCESS
    draw_white(screen)
    draw_text(screen, 'login', 48, BLACK, 640, 80)
    screen.blit(login_init_img, (526, 400))
    screen.blit(register_img, (650, 400))

    pygame.draw.rect(screen, BLACK, outline_rect_ID, 2)
    pygame.draw.rect(screen, BLACK, outline_rect_PASSWORD, 2)

    draw_text_init(screen, USERNAME, 40, BLACK, 450, 170)
    draw_text_init(screen, PASSWORD_TEXT_HIDE, 40, BLACK, 450, 270)
    if USERID_ERROR == 1:
        draw_text(screen, 'account is not found', 30, RED, 640, 330)
    elif USERID_ERROR == 2:
        draw_text(screen, 'password error', 30, RED, 640, 330)
    elif USERID_ERROR == 4:
        draw_text(screen, 'Can not login again', 30, RED, 640, 330)
    if CREATE_SUCCESS == 1:
        draw_text(screen, 'creat accept', 30, GREEN, 640, 330)
    elif CREATE_SUCCESS == -1:
        draw_text(screen, 'Duplicate user name', 30, RED, 640, 330)


def time_transform(seconds):  # 時間轉換
    secs = seconds % 60
    mins = seconds//60
    hours = mins//60
    mins = mins - (hours*60)
    days = hours//24
    hours = hours - (days*24)
    timel = []
    timel.append(days)
    timel.append(hours)
    timel.append(mins)
    timel.append(secs)
    count = 0
    while True:
        if timel[0] == 0 and count < 2:
            del timel[0]
            count += 1
        else:
            break
    result = ""
    i = 0
    while i < len(timel):
        if timel[i] < 10:
            result += f"0{timel[i]}:"
        else:
            result += f"{timel[i]}:"
        i += 1
    rl = list(result)
    rl[len(rl)-1] = ""
    result = "".join(rl)
    return result


def addText(text):
    global TEXT_LIST
    TEXT_LIST.append(str(text))
    if len(TEXT_LIST) > 7:
        del TEXT_LIST[0]


# 遊戲流程函式

def shuffle():  # 洗牌, 之後要丟到server
    global REMAINING_MAHJONG_LIST
    global CARD_MOUNTAIN
    if MANAGER_MODE == 0:
        REMAINING_MAHJONG_LIST = ["Man1", "Man1", "Man1", "Man1", "Man2", "Man2", "Man2", "Man2", "Man3", "Man3", "Man3", "Man3", "Man4", "Man4", "Man4", "Man4", "Man5", "Man5", "Man5", "Man6", "Man6", "Man6", "Man6", "Man7", "Man7", "Man7", "Man7", "Man8", "Man8", "Man8", "Man8", "Man9", "Man9", "Man9", "Man9", "Pin1", "Pin1", "Pin1", "Pin1", "Pin2", "Pin2", "Pin2", "Pin2", "Pin3", "Pin3", "Pin3", "Pin3", "Pin4", "Pin4", "Pin4", "Pin4", "Pin5", "Pin5", "Pin5", "Pin6", "Pin6", "Pin6", "Pin6", "Pin7", "Pin7", "Pin7", "Pin7", "Pin8", "Pin8", "Pin8", "Pin8", "Pin9",
                                  "Pin9", "Pin9", "Pin9", "Sou1", "Sou1", "Sou1", "Sou1", "Sou2", "Sou2", "Sou2", "Sou2", "Sou3", "Sou3", "Sou3", "Sou3", "Sou4", "Sou4", "Sou4", "Sou4", "Sou5", "Sou5", "Sou5", "Sou6", "Sou6", "Sou6", "Sou6", "Sou7", "Sou7", "Sou7", "Sou7", "Sou8", "Sou8", "Sou8", "Sou8", "Sou9", "Sou9", "Sou9", "Sou9", "Ton", "Ton", "Ton", "Ton", "Nan", "Nan", "Nan", "Nan", "Shaa", "Shaa", "Shaa", "Shaa", "Pei", "Pei", "Pei", "Pei", "Chun", "Chun", "Chun", "Chun", "Haku", "Haku", "Haku", "Haku", "Hatsu", "Hatsu", "Hatsu", "Hatsu", "Man5_red", "Pin5_red", "Sou5_red"]

    while len(REMAINING_MAHJONG_LIST) > 0:
        rand_index = random.randint(0, len(REMAINING_MAHJONG_LIST)-1)
        CARD_MOUNTAIN.append(REMAINING_MAHJONG_LIST[rand_index])
        del REMAINING_MAHJONG_LIST[rand_index]


def start_deal(seed):
    i = 0
    while i < 52:
        if i < 48:
            if seed == 1:
                for one in range(4):
                    deal("down")
            elif seed == 2:
                for one in range(4):
                    deal("right")
            elif seed == 3:
                for one in range(4):
                    deal("up")
            elif seed == 4:
                for one in range(4):
                    deal("left")
            i += 4
        else:
            if seed == 1:
                deal("down")
            elif seed == 2:
                deal("right")
            elif seed == 3:
                deal("up")
            elif seed == 4:
                deal("left")
            i += 1
        seed += 1
        if seed > 4:
            seed = 1
    seed -= 1
    if seed == 0:
        seed = 4
    return seed


# jump
HAND_CARDS_STARTX = 260  # 最右邊手牌x座標
HAND_CARDS_STARTY = 640  # 最右邊手牌y座標
RIGHT_HAND_CARD_STARTX = 1080  # 最右邊手牌x座標 下家
RIGHT_HAND_CARD_STARTY = 560  # 最右邊手牌y座標 下家
UP_HAND_CARD_STARTX = 840  # 最右邊手牌x座標 對家
UP_HAND_CARD_STARTY = 20  # 最右邊手牌y座標 對家
LEFT_HAND_CARD_STARTX = 154  # 最右邊手牌x座標 上家
LEFT_HAND_CARD_STARTY = 128  # 最右邊手牌y座標 上家
DEAL_CARD = []
SMALL_DEAL_CARD = []


def multi_deal(site="", type=""):  # 發牌, type="","draw"
    global MAHJONG_BUTTON_LIST
    global play_multi_sprites
    global HAND_CARDS_LIST
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST
    #global hand_card_startx
    #global hand_card_starty
    global DEAL_CARD
    global SMALL_DEAL_CARD
    global CARD_MOUNTAIN

    if type == "init":
        HAND_CARDS_LIST = []
        i = 0
        while i < len(RIGHT_HAND_CARDS_LIST):
            RIGHT_HAND_CARDS_LIST[i][1].kill()
            del RIGHT_HAND_CARDS_LIST[i]
        i = 0
        while i < len(UP_HAND_CARDS_LIST):
            UP_HAND_CARDS_LIST[i][1].kill()
            del UP_HAND_CARDS_LIST[i]
        i = 0
        while i < len(LEFT_HAND_CARDS_LIST):
            LEFT_HAND_CARDS_LIST[i][1].kill()
            del LEFT_HAND_CARDS_LIST[i]
        RIGHT_HAND_CARDS_LIST = []
        UP_HAND_CARDS_LIST = []
        LEFT_HAND_CARDS_LIST = []
        i = 0
        while i < 13:
            # right
            y = RIGHT_HAND_CARD_STARTY - \
                (SMALL_MAHJONG_WIDTH) * len(RIGHT_HAND_CARDS_LIST)
            card = Small_Mahjong(
                "", RIGHT_HAND_CARD_STARTX, y, "right", BACK_OR_FRONT)
            card.in_hand_id = len(RIGHT_HAND_CARDS_LIST)
            print("RIGHT APPEND",card)
            RIGHT_HAND_CARDS_LIST.append([len(RIGHT_HAND_CARDS_LIST), card])
            
            play_multi_sprites.add(card)
            # up
            x = UP_HAND_CARD_STARTX - SMALL_MAHJONG_WIDTH * \
                len(UP_HAND_CARDS_LIST)
            card = Small_Mahjong(
                "", x, UP_HAND_CARD_STARTY, "up", BACK_OR_FRONT)
            card.in_hand_id = len(UP_HAND_CARDS_LIST)
            print("UP APPEND",card)
            UP_HAND_CARDS_LIST.append([len(UP_HAND_CARDS_LIST), card])
            play_multi_sprites.add(card)
            # left
            y = LEFT_HAND_CARD_STARTY + SMALL_MAHJONG_WIDTH * \
                len(LEFT_HAND_CARDS_LIST)
            card = Small_Mahjong(
                "", LEFT_HAND_CARD_STARTX, y, "left", BACK_OR_FRONT)
            card.in_hand_id = len(LEFT_HAND_CARDS_LIST)
            print("LEFT APPEND",card)
            LEFT_HAND_CARDS_LIST.append([len(LEFT_HAND_CARDS_LIST), card])
            play_multi_sprites.add(card)

            i += 1

        i = 0
        while i < 13:
            x = HAND_CARDS_STARTX + MAHJONG_WIDTH * len(HAND_CARDS_LIST)
            card = Mahjong(
                player.cards[i], x, HAND_CARDS_STARTY)
            card.in_hand_id = len(HAND_CARDS_LIST)
            HAND_CARDS_LIST.append([len(HAND_CARDS_LIST), card])
            MAHJONG_BUTTON_LIST.append(card)
            play_multi_sprites.add(card)
            i += 1
    else:
        if site == "down":
            x = HAND_CARDS_STARTX + MAHJONG_WIDTH * (len(HAND_CARDS_LIST)+1)
            DEAL_CARD = [len(HAND_CARDS_LIST), Mahjong(
                player.deal_card, x, HAND_CARDS_STARTY)]
            DEAL_CARD[1].in_hand_id = DEAL_CARD[0]
            play_multi_sprites.add(DEAL_CARD[1])  # 多人
            MAHJONG_BUTTON_LIST.append(DEAL_CARD[1])
        elif site == "right":
            y = RIGHT_HAND_CARD_STARTY - \
                (SMALL_MAHJONG_WIDTH) * (len(RIGHT_HAND_CARDS_LIST) + 1)
            SMALL_DEAL_CARD = [len(RIGHT_HAND_CARDS_LIST), Small_Mahjong(
                "", RIGHT_HAND_CARD_STARTX, y, site, BACK_OR_FRONT)]
            SMALL_DEAL_CARD[1].in_hand_id = SMALL_DEAL_CARD[0]
            play_multi_sprites.add(SMALL_DEAL_CARD[1])  # 多人
        elif site == "up":
            x = UP_HAND_CARD_STARTX - SMALL_MAHJONG_WIDTH * \
                (len(UP_HAND_CARDS_LIST) + 1)
            SMALL_DEAL_CARD = [len(UP_HAND_CARDS_LIST), Small_Mahjong(
                "", x, UP_HAND_CARD_STARTY, site, BACK_OR_FRONT)]
            SMALL_DEAL_CARD[1].in_hand_id = SMALL_DEAL_CARD[0]
            play_multi_sprites.add(SMALL_DEAL_CARD[1])  # 多人
        elif site == "left":
            y = LEFT_HAND_CARD_STARTY + SMALL_MAHJONG_WIDTH * \
                (len(LEFT_HAND_CARDS_LIST) + 1)
            SMALL_DEAL_CARD = [len(LEFT_HAND_CARDS_LIST), Small_Mahjong(
                "", LEFT_HAND_CARD_STARTX, y, site, BACK_OR_FRONT)]
            SMALL_DEAL_CARD[1].in_hand_id = SMALL_DEAL_CARD[0]
            play_multi_sprites.add(SMALL_DEAL_CARD[1])  # 多人


def deal(site, type=""):  # 發牌, type="","draw"
    global MAHJONG_BUTTON_LIST
    global play_single_sprites
    global play_multi_sprites
    global HAND_CARDS_LIST
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST
    #global hand_card_startx
    #global hand_card_starty
    global DEAL_CARD
    global SMALL_DEAL_CARD
    global CARD_MOUNTAIN

    if site == "down":
        x = HAND_CARDS_STARTX + MAHJONG_WIDTH * len(HAND_CARDS_LIST)
        if type == "draw":
            x = HAND_CARDS_STARTX + MAHJONG_WIDTH * (len(HAND_CARDS_LIST)+1)
            DEAL_CARD = [len(HAND_CARDS_LIST), Mahjong(
                CARD_MOUNTAIN[0], x, HAND_CARDS_STARTY)]
            DEAL_CARD[1].in_hand_id = DEAL_CARD[0]
        else:
            card = Mahjong(
                CARD_MOUNTAIN[0], x, HAND_CARDS_STARTY)
            card.in_hand_id = len(HAND_CARDS_LIST)
            HAND_CARDS_LIST.append([len(HAND_CARDS_LIST), card])

        #hand_card_startx += MAHJONG_WIDTH

    if site == "right":
        y = RIGHT_HAND_CARD_STARTY - \
            (SMALL_MAHJONG_WIDTH) * len(RIGHT_HAND_CARDS_LIST)
        if type == "draw":
            y = RIGHT_HAND_CARD_STARTY - \
                (SMALL_MAHJONG_WIDTH) * (len(RIGHT_HAND_CARDS_LIST) + 1)
            SMALL_DEAL_CARD = [len(RIGHT_HAND_CARDS_LIST), Small_Mahjong(
                CARD_MOUNTAIN[0], RIGHT_HAND_CARD_STARTX, y, site, BACK_OR_FRONT)]
            SMALL_DEAL_CARD[1].in_hand_id = SMALL_DEAL_CARD[0]
        else:
            card = Small_Mahjong(
                CARD_MOUNTAIN[0], RIGHT_HAND_CARD_STARTX, y, site, BACK_OR_FRONT)
            card.in_hand_id = len(RIGHT_HAND_CARDS_LIST)
            print("RIGHT APPEND",card)
            RIGHT_HAND_CARDS_LIST.append([len(RIGHT_HAND_CARDS_LIST), card])

    if site == "up":
        x = UP_HAND_CARD_STARTX - SMALL_MAHJONG_WIDTH * \
            len(UP_HAND_CARDS_LIST)
        if type == "draw":
            x = UP_HAND_CARD_STARTX - SMALL_MAHJONG_WIDTH * \
                (len(UP_HAND_CARDS_LIST) + 1)
            SMALL_DEAL_CARD = [len(UP_HAND_CARDS_LIST), Small_Mahjong(
                CARD_MOUNTAIN[0], x, UP_HAND_CARD_STARTY, site, BACK_OR_FRONT)]
            SMALL_DEAL_CARD[1].in_hand_id = SMALL_DEAL_CARD[0]
        else:
            card = Small_Mahjong(
                CARD_MOUNTAIN[0], x, UP_HAND_CARD_STARTY, site, BACK_OR_FRONT)
            card.in_hand_id = len(UP_HAND_CARDS_LIST)
            print("UP APPEND",card)
            UP_HAND_CARDS_LIST.append([len(UP_HAND_CARDS_LIST), card])

    if site == "left":
        y = LEFT_HAND_CARD_STARTY + SMALL_MAHJONG_WIDTH * \
            len(LEFT_HAND_CARDS_LIST)
        if type == "draw":
            y = LEFT_HAND_CARD_STARTY + SMALL_MAHJONG_WIDTH * \
                (len(LEFT_HAND_CARDS_LIST) + 1)
            SMALL_DEAL_CARD = [len(LEFT_HAND_CARDS_LIST), Small_Mahjong(
                CARD_MOUNTAIN[0], LEFT_HAND_CARD_STARTX, y, site, BACK_OR_FRONT)]
            SMALL_DEAL_CARD[1].in_hand_id = SMALL_DEAL_CARD[0]
        else:
            card = Small_Mahjong(
                CARD_MOUNTAIN[0], LEFT_HAND_CARD_STARTX, y, site, BACK_OR_FRONT)
            card.in_hand_id = len(LEFT_HAND_CARDS_LIST)
            print("LEFT APPEND",card)
            LEFT_HAND_CARDS_LIST.append([len(LEFT_HAND_CARDS_LIST), card])
    #
    if type == "draw":
        if site == "down":
            play_single_sprites.add(DEAL_CARD[1])  # 單人
            play_multi_sprites.add(DEAL_CARD[1])  # 多人
            MAHJONG_BUTTON_LIST.append(DEAL_CARD[1])
        else:
            play_single_sprites.add(SMALL_DEAL_CARD[1])  # 單人
            play_multi_sprites.add(SMALL_DEAL_CARD[1])  # 多人

    else:
        if site == "down":
            MAHJONG_BUTTON_LIST.append(card)
        play_single_sprites.add(card)  # 單人
        play_multi_sprites.add(card)  # 多人

    del CARD_MOUNTAIN[0]


def manager_define_process(seed=""):  # 自訂四家手牌 seed
    global HAND_CARDS_LIST
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST
    global play_single_sprites
    global play_multi_sprites
    global MAHJONG_BUTTON_LIST
    global REMAINING_MAHJONG_LIST
    global SEED
    REMAINING_MAHJONG_LIST = ["Man1", "Man1", "Man1", "Man1", "Man2", "Man2", "Man2", "Man2", "Man3", "Man3", "Man3", "Man3", "Man4", "Man4", "Man4", "Man4", "Man5", "Man5", "Man5", "Man6", "Man6", "Man6", "Man6", "Man7", "Man7", "Man7", "Man7", "Man8", "Man8", "Man8", "Man8", "Man9", "Man9", "Man9", "Man9", "Pin1", "Pin1", "Pin1", "Pin1", "Pin2", "Pin2", "Pin2", "Pin2", "Pin3", "Pin3", "Pin3", "Pin3", "Pin4", "Pin4", "Pin4", "Pin4", "Pin5", "Pin5", "Pin5", "Pin6", "Pin6", "Pin6", "Pin6", "Pin7", "Pin7", "Pin7", "Pin7", "Pin8", "Pin8", "Pin8", "Pin8", "Pin9",
                          "Pin9", "Pin9", "Pin9", "Sou1", "Sou1", "Sou1", "Sou1", "Sou2", "Sou2", "Sou2", "Sou2", "Sou3", "Sou3", "Sou3", "Sou3", "Sou4", "Sou4", "Sou4", "Sou4", "Sou5", "Sou5", "Sou5", "Sou6", "Sou6", "Sou6", "Sou6", "Sou7", "Sou7", "Sou7", "Sou7", "Sou8", "Sou8", "Sou8", "Sou8", "Sou9", "Sou9", "Sou9", "Sou9", "Ton", "Ton", "Ton", "Ton", "Nan", "Nan", "Nan", "Nan", "Shaa", "Shaa", "Shaa", "Shaa", "Pei", "Pei", "Pei", "Pei", "Chun", "Chun", "Chun", "Chun", "Haku", "Haku", "Haku", "Haku", "Hatsu", "Hatsu", "Hatsu", "Hatsu", "Man5_red", "Pin5_red", "Sou5_red"]

    if seed != "":
        SEED = seed
    else:
        SEED = 1
    HAND_CARDS_LIST = []
    RIGHT_HAND_CARDS_LIST = []
    UP_HAND_CARDS_LIST = []
    LEFT_HAND_CARDS_LIST = []
    hand_cards_list_ids = ["Man2", "Man2", "Man7", "Pin5", "Pin7", "Pin9",
                           "Sou1", "Sou3", "Sou5", "Sou7", "Sou8", "Sou9", "Hatsu"]  # 自訂區(13張麻將id)
    right_hand_cards_list_ids = ["Man2", "Man3", "Pin2", "Pin3", "Sou1", "Sou1",
                                 "Sou6", "Pin4", "Sou7", "Sou8", "Sou7", "Sou8", "Chun"]  # 自訂區(13張麻將id)
    up_hand_cards_list_ids = ["Man3", "Man5", "Man5", "Man6", "Man7", "Pin1",
                              "Pin1", "Pin7", "Pin8", "Sou4", "Sou8", "Man4", "Hatsu"]  # 自訂區(13張麻將id)
    left_hand_cards_list_ids = ["Man3", "Man9", "Man9", "Pin2", "Pin5", "Pin9",
                                "Sou3", "Sou6", "Man4", "Man5", "Pin3", "Pin4", "Shaa"]  # 自訂區(13張麻將id)
    i = 0
    while i < 13:
        # player
        x = HAND_CARDS_STARTX + MAHJONG_WIDTH * len(HAND_CARDS_LIST)
        card = Mahjong(hand_cards_list_ids[i], x, HAND_CARDS_STARTY)
        card.in_hand_id = i
        HAND_CARDS_LIST.append([i, card])

        MAHJONG_BUTTON_LIST.append(card)
        play_single_sprites.add(card)  # 單人
        play_multi_sprites.add(card)  # 多人
        REMAINING_MAHJONG_LIST.remove(hand_cards_list_ids[i])
        # right
        y = RIGHT_HAND_CARD_STARTY - \
            (SMALL_MAHJONG_WIDTH) * len(RIGHT_HAND_CARDS_LIST)
        card = Small_Mahjong(
            right_hand_cards_list_ids[i], RIGHT_HAND_CARD_STARTX, y, "right")
        card.in_hand_id = i
        print("RIGHT APPEND",card)
        RIGHT_HAND_CARDS_LIST.append([i, card])

        play_single_sprites.add(card)  # 單人
        play_multi_sprites.add(card)  # 多人
        REMAINING_MAHJONG_LIST.remove(right_hand_cards_list_ids[i])
        # up
        x = UP_HAND_CARD_STARTX - SMALL_MAHJONG_WIDTH * \
            len(UP_HAND_CARDS_LIST)
        card = Small_Mahjong(
            up_hand_cards_list_ids[i], x, UP_HAND_CARD_STARTY, "up")
        card.in_hand_id = i
        print("UP APPEND",card)
        UP_HAND_CARDS_LIST.append([i, card])

        play_single_sprites.add(card)  # 單人
        play_multi_sprites.add(card)  # 多人
        REMAINING_MAHJONG_LIST.remove(up_hand_cards_list_ids[i])
        # left
        y = LEFT_HAND_CARD_STARTY + SMALL_MAHJONG_WIDTH * \
            len(LEFT_HAND_CARDS_LIST)
        card = Small_Mahjong(
            left_hand_cards_list_ids[i], LEFT_HAND_CARD_STARTX, y, "left")
        card.in_hand_id = i
        print("LEFT APPEND",card)
        LEFT_HAND_CARDS_LIST.append([i, card])

        play_single_sprites.add(card)  # 單人
        play_multi_sprites.add(card)  # 多人
        REMAINING_MAHJONG_LIST.remove(left_hand_cards_list_ids[i])
        i += 1


def combine_card(site):  # 四家組牌
    global DEAL_CARD
    global SMALL_DEAL_CARD
    global HAND_CARDS_LIST
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST
    if site == "down":
        try:
            if DEAL_CARD[0] != -1:
                HAND_CARDS_LIST.append([DEAL_CARD[0], DEAL_CARD[1]])
                #DEAL_CARD[0] = -1
        except:
            print("can't combine_card down")
            time.sleep(100)
    elif site == "right":
        try:
            if SMALL_DEAL_CARD[0] != -1:
                print("RIGHT APPEND",SMALL_DEAL_CARD[1])
                RIGHT_HAND_CARDS_LIST.append(
                    [SMALL_DEAL_CARD[0], SMALL_DEAL_CARD[1]])
                #SMALL_DEAL_CARD[0] = -1
        except:
            print("can't combine_card right")
            time.sleep(100)
    elif site == "up":
        try:
            if SMALL_DEAL_CARD[0] != -1:
                print("UP APPEND",SMALL_DEAL_CARD[1])
                UP_HAND_CARDS_LIST.append(
                    [SMALL_DEAL_CARD[0], SMALL_DEAL_CARD[1]])
                #SMALL_DEAL_CARD[0] = -1
        except:
            print("can't combine_card up")
            time.sleep(100)
    elif site == "left":
        try:
            if SMALL_DEAL_CARD[0] != -1:
                print("LEFT APPEND",SMALL_DEAL_CARD[1])
                LEFT_HAND_CARDS_LIST.append(
                    [SMALL_DEAL_CARD[0], SMALL_DEAL_CARD[1]])
                #SMALL_DEAL_CARD[0] = -1
        except:
            print("can't combine_card left")
            time.sleep(100)


def multi_out_cards(site, out_card_id):  # 其他三家出牌
    global right_card_river
    global up_card_river
    global left_card_river
    global SMALL_DEAL_CARD
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST
    print(site, SMALL_DEAL_CARD, out_card_id)
    print("IN multi_out_cards")
    try:
        if SMALL_DEAL_CARD[0] == -1:
            if site == "right":
                right_card_river.add_card((out_card_id, "small_right"), "vert")
                try:
                    RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1][1].kill()
                    del RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1][1]
                except:
                    print("RIGHT_HAND_CARDS_LIST",RIGHT_HAND_CARDS_LIST)
                    time.sleep(100)
            if site == "up":
                up_card_river.add_card((out_card_id, "small_up"), "vert")
                try:
                    UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1][1].kill()
                    del UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1][1]
                except:
                    print("UP_HAND_CARDS_LIST",UP_HAND_CARDS_LIST)
                    time.sleep(100)
            if site == "left":
                left_card_river.add_card((out_card_id, "small_left"), "vert")
                try:
                    LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1][1].kill()
                    del LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1][1]
                except:
                    print("LEFT_HAND_CARDS_LIST",LEFT_HAND_CARDS_LIST)
                    time.sleep(100)
        else:
            if site == "right":
                right_card_river.add_card((out_card_id, "small_right"), "vert")
                SMALL_DEAL_CARD[0] = -1
                SMALL_DEAL_CARD[1].kill()
            if site == "up":
                up_card_river.add_card((out_card_id, "small_up"), "vert")
                SMALL_DEAL_CARD[0] = -1
                SMALL_DEAL_CARD[1].kill()
            if site == "left":
                left_card_river.add_card((out_card_id, "small_left"), "vert")
                SMALL_DEAL_CARD[0] = -1
                SMALL_DEAL_CARD[1].kill()
    except:
        if site == "right":
            right_card_river.add_card((out_card_id, "small_right"), "vert")
            try:
                RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1][1].kill()
                del RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1][1]
            except:
                print("RIGHT_HAND_CARDS_LIST",RIGHT_HAND_CARDS_LIST)
                time.sleep(100)
        if site == "up":
            up_card_river.add_card((out_card_id, "small_up"), "vert")
            try:
                UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1][1].kill()
                del UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1][1]
            except:
                print("UP_HAND_CARDS_LIST",UP_HAND_CARDS_LIST)
                time.sleep(100)
        if site == "left":
            left_card_river.add_card((out_card_id, "small_left"), "vert")
            try:
                LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1][1].kill()
                del LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1][1]
            except:
                print("LEFT_HAND_CARDS_LIST",LEFT_HAND_CARDS_LIST)
                time.sleep(100)


def can_win(site, draw):  # 判斷是否可以和牌

    # 計算順序為
    # 1. 先把對子抓出來，並將1萬到白發中全都餵過一遍
    # 2. 一萬刻先抓，沒刻抓123萬 順 以此類推
    # 3. 若餵到能聽牌的結果，存入listen，並繼續
    # 4. 當一組餵完之後，從剛剛抓出對子的下一個next_pairs 繼續尋找對子出來抓 並重複23
    # 5. 當y 也就是對子找到最後一組時 break
    # 6. 把listen轉成id傳回去
    hand_card_number_list = []
    hand_card_number_list_copy = []
    next_pairs = 0  # 下一個對
    score_eyes = 0  # 有沒有一組眼
    xtriplet = 0  # 順的輪次
    offset = 0  # 同一輪次 刻順的位移 刻在順前面
    fourteen = 0  # 判斷手牌是否全 -1
    temp = []
    list = []
    score = 0
    while True:
        if site == "down":
            hand_card_number_list = []
            for i in range(len(HAND_CARDS_LIST)):
                hand_card_number_list.append(
                    MAHJONG_SORT_TABLE_LIST.index(HAND_CARDS_LIST[i][1].id))
        if site == "right":
            hand_card_number_list = []
            for i in range(len(RIGHT_HAND_CARDS_LIST)):
                hand_card_number_list.append(
                    MAHJONG_SORT_TABLE_LIST.index(RIGHT_HAND_CARDS_LIST[i][1].id))
        if site == "up":
            hand_card_number_list = []
            for i in range(len(UP_HAND_CARDS_LIST)):
                hand_card_number_list.append(
                    MAHJONG_SORT_TABLE_LIST.index(UP_HAND_CARDS_LIST[i][1].id))
        if site == "left":
            hand_card_number_list = []
            for i in range(len(LEFT_HAND_CARDS_LIST)):
                hand_card_number_list.append(
                    MAHJONG_SORT_TABLE_LIST.index(LEFT_HAND_CARDS_LIST[i][1].id))
        hand_card_number_list.append(
            MAHJONG_SORT_TABLE_LIST.index(draw))
        hand_card_number_list.sort()

        xtriplet = 0  # 順的輪次
        offset = 0  # 同一輪次 刻順的位移 刻在順前面

        y_pair = next_pairs
        score_eyes = 0
        fourteen = 0
        hand_card_number_list_copy = hand_card_number_list
        temp = []
        list = []
        score = 0
        # 對子
        for xx in range(len(SEQUENCE)):
            # y_pair 確認內容是否符合
            while (y_pair in SEQUENCE[xx]):
                temp = [i for i, find in enumerate(
                    hand_card_number_list_copy) if find == y_pair]
                for z in range(len(temp)):
                    list.append(temp[z])
                y_pair = y_pair + 1
            if len(list) >= 2:
                hand_card_number_list_copy[list[0]] = -1
                hand_card_number_list_copy[list[1]] = -1
                score_eyes = score_eyes + 1
            if score_eyes >= 1:
                break
            else:
                # print("False")
                # return (False)
                pass
            list = []
        next_pairs = y_pair
        list = []
        # 刻子
        for x in range(len(SEQUENCE)):
            # y 確認內容是否符合
            for y1 in SEQUENCE[x]:
                temp = [i for i, find in enumerate(
                    hand_card_number_list_copy) if find == y1]

                for z in range(len(temp)):
                    list.append(temp[z])
            if len(list) == 3:
                hand_card_number_list_copy[list[0]] = -1
                hand_card_number_list_copy[list[1]] = -1
                hand_card_number_list_copy[list[2]] = -1
                score = score + 3
            elif len(list) == 4:
                hand_card_number_list_copy[list[0]] = -1
                hand_card_number_list_copy[list[1]] = -1
                hand_card_number_list_copy[list[3]] = -1
                score = score + 3
            else:
                pass
            list = []

            if xtriplet < 29:
                # 順子 跟刻子要同輪次
                if(x == 8 or x == 9 or x == 18 or x == 19 or x == 28 or x == 29):
                    offset = offset - 1
                else:
                    xtriplet = x + offset
                    #print(f"\n{xtriplet, x}\n")
                    #print("---" + str(xtriplet))
                    # y 確認內容是否符合
                    for z in range(3):
                        for y in range(len(TRIPLET[xtriplet])):
                            if TRIPLET[xtriplet][y] in hand_card_number_list_copy:
                                list.append(
                                    hand_card_number_list_copy.index(TRIPLET[xtriplet][y]))
                        if len(list) >= 3:
                            hand_card_number_list_copy[list[0]] = -1
                            hand_card_number_list_copy[list[1]] = -1
                            hand_card_number_list_copy[list[2]] = -1
                            score = score + 3
                        else:
                            pass
                        list = []
                    if (x == 2 or x == 3 or x == 12 or x == 13 or x == 22 or x == 23):
                        offset = offset + 1
                        for z in range(3):
                            for y in range(len(TRIPLET[xtriplet+1])):
                                if TRIPLET[xtriplet+1][y] in hand_card_number_list_copy:
                                    list.append(
                                        hand_card_number_list_copy.index(TRIPLET[xtriplet+1][y]))
                            if len(list) >= 3:
                                hand_card_number_list_copy[list[0]] = -1
                                hand_card_number_list_copy[list[1]] = -1
                                hand_card_number_list_copy[list[2]] = -1
                                score = score + 3
                            else:
                                pass
                            list = []

        for i in range(len(hand_card_number_list_copy)):
            if hand_card_number_list_copy[i] == -1:
                fourteen = fourteen + 1
        # print(f"{site}:{hand_card_number_list_copy}")
        # print(f"手牌能不能和：{fourteen}")
        # print(f"眼睛:{y_pair-1}\n")
        if fourteen == len(hand_card_number_list):
            print("\nyyyyyyyyyyyyy\n")
            return(True)
        if y_pair >= 37:
            break
    return(False)


def out_cards(site, is_have_deal_card):  # 其他三家出牌
    global right_card_river
    global up_card_river
    global left_card_river
    global SMALL_DEAL_CARD
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST
    click_sound.play()
    # hand_cards_len = 0
    if site == "right":
        if is_have_deal_card:
            card_index = algorithm("right", SMALL_DEAL_CARD[1].id)
        else:
            card_index = algorithm("right", "")
       # print(card_index)
        if card_index == len(RIGHT_HAND_CARDS_LIST):
            right_card_river.add_card(
                (SMALL_DEAL_CARD[1].id, "small_right"), "vert")
            SMALL_DEAL_CARD[0] = -1
           #print(f"right out:{SMALL_DEAL_CARD[1].id}")
            SMALL_DEAL_CARD[1].kill()
        else:
            right_card_river.add_card(
                (RIGHT_HAND_CARDS_LIST[card_index][1].id, "small_right"), "vert")
           #print(f"right out:{RIGHT_HAND_CARDS_LIST[card_index][1].id}")
            RIGHT_HAND_CARDS_LIST[card_index][1].kill()
            del RIGHT_HAND_CARDS_LIST[card_index]
    if site == "up":
        if is_have_deal_card:
            card_index = algorithm("up", SMALL_DEAL_CARD[1].id)
        else:
            card_index = algorithm("up", "")
       # print(card_index)
        if card_index == len(UP_HAND_CARDS_LIST):
            up_card_river.add_card((SMALL_DEAL_CARD[1].id, "small_up"), "vert")
            SMALL_DEAL_CARD[0] = -1
           #print(f"up out:{SMALL_DEAL_CARD[1].id}")
            SMALL_DEAL_CARD[1].kill()
        else:
            up_card_river.add_card(
                (UP_HAND_CARDS_LIST[card_index][1].id, "small_up"), "vert")
           #print(f"up out:{UP_HAND_CARDS_LIST[card_index][1].id}")
            UP_HAND_CARDS_LIST[card_index][1].kill()
            del UP_HAND_CARDS_LIST[card_index]
    if site == "left":
        if is_have_deal_card:
            card_index = algorithm("left", SMALL_DEAL_CARD[1].id)
        else:
            card_index = algorithm("left", "")
       # print(card_index)
        if card_index == len(LEFT_HAND_CARDS_LIST):
            left_card_river.add_card(
                (SMALL_DEAL_CARD[1].id, "small_left"), "vert")
            SMALL_DEAL_CARD[0] = -1
           #print(f"left out:{SMALL_DEAL_CARD[1].id}")
            SMALL_DEAL_CARD[1].kill()
        else:
            left_card_river.add_card(
                (LEFT_HAND_CARDS_LIST[card_index][1].id, "small_left"), "vert")
           #print(f"left out:{LEFT_HAND_CARDS_LIST[card_index][1].id}")
            LEFT_HAND_CARDS_LIST[card_index][1].kill()
            del LEFT_HAND_CARDS_LIST[card_index]


def sort(site):  # 排牌
    global HAND_CARDS_LIST
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST
    list = []
    if site == 'down':
        for i in range(len(HAND_CARDS_LIST)):
            list.append([MAHJONG_SORT_TABLE_LIST.index(
                HAND_CARDS_LIST[i][1].id), i])
        for i in range(len(list)):
            min_idx = i
            for j in range(i+1, len(list)):
                if list[min_idx] > list[j]:
                    min_idx = j
            list[i], list[min_idx] = list[min_idx], list[i]
            HAND_CARDS_LIST[i], HAND_CARDS_LIST[min_idx] = HAND_CARDS_LIST[min_idx], HAND_CARDS_LIST[i]

        for i in range(len(list)):
            HAND_CARDS_LIST[i][1].rect.left = HAND_CARDS_STARTX + \
                MAHJONG_WIDTH * i
            HAND_CARDS_LIST[i][1].mahjong_box.move_ip(-1000, -1000)
            HAND_CARDS_LIST[i][1].mahjong_box = pygame.Rect(
                HAND_CARDS_LIST[i][1].rect.left, HAND_CARDS_LIST[i][1].rect.top, HAND_CARDS_LIST[i][1].rect.width, HAND_CARDS_LIST[i][1].rect.height)
            #HAND_CARDS_LIST[i][1].mahjong_box.move_ip(HAND_CARDS_LIST[i][1].rect.left, HAND_CARDS_LIST[i][1].rect.top)
            HAND_CARDS_LIST[i][1].in_hand_id = i
            HAND_CARDS_LIST[i][0] = i
    elif site == 'left':
        for i in range(len(LEFT_HAND_CARDS_LIST)):
            list.append([MAHJONG_SORT_TABLE_LIST.index(
                LEFT_HAND_CARDS_LIST[i][1].id), i])
        for i in range(len(list)):
            min_idx = i
            for j in range(i+1, len(list)):
                if list[min_idx] > list[j]:
                    min_idx = j
            list[i], list[min_idx] = list[min_idx], list[i]
            LEFT_HAND_CARDS_LIST[i], LEFT_HAND_CARDS_LIST[min_idx] = LEFT_HAND_CARDS_LIST[min_idx], LEFT_HAND_CARDS_LIST[i]

        for i in range(len(list)):
            LEFT_HAND_CARDS_LIST[i][1].rect.top = LEFT_HAND_CARD_STARTY + \
                SMALL_MAHJONG_WIDTH * i
            # LEFT_HAND_CARDS_LIST[i][1].mahjong_box = pygame.Rect(
            #    LEFT_HAND_CARDS_LIST[i][1].rect.left, LEFT_HAND_CARDS_LIST[i][1].rect.top, LEFT_HAND_CARDS_LIST[i][1].rect.width, LEFT_HAND_CARDS_LIST[i][1].rect.height)
            LEFT_HAND_CARDS_LIST[i][1].in_hand_id = i
            LEFT_HAND_CARDS_LIST[i][0] = i

    elif site == 'up':
        for i in range(len(UP_HAND_CARDS_LIST)):
            list.append([MAHJONG_SORT_TABLE_LIST.index(
                UP_HAND_CARDS_LIST[i][1].id), i])
        for i in range(len(list)):
            min_idx = i
            for j in range(i+1, len(list)):
                if list[min_idx] > list[j]:
                    min_idx = j
            list[i], list[min_idx] = list[min_idx], list[i]
            UP_HAND_CARDS_LIST[i], UP_HAND_CARDS_LIST[min_idx] = UP_HAND_CARDS_LIST[min_idx], UP_HAND_CARDS_LIST[i]

        for i in range(len(list)):
            UP_HAND_CARDS_LIST[i][1].rect.left = UP_HAND_CARD_STARTX - \
                SMALL_MAHJONG_WIDTH * i
            # UP_HAND_CARDS_LIST[i][1].mahjong_box = pygame.Rect(
            #    UP_HAND_CARDS_LIST[i][1].rect.left, UP_HAND_CARDS_LIST[i][1].rect.top, UP_HAND_CARDS_LIST[i][1].rect.width, UP_HAND_CARDS_LIST[i][1].rect.height)
            UP_HAND_CARDS_LIST[i][1].in_hand_id = i
            UP_HAND_CARDS_LIST[i][0] = i

    elif site == 'right':
        for i in range(len(RIGHT_HAND_CARDS_LIST)):
            list.append([MAHJONG_SORT_TABLE_LIST.index(
                RIGHT_HAND_CARDS_LIST[i][1].id), i])
        for i in range(len(list)):
            min_idx = i
            for j in range(i+1, len(list)):
                if list[min_idx] > list[j]:
                    min_idx = j
            list[i], list[min_idx] = list[min_idx], list[i]
            RIGHT_HAND_CARDS_LIST[i], RIGHT_HAND_CARDS_LIST[min_idx] = RIGHT_HAND_CARDS_LIST[min_idx], RIGHT_HAND_CARDS_LIST[i]

        for i in range(len(list)):
            RIGHT_HAND_CARDS_LIST[i][1].rect.top = RIGHT_HAND_CARD_STARTY - \
                SMALL_MAHJONG_WIDTH * i
            # RIGHT_HAND_CARDS_LIST[i][1].mahjong_box = pygame.Rect(
            #    RIGHT_HAND_CARDS_LIST[i][1].rect.left, RIGHT_HAND_CARDS_LIST[i][1].rect.top, RIGHT_HAND_CARDS_LIST[i][1].rect.width, RIGHT_HAND_CARDS_LIST[i][1].rect.height)
            RIGHT_HAND_CARDS_LIST[i][1].in_hand_id = i
            RIGHT_HAND_CARDS_LIST[i][0] = i


IS_SHOW_COUNTDOWN = 0  # 是否要顯示倒計時
COUNTDOWN_TIME = 0  # 剩餘秒數
IS_COUNTDOWN_FINISH = 0  # 是否數到0


def countdown(second, is_show):  # 倒計時函式,倒計時結束IS_COUNTDOWN_FINISH=1
    global IS_SHOW_COUNTDOWN
    global COUNTDOWN_TIME
    global IS_COUNTDOWN_FINISH
    if is_show == 1:
        IS_SHOW_COUNTDOWN = 1
    i = second
    time_event.clear()
    print("clear & wait")
    while i >= 0 and not time_event.is_set():
        COUNTDOWN_TIME = i
        time_event.wait(1)
        i -= 1
    IS_SHOW_COUNTDOWN = 0
    if i < 0:
        IS_COUNTDOWN_FINISH = 1
    else:
        IS_COUNTDOWN_FINISH = 0


def multi_auto_out_card():
    global player
    global MAHJONG_BUTTON_LIST
    global HAND_CARDS_LIST
    try:
        if DEAL_CARD[0] != -1:
            i = 0
            while i < len(MAHJONG_BUTTON_LIST):
                if MAHJONG_BUTTON_LIST[i].in_hand_id == DEAL_CARD[0] and MAHJONG_BUTTON_LIST[i].id == DEAL_CARD[1].id:
                    MAHJONG_BUTTON_LIST[i].mahjong_box.move_ip(-1000, -1000)
                    MAHJONG_BUTTON_LIST[i].kill()
                    del MAHJONG_BUTTON_LIST[i]
                    break
                i += 1
            id = DEAL_CARD[1].id
            player.out_card(DEAL_CARD[0], DEAL_CARD[1].id)
            print("send to server ",id)
            send_to_server(["out", id])
        else:
            i = 0
            while i < len(MAHJONG_BUTTON_LIST):
                if MAHJONG_BUTTON_LIST[i].in_hand_id == HAND_CARDS_LIST[len(HAND_CARDS_LIST)-1][0] and MAHJONG_BUTTON_LIST[i].id == HAND_CARDS_LIST[len(HAND_CARDS_LIST)-1][1].id:
                    MAHJONG_BUTTON_LIST[i].mahjong_box.move_ip(-1000, -1000)
                    MAHJONG_BUTTON_LIST[i].kill()
                    del MAHJONG_BUTTON_LIST[i]
                    break
                i += 1
            id = HAND_CARDS_LIST[len(HAND_CARDS_LIST)-1][1].id
            player.out_card(HAND_CARDS_LIST[len(
                HAND_CARDS_LIST)-1][0], HAND_CARDS_LIST[len(HAND_CARDS_LIST)-1][1].id)
            print("send to server ",id)
            send_to_server(["out", id])
    except:
        i = 0
        while i < len(MAHJONG_BUTTON_LIST):
            if MAHJONG_BUTTON_LIST[i].in_hand_id == HAND_CARDS_LIST[len(HAND_CARDS_LIST)-1][0] and MAHJONG_BUTTON_LIST[i].id == HAND_CARDS_LIST[len(HAND_CARDS_LIST)-1][1].id:
                MAHJONG_BUTTON_LIST[i].mahjong_box.move_ip(-1000, -1000)
                MAHJONG_BUTTON_LIST[i].kill()
                del MAHJONG_BUTTON_LIST[i]
                break
            i += 1
        id = HAND_CARDS_LIST[len(HAND_CARDS_LIST)-1][1].id
        player.out_card(HAND_CARDS_LIST[len(
            HAND_CARDS_LIST)-1][0], HAND_CARDS_LIST[len(HAND_CARDS_LIST)-1][1].id)
        print("send to server ",id)
        send_to_server(["out", id])

    countdown_send()


def player_auto_out_card(is_no_deal_card):  # 玩家倒計時結束自動出牌
    global player
    global MAHJONG_BUTTON_LIST
    global HAND_CARDS_LIST
    if is_no_deal_card:
        i = 0
        while i < len(MAHJONG_BUTTON_LIST):
            if MAHJONG_BUTTON_LIST[i].in_hand_id == HAND_CARDS_LIST[len(HAND_CARDS_LIST)-1][0] and MAHJONG_BUTTON_LIST[i].id == HAND_CARDS_LIST[len(HAND_CARDS_LIST)-1][1].id:
                MAHJONG_BUTTON_LIST[i].mahjong_box.move_ip(-1000, -1000)
                MAHJONG_BUTTON_LIST[i].kill()
                del MAHJONG_BUTTON_LIST[i]
                break
            i += 1
    else:
        i = 0
        while i < len(MAHJONG_BUTTON_LIST):
            if MAHJONG_BUTTON_LIST[i].in_hand_id == DEAL_CARD[0] and MAHJONG_BUTTON_LIST[i].id == DEAL_CARD[1].id:
                MAHJONG_BUTTON_LIST[i].mahjong_box.move_ip(-1000, -1000)
                MAHJONG_BUTTON_LIST[i].kill()
                del MAHJONG_BUTTON_LIST[i]
                break
            i += 1
    player.out_card(DEAL_CARD[0], DEAL_CARD[1].id)


PLAYER_CAN_CHI = 0
PLAYER_CAN_PONG = 0
PLAYER_CAN_KONG = 0
RIGHT_CAN_CHI = 0
RIGHT_CAN_PONG = 0
RIGHT_CAN_KONG = 0
UP_CAN_CHI = 0
UP_CAN_PONG = 0
UP_CAN_KONG = 0
LEFT_CAN_CHI = 0
LEFT_CAN_PONG = 0
LEFT_CAN_KONG = 0
CHI_TABLE = {
    "Man1": [["Man2", "Man3"]],
    "Man2": [["Man1", "Man3"], ["Man3", "Man4"]],
    "Man3": [["Man1", "Man2"], ["Man2", "Man4"], ["Man4", "Man5"], ["Man4", "Man5_red"]],
    "Man4": [["Man2", "Man3"], ["Man3", "Man5"], ["Man3", "Man5_red"], ["Man5", "Man6"], ["Man5_red", "Man6"]],
    "Man5": [["Man3", "Man4"], ["Man4", "Man6"], ["Man6", "Man7"]],
    "Man5_red": [["Man3", "Man4"], ["Man4", "Man6"], ["Man6", "Man7"]],
    "Man6": [["Man4", "Man5"], ["Man4", "Man5_red"], ["Man5", "Man7"], ["Man5_red", "Man7"], ["Man7", "Man8"]],
    "Man7": [["Man5", "Man6"], ["Man5_red", "Man6"], ["Man6", "Man8"], ["Man8", "Man9"]],
    "Man8": [["Man6", "Man7"], ["Man7", "Man9"]],
    "Man9": [["Man7", "Man8"]],
    "Pin1": [["Pin2", "Pin3"]],
    "Pin2": [["Pin1", "Pin3"], ["Pin3", "Pin4"]],
    "Pin3": [["Pin1", "Pin2"], ["Pin2", "Pin4"], ["Pin4", "Pin5"], ["Pin4", "Pin5_red"]],
    "Pin4": [["Pin2", "Pin3"], ["Pin3", "Pin5"], ["Pin3", "Pin5_red"], ["Pin5", "Pin6"], ["Pin5_red", "Pin6"]],
    "Pin5": [["Pin3", "Pin4"], ["Pin4", "Pin6"], ["Pin6", "Pin7"]],
    "Pin5_red": [["Pin3", "Pin4"], ["Pin4", "Pin6"], ["Pin6", "Pin7"]],
    "Pin6": [["Pin4", "Pin5"], ["Pin4", "Pin5_red"], ["Pin5", "Pin7"], ["Pin5_red", "Pin7"], ["Pin7", "Pin8"]],
    "Pin7": [["Pin5", "Pin6"], ["Pin5_red", "Pin6"], ["Pin6", "Pin8"], ["Pin8", "Pin9"]],
    "Pin8": [["Pin6", "Pin7"], ["Pin7", "Pin9"]],
    "Pin9": [["Pin7", "Pin8"]],
    "Sou1": [["Sou2", "Sou3"]],
    "Sou2": [["Sou1", "Sou3"], ["Sou3", "Sou4"]],
    "Sou3": [["Sou1", "Sou2"], ["Sou2", "Sou4"], ["Sou4", "Sou5"], ["Sou4", "Sou5_red"]],
    "Sou4": [["Sou2", "Sou3"], ["Sou3", "Sou5"], ["Sou3", "Sou5_red"], ["Sou5", "Sou6"], ["Sou5_red", "Sou6"]],
    "Sou5": [["Sou3", "Sou4"], ["Sou4", "Sou6"], ["Sou6", "Sou7"]],
    "Sou5_red": [["Sou3", "Sou4"], ["Sou4", "Sou6"], ["Sou6", "Sou7"]],
    "Sou6": [["Sou4", "Sou5"], ["Sou4", "Sou5_red"], ["Sou5", "Sou7"], ["Sou5_red", "Sou7"], ["Sou7", "Sou8"]],
    "Sou7": [["Sou5", "Sou6"], ["Sou5_red", "Sou6"], ["Sou6", "Sou8"], ["Sou8", "Sou9"]],
    "Sou8": [["Sou6", "Sou7"], ["Sou7", "Sou9"]],
    "Sou9": [["Sou7", "Sou8"]],
}


def other_can_chi(site, mahjong_id):  # 判斷是否可以吃牌
    global PLAYER_CAN_CHI
    global RIGHT_CAN_CHI
    global UP_CAN_CHI
    global LEFT_CAN_CHI

    can_or_can_not = False

    try:
        possiable_combination_list = CHI_TABLE[mahjong_id]
    except:
        return [False, []]

    comb_card1_id = ""
    comb_card2_id = ""
    found_card1 = False
    found_card2 = False
    target_cards = []  # 存可組合的牌id

    if site == "left":  # 判斷本家能不能吃
        i = 0
        while i < len(possiable_combination_list):
            comb_card1_id = possiable_combination_list[i][0]
            comb_card2_id = possiable_combination_list[i][1]
            j = 0
            while j < len(HAND_CARDS_LIST):
                if comb_card1_id == HAND_CARDS_LIST[j][1].id:
                    found_card1 = True
                    break
                j += 1
            while j < len(HAND_CARDS_LIST):
                if comb_card2_id == HAND_CARDS_LIST[j][1].id:
                    found_card2 = True
                    break
                j += 1
            if found_card1 and found_card2:
                target_cards.append([comb_card1_id, comb_card2_id])
                PLAYER_CAN_CHI = 1
                can_or_can_not = True
            found_card1 = False
            found_card2 = False
            i += 1

    elif site == "down":  # 判斷下家能不能吃
        i = 0
        while i < len(possiable_combination_list):
            comb_card1_id = possiable_combination_list[i][0]
            comb_card2_id = possiable_combination_list[i][1]
            j = 0
            while j < len(RIGHT_HAND_CARDS_LIST):
                if comb_card1_id == RIGHT_HAND_CARDS_LIST[j][1].id:
                    found_card1 = True
                    break
                j += 1
            while j < len(RIGHT_HAND_CARDS_LIST):
                if comb_card2_id == RIGHT_HAND_CARDS_LIST[j][1].id:
                    found_card2 = True
                    break
                j += 1
            if found_card1 and found_card2:
                target_cards.append([comb_card1_id, comb_card2_id])
                RIGHT_CAN_CHI = 1
                can_or_can_not = True
            found_card1 = False
            found_card2 = False
            i += 1

    elif site == "right":  # 判斷對家能不能吃
        i = 0
        while i < len(possiable_combination_list):
            comb_card1_id = possiable_combination_list[i][0]
            comb_card2_id = possiable_combination_list[i][1]
            j = 0
            while j < len(UP_HAND_CARDS_LIST):
                if comb_card1_id == UP_HAND_CARDS_LIST[j][1].id:
                    found_card1 = True
                    break
                j += 1
            while j < len(UP_HAND_CARDS_LIST):
                if comb_card2_id == UP_HAND_CARDS_LIST[j][1].id:
                    found_card2 = True
                    break
                j += 1
            if found_card1 and found_card2:
                target_cards.append([comb_card1_id, comb_card2_id])
                UP_CAN_CHI = 1
                can_or_can_not = True
            found_card1 = False
            found_card2 = False
            i += 1

    elif site == "up":  # 判斷上家能不能吃
        i = 0
        while i < len(possiable_combination_list):
            comb_card1_id = possiable_combination_list[i][0]
            comb_card2_id = possiable_combination_list[i][1]
            j = 0
            while j < len(LEFT_HAND_CARDS_LIST):
                if comb_card1_id == LEFT_HAND_CARDS_LIST[j][1].id:
                    found_card1 = True
                    break
                j += 1
            while j < len(LEFT_HAND_CARDS_LIST):
                if comb_card2_id == LEFT_HAND_CARDS_LIST[j][1].id:
                    found_card2 = True
                    break
                j += 1
            if found_card1 and found_card2:
                target_cards.append([comb_card1_id, comb_card2_id])
                LEFT_CAN_CHI = 1
                can_or_can_not = True
            found_card1 = False
            found_card2 = False
            i += 1

    return [can_or_can_not, target_cards]


def others_can_pong_or_kong(site, mahjong_id):  # 判斷是否可以碰牌&槓牌
    global PLAYER_CAN_PONG
    global PLAYER_CAN_KONG
    global RIGHT_CAN_PONG
    global RIGHT_CAN_KONG
    global UP_CAN_PONG
    global UP_CAN_KONG
    global LEFT_CAN_PONG
    global LEFT_CAN_KONG
    mahjong_number = MAHJONG_SORT_TABLE_LIST.index(mahjong_id)
    # 進來是紅寶只需要找普通牌
    if mahjong_number == 5 or mahjong_number == 15 or mahjong_number == 25:
        mahjong_number = mahjong_number == 5 - 1
    hand_card_number_list = []
    index = []  # 數相同的牌有幾張
    if site != "down":
        for i in range(len(HAND_CARDS_LIST)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(HAND_CARDS_LIST[i][1].id))
        for i in range(len(HAND_CARDS_LIST)):
            if mahjong_number == hand_card_number_list[i]:
                index.append(i)
        if mahjong_number == 4:
            mahjong_number = mahjong_number + 1
            for i in range(len(HAND_CARDS_LIST)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 14:
            mahjong_number = mahjong_number + 1
            for i in range(len(HAND_CARDS_LIST)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 24:
            mahjong_number = mahjong_number + 1
            for i in range(len(HAND_CARDS_LIST)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif len(index) == 2:
            PLAYER_CAN_PONG = 1
            return(True)
        elif len(index) == 3:
            PLAYER_CAN_KONG = 1
            PLAYER_CAN_PONG = 1
            return(True)
    hand_card_number_list = []
    index = []  # 數相同的牌有幾張
    if site != "right":
        for i in range(len(RIGHT_HAND_CARDS_LIST)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(RIGHT_HAND_CARDS_LIST[i][1].id))
        for i in range(len(RIGHT_HAND_CARDS_LIST)):
            if mahjong_number == hand_card_number_list[i]:
                index.append(i)
        if mahjong_number == 4:
            mahjong_number = mahjong_number + 1
            for i in range(len(RIGHT_HAND_CARDS_LIST)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 14:
            mahjong_number = mahjong_number + 1
            for i in range(len(RIGHT_HAND_CARDS_LIST)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 24:
            mahjong_number = mahjong_number + 1
            for i in range(len(RIGHT_HAND_CARDS_LIST)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif len(index) == 2:
            RIGHT_CAN_PONG = 1
            return(True)
        elif len(index) == 3:
            RIGHT_CAN_KONG = 1
            RIGHT_CAN_PONG = 1
            return(True)
    hand_card_number_list = []
    index = []  # 數相同的牌有幾張
    if site != "up":
        for i in range(len(UP_HAND_CARDS_LIST)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(UP_HAND_CARDS_LIST[i][1].id))
        for i in range(len(UP_HAND_CARDS_LIST)):
            if mahjong_number == hand_card_number_list[i]:
                index.append(i)
        if mahjong_number == 4:
            mahjong_number = mahjong_number + 1
            for i in range(len(UP_HAND_CARDS_LIST)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 14:
            mahjong_number = mahjong_number + 1
            for i in range(len(UP_HAND_CARDS_LIST)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 24:
            mahjong_number = mahjong_number + 1
            for i in range(len(UP_HAND_CARDS_LIST)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif len(index) == 2:
            UP_CAN_PONG = 1
            return(True)
        elif len(index) == 3:
            UP_CAN_KONG = 1
            UP_CAN_PONG = 1
            return(True)
    hand_card_number_list = []
    index = []  # 數相同的牌有幾張
    if site != "left":
        for i in range(len(LEFT_HAND_CARDS_LIST)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(LEFT_HAND_CARDS_LIST[i][1].id))
        for i in range(len(LEFT_HAND_CARDS_LIST)):
            if mahjong_number == hand_card_number_list[i]:
                index.append(i)
        if mahjong_number == 4:
            mahjong_number = mahjong_number + 1
            for i in range(len(LEFT_HAND_CARDS_LIST)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 14:
            mahjong_number = mahjong_number + 1
            for i in range(len(LEFT_HAND_CARDS_LIST)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif mahjong_number == 24:
            mahjong_number = mahjong_number + 1
            for i in range(len(LEFT_HAND_CARDS_LIST)):
                if mahjong_number == hand_card_number_list[i]:
                    index.append(i)
        elif len(index) == 2:
            LEFT_CAN_PONG = 1
            return(True)
        elif len(index) == 3:
            LEFT_CAN_KONG = 1
            LEFT_CAN_PONG = 1
            return(True)
    return(False)


# 三家鳴牌區
RIGHT_VICE_DEWS = []  # [[這一張的x,下一張的y,小麻將物件], ...]
UP_VICE_DEWS = []  # [[下一張的x,這(下)一張的y,小麻將物件], ...]
LEFT_VICE_DEWS = []  # [[這(下)一張的x,這一張的y,小麻將物件], ...]
RIGHT_VICE_DEWS_START_X = WIDTH - SMALL_MAHJONG_HEIGHT
RIGHT_VICE_DEWS_START_Y = 0
UP_VICE_DEWS_START_X = 200
UP_VICE_DEWS_START_Y = 0
LEFT_VICE_DEWS_START_X = 0
LEFT_VICE_DEWS_START_Y = HEIGHT

# 其他三家吃碰槓


def multi_chi(site, card_list):
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST
    global play_multi_sprites
    print("IN multi_chi")
    if site == "right":
        try:
            RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1][1].kill()
            del RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1]
            RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1][1].kill()
            del RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1]
        except:
            print("RIGHT_HAND_CARDS_LIST",RIGHT_HAND_CARDS_LIST)
            time.sleep(100)
        # 加到鳴牌區
        if len(RIGHT_VICE_DEWS) > 0:
            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(card_list[1], x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
        else:
            vdsm = Small_Mahjong(
                card_list[1], RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y, "right")
            RIGHT_VICE_DEWS.append(
                [RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y + SMALL_MAHJONG_WIDTH, vdsm])
        play_multi_sprites.add(vdsm)

        x = RIGHT_VICE_DEWS_START_X
        y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
        vdsm = Small_Mahjong(card_list[0], x, y, "right")
        RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
        play_multi_sprites.add(vdsm)

        x = RIGHT_VICE_DEWS_START_X + \
            (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH)
        y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
        vdsm = Small_Mahjong(card_list[2], x, y, "up")
        RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_HEIGHT, vdsm])
        play_multi_sprites.add(vdsm)

    elif site == "up":
        try:
            UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1][1].kill()
            del UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1]
            UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1][1].kill()
            del UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1]
        except:
            print("UP_HAND_CARDS_LIST",UP_HAND_CARDS_LIST)
            time.sleep(100)
        # 加到鳴牌區
        if len(UP_VICE_DEWS) > 0:
            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(card_list[1], x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
        else:
            vdsm = Small_Mahjong(
                card_list[1], UP_VICE_DEWS_START_X, UP_VICE_DEWS_START_Y, "up")
            UP_VICE_DEWS.append(
                [UP_VICE_DEWS_START_X + SMALL_MAHJONG_WIDTH, UP_VICE_DEWS_START_Y, vdsm])
        play_multi_sprites.add(vdsm)

        x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
        y = UP_VICE_DEWS_START_Y
        vdsm = Small_Mahjong(card_list[0], x, y, "up")
        UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
        play_multi_sprites.add(vdsm)

        x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
        y = UP_VICE_DEWS_START_Y
        vdsm = Small_Mahjong(card_list[2], x, y, "left")
        UP_VICE_DEWS.append([x + SMALL_MAHJONG_HEIGHT, y, vdsm])
        play_multi_sprites.add(vdsm)

    elif site == "left":
        try:
            LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1][1].kill()
            del LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1]
            LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1][1].kill()
            del LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1]
        except:
            print("LEFT_HAND_CARDS_LIST",LEFT_HAND_CARDS_LIST)
            time.sleep(100)
        # 加到鳴牌區
        if len(LEFT_VICE_DEWS) > 0:
            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(
                card_list[1], x, y - SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
        else:
            vdsm = Small_Mahjong(
                card_list[1], LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append(
                [LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, vdsm])
        play_multi_sprites.add(vdsm)

        x = LEFT_VICE_DEWS_START_X
        y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
        vdsm = Small_Mahjong(
            card_list[0], x, y - SMALL_MAHJONG_WIDTH, "left")
        LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
        play_multi_sprites.add(vdsm)

        x = LEFT_VICE_DEWS_START_X
        y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
        vdsm = Small_Mahjong(card_list[2], x, y -
                             SMALL_MAHJONG_HEIGHT, "down")
        LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_HEIGHT, vdsm])
        play_multi_sprites.add(vdsm)


def chi(site, target_cards_id_list):
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST

    global right_card_river
    global up_card_river
    global RIGHT_VICE_DEWS
    global UP_VICE_DEWS
    global LEFT_VICE_DEWS
    global play_single_sprites

    if site == "right":
        other_card_id = player_card_river.get_last_card_id()
        player_card_river.del_last_card()
       #print(f"right chi:{other_card_id}")
        # 根據id從手牌刪除
        i = 0
        while i < len(RIGHT_HAND_CARDS_LIST):
            if RIGHT_HAND_CARDS_LIST[i][1].id == target_cards_id_list[0]:
                RIGHT_HAND_CARDS_LIST[i][1].kill()
                del RIGHT_HAND_CARDS_LIST[i]
                break
            i += 1
        i = 0
        while i < len(RIGHT_HAND_CARDS_LIST):
            if RIGHT_HAND_CARDS_LIST[i][1].id == target_cards_id_list[1]:
                RIGHT_HAND_CARDS_LIST[i][1].kill()
                del RIGHT_HAND_CARDS_LIST[i]
                break
            i += 1
        sort("right")
        # 加到鳴牌區
        if len(RIGHT_VICE_DEWS) > 0:
            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_cards_id_list[1], x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
        else:
            vdsm = Small_Mahjong(
                target_cards_id_list[1], RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y, "right")
            RIGHT_VICE_DEWS.append(
                [RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y + SMALL_MAHJONG_WIDTH, vdsm])
        play_single_sprites.add(vdsm)

        x = RIGHT_VICE_DEWS_START_X
        y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
        vdsm = Small_Mahjong(target_cards_id_list[0], x, y, "right")
        RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
        play_single_sprites.add(vdsm)

        x = RIGHT_VICE_DEWS_START_X + \
            (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH)
        y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
        vdsm = Small_Mahjong(other_card_id, x, y, "up")
        RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_HEIGHT, vdsm])
        play_single_sprites.add(vdsm)

    if site == "up":
        other_card_id = right_card_river.get_last_card_id()
        right_card_river.del_last_card()
       #print(f"up chi:{other_card_id}")
        # 根據id從手牌刪除
        i = 0
        while i < len(UP_HAND_CARDS_LIST):
            if UP_HAND_CARDS_LIST[i][1].id == target_cards_id_list[0]:
                UP_HAND_CARDS_LIST[i][1].kill()
                del UP_HAND_CARDS_LIST[i]
                break
            i += 1
        i = 0
        while i < len(UP_HAND_CARDS_LIST):
            if UP_HAND_CARDS_LIST[i][1].id == target_cards_id_list[1]:
                UP_HAND_CARDS_LIST[i][1].kill()
                del UP_HAND_CARDS_LIST[i]
                break
            i += 1
        sort("up")
        # 加到鳴牌區
        if len(UP_VICE_DEWS) > 0:
            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_cards_id_list[1], x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
        else:
            vdsm = Small_Mahjong(
                target_cards_id_list[1], UP_VICE_DEWS_START_X, UP_VICE_DEWS_START_Y, "up")
            UP_VICE_DEWS.append(
                [UP_VICE_DEWS_START_X + SMALL_MAHJONG_WIDTH, UP_VICE_DEWS_START_Y, vdsm])
        play_single_sprites.add(vdsm)

        x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
        y = UP_VICE_DEWS_START_Y
        vdsm = Small_Mahjong(target_cards_id_list[0], x, y, "up")
        UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
        play_single_sprites.add(vdsm)

        x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
        y = UP_VICE_DEWS_START_Y
        vdsm = Small_Mahjong(other_card_id, x, y, "left")
        UP_VICE_DEWS.append([x + SMALL_MAHJONG_HEIGHT, y, vdsm])
        play_single_sprites.add(vdsm)

    if site == "left":
        other_card_id = up_card_river.get_last_card_id()
        up_card_river.del_last_card()
       #print(f"left chi:{other_card_id}")
        # 根據id從手牌刪除
        i = 0
        while i < len(LEFT_HAND_CARDS_LIST):
            if LEFT_HAND_CARDS_LIST[i][1].id == target_cards_id_list[0]:
                LEFT_HAND_CARDS_LIST[i][1].kill()
                del LEFT_HAND_CARDS_LIST[i]
                break
            i += 1
        i = 0
        while i < len(LEFT_HAND_CARDS_LIST):
            if LEFT_HAND_CARDS_LIST[i][1].id == target_cards_id_list[1]:
                LEFT_HAND_CARDS_LIST[i][1].kill()
                del LEFT_HAND_CARDS_LIST[i]
                break
            i += 1
        sort("left")
        # 加到鳴牌區
        if len(LEFT_VICE_DEWS) > 0:
            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(
                target_cards_id_list[1], x, y - SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
        else:
            vdsm = Small_Mahjong(
                target_cards_id_list[1], LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append(
                [LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, vdsm])
        play_single_sprites.add(vdsm)

        x = LEFT_VICE_DEWS_START_X
        y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
        vdsm = Small_Mahjong(
            target_cards_id_list[0], x, y - SMALL_MAHJONG_WIDTH, "left")
        LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
        play_single_sprites.add(vdsm)

        x = LEFT_VICE_DEWS_START_X
        y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
        vdsm = Small_Mahjong(other_card_id, x, y -
                             SMALL_MAHJONG_HEIGHT, "down")
        LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_HEIGHT, vdsm])
        play_single_sprites.add(vdsm)


def multi_kong(s_site, d_site, card_id):
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST
    global RIGHT_VICE_DEWS
    global UP_VICE_DEWS
    global LEFT_VICE_DEWS
    global play_multi_sprites
    global player_card_river
    global right_card_river
    global up_card_river
    global left_card_river
    target_card_id = card_id
    print("IN multi_kong")

    if d_site == "right":
        try:
            RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1][1].kill()
            del RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1]
            RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1][1].kill()
            del RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1]
            RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1][1].kill()
            del RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1]
        except:
            print("RIGHT_HAND_CARDS_LIST",RIGHT_HAND_CARDS_LIST)
            time.sleep(100)
        if s_site == "up":

            if len(RIGHT_VICE_DEWS) > 0:
                x = RIGHT_VICE_DEWS_START_X + \
                    (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH)
                y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(target_card_id, x, y, "up")
                RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_HEIGHT, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id, RIGHT_VICE_DEWS_START_X + (
                    SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH), RIGHT_VICE_DEWS_START_Y, "up")
                RIGHT_VICE_DEWS.append([RIGHT_VICE_DEWS_START_X + (SMALL_MAHJONG_HEIGHT -
                                       SMALL_MAHJONG_WIDTH), RIGHT_VICE_DEWS_START_Y + SMALL_MAHJONG_HEIGHT, vdsm])
            play_multi_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

        if s_site == "left":

            if len(RIGHT_VICE_DEWS) > 0:
                x = RIGHT_VICE_DEWS_START_X
                y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(target_card_id, x, y, "right")
                RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id, RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y, "right")
                RIGHT_VICE_DEWS.append(
                    [RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y + SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X + \
                (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH)
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y, "up")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_HEIGHT, vdsm])
            play_multi_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

        if s_site == "down":

            if len(RIGHT_VICE_DEWS) > 0:
                x = RIGHT_VICE_DEWS_START_X
                y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(target_card_id, x, y, "right")
                RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id, RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y, "right")
                RIGHT_VICE_DEWS.append(
                    [RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y + SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X + \
                (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH)
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y, "up")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_HEIGHT, vdsm])
            play_multi_sprites.add(vdsm)

    elif d_site == "up":
        try:
            UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1][1].kill()
            del UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1]
            UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1][1].kill()
            del UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1]
            UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1][1].kill()
            del UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1]
        except:
            print("UP_HAND_CARDS_LIST",UP_HAND_CARDS_LIST)
            time.sleep(100)

        if s_site == "left":

            if len(UP_VICE_DEWS) > 0:
                x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
                y = UP_VICE_DEWS_START_Y
                vdsm = Small_Mahjong(target_card_id, x, y, "left")
                UP_VICE_DEWS.append([x + SMALL_MAHJONG_HEIGHT, y, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id, UP_VICE_DEWS_START_X, UP_VICE_DEWS_START_Y, "left")
                UP_VICE_DEWS.append(
                    [UP_VICE_DEWS_START_X + SMALL_MAHJONG_HEIGHT, UP_VICE_DEWS_START_Y, vdsm])
            play_multi_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_multi_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_multi_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_multi_sprites.add(vdsm)

        if s_site == "down":

            if len(UP_VICE_DEWS) > 0:
                x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
                y = UP_VICE_DEWS_START_Y
                vdsm = Small_Mahjong(target_card_id, x, y, "up")
                UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id, UP_VICE_DEWS_START_X, UP_VICE_DEWS_START_Y, "up")
                UP_VICE_DEWS.append(
                    [UP_VICE_DEWS_START_X + SMALL_MAHJONG_WIDTH, UP_VICE_DEWS_START_Y, vdsm])
            play_multi_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id, x, y, "left")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_HEIGHT, y, vdsm])
            play_multi_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_multi_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_multi_sprites.add(vdsm)

        if s_site == "right":

            if len(UP_VICE_DEWS) > 0:
                x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
                y = UP_VICE_DEWS_START_Y
                vdsm = Small_Mahjong(target_card_id, x, y, "up")
                UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id, UP_VICE_DEWS_START_X, UP_VICE_DEWS_START_Y, "up")
                UP_VICE_DEWS.append(
                    [UP_VICE_DEWS_START_X + SMALL_MAHJONG_WIDTH, UP_VICE_DEWS_START_Y, vdsm])
            play_multi_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_multi_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_multi_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id, x, y, "left")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_HEIGHT, y, vdsm])
            play_multi_sprites.add(vdsm)

    elif d_site == "left":
        try:
            LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1][1].kill()
            del LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1]
            LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1][1].kill()
            del LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1]
            LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1][1].kill()
            del LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1]
        except:
            print("LEFT_HAND_CARDS_LIST",LEFT_HAND_CARDS_LIST)
            time.sleep(100)
        if s_site == "down":

            if len(LEFT_VICE_DEWS) > 0:
                x = LEFT_VICE_DEWS_START_X
                y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(
                    target_card_id, x, y - SMALL_MAHJONG_HEIGHT, "down")
                LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_HEIGHT, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id, LEFT_VICE_DEWS_START_X,
                                     LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_HEIGHT, "down")
                LEFT_VICE_DEWS.append(
                    [LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_HEIGHT, vdsm])
            play_multi_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

        if s_site == "right":

            if len(LEFT_VICE_DEWS) > 0:
                x = LEFT_VICE_DEWS_START_X
                y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(
                    target_card_id, x, y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id, LEFT_VICE_DEWS_START_X,
                                     LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append(
                    [LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y -
                                 SMALL_MAHJONG_HEIGHT, "down")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_HEIGHT, vdsm])
            play_multi_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

        if s_site == "up":

            if len(LEFT_VICE_DEWS) > 0:
                x = LEFT_VICE_DEWS_START_X
                y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(
                    target_card_id, x, y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id, LEFT_VICE_DEWS_START_X,
                                     LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append(
                    [LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y -
                                 SMALL_MAHJONG_HEIGHT, "down")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_HEIGHT, vdsm])
            play_multi_sprites.add(vdsm)


def multi_pong(s_site, d_site, card_id):
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST
    global RIGHT_VICE_DEWS
    global UP_VICE_DEWS
    global LEFT_VICE_DEWS
    global play_multi_sprites
    global player_card_river
    global right_card_river
    global up_card_river
    global left_card_river
    target_card_id = card_id
    print("IN multi_pong")

    if d_site == "right":
        try:
            RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1][1].kill()
            del RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1]
            RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1][1].kill()
            del RIGHT_HAND_CARDS_LIST[len(RIGHT_HAND_CARDS_LIST)-1]
        except:
            print("RIGHT_HAND_CARDS_LIST",RIGHT_HAND_CARDS_LIST)
            time.sleep(100)

        if s_site == "up":

            if len(RIGHT_VICE_DEWS) > 0:
                x = RIGHT_VICE_DEWS_START_X + \
                    (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH)
                y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(target_card_id, x, y, "up")
                RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_HEIGHT, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id, RIGHT_VICE_DEWS_START_X + (
                    SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH), RIGHT_VICE_DEWS_START_Y, "up")
                RIGHT_VICE_DEWS.append([RIGHT_VICE_DEWS_START_X + (SMALL_MAHJONG_HEIGHT -
                                       SMALL_MAHJONG_WIDTH), RIGHT_VICE_DEWS_START_Y + SMALL_MAHJONG_HEIGHT, vdsm])
            play_multi_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

        if s_site == "left":

            if len(RIGHT_VICE_DEWS) > 0:
                x = RIGHT_VICE_DEWS_START_X
                y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(target_card_id, x, y, "right")
                RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id, RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y, "right")
                RIGHT_VICE_DEWS.append(
                    [RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y + SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X + \
                (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH)
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y, "up")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_HEIGHT, vdsm])
            play_multi_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

        if s_site == "down":

            if len(RIGHT_VICE_DEWS) > 0:
                x = RIGHT_VICE_DEWS_START_X
                y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(target_card_id, x, y, "right")
                RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id, RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y, "right")
                RIGHT_VICE_DEWS.append(
                    [RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y + SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X + \
                (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH)
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y, "up")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_HEIGHT, vdsm])
            play_multi_sprites.add(vdsm)

    elif d_site == "up":
        try:
            UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1][1].kill()
            del UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1]
            UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1][1].kill()
            del UP_HAND_CARDS_LIST[len(UP_HAND_CARDS_LIST)-1]
        except:
            print("UP_HAND_CARDS_LIST",UP_HAND_CARDS_LIST)
            time.sleep(100)

        if s_site == "left":

            if len(UP_VICE_DEWS) > 0:
                x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
                y = UP_VICE_DEWS_START_Y
                vdsm = Small_Mahjong(target_card_id, x, y, "left")
                UP_VICE_DEWS.append([x + SMALL_MAHJONG_HEIGHT, y, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id, UP_VICE_DEWS_START_X, UP_VICE_DEWS_START_Y, "left")
                UP_VICE_DEWS.append(
                    [UP_VICE_DEWS_START_X + SMALL_MAHJONG_HEIGHT, UP_VICE_DEWS_START_Y, vdsm])
            play_multi_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_multi_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_multi_sprites.add(vdsm)

        if s_site == "down":

            if len(UP_VICE_DEWS) > 0:
                x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
                y = UP_VICE_DEWS_START_Y
                vdsm = Small_Mahjong(target_card_id, x, y, "up")
                UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id, UP_VICE_DEWS_START_X, UP_VICE_DEWS_START_Y, "up")
                UP_VICE_DEWS.append(
                    [UP_VICE_DEWS_START_X + SMALL_MAHJONG_WIDTH, UP_VICE_DEWS_START_Y, vdsm])
            play_multi_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id, x, y, "left")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_HEIGHT, y, vdsm])
            play_multi_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_multi_sprites.add(vdsm)

        if s_site == "right":

            if len(UP_VICE_DEWS) > 0:
                x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
                y = UP_VICE_DEWS_START_Y
                vdsm = Small_Mahjong(target_card_id, x, y, "up")
                UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id, UP_VICE_DEWS_START_X, UP_VICE_DEWS_START_Y, "up")
                UP_VICE_DEWS.append(
                    [UP_VICE_DEWS_START_X + SMALL_MAHJONG_WIDTH, UP_VICE_DEWS_START_Y, vdsm])
            play_multi_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_multi_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id, x, y, "left")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_HEIGHT, y, vdsm])
            play_multi_sprites.add(vdsm)

    elif d_site == "left":
        try:
            LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1][1].kill()
            del LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1]
            LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1][1].kill()
            del LEFT_HAND_CARDS_LIST[len(LEFT_HAND_CARDS_LIST)-1]
        except:
            print("LEFT_HAND_CARDS_LIST",LEFT_HAND_CARDS_LIST)
            time.sleep(100)

        if s_site == "down":

            if len(LEFT_VICE_DEWS) > 0:
                x = LEFT_VICE_DEWS_START_X
                y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(
                    target_card_id, x, y - SMALL_MAHJONG_HEIGHT, "down")
                LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_HEIGHT, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id, LEFT_VICE_DEWS_START_X,
                                     LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_HEIGHT, "down")
                LEFT_VICE_DEWS.append(
                    [LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_HEIGHT, vdsm])
            play_multi_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

        if s_site == "right":

            if len(LEFT_VICE_DEWS) > 0:
                x = LEFT_VICE_DEWS_START_X
                y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(
                    target_card_id, x, y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id, LEFT_VICE_DEWS_START_X,
                                     LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append(
                    [LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y -
                                 SMALL_MAHJONG_HEIGHT, "down")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_HEIGHT, vdsm])
            play_multi_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

        if s_site == "up":

            if len(LEFT_VICE_DEWS) > 0:
                x = LEFT_VICE_DEWS_START_X
                y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(
                    target_card_id, x, y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id, LEFT_VICE_DEWS_START_X,
                                     LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append(
                    [LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_multi_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id, x, y -
                                 SMALL_MAHJONG_HEIGHT, "down")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_HEIGHT, vdsm])
            play_multi_sprites.add(vdsm)


def ron(site, ron_card_id):
    global IS_PLAY_SINGLE
    global play_single_init
    global RON_HAND_CARD_ID_LIST
    global RON_VICE_DEWS_ID_LIST
    global RON_CARD_ID
    global IS_WIN
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST
    global RIGHT_VICE_DEWS
    global UP_VICE_DEWS
    global LEFT_VICE_DEWS
    global IS_PLAY_SINGLE_END
    global play_single_end_init
    global WIN_TEXT
    RON_HAND_CARD_ID_LIST = []
    RON_VICE_DEWS_ID_LIST = []
    RON_CARD_ID = ron_card_id

    if site == "right":
        WIN_TEXT = "下家和"
        i = 0
        while i < len(RIGHT_HAND_CARDS_LIST):
            RON_HAND_CARD_ID_LIST.append(RIGHT_HAND_CARDS_LIST[i][1].id)
            RIGHT_HAND_CARDS_LIST[i][1].kill()
            del RIGHT_HAND_CARDS_LIST[i]

        i = 0
        while i < len(RIGHT_VICE_DEWS):
            RON_VICE_DEWS_ID_LIST.append(RIGHT_VICE_DEWS[i][3].id)
            i += 1

    if site == "up":
        WIN_TEXT = "對家和"
        i = 0
        while i < len(UP_HAND_CARDS_LIST):
            RON_HAND_CARD_ID_LIST.append(UP_HAND_CARDS_LIST[i][1].id)
            UP_HAND_CARDS_LIST[i][1].kill()
            del UP_HAND_CARDS_LIST[i]

        i = 0
        while i < len(UP_VICE_DEWS):
            RON_VICE_DEWS_ID_LIST.append(UP_VICE_DEWS[i][3].id)
            i += 1

    if site == "left":
        WIN_TEXT = "上家和"
        i = 0
        while i < len(LEFT_HAND_CARDS_LIST):
            RON_HAND_CARD_ID_LIST.append(LEFT_HAND_CARDS_LIST[i][1].id)
            LEFT_HAND_CARDS_LIST[i][1].kill()
            del LEFT_HAND_CARDS_LIST[i]

        i = 0
        while i < len(LEFT_VICE_DEWS):
            RON_VICE_DEWS_ID_LIST.append(LEFT_VICE_DEWS[i][3].id)
            i += 1

    IS_WIN = 1
    IS_PLAY_SINGLE = 0
    IS_PLAY_SINGLE_END = 1
    play_single_end_init = True


WIN_TEXT = ""


def tsumo(site, ron_card_id):
    global IS_PLAY_SINGLE
    global play_single_init
    global RON_HAND_CARD_ID_LIST
    global RON_VICE_DEWS_ID_LIST
    global RON_CARD_ID
    global IS_WIN
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST
    global RIGHT_VICE_DEWS
    global UP_VICE_DEWS
    global LEFT_VICE_DEWS
    global IS_PLAY_SINGLE_END
    global play_single_end_init
    global WIN_TEXT
    RON_HAND_CARD_ID_LIST = []
    RON_VICE_DEWS_ID_LIST = []
    RON_CARD_ID = ron_card_id

    if site == "right":
        WIN_TEXT = "下家自摸"
        i = 0
        while i < len(RIGHT_HAND_CARDS_LIST):
            RON_HAND_CARD_ID_LIST.append(RIGHT_HAND_CARDS_LIST[i][1].id)
            RIGHT_HAND_CARDS_LIST[i][1].kill()
            del RIGHT_HAND_CARDS_LIST[i]

        i = 0
        while i < len(RIGHT_VICE_DEWS):
            RON_VICE_DEWS_ID_LIST.append(RIGHT_VICE_DEWS[i][3].id)
            i += 1

    if site == "up":
        WIN_TEXT = "對家自摸"
        i = 0
        while i < len(UP_HAND_CARDS_LIST):
            RON_HAND_CARD_ID_LIST.append(UP_HAND_CARDS_LIST[i][1].id)
            UP_HAND_CARDS_LIST[i][1].kill()
            del UP_HAND_CARDS_LIST[i]

        i = 0
        while i < len(UP_VICE_DEWS):
            RON_VICE_DEWS_ID_LIST.append(UP_VICE_DEWS[i][3].id)
            i += 1

    if site == "left":
        WIN_TEXT = "上家自摸"
        i = 0
        while i < len(LEFT_HAND_CARDS_LIST):
            RON_HAND_CARD_ID_LIST.append(LEFT_HAND_CARDS_LIST[i][1].id)
            LEFT_HAND_CARDS_LIST[i][1].kill()
            del LEFT_HAND_CARDS_LIST[i]

        i = 0
        while i < len(LEFT_VICE_DEWS):
            RON_VICE_DEWS_ID_LIST.append(LEFT_VICE_DEWS[i][3].id)
            i += 1

    IS_WIN = 1
    IS_PLAY_SINGLE = 0
    play_single_init = True
    IS_PLAY_SINGLE_END = 1
    play_single_end_init = True


def pong(source_site, destination_site):
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST
    global RIGHT_VICE_DEWS
    global UP_VICE_DEWS
    global LEFT_VICE_DEWS
    global play_single_sprites
    global player_card_river
    global right_card_river
    global up_card_river
    global left_card_river
    take_out_num = 0
    target_card_id = ""

    if destination_site == "right":

        if source_site == "up":

            target_card_id = up_card_river.get_last_card_id()
            up_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            target_card_id3 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
                target_card_id3 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
                target_card_id3 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
                target_card_id3 = "Sou5"
           #print(f"right pong:{target_card_id}")

            if len(RIGHT_VICE_DEWS) > 0:
                x = RIGHT_VICE_DEWS_START_X + \
                    (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH)
                y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(target_card_id1, x, y, "up")
                RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_HEIGHT, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id1, RIGHT_VICE_DEWS_START_X + (
                    SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH), RIGHT_VICE_DEWS_START_Y, "up")
                RIGHT_VICE_DEWS.append([RIGHT_VICE_DEWS_START_X + (SMALL_MAHJONG_HEIGHT -
                                       SMALL_MAHJONG_WIDTH), RIGHT_VICE_DEWS_START_Y + SMALL_MAHJONG_HEIGHT, vdsm])
            play_single_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id3, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

        if source_site == "left":

            target_card_id = left_card_river.get_last_card_id()
            left_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            target_card_id3 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
                target_card_id3 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
                target_card_id3 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
                target_card_id3 = "Sou5"
           #print(f"right pong:{target_card_id}")

            if len(RIGHT_VICE_DEWS) > 0:
                x = RIGHT_VICE_DEWS_START_X
                y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(target_card_id1, x, y, "right")
                RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id1, RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y, "right")
                RIGHT_VICE_DEWS.append(
                    [RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y + SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X + \
                (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH)
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y, "up")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_HEIGHT, vdsm])
            play_single_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id3, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

        if source_site == "down":

            target_card_id = player_card_river.get_last_card_id()
            player_card_river.get_last_card_id()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            target_card_id3 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
                target_card_id3 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
                target_card_id3 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
                target_card_id3 = "Sou5"
           #print(f"right pong:{target_card_id}")

            if len(RIGHT_VICE_DEWS) > 0:
                x = RIGHT_VICE_DEWS_START_X
                y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(target_card_id1, x, y, "right")
                RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id1, RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y, "right")
                RIGHT_VICE_DEWS.append(
                    [RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y + SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X + \
                (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH)
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id3, x, y, "up")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_HEIGHT, vdsm])
            play_single_sprites.add(vdsm)

        i = 0
        while take_out_num < 2 and i < len(RIGHT_HAND_CARDS_LIST):
            if RIGHT_HAND_CARDS_LIST[i][1].id == target_card_id1 or RIGHT_HAND_CARDS_LIST[i][1].id == target_card_id2:
                RIGHT_HAND_CARDS_LIST[i][1].kill()
                del RIGHT_HAND_CARDS_LIST[i]
                take_out_num += 1
                i -= 1
            i += 1

    if destination_site == "up":

        if source_site == "left":

            target_card_id = left_card_river.get_last_card_id()
            left_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            target_card_id3 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
                target_card_id3 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
                target_card_id3 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
                target_card_id3 = "Sou5"
           #print(f"up pong:{target_card_id}")

            if len(UP_VICE_DEWS) > 0:
                x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
                y = UP_VICE_DEWS_START_Y
                vdsm = Small_Mahjong(target_card_id1, x, y, "left")
                UP_VICE_DEWS.append([x + SMALL_MAHJONG_HEIGHT, y, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id1, UP_VICE_DEWS_START_X, UP_VICE_DEWS_START_Y, "left")
                UP_VICE_DEWS.append(
                    [UP_VICE_DEWS_START_X + SMALL_MAHJONG_HEIGHT, UP_VICE_DEWS_START_Y, vdsm])
            play_single_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id2, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_single_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id3, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_single_sprites.add(vdsm)

        if source_site == "down":

            target_card_id = player_card_river.get_last_card_id()
            player_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            target_card_id3 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
                target_card_id3 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
                target_card_id3 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
                target_card_id3 = "Sou5"
           #print(f"up pong:{target_card_id}")

            if len(UP_VICE_DEWS) > 0:
                x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
                y = UP_VICE_DEWS_START_Y
                vdsm = Small_Mahjong(target_card_id1, x, y, "up")
                UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id1, UP_VICE_DEWS_START_X, UP_VICE_DEWS_START_Y, "up")
                UP_VICE_DEWS.append(
                    [UP_VICE_DEWS_START_X + SMALL_MAHJONG_WIDTH, UP_VICE_DEWS_START_Y, vdsm])
            play_single_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id2, x, y, "left")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_HEIGHT, y, vdsm])
            play_single_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id3, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_single_sprites.add(vdsm)

        if source_site == "right":

            target_card_id = right_card_river.get_last_card_id()
            right_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            target_card_id3 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
                target_card_id3 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
                target_card_id3 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
                target_card_id3 = "Sou5"
           #print(f"up pong:{target_card_id}")

            if len(UP_VICE_DEWS) > 0:
                x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
                y = UP_VICE_DEWS_START_Y
                vdsm = Small_Mahjong(target_card_id1, x, y, "up")
                UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id1, UP_VICE_DEWS_START_X, UP_VICE_DEWS_START_Y, "up")
                UP_VICE_DEWS.append(
                    [UP_VICE_DEWS_START_X + SMALL_MAHJONG_WIDTH, UP_VICE_DEWS_START_Y, vdsm])
            play_single_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id2, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_single_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id3, x, y, "left")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_HEIGHT, y, vdsm])
            play_single_sprites.add(vdsm)

        i = 0
        while take_out_num < 2 and i < len(UP_HAND_CARDS_LIST):
            if UP_HAND_CARDS_LIST[i][1].id == target_card_id1 or UP_HAND_CARDS_LIST[i][1].id == target_card_id2:
                UP_HAND_CARDS_LIST[i][1].kill()
                del UP_HAND_CARDS_LIST[i]
                take_out_num += 1
                i -= 1
            i += 1

    if destination_site == "left":

        if source_site == "down":

            target_card_id = player_card_river.get_last_card_id()
            player_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            target_card_id3 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
                target_card_id3 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
                target_card_id3 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
                target_card_id3 = "Sou5"
           #print(f"left pong:{target_card_id}")

            if len(LEFT_VICE_DEWS) > 0:
                x = LEFT_VICE_DEWS_START_X
                y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(
                    target_card_id1, x, y - SMALL_MAHJONG_HEIGHT, "down")
                LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_HEIGHT, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id1, LEFT_VICE_DEWS_START_X,
                                     LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_HEIGHT, "down")
                LEFT_VICE_DEWS.append(
                    [LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_HEIGHT, vdsm])
            play_single_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id3, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

        if source_site == "right":

            target_card_id = right_card_river.get_last_card_id()
            right_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            target_card_id3 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
                target_card_id3 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
                target_card_id3 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
                target_card_id3 = "Sou5"
           #print(f"left pong:{target_card_id}")

            if len(LEFT_VICE_DEWS) > 0:
                x = LEFT_VICE_DEWS_START_X
                y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(
                    target_card_id1, x, y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id1, LEFT_VICE_DEWS_START_X,
                                     LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append(
                    [LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y -
                                 SMALL_MAHJONG_HEIGHT, "down")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_HEIGHT, vdsm])
            play_single_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id3, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

        if source_site == "up":

            target_card_id = up_card_river.get_last_card_id()
            up_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            target_card_id3 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
                target_card_id3 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
                target_card_id3 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
                target_card_id3 = "Sou5"
           #print(f"left pong:{target_card_id}")

            if len(LEFT_VICE_DEWS) > 0:
                x = LEFT_VICE_DEWS_START_X
                y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(
                    target_card_id1, x, y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id1, LEFT_VICE_DEWS_START_X,
                                     LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append(
                    [LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id3, x, y -
                                 SMALL_MAHJONG_HEIGHT, "down")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_HEIGHT, vdsm])
            play_single_sprites.add(vdsm)

        i = 0
        while take_out_num < 2 and i < len(LEFT_HAND_CARDS_LIST):
            if LEFT_HAND_CARDS_LIST[i][1].id == target_card_id1 or LEFT_HAND_CARDS_LIST[i][1].id == target_card_id2:
                LEFT_HAND_CARDS_LIST[i][1].kill()
                del LEFT_HAND_CARDS_LIST[i]
                take_out_num += 1
                i -= 1
            i += 1


def kong(source_site, destination_site):  # 手裡有三張 槓他家的牌
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST
    global RIGHT_VICE_DEWS
    global UP_VICE_DEWS
    global LEFT_VICE_DEWS
    global play_single_sprites
    global player_card_river
    global right_card_river
    global up_card_river
    global left_card_river
    take_out_num = 0
    target_card_id = ""

    if destination_site == "right":

        if source_site == "up":

            target_card_id = up_card_river.get_last_card_id()
            up_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
           #print(f"right kong:{target_card_id}")

            if len(RIGHT_VICE_DEWS) > 0:
                x = RIGHT_VICE_DEWS_START_X + \
                    (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH)
                y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(target_card_id1, x, y, "up")
                RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_HEIGHT, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id1, RIGHT_VICE_DEWS_START_X + (
                    SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH), RIGHT_VICE_DEWS_START_Y, "up")
                RIGHT_VICE_DEWS.append([RIGHT_VICE_DEWS_START_X + (SMALL_MAHJONG_HEIGHT -
                                       SMALL_MAHJONG_WIDTH), RIGHT_VICE_DEWS_START_Y + SMALL_MAHJONG_HEIGHT, vdsm])
            play_single_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

        if source_site == "left":

            target_card_id = left_card_river.get_last_card_id()
            left_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
           #print(f"right kong:{target_card_id}")

            if len(RIGHT_VICE_DEWS) > 0:
                x = RIGHT_VICE_DEWS_START_X
                y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(target_card_id1, x, y, "right")
                RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id1, RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y, "right")
                RIGHT_VICE_DEWS.append(
                    [RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y + SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X + \
                (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH)
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y, "up")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_HEIGHT, vdsm])
            play_single_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

        if source_site == "down":

            target_card_id = player_card_river.get_last_card_id()
            player_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
           #print(f"right kong:{target_card_id}")

            if len(RIGHT_VICE_DEWS) > 0:
                x = RIGHT_VICE_DEWS_START_X
                y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(target_card_id1, x, y, "right")
                RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id1, RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y, "right")
                RIGHT_VICE_DEWS.append(
                    [RIGHT_VICE_DEWS_START_X, RIGHT_VICE_DEWS_START_Y + SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y, "right")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = RIGHT_VICE_DEWS_START_X + \
                (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH)
            y = RIGHT_VICE_DEWS[len(RIGHT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y, "up")
            RIGHT_VICE_DEWS.append([x, y + SMALL_MAHJONG_HEIGHT, vdsm])
            play_single_sprites.add(vdsm)

        i = 0
        while take_out_num < 3 and i < len(RIGHT_HAND_CARDS_LIST):
            if RIGHT_HAND_CARDS_LIST[i][1].id == target_card_id1 or RIGHT_HAND_CARDS_LIST[i][1].id == target_card_id2:
                RIGHT_HAND_CARDS_LIST[i][1].kill()
                del RIGHT_HAND_CARDS_LIST[i]
                take_out_num += 1
                i -= 1
            i += 1

    if destination_site == "up":

        if source_site == "left":

            target_card_id = left_card_river.get_last_card_id()
            left_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
           #print(f"up kong:{target_card_id}")

            if len(UP_VICE_DEWS) > 0:
                x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
                y = UP_VICE_DEWS_START_Y
                vdsm = Small_Mahjong(target_card_id1, x, y, "left")
                UP_VICE_DEWS.append([x + SMALL_MAHJONG_HEIGHT, y, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id1, UP_VICE_DEWS_START_X, UP_VICE_DEWS_START_Y, "left")
                UP_VICE_DEWS.append(
                    [UP_VICE_DEWS_START_X + SMALL_MAHJONG_HEIGHT, UP_VICE_DEWS_START_Y, vdsm])
            play_single_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id2, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_single_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id2, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_single_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id2, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_single_sprites.add(vdsm)

        if source_site == "down":

            target_card_id = player_card_river.get_last_card_id()
            player_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
           #print(f"up kong:{target_card_id}")

            if len(UP_VICE_DEWS) > 0:
                x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
                y = UP_VICE_DEWS_START_Y
                vdsm = Small_Mahjong(target_card_id1, x, y, "up")
                UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id1, UP_VICE_DEWS_START_X, UP_VICE_DEWS_START_Y, "up")
                UP_VICE_DEWS.append(
                    [UP_VICE_DEWS_START_X + SMALL_MAHJONG_WIDTH, UP_VICE_DEWS_START_Y, vdsm])
            play_single_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id2, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_single_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id2, x, y, "left")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_HEIGHT, y, vdsm])
            play_single_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id2, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_single_sprites.add(vdsm)

        if source_site == "right":

            target_card_id = right_card_river.get_last_card_id()
            right_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
           #print(f"up kong:{target_card_id}")

            if len(UP_VICE_DEWS) > 0:
                x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
                y = UP_VICE_DEWS_START_Y
                vdsm = Small_Mahjong(target_card_id1, x, y, "up")
                UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            else:
                vdsm = Small_Mahjong(
                    target_card_id1, UP_VICE_DEWS_START_X, UP_VICE_DEWS_START_Y, "up")
                UP_VICE_DEWS.append(
                    [UP_VICE_DEWS_START_X + SMALL_MAHJONG_WIDTH, UP_VICE_DEWS_START_Y, vdsm])
            play_single_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id2, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_single_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id2, x, y, "up")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_WIDTH, y, vdsm])
            play_single_sprites.add(vdsm)

            x = UP_VICE_DEWS[len(UP_VICE_DEWS) - 1][0]
            y = UP_VICE_DEWS_START_Y
            vdsm = Small_Mahjong(target_card_id2, x, y, "left")
            UP_VICE_DEWS.append([x + SMALL_MAHJONG_HEIGHT, y, vdsm])
            play_single_sprites.add(vdsm)

        i = 0
        while take_out_num < 3 and i < len(UP_HAND_CARDS_LIST):
            if UP_HAND_CARDS_LIST[i][1].id == target_card_id1 or UP_HAND_CARDS_LIST[i][1].id == target_card_id2:
                UP_HAND_CARDS_LIST[i][1].kill()
                del UP_HAND_CARDS_LIST[i]
                take_out_num += 1
                i -= 1
            i += 1

    if destination_site == "left":

        if source_site == "down":

            target_card_id = player_card_river.get_last_card_id()
            player_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
           #print(f"left kong:{target_card_id}")

            if len(LEFT_VICE_DEWS) > 0:
                x = LEFT_VICE_DEWS_START_X
                y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(
                    target_card_id1, x, y - SMALL_MAHJONG_HEIGHT, "down")
                LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_HEIGHT, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id1, LEFT_VICE_DEWS_START_X,
                                     LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_HEIGHT, "down")
                LEFT_VICE_DEWS.append(
                    [LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_HEIGHT, vdsm])
            play_single_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

        if source_site == "right":

            target_card_id = right_card_river.get_last_card_id()
            right_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
           #print(f"left kong:{target_card_id}")

            if len(LEFT_VICE_DEWS) > 0:
                x = LEFT_VICE_DEWS_START_X
                y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(
                    target_card_id1, x, y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id1, LEFT_VICE_DEWS_START_X,
                                     LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append(
                    [LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y -
                                 SMALL_MAHJONG_HEIGHT, "down")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_HEIGHT, vdsm])
            play_single_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

        if source_site == "up":

            target_card_id = up_card_river.get_last_card_id()
            up_card_river.del_last_card()
            target_card_id1 = target_card_id
            target_card_id2 = target_card_id
            if target_card_id == "Man5_red":
                target_card_id2 = "Man5"
            if target_card_id == "Pin5_red":
                target_card_id2 = "Pin5"
            if target_card_id == "Sou5_red":
                target_card_id2 = "Sou5"
           #print(f"left kong:{target_card_id}")

            if len(LEFT_VICE_DEWS) > 0:
                x = LEFT_VICE_DEWS_START_X
                y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
                vdsm = Small_Mahjong(
                    target_card_id1, x, y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            else:
                vdsm = Small_Mahjong(target_card_id1, LEFT_VICE_DEWS_START_X,
                                     LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, "left")
                LEFT_VICE_DEWS.append(
                    [LEFT_VICE_DEWS_START_X, LEFT_VICE_DEWS_START_Y - SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y -
                                 SMALL_MAHJONG_WIDTH, "left")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_WIDTH, vdsm])
            play_single_sprites.add(vdsm)

            x = LEFT_VICE_DEWS_START_X
            y = LEFT_VICE_DEWS[len(LEFT_VICE_DEWS) - 1][1]
            vdsm = Small_Mahjong(target_card_id2, x, y -
                                 SMALL_MAHJONG_HEIGHT, "down")
            LEFT_VICE_DEWS.append([x, y - SMALL_MAHJONG_HEIGHT, vdsm])
            play_single_sprites.add(vdsm)

        i = 0
        while take_out_num < 3 and i < len(LEFT_HAND_CARDS_LIST):
            if LEFT_HAND_CARDS_LIST[i][1].id == target_card_id1 or LEFT_HAND_CARDS_LIST[i][1].id == target_card_id2:
                LEFT_HAND_CARDS_LIST[i][1].kill()
                del LEFT_HAND_CARDS_LIST[i]
                take_out_num += 1
                i -= 1
            i += 1


def logout():
    global cSocket
    cmd = 'quit'
    cSocket.send(cmd.encode('utf-8'))
    cSocket.close()


condition_event = threading.Condition()


def login_register():
    global USERID_ERROR
    global USERNAME
    global PASSWORD_TEXT
    global CREATE_SUCCESS
    global IS_MENU
    global IS_LOGIN
    msg = ""
    while True:
        print("click")
        if login_register_flag == -1:
            msg = USERNAME + "&" + PASSWORD_TEXT + "&0"
        elif login_register_flag == 1:
            msg = USERNAME + "&" + PASSWORD_TEXT + "&1"
        login_cSocket.send(str(msg).encode('utf-8'))
        receive = login_cSocket.recv(BUFF_SIZE)
        receive = int(receive.decode('utf-8'))
        print(receive)
        if login_register_flag == -1:
            CREATE_SUCCESS = 0
            # 登入成功會回傳 3
            if receive == 3:
                # 登入成功
                IS_LOGIN = 0
                IS_MENU = 1
                break
            else:
                USERID_ERROR = receive
                

        if login_register_flag == 1:
            USERID_ERROR = 0
            # 回傳1代表成功，回傳-1代表ID重複使用
            if receive == 1:
                CREATE_SUCCESS = 1
                # init()
            else:
                CREATE_SUCCESS = -1
                
        with condition_event:
            condition_event.wait()
        


# 和牌方向 只會固定一次
ROAD_DOWN = -1
ROAD_RIGHT = 6
ROAD_UP = 6
ROAD_LEFT = 6

TRIPLET = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [2, 3, 5], [3, 4, 6], [3, 5, 6], [4, 6, 7], [5, 6, 7], [6, 7, 8], [7, 8, 9], [10, 11, 12], [11, 12, 13],
           [12, 13, 14], [12, 13, 15], [13, 14, 16], [13, 15, 16], [14, 16, 17], [
               15, 16, 17], [16, 17, 18], [17, 18, 19], [20, 21, 22],
           [21, 22, 23], [22, 23, 24], [22, 23, 25], [23, 24, 26], [23, 25, 26], [24, 26, 27], [25, 26, 27], [26, 27, 28], [27, 28, 29]]
# 判斷對子跟刻子是一樣的
SEQUENCE = [[0], [1], [2], [3], [4, 5], [6], [7], [8], [9], [10], [11], [12], [13], [14, 15], [16], [17], [18],
            [19], [20], [21], [22], [23], [24], [24, 25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36]]

TWO_SITE = [[1, 2], [2, 3], [3, 4], [3, 5], [4, 6], [5, 6], [6, 7], [7, 8], [11, 12], [12, 13], [13, 14], [13, 15], [14, 16],
            [15, 16], [16, 17], [17, 18], [21, 22], [22, 23], [23, 24], [23, 25], [24, 26], [25, 26], [26, 27], [27, 28]]
# 中張
MIDDLE = [[1, 3], [2, 4], [2, 5], [3, 6], [4, 7], [5, 7], [6, 8], [11, 13], [12, 14], [12, 15], [13, 16], [14, 17],
          [15, 17], [16, 18], [21, 23], [22, 24], [22, 25], [23, 26], [24, 27], [25, 27], [26, 28]]

# 么九
ONE_SITE = [[0, 1], [0, 2], [7, 9], [8, 9], [10, 11], [10, 12],
            [17, 19], [18, 19], [20, 21], [20, 22], [27, 29], [28, 29]]
ZERO_SITE = [[0, 1, 2], [7, 8, 9], [10, 11, 12],
             [17, 18, 19], [20, 21, 22], [27, 28, 29]]
# 三元
R_G_W = [[34], [35], [36]]
# 風牌
E_S_W_T = [[30], [31], [32], [33]]
# 一氣
ONE_TO_NINE = [[0, 1, 2, 3, 4, 6, 7, 8, 9], [0, 1, 2, 3, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 16, 17, 18, 19],
               [10, 11, 12, 13, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 26, 27, 28, 29], [20, 21, 22, 23, 25, 26, 27, 28, 29]]
ONE_TO_NINE_THREE = [[0, 1, 2], [3, 4, 6], [3, 5, 6], [7, 8, 9],
                     [10, 11, 12], [13, 14, 16], [13, 15, 16], [17, 18, 19],
                     [20, 21, 22], [23, 24, 26], [23, 25, 26], [27, 28, 29]]
MAN_ONE_TO_NINE_THREE = [[0, 1, 2], [3, 4, 6], [3, 5, 6], [7, 8, 9]]
PIN_ONE_TO_NINE_THREE = [[10, 11, 12], [
    13, 14, 16], [13, 15, 16], [17, 18, 19]]
SOU_ONE_TO_NINE_THREE = [[20, 21, 22], [
    23, 24, 26], [23, 25, 26], [27, 28, 29]]
# 三色
TRIPLE_THREE = []
# 國士
NINE_AND_NINE = [[0], [9], [10], [19], [20], [
    29], [30], [31], [32], [33], [34], [35], [36]]
# 出牌順序
ORDER = [30, 31, 32, 33, 34, 35, 36, 0, 9, 10, 19, 20, 29, 1, 8, 11, 18, 21, 28, 2, 3, 5, 4, 6, 7, 12, 13, 15, 14, 16,
         17, 22, 23, 25, 24, 26, 27]
ORDER_TEXT = ["Ton", "Nan", "Shaa", "Pei", "Chun", "Haku", "Hatsu", "Man1", "Man9", "Pin1", "Pin9", "Sou1", "Sou9", "Man2", "Man8", "Pin2", "Pin8", "Sou2", "Sou8",
              "Man3", "Man4", "Man5_red", "Man5", "Man6", "Man7", "Pin3", "Pin4", "Pin5_red", "Pin5", "Pin6", "Pin7", "Sou3", "Sou4", "Sou5_red", "Sou5", "Sou6", "Sou7", ]

THROUGHT_TYPE = 0
THROUGHT_LAST_FOUR = 0
THROUGHT_EYES = 0


def algorithm_action(site, card_id, type):  # 吃碰演算法 tpye: 1 2 吃 碰槓
    global ROAD_DOWN
    global ROAD_RIGHT
    global ROAD_UP
    global ROAD_LEFT
    list = []
    hand_card_len = 0
    last = ""
    chi_pong = []
    chi_pong_number = []
    score = 0
    score_eyes = 0  # 和牌的眼
   # print("吃碰")
   # print(card_id)

    one_nine = ["Ton", "Nan", "Shaa", "Pei", "Chun", "Haku",
                "Hatsu", "Man1", "Man9", "Pin1", "Pin9", "Sou1", "Sou9"]
    Man_name = ["Man1", "Man2", "Man3", "Man4", "Man5", "Man5_red", "Man6",
                "Man7", "Man8", "Man9", ]
    Pin_name = ["Pin1", "Pin2", "Pin3", "Pin4", "Pin5", "Pin5_red", "Pin6",
                "Pin7", "Pin8", "Pin9", ]
    Sou_name = ["Sou1", "Sou2", "Sou3", "Sou4", "Sou5", "Sou5_red", "Sou6",
                "Sou7", "Sou8", "Sou9", ]
    one_nine_number = [0, 9, 10, 19, 20, 29, 30, 31, 32, 33, 34, 35, 36]
    # 確認各家役種
    if site == "down":
        card_type = ROAD_DOWN
        hand_card_len = len(HAND_CARDS_LIST)
        last = left_card_river.get_last_card_id()
    if site == "right":
        card_type = ROAD_RIGHT
        hand_card_len = len(RIGHT_HAND_CARDS_LIST)
        last = player_card_river.get_last_card_id()
    if site == "up":
        card_type = ROAD_UP
        hand_card_len = len(UP_HAND_CARDS_LIST)
        last = right_card_river.get_last_card_id()
    if site == "left":
        card_type = ROAD_LEFT
        hand_card_len = len(LEFT_HAND_CARDS_LIST)
        last = up_card_river.get_last_card_id()
    # 吃
    if type == 1:
        # 把手牌 & 要拿下來的牌組在一起
       # print(last)
        chi_pong.append(last)
        for i in range(len(card_id)):
            chi_pong.append(card_id[i])
        chi_pong.sort()
        print(chi_pong)
        chi_pong_through = []
        for i in range(len(chi_pong)):
            chi_pong_through.append(MAHJONG_SORT_TABLE_LIST.index(chi_pong[i]))
        # 只有手牌
        for i in range(len(card_id)):
            chi_pong_number.append(MAHJONG_SORT_TABLE_LIST.index(card_id[i]))
        # print(f"手牌 要吃的號碼{chi_pong_number}")
        # print(f"走的役種 {card_type}")

        # 門清 -1 7 國士 0 對對 2 七對 3 不吃
        if card_type == -1 or card_type == 7 or card_type == 0 or card_type == 2 or card_type == 3:
            return False
        # 三元 1
        elif card_type == 1:
            if hand_card_len > 4:
                return True
            else:
                return False
        # 混全 4
        elif card_type == 4:
            for i in range(len(chi_pong)):
                if not(chi_pong[i] in one_nine):
                    return False
            # 把手牌 轉成數字找出來
            if site == "down":
                temp = []
                hand_card_number_list = []
                for i in range(len(HAND_CARDS_LIST)):
                    hand_card_number_list.append(
                        MAHJONG_SORT_TABLE_LIST.index(HAND_CARDS_LIST[i][1].id))
            if site == "right":
                temp = []
                hand_card_number_list = []
                for i in range(len(RIGHT_HAND_CARDS_LIST)):
                    hand_card_number_list.append(
                        MAHJONG_SORT_TABLE_LIST.index(RIGHT_HAND_CARDS_LIST[i][1].id))
            if site == "up":
                temp = []
                hand_card_number_list = []
                for i in range(len(UP_HAND_CARDS_LIST)):
                    hand_card_number_list.append(
                        MAHJONG_SORT_TABLE_LIST.index(UP_HAND_CARDS_LIST[i][1].id))
            if site == "left":
                temp = []
                hand_card_number_list = []
                for i in range(len(LEFT_HAND_CARDS_LIST)):
                    hand_card_number_list.append(
                        MAHJONG_SORT_TABLE_LIST.index(LEFT_HAND_CARDS_LIST[i][1].id))
            # print(f"手牌號碼{hand_card_number_list}")

            # 123 or 789 順
            for x in range(len(ZERO_SITE)):
                # y 確認內容是否符合
                for y in range(len(ZERO_SITE[x])):
                    if ZERO_SITE[x][y] in hand_card_number_list:
                        list.append(
                            hand_card_number_list.index(ZERO_SITE[x][y]))
                if len(list) == 3:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    hand_card_number_list[list[2]] = -1
                else:
                    pass
                list = []
            # 刻子
            for x in range(len(NINE_AND_NINE)):
                # y 確認內容是否符合
                for y in NINE_AND_NINE[x]:
                    temp = [i for i, find in enumerate(
                        hand_card_number_list) if find == y]
                    for z in range(len(temp)):
                        list.append(temp[z])
                if len(list) >= 3:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    hand_card_number_list[list[2]] = -1
                else:
                    pass
                list = []

            # 如果 要吃的手牌 已經被順or刻子用掉 則不吃
            # print(f"手牌號碼 消除順&刻{hand_card_number_list}")
            for i in range(len(chi_pong_number)):
                if chi_pong_number[i] in hand_card_number_list:  # True 確定要拿
                    hand_card_number_list[hand_card_number_list.index(
                        chi_pong_number[i])] = -1
                    pass
                else:
                    return False
            # 對子 數眼
            for x in range(len(NINE_AND_NINE)):
                # y 確認內容是否符合
                for y in NINE_AND_NINE[x]:
                    temp = [i for i, find in enumerate(
                        hand_card_number_list) if find == y]
                    for z in range(len(temp)):
                        list.append(temp[z])
                if len(list) == 2:
                    score_eyes = score_eyes + 1
                else:
                    pass
                list = []
            if score_eyes >= 1:  # 吃完還有眼 ok
                return True
            else:
                return False  # 吃完沒有眼 false
        # 一氣 5
        elif card_type == 5:
            # 把手牌 轉成數字找出來
            if site == "down":
                temp = []
                hand_card_number_list = []
                for i in range(len(HAND_CARDS_LIST)):
                    hand_card_number_list.append(
                        MAHJONG_SORT_TABLE_LIST.index(HAND_CARDS_LIST[i][1].id))
            if site == "right":
                temp = []
                hand_card_number_list = []
                for i in range(len(RIGHT_HAND_CARDS_LIST)):
                    hand_card_number_list.append(
                        MAHJONG_SORT_TABLE_LIST.index(RIGHT_HAND_CARDS_LIST[i][1].id))
            if site == "up":
                temp = []
                hand_card_number_list = []
                for i in range(len(UP_HAND_CARDS_LIST)):
                    hand_card_number_list.append(
                        MAHJONG_SORT_TABLE_LIST.index(UP_HAND_CARDS_LIST[i][1].id))
            if site == "left":
                temp = []
                hand_card_number_list = []
                for i in range(len(LEFT_HAND_CARDS_LIST)):
                    hand_card_number_list.append(
                        MAHJONG_SORT_TABLE_LIST.index(LEFT_HAND_CARDS_LIST[i][1].id))
           # print(f"手牌號碼{hand_card_number_list}")
            # 先把么九牌拿掉 才計算順 & 刻
            for i in range(len(hand_card_number_list)):
                if hand_card_number_list[i] in one_nine_number:
                    hand_card_number_list[i] = -1
           # print(f"手牌號碼(拿掉么九){hand_card_number_list}")
            # 順子
            for x in range(len(ONE_TO_NINE_THREE)):
                # y 確認內容是否符合
                for z in range(3):
                    for y in range(len(ONE_TO_NINE_THREE[x])):
                        if ONE_TO_NINE_THREE[x][y] in hand_card_number_list:
                            list.append(
                                hand_card_number_list.index(ONE_TO_NINE_THREE[x][y]))
                    if len(list) >= 3:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        hand_card_number_list[list[2]] = -1
                    else:
                        pass
                    list = []
            if THROUGHT_TYPE == 1:
                if chi_pong in MAN_ONE_TO_NINE_THREE:
                    for i in range(len(chi_pong_number)):
                        if chi_pong_number[i] in hand_card_number_list:
                            # print("在")
                            pass
                        else:
                            return False
                    return True
            if THROUGHT_TYPE == 2:
                if chi_pong in PIN_ONE_TO_NINE_THREE:
                    for i in range(len(chi_pong_number)):
                        if chi_pong_number[i] in hand_card_number_list:
                            # print("在")
                            pass
                        else:
                            return False
                    return True
            if THROUGHT_TYPE == 3:
                if chi_pong in SOU_ONE_TO_NINE_THREE:
                    for i in range(len(chi_pong_number)):
                        if chi_pong_number[i] in hand_card_number_list:
                            # print("在")
                            pass
                        else:
                            return False
                    return True
            # 不是 13 46 79 的吃
            if (THROUGHT_LAST_FOUR == 2 and THROUGHT_EYES >= 1):  # 可以吃碰一次 且 多一個的眼 就可以吃
                THROUGHT_LAST_FOUR = THROUGHT_LAST_FOUR - 1
                return True
            else:
                return False
        # 段么 6 可以吃碰 么九以外
        elif card_type == 6:
            for i in range(len(chi_pong)):
                if chi_pong[i] in one_nine:
                    return False
            # 把手牌 轉成數字找出來
            if site == "down":
                temp = []
                hand_card_number_list = []
                for i in range(len(HAND_CARDS_LIST)):
                    hand_card_number_list.append(
                        MAHJONG_SORT_TABLE_LIST.index(HAND_CARDS_LIST[i][1].id))
            if site == "right":
                temp = []
                hand_card_number_list = []
                for i in range(len(RIGHT_HAND_CARDS_LIST)):
                    hand_card_number_list.append(
                        MAHJONG_SORT_TABLE_LIST.index(RIGHT_HAND_CARDS_LIST[i][1].id))
            if site == "up":
                temp = []
                hand_card_number_list = []
                for i in range(len(UP_HAND_CARDS_LIST)):
                    hand_card_number_list.append(
                        MAHJONG_SORT_TABLE_LIST.index(UP_HAND_CARDS_LIST[i][1].id))
            if site == "left":
                temp = []
                hand_card_number_list = []
                for i in range(len(LEFT_HAND_CARDS_LIST)):
                    hand_card_number_list.append(
                        MAHJONG_SORT_TABLE_LIST.index(LEFT_HAND_CARDS_LIST[i][1].id))
           # print(f"手牌號碼{hand_card_number_list}")
            # 先把么九牌拿掉 才計算順 & 刻
            for i in range(len(hand_card_number_list)):
                if hand_card_number_list[i] in one_nine_number:
                    hand_card_number_list[i] = -1
           # print(f"手牌號碼(拿掉么九){hand_card_number_list}")
            # 順子
            for x in range(len(TRIPLET)):
                # y 確認內容是否符合
                for z in range(3):
                    for y in range(len(TRIPLET[x])):
                        if TRIPLET[x][y] in hand_card_number_list:
                            list.append(
                                hand_card_number_list.index(TRIPLET[x][y]))
                    if len(list) >= 3:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        hand_card_number_list[list[2]] = -1
                        score = score + 3
                    else:
                        pass
                    list = []
            # 刻子
            for x in range(len(SEQUENCE)):
                # y 確認內容是否符合
                for y in SEQUENCE[x]:
                    temp = [i for i, find in enumerate(
                        hand_card_number_list) if find == y]
                    for z in range(len(temp)):
                        list.append(temp[z])
                if len(list) == 3:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    hand_card_number_list[list[2]] = -1
                    score = score + 3
                elif len(list) == 4:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    hand_card_number_list[list[3]] = -1
                    score = score + 3
                else:
                    pass
                list = []

            # 如果 要吃的手牌 已經被順or刻子用掉 則不吃
            # print(f"手牌號碼 消除順&刻{hand_card_number_list}")
            for i in range(len(chi_pong_number)):
                if chi_pong_number[i] in hand_card_number_list:
                   # print("在")
                    pass
                else:
                    return False
            return True
    # 碰
    if type == 2:
        # 門清 -1 7 國士 0 七對 3 不碰
        if card_type == -1 or card_type == 7 or card_type == 0 or card_type == 3:
            return False
        # 三元
        elif card_type == 1:
            if hand_card_len > 4:
                return True
            else:
                return False
        # 對對 只能碰 槓
        elif card_type == 2:
            return True
        # 混全
        elif card_type == 4:
            if card_id in one_nine:
               # print("碰")
                return True
            else:
               # print("不碰")
                return False
        # 一氣
        elif card_type == 5:
            if THROUGHT_TYPE == 1:
                if card_id in Man_name:
                    return False
            if THROUGHT_TYPE == 2:
                if card_id in Pin_name:
                    return False
            if THROUGHT_TYPE == 3:
                if card_id in Sou_name:
                    return False
            if (THROUGHT_LAST_FOUR == 2 and THROUGHT_EYES > 1):  # 可以吃碰一次 且 多餘一個的眼 就可以碰
                THROUGHT_LAST_FOUR = THROUGHT_LAST_FOUR - 1
                return True
            else:
                return False
        # 段么 可以吃碰 么九以外
        elif card_type == 6:
            if card_id in one_nine:
               # print("不碰")
                return False
            else:
               # print("碰")
                return True


def algorithm(site, draw):  # 演算法
    # 和牌方向
    global ROAD_DOWN
    global ROAD_RIGHT
    global ROAD_UP
    global ROAD_LEFT
    global THROUGHT_TYPE
    global THROUGHT_LAST_FOUR
    global THROUGHT_EYES
    road = -1
    # 存被找到的牌
    list = []
    hand_card_number_list = []
    break_down_hand_card_pairs = []  # 拆對
    break_down_hand_card_two = []  # 拆邊
    break_down_hand_card_small = []  # 拆 中張 or 邊張
    no_one_nine = []  # 出牌 斷么
    only_pairs = []  # 出牌 對對 七對
    output_chanta = []  # 出牌 混全
    output_chanta_one_nine = []  # 出牌 混全 么九 輪次較後
    output_thirteen_orphans = []  # 出牌 國士
    output_thirteen_orphans_one_nine = []  # 出牌 國士 么九 輪次較後
    # 門清可出的牌
    Men_Qing_list = []
    output_index = ""
    output_text = ""
    output_id = 0

    score = 0  # 分數
    score_eyes = 0  # 聽牌眼
    dragons_two = 0  # 三元 對
    dragons_three = 0  # 三元 刻
    origin_dragons_two = 0  # 原本手上的三元對
    origin_dragons_three = 0  # 原本手上的三元刻
    pairs = 0  # 對對
    chanta = 0  # 混全
    through = 0  # 一氣
    Sanshoku = 0  # 三色
    thirteen_orphans = 0  # 國士

    nine = 0  # 種九種牌
    for count in range(7):
        # 把手排轉數字 hand_card_number_list
        if site == "down":
            temp = []
            hand_card_number_list = []
            for i in range(len(HAND_CARDS_LIST)):
                hand_card_number_list.append(
                    MAHJONG_SORT_TABLE_LIST.index(HAND_CARDS_LIST[i][1].id))
        if site == "right":
            temp = []
            hand_card_number_list = []
            for i in range(len(RIGHT_HAND_CARDS_LIST)):
                hand_card_number_list.append(
                    MAHJONG_SORT_TABLE_LIST.index(RIGHT_HAND_CARDS_LIST[i][1].id))
        if site == "up":
            temp = []
            hand_card_number_list = []
            for i in range(len(UP_HAND_CARDS_LIST)):
                hand_card_number_list.append(
                    MAHJONG_SORT_TABLE_LIST.index(UP_HAND_CARDS_LIST[i][1].id))
        if site == "left":
            temp = []
            hand_card_number_list = []
            for i in range(len(LEFT_HAND_CARDS_LIST)):
                hand_card_number_list.append(
                    MAHJONG_SORT_TABLE_LIST.index(LEFT_HAND_CARDS_LIST[i][1].id))
        # 如果有抽牌 加入手牌
        if draw != "":
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(draw))
        # 把抽到的牌 加入手牌一起評分
        hand_card_number_list.sort()
        # 門清平分
        if count == 0:
            # 順子
            score_eyes = 0
            break_down_hand_card_two = []
            break_down_hand_card_small = []
            break_down_hand_card_pairs = []
            for x in range(len(TRIPLET)):
                # y 確認內容是否符合
                for z in range(3):
                    for y in range(len(TRIPLET[x])):
                        if TRIPLET[x][y] in hand_card_number_list:
                            list.append(
                                hand_card_number_list.index(TRIPLET[x][y]))
                    if len(list) >= 3:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        hand_card_number_list[list[2]] = -1
                        score = score + 3
                    else:
                        pass
                    list = []

            # 刻子
            for x in range(len(SEQUENCE)):
                # y 確認內容是否符合
                for y in SEQUENCE[x]:
                    temp = [i for i, find in enumerate(
                        hand_card_number_list) if find == y]
                    for z in range(len(temp)):
                        list.append(temp[z])
                if len(list) == 3:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    hand_card_number_list[list[2]] = -1
                    score = score + 3
                elif len(list) == 4:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    hand_card_number_list[list[3]] = -1
                    score = score + 3
                else:
                    pass
                list = []
            # 可以拆牌的方向
            for x in range(len(hand_card_number_list)):
                if hand_card_number_list[x] != -1:
                    break_down_hand_card_two.append(hand_card_number_list[x])
            # 兩邊
            for x in range(len(TWO_SITE)):
                # y 確認內容是否符合
                for y in range(len(TWO_SITE[x])):
                    if TWO_SITE[x][y] in hand_card_number_list:
                        list.append(
                            hand_card_number_list.index(TWO_SITE[x][y]))
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    score = score + 2
                else:
                    pass
                list = []
            # 可以拆牌的方向
            for x in range(len(hand_card_number_list)):
                if hand_card_number_list[x] != -1:
                    break_down_hand_card_pairs.append(hand_card_number_list[x])
            # 對子
            for x in range(len(SEQUENCE)):
                # y 確認內容是否符合
                for y in SEQUENCE[x]:
                    temp = [i for i, find in enumerate(
                        hand_card_number_list) if find == y]
                    for z in range(len(temp)):
                        list.append(temp[z])
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    score = score + 2
                    score_eyes = score_eyes + 1
                else:
                    pass
                list = []
            
            for x in range(len(hand_card_number_list)):
                if hand_card_number_list[x] != -1:
                    break_down_hand_card_small.append(hand_card_number_list[x])
            # 中張 & 邊張
            for x in range(len(MIDDLE)):
                # y 確認內容是否符合
                for y in range(len(MIDDLE[x])):
                    if MIDDLE[x][y] in hand_card_number_list:
                        list.append(
                            hand_card_number_list.index(MIDDLE[x][y]))
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    score = score + 1
                else:
                    pass
                list = []
            for x in range(len(ONE_SITE)):
                # y 確認內容是否符合
                for y in range(len(ONE_SITE[x])):
                    if ONE_SITE[x][y] in hand_card_number_list:
                        list.append(
                            hand_card_number_list.index(ONE_SITE[x][y]))
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    score = score + 1
                else:
                    pass
                list = []
            for i in range(len(hand_card_number_list)):
                if hand_card_number_list[i] != -1:
                    Men_Qing_list.append(i)
        # 三元 & 風 (風還沒做)
        if count == 1:
            for x in range(len(R_G_W)):
                # y 確認內容是否符合
                for y in R_G_W[x]:

                    temp = [i for i, find in enumerate(
                        hand_card_number_list) if find == y]
                    for z in range(len(temp)):
                        list.append(temp[z])

                if len(list) == 2:
                    dragons_two = dragons_two + 1
                if len(list) >= 3:
                    dragons_three = dragons_three + 1
                else:
                    pass
                # print(temp)
                # print(list)
                list = []
            if origin_dragons_two == 0:
                origin_dragons_two = dragons_two
            if origin_dragons_three == 0:
                origin_dragons_three = dragons_three
        # 對對
        if count == 2:
            for x in range(len(SEQUENCE)):
                # y 確認內容是否符合
                for y in SEQUENCE[x]:
                    temp = [i for i, find in enumerate(
                        hand_card_number_list) if find == y]
                    for z in range(len(temp)):
                        list.append(temp[z])
                if len(list) == 2:
                    pairs = pairs + 1
                else:
                    pass
                list = []
        # 混全
        if count == 3:
            break_down_hand_card_pairs = []  # 拆對
            break_down_hand_card_two = []  # 拆邊
            break_down_hand_card_small = []  # 拆 中張 or 邊張
            # 123 or 789 順
            for x in range(len(ZERO_SITE)):
                # y 確認內容是否符合
                for y in range(len(ZERO_SITE[x])):
                    if ZERO_SITE[x][y] in hand_card_number_list:
                        list.append(
                            hand_card_number_list.index(ZERO_SITE[x][y]))
                if len(list) == 3:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    hand_card_number_list[list[2]] = -1
                    chanta = chanta + 3
                else:
                    pass
                list = []
            # 刻子 么九刻
            for x in range(len(NINE_AND_NINE)):
                # y 確認內容是否符合
                for y in NINE_AND_NINE[x]:
                    temp = [i for i, find in enumerate(
                        hand_card_number_list) if find == y]
                    for z in range(len(temp)):
                        list.append(temp[z])
                if len(list) >= 3:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    hand_card_number_list[list[2]] = -1
                else:
                    pass
                list = []
            # 對子 么九對
            for x in range(len(NINE_AND_NINE)):
                # y 確認內容是否符合
                for y in NINE_AND_NINE[x]:
                    temp = [i for i, find in enumerate(
                        hand_card_number_list) if find == y]
                    for z in range(len(temp)):
                        list.append(temp[z])
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    score_eyes = score_eyes + 1
                else:
                    pass
                list = []
            # 等一張
            for x in range(len(ONE_SITE)):
                # y 確認內容是否符合
                for y in range(len(ONE_SITE[x])):
                    if ONE_SITE[x][y] in hand_card_number_list:
                        list.append(
                            hand_card_number_list.index(ONE_SITE[x][y]))
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    chanta = chanta + 2
                else:
                    pass
                list = []

            for x in range(len(hand_card_number_list)):
                if hand_card_number_list[x] != -1:
                    if hand_card_number_list[x] in NINE_AND_NINE:
                        output_chanta_one_nine.append(hand_card_number_list[x])
                    else:
                        output_chanta.append(hand_card_number_list[x])
        # 一氣
        if count == 4:
            for x in range(len(ONE_TO_NINE)):
                # y 確認內容是否符合
                for y in range(len(ONE_TO_NINE[x])):
                    if ONE_TO_NINE[x][y] in hand_card_number_list:
                        list.append(hand_card_number_list.index(
                            ONE_TO_NINE[x][y]))
                if len(list) >= 7:
                    through = 1
                    if 9 >= (hand_card_number_list[list[0]]) >= 10:
                        THROUGHT_TYPE = 1
                    elif 19 >= (hand_card_number_list[list[0]]) >= 10:
                        THROUGHT_TYPE = 2
                    elif 29 >= (hand_card_number_list[list[0]]) >= 20:
                        THROUGHT_TYPE = 3
                    for zero in range(len(list)):
                        hand_card_number_list[list[zero]] = -1
                    # 額外一組 順
                    break_down_hand_card_pairs = []  # 拆對
                    break_down_hand_card_two = []  # 拆邊
                    break_down_hand_card_small = []  # 拆 中張 or 邊張
                    # 額外一組 順
                    if THROUGHT_LAST_FOUR == 2:
                        for x in range(len(ONE_TO_NINE_THREE)):
                            # y 確認內容是否符合
                            for z in range(3):
                                for y in range(len(ONE_TO_NINE_THREE[x])):
                                    if ONE_TO_NINE_THREE[x][y] in hand_card_number_list:
                                        list.append(
                                            hand_card_number_list.index(ONE_TO_NINE_THREE[x][y]))
                                if len(list) >= 3:
                                    hand_card_number_list[list[0]] = -1
                                    hand_card_number_list[list[1]] = -1
                                    hand_card_number_list[list[2]] = -1
                                    THROUGHT_LAST_FOUR = 1  # 不能再吃碰
                                    break
                                else:
                                    pass
                                list = []
                    # 額外一組 刻
                    if THROUGHT_LAST_FOUR == 2:
                        # 刻子
                        for x in range(len(SEQUENCE)):
                            # y 確認內容是否符合
                            for y in SEQUENCE[x]:
                                temp = [i for i, find in enumerate(
                                    hand_card_number_list) if find == y]
                                for z in range(len(temp)):
                                    list.append(temp[z])
                            if len(list) == 3:
                                hand_card_number_list[list[0]] = -1
                                hand_card_number_list[list[1]] = -1
                                hand_card_number_list[list[2]] = -1
                                THROUGHT_LAST_FOUR = 1  # 不能再吃碰
                                break
                            elif len(list) == 4:
                                hand_card_number_list[list[0]] = -1
                                hand_card_number_list[list[1]] = -1
                                hand_card_number_list[list[3]] = -1
                                THROUGHT_LAST_FOUR = 1  # 不能再吃碰
                                break
                            else:
                                pass
                            list = []
                    # 可以拆牌的方向
                    for x in range(len(hand_card_number_list)):
                        if hand_card_number_list[x] != -1:
                            break_down_hand_card_pairs.append(
                                hand_card_number_list[x])
                    # 對子
                    for x in range(len(SEQUENCE)):
                        # y 確認內容是否符合
                        for y in SEQUENCE[x]:
                            temp = [i for i, find in enumerate(
                                hand_card_number_list) if find == y]
                            for z in range(len(temp)):
                                list.append(temp[z])
                        if len(list) == 2:
                            hand_card_number_list[list[0]] = -1
                            hand_card_number_list[list[1]] = -1
                            score_eyes = score_eyes + 1
                        else:
                            pass
                        list = []
                    THROUGHT_EYES = score_eyes
                    # 可以拆牌的方向
                    for x in range(len(hand_card_number_list)):
                        if hand_card_number_list[x] != -1:
                            break_down_hand_card_two.append(
                                hand_card_number_list[x])
                    # 兩邊
                    for x in range(len(TWO_SITE)):
                        # y 確認內容是否符合
                        for y in range(len(TWO_SITE[x])):
                            if TWO_SITE[x][y] in hand_card_number_list:
                                list.append(
                                    hand_card_number_list.index(TWO_SITE[x][y]))
                        if len(list) == 2:
                            hand_card_number_list[list[0]] = -1
                            hand_card_number_list[list[1]] = -1
                        else:
                            pass
                        list = []
                    # 可以拆牌的方向
                    for x in range(len(hand_card_number_list)):
                        if hand_card_number_list[x] != -1:
                            break_down_hand_card_small.append(
                                hand_card_number_list[x])
                else:
                    pass
                list = []
        # 三色
        if count == 5:
            pass
        # 國士
        if count == 6:
            no_one_nine = []  # 斷么
            for x in range(len(NINE_AND_NINE)):
                # y 確認內容是否符合
                for y in range(len(NINE_AND_NINE[x])):
                    if NINE_AND_NINE[x][y] in hand_card_number_list:
                        list.append(
                            hand_card_number_list.index(NINE_AND_NINE[x][y]))
                        no_one_nine.append(NINE_AND_NINE[x][y])
                        nine = nine + 1
                else:
                    pass
                list = []
            if nine >= 9:
                thirteen_orphans = 1
    #print("*** " + site + " ***")
    #print(f"分數(滿分{len(hand_card_number_list)})：" + str(score))
    # print("三元 刻(滿分3)：" + str(dragons_three))
    # print("對對(滿分6)：" + str(pairs))
    # print(f"混全(滿分{len(hand_card_number_list)})：" + str(chanta))
    # print("一氣(滿分1)：" + str(through))
    #print("國士(滿分1)：" + str(thirteen_orphans))
    # print("幾種九牌：" + str(nine))

    # 決定和牌役種
    if 70 > len(CARD_MOUNTAIN) > 55:
        if site == "down":
            if thirteen_orphans == 1:
                ROAD_DOWN = 0
            elif dragons_two > 0:
                ROAD_DOWN = 1
            elif pairs >= 4:
                ROAD_DOWN = 2
            elif pairs >= 5:
                ROAD_DOWN = 3
            elif chanta >= 10:
                pass
            elif through == 1:
                ROAD_DOWN = 5
            elif nine < 4 and score < 7:
                ROAD_DOWN = 6
            if score >= 10:
                ROAD_DOWN = 7
            #print("役種：" + str(ROAD_DOWN))
        if site == "right":
            if thirteen_orphans == 1:
                ROAD_RIGHT = 0
            elif dragons_two > 0:
                ROAD_RIGHT = 1
            elif pairs >= 4:
                ROAD_RIGHT = 2
            elif pairs >= 5:
                ROAD_RIGHT = 3
            elif chanta >= 10:
                pass
            elif through == 1:
                ROAD_RIGHT = 5
            elif nine < 4 and score < 7:
                ROAD_RIGHT = 6
            if score >= 10:
                ROAD_RIGHT = 7
        if site == "up":
            if thirteen_orphans == 1:
                ROAD_UP = 0
            elif dragons_two > 0:
                ROAD_UP = 1
            elif pairs >= 4:
                ROAD_UP = 2
            elif pairs >= 5:
                ROAD_UP = 3
            elif chanta >= 10:
                pass
            elif through == 1:
                ROAD_UP = 5
            elif nine < 4 and score < 7:
                ROAD_UP = 6
            if score >= 10:
                ROAD_UP = 7
        if site == "left":
            if thirteen_orphans == 1:
                ROAD_LEFT = 0
            elif dragons_two > 0:
                ROAD_LEFT = 1
            elif pairs >= 4:
                ROAD_LEFT = 2
            elif pairs >= 5:
                ROAD_LEFT = 3
            elif chanta >= 10:
                pass
            elif through == 1:
                ROAD_LEFT = 5
            elif nine < 4 and score < 7:
                ROAD_LEFT = 6
            if score >= 10:
                ROAD_LEFT = 7
    if site == "down":
        road = -1
    if site == "right":
        road = -1  # ROAD_RIGHT
    if site == "up":
        road = -1  # ROAD_UP
    if site == "left":
        road = -1  # ROAD_LEFT
    if site == "down":
        for i in range(len(HAND_CARDS_LIST)):
            pass
           # print(HAND_CARDS_LIST[i][1].id)

    # 不做讓牌分辨低的行為 計算丟牌 把數字(0~36)存到output_id
    # 把手排轉數字 hand_card_number_list
    if site == "down":
        temp = []
        hand_card_number_list = []
        for i in range(len(HAND_CARDS_LIST)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(HAND_CARDS_LIST[i][1].id))
    if site == "right":
        temp = []
        hand_card_number_list = []
        for i in range(len(RIGHT_HAND_CARDS_LIST)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(RIGHT_HAND_CARDS_LIST[i][1].id))
    if site == "up":
        temp = []
        hand_card_number_list = []
        for i in range(len(UP_HAND_CARDS_LIST)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(UP_HAND_CARDS_LIST[i][1].id))
    if site == "left":
        temp = []
        hand_card_number_list = []
        for i in range(len(LEFT_HAND_CARDS_LIST)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(LEFT_HAND_CARDS_LIST[i][1].id))
    # 如果有抽牌 加入手牌
    if draw != "":
        hand_card_number_list.append(
            MAHJONG_SORT_TABLE_LIST.index(draw))
    print()
    print(site)
    print(road)
    for i in range(len(hand_card_number_list)):
        print(hand_card_number_list[i], end=" ")
    # 國 0
    if road == 0:
        for x in range(len(NINE_AND_NINE)):
            # y 確認內容是否符合
            for y in range(len(NINE_AND_NINE[x])):
                if NINE_AND_NINE[x][y] in hand_card_number_list:
                    list.append(hand_card_number_list.index(
                        NINE_AND_NINE[x][y]))
                    hand_card_number_list[list[0]] = -1
            else:
                pass
            list = []
        print(hand_card_number_list)
        for i in range(len(hand_card_number_list)):
            if hand_card_number_list[i] != -1 and hand_card_number_list[i] not in NINE_AND_NINE:
                output_thirteen_orphans.append(hand_card_number_list[i])
        for i in range(len(hand_card_number_list)):
            if hand_card_number_list[i] != -1 and hand_card_number_list[i] in NINE_AND_NINE:
                output_thirteen_orphans_one_nine.append(
                    hand_card_number_list[i])

        print(output_thirteen_orphans)
        print(output_thirteen_orphans_one_nine)
        if len(output_thirteen_orphans) > 0:
           # print("(斷么)")
           # print(only_pairs)
            output_index = choice(output_thirteen_orphans)
            output_text = MAHJONG_SORT_TABLE_LIST[output_index]
           # print(output_text)
            output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
        elif len(output_thirteen_orphans_one_nine) > 0:
           # print("(斷么)")
           # print(only_pairs)
            output_index = choice(output_thirteen_orphans_one_nine)
            output_text = MAHJONG_SORT_TABLE_LIST[output_index]
           # print(output_text)
            output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
        else:
            pass
    # 三元 1
    elif road == 1:
        output = []
        # 三元對不再手上 or 三元刻
        if dragons_three > 0 or origin_dragons_two > dragons_two or origin_dragons_three > dragons_three:
            # print("有沒有眼：" + str(score_eyes))
            if score_eyes == 0:
                Men_Qing_list = []
                # 刻子
                break_down_hand_card_two = []
                break_down_hand_card_small = []
                break_down_hand_card_pairs = []
                for x in range(len(SEQUENCE)):
                    # y 確認內容是否符合
                    for y in SEQUENCE[x]:
                        temp = [i for i, find in enumerate(
                            hand_card_number_list) if find == y]
                        for z in range(len(temp)):
                            list.append(temp[z])
                    if len(list) == 3:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        hand_card_number_list[list[2]] = -1
                        score = score + 3
                    elif len(list) == 4:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        hand_card_number_list[list[3]] = -1
                        score = score + 3
                    else:
                        pass
                    list = []

                # 順子
                for x in range(len(TRIPLET)):
                    # y 確認內容是否符合
                    for z in range(3):
                        for y in range(len(TRIPLET[x])):
                            if TRIPLET[x][y] in hand_card_number_list:
                                list.append(
                                    hand_card_number_list.index(TRIPLET[x][y]))
                        if len(list) >= 3:
                            hand_card_number_list[list[0]] = -1
                            hand_card_number_list[list[1]] = -1
                            hand_card_number_list[list[2]] = -1
                            score = score + 3
                        else:
                            pass
                        list = []

                # 可以拆牌的方向
                for x in range(len(hand_card_number_list)):
                    if hand_card_number_list[x] != -1:
                        break_down_hand_card_two.append(
                            hand_card_number_list[x])
                # 對子
                for x in range(len(SEQUENCE)):
                    # y 確認內容是否符合
                    for y in SEQUENCE[x]:
                        temp = [i for i, find in enumerate(
                            hand_card_number_list) if find == y]
                        for z in range(len(temp)):
                            list.append(temp[z])
                    if len(list) == 2:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        score = score + 2
                        score_eyes = score_eyes + 1
                    else:
                        pass
                    list = []

                for x in range(len(hand_card_number_list)):
                    if hand_card_number_list[x] != -1:
                        break_down_hand_card_small.append(
                            hand_card_number_list[x])
                # 兩邊
                for x in range(len(TWO_SITE)):
                    # y 確認內容是否符合
                    for y in range(len(TWO_SITE[x])):
                        if TWO_SITE[x][y] in hand_card_number_list:
                            list.append(
                                hand_card_number_list.index(TWO_SITE[x][y]))
                    if len(list) == 2:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        score = score + 2
                    else:
                        pass
                    list = []

                # 可以拆牌的方向
                for x in range(len(hand_card_number_list)):
                    if hand_card_number_list[x] != -1:
                        break_down_hand_card_pairs.append(
                            hand_card_number_list[x])

                # 中張 & 邊張
                for x in range(len(MIDDLE)):
                    # y 確認內容是否符合
                    for y in range(len(MIDDLE[x])):
                        if MIDDLE[x][y] in hand_card_number_list:
                            list.append(
                                hand_card_number_list.index(MIDDLE[x][y]))
                    if len(list) == 2:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        score = score + 1
                    else:
                        pass
                    list = []
                for x in range(len(ONE_SITE)):
                    # y 確認內容是否符合
                    for y in range(len(ONE_SITE[x])):
                        if ONE_SITE[x][y] in hand_card_number_list:
                            list.append(
                                hand_card_number_list.index(ONE_SITE[x][y]))
                    if len(list) == 2:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        score = score + 1
                    else:
                        pass
                    list = []
                for i in range(len(hand_card_number_list)):
                    if hand_card_number_list[i] != -1:
                        Men_Qing_list.append(i)
                # 出牌
                if len(Men_Qing_list) > 0:
                    for i in range(len(Men_Qing_list)):
                        output.append(ORDER.index(
                            hand_card_number_list[Men_Qing_list[i]]))
                    output.sort()
                    # print("plan A 孤張")
                    # print(output)
                    output_text = ORDER_TEXT[output[0]]
                    # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                elif len(break_down_hand_card_small) > 0:
                    for i in range(len(break_down_hand_card_small)):
                        output.append(break_down_hand_card_small[i])
                    # print("plan B 中張or邊張")
                    # print(break_down_hand_card_small)
                    output_index = choice(output)
                    output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                    # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                elif len(break_down_hand_card_pairs) > 2:
                    for i in range(len(break_down_hand_card_pairs)):
                        output.append(break_down_hand_card_pairs[i])
                    # print("plan C 對子(兩組以上)")
                    # print(break_down_hand_card_pairs)
                    output_index = choice(output)
                    output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                    # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                elif len(break_down_hand_card_two) > 0:
                    for i in range(len(break_down_hand_card_two)):
                        if break_down_hand_card_two[i] in break_down_hand_card_pairs:
                            pass
                        else:
                            output.append(break_down_hand_card_two[i])
                    # print("plan D 兩邊")
                    # print(break_down_hand_card_two)
                    if len(output) > 0:
                        # print(output)
                        output_index = choice(output)
                        output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                        # print(output_text)
                        output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                    else:
                        pass
                    # print("和")
                        # exit(1)
            else:
                if len(Men_Qing_list) > 0:
                    for i in range(len(Men_Qing_list)):
                        output.append(ORDER.index(
                            hand_card_number_list[Men_Qing_list[i]]))
                    output.sort()
                    # print("plan A 孤張")
                    # print(output)
                    output_index = ORDER_TEXT[output[0]]
                    # print(output_index)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_index)
                elif len(break_down_hand_card_small) > 0:
                    for i in range(len(break_down_hand_card_small)):
                        output.append(break_down_hand_card_small[i])
                    # print("plan B 中張or邊張")
                    # print(break_down_hand_card_small)
                    output_index = choice(output)
                    output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                    # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                elif len(break_down_hand_card_pairs) > 2:
                    for i in range(len(break_down_hand_card_pairs)):
                        output.append(break_down_hand_card_pairs[i])
                    # print("plan C 對子(兩組以上)")
                    # print(break_down_hand_card_pairs)
                    output_index = choice(output)
                    output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                    # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                elif len(break_down_hand_card_two) > 0:
                    for i in range(len(break_down_hand_card_two)):
                        if break_down_hand_card_two[i] in break_down_hand_card_pairs:
                            pass
                        else:
                            output.append(break_down_hand_card_two[i])
                    # print("plan D 兩邊")
                    # print(break_down_hand_card_two)
                    if len(output) > 0:
                        # print(output)
                        output_index = choice(output)
                        output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                        # print(output_text)
                        output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                    else:
                        pass
                    # print("和")
                        # exit(1)
        # 三元對在手上
        else:
            if score_eyes == 1:
                Men_Qing_list = []
                # 刻子
                break_down_hand_card_two = []
                break_down_hand_card_small = []
                break_down_hand_card_pairs = []
                for x in range(len(SEQUENCE)):
                    # y 確認內容是否符合
                    for y in SEQUENCE[x]:
                        temp = [i for i, find in enumerate(
                            hand_card_number_list) if find == y]
                        for z in range(len(temp)):
                            list.append(temp[z])
                    if len(list) == 3:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        hand_card_number_list[list[2]] = -1
                        score = score + 3
                    elif len(list) == 4:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        hand_card_number_list[list[3]] = -1
                        score = score + 3
                    else:
                        pass
                    list = []

                # 順子
                for x in range(len(TRIPLET)):
                    # y 確認內容是否符合
                    for z in range(3):
                        for y in range(len(TRIPLET[x])):
                            if TRIPLET[x][y] in hand_card_number_list:
                                list.append(
                                    hand_card_number_list.index(TRIPLET[x][y]))
                        if len(list) >= 3:
                            hand_card_number_list[list[0]] = -1
                            hand_card_number_list[list[1]] = -1
                            hand_card_number_list[list[2]] = -1
                            score = score + 3
                        else:
                            pass
                        list = []

                # 可以拆牌的方向
                for x in range(len(hand_card_number_list)):
                    if hand_card_number_list[x] != -1:
                        break_down_hand_card_two.append(
                            hand_card_number_list[x])
                # 對子
                for x in range(len(SEQUENCE)):
                    # y 確認內容是否符合
                    for y in SEQUENCE[x]:
                        temp = [i for i, find in enumerate(
                            hand_card_number_list) if find == y]
                        for z in range(len(temp)):
                            list.append(temp[z])
                    if len(list) == 2:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        score = score + 2
                        score_eyes = score_eyes + 1
                    else:
                        pass
                    list = []

                for x in range(len(hand_card_number_list)):
                    if hand_card_number_list[x] != -1:
                        break_down_hand_card_small.append(
                            hand_card_number_list[x])
                # 兩邊
                for x in range(len(TWO_SITE)):
                    # y 確認內容是否符合
                    for y in range(len(TWO_SITE[x])):
                        if TWO_SITE[x][y] in hand_card_number_list:
                            list.append(
                                hand_card_number_list.index(TWO_SITE[x][y]))
                    if len(list) == 2:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        score = score + 2
                    else:
                        pass
                    list = []

                # 可以拆牌的方向
                for x in range(len(hand_card_number_list)):
                    if hand_card_number_list[x] != -1:
                        break_down_hand_card_pairs.append(
                            hand_card_number_list[x])

                # 中張 & 邊張
                for x in range(len(MIDDLE)):
                    # y 確認內容是否符合
                    for y in range(len(MIDDLE[x])):
                        if MIDDLE[x][y] in hand_card_number_list:
                            list.append(
                                hand_card_number_list.index(MIDDLE[x][y]))
                    if len(list) == 2:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        score = score + 1
                    else:
                        pass
                    list = []
                for x in range(len(ONE_SITE)):
                    # y 確認內容是否符合
                    for y in range(len(ONE_SITE[x])):
                        if ONE_SITE[x][y] in hand_card_number_list:
                            list.append(
                                hand_card_number_list.index(ONE_SITE[x][y]))
                    if len(list) == 2:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        score = score + 1
                    else:
                        pass
                    list = []
                for i in range(len(hand_card_number_list)):
                    if hand_card_number_list[i] != -1:
                        Men_Qing_list.append(i)
                # 出牌
                if len(Men_Qing_list) > 0:
                    for i in range(len(Men_Qing_list)):
                        output.append(ORDER.index(
                            hand_card_number_list[Men_Qing_list[i]]))
                    output.sort()
                    # print("plan A 孤張")
                    # print(output)
                    output_text = ORDER_TEXT[output[0]]
                    # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                elif len(break_down_hand_card_small) > 0:
                    for i in range(len(break_down_hand_card_small)):
                        output.append(break_down_hand_card_small[i])
                    # print("plan B 中張or邊張")
                    # print(break_down_hand_card_small)
                    output_index = choice(output)
                    output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                    # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                elif len(break_down_hand_card_pairs) > 2:
                    for i in range(len(break_down_hand_card_pairs)):
                        output.append(break_down_hand_card_pairs[i])
                    # print("plan C 對子(兩組以上)")
                    # print(break_down_hand_card_pairs)
                    output_index = choice(output)
                    output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                    # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                elif len(break_down_hand_card_two) > 0:
                    for i in range(len(break_down_hand_card_two)):
                        if break_down_hand_card_two[i] in break_down_hand_card_pairs:
                            pass
                        else:
                            output.append(break_down_hand_card_two[i])
                    # print("plan D 兩邊")
                    # print(break_down_hand_card_two)
                    if len(output) > 0:
                        # print(output)
                        output_index = choice(output)
                        output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                        # print(output_text)
                        output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                    else:
                        pass
                    # print("和")
                        # exit(1)
            else:
                if len(Men_Qing_list) > 0:
                    for i in range(len(Men_Qing_list)):
                        output.append(ORDER.index(
                            hand_card_number_list[Men_Qing_list[i]]))
                    output.sort()
                    # print("plan A 孤張")
                    # print(output)
                    output_index = ORDER_TEXT[output[0]]
                    # print(output_index)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_index)
                elif len(break_down_hand_card_small) > 0:
                    for i in range(len(break_down_hand_card_small)):
                        output.append(break_down_hand_card_small[i])
                    # print("plan B 中張or邊張")
                    # print(break_down_hand_card_small)
                    output_index = choice(output)
                    output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                    # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                elif len(break_down_hand_card_pairs) > 2:
                    for i in range(len(break_down_hand_card_pairs)):
                        output.append(break_down_hand_card_pairs[i])
                    # print("plan C 對子(兩組以上)")
                    # print(break_down_hand_card_pairs)
                    output_index = choice(output)
                    output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                    # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                elif len(break_down_hand_card_two) > 0:
                    for i in range(len(break_down_hand_card_two)):
                        if break_down_hand_card_two[i] in break_down_hand_card_pairs:
                            pass
                        else:
                            output.append(break_down_hand_card_two[i])
                    # print("plan D 兩邊")
                    # print(break_down_hand_card_two)
                    if len(output) > 0:
                        # print(output)
                        output_index = choice(output)
                        output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                        # print(output_text)
                        output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                    else:
                        pass
                    # print("和")
                        # exit(1)

    # 對對 2
    elif road == 2:
        # 刻子
        for x in range(len(SEQUENCE)):
            # y 確認內容是否符合
            for y in SEQUENCE[x]:
                temp = [i for i, find in enumerate(
                    hand_card_number_list) if find == y]
                for z in range(len(temp)):
                    list.append(temp[z])
            if len(list) == 3:
                hand_card_number_list[list[0]] = -1
                hand_card_number_list[list[1]] = -1
                hand_card_number_list[list[2]] = -1
                score = score + 3
            elif len(list) == 4:
                hand_card_number_list[list[0]] = -1
                hand_card_number_list[list[1]] = -1
                hand_card_number_list[list[3]] = -1
                score = score + 3
            else:
                pass
            list = []

        # 對子
        for x in range(len(SEQUENCE)):
            # y 確認內容是否符合
            for y in SEQUENCE[x]:
                temp = [i for i, find in enumerate(
                    hand_card_number_list) if find == y]
                for z in range(len(temp)):
                    list.append(temp[z])
            if len(list) == 2:
                hand_card_number_list[list[0]] = -1
                hand_card_number_list[list[1]] = -1
                score = score + 2
                score_eyes = score_eyes + 1
            else:
                pass
            list = []

        for x in range(len(hand_card_number_list)):
            if hand_card_number_list[x] != -1:
                only_pairs.append(hand_card_number_list[x])
        if len(only_pairs) > 0:
           # print("(斷么)")
           # print(only_pairs)
            output_index = choice(only_pairs)
            output_text = MAHJONG_SORT_TABLE_LIST[output_index]
           # print(output_text)
            output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)

    # 七對 3
    elif road == 3:
        # 對子
        for x in range(len(SEQUENCE)):
            # y 確認內容是否符合
            for y in SEQUENCE[x]:
                temp = [i for i, find in enumerate(
                    hand_card_number_list) if find == y]
                for z in range(len(temp)):
                    list.append(temp[z])
            if len(list) == 2:
                hand_card_number_list[list[0]] = -1
                hand_card_number_list[list[1]] = -1
                score = score + 2
                score_eyes = score_eyes + 1
            else:
                pass
            list = []

        for x in range(len(hand_card_number_list)):
            if hand_card_number_list[x] != -1:
                only_pairs.append(hand_card_number_list[x])
        if len(only_pairs) > 0:
           # print("(斷么)")
           # print(only_pairs)
            output_index = choice(only_pairs)
            output_text = MAHJONG_SORT_TABLE_LIST[output_index]
           # print(output_text)
            output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
    # 混全 4
    elif road == 4:
        if len(output_chanta) > 0:
           # print("(斷么)")
           # print(only_pairs)
            output_index = choice(output_chanta)
            output_text = MAHJONG_SORT_TABLE_LIST[output_index]
           # print(output_text)
            output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
        elif len(output_chanta_one_nine) > 0:
           # print("(斷么)")
           # print(only_pairs)
            output_index = choice(output_chanta_one_nine)
            output_text = MAHJONG_SORT_TABLE_LIST[output_index]
           # print(output_text)
            output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
        else:
            break_down_hand_card_pairs = []  # 拆對
            break_down_hand_card_two = []  # 拆邊 = 中張 = 邊張
            # 123 or 789 順
            for x in range(len(ZERO_SITE)):
                # y 確認內容是否符合
                for y in range(len(ZERO_SITE[x])):
                    if ZERO_SITE[x][y] in hand_card_number_list:
                        list.append(
                            hand_card_number_list.index(ZERO_SITE[x][y]))
                if len(list) == 3:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    hand_card_number_list[list[2]] = -1
                    chanta = chanta + 3
                else:
                    pass
                list = []
            # 刻子 么九刻
            for x in range(len(NINE_AND_NINE)):
                # y 確認內容是否符合
                for y in NINE_AND_NINE[x]:
                    temp = [i for i, find in enumerate(
                        hand_card_number_list) if find == y]
                    for z in range(len(temp)):
                        list.append(temp[z])
                if len(list) >= 3:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    hand_card_number_list[list[2]] = -1
                    score = score + 3
                else:
                    pass
                list = []
            # 可以拆牌的方向
            for x in range(len(hand_card_number_list)):
                if hand_card_number_list[x] != -1:
                    break_down_hand_card_pairs.append(hand_card_number_list[x])
            # 對子 么九對
            for x in range(len(NINE_AND_NINE)):
                # y 確認內容是否符合
                for y in NINE_AND_NINE[x]:
                    temp = [i for i, find in enumerate(
                        hand_card_number_list) if find == y]
                    for z in range(len(temp)):
                        list.append(temp[z])
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    score = score + 2
                    score_eyes = score_eyes + 1
                else:
                    pass
                list = []
            # 可以拆牌的方向
            for x in range(len(hand_card_number_list)):
                if hand_card_number_list[x] != -1:
                    break_down_hand_card_two.append(hand_card_number_list[x])
            # 等一張
            for x in range(len(ONE_SITE)):
                # y 確認內容是否符合
                for y in range(len(ONE_SITE[x])):
                    if ONE_SITE[x][y] in hand_card_number_list:
                        list.append(
                            hand_card_number_list.index(ONE_SITE[x][y]))
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    chanta = chanta + 2
                else:
                    pass
                list = []
            if len(break_down_hand_card_two) > 0:
                output_index = choice(break_down_hand_card_two)
                output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                # print(output_text)
                output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
            else:
                output_index = choice(break_down_hand_card_pairs)
                output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                # print(output_text)
                output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)

    # 一氣 5
    elif road == 5:
        if len(break_down_hand_card_small) > 0:
           # print("(斷么)")
           # print(only_pairs)
            output_index = choice(break_down_hand_card_small)
            output_text = MAHJONG_SORT_TABLE_LIST[output_index]
           # print(output_text)
            output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
        elif len(break_down_hand_card_two) > 0:
           # print("(斷么)")
           # print(only_pairs)
            output_index = choice(break_down_hand_card_two)
            output_text = MAHJONG_SORT_TABLE_LIST[output_index]
           # print(output_text)
            output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
        elif len(break_down_hand_card_pairs) > 0:
           # print("(斷么)")
           # print(only_pairs)
            output_index = choice(break_down_hand_card_pairs)
            output_text = MAHJONG_SORT_TABLE_LIST[output_index]
           # print(output_text)
            output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
        else:
            pass
    # 斷么 6
    elif road == 6:
        output = []
        if len(no_one_nine) > 0:
           # print("(斷么)")
           # print(no_one_nine)
            output_index = choice(no_one_nine)
            output_text = MAHJONG_SORT_TABLE_LIST[output_index]
           # print(output_text)
            output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
        else:
           #print("(斷么)有沒有眼：" + str(score_eyes))
            if score_eyes == 0:
                Men_Qing_list = []
                # 刻子
                break_down_hand_card_two = []
                break_down_hand_card_small = []
                break_down_hand_card_pairs = []
                for x in range(len(SEQUENCE)):
                    # y 確認內容是否符合
                    for y in SEQUENCE[x]:
                        temp = [i for i, find in enumerate(
                            hand_card_number_list) if find == y]
                        for z in range(len(temp)):
                            list.append(temp[z])
                    if len(list) == 3:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        hand_card_number_list[list[2]] = -1
                        score = score + 3
                    elif len(list) == 4:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        hand_card_number_list[list[3]] = -1
                        score = score + 3
                    else:
                        pass
                    list = []

                # 順子
                for x in range(len(TRIPLET)):
                    # y 確認內容是否符合
                    for z in range(3):
                        for y in range(len(TRIPLET[x])):
                            if TRIPLET[x][y] in hand_card_number_list:
                                list.append(
                                    hand_card_number_list.index(TRIPLET[x][y]))
                        if len(list) >= 3:
                            hand_card_number_list[list[0]] = -1
                            hand_card_number_list[list[1]] = -1
                            hand_card_number_list[list[2]] = -1
                            score = score + 3
                        else:
                            pass
                        list = []

                # 可以拆牌的方向
                for x in range(len(hand_card_number_list)):
                    if hand_card_number_list[x] != -1:
                        break_down_hand_card_two.append(
                            hand_card_number_list[x])
                # 對子
                for x in range(len(SEQUENCE)):
                    # y 確認內容是否符合
                    for y in SEQUENCE[x]:
                        temp = [i for i, find in enumerate(
                            hand_card_number_list) if find == y]
                        for z in range(len(temp)):
                            list.append(temp[z])
                    if len(list) == 2:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        score = score + 2
                        score_eyes = score_eyes + 1
                    else:
                        pass
                    list = []

                for x in range(len(hand_card_number_list)):
                    if hand_card_number_list[x] != -1:
                        break_down_hand_card_small.append(
                            hand_card_number_list[x])
                # 兩邊
                for x in range(len(TWO_SITE)):
                    # y 確認內容是否符合
                    for y in range(len(TWO_SITE[x])):
                        if TWO_SITE[x][y] in hand_card_number_list:
                            list.append(
                                hand_card_number_list.index(TWO_SITE[x][y]))
                    if len(list) == 2:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        score = score + 2
                    else:
                        pass
                    list = []

                # 可以拆牌的方向
                for x in range(len(hand_card_number_list)):
                    if hand_card_number_list[x] != -1:
                        break_down_hand_card_pairs.append(
                            hand_card_number_list[x])

                # 中張 & 邊張
                for x in range(len(MIDDLE)):
                    # y 確認內容是否符合
                    for y in range(len(MIDDLE[x])):
                        if MIDDLE[x][y] in hand_card_number_list:
                            list.append(
                                hand_card_number_list.index(MIDDLE[x][y]))
                    if len(list) == 2:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        score = score + 1
                    else:
                        pass
                    list = []
                for x in range(len(ONE_SITE)):
                    # y 確認內容是否符合
                    for y in range(len(ONE_SITE[x])):
                        if ONE_SITE[x][y] in hand_card_number_list:
                            list.append(
                                hand_card_number_list.index(ONE_SITE[x][y]))
                    if len(list) == 2:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        score = score + 1
                    else:
                        pass
                    list = []
                for i in range(len(hand_card_number_list)):
                    if hand_card_number_list[i] != -1:
                        Men_Qing_list.append(i)
                # 出牌
                if len(Men_Qing_list) > 0:
                    for i in range(len(Men_Qing_list)):
                        output.append(ORDER.index(
                            hand_card_number_list[Men_Qing_list[i]]))
                    output.sort()
                   #print("(斷么)plan A 孤張")
                   # print(output)
                    output_text = ORDER_TEXT[output[0]]
                   # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                elif len(break_down_hand_card_small) > 0:
                    for i in range(len(break_down_hand_card_small)):
                        output.append(break_down_hand_card_small[i])
                   #print("(斷么)plan B 中張or邊張")
                   # print(break_down_hand_card_small)
                    output_index = choice(output)
                    output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                   # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                elif len(break_down_hand_card_pairs) > 2:
                    for i in range(len(break_down_hand_card_pairs)):
                        output.append(break_down_hand_card_pairs[i])
                   #print("(斷么)plan C 對子(兩組以上)")
                   # print(break_down_hand_card_pairs)
                    output_index = choice(output)
                    output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                   # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                elif len(break_down_hand_card_two) > 0:
                    for i in range(len(break_down_hand_card_two)):
                        if break_down_hand_card_two[i] in break_down_hand_card_pairs:
                            pass
                        else:
                            output.append(break_down_hand_card_two[i])
                   #print("(斷么)plan D 兩邊")
                   # print(break_down_hand_card_two)
                    if len(output) > 0:
                       # print(output)
                        output_index = choice(output)
                        output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                       # print(output_text)
                        output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                    else:
                        pass
                       # print("(斷么)和")
            else:
                if len(Men_Qing_list) > 0:
                    for i in range(len(Men_Qing_list)):
                        output.append(ORDER.index(
                            hand_card_number_list[Men_Qing_list[i]]))
                    output.sort()
                   #print("(斷么)plan A 孤張")
                   # print(output)
                    output_index = ORDER_TEXT[output[0]]
                   # print(output_index)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_index)
                elif len(break_down_hand_card_small) > 0:
                    for i in range(len(break_down_hand_card_small)):
                        output.append(break_down_hand_card_small[i])
                   #print("(斷么)plan B 中張or邊張")
                   # print(break_down_hand_card_small)
                    output_index = choice(output)
                    output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                   # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                elif len(break_down_hand_card_pairs) > 2:
                    for i in range(len(break_down_hand_card_pairs)):
                        output.append(break_down_hand_card_pairs[i])
                   #print("(斷么)plan C 對子(兩組以上)")
                   # print(break_down_hand_card_pairs)
                    output_index = choice(output)
                    output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                   # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                elif len(break_down_hand_card_two) > 0:
                    for i in range(len(break_down_hand_card_two)):
                        if break_down_hand_card_two[i] in break_down_hand_card_pairs:
                            pass
                        else:
                            output.append(break_down_hand_card_two[i])
                   #print("(斷么)plan D 兩邊")
                   # print(break_down_hand_card_two)
                    if len(output) > 0:
                       # print(output)
                        output_index = choice(output)
                        output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                       # print(output_text)
                        output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                    else:
                        pass
                       # print("(斷么)和")

    # 門清 起始
    if road == 7 or road == -1:
        output = []
        ##print("有沒有眼：" + str(score_eyes))
        if score_eyes == 0:
            Men_Qing_list = []
            # 刻子
            break_down_hand_card_two = []
            break_down_hand_card_small = []
            break_down_hand_card_pairs = []
            for x in range(len(SEQUENCE)):
                # y 確認內容是否符合
                for y in SEQUENCE[x]:
                    temp = [i for i, find in enumerate(
                        hand_card_number_list) if find == y]
                    for z in range(len(temp)):
                        list.append(temp[z])
                if len(list) == 3:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    hand_card_number_list[list[2]] = -1
                    score = score + 3
                elif len(list) == 4:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    hand_card_number_list[list[3]] = -1
                    score = score + 3
                else:
                    pass
                list = []

            # 順子
            for x in range(len(TRIPLET)):
                # y 確認內容是否符合
                for z in range(3):
                    for y in range(len(TRIPLET[x])):
                        if TRIPLET[x][y] in hand_card_number_list:
                            list.append(
                                hand_card_number_list.index(TRIPLET[x][y]))
                    if len(list) >= 3:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        hand_card_number_list[list[2]] = -1
                        score = score + 3
                    else:
                        pass
                    list = []

            # 可以拆牌的方向
            for x in range(len(hand_card_number_list)):
                if hand_card_number_list[x] != -1:
                    break_down_hand_card_two.append(hand_card_number_list[x])
            # 對子
            for x in range(len(SEQUENCE)):
                # y 確認內容是否符合
                for y in SEQUENCE[x]:
                    temp = [i for i, find in enumerate(
                        hand_card_number_list) if find == y]
                    for z in range(len(temp)):
                        list.append(temp[z])
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    score = score + 2
                    score_eyes = score_eyes + 1
                else:
                    pass
                list = []

            for x in range(len(hand_card_number_list)):
                if hand_card_number_list[x] != -1:
                    break_down_hand_card_small.append(hand_card_number_list[x])
            
            # 兩邊
            for x in range(len(TWO_SITE)):
                # y 確認內容是否符合
                for y in range(len(TWO_SITE[x])):
                    if TWO_SITE[x][y] in hand_card_number_list:
                        list.append(
                            hand_card_number_list.index(TWO_SITE[x][y]))
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    score = score + 2
                else:
                    pass
                list = []

            # 可以拆牌的方向
            for x in range(len(hand_card_number_list)):
                if hand_card_number_list[x] != -1:
                    break_down_hand_card_pairs.append(hand_card_number_list[x])

            # 中張 & 邊張
            for x in range(len(MIDDLE)):
                # y 確認內容是否符合
                for y in range(len(MIDDLE[x])):
                    if MIDDLE[x][y] in hand_card_number_list:
                        list.append(
                            hand_card_number_list.index(MIDDLE[x][y]))
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    score = score + 1
                else:
                    pass
                list = []
            for x in range(len(ONE_SITE)):
                # y 確認內容是否符合
                for y in range(len(ONE_SITE[x])):
                    if ONE_SITE[x][y] in hand_card_number_list:
                        list.append(
                            hand_card_number_list.index(ONE_SITE[x][y]))
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    score = score + 1
                else:
                    pass
                list = []
            for i in range(len(hand_card_number_list)):
                if hand_card_number_list[i] != -1:
                    Men_Qing_list.append(i)
            
            # 出牌
            if len(Men_Qing_list) > 0:
                for i in range(len(Men_Qing_list)):
                    output.append(ORDER.index(
                        hand_card_number_list[Men_Qing_list[i]]))
                output.sort()
                print("plan A 孤張")
                print(output)
                output_text = ORDER_TEXT[output[0]]
                # print(output_text)
                output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
            elif len(break_down_hand_card_small) > 0:
                for i in range(len(break_down_hand_card_small)):
                    output.append(break_down_hand_card_small[i])
                print("plan B 中張or邊張")
                print(break_down_hand_card_small)
                output_index = choice(output)
                output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                # print(output_text)
                output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
            elif len(break_down_hand_card_pairs) > 2:
                for i in range(len(break_down_hand_card_pairs)):
                    output.append(break_down_hand_card_pairs[i])
                print("plan C 對子(兩組以上)")
                print(break_down_hand_card_pairs)
                output_index = choice(output)
                output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                # print(output_text)
                output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
            elif len(break_down_hand_card_two) > 0:
                for i in range(len(break_down_hand_card_two)):
                    if break_down_hand_card_two[i] in break_down_hand_card_pairs:
                        pass
                    else:
                        output.append(break_down_hand_card_two[i])
                print("plan D 兩邊")
                print(break_down_hand_card_two)
                if len(output) > 0:
                    # print(output)
                    output_index = choice(output)
                    output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                    # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                else:
                    pass
                   # print("和")
                    # exit(1)
        else:
            Men_Qing_list = []
            # 刻子
            break_down_hand_card_two = []
            break_down_hand_card_small = []
            break_down_hand_card_pairs = []
            for x in range(len(SEQUENCE)):
                # y 確認內容是否符合
                for y in SEQUENCE[x]:
                    temp = [i for i, find in enumerate(
                        hand_card_number_list) if find == y]
                    for z in range(len(temp)):
                        list.append(temp[z])
                if len(list) == 3:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    hand_card_number_list[list[2]] = -1
                    score = score + 3
                elif len(list) == 4:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    hand_card_number_list[list[3]] = -1
                    score = score + 3
                else:
                    pass
                list = []

            # 順子
            for x in range(len(TRIPLET)):
                # y 確認內容是否符合
                for z in range(3):
                    for y in range(len(TRIPLET[x])):
                        if TRIPLET[x][y] in hand_card_number_list:
                            list.append(
                                hand_card_number_list.index(TRIPLET[x][y]))
                    if len(list) >= 3:
                        hand_card_number_list[list[0]] = -1
                        hand_card_number_list[list[1]] = -1
                        hand_card_number_list[list[2]] = -1
                        score = score + 3
                    else:
                        pass
                    list = []

            # 可以拆牌的方向
            for x in range(len(hand_card_number_list)):
                if hand_card_number_list[x] != -1:
                    break_down_hand_card_two.append(hand_card_number_list[x])
            
            # 兩邊
            for x in range(len(TWO_SITE)):
                # y 確認內容是否符合
                for y in range(len(TWO_SITE[x])):
                    if TWO_SITE[x][y] in hand_card_number_list:
                        list.append(
                            hand_card_number_list.index(TWO_SITE[x][y]))
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    score = score + 2
                else:
                    pass
                list = []

            # 可以拆牌的方向
            for x in range(len(hand_card_number_list)):
                if hand_card_number_list[x] != -1:
                    break_down_hand_card_pairs.append(hand_card_number_list[x])
            # 對子
            for x in range(len(SEQUENCE)):
                # y 確認內容是否符合
                for y in SEQUENCE[x]:
                    temp = [i for i, find in enumerate(
                        hand_card_number_list) if find == y]
                    for z in range(len(temp)):
                        list.append(temp[z])
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    score = score + 2
                    score_eyes = score_eyes + 1
                else:
                    pass
                list = []

            for x in range(len(hand_card_number_list)):
                if hand_card_number_list[x] != -1:
                    break_down_hand_card_small.append(hand_card_number_list[x])
                    
            # 中張 & 邊張
            for x in range(len(MIDDLE)):
                # y 確認內容是否符合
                for y in range(len(MIDDLE[x])):
                    if MIDDLE[x][y] in hand_card_number_list:
                        list.append(
                            hand_card_number_list.index(MIDDLE[x][y]))
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    score = score + 1
                else:
                    pass
                list = []
            for x in range(len(ONE_SITE)):
                # y 確認內容是否符合
                for y in range(len(ONE_SITE[x])):
                    if ONE_SITE[x][y] in hand_card_number_list:
                        list.append(
                            hand_card_number_list.index(ONE_SITE[x][y]))
                if len(list) == 2:
                    hand_card_number_list[list[0]] = -1
                    hand_card_number_list[list[1]] = -1
                    score = score + 1
                else:
                    pass
                list = []
            for i in range(len(hand_card_number_list)):
                if hand_card_number_list[i] != -1:
                    Men_Qing_list.append(i)
            # 出牌
            if len(Men_Qing_list) > 0:
                for i in range(len(Men_Qing_list)):
                    output.append(ORDER.index(
                        hand_card_number_list[Men_Qing_list[i]]))
                output.sort()
                print("plan A 孤張 eye")
                print(output)
                output_index = ORDER_TEXT[output[0]]
                # print(output_index)
                output_id = MAHJONG_SORT_TABLE_LIST.index(output_index)
            elif len(break_down_hand_card_small) > 0:
                for i in range(len(break_down_hand_card_small)):
                    output.append(break_down_hand_card_small[i])
                print("plan B 中張or邊張")
                print(break_down_hand_card_small)
                output_index = choice(output)
                output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                # print(output_text)
                output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
            elif len(break_down_hand_card_pairs) > 2:
                for i in range(len(break_down_hand_card_pairs)):
                    output.append(break_down_hand_card_pairs[i])
                print("plan C 對子(兩組以上)")
                print(break_down_hand_card_pairs)
                output_index = choice(output)
                output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                # print(output_text)
                output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
            elif len(break_down_hand_card_two) > 0:
                for i in range(len(break_down_hand_card_two)):
                    if break_down_hand_card_two[i] in break_down_hand_card_pairs:
                        pass
                    else:
                        output.append(break_down_hand_card_two[i])
                print("plan D 兩邊")
                print(break_down_hand_card_two)
                if len(output) > 0:
                    # print(output)
                    output_index = choice(output)
                    output_text = MAHJONG_SORT_TABLE_LIST[output_index]
                    # print(output_text)
                    output_id = MAHJONG_SORT_TABLE_LIST.index(output_text)
                else:
                    pass
                   # print("和")
                    # exit(1)
        print(break_down_hand_card_small)
        print("aaaaaaaaaa")
    print(break_down_hand_card_small)
    # 回傳值 將output_id(數值) 轉回 字串 return
    if site == "down":
        temp = []
        hand_card_number_list = []
        for i in range(len(HAND_CARDS_LIST)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(HAND_CARDS_LIST[i][1].id))
        if draw != "":
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(draw))
        # print(hand_card_number_list.index(output_id))
        # 把抽到的牌 加入手牌一起評分
    if site == "right":
        temp = []
        hand_card_number_list = []
        for i in range(len(RIGHT_HAND_CARDS_LIST)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(RIGHT_HAND_CARDS_LIST[i][1].id))
        if draw != "":
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(draw))
        # print(hand_card_number_list.index(output_id))
        return(hand_card_number_list.index(output_id))
    if site == "up":
        temp = []
        hand_card_number_list = []
        for i in range(len(UP_HAND_CARDS_LIST)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(UP_HAND_CARDS_LIST[i][1].id))
        if draw != "":
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(draw))
        # print(hand_card_number_list.index(output_id))
        return(hand_card_number_list.index(output_id))
    if site == "left":
        temp = []
        hand_card_number_list = []
        for i in range(len(LEFT_HAND_CARDS_LIST)):
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(LEFT_HAND_CARDS_LIST[i][1].id))
        if draw != "":
            hand_card_number_list.append(
                MAHJONG_SORT_TABLE_LIST.index(draw))
        # print(hand_card_number_list.index(output_id))
        return(hand_card_number_list.index(output_id))

    # 2.要吃碰前 優先判斷役種
    """
    1. 字牌已經有役無限制
    2. 役牌有對不吃碰
    3. 么九少於4張 可以吃碰做段么
    4. 
    """

    # 3.處理振聽 (給他拼自摸)

    # 4.必要時 拆牌(降低牌分)

    # 5.


RON_HAND_CARD_START_X = 200
RON_HAND_CARD_START_Y = 310
RON_HAND_CARD_ID_LIST = []
RON_VICE_DEWS_ID_LIST = []
RON_CARD_ID = ""
WIN_SITE = ""
IS_WIN = 0
# class


class Player(pygame.sprite.Sprite):  # 玩家
    def __init__(self, site=""):
        pygame.sprite.Sprite.__init__(self)
        self.image = null_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.is_my_turn = False
        # 13張手牌列表(編號,Mahjong物件)
        self.cards = []
        self.site = site
        self.deal_card = ""
        self.vice_dews = []
        self.vice_dews_x = 1280
        self.vice_dews_y = 720 - SMALL_MAHJONG_HEIGHT
        self.point = 25000

    def update(self):
        pass

    # def draw(self,card_obj):
    #    self.cards.append([len(self.cards),card_obj])
    #    self.cards[len(self.cards)-1][1].in_hand_id = self.cards[len(self.cards)-1][0]

    def chi(self, target_cards_id_list):
        global left_card_river
        global play_single_sprites
        global play_multi_sprites
        global HAND_CARDS_LIST
        chi_card_id = left_card_river.get_last_card_id()
        left_card_river.del_last_card()
        # 根據id從手牌刪除
        i = 0
        while i < len(HAND_CARDS_LIST):
            if HAND_CARDS_LIST[i][1].id == target_cards_id_list[0]:
                HAND_CARDS_LIST[i][1].mahjong_box.move_ip(-1000, -1000)
                HAND_CARDS_LIST[i][1].kill()
                del HAND_CARDS_LIST[i]
                break
            i += 1
        i = 0
        while i < len(HAND_CARDS_LIST):
            if HAND_CARDS_LIST[i][1].id == target_cards_id_list[1]:
                HAND_CARDS_LIST[i][1].mahjong_box.move_ip(-1000, -1000)
                HAND_CARDS_LIST[i][1].kill()
                del HAND_CARDS_LIST[i]
                break
            i += 1
        sort("down")
        # 加到鳴牌區
        self.vice_dews_x -= SMALL_MAHJONG_WIDTH
        vdsm = Small_Mahjong(
            target_cards_id_list[1], self.vice_dews_x, self.vice_dews_y, "down")
        play_single_sprites.add(vdsm)
        play_multi_sprites.add(vdsm)
        self.vice_dews.append(vdsm)

        self.vice_dews_x -= SMALL_MAHJONG_WIDTH
        vdsm = Small_Mahjong(
            target_cards_id_list[0], self.vice_dews_x, self.vice_dews_y, "down")
        play_single_sprites.add(vdsm)
        play_multi_sprites.add(vdsm)
        self.vice_dews.append(vdsm)

        self.vice_dews_x -= SMALL_MAHJONG_HEIGHT
        vdsm = Small_Mahjong(chi_card_id, self.vice_dews_x, self.vice_dews_y +
                             (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH), "right")
        play_single_sprites.add(vdsm)
        play_multi_sprites.add(vdsm)
        self.vice_dews.append(vdsm)

        if IS_PLAY_MULTI == 1:
            send_to_server(["chi", target_cards_id_list[1],
                           target_cards_id_list[0], chi_card_id])

    def pong(self, source_site, pong_card_id=""):
        global right_card_river
        global up_card_river
        global left_card_river
        global HAND_CARDS_LIST
        global play_single_sprites
        global play_multi_sprites

        if source_site == "right":
            pong_card_id = right_card_river.get_last_card_id()
            right_card_river.del_last_card()
            pong_card_id1 = pong_card_id
            pong_card_id2 = pong_card_id
            pong_card_id3 = pong_card_id
            if pong_card_id == "Man5_red":
                pong_card_id2 = "Man5"
                pong_card_id3 = "Man5"
            if pong_card_id == "Pin5_red":
                pong_card_id2 = "Pin5"
                pong_card_id3 = "Pin5"
            if pong_card_id == "Sou5_red":
                pong_card_id2 = "Sou5"
                pong_card_id3 = "Sou5"

            self.vice_dews_x -= SMALL_MAHJONG_HEIGHT
            vdsm = Small_Mahjong(pong_card_id1, self.vice_dews_x, self.vice_dews_y +
                                 (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH), "right")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

            self.vice_dews_x -= SMALL_MAHJONG_WIDTH
            vdsm = Small_Mahjong(
                pong_card_id2, self.vice_dews_x, self.vice_dews_y, "down")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

            self.vice_dews_x -= SMALL_MAHJONG_WIDTH
            vdsm = Small_Mahjong(
                pong_card_id3, self.vice_dews_x, self.vice_dews_y, "down")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

        elif source_site == "up":
            pong_card_id = up_card_river.get_last_card_id()
            up_card_river.del_last_card()
            pong_card_id1 = pong_card_id
            pong_card_id2 = pong_card_id
            pong_card_id3 = pong_card_id
            if pong_card_id == "Man5_red":
                pong_card_id2 = "Man5"
                pong_card_id3 = "Man5"
            if pong_card_id == "Pin5_red":
                pong_card_id2 = "Pin5"
                pong_card_id3 = "Pin5"
            if pong_card_id == "Sou5_red":
                pong_card_id2 = "Sou5"
                pong_card_id3 = "Sou5"

            self.vice_dews_x -= SMALL_MAHJONG_WIDTH
            vdsm = Small_Mahjong(
                pong_card_id1, self.vice_dews_x, self.vice_dews_y, "down")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

            self.vice_dews_x -= SMALL_MAHJONG_HEIGHT
            vdsm = Small_Mahjong(pong_card_id2, self.vice_dews_x, self.vice_dews_y +
                                 (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH), "right")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

            self.vice_dews_x -= SMALL_MAHJONG_WIDTH
            vdsm = Small_Mahjong(
                pong_card_id3, self.vice_dews_x, self.vice_dews_y, "down")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

        elif source_site == "left":
            pong_card_id = left_card_river.get_last_card_id()
            left_card_river.del_last_card()
            pong_card_id1 = pong_card_id
            pong_card_id2 = pong_card_id
            pong_card_id3 = pong_card_id
            if pong_card_id == "Man5_red":
                pong_card_id2 = "Man5"
                pong_card_id3 = "Man5"
            if pong_card_id == "Pin5_red":
                pong_card_id2 = "Pin5"
                pong_card_id3 = "Pin5"
            if pong_card_id == "Sou5_red":
                pong_card_id2 = "Sou5"
                pong_card_id3 = "Sou5"

            self.vice_dews_x -= SMALL_MAHJONG_WIDTH
            vdsm = Small_Mahjong(
                pong_card_id1, self.vice_dews_x, self.vice_dews_y, "down")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

            self.vice_dews_x -= SMALL_MAHJONG_WIDTH
            vdsm = Small_Mahjong(
                pong_card_id2, self.vice_dews_x, self.vice_dews_y, "down")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

            self.vice_dews_x -= SMALL_MAHJONG_HEIGHT
            vdsm = Small_Mahjong(pong_card_id3, self.vice_dews_x, self.vice_dews_y +
                                 (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH), "right")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

        i = 0
        take_out_num = 0
        while take_out_num < 2 and i < len(HAND_CARDS_LIST):
            if HAND_CARDS_LIST[i][1].id == pong_card_id1 or HAND_CARDS_LIST[i][1].id == pong_card_id2:
                HAND_CARDS_LIST[i][1].mahjong_box.move_ip(-1000, -1000)
                HAND_CARDS_LIST[i][1].kill()
                del HAND_CARDS_LIST[i]
                take_out_num += 1
                i -= 1
            i += 1
        sort("down")

    def kong(self, source_site):  # 手裡有三張 槓他家的牌
        global right_card_river
        global up_card_river
        global left_card_river
        global HAND_CARDS_LIST
        global play_single_sprites
        global play_multi_sprites
        global dora_mountain

        if source_site == "right":
            pong_card_id = right_card_river.get_last_card_id()
            right_card_river.del_last_card()
            pong_card_id1 = pong_card_id
            pong_card_id2 = pong_card_id
            if pong_card_id == "Man5_red":
                pong_card_id2 = "Man5"
            if pong_card_id == "Pin5_red":
                pong_card_id2 = "Pin5"
            if pong_card_id == "Sou5_red":
                pong_card_id2 = "Sou5"

            self.vice_dews_x -= SMALL_MAHJONG_HEIGHT
            vdsm = Small_Mahjong(pong_card_id1, self.vice_dews_x, self.vice_dews_y +
                                 (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH), "right")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

            self.vice_dews_x -= SMALL_MAHJONG_WIDTH
            vdsm = Small_Mahjong(
                pong_card_id2, self.vice_dews_x, self.vice_dews_y, "down")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

            self.vice_dews_x -= SMALL_MAHJONG_WIDTH
            vdsm = Small_Mahjong(
                pong_card_id2, self.vice_dews_x, self.vice_dews_y, "down")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

            self.vice_dews_x -= SMALL_MAHJONG_WIDTH
            vdsm = Small_Mahjong(
                pong_card_id2, self.vice_dews_x, self.vice_dews_y, "down")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

        elif source_site == "up":
            pong_card_id = up_card_river.get_last_card_id()
            up_card_river.del_last_card()
            pong_card_id1 = pong_card_id
            pong_card_id2 = pong_card_id
            if pong_card_id == "Man5_red":
                pong_card_id2 = "Man5"
            if pong_card_id == "Pin5_red":
                pong_card_id2 = "Pin5"
            if pong_card_id == "Sou5_red":
                pong_card_id2 = "Sou5"

            self.vice_dews_x -= SMALL_MAHJONG_WIDTH
            vdsm = Small_Mahjong(
                pong_card_id1, self.vice_dews_x, self.vice_dews_y, "down")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

            self.vice_dews_x -= SMALL_MAHJONG_WIDTH
            vdsm = Small_Mahjong(
                pong_card_id2, self.vice_dews_x, self.vice_dews_y, "down")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

            self.vice_dews_x -= SMALL_MAHJONG_HEIGHT
            vdsm = Small_Mahjong(pong_card_id2, self.vice_dews_x, self.vice_dews_y +
                                 (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH), "right")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

            self.vice_dews_x -= SMALL_MAHJONG_WIDTH
            vdsm = Small_Mahjong(
                pong_card_id2, self.vice_dews_x, self.vice_dews_y, "down")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

        elif source_site == "left":
            pong_card_id = left_card_river.get_last_card_id()
            left_card_river.del_last_card()
            pong_card_id1 = pong_card_id
            pong_card_id2 = pong_card_id
            if pong_card_id == "Man5_red":
                pong_card_id2 = "Man5"
            if pong_card_id == "Pin5_red":
                pong_card_id2 = "Pin5"
            if pong_card_id == "Sou5_red":
                pong_card_id2 = "Sou5"

            self.vice_dews_x -= SMALL_MAHJONG_WIDTH
            vdsm = Small_Mahjong(
                pong_card_id1, self.vice_dews_x, self.vice_dews_y, "down")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

            self.vice_dews_x -= SMALL_MAHJONG_WIDTH
            vdsm = Small_Mahjong(
                pong_card_id2, self.vice_dews_x, self.vice_dews_y, "down")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

            self.vice_dews_x -= SMALL_MAHJONG_WIDTH
            vdsm = Small_Mahjong(
                pong_card_id2, self.vice_dews_x, self.vice_dews_y, "down")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

            self.vice_dews_x -= SMALL_MAHJONG_HEIGHT
            vdsm = Small_Mahjong(pong_card_id2, self.vice_dews_x, self.vice_dews_y +
                                 (SMALL_MAHJONG_HEIGHT - SMALL_MAHJONG_WIDTH), "right")
            play_single_sprites.add(vdsm)
            play_multi_sprites.add(vdsm)
            self.vice_dews.append(vdsm)

        i = 0
        take_out_num = 0
        while take_out_num < 3 and i < len(HAND_CARDS_LIST):
            if HAND_CARDS_LIST[i][1].id == pong_card_id1 or HAND_CARDS_LIST[i][1].id == pong_card_id2:
                HAND_CARDS_LIST[i][1].mahjong_box.move_ip(-1000, -1000)
                HAND_CARDS_LIST[i][1].kill()
                del HAND_CARDS_LIST[i]
                take_out_num += 1
                i -= 1
            i += 1
        sort("down")

    def ron(self, ron_card_id):
        global IS_PLAY_MULTI
        global IS_PLAY_MULTI_END
        global play_multi_end_init
        global HAND_CARDS_LIST
        global RON_HAND_CARD_ID_LIST
        global RON_VICE_DEWS_ID_LIST
        global RON_CARD_ID
        global IS_WIN
        global RESULT
        global IS_PLAY_SINGLE
        global IS_PLAY_SINGLE_END
        global play_single_end_init
        global play_single_init
        RESULT = "leave"
        RON_HAND_CARD_ID_LIST = []
        RON_VICE_DEWS_ID_LIST = []
        RON_CARD_ID = ron_card_id

        i = 0
        while i < len(HAND_CARDS_LIST):
            RON_HAND_CARD_ID_LIST.append(HAND_CARDS_LIST[i][1].id)

            HAND_CARDS_LIST[i][1].mahjong_box.move_ip(-1000, -1000)
            HAND_CARDS_LIST[i][1].kill()
            del HAND_CARDS_LIST[i]

        i = 0
        while i < len(self.vice_dews):
            RON_VICE_DEWS_ID_LIST.append(self.vice_dews[i].id)
            i += 1

        IS_WIN = 1
        if IS_PLAY_MULTI == 1:
            IS_PLAY_MULTI = 0
            IS_PLAY_MULTI_END = 1
            play_multi_end_init = True
        if IS_PLAY_SINGLE == 1:
            IS_PLAY_SINGLE = 0
            play_single_init = True
            IS_PLAY_SINGLE_END = 1
            play_single_end_init = True

    def tsumo(self, ron_card_id):
        global IS_PLAY_MULTI
        global IS_PLAY_MULTI_END
        global play_multi_end_init
        global HAND_CARDS_LIST
        global RON_HAND_CARD_ID_LIST
        global RON_VICE_DEWS_ID_LIST
        global RON_CARD_ID
        global IS_WIN
        global RESULT
        global IS_PLAY_SINGLE
        global IS_PLAY_SINGLE_END
        global play_single_end_init
        RESULT = "leave"
        RON_HAND_CARD_ID_LIST = []
        RON_VICE_DEWS_ID_LIST = []
        RON_CARD_ID = ron_card_id
        # if IS_PLAY_MULTI == 1:
        #    RON_CARD_ID = ron_card_id
        # else:
        #    pass

        i = 0
        while i < len(HAND_CARDS_LIST):
            RON_HAND_CARD_ID_LIST.append(HAND_CARDS_LIST[i][1].id)

            HAND_CARDS_LIST[i][1].mahjong_box.move_ip(-1000, -1000)
            HAND_CARDS_LIST[i][1].kill()
            del HAND_CARDS_LIST[i]

        i = 0
        while i < len(self.vice_dews):
            RON_VICE_DEWS_ID_LIST.append(self.vice_dews[i].id)
            i += 1

        IS_WIN = 1
        if IS_PLAY_MULTI == 1:
            IS_PLAY_MULTI = 0
            IS_PLAY_MULTI_END = 1
            play_multi_end_init = True
        if IS_PLAY_SINGLE == 1:
            IS_PLAY_SINGLE = 0
            IS_PLAY_SINGLE_END = 1
            play_single_end_init = True

    def out_card(self, in_hand_id, card_id):  # 出牌(我找不到正常的出牌的英文) ,傳入 麻將id, 手牌位置id
        click_sound.play()
        #draw_texts(screen, [f"{id}"], 40, WIDTH/2, HEIGHT/2)
        global HAND_CARDS_LIST
        global player_card_river
        global DEAL_CARD
        global IS_MULTI_DEAL
        # for h in HAND_CARDS_LIST:
        #   #print(h[1].id)
        is_match = 0
       # print(f"wait_match:{in_hand_id},{card_id}")
        for i in range(len(HAND_CARDS_LIST)):
            pass
           # print(HAND_CARDS_LIST[i][0],HAND_CARDS_LIST[i][1].id)
       # print()
        i = 0
        while i < len(HAND_CARDS_LIST):
            """print(HAND_CARDS_LIST[i][0], in_hand_id,
                  HAND_CARDS_LIST[i][1].id, card_id)"""
            if (HAND_CARDS_LIST[i][0] == in_hand_id and HAND_CARDS_LIST[i][1].id == card_id):
                #[site_img_id, site] = random.choice([["small", "vert"], ["small_right", "hori"]])
                player_card_river.add_card(
                    (HAND_CARDS_LIST[i][1].id, "small"), "vert")
                HAND_CARDS_LIST[i][1].mahjong_box.move_ip(-1000, -1000)
                HAND_CARDS_LIST[i][1].kill()
                del HAND_CARDS_LIST[i]
                is_match = 1
                break
            i += 1
        try:
            if DEAL_CARD[0] == in_hand_id and DEAL_CARD[1].id == card_id:
                player_card_river.add_card((DEAL_CARD[1].id, "small"), "vert")
                DEAL_CARD[0] = -1
                DEAL_CARD[1].mahjong_box.move_ip(-1000, -1000)
                DEAL_CARD[1].kill()
                is_match = 1
        except:
            pass
        if is_match == 0:
            pass
           # print(f"unmatch:{in_hand_id},{card_id}")
        # print()
        # for h in HAND_CARDS_LIST:
        #   #print(h[1].id)
        # print()
        if IS_PLAY_MULTI == 1:
            if IS_MULTI_DEAL==1:
                IS_MULTI_DEAL=0
                combine_card("down")
            sort("down")
        else:
            print("set")
            time_event.set()  # 不使用wait
        player.is_my_turn = False


class Card_river(pygame.sprite.Sprite):  # 牌河物件(不可點擊)
    def __init__(self, x, y, site):  # xy為牌河大框左上角座標, site="down","right","up","left"
        pygame.sprite.Sprite.__init__(self)
        self.image = null_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        # 方向
        self.site = site
        #一排最多有幾個小麻將, 當前排有幾個小麻將
        self.max_row_num = 6
        self.current_row_num = 0
        # 當前小麻將xy數值
        self.current_x = 0
        self.current_y = 0
        # 每排起始x
        self.row_start_x = 0
        # 重新配置
        if self.site == "down":
            self.river_box_width = SMALL_MAHJONG_WIDTH * \
                (self.max_row_num-1)+SMALL_MAHJONG_HEIGHT
            self.river_box_height = SMALL_MAHJONG_HEIGHT*3
            self.current_x = self.rect.left
            self.current_y = self.rect.top
            self.row_start_x = self.current_x
        if self.site == "right":
            self.river_box_width = SMALL_MAHJONG_HEIGHT*3
            self.river_box_height = SMALL_MAHJONG_WIDTH * \
                (self.max_row_num-1)+SMALL_MAHJONG_HEIGHT
            self.current_x = self.rect.left
            self.current_y = self.rect.top + self.river_box_height
            self.row_start_x = self.current_y
        if self.site == "up":
            self.river_box_width = SMALL_MAHJONG_WIDTH * \
                (self.max_row_num-1)+SMALL_MAHJONG_HEIGHT
            self.river_box_height = SMALL_MAHJONG_HEIGHT*3
            self.current_x = self.rect.left + self.river_box_width
            self.current_y = self.rect.top + self.river_box_height - SMALL_MAHJONG_HEIGHT
            self.row_start_x = self.current_x
        if self.site == "left":
            self.river_box_width = SMALL_MAHJONG_HEIGHT*3
            self.river_box_height = SMALL_MAHJONG_WIDTH * \
                (self.max_row_num-1)+SMALL_MAHJONG_HEIGHT
            self.current_x = self.rect.left + self.river_box_width - SMALL_MAHJONG_HEIGHT
            self.current_y = self.rect.top
            self.row_start_x = self.current_y
        # 牌河框
        self.river_box = pygame.Rect(
            self.rect.left, self.rect.top, self.river_box_width, self.river_box_height)
        # 小麻將列表
        self.cards = []  # id(小麻將名稱,小麻將方向),x座標,y座標,圖片
        # 最後一張的id(小麻將名稱,小麻將方向)
        self.last_card_id = ("", "")
        # 最後一張的xy
        self.next_x = 0
        self.next_y = 0
        # 是否從牌河拿過牌
        self.is_take = False

    def update(self):
        # 畫框
        pygame.draw.rect(screen, BLACK, self.river_box, 2)
        # 畫麻將&麻將框
        i = 0
        while i < len(self.cards):
            screen.blit(self.cards[i][3], (self.cards[i][1], self.cards[i][2]))
            small_mahjong_box = self.cards[i][3].get_rect()
            small_mahjong_box.left = self.cards[i][1]
            small_mahjong_box.top = self.cards[i][2]
            pygame.draw.rect(screen, BLACK, small_mahjong_box, 1)
            i += 1

    def add_card(self, id, type):  # 傳入要畫的圖片id(小麻將名稱,小麻將方向), type="vert","hori" (直放/橫放)
        if not self.is_take:
            (x, y) = self.position_calculate(type)
        else:
            (x, y) = (self.next_x, self.next_y)
            self.is_take = False
        card_img = SMALL_MAHJONG_IMG_DICT[id[0]][id[1]]
        self.cards.append([id, x, y, card_img])
        # print(self.current_row_num,self.current_x,self.current_y)
        self.last_card_id = id[0]

    def position_calculate(self, type):  # 計算下一顆要放的xy位置
        x = 0
        y = 0
        # variation為非換行時的座標變化量
        if type == "vert":
            variation = SMALL_MAHJONG_WIDTH
        if type == "hori":
            variation = SMALL_MAHJONG_HEIGHT

        if self.site == "down":  # 自己
            if self.current_row_num < self.max_row_num:
                x = self.current_x
                self.current_x += variation
                y = self.current_y
                self.current_row_num += 1
            else:
                self.current_row_num = 1
                self.current_x = self.row_start_x + variation
                self.current_y += SMALL_MAHJONG_HEIGHT
                x = self.row_start_x
                y = self.current_y

        if self.site == "right":  # 右邊(下家)
            if self.current_row_num < self.max_row_num:
                x = self.current_x
                y = self.current_y
                self.current_y -= variation
                self.current_row_num += 1
            else:
                self.current_row_num = 1
                self.current_x += SMALL_MAHJONG_HEIGHT
                self.current_y = self.row_start_x - variation
                x = self.current_x
                y = self.row_start_x
            y -= variation

        if self.site == "up":  # 上面(對家)
            if self.current_row_num < self.max_row_num:
                x = self.current_x
                self.current_x -= variation
                y = self.current_y
                self.current_row_num += 1
            else:
                self.current_row_num = 1
                self.current_x = self.row_start_x - variation
                self.current_y -= SMALL_MAHJONG_HEIGHT
                x = self.row_start_x
                y = self.current_y
            x -= variation

        if self.site == "left":  # 左邊(上家)
            if self.current_row_num < self.max_row_num:
                x = self.current_x
                y = self.current_y
                self.current_y += variation
                self.current_row_num += 1
            else:
                self.current_row_num = 1
                self.current_x -= SMALL_MAHJONG_HEIGHT
                self.current_y = self.row_start_x + variation
                x = self.current_x
                y = self.row_start_x
        return (x, y)

    def get_last_card_id(self):
        return self.last_card_id

    def del_last_card(self):
        self.next_x = self.cards[len(self.cards)-1][1]
        self.next_y = self.cards[len(self.cards)-1][2]
        del self.cards[len(self.cards)-1]
        self.is_take = True


class Dora_Mountain(pygame.sprite.Sprite):  # 算了啦
    def __init__(self, x, y, type=""):  # xy為5墩寶牌山大框左上角座標
        pygame.sprite.Sprite.__init__(self)
        self.image = null_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.kong_mountain = []
        # 當前最左邊小麻將物件xy座標
        self.current_x = x
        self.current_y = y
        # 表寶牌(小麻將物件list)
        self.dora_cards = []
        # 裏寶牌(id list)
        self.inner_dora_cards = []
        # 寶牌山框
        self.dora_box_width = SMALL_MAHJONG_WIDTH*5
        self.dora_box_height = SMALL_MAHJONG_HEIGHT
        self.dora_mountain_box = pygame.Rect(
            self.rect.left, self.rect.top, self.dora_box_width, self.dora_box_height)
        # 目前寶牌翻出數量
        self.flip_out_num = 0
        self.next_flip_index = 0
        self.type = type

    def update(self):
        pygame.draw.rect(screen, BLACK, self.dora_mountain_box, 2)

    def dora_init(self, id=""):
        global CARD_MOUNTAIN
        global play_single_sprites
        if self.type == "multi":
            i = 0
            while i < 5:
                small_mahjong = Small_Mahjong_Img(
                    self.current_x + (i*SMALL_MAHJONG_WIDTH), self.current_y, SMALL_MAHJONG_IMG_DICT["back"]["down"])
                self.dora_cards.append(small_mahjong)
                play_multi_sprites.add(small_mahjong)
                i += 1
            self.flip_dora(id)
        else:
            # 抓槓牌四張
            i = 0
            while i < 4:
                self.kong_mountain.append(
                    CARD_MOUNTAIN[(len(CARD_MOUNTAIN)-1)])
                del CARD_MOUNTAIN[(len(CARD_MOUNTAIN)-1)]
                i += 1
            # 抓寶牌十張
            i = 0
            while i < 5:
                small_mahjong = Small_Mahjong(
                    CARD_MOUNTAIN[(len(CARD_MOUNTAIN)-1)], self.current_x + (i*SMALL_MAHJONG_WIDTH), self.current_y, "down", BACK_OR_FRONT)
                self.dora_cards.append(small_mahjong)
                play_single_sprites.add(small_mahjong)
                del CARD_MOUNTAIN[(len(CARD_MOUNTAIN)-1)]
                self.inner_dora_cards.append(
                    CARD_MOUNTAIN[(len(CARD_MOUNTAIN)-1)])
                del CARD_MOUNTAIN[(len(CARD_MOUNTAIN)-1)]
                i += 1

            self.flip_dora()

    def deal(self, site):  # 發牌, type="","draw"
        global MAHJONG_BUTTON_LIST
        global play_single_sprites
        global play_multi_sprites
        global HAND_CARDS_LIST
        global RIGHT_HAND_CARDS_LIST
        global UP_HAND_CARDS_LIST
        global LEFT_HAND_CARDS_LIST
        global CARD_MOUNTAIN
        #global hand_card_startx
        #global hand_card_starty
        global DEAL_CARD
        global SMALL_DEAL_CARD
        if site == "down":
            x = HAND_CARDS_STARTX + MAHJONG_WIDTH * (len(HAND_CARDS_LIST)+1)
            DEAL_CARD = [len(HAND_CARDS_LIST), Mahjong(
                self.kong_mountain[0], x, HAND_CARDS_STARTY)]
            DEAL_CARD[1].in_hand_id = DEAL_CARD[0]

            #hand_card_startx += MAHJONG_WIDTH

        if site == "right":
            y = RIGHT_HAND_CARD_STARTY - \
                (SMALL_MAHJONG_WIDTH) * (len(RIGHT_HAND_CARDS_LIST) + 1)
            SMALL_DEAL_CARD = [len(RIGHT_HAND_CARDS_LIST), Small_Mahjong(
                self.kong_mountain[0], RIGHT_HAND_CARD_STARTX, y, site, BACK_OR_FRONT)]
            SMALL_DEAL_CARD[1].in_hand_id = SMALL_DEAL_CARD[0]

        if site == "up":
            x = UP_HAND_CARD_STARTX - SMALL_MAHJONG_WIDTH * \
                (len(UP_HAND_CARDS_LIST) + 1)
            SMALL_DEAL_CARD = [len(UP_HAND_CARDS_LIST), Small_Mahjong(
                self.kong_mountain[0], x, UP_HAND_CARD_STARTY, site, BACK_OR_FRONT)]
            SMALL_DEAL_CARD[1].in_hand_id = SMALL_DEAL_CARD[0]

        if site == "left":

            y = LEFT_HAND_CARD_STARTY + SMALL_MAHJONG_WIDTH * \
                (len(LEFT_HAND_CARDS_LIST) + 1)
            SMALL_DEAL_CARD = [len(LEFT_HAND_CARDS_LIST), Small_Mahjong(
                self.kong_mountain[0], LEFT_HAND_CARD_STARTX, y, site, BACK_OR_FRONT)]
            SMALL_DEAL_CARD[1].in_hand_id = SMALL_DEAL_CARD[0]

        #
        if site == "down":
            play_single_sprites.add(DEAL_CARD[1])  # 單人
            play_multi_sprites.add(DEAL_CARD[1])  # 多人
            MAHJONG_BUTTON_LIST.append(DEAL_CARD[1])
        else:
            play_single_sprites.add(SMALL_DEAL_CARD[1])  # 單人
            play_multi_sprites.add(SMALL_DEAL_CARD[1])  # 多人

        del self.kong_mountain[0]
        # 牌山-1張牌
        del CARD_MOUNTAIN[(len(CARD_MOUNTAIN)-1)]

        # 寶牌翻牌
        self.flip_dora()

    def flip_dora(self, id=""):  # 寶牌翻牌
        global play_multi_sprites
        if id == "":
            self.flip_out_num += 1
            self.dora_cards[self.next_flip_index].to_front()
            self.next_flip_index += 1
        else:
            print("hi", id)
            small_mahjong = Small_Mahjong_Img(
                self.current_x + (self.next_flip_index*SMALL_MAHJONG_WIDTH), self.current_y, SMALL_MAHJONG_IMG_DICT[id]["small"])
            self.dora_cards[self.next_flip_index].kill()
            del self.dora_cards[self.next_flip_index]
            self.dora_cards.insert(self.next_flip_index, small_mahjong)
            play_multi_sprites.add(small_mahjong)
            self.next_flip_index += 1
            self.flip_out_num += 1


class Mahjong_Img(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


class Small_Mahjong_Img(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


class Small_Mahjong(pygame.sprite.Sprite):  # 麻將物件(不可點擊)/小麻將
    def __init__(self, id, x, y, site, is_back=False):  # id = 圖片字典index
        pygame.sprite.Sprite.__init__(self)
        self.id = id  # 牌名
        if id != "":
            self.down_image = SMALL_MAHJONG_IMG_DICT[self.id]['small']
            self.right_image = SMALL_MAHJONG_IMG_DICT[self.id]['small_right']
            self.up_image = SMALL_MAHJONG_IMG_DICT[self.id]['small_up']
            self.left_image = SMALL_MAHJONG_IMG_DICT[self.id]['small_left']
        else:
            self.down_image = SMALL_MAHJONG_IMG_DICT["back"]["down"]
            self.right_image = SMALL_MAHJONG_IMG_DICT["back"]["right"]
            self.up_image = SMALL_MAHJONG_IMG_DICT["back"]["up"]
            self.left_image = SMALL_MAHJONG_IMG_DICT["back"]["left"]
        self.back_down_image = SMALL_MAHJONG_IMG_DICT["back"]["down"]
        self.back_right_image = SMALL_MAHJONG_IMG_DICT["back"]["right"]
        self.back_up_image = SMALL_MAHJONG_IMG_DICT["back"]["up"]
        self.back_left_image = SMALL_MAHJONG_IMG_DICT["back"]["left"]
        self.site = site
        if site == "down":
            self.image = self.down_image
            self.back_image = self.back_down_image
        if site == "right":
            self.image = self.right_image
            self.back_image = self.back_right_image
        if site == "up":
            self.image = self.up_image
            self.back_image = self.back_up_image
        if site == "left":
            self.image = self.left_image
            self.back_image = self.back_left_image
        if is_back:
            if site == "down":
                self.image = self.back_down_image
            if site == "right":
                self.image = self.back_right_image
            if site == "up":
                self.image = self.back_up_image
            if site == "left":
                self.image = self.back_left_image

        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y

        self.in_hand_id = 0

        # self.image.set_colorkey(BLACK)
        # 縱向 原圖

    def update(self):
        pass

    def change_site(self, site):  # 轉方向+重新定框
        if site == "down":
            self.image = self.down_image
        if site == "right":
            self.image = self.right_image
        if site == "up":
            self.image = self.up_image
        if site == "left":
            self.image = self.left_image

        self.rect = self.image.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y

    def to_back(self):
        if self.site == "down":
            self.image = self.back_down_image
        if self.site == "right":
            self.image = self.back_right_image
        if self.site == "up":
            self.image = self.back_up_image
        if self.site == "left":
            self.image = self.back_left_image

    def to_front(self):
        if self.site == "down":
            self.image = self.down_image
        if self.site == "right":
            self.image = self.right_image
        if self.site == "up":
            self.image = self.up_image
        if self.site == "left":
            self.image = self.left_image


OUT_CARD_ID = ""


class Mahjong(pygame.sprite.Sprite):  # 麻將物件(可點擊)/麻將按鈕
    def __init__(self, id, x, y):  # id = 圖片字典index
        pygame.sprite.Sprite.__init__(self)
        self.id = id  # 牌名
        self.image = MAHJONG_IMG_DICT[self.id]
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.mahjong_box = pygame.Rect(
            self.rect.left, self.rect.top, self.rect.width, self.rect.height)
        self.active = False
        self.active_y = y - 20
        self.inactive_y = y
        self.in_hand_id = 0

    def update(self):
        if self.active:
            self.rect.top = self.active_y
        else:
            self.rect.top = self.inactive_y
        #pygame.draw.rect(screen, BLACK, self.mahjong_box, 10)

    def click(self):
        global OUT_CARD_ID
        if IS_PLAY_MULTI == 1:
            OUT_CARD_ID = self.id
            return (self.id, self.in_hand_id)
        else:
            return (self.id, self.in_hand_id)


VICE_DEWS_BUTTON_LIST = []
VICE_DEWS_BUTTON_STARTX = 430
VICE_DEWS_BUTTON_STARTY = 480
VICE_DEWS_BG_WIDTH = 108
VICE_DEWS_BG_HEIGHT = 72


class Vice_Dews_Button(pygame.sprite.Sprite):  # 鳴牌組合選擇按鈕
    def __init__(self, x, y, type, target_cards=[], source_site=""):
        # target_cards:兩個小麻將id
        # type: chi, pong
        # source: right, up, left
        pygame.sprite.Sprite.__init__(self)
        global play_single_sprites
        global play_multi_sprites
        global right_card_river
        global up_card_river
        global left_card_river
        self.source_site = source_site
        self.type = type

        #self.image = vice_dews_choice_bg_img
        self.image = null_img
        self.vice_dews_bg_img = vice_dews_choice_bg_img
        self.vice_dews_bg_rect = self.vice_dews_bg_img.get_rect()
        self.vice_dews_bg_rect.left = x
        self.vice_dews_bg_rect.top = y

        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.target_cards_id_list = []
        if self.type == "chi":
            i = 0
            while i < len(target_cards):
                self.target_cards_id_list.append(target_cards[i])
                i += 1
        #    self.small_mahjonh1 = Small_Mahjong(self.target_cards_id_list[0],self.rect.left+(SMALL_MAHJONG_WIDTH/2),self.rect.top+(SMALL_MAHJONG_HEIGHT/4),"down")
        #    self.small_mahjonh2 = Small_Mahjong(self.target_cards_id_list[1],self.rect.left+(SMALL_MAHJONG_WIDTH/2)+SMALL_MAHJONG_WIDTH,self.rect.top+(SMALL_MAHJONG_HEIGHT/4),"down")
            self.small_mahjonh1_img = SMALL_MAHJONG_IMG_DICT[self.target_cards_id_list[0]]["small"]
            self.small_mahjonh2_img = SMALL_MAHJONG_IMG_DICT[self.target_cards_id_list[1]]["small"]
        elif self.type == "pong":
            if source_site == "right":
                self.target_card_id = right_card_river.get_last_card_id()
            elif source_site == "up":
                self.target_card_id = up_card_river.get_last_card_id()
            elif source_site == "left":
                self.target_card_id = left_card_river.get_last_card_id()
            #self.small_mahjonh1 = Small_Mahjong(self.target_card_id,self.rect.left+(SMALL_MAHJONG_WIDTH/2),self.rect.top+(SMALL_MAHJONG_HEIGHT/4),"down")
            #self.small_mahjonh2 = Small_Mahjong(self.target_card_id,self.rect.left+(SMALL_MAHJONG_WIDTH/2)+SMALL_MAHJONG_WIDTH,self.rect.top+(SMALL_MAHJONG_HEIGHT/4),"down")
            self.small_mahjonh1_img = SMALL_MAHJONG_IMG_DICT[self.target_card_id]["small"]
            self.small_mahjonh2_img = SMALL_MAHJONG_IMG_DICT[self.target_card_id]["small"]
        # play_single_sprites.add(self.small_mahjonh1)
        # play_single_sprites.add(self.small_mahjonh2)
        # play_multi_sprites.add(self.small_mahjonh1)
        # play_multi_sprites.add(self.small_mahjonh2)
        #self.vice_dews_box = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, self.rect.height)

        self.vice_dews_box = pygame.Rect(
            self.rect.left, self.rect.top, VICE_DEWS_BG_WIDTH, VICE_DEWS_BG_HEIGHT)
        self.small_mahjonh1_img_rect = self.small_mahjonh1_img.get_rect()
        self.small_mahjonh1_img_rect.left = self.rect.left + \
            (SMALL_MAHJONG_WIDTH/2)
        self.small_mahjonh1_img_rect.top = self.rect.top + \
            (SMALL_MAHJONG_HEIGHT/4)

        self.small_mahjonh2_img_rect = self.small_mahjonh2_img.get_rect()
        self.small_mahjonh2_img_rect.left = self.rect.left + \
            (SMALL_MAHJONG_WIDTH/2)+SMALL_MAHJONG_WIDTH
        self.small_mahjonh2_img_rect.top = self.rect.top + \
            (SMALL_MAHJONG_HEIGHT/4)

    def update(self):
        global screen
        screen.blit(self.vice_dews_bg_img, self.vice_dews_bg_rect)
        screen.blit(self.small_mahjonh1_img, self.small_mahjonh1_img_rect)
        screen.blit(self.small_mahjonh2_img, self.small_mahjonh2_img_rect)

    def click(self):
        global player
        global VICE_DEWS_BUTTON_LIST
        if self.type == "chi":
            player.chi(self.target_cards_id_list)
        elif self.type == "pong":
            player.pong(self.source_site)
        i = 0
        while i < len(VICE_DEWS_BUTTON_LIST):
            VICE_DEWS_BUTTON_LIST[i].vice_dews_box.move_ip(-1000, -1000)
            # VICE_DEWS_BUTTON_LIST[i].small_mahjonh1.kill()
            # VICE_DEWS_BUTTON_LIST[i].small_mahjonh2.kill()
            VICE_DEWS_BUTTON_LIST[i].kill()
            i += 1
        VICE_DEWS_BUTTON_LIST = []
        if IS_PLAY_MULTI == 1:
            player.is_my_turn = True
            pass
        else:
            print("set")
            time_event.set()


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, type, have_img, img=null_img, width=0, height=0):  # 無預設值參數不可放在有預設值參數的右邊
        pygame.sprite.Sprite.__init__(self)
        # have_img: True, False, 有無圖片
        # type:login, logout, setting, left_arrow, right_arrow, chi, pong, kong, ron, cancel, ...
        self.type = type
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.width = 0
        self.height = 0
        if have_img:
            self.width = self.rect.width
            self.height = self.rect.height
        else:
            self.image.set_colorkey(BLACK)
            self.width = width
            self.height = height

        self.button_box = pygame.Rect(x, y, self.width, self.height)
        self.color = BLACK

    def update(self):  # 更新函式
        #pygame.draw.rect(screen, self.color, self.button_box, 3)
        pass

    def click(self):
        global IS_LOGIN
        global IS_MENU
        global IS_PLAY_SINGLE
        global IS_PLAY_MULTI
        global login_init
        global menu_init
        global play_multi_init
        global play_single_init
        global IS_PLAY_MULTI_END
        global play_multi_end_init
        global IS_WAIT
        global wait_init
        global IS_PLAY_SINGLE_END
        global play_single_end_init
        if self.type == "login":
            IS_LOGIN = 0
            IS_MENU = 1
            login_init = True
            menu_init = True
            self.button_box.move_ip(-1000, -1000)
            self.kill()

        if self.type == "single_mode":
            IS_MENU = 0
            IS_PLAY_SINGLE = 1
            menu_init = True
            play_single_init = True
            self.button_box.move_ip(-1000, -1000)
            self.kill()

        if self.type == "multi_mode":
            IS_MENU = 0
            #IS_PLAY_MULTI = 1
            IS_WAIT = 1
            wait_init = True
            menu_init = True
            #play_multi_init = True
            self.button_box.move_ip(-1000, -1000)
            self.kill()

        if self.type == "end":
            IS_MENU = 1
            IS_PLAY_MULTI_END = 0
            IS_PLAY_SINGLE_END = 0
            menu_init = True
            play_multi_end_init = True
            play_single_end_init = True
            self.button_box.move_ip(-1000, -1000)
            self.kill()
            print("ayaya")


class Image_button(pygame.sprite.Sprite):
    # 建構子
    def __init__(self, x, y, width, height):
        # side = 0 (左) side = 1 (右)
        pygame.sprite.Sprite.__init__(self)
        # self.image.set_colorkey(BLACK)
        # 物件變數
        self.active = True
        self.button_box = pygame.Rect(x, y, width, height)

        # self.init_cSocket.send(str(USER).encode('utf-8'))

    def update(self):
        pass

    def go(self):
        pass

    def register(self):
        pass

# class ?(pygame.sprite.Sprite): #傳入圖片, xy座標, 時間 =>可決定在某個位置讓某個圖片持續出現某個時間


IS_RON = 0
IS_TSUMO = 0
# 用於Playing_Button跟t_pong_kong之間的溝通
IS_PONG = 0
IS_KONG = 0
IS_CHI = 0

# class


class Playing_Button(pygame.sprite.Sprite):  # 吃碰槓和取消,
    def __init__(self, x, y, type, img, target_cards=[], pong_kong_source_site="", pong_kong_card_id="", ron_card_id=""):  # 無預設值參數不可放在有預設值參數的右邊
        pygame.sprite.Sprite.__init__(self)
        # target_cards : 吃 組合牌id list
        # type: chi, pong, kong, ron, cancel, ...
        self.ron_card_id = ron_card_id
        self.pong_kong_card_id = pong_kong_card_id
        self.type = type
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.width = 0
        self.height = 0
        self.target_cards_id_lists = []
        i = 0
        while i < len(target_cards):
            self.target_cards_id_lists.append(target_cards[i])
            i += 1
        self.width = self.rect.width
        self.height = self.rect.height

        self.button_box = pygame.Rect(x, y, self.width, self.height)
        self.color = BLACK

        self.source_site = pong_kong_source_site

    def update(self):  # 更新函式
        #pygame.draw.rect(screen, self.color, self.button_box, 3)
        pass

    def click(self):
        global IS_SHOW_COUNTDOWN
        global player
        global PLAYING_BUTTON_LIST
        global IS_CHI
        global IS_PONG
        global IS_KONG
        global VICE_DEWS_BUTTON_LIST
        global time_event
        global play_single_sprites
        global play_multi_sprites
        global IS_PONGED_OR_KONGED
        global IS_RON
        global IS_TSUMO
        global DOWN_TSUMO
        global DOWN_RON
        VICE_DEWS_BUTTON_LIST = []
        is_cancel = False

        i = 0
        while i < len(PLAYING_BUTTON_LIST):
            PLAYING_BUTTON_LIST[i].button_box.move_ip(-1000, -1000)
            PLAYING_BUTTON_LIST[i].kill()
            i += 1
        PLAYING_BUTTON_LIST = []
        print("清空")

        if self.type == "chi":
            if IS_PLAY_MULTI == 1:
                if len(self.target_cards_id_lists) == 1:  # 如果能吃的只有一組就直接呼叫吃
                    player.chi(self.target_cards_id_lists[0])
                    IS_CHI = 1
                    player.is_my_turn = True
                else:  # 不然就呼叫組合按鈕
                    i = 0
                    while i < len(self.target_cards_id_lists):
                        vd_button = Vice_Dews_Button(VICE_DEWS_BUTTON_STARTX+(
                            i*VICE_DEWS_BG_WIDTH), VICE_DEWS_BUTTON_STARTY+VICE_DEWS_BG_HEIGHT, "chi", self.target_cards_id_lists[i])
                        play_single_sprites.add(vd_button)
                        play_multi_sprites.add(vd_button)
                        VICE_DEWS_BUTTON_LIST.append(vd_button)
                        i += 1
            else:
                if IS_PONGING_OR_KONGING == 1:  # 如果別家正在思考要不要碰槓
                    if VICE_DEWS_SITE_CHI == "down" and VICE_DEWS_SITE_PONG_KONG == "down":
                        IS_PONGED_OR_KONGED = 0
                    else:
                        print("clear & wait")
                        time_event.clear()
                        time_event.wait()
                if IS_PONGED_OR_KONGED == 0:  # 如果別家選擇不要碰槓
                    if len(self.target_cards_id_lists) == 1:  # 如果能吃的只有一組就直接呼叫吃
                        player.chi(self.target_cards_id_lists[0])
                        is_cancel = True
                    else:  # 不然就呼叫組合按鈕

                        i = 0
                        while i < len(self.target_cards_id_lists):
                            vd_button = Vice_Dews_Button(VICE_DEWS_BUTTON_STARTX+(
                                i*VICE_DEWS_BG_WIDTH), VICE_DEWS_BUTTON_STARTY+VICE_DEWS_BG_HEIGHT, "chi", self.target_cards_id_lists[i])
                            play_single_sprites.add(vd_button)
                            play_multi_sprites.add(vd_button)
                            VICE_DEWS_BUTTON_LIST.append(vd_button)
                            i += 1

                    IS_CHI = 1
                    # self.kill()

        if self.type == "pong":
            if IS_PLAY_MULTI == 1:
                player.pong(self.source_site, self.pong_kong_card_id)
                player.is_my_turn = True
                send_to_server(["pong", self.pong_kong_card_id])
            else:
                is_cancel = True
                player.pong(self.source_site)
                print("is_my_turn=True")
                # player.is_my_turn=True
            IS_PONG = 1
            # self.kill()

        if self.type == "kong":
            if IS_PLAY_MULTI == 1:
                player.kong(self.source_site)
                # player.is_my_turn=True
                send_to_server(["kong", self.pong_kong_card_id])
            else:
                is_cancel = True
                player.kong(self.source_site)
            IS_KONG = 1
            # self.kill()

        if self.type == "ron":
            if IS_PLAY_MULTI == 1:
                player.ron(self.ron_card_id)
                send_to_server(["ron", self.ron_card_id])
            else:
                DOWN_RON=1
                time.sleep(5)
                is_cancel = True
                player.tsumo(DEAL_CARD[1].id)
            IS_RON = 1

        if self.type == "tsumo":
            if IS_PLAY_MULTI == 1:
                player.tsumo(self.ron_card_id)
                send_to_server(["tsumo", self.ron_card_id])
            else:
                DOWN_TSUMO=1
                time.sleep(5)
                is_cancel = True
                player.tsumo(DEAL_CARD[1].id)
            IS_TSUMO = 1

        if self.type == "cancel":
            is_cancel = True
            if IS_PLAY_MULTI == 1:
                IS_SHOW_COUNTDOWN = 0
                send_to_server(["cancel"])

        if IS_PLAY_MULTI == 1:
            pass
        elif len(self.target_cards_id_lists) == 1 or is_cancel:
            print("set")
            time_event.set()
        # else:
        #    time_event.set()


class Input_num_box(pygame.sprite.Sprite):  # 帳號, 密碼
    def __init__(self, info_text, x, y, init_text, size, active_info, input_type):
        # input_type: USER, PASS
        self.intext = init_text
        self.intext_hide = "*" * len(init_text)
        self.password = init_text
        self.type = input_type
        pygame.sprite.Sprite.__init__(self)
        self.image = null_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        if input_type == "PASS":
            if str(init_text).isdigit():
                self.num = int(init_text)
                self.intext = str(init_text)
        if not init_text == "" and input_type == "USER":
            self.iptext = str(init_text)
            self.intext = str(init_text)

        self.font = pygame.font.Font(None, size)
        self.input_box = pygame.Rect(100, 100, 140, size)
        self.active = False

        self.text_surface = self.font.render(self.intext, True, WHITE)
        input_box_width = max(100, self.text_surface.get_width()+10)
        self.input_box.w = input_box_width

        self.info_box = pygame.Rect(100, 100, 140, size)
        self.info_text = info_text
        self.info_surface = self.font.render(self.info_text, True, WHITE)

        self.active_info_box = pygame.Rect(100, 100, 140, size-15)
        self.active_info_text = active_info
        self.active_font = pygame.font.Font(None, size-7)
        self.active_info_surface = self.active_font.render(
            self.active_info_text, True, WHITE)

    def text_save(self):
        global USER
        global PASS
        if self.type == "USER" and self.intext != "":
            USER = self.intext
        elif self.type == "USER":
            self.intext = USER

        if self.type == "PASS" and self.intext_hide != "" and self.intext != "":
            self.password = self.intext
            PASS = self.intext
            self.intext_hide = "*" * len(self.intext_hide)
        elif self.type == "PASS":
            self.intext_hide = "*" * len(self.password)

    def update(self):

        # 畫

        # info
        self.info_surface = self.font.render(self.info_text, True, WHITE)
        info_box_width = max(50, self.info_surface.get_width()+10)
        self.info_box.w = info_box_width
        self.info_box.x = self.rect.x
        self.info_box.y = self.rect.y
        screen.blit(self.info_surface, (self.info_box.x+5, self.info_box.y+5))

        # 數字
        if self.type == "PASS":
            # 字體.render(要畫的文字,平滑值,文字顏色,背景顏色(沒填就是沒有)) #將文字以此字體渲染成可畫物件
            self.text_surface = self.font.render(self.intext_hide, True, WHITE)
        else:
            # 字體.render(要畫的文字,平滑值,文字顏色,背景顏色(沒填就是沒有)) #將文字以此字體渲染成可畫物件
            self.text_surface = self.font.render(self.intext, True, WHITE)
        input_box_width = max(100, self.text_surface.get_width()+10)
        self.input_box.w = input_box_width
        self.input_box.x = self.rect.x + self.info_box.w
        self.input_box.y = self.rect.y
        screen.blit(self.text_surface,
                    (self.input_box.x+5, self.input_box.y+5))  # 畫文字

        # active_info
        self.active_info_surface = self.active_font.render(
            self.active_info_text, True, WHITE)
        info_box_width = max(100, self.active_info_surface.get_width()+10)
        self.active_info_box.w = info_box_width
        self.active_info_box.x = self.input_box.x + self.input_box.w + 10
        self.active_info_box.y = self.rect.y + 7

        if self.active and (self.type == "USER" or self.type == "PASS"):
            pygame.draw.rect(screen, WHITE, self.input_box, 3)  # 畫邊框
            screen.blit(self.active_info_surface,
                        (self.active_info_box.x+5, self.active_info_box.y+5))  # 畫文字


# 麻將圖片字典
MAHJONG_IMG_DICT = {"Man1": Man1_img, "Man2": Man2_img, "Man3": Man3_img, "Man4": Man4_img, "Man5": Man5_img, "Man6": Man6_img, "Man7": Man7_img, "Man8": Man8_img, "Man9": Man9_img, "Pin1": Pin1_img, "Pin2": Pin2_img, "Pin3": Pin3_img, "Pin4": Pin4_img, "Pin5": Pin5_img, "Pin6": Pin6_img, "Pin7": Pin7_img, "Pin8": Pin8_img, "Pin9": Pin9_img, "Sou1": Sou1_img,
                    "Sou2": Sou2_img, "Sou3": Sou3_img, "Sou4": Sou4_img, "Sou5": Sou5_img, "Sou6": Sou6_img, "Sou7": Sou7_img, "Sou8": Sou8_img, "Sou9": Sou9_img, "Ton": Ton_img, "Nan": Nan_img, "Shaa": Shaa_img, "Pei": Pei_img, "Chun": Chun_img, "Haku": Haku_img, "Hatsu": Hatsu_img, "Man5_red": Man5_red_img, "Pin5_red": Pin5_red_img, "Sou5_red": Sou5_red_img}
SMALL_MAHJONG_IMG_DICT = {"back": {"down": back_img, "right": back_right_img, "up": back_up_img, "left": back_left_img}, "Man1": {"small": small_Man1_img, "small_right": small_right_Man1_img, "small_up": small_up_Man1_img, "small_left": small_left_Man1_img}, "Man2": {"small": small_Man2_img, "small_right": small_right_Man2_img, "small_up": small_up_Man2_img, "small_left": small_left_Man2_img}, "Man3": {"small": small_Man3_img, "small_right": small_right_Man3_img, "small_up": small_up_Man3_img, "small_left": small_left_Man3_img}, "Man4": {"small": small_Man4_img, "small_right": small_right_Man4_img, "small_up": small_up_Man4_img, "small_left": small_left_Man4_img}, "Man5": {"small": small_Man5_img, "small_right": small_right_Man5_img, "small_up": small_up_Man5_img, "small_left": small_left_Man5_img}, "Man6": {"small": small_Man6_img, "small_right": small_right_Man6_img, "small_up": small_up_Man6_img, "small_left": small_left_Man6_img}, "Man7": {"small": small_Man7_img, "small_right": small_right_Man7_img, "small_up": small_up_Man7_img, "small_left": small_left_Man7_img}, "Man8": {"small": small_Man8_img, "small_right": small_right_Man8_img, "small_up": small_up_Man8_img, "small_left": small_left_Man8_img}, "Man9": {"small": small_Man9_img, "small_right": small_right_Man9_img, "small_up": small_up_Man9_img, "small_left": small_left_Man9_img}, "Pin1": {"small": small_Pin1_img, "small_right": small_right_Pin1_img, "small_up": small_up_Pin1_img, "small_left": small_left_Pin1_img}, "Pin2": {"small": small_Pin2_img, "small_right": small_right_Pin2_img, "small_up": small_up_Pin2_img, "small_left": small_left_Pin2_img}, "Pin3": {"small": small_Pin3_img, "small_right": small_right_Pin3_img, "small_up": small_up_Pin3_img, "small_left": small_left_Pin3_img}, "Pin4": {"small": small_Pin4_img, "small_right": small_right_Pin4_img, "small_up": small_up_Pin4_img, "small_left": small_left_Pin4_img}, "Pin5": {"small": small_Pin5_img, "small_right": small_right_Pin5_img, "small_up": small_up_Pin5_img, "small_left": small_left_Pin5_img}, "Pin6": {"small": small_Pin6_img, "small_right": small_right_Pin6_img, "small_up": small_up_Pin6_img, "small_left": small_left_Pin6_img}, "Pin7": {"small": small_Pin7_img, "small_right": small_right_Pin7_img, "small_up": small_up_Pin7_img, "small_left": small_left_Pin7_img}, "Pin8": {"small": small_Pin8_img, "small_right": small_right_Pin8_img, "small_up": small_up_Pin8_img, "small_left": small_left_Pin8_img}, "Pin9": {"small": small_Pin9_img, "small_right": small_right_Pin9_img, "small_up": small_up_Pin9_img, "small_left": small_left_Pin9_img}, "Sou1": {"small": small_Sou1_img, "small_right": small_right_Sou1_img,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      "small_up": small_up_Sou1_img, "small_left": small_left_Sou1_img}, "Sou2": {"small": small_Sou2_img, "small_right": small_right_Sou2_img, "small_up": small_up_Sou2_img, "small_left": small_left_Sou2_img}, "Sou3": {"small": small_Sou3_img, "small_right": small_right_Sou3_img, "small_up": small_up_Sou3_img, "small_left": small_left_Sou3_img}, "Sou4": {"small": small_Sou4_img, "small_right": small_right_Sou4_img, "small_up": small_up_Sou4_img, "small_left": small_left_Sou4_img}, "Sou5": {"small": small_Sou5_img, "small_right": small_right_Sou5_img, "small_up": small_up_Sou5_img, "small_left": small_left_Sou5_img}, "Sou6": {"small": small_Sou6_img, "small_right": small_right_Sou6_img, "small_up": small_up_Sou6_img, "small_left": small_left_Sou6_img}, "Sou7": {"small": small_Sou7_img, "small_right": small_right_Sou7_img, "small_up": small_up_Sou7_img, "small_left": small_left_Sou7_img}, "Sou8": {"small": small_Sou8_img, "small_right": small_right_Sou8_img, "small_up": small_up_Sou8_img, "small_left": small_left_Sou8_img}, "Sou9": {"small": small_Sou9_img, "small_right": small_right_Sou9_img, "small_up": small_up_Sou9_img, "small_left": small_left_Sou9_img}, "Ton": {"small": small_Ton_img, "small_right": small_right_Ton_img, "small_up": small_up_Ton_img, "small_left": small_left_Ton_img}, "Nan": {"small": small_Nan_img, "small_right": small_right_Nan_img, "small_up": small_up_Nan_img, "small_left": small_left_Nan_img}, "Shaa": {"small": small_Shaa_img, "small_right": small_right_Shaa_img, "small_up": small_up_Shaa_img, "small_left": small_left_Shaa_img}, "Pei": {"small": small_Pei_img, "small_right": small_right_Pei_img, "small_up": small_up_Pei_img, "small_left": small_left_Pei_img}, "Chun": {"small": small_Chun_img, "small_right": small_right_Chun_img, "small_up": small_up_Chun_img, "small_left": small_left_Chun_img}, "Haku": {"small": small_Haku_img, "small_right": small_right_Haku_img, "small_up": small_up_Haku_img, "small_left": small_left_Haku_img}, "Hatsu": {"small": small_Hatsu_img, "small_right": small_right_Hatsu_img, "small_up": small_up_Hatsu_img, "small_left": small_left_Hatsu_img}, "Man5_red": {"small": small_Man5_red_img, "small_right": small_right_Man5_red_img, "small_up": small_up_Man5_red_img, "small_left": small_left_Man5_red_img}, "Pin5_red": {"small": small_Pin5_red_img, "small_right": small_right_Pin5_red_img, "small_up": small_up_Pin5_red_img, "small_left": small_left_Pin5_red_img}, "Sou5_red": {"small": small_Sou5_red_img, "small_right": small_right_Sou5_red_img, "small_up": small_up_Sou5_red_img, "small_left": small_left_Sou5_red_img}}

# 剩餘麻將列表
REMAINING_MAHJONG_LIST = ["Man1", "Man1", "Man1", "Man1", "Man2", "Man2", "Man2", "Man2", "Man3", "Man3", "Man3", "Man3", "Man4", "Man4", "Man4", "Man4", "Man5", "Man5", "Man5", "Man6", "Man6", "Man6", "Man6", "Man7", "Man7", "Man7", "Man7", "Man8", "Man8", "Man8", "Man8", "Man9", "Man9", "Man9", "Man9", "Pin1", "Pin1", "Pin1", "Pin1", "Pin2", "Pin2", "Pin2", "Pin2", "Pin3", "Pin3", "Pin3", "Pin3", "Pin4", "Pin4", "Pin4", "Pin4", "Pin5", "Pin5", "Pin5", "Pin6", "Pin6", "Pin6", "Pin6", "Pin7", "Pin7", "Pin7", "Pin7", "Pin8", "Pin8", "Pin8", "Pin8", "Pin9",
                          "Pin9", "Pin9", "Pin9", "Sou1", "Sou1", "Sou1", "Sou1", "Sou2", "Sou2", "Sou2", "Sou2", "Sou3", "Sou3", "Sou3", "Sou3", "Sou4", "Sou4", "Sou4", "Sou4", "Sou5", "Sou5", "Sou5", "Sou6", "Sou6", "Sou6", "Sou6", "Sou7", "Sou7", "Sou7", "Sou7", "Sou8", "Sou8", "Sou8", "Sou8", "Sou9", "Sou9", "Sou9", "Sou9", "Ton", "Ton", "Ton", "Ton", "Nan", "Nan", "Nan", "Nan", "Shaa", "Shaa", "Shaa", "Shaa", "Pei", "Pei", "Pei", "Pei", "Chun", "Chun", "Chun", "Chun", "Haku", "Haku", "Haku", "Haku", "Hatsu", "Hatsu", "Hatsu", "Hatsu", "Man5_red", "Pin5_red", "Sou5_red"]

# 牌山
CARD_MOUNTAIN = []

# 麻將排序
MAHJONG_SORT_TABLE_LIST = ["Man1", "Man2", "Man3", "Man4", "Man5", "Man5_red", "Man6", "Man7", "Man8", "Man9", "Pin1", "Pin2", "Pin3", "Pin4", "Pin5", "Pin5_red", "Pin6",
                           "Pin7", "Pin8", "Pin9", "Sou1", "Sou2", "Sou3", "Sou4", "Sou5", "Sou5_red", "Sou6", "Sou7", "Sou8", "Sou9", "Ton", "Nan", "Shaa", "Pei", "Chun", "Haku", "Hatsu"]

#手牌, 二維列表, [順位,Mahjong物件]
HAND_CARDS_LIST = []
RIGHT_HAND_CARDS_LIST = []
UP_HAND_CARDS_LIST = []
LEFT_HAND_CARDS_LIST = []

# 連線全域變數
BUFF_SIZE = 4096
SERVER_IP = "127.0.0.1"
PORT = 6666
cSocket = 0

# event偵測列表
INPUT_BOX_LIST = []  # 輸入框物件列表
BUTTON_LIST = []  # 按鈕物件列表
MAHJONG_BUTTON_LIST = []  # 麻將按鈕物件列表
PLAYING_BUTTON_LIST = []  # 吃碰槓和取消按鈕列表

# login畫面全域變數
IS_LOGIN = 1  # 登入畫面控制變數
login_init = True  # 登入初始化控制變數
login_sprites = pygame.sprite.Group()  # 登入畫面精靈群組

# 主畫面全域變數
IS_MENU = 0  # 主畫面控制變數
menu_init = True  # 主畫面初始化控制變數
menu_sprites = pygame.sprite.Group()  # 主畫面精靈群組

# 等待中全域變數
IS_WAIT = 0  # 主畫面控制變數
wait_init = True

# 單人模式全域變數
IS_PLAY_SINGLE = 0  # 單人模式畫面控制變數
play_single_init = True  # 單人模式初始化控制變數
play_single_sprites = pygame.sprite.Group()  # 單人模式畫面精靈群組
player = Player()  # 玩家物件全域變數
dora_mountain = Dora_Mountain(10, 10)  # 寶牌山物件全域變數

# 多人模式全域變數
IS_PLAY_MULTI = 0  # 多人模式畫面控制變數
play_multi_init = True  # 多人模式初始化控制變數
play_multi_sprites = pygame.sprite.Group()  # 多人模式畫面精靈群組
player = Player()  # 玩家物件全域變數

# 單人結算畫面
IS_PLAY_SINGLE_END = 0
play_single_end_init = True
play_single_end_sprites = pygame.sprite.Group()

# 多人結算畫面
IS_PLAY_MULTI_END = 0
play_multi_end_init = True
play_multi_end_sprites = pygame.sprite.Group()

# 多執行緒函式
# 流程
SEED = 0
NO_DEAL = 0  # =1玩家不抽牌

VICE_DEWS_SITE_CHI = ""
VICE_DEWS_SITE_PONG_KONG = ""

# multi jump
main_send_cSocket = ""  # recv
main_recv_cSocket = ""  # send
sub_send_cSocket = ""  # recv
sub_recv_cSocket = ""  # send
IS_MULTI_ING = 0  # 連線狀態
RESULT = ""


def multi_play():
    global RECV_END
    global main_send_cSocket
    global main_recv_cSocket
    global sub_send_cSocket
    global sub_recv_cSocket
    global IS_MULTI_ING
    global RESULT
    print("multi_play")
    # send = recv server data
    main_send_cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_send_cSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    main_send_cSocket.connect(('127.0.0.1', 8880))
    main_send_cSocket.send(str(USERNAME).encode('utf-8'))

    # recv = send server data
    main_recv_cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_recv_cSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    main_recv_cSocket.connect(('127.0.0.1', 8883))
    main_recv_cSocket.send(str(USERNAME).encode('utf-8'))

    # send = recv server time data
    sub_send_cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sub_send_cSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sub_send_cSocket.connect(('127.0.0.1', 8881))
    sub_send_cSocket.send(str(USERNAME).encode('utf-8'))

    # recv = send server time interrupt
    sub_recv_cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sub_recv_cSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sub_recv_cSocket.connect(('127.0.0.1', 8882))
    sub_recv_cSocket.send(str(USERNAME).encode('utf-8'))

    IS_MULTI_ING = 1

    multi_recv_t = threading.Thread(
        target=main_multi_recv, args=(main_send_cSocket,))
    multi_recv_t.setDaemon(True)
    multi_recv_t.start()
    multi_recv_t.is_alive()
    #countdown_send_t = threading.Thread(target=countdown_send,args=(sub_send_cSocket,))
    # countdown_send_t.setDaemon(True)

    countdown_recv_t = threading.Thread(
        target=countdown_recv, args=(sub_send_cSocket,))
    countdown_recv_t.setDaemon(True)
    countdown_recv_t.start()

    while multi_recv_t.is_alive() and countdown_recv_t.is_alive():
        print("clear & wait")
        time_event.clear()
        time_event.wait()
        print("data_processing")
        data_processing()
        if RESULT == "leave":
            break
    print("multi_play end")


DATA_PROCESS_END = True

IS_MULTI_DEAL=0
def data_processing():
    global player
    global player_card_river
    global right_card_river
    global up_card_river
    global left_card_river
    global play_multi_sprites
    global dora_mountain
    global DATA_PROCESS_END
    global running
    global PLAYING_BUTTON_LIST
    global LEFT_CARD_NUM
    global IS_SHOW_LEFT_CARD_NUM
    global RON_CARD_ID
    global RON_HAND_CARD_ID_LIST
    global RON_VICE_DEWS_ID_LIST
    global IS_WIN
    global IS_PLAY_MULTI
    global play_multi_init
    global IS_PLAY_MULTI_END
    global play_multi_end_init
    global main_send_cSocket  # recv
    global main_recv_cSocket  # send
    global sub_send_cSocket  # recv
    global sub_recv_cSocket  # send
    global WIN_SITE
    global BUTTON_LIST
    global MAHJONG_BUTTON_LIST
    global PLAYING_BUTTON_LIST
    global VICE_DEWS_BUTTON_LIST
    global HAND_CARDS_LIST
    global RIGHT_HAND_CARDS_LIST
    global UP_HAND_CARDS_LIST
    global LEFT_HAND_CARDS_LIST
    global IS_MENU
    global menu_init
    global IS_WAIT
    global WAIT_PEOPLE_NUM
    global RESULT
    global IS_MULTI_DEAL

    DATA_PROCESS_END = False
    result = ""

    if RECEIVE_DATA[0] == "no_result_end":
        WIN_SITE = "流局"
        IS_WIN = 0
        IS_PLAY_MULTI = 0
        IS_PLAY_MULTI_END = 1
        play_multi_end_init = True

    if RECEIVE_DATA[0] == "wait_people":
        WAIT_PEOPLE_NUM = int(RECEIVE_DATA[1])

    if RECEIVE_DATA[0] == "init":
        IS_PLAY_MULTI = 1
        play_multi_init = True
        IS_WAIT = 0

        result = "init"
        player = Player(RECEIVE_DATA[1])
        player.is_my_turn = False
        player_card_river = Card_river(
            int((WIDTH/2)-((SMALL_MAHJONG_WIDTH*5+SMALL_MAHJONG_HEIGHT)/2)), 475, "down")
        play_multi_sprites.add(player_card_river)

        right_card_river = Card_river(
            760, (HEIGHT/2)-(SMALL_MAHJONG_HEIGHT*3)+30, "right")
        play_multi_sprites.add(right_card_river)

        up_card_river = Card_river(
            int((WIDTH/2)-((SMALL_MAHJONG_WIDTH*5+SMALL_MAHJONG_HEIGHT)/2)), 100, "up")
        play_multi_sprites.add(up_card_river)

        left_card_river = Card_river(
            376, (HEIGHT/2)-(SMALL_MAHJONG_HEIGHT*3)+30, "left")
        play_multi_sprites.add(left_card_river)

        # hand_card_startx = HAND_CARDS_STARTX  # 最右邊手牌x座標
        # hand_card_starty = HAND_CARDS_STARTY  # 最右邊手牌y座標
        # 手牌重置
        HAND_CARDS_LIST = []
        RIGHT_HAND_CARDS_LIST = []
        UP_HAND_CARDS_LIST = []
        LEFT_HAND_CARDS_LIST = []
        i = 0
        while i < 13:
            player.cards.append(RECEIVE_DATA[i+2])
            i += 1
        multi_deal(type="init")
        dora_mountain = Dora_Mountain(10, 10, "multi")
        play_multi_sprites.add(dora_mountain)
        dora_mountain.dora_init(RECEIVE_DATA[15])

    if RECEIVE_DATA[0] == "draw":
        result = "draw"
        player.is_my_turn = False
        if RECEIVE_DATA[1] == "down":
            IS_MULTI_DEAL=1
            player.deal_card = RECEIVE_DATA[2]
            print("is_my_turn=True")
            player.is_my_turn = True
            multi_deal("down")
        elif RECEIVE_DATA[1] == "right":
            multi_deal("right")
        elif RECEIVE_DATA[1] == "up":
            multi_deal("up")
        elif RECEIVE_DATA[1] == "left":
            multi_deal("left")
        # RECEIVE_DATA=[]

    if RECEIVE_DATA[0] == "out":
        result = "out"
        multi_out_cards(RECEIVE_DATA[1], RECEIVE_DATA[2])

    if RECEIVE_DATA[0] == "can_chi":
        result = "can_chi"
        i = 1
        can_chi_list = []
        while i+1 < len(RECEIVE_DATA):
            can_chi_list.append([RECEIVE_DATA[i], RECEIVE_DATA[i+1]])
            i += 2
        print("hi")
        # 吃按鈕
        chi_button = Playing_Button(
            760, 530, "chi", chi_img, can_chi_list)
        play_multi_sprites.add(chi_button)
        PLAYING_BUTTON_LIST.append(chi_button)
        # 取消按鈕
        cancel_button = Playing_Button(960, 530, "cancel", cancel_img)
        play_multi_sprites.add(cancel_button)
        PLAYING_BUTTON_LIST.append(cancel_button)

    if RECEIVE_DATA[0] == "other_chi":
        result = "other_chi"
        card_list = [RECEIVE_DATA[3], RECEIVE_DATA[4], RECEIVE_DATA[5]]
        if RECEIVE_DATA[1] == "down":
            player_card_river.del_last_card()
        elif RECEIVE_DATA[1] == "right":
            right_card_river.del_last_card()
        elif RECEIVE_DATA[1] == "up":
            up_card_river.del_last_card()
        elif RECEIVE_DATA[1] == "left":
            left_card_river.del_last_card()
        multi_chi(RECEIVE_DATA[2], card_list)

    if RECEIVE_DATA[0] == "can_pong":
        result = "can_pong"
        i = 1
        can_pong_site = RECEIVE_DATA[1]
        can_pong_id = RECEIVE_DATA[2]
        print("he")
        # 碰按鈕
        pong_button = Playing_Button(
            810, 530, "pong", pong_img, pong_kong_source_site=can_pong_site, pong_kong_card_id=can_pong_id)
        play_multi_sprites.add(pong_button)
        PLAYING_BUTTON_LIST.append(pong_button)
        # 取消按鈕
        cancel_button = Playing_Button(960, 530, "cancel", cancel_img)
        play_multi_sprites.add(cancel_button)
        PLAYING_BUTTON_LIST.append(cancel_button)

    if RECEIVE_DATA[0] == "other_pong":
        result = "other_pong"
        card_id = RECEIVE_DATA[3]
        if RECEIVE_DATA[1] == "down":
            player_card_river.del_last_card()
        elif RECEIVE_DATA[1] == "right":
            right_card_river.del_last_card()
        elif RECEIVE_DATA[1] == "up":
            up_card_river.del_last_card()
        elif RECEIVE_DATA[1] == "left":
            left_card_river.del_last_card()
        multi_pong(RECEIVE_DATA[1], RECEIVE_DATA[2], card_id)

    if RECEIVE_DATA[0] == "can_pong_and_kong":
        result = "can_pong_and_kong"
        can_pong_kong_site = RECEIVE_DATA[1]
        can_pong_kong_id = RECEIVE_DATA[2]
        # print("he")
        # 碰按鈕
        pong_button = Playing_Button(
            810, 530, "pong", pong_img, pong_kong_source_site=can_pong_kong_site, pong_kong_card_id=can_pong_kong_id)
        play_multi_sprites.add(pong_button)
        PLAYING_BUTTON_LIST.append(pong_button)
        # 槓按鈕
        kong_button = Playing_Button(
            860, 530, "kong", kong_img, pong_kong_source_site=can_pong_kong_site, pong_kong_card_id=can_pong_kong_id)
        play_multi_sprites.add(kong_button)
        PLAYING_BUTTON_LIST.append(kong_button)
        # 取消按鈕
        cancel_button = Playing_Button(960, 530, "cancel", cancel_img)
        play_multi_sprites.add(cancel_button)
        PLAYING_BUTTON_LIST.append(cancel_button)

    if RECEIVE_DATA[0] == "other_kong":
        result = "other_kong"
        card_id = RECEIVE_DATA[3]
        if RECEIVE_DATA[1] == "down":
            player_card_river.del_last_card()
        elif RECEIVE_DATA[1] == "right":
            right_card_river.del_last_card()
        elif RECEIVE_DATA[1] == "up":
            up_card_river.del_last_card()
        elif RECEIVE_DATA[1] == "left":
            left_card_river.del_last_card()
        multi_kong(RECEIVE_DATA[1], RECEIVE_DATA[2], card_id)

    if RECEIVE_DATA[0] == "flip_dora":
        result = "flip_dora"
        dora_mountain.flip_dora(RECEIVE_DATA[1])

    if RECEIVE_DATA[0] == "tsumo":
        WIN_SITE = "本家自摸"
        # result="leave"
        # 自摸按鈕
        tsumo_button = Playing_Button(
            760, 580, "tsumo", tsumo_img, ron_card_id=RECEIVE_DATA[1])
        play_multi_sprites.add(tsumo_button)
        PLAYING_BUTTON_LIST.append(tsumo_button)
        # 取消按鈕
        cancel_button = Playing_Button(960, 530, "cancel", cancel_img)
        play_multi_sprites.add(cancel_button)
        PLAYING_BUTTON_LIST.append(cancel_button)
        print(PLAYING_BUTTON_LIST)

    if RECEIVE_DATA[0] == "other_tsumo":
        result = "leave"
        tsumo_site = RECEIVE_DATA[1]
        if tsumo_site == "right":
            WIN_SITE = "下家自摸"
        if tsumo_site == "up":
            WIN_SITE = "對家自摸"
        if tsumo_site == "left":
            WIN_SITE = "上家自摸"
        RON_CARD_ID = RECEIVE_DATA[2]
        RON_HAND_CARD_ID_LIST = []
        RON_VICE_DEWS_ID_LIST = []
        i = 3
        while i < len(RECEIVE_DATA) and RECEIVE_DATA[i] != "CUT":
            RON_HAND_CARD_ID_LIST.append(RECEIVE_DATA[i])
            i += 1
        i += 1
        while i < len(RECEIVE_DATA):
            RON_VICE_DEWS_ID_LIST.append(RECEIVE_DATA[i])
            i += 1

        IS_WIN = 1
        IS_PLAY_MULTI = 0
        IS_PLAY_MULTI_END = 1
        play_multi_end_init = True

    if RECEIVE_DATA[0] == "ron":
        # result="leave"
        WIN_SITE = "本家和"
        # 和按鈕
        ron_button = Playing_Button(
            910, 530, "ron", ron_img, ron_card_id=RECEIVE_DATA[1])
        play_multi_sprites.add(ron_button)
        PLAYING_BUTTON_LIST.append(ron_button)
        # 取消按鈕
        cancel_button = Playing_Button(960, 530, "cancel", cancel_img)
        play_multi_sprites.add(cancel_button)
        PLAYING_BUTTON_LIST.append(cancel_button)
        print(PLAYING_BUTTON_LIST)

    if RECEIVE_DATA[0] == "other_ron":
        result = "leave"
        ron_site = RECEIVE_DATA[1]
        if ron_site == "right":
            WIN_SITE = "下家和"
        if ron_site == "up":
            WIN_SITE = "對家和"
        if ron_site == "left":
            WIN_SITE = "上家和"
        RON_CARD_ID = RECEIVE_DATA[2]
        RON_HAND_CARD_ID_LIST = []
        RON_VICE_DEWS_ID_LIST = []
        i = 3
        while i < len(RECEIVE_DATA) and RECEIVE_DATA[i] != "CUT":
            RON_HAND_CARD_ID_LIST.append(RECEIVE_DATA[i])
            i += 1
        i += 1
        while i < len(RECEIVE_DATA):
            RON_VICE_DEWS_ID_LIST.append(RECEIVE_DATA[i])
            i += 1

        IS_WIN = 1
        IS_PLAY_MULTI = 0
        IS_PLAY_MULTI_END = 1
        play_multi_end_init = True

    if RECEIVE_DATA[0] == "left_card_num":
        result = "left_card_num"
        IS_SHOW_LEFT_CARD_NUM = 1
        LEFT_CARD_NUM = RECEIVE_DATA[1]

    if RECEIVE_DATA[0] == "leave":
        result = "leave"
        i = 0
        while i < len(BUTTON_LIST):
            BUTTON_LIST[i].button_box.move_ip(-1000, -1000)
            BUTTON_LIST[i].kill()
            del BUTTON_LIST[i]

        while i < len(MAHJONG_BUTTON_LIST):
            MAHJONG_BUTTON_LIST[i].mahjong_box.move_ip(-1000, -1000)
            MAHJONG_BUTTON_LIST[i].kill()
            del MAHJONG_BUTTON_LIST[i]

        while i < len(PLAYING_BUTTON_LIST):
            PLAYING_BUTTON_LIST[i].button_box.move_ip(-1000, -1000)
            PLAYING_BUTTON_LIST[i].kill()
            del PLAYING_BUTTON_LIST[i]

        while i < len(VICE_DEWS_BUTTON_LIST):
            VICE_DEWS_BUTTON_LIST[i].vice_dews_box.move_ip(-1000, -1000)
            VICE_DEWS_BUTTON_LIST[i].kill()
            del VICE_DEWS_BUTTON_LIST[i]

        while i < len(HAND_CARDS_LIST):
            HAND_CARDS_LIST[i][1].mahjong_box.move_ip(-1000, -1000)
            HAND_CARDS_LIST[i][1].kill()
            del HAND_CARDS_LIST[i]

        IS_PLAY_MULTI = 0
        IS_MENU = 1
        menu_init = True

    DATA_PROCESS_END = True
    RESULT = result
    # return RESULT


def send_to_server(data_list):
    main_recv_cSocket.send(str(len(data_list)).encode('utf-8'))
    i = 0
    time.sleep(0.01)
    while i < len(data_list):
        main_recv_cSocket.send(str(data_list[i]).encode('utf-8'))
        time.sleep(0.01)
        i += 1


NOT_RECEIVE = True
RECEIVE_DATA = []
RECV_END = False


def main_multi_recv(client):
    global NOT_RECEIVE
    global RECEIVE_DATA
    global RECV_END
    global DATA_PROCESS_END
    while True:
        try:
            data = client.recv(BUFF_SIZE)
        except:
            break
       # print(data)
        while not DATA_PROCESS_END:
            pass
        RECEIVE_DATA = []
        if data.decode('utf-8').isdigit():
            data_num = int(data.decode('utf-8'))
            print(data_num)
            i = 0
            while i < data_num:
                data = client.recv(BUFF_SIZE)
                RECEIVE_DATA.append(data.decode('utf-8'))
                i += 1
        else:
            print("ERROR#############################################")

        print(RECEIVE_DATA)

        # while time_event.is_set():
        #	pass
        time_event.set()
        print("set")
       # print("is_set")

# condition_event=threading.Condition()


def countdown_recv(client):
    global IS_SHOW_COUNTDOWN
    global COUNTDOWN_TIME
    global IS_COUNTDOWN_FINISH
    global player
    global PLAYING_BUTTON_LIST
    global IS_CHI
    global IS_PONG
    global IS_KONG

    while IS_WAIT == 1 or IS_PLAY_MULTI == 1:
        try:
            t = client.recv(BUFF_SIZE).decode('utf-8')
        except:
            break
        print(t)
        if str(t).isdigit():
            COUNTDOWN_TIME = int(t)
            print("count: ", COUNTDOWN_TIME)
            if COUNTDOWN_TIME == 0:
                IS_COUNTDOWN_FINISH = 1
                IS_SHOW_COUNTDOWN = 0
                player.is_my_turn = False
                print("IS_CHI: ", IS_CHI, "RECEIVE_DATA[0]: ", RECEIVE_DATA[0])
                if (RECEIVE_DATA[0] == "can_chi" and IS_CHI == 0) or (RECEIVE_DATA[0] == "can_pong" and IS_PONG == 0) or (RECEIVE_DATA[0] == "can_pong_and_kong" and IS_PONG == 0 and IS_KONG == 0) or (RECEIVE_DATA[0] == "tsumo" and IS_WIN == 0) or (RECEIVE_DATA[0] == "ron" and IS_WIN == 0):
                    i = 0
                    while i < len(PLAYING_BUTTON_LIST):
                        PLAYING_BUTTON_LIST[i].button_box.move_ip(-1000, -1000)
                        PLAYING_BUTTON_LIST[i].kill()
                        i += 1
                    PLAYING_BUTTON_LIST = []
                    send_to_server(["cancel"])
                elif IS_CHI == 1:
                    IS_CHI = 0
                    multi_auto_out_card()
                elif IS_PONG == 1:
                    IS_PONG = 0
                    multi_auto_out_card()
                elif IS_KONG == 1:
                    IS_KONG = 0
                    multi_auto_out_card()
                else:
                    multi_auto_out_card()
                print("???")

            else:
                IS_COUNTDOWN_FINISH = 0
                IS_SHOW_COUNTDOWN = 1


def countdown_send():
    global IS_SHOW_COUNTDOWN
    sub_recv_cSocket.send(str(USERNAME).encode("utf-8"))
    IS_SHOW_COUNTDOWN = 0


def play_cards():
    global IS_PLAY_SINGLE
    global player
    global PLAYER_CAN_CHI
    global PLAYER_CAN_PONG
    global PLAYER_CAN_KONG
    global RIGHT_CAN_CHI
    global RIGHT_CAN_PONG
    global RIGHT_CAN_KONG
    global UP_CAN_CHI
    global UP_CAN_PONG
    global UP_CAN_KONG
    global LEFT_CAN_CHI
    global LEFT_CAN_PONG
    global LEFT_CAN_KONG
    global IS_COUNTDOWN_FINISH
    global play_single_sprites
    global dora_mountain
    global SEED
    global NO_DEAL
    global IS_CHI
    global IS_PONG
    global IS_KONG
    global IS_WIN
    global IS_PONGING_OR_KONGING
    global IS_CHIING
    global VICE_DEWS_SITE_CHI
    global VICE_DEWS_SITE_PONG_KONG
    global IS_PLAY_SINGLE_END
    global play_single_end_init
    global WIN_TEXT
    global IS_MENU
    global menu_init
    global PLAYING_BUTTON_LIST
    global play_single_init
    global IS_RON
    global IS_TSUMO
    global DOWN_RON
    global RIGHT_RON
    global UP_RON
    global LEFT_RON
    global DOWN_TSUMO
    global RIGHT_TSUMO
    global UP_TSUMO
    global LEFT_TSUMO
    do_not_add = 0
    target_river = ""
    chi_pong_kong_threads = []
    if MANAGER_MODE == 1:
        manager_define_process(1)
    # 洗牌
    shuffle()
    # 抓王牌七墩
    dora_mountain = Dora_Mountain(10, 10)
    play_single_sprites.add(dora_mountain)
    dora_mountain.dora_init()
    if MANAGER_MODE == 0:
        # 決定順序(1為自己,2為下家(右邊),3為對家(上面),4為上家(左邊))
        SEED = random.randint(1, 4)
        # 發牌
        SEED = start_deal(SEED)
    # 排牌
    sort('down')
    sort('right')
    sort('up')
    sort('left')
    while len(CARD_MOUNTAIN) > 0:
        VICE_DEWS_SITE_CHI = ""
        VICE_DEWS_SITE_PONG_KONG = ""
        chi_pong_kong_threads = []
        other_target_cards = []  # 其他家可以吃的組合
        target_river = ""
        do_not_add = 0
        NO_DEAL = 0
        """print(f"seed:{SEED}")
        i = 0
        while i < len(HAND_CARDS_LIST):
           #print(f"{HAND_CARDS_LIST[i][1].id} ", end="")
            i += 1
       #print()"""
        if SEED == 1:
            print("is_my_turn=True")
            player.is_my_turn = True
            if IS_CHI == 1:
                algorithm("down", "")
                IS_CHI = 0
                NO_DEAL = 1

            elif IS_PONG == 1:
                algorithm("down", "")
                IS_PONG = 0
                NO_DEAL = 1

            elif IS_KONG == 1:
                dora_mountain.deal("down")
                algorithm("down", DEAL_CARD[1].id)
                IS_KONG = 0
                NO_DEAL = 0

            else:
                time.sleep(0.5)
                deal("down", "draw")
                is_win = can_win("down", DEAL_CARD[1].id)
                if is_win:
                    print("贏了啦幹")
                    # 自摸按鈕
                    tsumo_button = Playing_Button(
                        760, 580, "tsumo", tsumo_img, ron_card_id=DEAL_CARD[1].id)
                    play_single_sprites.add(tsumo_button)
                    PLAYING_BUTTON_LIST.append(tsumo_button)
                    # 取消按鈕
                    cancel_button = Playing_Button(
                        960, 530, "cancel", cancel_img)
                    play_single_sprites.add(cancel_button)
                    PLAYING_BUTTON_LIST.append(cancel_button)
                    print(PLAYING_BUTTON_LIST)
                    # i=0
                    # while i<len(HAND_CARDS_LIST):
                    #    HAND_CARDS_LIST[i][1]
                    #    i+=1

                algorithm("down", DEAL_CARD[1].id)
            # print(player.is_my_turn)
            countdown(20, 1)
            if IS_TSUMO == 1:
                IS_TSUMO = 0
                break
            if IS_COUNTDOWN_FINISH == 1:  # 如果倒計時結束沒動作就自動出牌
                player_auto_out_card(NO_DEAL == 1)
            # 組牌
            if NO_DEAL == 0:
                combine_card("down")
            # 排牌
            sort('down')
            # 判斷其他家是否可以吃牌碰牌或槓牌
            can_or_can_not_pong_kong = others_can_pong_or_kong(
                "down", player_card_river.get_last_card_id())
            if can_or_can_not_pong_kong:
                target_river = "down"
            [can_or_can_not_chi, other_target_cards] = other_can_chi(
                "down", player_card_river.get_last_card_id())

            if can_or_can_not_pong_kong or can_or_can_not_chi:
                do_not_add = 1

        elif SEED == 2:
            deal("right", "draw")
            is_win = can_win("right", SMALL_DEAL_CARD[1].id)
            if is_win:
                RIGHT_TSUMO=1
                time.sleep(5)
                print("贏了啦幹")
                tsumo("right", SMALL_DEAL_CARD[1].id)
                break
            time.sleep(1)
            # 出牌
            out_cards("right", True)
            # 組牌
            combine_card("right")
            # 排牌
            sort('right')
            # 判斷其他家是否可以吃牌碰牌或槓牌
            can_or_can_not_pong_kong = others_can_pong_or_kong(
                "right", right_card_river.get_last_card_id())
            if can_or_can_not_pong_kong:
                target_river = "right"
            [can_or_can_not_chi, other_target_cards] = other_can_chi(
                "right", right_card_river.get_last_card_id())

        elif SEED == 3:
            deal("up", "draw")
            is_win = can_win("up", SMALL_DEAL_CARD[1].id)
            if is_win:
                UP_TSUMO=1
                time.sleep(5)
                print("贏了啦幹")
                tsumo("up", SMALL_DEAL_CARD[1].id)
                break
            time.sleep(1)
            # 出牌
            out_cards("up", True)
            # 組牌
            combine_card("up")
            # 排牌
            sort('up')
            # 判斷其他家是否可以吃牌碰牌或槓牌
            can_or_can_not_pong_kong = others_can_pong_or_kong(
                "up", up_card_river.get_last_card_id())
            if can_or_can_not_pong_kong:
                target_river = "up"

            [can_or_can_not_chi, other_target_cards] = other_can_chi(
                "up", up_card_river.get_last_card_id())

        elif SEED == 4:
            deal("left", "draw")
            is_win = can_win("left", SMALL_DEAL_CARD[1].id)
            if is_win:
                LEFT_TSUMO=1
                time.sleep(5)
                print("贏了啦幹")
                tsumo("left", SMALL_DEAL_CARD[1].id)
                break
            time.sleep(1)
            # 出牌
            out_cards("left", True)
            # 組牌
            combine_card("left")
            # 排牌
            sort('left')
            # 判斷其他家是否可以吃牌碰牌或槓牌
            can_or_can_not_pong_kong = others_can_pong_or_kong(
                "left", left_card_river.get_last_card_id())
            if can_or_can_not_pong_kong:
                target_river = "left"

            [can_or_can_not_chi, other_target_cards] = other_can_chi(
                "left", left_card_river.get_last_card_id())

        if SEED == 1:
            is_win = can_win("right", player_card_river.get_last_card_id())
            if is_win:
                RIGHT_RON=1
                time.sleep(5)
                ron("right", player_card_river.get_last_card_id())
                break
            is_win = can_win("up", player_card_river.get_last_card_id())
            if is_win:
                UP_RON=1
                time.sleep(5)
                ron("up", player_card_river.get_last_card_id())
                break
            is_win = can_win("left", player_card_river.get_last_card_id())
            if is_win:
                LEFT_RON=1
                time.sleep(5)
                ron("left", player_card_river.get_last_card_id())
                break
        if SEED == 2:
            is_win = can_win("up", right_card_river.get_last_card_id())
            if is_win:
                UP_RON=1
                time.sleep(5)
                ron("up", right_card_river.get_last_card_id())
                break
            is_win = can_win("left", right_card_river.get_last_card_id())
            if is_win:
                LEFT_RON=1
                time.sleep(5)
                ron("left", right_card_river.get_last_card_id())
                break
            is_win = can_win("down", right_card_river.get_last_card_id())
            if is_win:
                print("贏了啦幹")
                # 和按鈕
                ron_button = Playing_Button(
                    910, 530, "ron", ron_img, ron_card_id=right_card_river.get_last_card_id())
                play_single_sprites.add(ron_button)
                PLAYING_BUTTON_LIST.append(ron_button)
                # 取消按鈕
                cancel_button = Playing_Button(
                    960, 530, "cancel", cancel_img)
                play_single_sprites.add(cancel_button)
                PLAYING_BUTTON_LIST.append(cancel_button)
                countdown(20, 1)
                if IS_RON == 1:
                    IS_RON = 0
                    break
        if SEED == 3:
            is_win = can_win("left", up_card_river.get_last_card_id())
            if is_win:
                LEFT_RON=1
                time.sleep(5)
                ron("left", up_card_river.get_last_card_id())
                break
            is_win = can_win("down",  up_card_river.get_last_card_id())
            if is_win:
                print("贏了啦幹")
                # 和按鈕
                ron_button = Playing_Button(
                    910, 530, "ron", ron_img, ron_card_id=right_card_river.get_last_card_id())
                play_single_sprites.add(ron_button)
                PLAYING_BUTTON_LIST.append(ron_button)
                # 取消按鈕
                cancel_button = Playing_Button(
                    960, 530, "cancel", cancel_img)
                play_single_sprites.add(cancel_button)
                PLAYING_BUTTON_LIST.append(cancel_button)
                countdown(20, 1)
                if IS_RON == 1:
                    IS_RON = 0
                    break
            is_win = can_win("right",  up_card_river.get_last_card_id())
            if is_win:
                RIGHT_RON=1
                time.sleep(5)
                ron("right", up_card_river.get_last_card_id())
                break
        if SEED == 4:
            is_win = can_win("down", left_card_river.get_last_card_id())
            if is_win:
                print("贏了啦幹")
                # 和按鈕
                ron_button = Playing_Button(
                    910, 530, "ron", ron_img, ron_card_id=right_card_river.get_last_card_id())
                play_single_sprites.add(ron_button)
                PLAYING_BUTTON_LIST.append(ron_button)
                # 取消按鈕
                cancel_button = Playing_Button(
                    960, 530, "cancel", cancel_img)
                play_single_sprites.add(cancel_button)
                PLAYING_BUTTON_LIST.append(cancel_button)
                countdown(20, 1)
                if IS_RON == 1:
                    IS_RON = 0
                    break
            is_win = can_win("right", left_card_river.get_last_card_id())
            if is_win:
                RIGHT_RON=1
                time.sleep(5)
                ron("right", left_card_river.get_last_card_id())
                break
            is_win = can_win("up", left_card_river.get_last_card_id())
            if is_win:
                UP_RON=1
                time.sleep(5)
                ron("up", left_card_river.get_last_card_id())
                break

        if can_or_can_not_pong_kong or can_or_can_not_chi:
            do_not_add = 1

        if do_not_add == 0:
            SEED += 1

        if PLAYER_CAN_CHI == 1:
            PLAYER_CAN_CHI = 0
            tchi = threading.Thread(target=t_chi, args=(
                "down", other_target_cards))
            chi_pong_kong_threads.append(tchi)
            IS_CHIING = 1
            VICE_DEWS_SITE_CHI = "down"

        if PLAYER_CAN_PONG == 1 and PLAYER_CAN_KONG == 0:
            PLAYER_CAN_PONG = 0
            tpong = threading.Thread(
                target=t_pong_kong, args=(target_river, "down", 2))
            chi_pong_kong_threads.append(tpong)
            IS_PONGING_OR_KONGING = 1
            VICE_DEWS_SITE_PONG_KONG = "down"

        elif PLAYER_CAN_KONG == 1:
            PLAYER_CAN_KONG = 0
            PLAYER_CAN_PONG = 0
            tkong = threading.Thread(
                target=t_pong_kong, args=(target_river, "down", 3))
            chi_pong_kong_threads.append(tkong)
            IS_PONGING_OR_KONGING = 1
            VICE_DEWS_SITE_PONG_KONG = "down"

        if RIGHT_CAN_CHI == 1:
            RIGHT_CAN_CHI = 0
            tchi = threading.Thread(target=t_chi, args=(
                "right", other_target_cards))
            chi_pong_kong_threads.append(tchi)
           # print("RIGHT_CAN_CHI")
            IS_CHIING = 1
            VICE_DEWS_SITE_CHI = "right"

        if RIGHT_CAN_PONG == 1 and RIGHT_CAN_KONG == 0:
            RIGHT_CAN_PONG = 0
            tpong = threading.Thread(
                target=t_pong_kong, args=(target_river, "right", 2))
            chi_pong_kong_threads.append(tpong)
            IS_PONGING_OR_KONGING = 1
            VICE_DEWS_SITE_PONG_KONG = "right"
           # print("RIGHT_CAN_PONG")

        elif RIGHT_CAN_KONG == 1:
            RIGHT_CAN_KONG = 0
            RIGHT_CAN_PONG = 0
            tkong = threading.Thread(
                target=t_pong_kong, args=(target_river, "right", 3))
            chi_pong_kong_threads.append(tkong)
            IS_PONGING_OR_KONGING = 1
            VICE_DEWS_SITE_PONG_KONG = "right"
           # print("RIGHT_CAN_PONG_KONG")

        if UP_CAN_CHI == 1:
            UP_CAN_CHI = 0
            tchi = threading.Thread(
                target=t_chi, args=("up", other_target_cards))
            chi_pong_kong_threads.append(tchi)
            IS_CHIING = 1
            VICE_DEWS_SITE_CHI = "up"
           # print("UP_CAN_CHI")

        if UP_CAN_PONG == 1 and UP_CAN_KONG == 0:
            UP_CAN_PONG = 0
            tpong = threading.Thread(
                target=t_pong_kong, args=(target_river, "up", 2))
            chi_pong_kong_threads.append(tpong)
            IS_PONGING_OR_KONGING = 1
            VICE_DEWS_SITE_PONG_KONG = "up"
           # print("UP_CAN_PONG")

        elif UP_CAN_KONG == 1:
            UP_CAN_KONG = 0
            UP_CAN_PONG = 0
            tkong = threading.Thread(
                target=t_pong_kong, args=(target_river, "up", 3))
            chi_pong_kong_threads.append(tkong)
            IS_PONGING_OR_KONGING = 1
            VICE_DEWS_SITE_PONG_KONG = "up"
           # print("UP_CAN_PONG_KONG")

        if LEFT_CAN_CHI == 1:
            LEFT_CAN_CHI = 0
            tchi = threading.Thread(target=t_chi, args=(
                "left", other_target_cards))
            chi_pong_kong_threads.append(tchi)
            IS_CHIING = 1
            VICE_DEWS_SITE_CHI = "left"
           # print("LEFT_CAN_CHI")

        if LEFT_CAN_PONG == 1 and LEFT_CAN_KONG == 0:
            LEFT_CAN_PONG = 0
            tpong = threading.Thread(
                target=t_pong_kong, args=(target_river, "left", 2))
            chi_pong_kong_threads.append(tpong)
            IS_PONGING_OR_KONGING = 1
            VICE_DEWS_SITE_PONG_KONG = "left"
           # print("LEFT_CAN_PONG")

        elif LEFT_CAN_KONG == 1:
            LEFT_CAN_KONG = 0
            LEFT_CAN_PONG = 0
            tkong = threading.Thread(
                target=t_pong_kong, args=(target_river, "left", 3))
            chi_pong_kong_threads.append(tkong)
            IS_PONGING_OR_KONGING = 1
            VICE_DEWS_SITE_PONG_KONG = "left"
           # print("LEFT_CAN_PONG_KONG")

        i = 0
        while i < len(chi_pong_kong_threads):
            chi_pong_kong_threads[i].start()
            i += 1

        i = 0
        while i < len(chi_pong_kong_threads):
            chi_pong_kong_threads[i].join()
            i += 1
        if SEED > 4:
            SEED = 1

    print("play end")

    # print(f"oriSEED:{SEED}")

    if len(CARD_MOUNTAIN) <= 0:
        IS_PLAY_SINGLE = 0
        play_single_init = True
        IS_PLAY_SINGLE_END = 1
        play_single_end_init = True
        menu_init = True
        WIN_TEXT = "流局"


# 吃碰槓的流程的額外多執行緒
#chi_button = Playing_Button(760,530,"chi",chi_img,target_cards_id_list)
#pong_button = Playing_Button(810,530,"pong",pong_img, pong_kong_source_site = source_site)
#kong_button = Playing_Button(860,530,"kong",kong_img,pong_kong_source_site = source_site)
#ron_button = Playing_Button(910,530,"ron",True,ron_img)
#cancel_button = Playing_Button(960,530,"cancel",cancel_img)


def t_chi(site, target_cards_id_lists):
    global play_single_sprites
    global PLAYING_BUTTON_LIST
    global SEED
    global NO_DEAL
    global player_card_river
    global right_card_river
    global up_card_river
    global left_card_river
    global IS_CHIING
    if site == "down":
        # 吃按鈕
        chi_button = Playing_Button(
            760, 530, "chi", chi_img, target_cards_id_lists)
        play_single_sprites.add(chi_button)
        PLAYING_BUTTON_LIST.append(chi_button)
        # 取消按鈕
        cancel_button = Playing_Button(960, 530, "cancel", cancel_img)
        play_single_sprites.add(cancel_button)
        PLAYING_BUTTON_LIST.append(cancel_button)
        countdown(20, 1)
        if IS_COUNTDOWN_FINISH == 1:  # 沒有動作
            i = 0
            while i < len(PLAYING_BUTTON_LIST):
                PLAYING_BUTTON_LIST[i].button_box.move_ip(-1000, -1000)
                PLAYING_BUTTON_LIST[i].kill()
                i += 1
            PLAYING_BUTTON_LIST = []
            #SEED += 1
           #print("player no chi")
        elif IS_CHI == 1:  # 有吃
            NO_DEAL = 1
        else:  # 沒有吃
            pass
           #print("player no chi")
        SEED = 1

        #tcountdown = threading.Thread(target=countdown,args=(20,1))
        # tcountdown.start()

    if site == "right":
        random_thinking_time = 0
        print("clear & wait")
        time_event.clear()
        time_event.wait(random_thinking_time)
        # print("下家吃")
        # algorithm_action("right", target_cards_id_list, 1)
        yes_or_not = False
        # print(yes_or_not)
        # if VICE_DEWS_SITE_CHI == "right" and VICE_DEWS_SITE_PONG_KONG == "right":
        #    IS_PONGING_OR_KONGING = 0
        #    IS_PONGED_OR_KONGED = 0
        if yes_or_not:
            if IS_PONGING_OR_KONGING == 1:  # 如果別家正在思考要不要碰槓
                print("clear & wait")
                time_event.clear()
                time_event.wait()
            if IS_PONGED_OR_KONGED == 0:  # 如果別家選擇不要碰槓
                chi("right", target_cards_id_lists)
                sort('right')
                random_thinking_time = 0
                print("clear & wait")
                time_event.clear()
                time_event.wait(random_thinking_time)
                out_cards("right", False)
                sort('right')
                SEED = 3
            else:
                SEED = 2
               #print("right can't chi")
        else:
            SEED = 2
           #print("right no chi")
    if site == "up":
        random_thinking_time = 0
        print("clear & wait")
        time_event.clear()
        time_event.wait(random_thinking_time)
        # print("對家吃")
        yes_or_not = False  # algorithm_action("up", target_cards_id_list, 1)
        # print(yes_or_not)
        if yes_or_not:
            if IS_PONGING_OR_KONGING == 1:  # 如果別家正在思考要不要碰槓
                print("clear & wait")
                time_event.clear()
                time_event.wait()
            if IS_PONGED_OR_KONGED == 0:  # 如果別家選擇不要碰槓
                chi("up", target_cards_id_lists)
                sort('up')
                random_thinking_time = 0
                print("clear & wait")
                time_event.clear()
                time_event.wait(random_thinking_time)
                out_cards("up", False)
                sort('up')
                SEED = 4
            else:
                SEED = 3
               #print("up can't chi")
        else:
            SEED = 3
           #print("up no chi")
    if site == "left":
        random_thinking_time = 0
        print("clear & wait")
        time_event.clear()
        time_event.wait(random_thinking_time)
        # print("上家吃")
        yes_or_not = False  # algorithm_action("left", target_cards_id_list, 1)
        # print(yes_or_not)
        if yes_or_not:
            if IS_PONGING_OR_KONGING == 1:  # 如果別家正在思考要不要碰槓
                print("clear & wait")
                time_event.clear()
                time_event.wait()
            if IS_PONGED_OR_KONGED == 0:  # 如果別家選擇不要碰槓
                chi("left", target_cards_id_lists)
                sort('left')
                random_thinking_time = 0
                print("clear & wait")
                time_event.clear()
                time_event.wait(random_thinking_time)
                out_cards("left", False)
                sort('left')
                SEED = 1
            else:
                SEED = 4
               #print("left can't chi")
        else:
            SEED = 4
           #print("left no chi")
    IS_CHIING = 0


def source_site_to_next_SEED(source_site):
    if source_site == "down":
        return 2
    elif source_site == "right":
        return 3
    elif source_site == "up":
        return 4
    elif source_site == "left":
        return 1


IS_PONGING_OR_KONGING = 0  # 給t_chi判斷是否有其他人可以碰槓
IS_PONGED_OR_KONGED = 0  # 讓t_chi知道其他人最後是否有碰槓
IS_CHIING = 0  # 讓t_pong_kong判斷SEED要不要直接加(沒有其他家能吃就可以直接加)
#IS_CHIED = 0#


def t_pong_kong(source_site, destination_site, hand_card_take_out_number):  # 槓為手裡有三張 槓他家的牌
    global play_single_sprites
    global PLAYING_BUTTON_LIST
    global SEED
    global NO_DEAL
    global player_card_river
    global right_card_river
    global up_card_river
    global left_card_river
    global IS_PONGING_OR_KONGING
    global IS_PONGED_OR_KONGED
    global time_event
    # IS_PONGING_OR_KONGING = 1 已經直接寫在play_card()裡了
    if destination_site == "down":
        # 碰按鈕
        pong_button = Playing_Button(
            810, 530, "pong", pong_img, pong_kong_source_site=source_site)
        play_single_sprites.add(pong_button)
        PLAYING_BUTTON_LIST.append(pong_button)
        # 槓按鈕
        if hand_card_take_out_number == 3:
            kong_button = Playing_Button(
                860, 530, "kong", kong_img, pong_kong_source_site=source_site)
            play_single_sprites.add(kong_button)
            PLAYING_BUTTON_LIST.append(kong_button)
        # 取消按鈕
        cancel_button = Playing_Button(960, 530, "cancel", cancel_img)
        play_single_sprites.add(cancel_button)
        PLAYING_BUTTON_LIST.append(cancel_button)
        countdown(20, 1)
        if IS_COUNTDOWN_FINISH == 1:  # 沒有動作
            i = 0
            while i < len(PLAYING_BUTTON_LIST):
                PLAYING_BUTTON_LIST[i].button_box.move_ip(-1000, -1000)
                PLAYING_BUTTON_LIST[i].kill()
                i += 1
            PLAYING_BUTTON_LIST = []
            # pass
            if IS_CHIING == 0:  # 沒有其他家能吃
               #print(f"SEED {SEED} => {SEED + 1}")
                SEED = source_site_to_next_SEED(source_site)
           #print("player no pong and kong")
            IS_PONGED_OR_KONGED = 0
        elif IS_PONG == 1 or IS_KONG == 1:  # 有碰槓
            NO_DEAL = 1
           #print(f"SEED {SEED} => 1")
            SEED = 1
            IS_PONGED_OR_KONGED = 1
        else:  # 取消碰槓
           #print("player no pong and kong")
            if IS_CHIING == 0:  # 沒有其他家能吃
               #print(f"SEED {SEED} => {SEED + 1}")
                SEED = source_site_to_next_SEED(source_site)
            IS_PONGED_OR_KONGED = 0

    elif destination_site == "right" or destination_site == "up" or destination_site == "left":
        random_thinking_time = 0
        print("clear & wait")
        time_event.clear()
        time_event.wait(random_thinking_time)
        if hand_card_take_out_number == 2:
            if source_site == "down":
                target_cards_id = player_card_river.get_last_card_id()
            elif source_site == "right":
                target_cards_id = right_card_river.get_last_card_id()
            elif source_site == "up":
                target_cards_id = up_card_river.get_last_card_id()
            elif source_site == "left":
                target_cards_id = left_card_river.get_last_card_id()
            # algorithm_action(destination_site, target_cards_id, 2)
            yes_or_not = False
            if yes_or_not:  # pong
                pong(source_site, destination_site)
                sort(destination_site)
                random_thinking_time = 0
                print("clear & wait")
                time_event.clear()
                time_event.wait(random_thinking_time)
                out_cards(destination_site, False)
                sort(destination_site)
                if destination_site == "right":
                   #print(f"SEED {SEED} => 3")
                    SEED = 3
                elif destination_site == "up":
                   #print(f"SEED {SEED} => 4")
                    SEED = 4
                elif destination_site == "left":
                   #print(f"SEED {SEED} => 1")
                    SEED = 1
                IS_PONGED_OR_KONGED = 1
            else:
                # pass
                if IS_CHIING == 0:  # 沒有其他家能吃
                   #print(f"SEED {SEED} => {SEED + 1}")
                    SEED = source_site_to_next_SEED(source_site)
               #print(f"{destination_site} no pong")
                IS_PONGED_OR_KONGED = 0
        else:
            pong_kong_no = random.randint(0, 2)
            if pong_kong_no == 1:  # pong
                pong(source_site, destination_site)
                sort(destination_site)
                random_thinking_time = 0
                print("clear & wait")
                time_event.clear()
                time_event.wait(random_thinking_time)
                out_cards(destination_site, False)
                sort(destination_site)
                if destination_site == "right":
                   #print(f"SEED {SEED} => 3")
                    SEED = 3
                elif destination_site == "up":
                   #print(f"SEED {SEED} => 4")
                    SEED = 4
                elif destination_site == "left":
                   #print(f"SEED {SEED} => 1")
                    SEED = 1
                IS_PONGED_OR_KONGED = 1
            else:
                # pass
                if IS_CHIING == 0:  # 沒有其他家能吃
                   #print(f"SEED {SEED} => {SEED + 1}")
                    SEED = source_site_to_next_SEED(source_site)
               #print(f"{destination_site} no pong")
                IS_PONGED_OR_KONGED = 0
            if pong_kong_no == 2:  # kong
                kong(source_site, destination_site)
                sort(destination_site)
                dora_mountain.deal(destination_site)  # 從寶牌山抽一張牌
                random_thinking_time = 0
                print("clear & wait")
                time_event.clear()
                time_event.wait(random_thinking_time)
                out_cards(destination_site, False)
                combine_card(destination_site)
                sort(destination_site)
                if destination_site == "right":
                   #print(f"SEED {SEED} => 3")
                    SEED = 3
                elif destination_site == "up":
                   #print(f"SEED {SEED} => 4")
                    SEED = 4
                elif destination_site == "left":
                   #print(f"SEED {SEED} => 1")
                    SEED = 1
                IS_PONGED_OR_KONGED = 1
            else:
                # pass
                if IS_CHIING == 0:  # 沒有其他家能吃
                   #print(f"SEED {SEED} => {SEED + 1}")
                    SEED = source_site_to_next_SEED(source_site)
               #print(f"{destination_site} no kong")
                IS_PONGED_OR_KONGED = 0
            if pong_kong_no == 0:
               #print(f"{destination_site} no pong and kong")
                if IS_CHIING == 0:  # 沒有其他家能吃
                   #print(f"SEED {SEED} => {SEED + 1}")
                    SEED = source_site_to_next_SEED(source_site)
                IS_PONGED_OR_KONGED = 0
    IS_PONGING_OR_KONGING = 0
    print("set")
    time_event.set()


# wait
time_event = threading.Event()
#time_condition = threading.Condition()

running = True

while running:

    clock.tick(FPS)
    for event in pygame.event.get():  # pygame.event.get()回傳現在發生的所有事件,ex:滑鼠滑到哪或鍵盤按了甚麼按鍵,回傳列表
        if event.type == pygame.QUIT:  # 偵測事件類型是否把遊戲關閉
            if IS_MULTI_ING == 1:
                try:
                    main_recv_cSocket.send("1".encode('utf-8'))
                    main_recv_cSocket.send("leave".encode('utf-8'))
                except:
                    pass
            # logout()
            running = False
        # 事件偵測
        if IS_LOGIN == 1:  # 登入畫面
            if event.type == pygame.MOUSEBUTTONUP:
                LOGIN.active = True
                REGISTER.active = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                # 點擊輸入 ID
                if ID.button_box.collidepoint(event.pos):
                    USERID = ''
                    ID.active = True
                else:
                    ID.active = False
                # 點擊輸入password
                if PASSWORD.button_box.collidepoint(event.pos):
                    PASSWORD_TEXT = ''
                    PASSWORD_TEXT_HIDE = ''
                    PASSWORD.active = True
                else:
                    PASSWORD.active = False
                # 點擊登入
                if LOGIN.button_box.collidepoint(event.pos) and LOGIN.active:
                    LOGIN.active = False
                    if thread_flag == 0:
                        thread_init = threading.Thread(target=login_register)
                        thread_init.setDaemon(True)
                        thread_init.start()
                    #print("wake up login")
                    else:
                        with condition_event:
                            condition_event.notify()
                        # time_event.set()
                    login_register_flag = -1
                # 點擊註冊
                if REGISTER.button_box.collidepoint(event.pos) and REGISTER.active:
                    REGISTER.active = False
                    if thread_flag == 0:
                        thread_init = threading.Thread(target=login_register)
                        thread_init.setDaemon(True)
                        thread_init.start()
                    #print("wake up")
                    else:
                        with condition_event:
                            condition_event.notify()
                        # time_event.set()
                    login_register_flag = 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and ID.active == True:
                    USERNAME = USERNAME[:-1]
                elif len(USERNAME) < 15 and ID.active == True:
                    USERNAME += event.unicode
                if event.key == pygame.K_BACKSPACE and PASSWORD.active == True:
                    PASSWORD_TEXT = PASSWORD_TEXT[:-1]
                elif len(PASSWORD_TEXT) < 20 and PASSWORD.active == True:
                    PASSWORD_TEXT_HIDE += '*'
                    PASSWORD_TEXT += event.unicode

        if IS_MENU == 1:  # 主畫面

            if event.type == pygame.MOUSEBUTTONDOWN:  # 當按下滑鼠按鍵時
                i = 0
                while i < len(BUTTON_LIST):  # 按鈕事件偵測
                    # 當鼠標位置在按鈕內時
                    if BUTTON_LIST[i].button_box.collidepoint(event.pos):
                        BUTTON_LIST[i].click()

                    i += 1

        if IS_PLAY_SINGLE == 1:  # 單人模式畫面
            if event.type == pygame.MOUSEBUTTONDOWN:  # 當按下滑鼠按鍵時
                i = 0
                while i < len(BUTTON_LIST):  # 按鈕事件偵測
                    # 當鼠標位置在按鈕內時
                    if BUTTON_LIST[i].button_box.collidepoint(event.pos):
                        BUTTON_LIST[i].click()
                    i += 1
                i = 0
                while i < len(MAHJONG_BUTTON_LIST):  # 麻將按鈕事件偵測
                    # 當鼠標位置在按鈕內時
                    if MAHJONG_BUTTON_LIST[i].mahjong_box.collidepoint(event.pos) and player.is_my_turn:
                        (out_card_id,
                         in_hand_id) = MAHJONG_BUTTON_LIST[i].click()
                        MAHJONG_BUTTON_LIST[i].mahjong_box.move_ip(
                            -1000, -1000)
                        MAHJONG_BUTTON_LIST[i].kill()
                        del MAHJONG_BUTTON_LIST[i]
                        i -= 1
                        player.out_card(in_hand_id, out_card_id)
                       #print(f"player out:{out_card_id}")
                    i += 1

                i = 0
                while i < len(PLAYING_BUTTON_LIST):  # 吃碰槓和取消按鈕
                    # 當鼠標位置在按鈕內時
                    if PLAYING_BUTTON_LIST[i].button_box.collidepoint(event.pos):
                        PLAYING_BUTTON_LIST[i].button_box.move_ip(-1000, -1000)
                        PLAYING_BUTTON_LIST[i].click()
                        # PLAYING_BUTTON_LIST[i].kill()
                        #del PLAYING_BUTTON_LIST[i]
                        #i -= 1
                    i += 1

                i = 0
                while i < len(VICE_DEWS_BUTTON_LIST):  # 吃碰槓和取消按鈕
                    # 當鼠標位置在按鈕內時
                    if VICE_DEWS_BUTTON_LIST[i].vice_dews_box.collidepoint(event.pos):
                        VICE_DEWS_BUTTON_LIST[i].click()
                    i += 1

            if event.type == pygame.MOUSEMOTION:  # 當事件為MOUSEMOTION時
                i = 0
                while i < len(MAHJONG_BUTTON_LIST):
                    if MAHJONG_BUTTON_LIST[i].mahjong_box.collidepoint(event.pos):
                        MAHJONG_BUTTON_LIST[i].active = True
                    else:
                        MAHJONG_BUTTON_LIST[i].active = False
                    i += 1

        if IS_PLAY_MULTI == 1:  # 多人模式畫面
            if event.type == pygame.MOUSEBUTTONDOWN:  # 當按下滑鼠按鍵時
                i = 0
                while i < len(BUTTON_LIST):  # 按鈕事件偵測
                    # 當鼠標位置在按鈕內時
                    if BUTTON_LIST[i].button_box.collidepoint(event.pos):
                        BUTTON_LIST[i].click()
                    i += 1
                i = 0
                while i < len(MAHJONG_BUTTON_LIST):  # 麻將按鈕事件偵測
                    # 當鼠標位置在按鈕內時
                    if MAHJONG_BUTTON_LIST[i].mahjong_box.collidepoint(event.pos) and player.is_my_turn == True:
                        out_card_id, in_hand_id = MAHJONG_BUTTON_LIST[i].click(
                        )
                        MAHJONG_BUTTON_LIST[i].mahjong_box.move_ip(
                            -1000, -1000)
                        MAHJONG_BUTTON_LIST[i].kill()
                        del MAHJONG_BUTTON_LIST[i]
                        i -= 1
                        #try:
                        #    print("DEAL_CARD[0]==in_hand_id",DEAL_CARD[0],in_hand_id)
                        #except:
                        #    print("DEAL_CARD[0]==in_hand_id, except")
                        #if DEAL_CARD[0]==in_hand_id:
                        #    is_deal = "True"
                        #else:
                        #    is_deal = "False"

                        player.out_card(in_hand_id, out_card_id)
                        
                        print("send to server ",OUT_CARD_ID)
                        send_to_server(["out", OUT_CARD_ID])
                        countdown_send()
                       #print(f"player out:{out_card_id}")
                    i += 1

                i = 0
                while i < len(PLAYING_BUTTON_LIST):  # 吃碰槓和取消按鈕
                    # 當鼠標位置在按鈕內時
                    if PLAYING_BUTTON_LIST[i].button_box.collidepoint(event.pos):
                        PLAYING_BUTTON_LIST[i].button_box.move_ip(-1000, -1000)
                        PLAYING_BUTTON_LIST[i].click()
                        # PLAYING_BUTTON_LIST[i].kill()
                        #del PLAYING_BUTTON_LIST[i]
                        #i -= 1
                    i += 1

                i = 0
                while i < len(VICE_DEWS_BUTTON_LIST):  # 吃碰槓和取消按鈕
                    # 當鼠標位置在按鈕內時
                    if VICE_DEWS_BUTTON_LIST[i].vice_dews_box.collidepoint(event.pos):
                        VICE_DEWS_BUTTON_LIST[i].click()
                    i += 1

            if event.type == pygame.MOUSEMOTION:  # 當事件為MOUSEMOTION時
                i = 0
                while i < len(MAHJONG_BUTTON_LIST):
                    if MAHJONG_BUTTON_LIST[i].mahjong_box.collidepoint(event.pos):
                        MAHJONG_BUTTON_LIST[i].active = True
                    else:
                        MAHJONG_BUTTON_LIST[i].active = False
                    i += 1

        if IS_PLAY_MULTI_END == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:  # 當按下滑鼠按鍵時
                i = 0
                while i < len(BUTTON_LIST):  # 按鈕事件偵測
                    # 當鼠標位置在按鈕內時
                    if BUTTON_LIST[i].button_box.collidepoint(event.pos):
                        BUTTON_LIST[i].click()

                    i += 1

        if IS_PLAY_SINGLE_END == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:  # 當按下滑鼠按鍵時
                i = 0
                while i < len(BUTTON_LIST):  # 按鈕事件偵測
                    # 當鼠標位置在按鈕內時
                    if BUTTON_LIST[i].button_box.collidepoint(event.pos):
                        BUTTON_LIST[i].click()
                    i+=1

    # screen.blit(background_img,(0,0))#bilt()畫,(要畫的圖片,要畫的位置)#####底,要顯示的東西放在這後面

    if IS_LOGIN == 1:  # 登入畫面

        if login_init:  # 登入初始化
            login_init = False
            login_sprites = pygame.sprite.Group()
            INPUT_BOX_LIST = []
            BUTTON_LIST = []

            button = pygame.sprite.Group()
            ID = Image_button(440, 150, 400, 50)
            button.add(ID)
            PASSWORD = Image_button(440, 250, 400, 50)
            button.add(PASSWORD)
            LOGIN = Image_button(526, 400, 104, 44)
            button.add(LOGIN)
            REGISTER = Image_button(650, 400, 104, 44)
            button.add(REGISTER)

        # code
        # draw_texts(screen, ["Login"], 40, BLACK, 20, 20)

        login_sprites.update()
        init()
        # login_sprites.draw(screen)

    if IS_MENU == 1:  # 主畫面
        if menu_init:  # 主畫面初始化
            pygame.mixer.music.stop()
            pygame.mixer.music.play(-1)
            try:
                main_send_cSocket.close()
                main_recv_cSocket.close()
                sub_send_cSocket.close()
                sub_recv_cSocket.close()
            except:
                pass
            main_send_cSocket = ""
            main_recv_cSocket = ""
            sub_send_cSocket = ""
            sub_recv_cSocket = ""
            menu_init = False
            menu_sprites = pygame.sprite.Group()
            INPUT_BOX_LIST = []
            BUTTON_LIST = []

            single_mode_button = Button(
                850, 170, "single_mode", True, single_mode_img)
            menu_sprites.add(single_mode_button)
            BUTTON_LIST.append(single_mode_button)

            multi_mode_button = Button(
                850, 350, "multi_mode", True, multi_mode_img)
            menu_sprites.add(multi_mode_button)
            BUTTON_LIST.append(multi_mode_button)

        # code
        # draw_texts(screen, ["Menu"], 40, BLACK, 20, 20)
        screen.blit(background_img, (0, 0))
        screen.blit(shadow_img, (30, 90))
        draw_text_background(screen, f"welcom:{USERNAME}", 40, BLACK, 5, 10)
        menu_sprites.update()
        menu_sprites.draw(screen)

    if IS_PLAY_SINGLE == 1:  # 單人模式畫面

        if play_single_init:  # 單人模式初始化
            pygame.mixer.music.stop()
            pygame.mixer.music.play(-1)
            play_single_init = False
            play_single_sprites = pygame.sprite.Group()
            INPUT_BOX_LIST = []
            BUTTON_LIST = []
            MAHJONG_BUTTON_LIST = []
            VICE_DEWS_BUTTON_LIST = []
            THROUGHT_TYPE = 0
            THROUGHT_LAST_FOUR = 0
            THROUGHT_EYES = 0

            player = Player()
            play_single_sprites.add(player)

            player_card_river = Card_river(
                int((WIDTH/2)-((SMALL_MAHJONG_WIDTH*5+SMALL_MAHJONG_HEIGHT)/2)), 475, "down")
            play_single_sprites.add(player_card_river)

            right_card_river = Card_river(
                760, (HEIGHT/2)-(SMALL_MAHJONG_HEIGHT*3)+30, "right")
            play_single_sprites.add(right_card_river)

            up_card_river = Card_river(
                int((WIDTH/2)-((SMALL_MAHJONG_WIDTH*5+SMALL_MAHJONG_HEIGHT)/2)), 100, "up")
            play_single_sprites.add(up_card_river)

            left_card_river = Card_river(
                376, (HEIGHT/2)-(SMALL_MAHJONG_HEIGHT*3)+30, "left")
            play_single_sprites.add(left_card_river)

            # hand_card_startx = HAND_CARDS_STARTX  # 最右邊手牌x座標
            # hand_card_starty = HAND_CARDS_STARTY  # 最右邊手牌y座標
            RIGHT_TSUMO = 0
            LEFT_TSUMO = 0
            DOWN_TSUMO = 0
            UP_TSUMO = 0
            DOWN_RON = 0
            RIGHT_RON = 0
            UP_RON = 0
            LEFT_RON = 0
            # 手牌重置
            HAND_CARDS_LIST = []
            RIGHT_HAND_CARDS_LIST = []
            UP_HAND_CARDS_LIST = []
            LEFT_HAND_CARDS_LIST = []
            # 牌山重置
            CARD_MOUNTAIN = []
            # 流程執行緒
            thread = threading.Thread(target=play_cards)
            thread.setDaemon(True)
            thread.start()
        screen.fill(GREEN)  # 設定顏色(r,g,b)
        # code
        #draw_chinese_texts(screen, [f"剩餘: {len(CARD_MOUNTAIN)} 張"], 40,BLACK, WIDTH/2, HEIGHT/2)
        draw_texts(screen, [f"{len(CARD_MOUNTAIN)}"],
                   35, BLACK, WIDTH/2-10, HEIGHT/2-10)

        if IS_SHOW_COUNTDOWN == 1:  # 顯示倒計時
            draw_texts(screen, [f"{COUNTDOWN_TIME}"], 50, BLACK, 1020, 550)

        # draw_texts(screen, [f"SEED:{SEED}"], 50,
        #		   BLACK, WIDTH/2-50, HEIGHT/2+20)  # 顯示SEED
        # draw_texts(screen, [f"hc:{len(HAND_CARDS_LIST)}"],
        #		   30, BLACK, WIDTH - 100, HEIGHT - 100)  # 顯示手牌數量

        play_single_sprites.update()
        play_single_sprites.draw(screen)

        if DOWN_TSUMO == 1:
            screen.blit(tsumo_effect_img, (580, 460))
        if RIGHT_TSUMO == 1:
            screen.blit(tsumo_effect_img, (935, 315))
        if UP_TSUMO == 1:
            screen.blit(tsumo_effect_img, (580, 175))
        if LEFT_TSUMO == 1:
            screen.blit(tsumo_effect_img, (230, 315))

        if DOWN_RON == 1:
            screen.blit(ron_effect_img, (580, 460))
        if RIGHT_RON == 1:
            screen.blit(ron_effect_img, (935, 315))
        if UP_RON == 1:
            screen.blit(ron_effect_img, (580, 175))
        if LEFT_RON == 1:
            screen.blit(ron_effect_img, (230, 315))

    if IS_WAIT == 1:
        if wait_init:
            wait_init = False
            play_multi_sprites = pygame.sprite.Group()
            BUTTON_LIST = []
            MAHJONG_BUTTON_LIST = []
            VICE_DEWS_BUTTON_LIST = []
            IS_MULTI_ING = 0
            LEFT_CARD_NUM = 0
            IS_SHOW_LEFT_CARD_NUM = 0
            WAIT_PEOPLE_NUM = 0
            multi_play_t = threading.Thread(target=multi_play)
            multi_play_t.setDaemon(True)
            multi_play_t.start()
        screen.blit(background_img, (0, 0))
        screen.blit(wait_people_img_list[0], (541, 280))
        if WAIT_PEOPLE_NUM != 0:
            screen.blit(wait_people_img_list[WAIT_PEOPLE_NUM], (541, 360))

    if IS_PLAY_MULTI == 1:  # 多人模式畫面
        if play_multi_init:  # 多人模式初始化
            pygame.mixer.music.stop()
            play_multi_init = False
            COUNTDOWN_TIME = 0
            #BUTTON_LIST = []
            #MAHJONG_BUTTON_LIST = []
            #VICE_DEWS_BUTTON_LIST = []
            #IS_MULTI_ING = 0
            #LEFT_CARD_NUM = 0
            #IS_SHOW_LEFT_CARD_NUM = 0
            #
            #multi_play_t = threading.Thread(target=multi_play)
            # multi_play_t.setDaemon(True)
            # multi_play_t.start()
        screen.fill(GREEN)  # 設定顏色(r,g,b)
        if IS_SHOW_COUNTDOWN == 1:  # 顯示倒計時
            draw_texts(screen, [f"{COUNTDOWN_TIME}"], 50, BLACK, 1020, 550)

        if IS_SHOW_LEFT_CARD_NUM == 1:
            draw_texts(screen, [f"{LEFT_CARD_NUM}"],
                       35, BLACK, WIDTH/2-10, HEIGHT/2-10)

        play_multi_sprites.update()
        play_multi_sprites.draw(screen)

    if IS_PLAY_SINGLE_END == 1:
        if play_single_end_init:
            pygame.mixer.music.stop()
            play_single_end_init = False
            play_single_end_sprites = pygame.sprite.Group()
            while len(BUTTON_LIST) > 0:
                BUTTON_LIST[0].button_box.move_ip(-1000, -1000)
                BUTTON_LIST[0].kill()
                del BUTTON_LIST[0]
            BUTTON_LIST=[]
            if IS_WIN == 1:
                IS_WIN = 0
                i = 0
                while i < len(RON_HAND_CARD_ID_LIST):
                    ron_card = Mahjong_Img(RON_HAND_CARD_START_X + (i*MAHJONG_WIDTH),
                                           RON_HAND_CARD_START_Y, MAHJONG_IMG_DICT[RON_HAND_CARD_ID_LIST[i]])
                    play_single_end_sprites.add(ron_card)
                    i += 1
                i += 1
                vice_dews_start_x = RON_HAND_CARD_START_X + (i*MAHJONG_WIDTH)
                i = 0
                while i < len(RON_VICE_DEWS_ID_LIST):
                    ron_card = Mahjong_Img(vice_dews_start_x + (i*MAHJONG_WIDTH),
                                           RON_HAND_CARD_START_Y, MAHJONG_IMG_DICT[RON_VICE_DEWS_ID_LIST[i]])
                    play_single_end_sprites.add(ron_card)
                    i += 1
                i += 1
                ron_card_start_x = vice_dews_start_x + (i*MAHJONG_WIDTH)
                ron_card = Mahjong_Img(
                    ron_card_start_x, RON_HAND_CARD_START_Y, MAHJONG_IMG_DICT[RON_CARD_ID])
                play_single_end_sprites.add(ron_card)
            ###########################
            # 結束按鈕
            end_button = Button(574, 490, "end", True, end_img)
            play_single_end_sprites.add(end_button)
            BUTTON_LIST.append(end_button)

        # bilt()畫,(要畫的圖片,要畫的位置)#####底,要顯示的東西放在這後面
        screen.blit(end_background_img, (0, 0))

        draw_chinese_texts(screen, [f"{WIN_TEXT}"], 50, WHITE, 100, 130)
        



        play_single_end_sprites.update()
        play_single_end_sprites.draw(screen)

    if IS_PLAY_MULTI_END == 1:
        if play_multi_end_init:
            play_multi_end_init = False
            play_multi_end_sprites = pygame.sprite.Group()
            main_send_cSocket.close()
            main_recv_cSocket.close()
            sub_send_cSocket.close()
            sub_recv_cSocket.close()

            if IS_WIN == 1:
                i = 0
                while i < len(RON_HAND_CARD_ID_LIST):
                    ron_card = Mahjong_Img(RON_HAND_CARD_START_X + (i*MAHJONG_WIDTH),
                                           RON_HAND_CARD_START_Y, MAHJONG_IMG_DICT[RON_HAND_CARD_ID_LIST[i]])
                    play_multi_end_sprites.add(ron_card)
                    i += 1
                i += 1
                vice_dews_start_x = RON_HAND_CARD_START_X + (i*MAHJONG_WIDTH)
                i = 0
                while i < len(RON_VICE_DEWS_ID_LIST):
                    ron_card = Mahjong_Img(vice_dews_start_x + (i*MAHJONG_WIDTH),
                                           RON_HAND_CARD_START_Y, MAHJONG_IMG_DICT[RON_VICE_DEWS_ID_LIST[i]])
                    play_multi_end_sprites.add(ron_card)
                    i += 1
                i += 1
                ron_card_start_x = vice_dews_start_x + (i*MAHJONG_WIDTH)
                ron_card = Mahjong_Img(
                    ron_card_start_x, RON_HAND_CARD_START_Y, MAHJONG_IMG_DICT[RON_CARD_ID])
                play_multi_end_sprites.add(ron_card)
            ###########################
            # 結束按鈕
            end_button = Button(574, 490, "end", True, end_img)
            play_multi_end_sprites.add(end_button)
            BUTTON_LIST.append(end_button)
        # bilt()畫,(要畫的圖片,要畫的位置)#####底,要顯示的東西放在這後面
        screen.blit(end_background_img, (0, 0))

        draw_chinese_texts(screen, [f"{WIN_SITE}"], 50, WHITE, 100, 130)

        play_multi_end_sprites.update()
        play_multi_end_sprites.draw(screen)

    # draw_texts(screen,TEXT_LIST,40,20,20)
    # .update()
    # .draw(screen)
    pygame.display.update()  # 更新畫面
