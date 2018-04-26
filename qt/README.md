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



https://stackoverflow.com/questions/45100018/increase-height-of-qpushbutton-in-pyqt