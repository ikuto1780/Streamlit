import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

#タイトル名
st.title('Streamlit 超入門')

#テキストを追加
st.write('一昔前の個人ブログ味を感じる出来栄え。')
st.write('st.writeで囲ったら文字として表紙出来るし、')
'シングルクオーテーションで囲ったものも文字として表示できる。'

#空を用意する
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'読み込み中... {i+1}%')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!!'


#マークダウン記法
"""
### 二段組にする
"""
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
    img = Image.open("KH1")
    st.image(img, caption = '画像は右カラムだけに表示するとかはできない？', use_column_width = True)

"""
## 動的なコンテンツ
"""
st.write('動的なコンテンツはサイドバー(左側)へ移動しました。')

#プルダウンの選択ボックス
option = st.sidebar.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11)),
)
st.sidebar.write('あなたの好きな数字は、', option, 'です。')

#テキスト入力欄
text = st.sidebar.text_input('あなたの趣味を教えてください。')
st.sidebar.write('あなたの趣味は', text, 'です。')

#スライダー
evaluation = st.sidebar.slider('このWebアプリの評価は？', 0, 100, 50)
st.sidebar.write('あなたの評価：', evaluation)

#########################################################################
########画像、動画の表示##################################################
#########################################################################

"""
## 画像の埋め込み
"""

#画像表示の有無を選択するチェックボックスを追加
if st.checkbox('各ゲームの画像/動画を表示する'):
    """
    ### ゲームプレイ画像
    """
    st.write('・KH Chain of Memories  より')

    #画像の読み込み
    img = Image.open("KH2.png")

    #画像を横幅に合わせて表示
    st.image(img, caption = 'カードになってしまった友人たち', use_column_width = True)

    img = Image.open(r"KH3.png")
    st.image(img, caption = '大切じゃないので拾いません', use_column_width = True)

    st.write('・友人からもらった写真')

    #画像の読み込み
    img = Image.open(r"IMG_3065.jpg")

    #画像を横幅に合わせて表示
    st.image(img, caption = 'ホラーゲームのような雰囲気', use_column_width = True)


#########################################################################
#######各種グラフの表示###################################################
#########################################################################
#マップ用の変数
map_df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)

#グラフ用の変数
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ['a', 'b', 'c']
)
"""
## グラフのプロット
### 折れ線グラフ
"""
st.line_chart(df)

"""
### 色塗ったver
"""
st.area_chart(df)

"""
### 棒グラフ
"""
st.bar_chart(df)

"""
### マップ
"""
st.map(map_df)

"""
## 表の表示
### ソートなどができる、動的な表
"""
#縦と横の長さを引数で指定できるのはdataframeだけ。writeではできない
#axis = 0 ...行、 1...列を強調
st.dataframe(df.style.highlight_max(axis = 0), width = 1000, height = 1000)

"""
### スタティック(静的)な表
"""
st.table(df.style.highlight_max(axis = 0))


"""
## コード形式での表示
このWebアプリを動かすためには、VSCode、Streamlit、Pythonが必要です。
Windows PowerShellを起動して、下記を実行してください。
```python
pip install streamlit
```
VSCode、Streamlitをインストールしたら、VSCode上でPython、Jupyterをインストールしてください。
これにて、準備完了です！
"""

"""
### Q&A
"""
expander1 = st.expander('1.YouTubeの動画は埋め込めないの？')
expander1.write('公式ドキュメント読む感じだと埋め込めそう。でもやり方は分からない。')
expander2 = st.expander('2.サイドバーに動的コンテンツの結果返す枠も移せないの？')
expander2.write('シングルクォーテーションで囲むんじゃなくて、st.write文使って書けば行ける。')
expander2 = st.expander('3.Q&A欄はfor文で回せないの？')
expander2.write('行けそうな気もする。やり方が分からん。。。')