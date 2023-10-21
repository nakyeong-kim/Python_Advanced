# [OSS project] PyPI 배포

# PyPI, build, package deploy


# gif_converter 패키지 import
from gif_converter import GifConverter as gfc

# class 생성
c = gfc('./project/images/*.png', './project/image_out/result.gif', (320, 240))

# 실행
c.convert_gif()


"""
패키지 배포 순서(PyPI)

1. http://pypi.org 회원가입
2. 프로젝트 구조 확인 (하기 3, 4번에 해당하는 내용들)
3. __init__.py 작성
4. 프로젝트 root 필수 파일 작성
   - README.md
   - setup.py
   - setup.cf (optional)
   - LICENSE
   - MANIFEST.in
5. pip install setuptools wheel 설치 후 빌드 업 → 설치판 생성
   [설치 1] python -m pip install --upgrade setuptools wheel
   [설치 2] python -m pip install --user --upgrade setuptools wheel
   [빌드] python setup.py sdist bdist_wheel
   - wheel : 파일을 압축해서 실행 파일(c, python 등) 형식으로 만들어주는 역할
   - setuptools : setup.py를 실행해서 압축해주는 역할
   - 즉, 배포판 형식으로 만들어주는 역할
6. PyPI 배포
   [설치] pip install twine
   [배포] python -m twine upload dist/*
7. 설치 확인

"""