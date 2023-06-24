import tkinter
import random
from PIL import Image, ImageTk

MOLE_PATH = "animal_chara_mogura_hakase.png" # モグラの画像のファイルパス
NUM_H_HOLE = 4 # 横方向の穴の数
NUM_V_HOLE = 3 # 縦方向の穴の数
WIDTH_HOLE = 100 # 穴の幅（長軸の長さ）
HEIGHT_HOLE = 50 # 穴の高さ（短軸の長さ）
WIDTH_SPACE = 20 # 穴と穴のスペースの幅
HEIGHT_SPACE = 80 # 穴と穴のスペースの高さ
POINT_DRAW_TIME = 500 # 加算or減算されたポイントが表示される時間
MOLE_UPDATE_INTERVAL = 100 # モグラの状態や位置を更新する時間間隔
FIGURE_UPDATE_INTERVAL = 100 # モグラの画像を更新する時間間隔
MOLE_CHOICE_INTERVAL = 1000 # 穴から出すモグラを決める時間間隔