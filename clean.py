from xml.dom import minidom
import math
import os

#Annotation folder containing XML : convert to .txt and save in image folder.
annotation_folder = "annotations"
image_folder = "image"

#Convert XML to txt function
def convert(input_path):
    class_id = 0
    xmldoc = minidom.parse(input_path)

    width = float(xmldoc.documentElement.getElementsByTagName('width')[0].firstChild.data)
    height = float(xmldoc.documentElement.getElementsByTagName('height')[0].firstChild.data)

    xmax = float(xmldoc.documentElement.getElementsByTagName('xmax')[0].firstChild.data)
    xmin = float(xmldoc.documentElement.getElementsByTagName('xmin')[0].firstChild.data)
    ymax = float(xmldoc.documentElement.getElementsByTagName('ymax')[0].firstChild.data)
    ymin = float(xmldoc.documentElement.getElementsByTagName('ymin')[0].firstChild.data)


    box_width = math.fabs(xmax-xmin)/width
    box_height = math.fabs(ymax-ymin)/height
    mid_point_x = (xmin+(box_width/2))/width
    mid_point_y = (ymin+(box_height/2))/height

    return("{} {} {} {}".format(class_id,mid_point_x,mid_point_y,box_width,box_height))


def main():
    files = os.listdir(annotation_folder)

    print("Starting Conversion..")
    
    for i in files:
        path = "{}/{}".format(folder,i)
        save_path = "{}/{}".format(training_folder,i.replace('.xml','.txt'))
        f = open(save_path,'w')
        f.write(convert(path))
        f.close()
        
     print("Conversion finished.")

    
 if __name__ == "__main__":
    madin()
