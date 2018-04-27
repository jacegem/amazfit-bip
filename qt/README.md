## 참고

- https://gist.github.com/gioditalia/03c9fd5d793aeccbe065fea45d842431

```python
import webbrowser
webbrowser.open('http://stackoverflow.com')
```

https://stackoverflow.com/questions/49813237/create-a-portable-version-of-the-desktop-app-in-pyqt5

You can use cx_Freeze to create a desktop app from a python program.

There's a [guide to packaging a PyQt application](https://www.smallsurething.com/a-really-simple-guide-to-packaging-your-pyqt-application-with-cx_freeze/):

cxfreeze-quickstart # generates a creation script
On OSX, you have the option of building a .dmg or a .app, by executing one of these at the prompt:

python setup.py bdist_dmg
python setup.py bdist_mac
On Windows:

python setup.py bdist_msi
There's a comparison of deployment tools [here](http://docs.python-guide.org/en/latest/shipping/freezing/).



## 화면 디자인

### 컬럼 1

- 후원하기 (paypal)
- $1, $5, $10, $99

### 컬럼 2

- ttf 파일 선택
- marginTop, marginLeft 선택
- ft  파일 선택
- 시작 버튼

- 체크박스 / delete bmp files

### 상태 바

- 현재 진행중 (1/4) 변환 파일 명 / 패키징 /


## display markdown

```python
from IPython.display import display, Markdown, Latex
display(Markdown('*some markdown* $\phi$'))
# If you particularly want to display maths, this is more direct:
display(Latex('\phi'))
```


## 참고

- https://stackoverflow.com/questions/45100018/increase-height-of-qpushbutton-in-pyqt
- https://github.com/kenwaldek/pythonprogramming/blob/pythonprogramming/pyqt5_lesson_15.py




```python
pyinstaller --onefile font_creator.py
```
`

## How to include GUI images with PyInstaller.
https://www.reddit.com/r/learnpython/comments/4kjie3/how_to_include_gui_images_with_pyinstaller/

```
How to include GUI images with Pyinstaller? (self.learnpython)

submitted 1 년 전에 by diggity801

Hello,

I'm trying to convert a .py file to an .exe using Pyinstaller. I am able to do so but I cannot get the images to show up on the executable. How do I bundle an image with Pyinstaller and then refer to that image inside of the script?

Almost all of the help topics I found are talking about the icon file which I do not care about and doesn't seem to be imported the same way.

So far I have added the following line to the .spec file and no errors are generated when I package as an EXE:

a.datas += [('C:\Python34\Scripts\image.jpg','final')]

Although the jpg seemed to be bundled in the exe im not sure how I can refer to it from within the Python script.

Any help would be appreciated.

댓글 2추천하기보관하기숨기기신고하기
댓글 2개
정렬: 최고 인기

Want to add to the discussion?
Post a comment!


[–]diggity801[S] 2 점 1 년 전에
I figured it out myself, no thanks to any official documentation. This was way more difficult than it should have been.

Step 1: Add function at beginning of script to refer to image inside of Pyinstaller exe.

 def resource_path(relative_path):
     if hasattr(sys, '_MEIPASS'):
         return os.path.join(sys._MEIPASS, relative_path)
     return os.path.join(os.path.abspath("."), relative_path)
Step 2: Create and edit .spec file to point to the .jpg or whatever picture you want on a local drive.

a.datas += [ ('picture.jpg', '.\\picture.jpg', 'DATA')]'
Step 3: Use resource_path function to refer to picture inside script.

self.label.setPixmap(QtGui.QPixmap(resource_path("picture.jpg")))
Step 4: Build EXE using Pyinstaller and edited spec file.

pyinstaller.exe --specpath c:\program.spec
댓글 주소로 가기embed보관하기골드 주기

[–]DtotheJtotheH 2 점 1 년 전에
Thanks a ton for posting the solution. Helped me out a t
```


```python
It has worked, just a problem with cached icons. If you move the .exe to another folder the icon should change. Just to be sure though rebuild using :

pyinstaller --onefile --icon=myicon.ico --clean yourapp.py
The --clean command cleans the cache and your icon will appear correctly
```

```shell
$ pyinstaller --onefile --clean --windowed --icon=font.ico Amazfit_Bip_Font_Creator.py
$ pyinstaller --onefile --clean --windowed --icon=.\assets\font.ico --add-data ".\assets\font.png;.\assets\font.png" Amazfit_Bip_Font_Creator.py

add to spec file

a.datas += [('.\\assets\\font.png', '.\\assets\\font.png', 'DATA')]
```

