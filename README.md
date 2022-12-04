# PyOSCPokemon
ポケモンの能力をOCR解析で判定するプログラム

## 参考
- https://myafu-python.com/work/text-extraction/

## 内容
### 座標確認
`gui.py`

クリックした画像の座標をログに出力する。

- 判定したい画像ファイル名を `IMAGE_FILE_NAME` に指定する

### OCR検証
`app.py`

座標のテキスト解析

- 判定したい画像ファイル名を `IMAGE_FILE_NAME` に指定する
- 解析したい範囲を `RECT_RANGE` に指定する。
    - `x` 抽出したい部分の画像左上からのx座標
    - `y` 抽出したい部分の画像左上からのy座標
    - `w` 抽出したい部分の幅
    - `h` 抽出したい部分の高さ