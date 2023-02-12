from typing import Dict, Union, Optional


class Computer:
    def __init__(
        self,
        description: str,
        processor_type: str,
        hard_drive_capacity: int,
        memory: int,
        os: str,
        made_in_year: int,
        price: int
    ):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.os = os
        self.made_in_year = made_in_year
        self.price = price


class ComputerShop:
    def __init__(self):
        self.shop_inventory: Dict[int, Computer] = {}
        self.item_id_generator: int = 0

    def buy(self, computer: Computer) -> int:
        self.item_id_generator = self.item_id_generator + 1
        self.shop_inventory[self.item_id_generator] = computer
        return self.item_id_generator

    def update_price(self, item_id: int, new_price: int) -> None :
        if item_id in self.shop_inventory:
            self.shop_inventory[item_id].price = new_price
        else:
            print('Cannot update price for an item that does not exist')

    def sell(self, item_id: int) -> None:
        del self.shop_inventory[item_id]

    def print_item(self, item_id: int, shop_inventory: dict) -> None:
        if item_id in self.shop_inventory:
            print(f'Item with id {item_id} : {self.shop_inventory[item_id]}')
        else:
            print(f'Item with id {item_id} does not exist')


class RebuyShop(ComputerShop):
    shop_inventory: Dict[int, Dict[str, Union[str, int, bool]]] = {}
    item_id: int = 0

    def refurbish(self, item_id: int, shop_inventory: dict, new_os: Optional[str] = None) -> None:
        if item_id in shop_inventory:

            computer = shop_inventory[item_id]

            if int(computer['made_in_year']) < 2000:
                computer['price'] = 0
            elif int(computer['made_in_year']) < 2010:
                computer['price'] = 250
            elif int(computer['made_in_year']) < 2018:
                computer['price'] = 650
            else:
                computer['price'] = 1000

            if new_os is not None:
                computer['os'] = new_os
        else:
            print('Cannot refurbish an item that does not exist')


def create_computer(
                    description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    os: str,
                    made_in_year: int,
                    price: int
                    ) -> Dict[str, Union[str, int, bool]]:
    return {
            'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'os': os,
            'made_in_year': made_in_year,
            'price': price
        }


if __name__ == "main":
    # Computer Shop
    print('CREATE COMPUTER')
    computer_shop = ComputerShop()

    computer = create_computer(
        "Triston XPT 3352",
        "1.4 GHz Quad‑Core Intel Core i5",
        256, 16,
        "Unix", 2016, 1400)

    print(computer)

    print('\nCOMPUTER SHOP')
    print('#' * 20)
    cid: int = computer_shop.buy(computer)

    print('UPDATE PRICE')
    computer_shop.update_price(cid, 1450)
    computer_shop.print_item(cid)

    print('SELL')
    computer_shop.sell(cid)

    print('PRINT AFTER SELLING')
    computer_shop.print_item(cid)


# Rebuy Shop
    rebuy_shop = RebuyShop()
    rcid: int = rebuy_shop.buy(computer)
    print('\nREBUY SHOP')
    print('#' * 20)

    print('REFURBISH')
    rebuy_shop.refurbish(rcid, "Linux Mint")
    rebuy_shop.print_item(rcid)

    print('R SELL')
    rebuy_shop.sell(rcid)

    print('PRINT AFTER R SELLING')
    rebuy_shop.print_item(rcid)
