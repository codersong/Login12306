
import cv2 as cv
import numpy as np
import os
import binascii
from PIL import Image
import pytesseract
temp_path = r'F:\python\StockAnalyzer\test\test.avi'
#img_path = r'F:\12306'
data_path = r'F:\python\data'
file_path = r'F:\python\StockAnalyzer\test'
img_path = file_path


def split_img(file, x, y):
    '''
    把12306图片切分，获取x,y处图片，以及图片title
    :param file:
    :param x:
    :param y:
    :return:
    '''
    try:
        img = cv.imread(file)
        img_title = img[:30, 120:270, :]
        print(img_title.shape)
        left = 5 + (5+68)*x
        top = 36 + 5 + (5+68)*y
        right = left + 68
        bottom = top + 68
        return img_title, img[top:bottom, left:right, :]
    except Exception as e:
        print(e)
        return -1

def makeFile(path,file_name):
    '''
    根据路径path创建文件夹，根据file_name查看是否存在文件，否创建新文件
    :param path:
    :param file_name:
    :return: 返回0创建成功，-1创建失败
    '''
    if not os.path.exists(path):
        os.mkdirs(path)
    if file_name in os.listdir(path):
        print('文件名已经存在')
        return 0
    else:
        try:
            f = open(path + '\\' + file_name, 'w')
            f.close()
            print('文件创建成功')
            print(path + '\\' + file_name)
            return 0
        except Exception as e:
            print(repr(e))
            print('文件创建失败')
            return -1


def write2dat(source_list, fpath, fname):

    """
    将数据列表，转为二进制写入dat文件
    :param source_list: 将要写入的一维数据列表（类型整型）
    :param fpath: 写入的文件路径
    :param fname: 写入的文件名称
    :return: -1，写入失败，0写入成功
    文件格式：@开头 \n  元素序列号 \n 像素值
    """

    if makeFile(fpath, fname) == -1:
        print('写入失败，要写入的文件创建失败')
        return -1
    file_name = fpath + '\\' + fname
    with open(file_name, 'a') as f:
        f.write('@')
        f.write(' ')
        try:
            for m, j in enumerate(source_list):
                #f.write(hex(m)[2:].zfill(4))
                #f.write(hex(m))
                #f.write(' ')
                f.write(hex(j)[2:].zfill(4))
                #f.write(hex(j))
                f.write(' ')
            print('写入成功')
            f.write('\n')
            return 0
        except:
            print('写入二进制文件失败')
            return -1


def cutterTitle_write2dat(img_path,data_path, dName):
    for file in os.listdir(img_path):
        if file.find('.png') != -1:
            file_path = img_path+ '\\'+file
            title, img_x_y = split_img(file_path, 3, 1)
            #cv.imshow('title', title)
            #cv.waitKey(0)
            #cv.imshow('img', img_x_y)
            #print(title[:, :, 0])
            title_b = title[:, :, 0].reshape(-1)
            #print(title_b)
            title_g = title[:, :, 1].reshape(-1)
            title_r = title[:, :, 2].reshape(-1)
            merge_r_g_b = np.concatenate((title_b, title_g, title_r))
            #print(merge_r_g_b.shape)
            write2dat(merge_r_g_b, data_path, dName)


