from multiprocessing import Pool
import os

def bomber_function(bomber):
    os.system(f'{bomber}.py')
    time.sleep(2)


bomber_list = ['bomber1', 'bomber2', 'bomber3', 'bomber4', 'bomber5', 'bomber6', 'bomber7', 'bomber8', 'bomber9', 'bomber10']
# bomber_list = ['bomber1', 'bomber2', 'bomber3', 'bomber4', 'bomber5', 'bomber6']
if __name__ == '__main__': 
    p = Pool(10)
    # p = Pool(6)
    x = p.imap(bomber_function, bomber_list)
    p.close()
    p.join()