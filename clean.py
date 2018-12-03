#Handling only one classification.
#Converting XML into yolo format.
#Author Matth3wology

from xml.dom import minidom
import math
import os

annotation_folder = "annotations"
image_folder = "weapon"

def convert_write(input_path,save_path):
    print(input_path)
    xmldoc = minidom.parse(input_path)

    #Image Width and Height from XML
    width = float(xmldoc.documentElement.getElementsByTagName('width')[0].firstChild.data)
    height = float(xmldoc.documentElement.getElementsByTagName('height')[0].firstChild.data)

    objects = xmldoc.documentElement.getElementsByTagName('object')

    w = open(save_path,'w')
    for obj in objects:
        #Class Info from XML
        class_id = 0
        class_name = obj.getElementsByTagName('name')[0].nodeName

        #Bounding Box from XML
        xmax = float(obj.getElementsByTagName('xmax')[0].firstChild.data)
        xmin = float(obj.getElementsByTagName('xmin')[0].firstChild.data)
        ymax = float(obj.getElementsByTagName('ymax')[0].firstChild.data)
        ymin = float(obj.getElementsByTagName('ymin')[0].firstChild.data)

        box_width = math.fabs(xmax-xmin)/width
        box_height = math.fabs(ymax-ymin)/height
        mid_point_x = (xmin+(box_width/2))/width
        mid_point_y = (ymin+(box_height/2))/height

        output_row = "{} {} {} {} {} \n".format(class_id,mid_point_x,mid_point_y,box_width,box_height)
        w.write(output_row)

    w.close()


files = os.listdir(annotation_folder)

for i in files:
    path = "{}/{}".format(annotation_folder,i)
    save_path = "{}/{}".format(image_folder,i.replace('.xml','.txt'))

    convert_write(path,save_path)
