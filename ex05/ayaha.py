import pygame as pg
import sys
import time, random
def main():
    color_red = pg.Color(255, 0, 0)
    color_white = pg.Color(255, 255, 255)
    color_green = pg.Color(0, 255, 0)
    pg.init()
    screen = pg.display.set_mode((600, 400))
    screen.fill(color_white)
    pg.display.set_caption("蛇")
    arr = [([0] * 41) for i in range(61)]  
    x = 10  # 蛇の初期x座標
    y = 10  # 蛇の初期y座標
    foodx = random.randint(1, 60)  # 食べ物のx座標
    foody = random.randint(1, 40)  # 食べ物のy座標
    arr[foodx][foody] = -1
    snake_lon = 3 #蛇の長さ
    way = 1  # 蛇の運動方向

    fonto = pg.font.Font(None,80)
    fonto2 = pg.font.Font(None,30)
    appnum = 3 #りんごゲットのノルマ
    app = fonto2.render((f"APPLE:{appnum}"),True,(0,0,0)) #残りのりんごの獲得ノルマ表示
    clear = fonto.render("Game Clear",True,(0,0,255))#ゲームクリアの表示
    gover = fonto.render("Game Over",True,(255,0,0))#ゲームオーバーの表示
    game = True #ゲームが続いているかのフラグ
    while True:
        if game:
            screen.fill(color_white)
            screen.blit(app,(50,50))#スクリーンに表示
            time.sleep(0.1)
            for event in pg.event.get():  
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if (event.key == pg.K_RIGHT) and (way != 2):  # 右
                        way = 1
                    if (event.key == pg.K_LEFT) and (way != 1):  # 左
                        way = 2
                    if (event.key == pg.K_UP) and (way != 4):  # 上
                        way = 3
                    if (event.key == pg.K_DOWN) and (way != 3):  # 下に移動
                        way = 4
            if way == 1:
                x += 1
            if way == 2:
                x -= 1
            if way == 3:
                y -= 1
            if way == 4:
                y += 1
            if (x > 60) or (y > 40) or (x < 1) or (y < 1):  # 死亡(壁にぶつかったら)
                screen.blit(gover,(160,150))#ゲームオーバーの表示
                pg.display.update()
                game= False
            arr[x][y] = snake_lon
            for a, b in enumerate(arr, 1):
                for c, d in enumerate(b, 1):
                    # 食べ物は-1，空地は0，蛇の位置は正数
                    if (d > 0):
                        # print(a,c) #蛇の座標を表示
                        arr[a - 1][c - 1] = arr[a - 1][c - 1] - 1
                        pg.draw.rect(screen, color_green, ((a - 1) * 10, (c - 1) * 10, 10, 10))
                    if (d < 0):
                        pg.draw.rect(screen, color_red, ((a - 1) * 10, (c - 1) * 10, 10, 10))
            if (x == foodx) and (y == foody):   #蛇が食べ物を食べったら
                appnum -= 1
                app = fonto2.render((f"APPLE:{appnum}"),True,(0,0,0)) #残りのりんごの獲得ノルマ表示
                snake_lon += 1
                while (arr[foodx][foody] != 0):    #新しい食べ物を表示
                    foodx = random.randint(1, 60)
                    foody = random.randint(1, 40)
                arr[foodx][foody] = -1
                pg.display.update()
                if appnum < 1:                   #りんごのノルマを達成していたら
                    screen.blit(clear,(160,160)) #クリア表示
                    pg.display.update()
                    game = False #ゲームオーバーのフラグ
        else:
            for event in pg.event.get():  
                if event.type == pg.QUIT:
                    sys.exit()
            
        pg.display.flip()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
