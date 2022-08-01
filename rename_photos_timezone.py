import os
import glob
import PIL.Image
import PIL.ExifTags
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from time import strptime
from dateutil import parser as dateparser

PATH_images = '/media/maria/Maxtor/photos/2020/Каменоломни под Старицей/canon-share/'
PATH_images = '/media/maria/Maxtor/photos/2020/Поход КБР/'
PATH_images = '/media/maria/Maxtor/photos/2020/ПВД Аргуновская волость/'
model_dict = {'X-A1': 'Fuji-X-A1',
              'Pixel 3': 'Pixel-3',
              'Mi MIX 2S': 'Mi-MIX-2S',
              'Canon PowerShot SX540 HS': 'Canon-PS-SX540-HS'
              }

#'2018-09-30 11.55.23.jpg'


def modify_dt(cur_dt):
    # tz = timezone('Iran')
    # cur_dt = tz.localize(cur_dt)
    # tz = timezone('Atlantic/Cape_Verde')
    # cur_dt = tz.localize(cur_dt)
    cur_dt = cur_dt - timedelta(hours=1, minutes=35)
    return cur_dt


def move_pixel_portrait_folders():
    ptr_folders = sorted([f for f in os.listdir(PATH_images) if f.startswith('IMG') and os.path.isdir(PATH_images + f)])
    for dir in ptr_folders:
        path_cur_dir = '{0}{1}/'.format(PATH_images, dir)
        for i_, fname in enumerate(os.listdir(path_cur_dir)):
            os.system('cp "{0}{1}" "{2}{3}_prtr_{4}.jpg"'.format(path_cur_dir, fname,
                                                        PATH_images,
                                                        dir, i_))


def print_or_run(cmd_, print_only=True):
    if print_only:
        print(cmd_)
    else:
        os.system(cmd_)


def do_renaming(skip_corrected=True, print_only=True):
    time_format = "%Y-%m-%d %H.%M.%S"
    img_names = sorted([f for f in os.listdir(PATH_images) if f.split('.')[-1] in ['jpg', 'JPG', 'jpeg']])
    do_renaming = True
    for img_name in img_names:
        if skip_corrected and 'Fuji' in img_name:
            continue
        img = PIL.Image.open('{0}{1}'.format(PATH_images, img_name))
        exif_data = img._getexif()
        exif = {
            PIL.ExifTags.TAGS[k]: v
            for k, v in img._getexif().items()
            if k in PIL.ExifTags.TAGS
        }
        date_time = exif['DateTime']
        year_month = date_time.split()[0].replace(':', '-')
        day_time = date_time.split()[1].replace(':', '.')
        model = exif['Model']
        if model not in model_dict.keys():
            print(model)

        model = model_dict[model]
        if 'Fuji' not in model:
            continue
        if 'Fuji' in model:
            cur_time_new = modify_dt(dateparser.parse('{0} {1}'.format(year_month, day_time).replace('.', ':')))

            new_name = '{0}.{1}.jpg'.format(cur_time_new.strftime(time_format), model)
            print(img_name)
            print(new_name)
            if do_renaming:
                print_or_run('mv "{0}{1}" "{0}{2}"'.format(PATH_images, img_name, new_name), print_only=print_only)
                print_or_run('mv "{0}{1}" "{0}{2}"'.format(PATH_images,
                                                        img_name.replace('.JPG', '.RAF'),
                                                        new_name.replace('.jpg', '.RAF')), print_only=print_only)
        elif 'Pixel' in model:
            cur_time_new = dateparser.parse('{0} {1}'.format(year_month, day_time).replace('.', ':'))
            if 'PANO' in img_name or '.vr.jpg' in img_name:
                new_name = '{0}.{1}.vr.jpg'.format(cur_time_new.strftime(time_format), model)
            elif 'prtr' in img_name:
                tail = img_name.split('.')[-2].split('prtr_')[-1]
                new_name = '{0}_prtr_{2}.{1}.jpg'.format(cur_time_new.strftime(time_format), model, tail)
            elif img_name.count('_') == 3:
                tail = img_name.split('.')[-2].split('_')[-1]
                new_name = '{0}_{2}.{1}.jpg'.format(cur_time_new.strftime(time_format), model, tail)
            elif img_name.count('_') > 3:
                print(img_name + '!!!!!')
                continue
            else:
                new_name = '{0}.{1}.jpg'.format(cur_time_new.strftime(time_format), model)
            print(img_name)
            print(new_name)
            if do_renaming:
                print_or_run('mv "{0}{1}" "{0}{2}"'.format(PATH_images, img_name, new_name), print_only=print_only)
        elif 'Mi' in model:
            cur_time_new = dateparser.parse('{0} {1}'.format(year_month, day_time).replace('.', ':'))
            new_name = '{0}.{1}.jpg'.format(cur_time_new.strftime(time_format), model)
            print(img_name)
            print(new_name)
            if do_renaming:
                print_or_run('mv "{0}{1}" "{0}{2}"'.format(PATH_images, img_name, new_name), print_only=print_only)
        elif 'Canon' in model:
            cur_time_new = dateparser.parse('{0} {1}'.format(year_month, day_time).replace('.', ':'))
            new_name = '{0}.{1}.jpg'.format(cur_time_new.strftime(time_format), model)
            print(img_name)
            print(new_name)
            if do_renaming:
                print_or_run('mv "{0}{1}" "{0}{2}"'.format(PATH_images, img_name, new_name), print_only=print_only)


def move_by_day():
    for i in range(1, 17):
        path_date = '{0}day_{1}/'.format(PATH_images,
                                         i)
        path_date_raw = '{0}day_{1}_raw/'.format(PATH_images,
                                         i)
        try:
            os.mkdir(path_date)
        except FileExistsError:
            pass
        try:
            os.mkdir(path_date_raw)
        except FileExistsError:
            pass
        for f in os.listdir(PATH_images):
            if 'VID' in f:
                continue
            if os.path.isdir(PATH_images + f):
                continue
            dt_up = int(f.split()[0].split('-')[-1])
            if dt_up == i:
                if f.endswith('RAF') or f.endswith('raf'):
                    os.system('mv "{0}{1}" "{2}"'.format(PATH_images, f,
                                                            path_date_raw, f))
                else:
                    os.system('mv "{0}{1}" "{2}"'.format(PATH_images, f,
                                                            path_date, f))




# move_pixel_portrait_folders()
do_renaming(print_only=False, skip_corrected=False)
# move_by_day()
