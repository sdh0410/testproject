import tkinter
import random

fnt1 = ("Times New Roman", 24)
fnt2 = ("Times New Roman", 50)
index = 0
timer = 0
score = 0
bg_pos = 0
METEO_MAX = 5
umx = [0] * METEO_MAX
umy = [0] * METEO_MAX
lmx = [0] * METEO_MAX
lmy = [0] * METEO_MAX
rmx = [0] * METEO_MAX
rmy = [0] * METEO_MAX
dmx = [0] * METEO_MAX
dmy = [0] * METEO_MAX
w=1440
h=1200
gamesp=20;
px = w/2
py = h/2
key = ""
koff = False
def key_down(e):
    global key, koff
    key = e.keysym
    koff = False

def key_up(e):
    global koff
    koff = True

def main():
    global key, koff, index, timer, score, bg_pos, px
    timer = timer + 1
    bg_pos = (bg_pos + 1) % h
    canvas.delete("SCREEN")
    canvas.create_image(w/2, bg_pos - h/2, image=img_bg, tag="SCREEN")
    canvas.create_image(w/2, bg_pos + h/2, image=img_bg, tag="SCREEN")
    if index == 0:
        canvas.create_text(w/2, 240, text="AVODING LOL", fill="gold", font=fnt2, tag="SCREEN")
        canvas.create_text(w/2, 480, text="Press [SPACE] Key", fill="lime", font=fnt1, tag="SCREEN")
        if key == "space":
            score = 0
            px = 240
            init_enemy()
            index = 1
    if index == 1:
        score = score + 1
        move_player()
        umove_enemy()
        lmove_enemy()
        rmove_enemy()
        dmove_enemy()
    if index == 2:
        umove_enemy()
        lmove_enemy()
        rmove_enemy()
        dmove_enemy()
        canvas.create_text(w/2, timer * 4, text="GAME OVER", fill="red", font=fnt2, tag="SCREEN")
        if timer == 60:
            index = 0
            timer = 0
    canvas.create_text(w/2, 30, text="SCORE " + str(score), fill="white", font=fnt1, tag="SCREEN")
    if koff == True:
        key = ""
        koff = False
    root.after(gamesp, main)#속도감 설명(실행 빈도 연관지어서)

def hit_check(x1, y1, x2, y2):
    if ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) < 50 * 50):
        return True
    return False

def init_enemy():
    for i in range(METEO_MAX):
        umx[i] = random.randint(0, w)
        umy[i] = random.randint(-h, 0)
        lmx[i] = random.randint(-w,0)
        lmy[i] = random.randint(0,h)
        rmx[i] = random.randint(0,w)
        rmy[i] = random.randint(0,h)

def umove_enemy():
    global index, timer
    for i in range(METEO_MAX):
        umy[i] = umy[i] + 6 + i*5 / 5
        if umy[i] > h:
            umx[i] = random.randint(0, w)
            umy[i] = random.randint(-h, 0)
        if index == 1 and hit_check(px, py, umx[i], umy[i]) == True:
            index = 2
            timer = 0
        if(i<=2):
            canvas.create_image(umx[i], umy[i], image=img_enemy1, tag="SCREEN")
        elif(i<=3):
            umy[i]+=1
            canvas.create_image(umx[i], umy[i], image=img_enemy2, tag="SCREEN")
        else:
            umy[i]+=3
            canvas.create_image(umx[i], umy[i], image=img_enemy3, tag="SCREEN")

def dmove_enemy():
    global index, timer
    for i in range(METEO_MAX):
        dmy[i] -=  6 + i*5 / 5
        if dmy[i] < 0:
            dmx[i] = random.randint(0, w)
            dmy[i] = random.randint(h, 2*h)
        if index == 1 and hit_check(px, py, dmx[i], dmy[i]) == True:
            index = 2
            timer = 0
        if(i<=2):
            canvas.create_image(dmx[i], dmy[i], image=img_enemy1d, tag="SCREEN")
        elif(i<=3):
            dmy[i]-=1
            canvas.create_image(dmx[i], dmy[i], image=img_enemy2d, tag="SCREEN")
        else:
            dmy[i]-=3
            canvas.create_image(dmx[i], dmy[i], image=img_enemy3d, tag="SCREEN")
     
def lmove_enemy():
    global index, timer
    for i in range(METEO_MAX):
        lmx[i] = lmx[i] + 6 + i*5 / 5
        if lmx[i] > w:
            lmx[i] = random.randint(-w,0)
            lmy[i] = random.randint(0,h)
        if index == 1 and hit_check(px, py, lmx[i], lmy[i]) == True:
            index = 2
            timer = 0
        if(i<2):
            canvas.create_image(lmx[i], lmy[i], image=img_enemy1l, tag="SCREEN")
        elif(i<=3):
            lmx[i]+=1
            canvas.create_image(lmx[i], lmy[i], image=img_enemy2l, tag="SCREEN")
        else:
            lmx[i]+=3
            canvas.create_image(lmx[i], lmy[i], image=img_enemy3l, tag="SCREEN")
def rmove_enemy():
    global index, timer
    for i in range(METEO_MAX):
        rmx[i] -= 6 + i*5 / 5
        if rmx[i] < 0:
            rmx[i] = random.randint(w,2*w)
            rmy[i] = random.randint(0,h)
        if index == 1 and hit_check(px, py, rmx[i], rmy[i]) == True:
            index = 2
            timer = 0
        if(i<2):
            canvas.create_image(rmx[i], rmy[i], image=img_enemy1r, tag="SCREEN")
        elif(i<=3):
            rmx[i]-=1
            canvas.create_image(rmx[i], rmy[i], image=img_enemy2r, tag="SCREEN")
        else:
            rmx[i]-=3
            canvas.create_image(rmx[i], rmy[i], image=img_enemy3r, tag="SCREEN")

def move_player():#방향키를 wasd등으로 바꾸는 방법 설명
    global px,py,score,gamesp
    if key == "Left" and px > 30:
        px = px - 10
    if key == "Right" and px < w-30:
        px = px + 10
    if key == "Up" and py > 30:
        py = py - 10
    if key == "Down" and py < h-30:
        py = py + 10
    if score<=1000:
        canvas.create_image(px, py, image=img_player[0], tag="SCREEN")
    else:
        gamesp=16
        canvas.create_image(px, py, image=img_player[1], tag="SCREEN")
        

root = tkinter.Tk()
root.title("Mini Game")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=w, height=h)
canvas.pack()
img_player = [
    tkinter.PhotoImage(file="바위게.png"),
    tkinter.PhotoImage(file="공허바위게.png")
]
img_enemy1 = tkinter.PhotoImage(file="가렌.png")#이미지 설명(원하는 그림으로 바꾸는 방법 설명)
img_enemy2 = tkinter.PhotoImage(file="사이온.png")
img_enemy3 = tkinter.PhotoImage(file="워윅.png")
img_enemy1d = tkinter.PhotoImage(file="d가렌.png")
img_enemy2d = tkinter.PhotoImage(file="d사이온.png")
img_enemy3d = tkinter.PhotoImage(file="d워윅.png")
img_enemy1l = tkinter.PhotoImage(file="l가렌.png")
img_enemy2l= tkinter.PhotoImage(file="l사이온.png")
img_enemy3l = tkinter.PhotoImage(file="l워윅.png")
img_enemy1r = tkinter.PhotoImage(file="r가렌.png")
img_enemy2r= tkinter.PhotoImage(file="r사이온.png")
img_enemy3r = tkinter.PhotoImage(file="r워윅.png")


img_bg = tkinter.PhotoImage(file="협곡.png")
main()
root.mainloop()
