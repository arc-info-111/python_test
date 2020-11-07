# 8.1 パス
import os
PROJECT_DIR = "/Users/M.A/Desktop/python_test"
SETTINGS_FILE = "python_test8.py"


print(os.path.join(PROJECT_DIR, SETTINGS_FILE))
print(os.path.join(PROJECT_DIR, "settings_dir", SETTINGS_FILE))

# 8.2 if文
value = 2

if value == 1:
    print("valueの値は1です")
elif value == 2:
    print("valueの値は2です")
elif value == 3:
    print("valueの値は3です")
else:
    print("該当する値はありません")
    
### 8.2.2 条件の組み合わせ
value_1 = "python"
value_2 = "izm"

if value_1 == "Python":
    pass
elif value_1 == "python" and value_2 == "izm":
    print("２番目の条件式がTrue")
elif value_1 == "IZM" or value_2 == "PYTHON":
    print("3番目の条件式がTrue")
    

