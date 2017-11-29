import os
#importem la funcio get_params de params (funcio params)
from params import get_params

# definim la funcio build_database
def build_database(params):

    # List images
    # llista les imatges dins del path root(GDSA)->database(TB2016) per als grups de train, val i test
    image_names = os.listdir(os.path.join(params['root'],
                             params['database'],params['split'],'images'))

    # File to be saved
    # crea el fitxer a la carpeta save dins de root, escriu la llista d'imatges
    # i li dona el nom de split(train, val o test).txt
    file = open(os.path.join(params['root'],params['root_save'],
                             params['image_lists'],
                             params['split'] + '.txt'),'w')

    # Save image list to disk
    # guarda el fitxer creat anteriorment i el tanca
    for imname in image_names:
        file.write(imname + "\n")
    file.close()

if __name__=="__main__":

    # crida a la funcio get_params dins de params.py
    # obtenim tots els parametres necesaris per cridar la funcio build_database
    params = get_params()

    # cridem la funcio build_database  amb la que creem el fitxer de la llista d'imatges per cada grup
    # train, val i test
    for split in ['train','val','test']:
        params['split'] = split
        build_database(params)
