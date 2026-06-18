from abc import ABC  , abstractmethod
class SmartDevice(ABC):

    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
   

class SmartDoor(SmartDevice):

     def __init__(self):
      self.__locked = True
     def turn_on(self):
      print("Door system activated")

     def turn_off(self):
      print("Door system deactivated")

     def lock(self):
      self.__is_locked = True
     print("Door locked")

     def unlock(self):
      self.__is_locked = False
     print("Door unlocked")

     def is_locked(self):
        return self.__is_locked


door = SmartDoor()

door.turn_on()
door.unlock()
print("Locked?", door.is_locked())
door.lock()
door.turn_off()