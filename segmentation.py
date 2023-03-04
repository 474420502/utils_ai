from string import punctuation

special_char = ".．"
seg_char = "。!;！；\r\t\n"

class Segmentation:
    def __init__(self, text, start, end) -> None:
        self.text = text
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return self.text[self.start:self.end]

    """ 
        获取分段的字符串
    """
    def seg_text(self) -> str:
        return self.text[self.start:self.end]

class TextSegmentation:
 
    def __init__(self, text) -> None:
        self.text = text
        self.special_char = special_char
        self.seg_char = seg_char
        self.segmentation = []

    def get_segmentation(self):
        """ 
            获取分段
        """
        return self.segmentation

    def split_segmentation(self):
        """ 
            拆分段
        """
        text = self.text
        self.segmentation = []

        i = 0
        start = 0
        is_ready_cut = 0

        while i < len(text):
            c = text[i]

            if c in self.seg_char:
                if is_ready_cut == 0: is_ready_cut += 1
            else:
                if is_ready_cut == 1: 

                    is_ready_cut = 0
                    if start != i:
                        self.segmentation.append(Segmentation(self.text,start,i))
                        start = i
            i += 1
        return self.segmentation
 
if __name__ == "__main__":
    text = "随着社会经济的发展，糖尿病患病率逐渐增加，已成为严重的世界性问题。糖尿病特别是其慢性并发症影响患者的生活质量，甚至威胁患者的生命，给社会、家庭以及患者带来沉重的经济负担。中国的流行病学调查显示，中国20岁以上人群2型糖尿病患病率达9.7%；且近2/3的患者HbA1c得不到有效控制(HbA1c≤7%)；60.7%的患者因未被诊断而无法及早进行有效的治疗和指导。"
    ts = TextSegmentation(text)
 
    for iter in ts.split_segmentation():
        print( str(iter) )