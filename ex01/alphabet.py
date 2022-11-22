import random
import datetime

repeat = 5
sub = 10
miss = 2



if __name__ == "__main__":
    st = datetime.datetime.now()
    for i in rage(repeat):
        seikai = shutudai()
        f = kaitou(seikai)
        if f == 1:
            break
    et = datetime.datetime.now()
    time = et - st
    print(f"回答時間{time}秒")

def shutudai():
    alphabets = [chr(c+65) for c in range(26)]
    sub_lst = random.sample(alphabets,repeat)
    print(f"対象文字:{sub_lst}")
    miss_lst = 
