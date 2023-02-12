from typing import Dict, Union

from procedural_computer_shop import buy, print_item, sell, update_price
from procedural_rebuy_shop import buy as rbuy
from procedural_rebuy_shop import print_item as rprint_item
from procedural_rebuy_shop import refurbish
from procedural_rebuy_shop import sell as rsell
from procedural_rebuy_shop import update_price as update_price


def create_computer(
        description: str, processor_type: str,
        hard_drive_capacity: int, memory: int,
        os: str, made_in_year: int,
        price: int) -> Dict[str, Union[str, int, bool]]:
    return {
        'description': description,
        'processor_type': processor_type,
        'hard_drive_capacity': hard_drive_capacity,
        'memory': memory,
        'os': os,
        'made_in_year': made_in_year,
        'price': price
    }


def use_procedural() -> None:

    # Computer Shop
    print('CREATE COMPUTER')
    computer = create_computer(
        "Triston XPT 3352",
        "1.4 GHz Quad‑Core Intel Core i5",
        256, 16,
        "Unix", 2016, 1400)

    print(computer)

    print('\nCOMPUTER SHOP')
    print('#' * 20)
    cid: int = buy(computer)

    print('UPDATE PRICE')
    update_price(cid, 1450)
    print_item(cid)

    print('SELL')
    sell(cid)

    print('PRINT AFTER SELLING')
    print_item(cid)

    # Rebuy Shop
    rcid: int = rbuy(computer)
    print('\nREBUY SHOP')
    print('#' * 20)

    print('REFURBISH')
    refurbish(rcid, "Linux Mint")
    rprint_item(rcid)

    print('R SELL')
    rsell(rcid)

    print('PRINT AFTER R SELLING')
    rprint_item(rcid)

use_procedural()

