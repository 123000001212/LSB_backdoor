class LSB(): # 32*32*3*4=12288, 12288/40=307.2
    def __init__(self, text='Alice', height=32, width=32, channel=3, num_bytes=4) -> None:
        self.text=text
        self.height=height
        self.width=width
        self.channel=channel
        self.num_bytes=num_bytes
        self.repeat_time=(height*width*channel*num_bytes)//(len(text)*8) + 1
        self.bin="".join([bin(ord(i))[2:].zfill(8) for i in text*self.repeat_time])[:height*width*channel*num_bytes]
    def add_trigger(trainset)->None:
        pass

lsb=LSB()
print(len(lsb.bin))
print(lsb.bin)
