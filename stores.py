import logging

logger = logging.getLogger(__name__)


class ContainerTypes:
    LIGHT = 1
    MEDIUM = 2
    HEAVY = 3


class Store:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class Container(Store):
    def __init__(self, name, volume=100, type=ContainerTypes.LIGHT):
        super().__init__(name, volume)
        self.type = type
        logger.info(f"Container: {self.name}, vol: {self.volume} has been created!")


class Warehouse(Store):
    def __init__(self, name, volume):
        super().__init__(name, volume)
        self.containers = {}
        logger.info(f"Warehouse: {self.name}, vol: {self.volume} has been created!")

    @property
    def free_volume(self):
        return self.volume - sum(c.volume for c in self.containers)

    def has(self, container_name):
        return container_name in self.containers.keys()

    def put(self, container):
        self.containers[container.name] = container
        logger.info(f"Container {container} has been put into the {self.name}")

    def pop(self, container_name):
        logger.info(f"Container {container_name} has been popped from the {self.name}")
        return self.containers.pop(container_name)


class Ship:
    def __init__(self, name, volume):
        self.name = name
        self.holder = Warehouse(f"{self.name}'s holder", volume)
        logger.info(f"Ship: {self.name} has been created!")

