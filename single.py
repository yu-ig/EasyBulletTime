
import ffmpeg
import glob2
import os
import cv2
import copy
from PIL import Image, ImageFilter, ImageDraw


list_serialNum = [
"Canon EOS Kiss X8i (211032004233)",
"Canon EOS Kiss X8i (211032004234)",
"Canon EOS Kiss X8i (211032004209)",
"Canon EOS Kiss X8i (211032004210)",
"Canon EOS Kiss X8i (211032004212)",
"Canon EOS Kiss X8i (211032004211)",
"Canon EOS Kiss X8i (211032004213)",
"Canon EOS Kiss X8i (211032004214)",
"Canon EOS Kiss X8i (211032004230)",
"Canon EOS Kiss X8i (211032004229)",
"Canon EOS Kiss X8i (211032004228)",
"Canon EOS Kiss X8i (211032004227)",
"Canon EOS Kiss X8i (211032004238)",
"Canon EOS Kiss X8i (211032004237)",
"Canon EOS Kiss X8i (211032004235)",
"Canon EOS Kiss X8i (211032004236)",
"Canon EOS Kiss X8i (211032004166)",
"Canon EOS Kiss X8i (211032004162)",
"Canon EOS Kiss X8i (211032004164)",
"Canon EOS Kiss X8i (211032004165)",
"Canon EOS Kiss X8i (211032004232)",
"Canon EOS Kiss X8i (211032004231)",
"Canon EOS Kiss X8i (211032004161)"
]

# Setting Path
dir = '/Users/yu_mbp/Desktop/05/'
dirMov = '/Users/yu_mbp/Desktop/'


"""
カメラからデータをダウンロード
"""
def getImageList():
    fList = glob2.glob(dir + '*.jpg')
    num = len(list_serialNum)
    list_cam = []
    for i in range(23):
        l = []
        list_cam.append(l)

    for i in range(num):
        # dir = '/Users/Yu/Pictures/digiCamControl/Session1\\'
        file_name = dir + str(list_serialNum[i])

        # print(file_name)
        n = len(fList)
        for j in range(n):
            # print("LIST : "+f)
            if fList[j].find(list_serialNum[i]) > -1:
                # os.remove(dir + str("{0:02d}".format(j))+".jpg")
                # f = os.rename(fList[i], dir + str("{0:02d}".format(j))+".jpg")
                list_cam[i].append(fList[j])
                # print("RENAME : "+dir + str("{0:04d}".format(j))+".jpg")
        print(str(i) +' : ' + str(list_cam[i]))

    return list_cam


"""
初期化
フォルダ内のデータを削除
"""
def deleteAllImages():
    l = glob2.glob(dir+'*')
    for i in l:
        os.remove(i)


def rename(camList):
    sortedList = []
    count = 0
    l1 = camList[1]
    print("camList[0] : "+str(len(l1)))

    n = len(l1)
    for i in range(n):
        for imgList in camList:
            imgList.sort()

            print("i "+str(i))
            tmp = imgList[i]
            sortedList.append(tmp)
            # f = os.rename(camList[i], dir+str("{0:04d}".format(count))+'.jpg')
            # sortedList.append(f)
            # print("RENAME : "+dir+str("{0:04d}".format(count))+'.jpg')
            # count+=1


        # for imgList in camList:
        #     imgList.sort(reverse=True)
        #     print(str(imgList[i]))
        #     sortedList.append(imgList[i])
        #     # count+=1

    print(str(sortedList))


    return sortedList


def compositeImage(src_image, overlay_image):
    tmp = Image.new("RGBA", (1080, 1080), (0, 0, 0))

    # 入力する動画と出力パスを指定。
    target = "target/test_input.mp4"
    result = "result/test_output.m4v"  # .m4vにしないとエラーが出る

    # 動画の読み込みと動画情報の取得
    movie = cv2.VideoCapture(target)
    fps = movie.get(cv2.CAP_PROP_FPS)
    height = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = movie.get(cv2.CAP_PROP_FRAME_WIDTH)

    # 形式はMP4Vを指定
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

    # 出力先のファイルを開く
    out = cv2.VideoWriter(result, int(fourcc), fps, (int(width), int(height)))

    # オーバーレイ画像の読み込み
    ol_imgae_path = "target/warai_otoko.png"
    ol_image = cv2.imread(ol_imgae_path, cv2.IMREAD_UNCHANGED)


    # 用意したキャンパスに上書き
    # tmp.paste(overlay_image_PIL, (0, 0), overlay_image_PIL)

    # オリジナルとキャンパスを合成して保存
    # result = Image.alpha_composite(src_image_PIL, tmp)

    # COLOR_RGBA2BGRA から COLOR_RGBA2BGRに変更。アルファチャンネルを含んでいるとうまく動画に出力されない。
    # return cv2.cvtColor(np.asarray(result), cv2.COLOR_RGBA2BGR)




def encodeToMp4():
    pass

"""
DropboxにアップロードしURLを返す？
"""
def uploadToDropbox(url):
    pass


"""
Tornade server にリダイレクト用のページを作成。
ページを開くとダウンロード。
ダウンロードされない場合ボタンを作成。
"""
def createQR():
    pass

"""
"""
def showQR():
    pass

"""
別フォルダを作成しイメージをバックアップする
"""
def backup():
    pass






def main():

    # deleteAllImages()
    print("##### "+str(getImageList()))
    l = getImageList()
    m = rename(l)
    print(str(m))
    # l_reverse = copy.deepcopy(l)
    # l_reverse.sort(reverse=True)
    # l.append(l_reverse)



    # seqList = glob2.glob('/Users/Yu/Pictures/digiCamControl/Session1/*.jpg')
    fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
    video = cv2.VideoWriter(dirMov+'video.mp4', fourcc, 10.0, (1280, 960))

    for i in m:
        img = cv2.imread(i)
        img = cv2.resize(img, (1280, 960))
        video.write(img)
        # os.remove(i)
        print("REMOVE :" + str(i))

    video.release()
    print("Video encoded")




if __name__ == '__main__':
    main()