from tkinter import * 
from tkinter.tix import *
import numpy as np
from PIL import Image,ImageTk
from docx2python import docx2python 



root = Tk()
root.geometry("1200x600")
root.title("Make by Ingredients")
root.option_add("*font","helevitica 24")
root.resizable(0,0)


swin = ScrolledWindow(root, width=1200, height=500)
swin.grid(column = 0,columnspan = 2 , row = 0)
win = swin.window



Label(win,text = " ").pack()
Label(win,text = " ").pack()
Label(win,text = "ผัก 🥦",fg = "green").pack()
Label(win,text = " ").pack()

swinveg = ScrolledWindow(win, width=1000, height=300)
swinveg.pack()
winveg = swinveg.window




Label(win,text = " ").pack()
Label(win,text = " ").pack()    
Label(win,text = "ความเผ็ด 🌶",fg = "red").pack()
Label(win,text = " ").pack()

swinpep = ScrolledWindow(win, width=1000, height=300)
swinpep.pack()
winpep = swinpep.window




Label(win,text = " ").pack()
Label(win,text = " ").pack()
Label(win,text = "เนื้อสัตว์ 🥩",fg = "red").pack()
Label(win,text = " ").pack()

swinmeat = ScrolledWindow(win, width=1000, height=300)
swinmeat.pack()
winmeat = swinmeat.window




Label(win,text = " ").pack()
Label(win,text = " ").pack()
Label(win,text = "อาหารทะเล 🌴",fg = "blue").pack()
Label(win,text = " ").pack()

swinsea = ScrolledWindow(win, width=1000, height=300)
swinsea.pack()
winsea = swinsea.window




Label(win,text = " ").pack()
Label(win,text = " ").pack()
Label(win,text = "เครื่องปรุง 🍦",fg = "black").pack()
Label(win,text = " ").pack()

swingar = ScrolledWindow(win, width=1000, height=300)
swingar.pack()
wingar = swingar.window




Label(win,text = " ").pack()
Label(win,text = " ").pack()
Label(win,text = "ทั่วไป 🍽",fg = "black").pack()
Label(win,text = " ").pack()

swinnm = ScrolledWindow(win, width=1000, height=300)
swinnm.pack()
winnm = swinnm.window







veg = np.array(['ใบกะเพรา','ถั่วฝักยาว','แตงกวา','ต้นหอม','ใบโหระพา','มะเขือเทศ','ใบมะกรูด','ตะไคร้','ข่า','แครอท','คะน้า','ขึ้นฉ่าย','ผักกาดหอม'])  #13
veg2 = np.array(['ผักบุ้ง','ผักกาดขาว','ผักชีฝรั่ง','ผักกระเฉด','เห็ดหูหนู','มะระ','เห็ดหอม','ขิงอ่อน','สะระแหน่','เห็ดฟาง','เห็ดเข็มทอง','บล็อกโคลี่','พริกหยวก','เห็ดหิมะ'])    #14
pep = np.array(['พริกขี้หนู','พริกไทยเม็ด','น้ำพริก','พริกไทยป่น','พริกชี้ฟ้า']) #5
meat = np.array(["กุนเชียง","แหนม","เนื้อหมู","หมูยอ","ไส้กรอก","เนื้อวัว","เนื้อไก่","ปีกไก่","เนื้อปลากราย","มันหมู","หมูสับ"])   #11
sea = np.array(["กุ้ง","ปลาหมึก","ปลากระป๋อง","เนื้อปลา","ปูอัด","ปลาทู"])   #6
gar = np.array(["เกลือ","กระเทียม","น้ำปลา","น้ำตาลทราย","ซอสหอยนางรม","ซีอิ๊วขาว","ผงชูรส","หอมใหญ่","น้ำส้มสายชู","เต้าหู้ยี้"])  #10
gar2 = np.array(["มะนาว","ซุปก้อน","หอมแดง","กระเทียมเจียว","ซีอิ๊วดำ","รากผักชี","น้ำมะนาว","น้ำตาลปิ๊บ","น้ำตาลทราย"])  #9
nm = np.array(["วุ้นเส้น","ไข่ไก่","ไข่เป็ด","เนยสด","ขนมจีน","มาม่า","เต้าหู้ไข่","เกล็ดขนมปัง","แป้งข้าวโพด","แป้งสาลี"])    #10
together = np.array([veg,veg2,pep,meat,sea,gar,gar2,nm])



