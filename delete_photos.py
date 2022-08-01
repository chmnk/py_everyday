import os

to_delete = [2981, 2989, 2991, 2992, 2998, 3011, 3042, 3059, 3064, 3076, 3087, 3089, 3091, 3094, 3106, 3107, 3110,
             3194, 3196, ]
PATH_files = '/media/maria/Maxtor/photos/2019/Подосинки-Нерская-Анциферово/'
for f_id in to_delete:
    os.system('rm {0}DSCF{1}.JPG'.format(PATH_files, f_id))
    os.system('rm {0}DSCF{1}.RAF'.format(PATH_files, f_id))