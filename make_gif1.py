import os
from PIL import Image
from IPython.display import Image as Img
from IPython.display import display


def generate_gif(path,save_name):
    img_list = sorted(os.listdir(path))[:800]  # 1496
    img_list = [path + '/' + x for x in img_list]
    images = [Image.open(x) for x in img_list]
    
    im = images[0]
    im.save(save_name, save_all=True, append_images=images[1:],loop=0xff, duration=50)
    # loop 반복 횟수
    # duration 프레임 전환 속도 (500 = 0.5초)
    return Img(url=save_name)


root = '/media/khw/Samsung_T5/0703/H36M4/experiments/eval_trainset_S8'
save_name = 'h36m.gif'
gif = generate_gif(root,save_name)

display(gif)