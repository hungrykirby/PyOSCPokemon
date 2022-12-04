import tkinter
import tkinter.ttk
from PIL import Image, ImageTk, ImageDraw
import os

'''
クリックした画像の座標位置をログに出力する
OCR解析するときに座標が知りたいので
'''

class Application(tkinter.Frame):
    image_width = 0
    image_height = 0

    def __init__(self, master=None):
        super().__init__(master)

        self.ratio = 0.3

        self.master = master
        self.master.title('title')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # ボタン
        self.original_button = tkinter.ttk.Button(self, text='reset')
        self.original_button.grid(row=0, column=1)
        self.original_button.bind('<Button-1>', make_original)

        # canvas
        self.test_canvas = tkinter.Canvas(self,
            width=resized_image.width,
            height=resized_image.height
        )
        self.test_canvas.grid(row=0, column=0, rowspan=3)

        # canvasに初期画像を表示
        self.test_canvas.photo = ImageTk.PhotoImage(resized_image)
        self.image_on_canvas = self.test_canvas.create_image(0, 0, anchor='nw', image=self.test_canvas.photo)

        #クリックで座標取得
        self.test_canvas.bind("<ButtonPress-1>", ButtonPress)


def make_original(event):
    os.remove('tmp.png')
    set_image(event, resized_image)

def ButtonPress(event):        
    a = event.x
    b = event.y
    a_m = a - 5
    b_p = b + 5
    a_p = a + 5
    b_m = b - 5
    
    draw = resized_image.copy()
    draw2 = ImageDraw.Draw(draw)
    draw2.rectangle(((a_m, b_p), (a_p, b_m)), fill = (0, 0, 255), outline = 'white',  width = 2)
    draw.save('tmp.png')
    draw_image = Image.open('tmp.png')
    set_image(event, draw_image)
    print("clicked at ", event.x / ratio, event.y / ratio) 

def set_image(_event, img):
    # canvasの書き換え
    app.test_canvas.photo = ImageTk.PhotoImage(img)
    app.test_canvas.itemconfig(app.image_on_canvas, image=app.test_canvas.photo)

ratio = 0.3

IMAGE_FILE_NAME = 'input02.jpg'

# 画像ファイル読み込み
original_image = Image.open('images/' + IMAGE_FILE_NAME)
resized_image = original_image.resize((
    int(original_image.width * ratio),
    int(original_image.height * ratio)
))

# アプリケーション起動
root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