def cutterImg_write2dat(img_path, data_path, fname):

    '''
    分割12306图片并存入fname.dat
    :param img_path:
    :param fname:
    :return: 成功返回0
    '''

    for file in os.listdir(img_path):
        if file.find('.png') != -1:
            file_path = img_path + '\\' + file
            for i in range(2):
                for j in range(4):
                    title, img_x_y = split_img(file_path, j, i)  #获取12306验证码x,y处的图片
                    #print(img_x_y[:, :, 0])
                    img_x_y_b = img_x_y[:, :, 0].reshape(-1)
                    #print(img_x_y_b)
                    #print(img_x_y_b.reshape((68, 68)))
                    img_x_y_g = img_x_y[:, :, 1].reshape(-1)
                    img_x_y_r = img_x_y[:, :, 2].reshape(-1)
                    merge_img_r_g_b = np.concatenate((img_x_y_b, img_x_y_g, img_x_y_r))
                    write2dat(merge_img_r_g_b, data_path, fname)
                    #print(type(img_x_y[:, :, 0][0][0]))
                    # cv.imshow('img0', img_x_y)
                    # img_b = np.array(merge_img_r_g_b[0:68 * 68]).reshape((68, 68))
                    # # print(img_b)
                    # img_g = np.array(merge_img_r_g_b[68 * 68:2 * 68 * 68]).reshape((68, 68))
                    # img_r = np.array(merge_img_r_g_b[2 * 68 * 68:]).reshape((68, 68))
                    # img = np.zeros((68, 68, 3), dtype=np.uint8)
                    # img[:, :, 0] = img_b
                    # img[:, :, 1] = img_g
                    # img[:, :, 2] = img_r
                    # print('*********************************************')
                    # print(type(img[:, :, 0][0][0]))
                    # cv.imshow('img', img)
                    # cv.waitKey(0)
    #cv.destroyAllWindows()
    return 0

def decodeImg(data_img_line):
    """
    解析二进制文件存储的图片，解析后并返回图片列表
    :param data_img_line: dat文件每行存储一张图片，图片以'@'开头，图片大小68,68
    :return:
    """

    line = data_img_line
    pix = line.split(' ')[1:-1]
    #print(pix)
    pix10 = [int(i.upper(), 16) for i in pix]
    #print(pix10)
    #print(len(pix10))
    try:
        img_b = np.array(pix10[0:68*68]).reshape((68, 68))
        #print(img_b)
        img_g = np.array(pix10[68*68:2*68*68]).reshape((68, 68))
        img_r = np.array(pix10[2*68*68:]).reshape((68, 68))
        img = np.zeros((68, 68, 3), dtype=np.uint8)
        img[:, :, 0] = img_b
        img[:, :, 1] = img_g
        img[:, :, 2] = img_r
        return img
    except Exception as e:
        print(e)
        return None


def decodeTitleImg(title_img_line):
    """
    解析二进制存储的验证码的标题，并返回图片

    :param title_img_line:
    :return:
    """
    line = title_img_line
    pix = line.split(' ')[1:-1]
    #print(pix)
    pix10 = [int(i.upper(), 16) for i in pix]
    print(pix10)
    print(len(pix10))
    try:
        img_b = np.array(pix10[0:30*150]).reshape((30, 150))
        #print(img_b)
        img_g = np.array(pix10[30*150:2*30*150]).reshape((30, 150))
        img_r = np.array(pix10[2*30*150:]).reshape((30, 150))
        img = np.zeros((30, 150, 3), dtype=np.uint8)
        img[:, :, 0] = img_b
        img[:, :, 1] = img_g
        img[:, :, 2] = img_r
        return img
    except Exception as e:
        print(e)
        return None

#np.set_printoptions(threshold=np.inf)
#cutterImg_write2dat(file_path, data_path,  '12306img' + '.dat')


def test(fname):
    """
    测试相关功能
    :param fname:
    :return:
    """
    with open(fname) as f:
        print('打开文件成功')
        for line in f.readlines():
            #print('******')
            img = decodeTitleImg(line)
            cv.imshow('img', img)
            cv.waitKey(0)
            #cv.imwrite('F:\\python\\data\\title.png', img)
            title_text = pytesseract.image_to_string(Image.open('F:\\python\\data\\title.png'), lang='chi_sim')
            print('********')
            print(title_text)
            print(type(title_text))

    cv.destroyAllWindows()

if __name__ == '__main__':
    print('**************')
    #cutterImg_write2dat(img_path, data_path,  '12306img' + '.dat')
    #cutterTitle_write2dat(img_path,data_path,'12306titleImg' + '.dat')
    fname = data_path + '\\' + '12306img.dat'
    title_fname = data_path + '\\' + '12306titleImg.dat'
    print(fname)
    #test(fname)
    test(title_fname)













