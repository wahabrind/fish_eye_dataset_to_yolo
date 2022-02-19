 
import json
from posixpath import abspath
import cv2
from matplotlib.pyplot import annotate
import numpy as np
import math
import os



fol = 0
for root , dir , files in os.walk('HABBOF/'):
    # print(dir )
    for fname in files:
        src = abspath(os.path.join(root  , fname))
        if fname.endswith('.jpg'):
            fol+=1

            if fol%5==0:
                img  = cv2.imread(src)
                H , W , e = img.shape
                
                img = cv2.resize(img , (416,416))
                size = 416
                
                txt = open(f'{src[:-4]}.txt' , 'r')

                txt1 = open(f'habbof_output_1/{fol}.txt' , 'w')
                for line in txt:
                    label , cx , cy , w , h , d  = line.split(' ')
                    cx , cy , w , h , d = int(cx) , int(cy) , int(w) , int(h) , int(d)
                    d = math.radians(d)

                    x1 = int( cx + ( (w/2) * np.cos(d) )  - ( (h/2) * np.sin(d) ) )
                    y1 = int( cy + ( (w/2) * np.sin(d) )  + ( (h/2) * np.cos(d) ) )
                    
                    
                    x2 = int( cx - ( (w/2) * np.cos(d) )  - ( (h/2) * np.sin(d) ) )
                    y2 = int( cy - ( (w/2) * np.sin(d) )  + ( (h/2) * np.cos(d) ) )

                    x3 = int( cx - ( (w/2) * np.cos(d) )  + ( (h/2) * np.sin(d) ) )
                    y3 = int( cy - ( (w/2) * np.sin(d) )  - ( (h/2) * np.cos(d) ) )

                    x4 = int( cx + ( (w/2) * np.cos(d) )  + ( (h/2) * np.sin(d) ) )
                    y4 = int( cy + ( (w/2) * np.sin(d) )  - ( (h/2) * np.cos(d) ) )


                    xmin = min([x1,x2,x3,x4])
                    xmax = max([x1,x2,x3,x4])
                    ymin = min([y1,y2,y3,y4])
                    ymax = max([y1,y2,y3,y4])



                    width = xmax - xmin
                    height = ymax - ymin

                    cx = (( xmin + (width/2) ) * size / W) / size 
                    cy = (( ymin + (height/2) ) *  size / H) / size

                    width = ((width *size) /W) / size
                    height  = ((height *size)/H ) / size


                    # cx = ( xmin + (width/2) ) * W / size
                    # cy = ( ymin + (height/2) ) *  H / size

                    # width = (width *W) /size
                    # height  = (height *H) /size


                    txt1.write(f"{1} {cx} {cy} {width} {height} \n")
                
                cv2.imwrite(f'habbof_output_1/{fol}.jpg'  , img)
                txt1.close()
            # print(src)
            # break