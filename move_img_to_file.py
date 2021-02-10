import shutil
import os
 
def move_img_to_file(data_dir, dir_img):
    # move data img to train file            
    for data_file in os.listdir(data_dir):
        if data_file.endswith('.jpg'):
            os.path.join(data_dir, data_file)
            shutil.move(os.path.join(data_dir, data_file), os.path.join(dir_img, data_file))

        if data_file.endswith('.JPG'):
          new_data_file = data_file.split('.')[0]+ '.jpg'
          shutil.move(os.path.join(data_dir, data_file), os.path.join(dir_img, new_data_file))

train_data_dir = "data_fruit/train_zip/train"                
train_img = "data/train_images"
train_annotation = "data/train_annotations"

test_data_dir = "data_fruit/test_zip/test"                
test_img = "data/test_images"
test_annotation = "data/test_annotations"

## data image file
# train
if not os.path.exists(train_img):
    os.mkdir(train_img)
else:
    lsdir = os.listdir(train_img)
    for name in lsdir:
        if train_data_dir.endswith('.jpg') or name.endswith('.JPG'):
            os.remove(os.path.join(train_img, name))
# test
if not os.path.exists(test_img):
    os.mkdir(test_img)
else:
    lsdir = os.listdir(test_img)
    for name in lsdir:
        if test_data_dir.endswith('.jpg') or name.endswith('.JPG'):
            os.remove(os.path.join(test_img, name))
            
## xml file
# train
if not os.path.exists(train_annotation):
    os.mkdir(train_annotation)
else:
    lsdir = os.listdir(train_annotation)
    for name in lsdir:
        if name.endswith('.xml'):
            os.remove(os.path.join(train_annotation, name))      

# test
if not os.path.exists(test_annotation):
    os.mkdir(test_annotation)
else:
    lsdir = os.listdir(test_annotation)
    for name in lsdir:
        if name.endswith('.xml'):
            os.remove(os.path.join(test_annotation, name))  

move_img_to_file(train_data_dir, train_img)
move_img_to_file(test_data_dir, test_img)