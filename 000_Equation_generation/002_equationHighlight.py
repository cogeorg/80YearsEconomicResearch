from PIL import Image, ImageColor, ImageDraw
import json
import pandas as pd
from os import listdir
from os.path import isfile, join

def highlight_area(img, region, outline_color, outline_width=1):
    """ draw colored border around specified rectangular regions of 
        image and return the result.
    """
    img = img.copy()  # Avoid changing original image.
    
    # draw a colored outline around the edge of the rectangular region of the equation.
    draw = ImageDraw.Draw(img)  # Create a drawing context.

    for i in range(len(region)):
        left, upper, right, lower = region[i]  # Get bounds.
        page_info = [(left, upper), (right, upper), (right, lower), (left, lower), (left, upper)]
        draw.line(page_info, fill=outline_color, width=outline_width)

    return img

def openJson(filename):
    # Opening JSON file
    f = open(filename)   
    # returns JSON object as a dictionary
    data = json.load(f)    
    # Closing file
    f.close()
    return data

if __name__ == '__main__':
    print("uncomment out line 34 in the script to show the outlined shots or look in the outlined folder")
    # path set up, the base path should have three folders in it
    base_path="/Users/sijiawu/Work/Thesis/Data/0_eq_training/" 
    json_path="0_json/"
    screenshot_path="0_screenshots/"
    outlined_path="1_outlined/"

    # reads in a folder containing the files and processes them
    fns = [f.split(".")[0] for f in listdir(base_path+json_path) if isfile(join(base_path+json_path, f))]
    # fns = ["1710534853501", "1710534834860", "1710534896177"] # uncomment to avoid processing a folder

    eq_data = {}
    for fn in fns:
        img = Image.open(base_path + screenshot_path + fn + '.png')
        page_info = openJson(base_path + json_path + fn + ".json")
        coords = page_info["positions"]

        # height of original window when a screenshot was taken
        windowWidth=page_info["innerWidth"]
        windowHeight=page_info["innerHeight"]

        # Ratios of image size to original window size
        width_ratio=img.width/windowWidth
        height_ratio=img.height/windowHeight
        eqCoords=[]
        for i in coords.keys():
                eqPos = coords[i]  
                # left top right bottom coordinates of blocks
                # must adjust the pixel position relative to height and width of image size          
                eq_region = int(eqPos["left"]*width_ratio), int(eqPos["top"]*height_ratio), int(eqPos["right"]*width_ratio), int(eqPos["bottom"]*height_ratio)
                if int(eqPos["top"]*height_ratio)>img.height:
                    # print("discard pos "+i) 
                    continue
                elif int(eqPos["bottom"]*height_ratio)<0:
                    # print("discard pos "+i)
                    continue
                eqCoords.append(eq_region) 
        
        img2 = highlight_area(img, eqCoords, outline_color=ImageColor.getrgb('red'), outline_width=2)
        img2.save(base_path+outlined_path+"outlined_"+fn+".png")
        # img2.show()  # Display the result.
        eq_data[fn]={"pos":tuple(eqCoords), "count":len(eqCoords)} # save the output

    names=["pos", "count"] # name the columns
    pd.DataFrame.from_dict(eq_data, orient='index').rename_axis('fileRef').reset_index().to_csv("eq_training.csv",index=False)

