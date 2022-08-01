import os



# os.chdir('/home/maria/yadisk/lab/supporting/PhD/PhD-docs/2020-2021/rst')
# os.chdir('/home/maria/yadisk/lab/supporting/PhD/PhD-docs/2020-2021/inscr')
# os.chdir('/home/maria/yadisk/lab/supporting/PhD/PhD-docs/2020-2021/rapport de suivi-these-partially-signed')
# os.chdir('/home/maria/yadisk/lab/supporting/PhD/PhD-docs/2020-2021/inscr/MIPT')
# os.chdir('/home/maria/yadisk/lab/supporting/PhD/PhD-docs/2020-2021')
os.chdir('/home/maria/yadisk/lab/supporting/Postdoc/Astex/')
# fname = 'kadukova-inscription-signed'
# fname = 'Kadukova-rapport-de-suivi-these-signed-MK-SR-VC-SG'
# fname = 'Kadukova-UGA-letter-2-long'
fname = 'Maria Kadukova - Offer Letter - April 2021'.replace(' ', '\ ')
# os.system('pdfseparate -f 1 -l 2 {0}.pdf p%d.pdf'.format(fname))

# for i in range(1, 3):
#     os.system('convert -density 300 -quality 100 -background white -flatten p{0}.pdf p{0}.png'.format(i))

# cmd_ = 'convert -density 300 -quality 100 -background white -flatten {0}.pdf {0}.png'.format(fname.replace(' ', '\ '))
# os.system(cmd_)
# fname = 'Kadukova-UGA-letter-2-Chupin'
# fname = 'Kadukova-declaration_de_l_auteur_prealable_a_la_soutenance_MK'
# os.system('convert -density 300 -quality 100  {0}.png {0}.pdf'.format(fname))

fname = 'Maria Kadukova - Offer Letter - April 2021_MK'.replace(' ', '\ ')

for i in range(1, 3):
    os.system('convert -density 300 -quality 100  p{0}.png p{0}.pdf'.format(i))

os.system('pdfunite {0} {1}.pdf'.format(' '.join('p{0}.pdf'.format(i) for i in range(1, 3)),
                                     fname))

# os.chdir('/home/maria/yadisk/lab/supporting/PhD/PhD-docs/2020-2021')
# os.system('convert -density 300 -quality 100 -background white -flatten Kadukova-RGPD_ADUM.pdf Kadukova-RGPD_ADUM.png')
# os.system('convert -density 300 -quality 100  {0}.png {1}.pdf')


# fname = 'kadukova-inscription-unsigned'
# os.system('convert -density 300 -quality 100 -background white -flatten {0}.pdf {0}.png'.format(fname))
# fname = 'Kadukova-UGA_exoneration_soutenance_31032021_signed'
# os.system('convert -density 300 -quality 100  {0}.png {0}.pdf'.format(fname))