import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm

def key_down(event):
    global key, start
    key = event.keysym
    if not start:
        start=True #ゲームがスタートしたフラグ
        count_up()#ゲームがスタートしたら一度呼び出される


def key_up(event):
    global key
    key = ""

def count_up():
    global tmr
    label["text"] = tmr
    tmr += 1
    root.after(1000,count_up)


def main_proc():
    global cx, cy, mx, my
    if key == "Shift_L":#左シフトを押したらやり直し
        mx = 1
        my = 1
    if maze_list[mx][my] == 0:
        if key == "Up": my -= 1
        if key == "Down": my += 1
        if key == "Left": mx -= 1
        if key == "Right": mx += 1
        canvas.coords("kokaton", cx, cy)#迷っているこうかとん

    if maze_list[mx][my] == 1:#移動先が壁だったら
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1
        canvas.coords("komarukokaton",cx,cy)#壁に当たり困るこうかとん

    cx ,cy = (mx*100)+50, (my*100)+50
    if mx == 7 and my == 13:#右下のマスに着いたらクリア表示
        canvas.update()
        tkm.showinfo("クリア")
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()

    start = False

    tmr = 0
    label = tk.Label(root,text="-",font=("",80))
    label.pack()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_list = mm.make_maze(15,9)
    mm.show_maze(canvas,maze_list)
    #print(maze_list)

    mx, my = 1, 1
    cx, cy = (mx*100)+50, (my*100)+50
    tori = tk.PhotoImage(file="fig/0.png")
    komarutori = tk.PhotoImage(file="fig/8.png")
    canvas.create_image(cx, cy, image=tori, tag="kokaton")
    canvas.create_image(cx, cy, image=komarutori, tag="komarukokaton")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()

    root.mainloop()