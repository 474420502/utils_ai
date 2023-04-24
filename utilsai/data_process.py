

from multiprocessing import Pool
import os

from tqdm import tqdm


class DataProcess:


    def __init__(self,  dofunc, splited_items_count = 10000,  cpu_count = 0 ) -> None:
        tqdm()
        pnum = cpu_count
        if pnum <= 0:
            pnum = os.cpu_count() - 1
            if pnum <= 0:
                pnum = 1
            
        self.pool = Pool(pnum)
        self.dofunc = dofunc
        self.splited_items_count = splited_items_count

    def processing(self, iterable, desc = "...",  limit = 1 << 32):

        result_items = []

        total = 0
        datas = []
        cur = []
        for line in tqdm(iterable):
 
            total += 1
            cur.append(line)
            if len(cur) >= self.splited_items_count:
                datas.append(cur)
                cur = []

            limit -= 1
            if limit <= 0:
                break

        if len(cur) != 0:
            datas.append(cur)
            cur = []

        
        with tqdm(desc=f"{desc} load data", total=total) as bar:
            for items in self.pool.imap_unordered(self.dofunc, datas):
                for item in items:
                    result_items.append(item)
                bar.update(len(items))

        return result_items
        

    


