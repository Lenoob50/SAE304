from tqdm import tqdm
from time import sleep
def pg():
    for i in tqdm(range(0, 100), desc="Progression"):
        sleep(.1)
