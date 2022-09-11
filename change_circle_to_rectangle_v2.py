### インポート
import tkinter
import tkinter.filedialog
import cv2
import numpy as np

### 定数
WIDTH  = 1000        # 幅
HEIGHT = 700        # 高さ

### tkinterで画像を選択する関数
def select_photo():

    ### グローバル変数
    global image

    ### ファイルダイアログ
    name = tkinter.filedialog.askopenfilename(title="ファイル選択", initialdir="C:/", filetypes=[("Image File","*.png")])

    ### 画像ロード
    image = tkinter.PhotoImage(file=name)

    ### キャンバスに表示
    #canvas.create_image(WIDTH/2, HEIGHT/2, image=image)

    return image

# 画像をtkinter形式からcv2形式へ変換する関数
def tk_to_cv2(tk_image):
    'Tkinter -> CV2'

    # 画像の縦横サイズを取得
    height = tk_image.height()
    width = tk_image.width()

    # ピクセルデータの３次元リストを作成

    # 空のリストを作成
    bitmap = []
    for y in range(height):
        # 空のリストを作成
        line = []
        for x in range(width):

            # 座標(x,y)のピクセルデータを取得
            pixel = list(tk_image.get(x, y))

            # 取得したピクセルデータをリストに追加
            line.append(pixel)

        # 1行分のピクセルデータを追加
        bitmap.append(line)

    # 作成したリストをNumPy配列に変換
    cv2_rgb_image = np.array(bitmap, dtype='uint8')

    # RGB -> BGRによりCV2画像オブジェクトに変換
    cv2_image = cv2.cvtColor(cv2_rgb_image, cv2.COLOR_RGB2BGR)

    return cv2_image

# 画像から円を検出する関数
def change_rec_img(img):
    # 検出する画像の選択(プログラム実行時に選択できるようにしたいなぁ...)
    #path = "2022-06-21 (83).png"
    # OpenCVでの画像の読み込み
    #img = cv2.imread(path)

    #変換フラグ(キュービック補間 + 外れ値塗りつぶし + 極座標へのリニアマッピング)
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
          # 円周を描画
          img_painted1 = cv2.circle(img, (circle[0], circle[1]), circle[2], (0, 0, 255), 2)
          # circle(画像の読込，(中心のx座標，中心のy座標)，中心からの距離，(色)，線の太さ)
          # 中心からの距離を検出した円の半径にすることで検出円の外周を描くことができる．

          # 中心点を描画
          img_painted2 = cv2.circle(img_painted1, (circle[0], circle[1]), 2, (0, 0, 255), 2)
          # circle(画像の読込，(中心のx座標，中心のy座標)，中心からの距離，(色)，線の太さ)
          # 線の太さと中心からの距離を同じ値にすることで点にできる→検出円の中心を描画できる．

          #中心点の座標=(x,y)の取得
          center = (circle[0], circle[1])

          #半径の取得
          radius = circle[2]
          
          #変換後の画像サイズ
          height, width = 625, 500
          
          #極座標化
          rec_image = cv2.warpPolar(img, (height, width), center, radius + 50, flags)
          #warpPolar(対象画像, (出力画像サイズ), 極座標化の中心, 極座標化する部分の半径, 変換フラグ)

          # 画像の表示
          cv2.imshow('rec_img{}'.format(circle), rec_image)
          # 画像の名前を検出円ごとに変えないと1枚しか出てこなくなる．
          # ''の中に{}を入れ，.format(circle)を付けることで{}にcircleの値を入れた文字列に変換できる．

        #キーボードで何か押すのを待つ(このあとのは何もないので何を押しても終了する．)
        cv2.waitKey(0)

    else: #円が検出されなかった場合
        print('見つかりませんでした')

### メイン画面作成
main = tkinter.Tk()

### 画面サイズ設定
main.geometry("1000x700")

### ボタン作成・配置
button = tkinter.Button(main, text="ファイル選択", command=change_rec_img(tk_to_cv2(select_photo())))
button.pack()

### キャンバス作成・配置
canvas = tkinter.Canvas(main, width=WIDTH, height=HEIGHT)
canvas.pack()

### イベントループ
main.mainloop()