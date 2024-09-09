import os

# 創建 myapp 目錄
os.makedirs('myapp', exist_ok=True)

# 在 myapp 目錄中創建 __init__.py 文件
with open('myapp/__init__.py', 'w') as f:
    pass
