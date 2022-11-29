import tkinter as tk
import tkinter.messagebox as tkm


# 練習３
def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        siki = entry.get()
        res = eval(siki)#数式の評価
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)#計算結果
    elif num == "AC":
        entry.delete(0,tk.END)#表示文字列全て削除
    elif num == "C":
        entry.delete(tk.END,-1)
    else: #「=」以外のボタン字
        #tkm.showinfo("", f"{num}ボタンがクリックされました")
        # 練習６
        entry.insert(tk.END, num)

    
# 練習１
root = tk.Tk()
root.geometry("400x600")

# 練習４
entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row=0, column=0, columnspan=4)

# 練習２
r, c = 1, 0
operatorsn =["7","8","9","4","5","6","1","2","3","0"]
for num in operatorsn:
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30),bg="white")
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0
# 練習５
operators = ["+", "-","/","*","="]
r,c=1,3
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30),bg="skyblue")
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    if c%3==0:
        r+=1

fanctions = ["AC"]
r,c = 4,2
for fnc in fanctions:
    button = tk.Button(root, text=f"{fnc}", width=4, height=2, font=("", 30),bg="skyblue")
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1

root.mainloop()