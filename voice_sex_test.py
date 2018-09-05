# -*- encoding: utf-8 -*-
import requests
import os

__author__ = "Lone"

class VoiceSexTest():
    def __init__(self):
        self.url = "http://134.175.166.135:8080/slot/voice-sex/recognize.do?" \
                   "token=f27fdc05694b645686f55b691f015ef1&flow_id=982eee56c6cc" \
                   "9fda36c823e58692d974&user_id=6419796842174746636"
    
    def getRes(self, file):
        files = {
            "file": open(file, "rb")
        }
        r = requests.post(self.url, files=files)
        #print(r.status_code)
        res = r.json()
        return res

def getFileName(path):
    """读取目录下的所有文件及文件个数"""
    fileNum = 0
    fileList = []
    files = os.listdir(path)
    #print(files)
    for f in files:
        if(os.path.isfile(path+"/"+f)):
            fileList.append(f)
            fileNum += 1
    return fileNum, fileList

def runTest():
    test = VoiceSexTest()
    malePath = "/data/sound/male"
    femalePath = "/data/sound/female"
    maleVoiceCount, maleFiles = getFileName(malePath)
    femaleVoiceCount, femaleFiles = getFileName(femalePath)
    print("maleVoiceCount %d" % maleVoiceCount)
    print("femaleVoiceCount %d" % femaleVoiceCount)
    maleResCount, femaleResCount = 0, 0
    # print(count, files)
    for maleFile in maleFiles:
        """男声测试数据收集"""
        res = test.getRes(malePath + '/' + maleFile)
        # print(res)
        if res["data"] == "male":
            maleResCount += 1
        elif res["data"] == "female":
            print("男声识别错误")
        else:
            print(res["message"])

    for femaleFile in femaleFiles:
        """女声测试数据收集"""
        res = test.getRes(femalePath + '/' + femaleFile)
        # print(res)
        if res["data"] == "female":
            femaleResCount += 1
        elif res["data"] == "male":
            print("女声识别错误")
        else:
            print(res["message"])

    maleResult = maleResCount / maleVoiceCount
    femaleResult = femaleResCount / femaleVoiceCount

    print("Test result for male voice: %0.4f" % maleResult)
    print("Test result for female voice: %0.4f" % femaleResult)

if __name__ == "__main__":
    runTest()