

from multiprocessing import Pool
import os

from tqdm import tqdm


class DataProcess:
    
  
    def __init__(self,  dofunc, batch_size = 10000,  cpu_count = 0 ) -> None:
        """
            dofunc 
            like do(batch): 
            传入 splited_items 处理的batch数据

            batch_size 
            把数据拆分为多少batch处理, 默认10000

            cpu_count
            使用并行的cpu处理的个数. 默认系统cpu_count - 1
        """
        pnum = cpu_count
        if pnum <= 0:
            pnum = os.cpu_count() - 1
            if pnum <= 0:
                pnum = 1
            
        self.pnum = pnum
        self.dofunc = dofunc
        self.splited_items_count = batch_size

    def processing(self, iterable, desc = "...",  limit = 1 << 32):
        """
            iterable 迭代器 eg. open(filename)  
            desc 加载进度条描述
            limit 限制加载的个数
        """

        self.pool = Pool(self.pnum)

        result_items = []

        total = 0
        datas = []
        cur = []
        for line in tqdm(iterable, desc="load and count the total of iterable"):
 
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

        
        with tqdm(desc=f"{desc} multi processing data", total=total) as bar:
            for items in self.pool.imap_unordered(self.dofunc, datas):
                for item in items:
                    result_items.append(item)
                bar.update(len(items))

        self.pool.close()
        return result_items
        

    


