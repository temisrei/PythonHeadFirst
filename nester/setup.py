# 從 Python 的發行套件公用程式匯入 setup 函式
from distutils.core import setup

setup(
  name = 'nester',
  version = '1.0.0',
  py_modules = ['nester'],
  author = 'rei',
  author_email = 'temisrei@gmail.com',
  url='https://temisrei.github.io/',
  description = 'Exercise: printer of nested lists',
)
