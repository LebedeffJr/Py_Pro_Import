import random
from time import sleep
from tqdm import tqdm

def hacking():
    print("Взлом серверов в процессе ...")
    for i in tqdm(range(100), colour="green"):
        sleep(random.uniform(0.01,0.1))
