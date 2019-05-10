from Header import Header

class ROM(object):
    def __init__(self, rom_path: str):
        with open(rom_path, "rb") as file:
            self.rom = file.read()
        self.header = Header(self.rom[0:15])
        self.trainer_data = []
        if self.header.trainer:
            self.trainer_data = self.rom[16: 16 + 512]
            self.prg_data = self.rom[16 + 512: 16 + 512 + self.header.prg_data_size]
        else:
            self.prg_data = self.rom[16: 16 + self.header.prg_data_size]
            
