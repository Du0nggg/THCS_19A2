import sys
import os

thu_vien_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'thu_vien_chung'))
sys.path.append("../thu_vien_chung")

import thu_vien_chung

print(thu_vien_chung.xu_ly_so(5))




