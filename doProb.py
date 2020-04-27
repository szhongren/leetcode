import argparse
import os

initKey = {
    'p': {
        'extension': 'py',
        'skeleton': """class Solution(object):
    def stub(self):
        pass

ans = Solution()
print(ans.stub())
"""
    },
    'g': {
        'extension': 'go',
        'skeleton': """package main

import "fmt"

func main() {
	fmt.Println("test")
}
"""
    }
}


def getFullFolder(probNum):
    return "{:03}".format(probNum)


def main():
    parser = argparse.ArgumentParser(description='start/continue a problem on leetcode')
    parser.add_argument('number', metavar='N', type=int, help='problem number I want to do', nargs=1)
    parser.add_argument('type', metavar='T', help='type of code I want to write', nargs=1, choices=['go', 'g', 'py', 'p'],)
    args = parser.parse_args()
    probNum = args.number[0]
    fileType = args.type[0][0]

    probFolder = os.path.join(os.getcwd(), getFullFolder(probNum))
    if not os.path.isdir(probFolder):
        os.mkdir(probFolder)

    filePath = os.path.join(probFolder, 'main.{}'.format(initKey[fileType]['extension']))
    if not os.path.isfile(probFolder):
        file = open(filePath, 'w+')
        file.write(initKey[fileType]['skeleton'])


if __name__ == "__main__":
    main()
