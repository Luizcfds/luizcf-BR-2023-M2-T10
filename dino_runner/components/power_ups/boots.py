from dino_runner.utils.constants import BOOTS, BOOTS_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Boots(PowerUp):
    def __init__(self):
        self.image = BOOTS
        self.type = BOOTS_TYPE
        super().__init__(self.image, self.type)