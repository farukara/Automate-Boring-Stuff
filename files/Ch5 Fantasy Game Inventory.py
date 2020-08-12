#! Python3
# inventory.py


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print("Total number of items: " + str(item_total))
    return


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


if __name__ == "__main__":
    
    
    print('---------------')
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventory(stuff)
    print('---------------')

    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = {'gold coin': 42, 'rope': 1}
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)
    
    print('---------------')
