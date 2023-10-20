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
2. 
"""