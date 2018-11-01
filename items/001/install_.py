# 利用PyIstaller制作python的exe可执行文件
from PyInstaller.__main__ import run

if __name__ == "__main__":
	opts = ["test1.py", "-F"]
	run(opts)
