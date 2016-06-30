from PIL import Image, ImageDraw, ImageFont

v=Image.open("blankMap.png")
w=ImageDraw.Draw(v)

pointsListPubs=[ [1082,374],\
             [738,226],\
             [729,240],\
             [667,364],\
             [594,488],\
             [594,515],\
             [611,611],\
             [572,593],\
             [547,761],\
             [745,892],\
             [812,895],\
             [831,924],\
             [794,958],\
             [738,1059],\
             [876,1021],\
             [840,995],\
             [825,998],\
             [851,967],\
             [1006,997],\
             [1055,960],\
             [995,921],\
             [1005,901],\
             [403,1340],\
             [587,1450],\
             [519,1635],\
             [479,1711]]

pointsListPoolHalls = [ [733,676],\
                        [182,515],\
                        [784,702],\
                        [776,621] ]

Font = ImageFont.truetype("arial.ttf", 40)

i=0
for point in pointsListPubs:
    i+=1
    x, y = point[0], point[1]
    w.polygon( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
                 (x-30,y-80), (x-30,y-20), (x-10,y-20) ), fill = "red")
    w.line( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
                 (x-30,y-80), (x-30,y-20), (x-10,y-20), (x,y) ), fill = "blue", width=4)
    w.text( (x-20,y-70), str(i), fill="white", font=Font)

for point in pointsListPoolHalls:
    i+=1
    x, y = point[0], point[1]
    w.polygon( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
                 (x-30,y-80), (x-30,y-20), (x-10,y-20) ), fill = "yellow")
    w.line( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
                 (x-30,y-80), (x-30,y-20), (x-10,y-20), (x,y) ), fill = "green", width=4)
    w.text( (x-20,y-70), str(i), fill="blue", font=Font)

##### KEYS #####
    
x, y = 830,1370
w.polygon( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
             (x-30,y-80), (x-30,y-20), (x-10,y-20) ), fill = "red")
w.line( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
          (x-30,y-80), (x-30,y-20), (x-10,y-20), (x,y) ), fill = "blue", width=4)

x, y = 830,1550
w.polygon( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
             (x-30,y-80), (x-30,y-20), (x-10,y-20) ), fill = "yellow")
w.line( ( (x,y), (x+10,y-20), (x+30,y-20), (x+30,y-80),\
          (x-30,y-80), (x-30,y-20), (x-10,y-20), (x,y) ), fill = "green", width=4)



v.save("marked_map_3.png")


    
    
