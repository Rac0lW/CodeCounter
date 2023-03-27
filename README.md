# CodeCounter
This program could count your the total number of your code in the selecter folder on your device.

计算在你所选择文件夹里面的代码行数

默认：.py, .html, .css, .txt

# Usage：

```
python CodeCounter.py 你选择的目标地址
```

# Change the file type

打开CodeCounter.py

```python
# change .* to the type that u want/ 直接改写下面文件后缀类型来指定你想要探测的文件类型

# the showcase already include four types with .py, .html, .css, .txt/ 已经写了四种文件类型

if file.endswith('.py') or file.endswith('.html') or file.endswith('.css') or file.endswith('txt'):
```

