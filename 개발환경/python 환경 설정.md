# Python 개발 환경

## 1. vscode
1. anaconda 설치
2. vsCode 설치
3. VS Code Python extension 설치  
https://marketplace.visualstudio.com/items?itemName=ms-python.python
4. .py 파일 만들기
5. 하단의 인터프린터를 conda로 설정  
CTRL + SHIFT + P -> Python: Select Interpreter
5. run 후 환경 고르기

## 2. pyCharm
1. anaconda 설치
2. pyCharm 설치
3. 인터프린터를 anaconda로 설정

# 유용한 모듈
## 1. black
- 설치  
pip install black
- ERROR : ImportError: cannot import the name '_ast3' from 'typed_ast  
해결책 : pip install --force-reinstall --upgrade typed-ast black

