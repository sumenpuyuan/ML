import os
import csv

path = "newimage"
__author__ = "xuejie"
attrs = dict()
temp = []
import xml.dom
import xml.dom.minidom

from PIL import Image

filelist = os.listdir(path)
count = 0
i = 0
_INDENT = ' ' * 4
_NEW_LINE = '\n'
_FOLDER_NODE = 'trafic'
_ROOT_NODE = 'annotation'
_DATABASE_NAME = 'INRIA'
_ANNOTATION = 'PASCAL VOC2007'
_AUTHOR = 'Xuejie'

_SEGMENTED = '0'
_DIFFICULT = '0'
_TRUNCATED = '0'
_POSE = 'Unspecified'

_IMAGE_PATH = 'JPEGImages'
_ANNOTATION_SAVE_PATH = 'Annotations'

_IMAGE_CHANNEL = 3


# ��װ�����ڵ�Ĺ���
def createElementNode(doc, tag, attr):
    # ����һ��Ԫ�ؽڵ�
    element_node = doc.createElement(tag)

    # ����һ���ı��ڵ�
    text_node = doc.createTextNode(attr)

    # ���ı��ڵ���ΪԪ�ؽڵ���ӽڵ�
    element_node.appendChild(text_node)

    return element_node


# ��װ���һ���ӽڵ�Ĺ���
def createChildNode(doc, tag, attr, parent_node):
    child_node = createElementNode(doc, tag, attr)
    parent_node.appendChild(child_node)


# object�ڵ�Ƚ�����
def createObjectNode(doc, attrs):
    object_node = doc.createElement('object')
    createChildNode(doc, 'name', attrs['classification'], object_node)
    createChildNode(doc, 'pose', _POSE, object_node)
    createChildNode(doc, 'truncated', _TRUNCATED, object_node)
    createChildNode(doc, 'difficult', _DIFFICULT, object_node)

    bndbox_node = doc.createElement('bndbox')
    createChildNode(doc, 'xmin', attrs['xmin'], bndbox_node)
    createChildNode(doc, 'ymin', attrs['ymin'], bndbox_node)
    createChildNode(doc, 'xmax', attrs['xmax'], bndbox_node)
    createChildNode(doc, 'ymax', attrs['ymax'], bndbox_node)
    object_node.appendChild(bndbox_node)

    return object_node


# ��documentElementд��XML�ļ���
def writeXMLFile(doc, filename):
    tmpfile = open('tmp.xml', 'w')
    doc.writexml(tmpfile, addindent=' ' * 4, newl='\n', encoding='utf-8')
    tmpfile.close()

    # ɾ����һ��Ĭ����ӵı��
    fin = open('tmp.xml')
    fout = open(filename, 'w')
    lines = fin.readlines()

    for line in lines[1:]:
        if line.split():
            fout.writelines(line)

    # new_lines = ''.join(lines[1:])
    # fout.write(new_lines)
    fin.close()
    fout.close()


# ����XML�ĵ���д��ڵ���Ϣ
def createXMLFile(attrs, width, height, filename):
    # �����ĵ�����, �ĵ��������ڴ������ֽڵ�
    my_dom = xml.dom.getDOMImplementation()
    doc = my_dom.createDocument(None, _ROOT_NODE, None)

    # ��ø��ڵ�
    root_node = doc.documentElement

    # folder�ڵ�
    createChildNode(doc, 'folder', _FOLDER_NODE, root_node)

    # filename�ڵ�
    createChildNode(doc, 'filename', attrs['name'], root_node)
    # createChildNode(doc, 'filename', _FOLDER_NODE, root_node)
    # source�ڵ�
    source_node = doc.createElement('source')
    # source���ӽڵ�
    createChildNode(doc, 'database', _DATABASE_NAME, source_node)
    createChildNode(doc, 'annotation', _ANNOTATION, source_node)
    createChildNode(doc, 'image', 'flickr', source_node)
    createChildNode(doc, 'flickrid', 'NULL', source_node)
    root_node.appendChild(source_node)

    # owner�ڵ�
    owner_node = doc.createElement('owner')
    # owner���ӽڵ�
    createChildNode(doc, 'flickrid', 'NULL', owner_node)
    createChildNode(doc, 'name', _AUTHOR, owner_node)
    root_node.appendChild(owner_node)

    # size�ڵ�
    size_node = doc.createElement('size')
    createChildNode(doc, 'width', str(width), size_node)
    createChildNode(doc, 'height', str(height), size_node)
    createChildNode(doc, 'depth', str(_IMAGE_CHANNEL), size_node)
    root_node.appendChild(size_node)

    # segmented�ڵ�
    createChildNode(doc, 'segmented', _SEGMENTED, root_node)

    # object�ڵ�
    object_node = createObjectNode(doc, attrs)
    root_node.appendChild(object_node)

    # д���ļ�
    writeXMLFile(doc, filename)


# for file in filelist:
#  print(file)
if __name__ == "__main__":
    for file in filelist:

        Olddir = os.path.join(path, file)
        if os.path.isdir(Olddir):
            continue
        filename = os.path.splitext(file)[0]
        # get the origin name (no type)
        print(filename)

        # then in sum.csv update the image name and get the information to generate xml

        # ok first read sum.csv
        c = open("sum.csv", "r")
        read = csv.reader(c)
        flag=0 #dai biao mei zhao dao
        for line in read:
            if (filename in line[0]):
                flag=1

                print(line[0], filename)
                # ok we get image informatin let's generate xml
                # we get 00001_00000.ppm;286;284;24;24;262;259;32 00001_00000 example
                # first acoording ; to split
                temp = line[0].split(';')
                attrs['name'] = str(count).zfill(6)+".jpg"
                attrs['classification'] = temp[7]
                attrs['xmin'] = temp[3]
                attrs['ymin'] = temp[4]
                attrs['xmax'] = temp[5]
                attrs['ymax'] = temp[6]
                # ����XML�ļ�
                width = temp[1]
                height = temp[2]
                createXMLFile(attrs, width, height, str(count).zfill(6) + ".xml")
        if flag == 0:
            print("not found",filename,"count is",count)
            ## 数据集里竟然有重名的 ……
            #input()
            #还应该删掉这张图片吧
            os.remove("newimage/"+filename+".jpg")
        else:
            filetype=os.path.splitext(file)[1]
            Newdir=os.path.join(path,str(count).zfill(6)+filetype)
            os.rename(Olddir,Newdir)
            count+=1
    print("count is",count)