# [OSS project] GIF Coverter

# 정적이미지(JPG, PNG) → GIF(애니메이션) 이미지 변환 패키지

import glob
from PIL import Image

class GifConverter:
  def __init__(self, path_in=None, path_out=None, resize=(320, 240)):
    """
    path_in : 원본 여러 이미지 경로(Ex: images/*.png)
    path_out : 결과 이미지 경로(Ex : output/filename.gif)
    resize : 리사이징 크기((320, 240))
    """
    self.path_in = path_in or './*.png'   # 에러를 줄이기 위한 예외 처리
    self.path_out = path_out or './output.gif'
    self.resize = resize

  def convert_gif(self):
    """
    GIF 이미지 변환 기능 수행
    """
    print(self.path_in, self.path_out, self.resize)   # 배포 시에는 logging 사용

    img, *images = \
        [Image.open(f).resize(self.resize, Image.Resampling.LANCZOS) for f in sorted(glob.glob(self.path_in))]

    try:
      img.save(
          fp=self.path_out,
          format='GIF',
          append_images=images,
          save_all=True,
          duration=500,
          loop=0
      )
    except IOError:
      print('Cannot convert!', img)


if __name__ == '__main__':  # 이 파일을 직접 실행할 때에만 실행됨. 다른 사람이 import했을 때에는 main이 아니므로 직접 호출할 때까지 실행되지 않음.
  c = GifConverter('./project/images/*.png', './project/image_out/result.gif', (320, 240))
  c.convert_gif()

  print(GifConverter.__init__.__doc__)
  print(GifConverter.convert_gif.__doc__)


# import glob
# from PIL import Image

# # 원본 이미지, 결과 이미 생성 경로
# path_in = './project/images/*.png'
# path_out = './project/image_out/result.gif'

# # 첫번째 이미지, 나머지 이미지 리스트 패킹 & resize
# img, *images = [Image.open(f).resize((320, 240), Image.ANTIALIAS) for f in sorted(glob.glob(path_in))]

# # 이미지 저장
# img.save(
#     fp=path_out,
#     format='GIF',
#     append_images=images,
#     save_all=True,
#     duration=500,
#     loop=0
# )