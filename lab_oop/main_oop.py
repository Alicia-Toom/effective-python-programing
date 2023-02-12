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
