 
special_char = ".．"
seg_char = "。!;！；\r\t\n"

class TextSegmentation:
    pass

class Segmentation:
    def __init__(self, ts:TextSegmentation, start, end) -> None:
        """
        Keyword Args:
            bio_labels (list): description 
        """
 
        self.ts = ts
        self.start = start
        self.end = end
 
    def __str__(self) -> str:
        return self.ts._text[self.start:self.end]

    """ 
        获取分段的字符串
    """
    def text(self) -> str:
        return self.ts._text[self.start:self.end]
 

    """ 
        分段的bio信息
    """
    def bio_labels(self):
        return self.ts.bio_labels[self.start:self.end]
    
    """ 
        分段的bio信息
    """
    def bio_labels_ids(self):
        return self.ts.bio_labels_ids[self.start:self.end]


class TextSegmentation:
 
    def __init__(self, text, **kargs ) -> None:
        """
        Keyword Args:
        seg_char (str): description 
        bio_labels (list): desc
        """
        self._text = text
        self.segmentation: list[Segmentation] = []

        if 'seg_char' in kargs:
            self.seg_char = kargs['seg_char']
        else:
            self.seg_char = seg_char

        if 'bio_labels' in kargs:
            self.bio_labels = kargs['bio_labels']
            if 'bio_labels_idx_map' in kargs:
                self.bio_labels_ids_map = kargs['bio_labels_idx_map']
                self.bio_labels_ids = []
                for l in self.bio_labels:
                    self.bio_labels_ids.append(self.bio_labels_ids_map[l])
            else:
                self.bio_labels_ids_map = None
        else:
            self.bio_labels = None

        self._split_segmentation()

    def text(self):
        return self._text


    def get_segmentation(self) ->  list[Segmentation]:
        """ 
            获取分段
        """
        return self.segmentation

    def _split_segmentation(self) ->  list[Segmentation]:
        """ 
            拆分段
        """
  
        self.segmentation: list[Segmentation] = []

        i = 0
        start = 0
        is_ready_cut = 0

        while i < len(self._text):
            c = self._text[i]

            if c in self.seg_char:
                if is_ready_cut == 0: is_ready_cut += 1
            else:
                if is_ready_cut == 1: 

                    is_ready_cut = 0
                    if start != i:
                        self.segmentation.append(Segmentation(self,start,i))
                        start = i
            i += 1
        return self.segmentation
 
if __name__ == "__main__":
 
    text = "随着社会经济的发展，糖尿病患病率逐渐增加，已成为严重的世界性问题。糖尿病特别是其慢性并发症影响患者的生活质量，甚至威胁患者的生命，给社会、家庭以及患者带来沉重的经济负担。中国的流行病学调查显示，中国20岁以上人群2型糖尿病患病率达9.7%；且近2/3的患者HbA1c得不到有效控制(HbA1c≤7%)；60.7%的患者因未被诊断而无法及早进行有效的治疗和指导。"
    BIO = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-Disease', 'I-Disease', 'I-Disease', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-Disease', 'I-Disease', 'I-Disease', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-Class', 'I-Class', 'I-Disease', 'I-Disease', 'I-Disease', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-Test_items', 'I-Test_items', 'I-Test_items', 'I-Test_items', 'I-Test_items', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-Test_items', 'I-Test_items', 'I-Test_items', 'I-Test_items', 'I-Test_items', 'B-Test_Value', 'I-Test_Value', 'I-Test_Value', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
    ts = TextSegmentation(text, bio_labels=BIO)
 
    for iter in ts._split_segmentation():
        print( str(iter) )