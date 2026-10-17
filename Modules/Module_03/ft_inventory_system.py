import sys


class InventoryError(Exception):
    def __init__(self, message: str) -> None:
        self._message = message
        super().__init__(self._message)


class RedundantError(InventoryError):
    def __init__(self, message: str) -> None:
        self._message = message
        super().__init__(self._message)


def main() -> None:
    print("=== Inventory System Analysis ===\n")
    inventory: dict[str, int] = dict()
    for arg in sys.argv[1:]:
        try:
            pair = arg.split(":")
            if len(pair) == 2:
                if pair[0] in inventory.keys():
                    raise RedundantError(f"🚫 Redundant item '{pair[0]}'"
                                         " - discarding")
                elif int(pair[1]) > 0:
                    inventory.update({pair[0]: int(pair[1])})
                else:
                    raise InventoryError(f"🚫 Error - invalid quantity"
                                         f" '{pair[1]}'")
            else:
                raise InventoryError(f"🚫 Error - invalid parameter '{arg}'")
        except InventoryError as e:
            print(f"{e}")
        except RedundantError as e:
            print(f"{e}")
        except ValueError as e:
            print(f"🚫 Quantity error for '{pair[0]}': {e}")
    print(f"🎒 Got inventory: {inventory}")
    print(f"📋 Item list: {list(inventory.keys())}")
    total_quantity = sum(inventory.values())
    print(f"📋 Total quantity of the {len(inventory)} items:"
          f" {total_quantity}\n")
    for item in inventory:
        proportion = round(inventory[item] / total_quantity * 100, 1)
        print(f"➤ Item {item} represents {proportion}%")
    keys = list(inventory.keys())
    try:
        min_key = keys[0]
        max_key = keys[0]
        min_val = inventory[min_key]
        max_val = inventory[max_key]
        for key in keys:
            if inventory[min_key] > inventory[key]:
                min_key = key
                min_val = inventory[key]
            if inventory[max_key] < inventory[key]:
                max_key = key
                max_val = inventory[key]
    except IndexError:
        min_key = None
        max_key = None
        min_val = 0
        max_val = 0
    print(f"\n📈 Item most abundant: {max_key} with quantity {max_val}")
    print(f"🤏 Item least abundant: {min_key} with quantity {min_val}\n")
    inventory.update({"magic_item": 42})
    print(f"🎉 Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
