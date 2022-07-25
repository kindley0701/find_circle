# ライブラリの読込
import cv2
import numpy as np


def find_circle():
    # 検出する画像の選択(プログラム実行時に選択できるようにしたいなぁ...)
    path = "2022-06-21 (83).png"
    # OpenCVでの画像の読み込み
    img = cv2.imread(path)

    # 画像処理のノイズ除去のため一旦グレースケールに変更
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 円を検出
    circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, dp=0.8, minDist=600, param1=100, param2=60, minRadius=100, maxRadius=400)
    # HoughCircles(画像の取込，ハフ変換の手法，dp=解像度，minDist=円同士の最小距離，param1=わからん，param2=円検出レベル，minRadius=最小半径，maxRadius=最大半径)

    # numpyを用いて描画できる形に変換
    circles = np.uint16(np.around(circles))

    # 円が見つかるかで条件分岐
    if len(circles): #円が検出された場合
        for circle in circles[0, :]:
        # 円周を描画
            img_painted1 = cv2.circle(img, (circle[0], circle[1]), circle[2], (0, 0, 255), 3)
            # circle(画像の読込，(わからん，わからん)，わからん，(色)，線の太さ)

        # 中心点を描画
            img_painted2 = cv2.circle(img_painted1, (circle[0], circle[1]), 2, (0, 0, 255), 2)
            # circle(画像の読込，(わからん，わからん)，わからん，(色)，点の大きさ)


        # 拡大縮小
        img_resize = cv2.resize(img_painted2, dsize=None, fx=0.5, fy=0.5)

        # 画像の表示
        cv2.imshow('img2', img_resize)
        cv2.waitKey(0)

    else: #円が検出されなかった場合
        print('見つかりませんでした')

find_circle()