import numpy as np

comidas = ['salada', 'falafel', 'hamburguer', 'mexicano', 'japonês', 'indiano', 
           'chinês', 'fondue', 'pizza', 'self-service', 'churrasco', 'sopa',
           'omelete', 'frango', 'peixe', 'risoto', 'poke', 'crepe', 'strogonofe',
           'sanduíche', 'açaí', 'pipoca', 'chá', 'pastel', 'macarrão']

decisao = np.random.choice(comidas)

print(decisao)