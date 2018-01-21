import os
from params import get_params


if __name__ == "__main__":

    params = get_params()

    inputfile = open(os.path.join(params['root'], params['root_save'],
                                params['rankings_dir'], 'resnet_ranking.csv'), 'r')
    inputfile.readline()
    x = inputfile.readlines()
    for line in x:
        end=len(line)
        coma = line.find(",")
        id=line[0:coma]
        outfile = open(os.path.join(params['root'], params['root_save'],
                    params['rankings_dir'], 'deepfeats',id+'.txt'), 'w')
        query=line[coma+1:end]
        query=query.split(' ')
        for item in query:
            outfile.write (item + '\n')