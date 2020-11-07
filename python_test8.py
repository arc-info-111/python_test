# 8.1 パス
import os
PROJECT_DIR = "/Users/M.A/Desktop/python_test"
SETTINGS_FILE = "python_test8.py"


print(os.path.join(PROJECT_DIR, SETTINGS_FILE))
print(os.path.join(PROJECT_DIR, "settings_dir", SETTINGS_FILE))

