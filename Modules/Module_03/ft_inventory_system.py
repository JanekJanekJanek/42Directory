import sys


class InventoryError(Exception):
    def __init__(self, message: str) -> None:
        self._message = message
        super().__init__(self._message)


class RedundantError(InventoryError):
    def __init__(self, message: str) -> None:
        self._message = message
        super().__init__(self._message)


def main():
    print("=== Inventory System Analysis ===")
    inventory = dict()
    for arg in sys.argv[1:]:
        try:
            pair = arg.split(":")
            if len(pair) == 2:
                if pair[0] in inventory.keys():
                    raise RedundantError(f"Redundant item '{pair[0]}'"
                                         " - discarding")
                else:
                    inventory.update({pair[0] : int(pair[1])})
            else:
                raise InventoryError(f"Error - invalid parameter '{arg}'")
        except InventoryError as e:
            print(f"{e}")
        except RedundantError:
            print(f"{e}")
        except ValueError as e:
            print(f"Quantity error for '{pair[0]}': {e}")
    print(f"Got inventory: {inventory}")
    print(f"Item list: {inventory.keys()}")
    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")
    for item in inventory:
        proportion = round(inventory[item] / total_quantity * 100, 1)
        print(f"Item {item} represents {proportion}%")
    print(f"Item most abundant: ")
    print(f"Item least abundant: ")
    inventory.update({"magic_item" : 42})
    print(f"Updated inventory: {inventory}")

if __name__ == "__main__":
    main()
