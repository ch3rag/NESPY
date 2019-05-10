from HexToBin import HexToBin

class Header(object):
    def __init__(self, header_bytes):
            self.prg_data_size = 16384 * header_bytes[4]
            self.chr_data_size = 8192  * header_bytes[5]
            binify = HexToBin()
            flags = (binify.convert(hex(header_bytes[6])[2:], 2))
            flags_bool = list(map(lambda char: True if char == "1" else False, flags))
            self.horizontal_mirror = flags_bool[7]
            self.rom_battery = flags_bool[6]
            self.trainer = flags_bool[5]
            self.ignore_mirroring = flags_bool[4]
            self.nybble_mapper_number = flags[0:4]