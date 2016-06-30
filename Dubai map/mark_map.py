from PIL import Image, ImageDraw, ImageFont

v=Image.open("dxbMap.png")
w=ImageDraw.Draw(v)

pointsListPoolHalls_Malls=[ [858,297],\
                            [894,334],\
                            [833,353],\
                            [789,395],\
                            [782,459],\
                            [713,461],\
                            [672,503],\
                            [556,515],\
                            [542,554],\
                            [1027,722],\
                            [992,744],\
                            [1045,754],\
                            [1062,768],\
                            [170,1022],\
                            [188,1086],\
                            # end of pool halls/clubs
                            #start malls
                            [73,1175],\
                            [145,1075],\
                            [313,929],\
                            [767,454],\
                            [559,648] ]
                    
pointsListAlcohol= [ [667,782],\
                   [249,1014],\
                   [687,438],\
                   [520,687] ]

Font = ImageFont.truetype("arial.ttf", 40)

i=0

for point in pointsListPoolHalls_Malls:
    i+=1
    x, y = point[0], point[1]
    w.polygon( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
                 (x-30,y-80), (x-30,y-20), (x-10,y-20) ), fill = "green")
    w.line( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
                 (x-30,y-80), (x-30,y-20), (x-10,y-20), (x,y) ), fill = "black", width=4)
    w.text( (x-20,y-70), str(i), fill="white", font=Font)

for point in pointsListAlcohol:
    i+=1
    x, y = point[0], point[1]
    w.polygon( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
                 (x-30,y-80), (x-30,y-20), (x-10,y-20) ), fill = "red")
    w.line( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
                 (x-30,y-80), (x-30,y-20), (x-10,y-20), (x,y) ), fill = "blue", width=4)
    w.text( (x-20,y-70), str(i), fill="white", font=Font)

###### KEY #####

x=730
y=1300
w.polygon( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
             (x-30,y-80), (x-30,y-20), (x-10,y-20) ), fill = "green")
w.line( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
          (x-30,y-80), (x-30,y-20), (x-10,y-20), (x,y) ), fill = "black", width=4)

x=730
y=1450
w.polygon( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
             (x-30,y-80), (x-30,y-20), (x-10,y-20) ), fill = "red")
w.line( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
          (x-30,y-80), (x-30,y-20), (x-10,y-20), (x,y) ), fill = "blue", width=4)

v.save("dxbMap_marked.png")


    
    
