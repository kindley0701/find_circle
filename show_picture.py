### インポート
import tkinter
import tkinter.filedialog
 
### 定数
WIDTH  = 1000        # 幅
HEIGHT = 700        # 高さ
 
### 関数
def func():
 
    ### グローバル変数
    global image
 
    ### ファイルダイアログ
    name = tkinter.filedialog.askopenfilename(title="ファイル選択", initialdir="C:/", filetypes=[("Image File","*.png")])
 
    ### 画像ロード
    image = tkinter.PhotoImage(file=name)
 
    ### キャンバスに表示
    canvas.create_image(WIDTH/2, HEIGHT/2, image=image)
 
### メイン画面作成
main = tkinter.Tk()
 
### 画面サイズ設定
main.geometry("1000x700")
 
### ボタン作成・配置
button = tkinter.Button(main, text="ファイル選択", command=func)
button.pack()
 
### キャンバス作成・配置
canvas = tkinter.Canvas(main, width=WIDTH, height=HEIGHT)
canvas.pack()
 
### イベントループ
main.mainloop()