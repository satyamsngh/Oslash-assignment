from sys import argv
from additionals import shopkeeper, inventory, system

def parse():
    if len(argv) != system.maxArgs:
        raise Exception(system.filePathError)
    
    file_path = argv[system.filePath]
    lines = open(file_path, system.readOnly).readlines()
    return lines

def main():
    lines = parse()
    localInventory = inventory.inventory(shopkeeper.InventoryList)
    print(localInventory.getBill(lines))  

if __name__ == system.main:
    main()
