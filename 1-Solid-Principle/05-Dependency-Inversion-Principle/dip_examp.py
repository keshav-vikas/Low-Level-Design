'''
Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules. Both should depend on abstractions, not concretions.
High-level modules should not depend on low-level modules. Instead, both should depend on abstractions. Additionally, abstractions should not depend on details.
Details should depend on abstractions.
Make classes depend on abstract classes rather than non-abstract classes.
        e.g. Make classes inherit from abstract classes.
'''
# Violation of DIP:


from abc import ABC, abstractmethod


class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class ElectricPowerSwitch:

    def __init__(self, l: LightBulb):
        self.lightBulb = l
        self.on = False

    def press(self):
        if self.on:
            self.lightBulb.turn_off()
            self.on = False
        else:
            self.lightBulb.turn_on()
            self.on = True


l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()

'''
In this example, the ElectricPowerSwitch class depends directly on the LightBulb class. This violates the DIP because a high-level module (ElectricPowerSwitch)
depends on a low-level module (LightBulb).
'''

# Following DIP:


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: Bulb turned on")

    def turn_off(self):
        print("LightBulb: Bulb turned off")


class ElectricPowerSwitch:
    def __init__(self, switchable: Switchable):
        self.switchable = switchable
        self.on = False

    def press(self):
        if self.on:
            self.switchable.turn_off()
            self.on = False
        else:
            self.switchable.turn_on()
            self.on = True


# create a light bulb object
light_bulb = LightBulb()

# create an electric power switch object
electric_power_switch = ElectricPowerSwitch(light_bulb)

# press the switch to turn on the light bulb
electric_power_switch.press()

# press the switch again to turn off the light bulb
electric_power_switch.press()


'''
In this example, the ElectricPowerSwitch class depends on an abstraction (Switchable) instead of a low-level module (LightBulb). The LightBulb class 
implements the Switchable interface, which allows it to be passed as a dependency to the ElectricPowerSwitch class. This follows the DIP because high-level 
modules (ElectricPowerSwitch) depend on abstractions (Switchable) instead of low-level modules (LightBulb).
'''