vegch = [BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False)]
vegch2 = [BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False) ]
pepch = [BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False)]
meatch = [BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False)]
seach = [BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False)]
garch = [BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False)]
garch2 = [BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False)]
nmch =  [BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False),BooleanVar(value = False)]




cb = []
row = 2
column = 0
for i in range(len(veg)) :
    vegin = Checkbutton(winveg,text = veg[i],variable = vegch[i],width = 10 , height = 3)
    vegin.grid(row = row,column = column)
    cb.append(vegin)
    if column == 3 :
        column = -1
        row = row + 1
    column = column + 1

for i in range(len(veg2)) :
    vegin = Checkbutton(winveg,text = veg2[i],variable = vegch2[i],width = 10 , height = 3)
    vegin.grid(row = row,column = column)
    cb.append(vegin)
    if column == 3 :
        column = -1
        row = row + 1
    column = column + 1




row = 2
column = 0
for i in range(len(pep)) :
    pepin = Checkbutton(winpep,text = pep[i],variable = pepch[i],width = 10 , height = 3)
    pepin.grid(row = row,column = column)
    cb.append(pepin)
    if column == 3 :
        column = -1
        row = row + 1
    column = column + 1






row = 2
column = 0
for i in range(len(meat)) :
    meatin = Checkbutton(winmeat,text = meat[i],variable = meatch[i],width = 10 , height = 3)
    meatin.grid(row = row,column = column)
    cb.append(meatin)
    if column == 3 :
        column = -1
        row = row + 1
    column = column + 1






row = 2
column = 0
for i in range(len(sea)) :
    seain = Checkbutton(winsea,text = sea[i],variable = seach[i],width = 10 , height = 3)
    seain.grid(row = row,column = column)
    cb.append(seain)
    if column == 3 :
        column = -1
        row = row + 1
    column = column + 1






row = 2
column = 0
for i in range(len(gar)) :
    if(i != 3)  :
        garin = Checkbutton(wingar,text = gar[i],variable = garch[i],width = 10 , height = 3)
        garin.grid(row = row,column = column)
        cb.append(garin)
        if column == 3 :
            column = -1
            row = row + 1
        column = column + 1

for i in range(len(gar2)) :
    garin = Checkbutton(wingar,text = gar2[i],variable = garch2[i],width = 10 , height = 3)
    garin.grid(row = row,column = column)
    cb.append(garin)
    if column == 3 :
        column = -1
        row = row + 1
    column = column + 1





row = 2
column = 0
for i in range(len(nm)) :
    nmin = Checkbutton(winnm,text = nm[i],variable = nmch[i],width = 10 , height = 3)
    nmin.grid(row = row,column = column)
    cb.append(nmin)
    if column == 3 :
        column = -1
        row = row + 1
    column = column + 1



rww = 1
cll = 1


