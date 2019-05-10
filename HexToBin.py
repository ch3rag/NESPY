class HexToBin:
    def convert(self, hex: str, num_bytes: int):
        diff = num_bytes - len(hex) 
        if diff > 0:
            hex = "0" * diff +  hex
        switcher = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "a": "1010",
            "b": "1011",
            "c": "1100",
            "d": "1101",
            "e": "1110",
            "f": "1111"
        }
        bin = ""
        for char in hex:
            bin = bin + switcher.get(char)
        return bin

