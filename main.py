from urllib.request import urlretrieve
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def download(urlsFiles, savePath):
    # 显示下载进度
    def downloadProgress(blocknum, bs, size):
        progress = 100*blocknum*bs/size
        if 0 <= progress < 100:
            print('\r\t\t\t\t\t\t%d%%' % progress, end="")

    for urlFile in urlsFiles:
        # 新建存储图片文件夹存储图片
        os.makedirs('%s/%s' % (savePath, urlFile.split('.')[0]), exist_ok=True)
        # 读取txt文件
        with open('%s' % urlFile, 'r') as file:
            urls = file.readlines()
            # print(urls)
            # 计算链接地址条数
            num_urls = len(urls)
            # print(num_urls)
            print(urlFile, 'total urls:', num_urls)
            # 成功和失败下载总数
            failCount = 0
            succCount = 0
            # 遍历链接地址下载图片
            for i, url in enumerate(urls):
                # print(url.strip().split('/')[-1].split(".")[0])
                filesPath = 'data/%s/%s_%s.%s' % (urlFile.strip().split('.')[0], i+1, url.strip().split('/')[-1].split(".")[0][-3:], url.strip().split('.')[-1].split('?')[0])
                print('\rDownloading:\t%s\t[%s/%s]\t' % (urlFile, i, num_urls),end="      ")
                if not os.path.exists(filesPath):
                    try:
                        # 请求下载图片，并截取最后链接第一最后一节字段命名图片
                        # or download filename = url.strip().split('/')[-1]
                        urlretrieve(url.strip(), filesPath, downloadProgress)
                        print("\r\t\t\t\t\t\tok!", end="")
                        succCount += 1
                    except:
                        print("\r\t\t\t\t\t\tfail!", end="")
                        failCount += 1
                else:
                    print('\r\t\t\t\t\t\texist',end="")
                    continue
            print('\nsucceed:', succCount, 'failure:', failCount)


if __name__ == '__main__':
    # 此数组中定义所需下载url的文件名
    urlsFiles = ["hentai.txt"]
    # 在此定义写入的文件根路径
    savePath = './data'
    download(urlsFiles, savePath)
    os.system('poweroff')
