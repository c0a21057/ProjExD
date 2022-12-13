import pygame as pg
import random
import sys


def check_bound(obj_rct, scr_rct):
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()
    (x,y) = (900,400)
    pg.init()
    koka_sfc = pg.image.load("fig/6.png")            #こうかとんの画像
    koka_sfc = pg.transform.rotozoom(koka_sfc,0,2.0) #画像を二倍

    # 練習１
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    font = pg.font.Font(None,100)                     #画面に文字を表示
    txt = font.render("Douge the bomb!",False,(0,0,0))

 

    # 練習５
    bomb_sfc = pg.Surface((60, 60)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))

    pg.draw.circle(bomb_sfc, (255, 0, 0), (30, 30), 30) #爆弾のサイズを大きくした
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)
    

    vx, vy = +8, +8

    # 練習２
    while True:
        pg.display.update()     #画面更新
        pg.time.wait(1)         #更新時間間隔
        koka_rct = scrn_sfc.blit(koka_sfc,(x,y)) #こうかとんの描画
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 
        scrn_sfc.blit(koka_sfc, koka_rct)

        for event in pg.event.get():
            #マウスポインタで画像移動
            if event.type == pg.MOUSEMOTION:
                x, y = event.pos
                x -= int(koka_sfc.get_width() / 2) #こうかとんの真ん中にマウスカーソルがくる
                y -= int(koka_sfc.get_height() / 2)
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:    #エスケープキーが押されたら終了
                if event.key == pg.K_ESCAPE:
                    sys.exit()

            

        # 練習６
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        scrn_sfc.blit(txt,(10,10))

        #練習８
        if koka_rct.colliderect(bomb_rct):
            return#mainから出る

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()