
# Annotation Converter
![](https://static.rectlabel.com/waysify_app/img/appicon48.png)

Convert [RectLabel](https://rectlabel.com) XML data to [YOLOV3](https://pjreddie.com/darknet/yolo) format.

### Structure
Folder structure should looke like this:
```
+data
  -clean.py
  +annotations
    - img1.xml
    - img2.xml
    - imgn.xml
  +images
    - img1.jpg
    - img2,jpg
    - img3.jpg
```

Conversion should have .txt files for each image:
```
+data
  -clean.py
  +annotations
    - img1.xml
    - img2.xml
    - imgn.xml
  +images
    - img1.jpg
    - img1.txt
    - img2,jpg
    - img2,txt
    - img3.jpg
    - img3.txt
```

### To Do:

Not much todo. I think I will want to automate the seperation of training and validation. Hmm..will work on repo later.
