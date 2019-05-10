import argparse
from CPU import CPU
from ROM import ROM
def main():
    parser = argparse.ArgumentParser(description = "Nes Emulator")
    parser.add_argument("rom_path",
                        type = str,
                        metavar = "ROM",
                        help = "Path to rom")
    args = parser.parse_args()

    # TODO: Verify ROM Path
    rom = ROM(args.rom_path)
    cpu = CPU()
    #print(rom.prg_data[0])

if __name__ == "__main__":
    main()
