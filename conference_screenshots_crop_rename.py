import os


PATH_imgs = '/home/maria/Pictures/ccp_biosim_2024/02_07_9'
PATH_cropped = os.path.join(PATH_imgs, "crop")
os.makedirs(PATH_cropped, exist_ok=True)

# 1 -- rename
for f in os.listdir(PATH_imgs):
    if ' ' in f:
        new_f = f.replace("Screenshot from ", "").replace(' ', '_')
        os.system(f'mv "{PATH_imgs}/{f}" "{PATH_imgs}/{new_f}"')


# 2 -- crop
# x_offset = 249
x_offset = 0
y_offset = 107
# y_offset = 257
x_size = 1446 - x_offset
# x_size = 1281 - x_offset
# x_size = 1330 - x_offset
y_size = 920 - y_offset
# y_size = 836 - y_offset
for f in os.listdir(PATH_imgs):
    if f.endswith('png') or f.endswith('jpg'):
        cmd = f"convert -crop {x_size}x{y_size}+{x_offset}+{y_offset} {PATH_imgs}/{f} {PATH_cropped}/crop_{f}"
        os.system(cmd)
