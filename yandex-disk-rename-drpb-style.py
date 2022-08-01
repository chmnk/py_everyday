import os


PATH_images = '/home/maria/yadisk/Фотокамера/2020/Зима в Москве/Тренировка в роще/'

img_files = [f for f in os.listdir(PATH_images) if f.endswith('.JPG')]

for f in img_files:
    old_name = f
    new_name = f[:13] + '.' + f[14:16] + '.' + f[17:]
    new_name = new_name.replace('.JPG', '.jpg')
    print(old_name, new_name)
    os.system('mv "{0}{1}" "{0}{2}"'.format(PATH_images,
                                            old_name,
                                            new_name))