def search() :
    root2 = Toplevel()
    root2.geometry("1600x800")
    root2.title("Make by Ingredients")
    root2.option_add("*font","helevitica 24")
    root2.resizable(0,0)
    root2.grab_set()
    swin2 = ScrolledWindow(root2, width=1600, height=800)
    swin2.pack()
    win2 = swin2.window   
    def scb(name,row,col) :
        swinmenu = ScrolledWindow(win2, width=600, height=750)
        swinmenu.grid(row = row,column = col,padx = 70,pady = 100)
        winmenu = swinmenu.window
        Label(winmenu,text = " ").pack()
        Label(winmenu,text = name).pack()
        Label(winmenu,text = " ").pack()
        load = Image.open(name + ".jpg").resize((400,400))
        render = ImageTk.PhotoImage(load)
        photo = Label(winmenu,image = render)
        photo.image = render
        photo.pack()

        
        def detail() :
            root3 = Toplevel()
            root3.geometry("800x1000")
            root3.title(name)
            root3.option_add("*font","helevitica 24")
            root3.resizable(0,0)
            root3.grab_set()
            swin3 = ScrolledWindow(root3, width=800, height=1000)
            swin3.pack()
            win3 = swin3.window 

            Label(win3,text = " ").pack()
            Label(win3,text = name).pack()
            Label(win3,text = " ").pack()
            photo = Label(win3,image = render)
            photo.image = render
            photo.pack()
            Label(win3,text = " ").pack()

            
            def displaymethod(name) :
                cat=[]
                dog=[]
                mix=[cat,dog]
                buf=0
                method = docx2python(name+".docx")
                for i in method.body[0][0][0]   :
                    if i == "    วิธีทำ" :
                        buf=buf+1
                    mix[buf].append(i)
                for i in range(len(cat)) :
                    if ("ส่วนผสม" in cat[i]) or ("ใบกะเพรา" in cat[i] and vegch[0].get() == True) or ("ถั่วฝักยาว" in cat[i] and vegch[1].get() == True) or ("แตงกวา" in cat[i] and vegch[2].get() == True) or ("ต้นหอม" in cat[i] and vegch[3].get() == True) or ("ใบโหระพา" in cat[i] and vegch[4].get() == True) or ("มะเขือเทศ" in cat[i] and vegch[5].get() == True)  or ("ใบมะกรูด" in cat[i] and vegch[6].get() == True)   or ("ตะไคร้" in cat[i] and vegch[7].get() == True)  or ("ข่า" in cat[i] and vegch[8].get() == True)   or ("แครอท" in cat[i] and vegch[9].get() == True)   or ("คะน้า" in cat[i] and vegch[10].get() == True)    or ("ขึ้นฉ่าย" in cat[i] and vegch[11].get() == True)  or ("ผักกาดหอม" in cat[i] and vegch[12].get() == True)   or ("ผักบุ้ง" in cat[i] and vegch2[0].get() == True)  or ("ผักกาดขาว" in cat[i] and vegch2[1].get() == True)  or ("ผักชีฝรั่ง" in cat[i] and vegch2[2].get() == True)  or ("ผักกระเฉด" in cat[i] and vegch2[3].get() == True)  or ("เห็ดหูหนู" in cat[i] and vegch2[4].get() == True)  or ("มะระ" in cat[i] and vegch2[5].get() == True)  or ("เห็ดหอม" in cat[i] and vegch2[6].get() == True)  or ("ขิงอ่อน" in cat[i] and vegch2[7].get() == True)  or ("สาระแหน่" in cat[i] and vegch2[8].get() == True) or ("เห็ดฟาง" in cat[i] and vegch2[9].get() == True) or ("เห็ดเข็มทอง" in cat[i] and vegch2[10].get() == True) or ("บล็อกโคลี่" in cat[i] and vegch2[11].get() == True)  or ("พริกหยวก" in cat[i] and vegch2[12].get() == True)   or ("เห็ดหิมะ" in cat[i] and vegch2[13].get() == True)  or ("พริกขี้หนู" in cat[i] and pepch[0].get() == True) or ("พริกไทย" in cat[i] and pepch[1].get() == True)  or ("น้ำพริก" in cat[i] and pepch[2].get() == True)  or ("พริกไทย" in cat[i] and pepch[3].get() == True) or ("พริกชี้ฟ้า" in cat[i] and pepch[4].get() == True)   or ("กุนเชียง" in cat[i] and meatch[0].get() == True)  or ("แหนม" in cat[i] and meatch[1].get() == True) or ("เนื้อหมู" in cat[i] and meatch[2].get() == True)  or ("หมูยอ" in cat[i] and meatch[3].get() == True)  or ("ไส้กรอก" in cat[i] and meatch[4].get() == True)  or ("เนื้อวัว" in cat[i] and meatch[5].get() == True)  or ("เนื้อไก่" in cat[i] and meatch[6].get() == True)  or ("ปีกไก่" in cat[i] and meatch[7].get() == True) or ("เนื้อปลากราย" in cat[i] and meatch[8].get() == True)  or ("มันหมู" in cat[i] and meatch[9].get() == True)  or ("หมูสับ" in cat[i] and meatch[10].get() == True)  or ("กุ้ง" in cat[i] and seach[0].get() == True)  or ("ปลาหมึก" in cat[i] and seach[1].get() == True)  or ("ปลากระป๋อง" in cat[i] and seach[2].get() == True)  or ("เนื้อปลา" in cat[i] and seach[3].get() == True)  or ("ปูอัด" in cat[i] and seach[4].get() == True)  or ("ปลาทู" in cat[i] and seach[5].get() == True)   or ("เกลือ" in cat[i] and garch[0].get() == True)  or ("กระเทียม" in cat[i] and garch[1].get() == True)  or ("น้ำปลา" in cat[i] and garch[2].get() == True) or ("ซอสหอยนางรม" in cat[i] and garch[4].get() == True)  or ("ซีอิ๊วขาว" in cat[i] and garch[5].get() == True)  or ("ผงชูรส" in cat[i] and garch[6].get() == True)  or ("หอมใหญ่" in cat[i] and garch[7].get() == True)  or ("น้ำส้มสายชู" in cat[i] and garch[8].get() == True)  or ("เต้าหู้ยี้" in cat[i] and garch[9].get() == True)  or ("มะนาว" in cat[i] and garch2[0].get() == True)  or ("ซุปก้อน" in cat[i] and garch2[1].get() == True)  or ("หอมแดง" in cat[i] and garch2[2].get() == True)  or ("กระเทียมเจียว" in cat[i] and garch2[3].get() == True)  or ("ซีอิ๊วดำ" in cat[i] and garch2[4].get() == True)   or ("รากผักชี" in cat[i] and garch2[5].get() == True)  or ("น้ำมะนาว" in cat[i] and garch2[6].get() == True)  or ("น้ำตาลปิ๊บ" in cat[i] and garch2[7].get() == True)  or ("น้ำตาลทราย" in cat[i] and garch2[8].get() == True)  or ("วุ้นเส้น" in cat[i] and nmch[0].get() == True) or ("ไข่ไก่" in cat[i] and nmch[1].get() == True)  or ("ไข่เป็ด" in cat[i] and nmch[2].get() == True)  or ("เนยสด" in cat[i] and nmch[3].get() == True)  or ("ขนมจีน" in cat[i] and nmch[4].get() == True)  or ("มาม่า" in cat[i] and nmch[5].get() == True)  or ("เต้าหู้ไข่" in cat[i] and nmch[6].get() == True) or ("เกล็ดขนมปัง" in cat[i] and nmch[7].get() == True)   or ("แป้งข้าวโพด" in cat[i] and nmch[8].get() == True)  or ("แป้งสาลี" in cat[i] and nmch[9].get() == True)   :
                        Label(win3,text = cat[i],fg = "black",anchor = "w").pack(fill = BOTH)
                    else :
                        Label(win3,text = cat[i],fg = "red",anchor = "w").pack(fill = BOTH)
                for i in dog :
                    Label(win3,text = i,anchor = "w").pack(fill = BOTH)
            
            displaymethod(name)
        
    
        Label(winmenu,text = " ").pack()
        Label(winmenu,text = " ").pack()
        Button(winmenu,text = "Detail",command = detail,height = 2,width = 10).pack()

    def tab() :
        global rww
        global cll
        cll = cll + 1
        if cll == 3 :
            rww = rww + 1
            cll = 1

    
     
    if meatch[10].get() == True and nmch[6].get() == True and nmch[1].get() == True   :
        scb("แกงจืดไข่น้ำเต้าหู้ไข่หมูสับ",rww,cll)
        tab()
    

          
    if meatch[10].get() == True and vegch2[9].get() == True  :
        scb("ต้มยำน้ำใสหมูสับ",rww,cll)
        tab()
    

          
    if meatch[7].get() == True and meatch[6].get() == True  :
        scb("ต้มยำไก่",rww,cll)
        tab()
    

    
    if seach[0].get() == True and pepch[2].get() == True   :
        scb("ต้มยำกุ้งน้ำข้น",rww,cll)
        tab()
    


    if seach[1].get() == True and pepch[2].get() == True   :
        scb("ต้มยำปลาหมึกน้ำข้น",rww,cll)
        tab()
    

    
    if seach[0].get() == True and  seach[1].get() == True and pepch[2].get() == True :
        scb("ต้มยำรวมมิตรทะเล",rww,cll)
        tab()
    

    
    if meatch[10].get() == True and nmch[6].get() == True   :
        scb("แกงจืดเต้าหู้หมูสับ",rww,cll)
        tab()
    

    
    if meatch[10].get() == True and vegch2[1].get() == True and nmch[6].get() == True :
        scb("แกงจืดเต้าหู้หมูสับผักกาดขาว",rww,cll)
        tab()
    

    
    if meatch[10].get() == True and nmch[6].get() == True   :
        scb("แกงจืดหมูสับเต้าหู้สาหร่าย",rww,cll)
        tab()
    

    
    if meatch[10].get() == True and nmch[0].get() == True   :
        scb("ยำวุ้นเส้นหมูสับ",rww,cll)
        tab()
    

    
    if nmch[0].get() == True and seach[0].get() == True :
        scb("ยำวุ้นเส้นกุ้ง",rww,cll)
        tab()
    

    
    if nmch[0].get() == True and meatch[10].get() == True   and meatch[3].get() == True and seach[4].get() == True :
        scb("ยำวุ้นเส้นรวมมิตร",rww,cll)
        tab()
    

    
    if meatch[3].get() == True and seach[0].get() == True    and meatch[4].get() == True   :
        scb("ยำรวมมิตร",rww,cll)
        tab()
    

    
    if nmch[5].get() == True and seach[0].get() == True     :
        scb("ยำมาม่ากุ้งสด",rww,cll)
        tab()
    

    
    if nmch[5].get() == True and seach[0].get() == True and seach[1].get() == True   :
        scb("ยำมาม่ารวมมิตร",rww,cll)
        tab()
    

    
    if nmch[5].get() == True and meatch[10].get() == True :
        scb("ยำมาม่าหมูสับ",rww,cll)
        tab()
    

    
    if nmch[1].get() == True and meatch[10].get() == True and vegch2[6].get() == True  :
        scb("ไข่ตุ๋นหมูสับเห็ดหอม",rww,cll)
        tab()
    

    
    if seach[5].get() == True and garch[5].get() == True and vegch2[6].get() == True :
        scb("ปลาทูนึ่งซีอิ๊ว",rww,cll)
        tab()
    

    
    if meatch[4].get() == True  :
        scb("ไส้กรอกทอด",rww,cll)
        tab()
    
    
    
    if seach[3].get() == True and nmch[1].get() == True and nmch[7].get() == True :
        scb("ปลาชุบเกล็ดขนมปังทอด",rww,cll)
        tab()
    

    
    if nmch[1].get() == True and meatch[8].get() == True  :
        scb("ทอดมันปลากราย",rww,cll)
        tab()
    

    
    if seach[0].get() == True  and nmch[7].get() == True  :
        scb("ทอดมันกุ้ง",rww,cll)
        tab()
    
    
    
    if nmch[1].get() == True  and nmch[7].get() == True  :
        scb("นักเก็ตไก่",rww,cll)
        tab()
    

    
    if meatch[9].get() == True and seach[0].get() == True and nmch[1].get() == True :
        scb("หอยจ้อหมูกุ้ง",rww,cll)
        tab()
    

    
    if meatch[2].get() == True :
        scb("กะเพราหมู",rww,cll)
        tab()
    
    
    
    if meatch[6].get() == True  :
        scb("กะเพราไก่",rww,cll)
        tab()
    

    
    if seach[0].get() == True  :
        scb("กะเพรากุ้ง",rww,cll)
        tab()
    

    
    if seach[1].get() == True :
        scb("กะเพราปลาหมึก",rww,cll)
        tab()
    
    
    
    if  meatch[2].get() == True  :
        scb("ผัดพริกแกงหมู",rww,cll)
        tab()
    

    
    if meatch[6].get() == True :
        scb("ผัดพริกแกงไก่",rww,cll)
        tab()
    

    
    if seach[0].get() == True   :
        scb("ผัดพริกแกงกุ้ง",rww,cll)
        tab()
    
    
    
    if seach[1].get() == True   :
        scb("ผัดพริกแกงปลาหมึก",rww,cll)
        tab()
    

    
    if meatch[2].get() == True and pepch[2].get() == True :
        scb("ผัดพริกเผาหมู",rww,cll)
        tab()
    

    
    if meatch[6].get() == True and pepch[2].get() == True :
        scb("ผัดพริกเผาไก่",rww,cll)
        tab()
    

    
    if seach[0].get() == True  and pepch[2].get() == True :
        scb("ผัดพริกเผากุ้ง",rww,cll)
        tab()
    

    
    if meatch[2].get() == True  and vegch2[6].get() == True  :
        scb("ผัดผักรวมหมู",rww,cll)
        tab()  
    

    
    if meatch[6].get() == True  and vegch[9].get() == True :
        scb("ผัดผักรวมไก่",rww,cll)
        tab()
    

    
    if seach[0].get() == True and vegch[9].get() == True  :
        scb("ผัดผักรวมกุ้ง",rww,cll)
        tab()
    

    
    if vegch2[0].get() == True  :
        scb("ผัดผักบุ้งไฟแดง",rww,cll)
        tab()
    

    
    if vegch[10].get() == True    :
        scb("ผัดคะน้าหมูกรอบ",rww,cll)
        tab()
    

    	
    if meatch[2].get() == True and nmch[8].get() == True     :
        scb("ผัดเปรี้ยวหวานหมู",rww,cll)
        tab()
    

    
    if meatch[10].get() == True   :
        scb("ผัดเต้าหู้หมูสับ",rww,cll)
        tab()
    

    
    if seach[1].get() == True and seach[0].get() == True  and seach[3].get() == True  :
        scb("ผัดฉ่าทะเล",rww,cll)
        tab()
    

   
    if nmch[1].get() == True   :
        scb("ข้าวไข่เจียว",rww,cll)
        tab()
    

    
    if nmch[1].get() == True and meatch[1].get() == True  :
        scb("ข้าวไข่เจียวแหนม",rww,cll)
        tab()
    

    
    if meatch[10].get() == True and nmch[1].get() == True  :
        scb("ข้าวไข่เจียวหมูสับ",rww,cll)
        tab()
    

    
    if meatch[2].get() == True and nmch[1].get() == True   :
        scb("ข้าวผัดหมู",rww,cll)
        tab()
    

    
    if meatch[6].get() == True and nmch[1].get() == True  :
        scb("ข้าวผัดไก่",rww,cll)
        tab()
    

    
    if meatch[4].get() == True and nmch[1].get() == True   :
        scb("ข้าวผัดไส้กรอก",rww,cll)
        tab()
    

   
    if nmch[1].get() == True  :
        scb("ข้าวผัดแฮม",rww,cll)
        tab()
    

    
    if meatch[0].get() == True and nmch[1].get() == True   :
        scb("ข้าวผัดกุนเชียง",rww,cll)
        tab()
    

   
    if seach[0].get() == True and nmch[1].get() == True   :
        scb("ข้าวผัดกุ้ง",rww,cll)
        tab()
    

    
    if seach[1].get() == True and nmch[1].get() == True   :
        scb("ข้าวผัดปลาหมึก",rww,cll)
        tab()
    

    
    if meatch[1].get() == True and nmch[1].get() == True  :
        scb("ข้าวผัดแหนม",rww,cll)
        tab()
    

    
    if garch[1].get() == True and meatch[2].get() == True :
        scb("ข้าวหมูทอดกระเทียม",rww,cll)
        tab()
    

    
    if garch[1].get() == True and meatch[6].get() == True :
        scb("ข้าวไก่ทอดกระเทียม",rww,cll)
        tab()
    

   
    if seach[0].get() == True and garch[1].get() == True  :
        scb("ข้าวกุ้งทอดกระเทียม",rww,cll)
        tab()
    

   
    if seach[1].get() == True and garch[1].get() == True  :
        scb("ข้าวปลาหมึกทอดกระเทียม",rww,cll)
        tab()
    

    
    if meatch[2].get() == True and  vegch2[12].get() == True  :
        scb("ข้าวหมูผัดพริกหยวก",rww,cll)
        tab()
    

    
    if meatch[6].get() == True and vegch2[12].get() == True  :
        scb("ข้าวไก่ผัดพริกหยวก",rww,cll)
        tab()
    

    
    if seach[0].get() == True and vegch2[12].get() == True :
        scb("ข้าวกุ้งผัดพริกหยวก",rww,cll)
        tab()
    
    
    
    if seach[1].get() == True and vegch2[12].get() == True  :
        scb("ข้าวปลาหมึกผัดพริกหยวก",rww,cll)
        tab()
    
    



Button(root,text = "Search",command = search,height = 2,width = 20).grid(row =  1 ,column = 0)


#RESET
def clear() :
    for i in range(len(pep)+len(veg)+len(veg2)+len(meat)+len(gar)+len(gar2)+len(nm)+len(sea)-1):
        cb[i].deselect()

Button(root,text = "Reset",command = clear,height = 2,width = 20).grid(row =  1 ,column = 1)


root.mainloop()