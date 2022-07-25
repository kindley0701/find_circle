import cv2
import numpy as np


# 検出する画像の選択(プログラム実行時に選択できるようにしたいなぁ...)
path = "capture.png"
# OpenCVでの画像の読み込み
img = cv2.imread(path)

flags = cv2.INTER_CUBIC + cv2.WARP_FILL_OUTLIERS + cv2.WARP_POLAR_LINEAR

# 画像処理のノイズ除去のため一旦グレースケールに変更
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 円を検出
circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, dp=0.8, minDist=600, param1=100, param2=60, minRadius=100, maxRadius=400)
# HoughCircles(画像の取込，ハフ変換の手法，dp=解像度，minDist=円同士の最小距離，param1=わからん，param2=円検出レベル，minRadius=最小半径，maxRadius=最大半径)
#circle = [中心x，中心y，半径]の配列で数値が得られる．

# numpyを用いて描画できる形に変換
circles = np.uint16(np.around(circles))

# 円が見つかるかで条件分岐
if len(circles): #円が検出された場合
    for circle in circles[0, :]:
      center = (circle[0], circle[1])
      radius = circle[2]
      height, width = 250, 500
      result_image = cv2.warpPolar(img, (height, width), center, radius + 50, flags)

      # 画像の表示
      cv2.imshow('rec_img', result_image)

    #キーボードで何か押すのを待つ(このあとのは何もないので何を押しても終了する．)
    cv2.waitKey(0)

else: #円が検出されなかった場合
    print('見つかりませんでした')