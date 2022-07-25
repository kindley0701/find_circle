# バブルの変形を検出するためのプログラムを作成中

## change_circle_to_rectangle
このファイルと同レベルに画像を入れ，ファイル内のpathに代入．
その画像から円を検出し，その中心からの距離を横軸，極座標時の角度を縦軸として，長方形表示に変換した画像をcv2形式で表示．
問題点：2つの円を検出しているはずなのに，長方形化画像は一つしか出てこない．

## find_circle_movie.py
動画内で円の検出を行うもの(未完成)

## find_circle_v1.py
このファイルと同レベルに画像を入れ，ファイル内のpathに代入．
その画像の円を検出し，cv2形式で表示．

## find_circle_v2.py
プログラム実行後，画像ファイルを選択可能．
その画像の円を検出し，cv2形式で表示．

## find_circle_v3.py
プログラム実行後，画像ファイルを選択可能．
その画像の円を検出し，tkinter形式でキャンバスに表示．

## find_contour.py
このファイルと同レベルに画像を入れ，ファイル内の4行目にpathを記入．
実行すると輪郭を検出し，cv2形式で表示．

## show_picture.py
プログラム実行後，画像ファイルを選択可能．
選択した画像をtkinter形式でキャンバスに表示．