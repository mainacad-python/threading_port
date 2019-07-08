import logging
import time
import threading

from stores import Warehouse, Container

logger = logging.getLogger(__name__)


class Queue:
    def __init__(self):
        self._list = []

    def put(self, obj):
        self._list.append(obj)

    def pop(self):
        if self._list:
            return self._list.pop(0)
        else:
            logger.warning("Queue is empty")


class Docker:
    def __init__(self, id, warehouse):
        self.id = id
        self.warehouse = warehouse
        self.is_free = True
        self.flags = [False, False]
        self.load_thrd = None
        self.unload_thrd = None
        logger.info(f"Docker: {self.id} has been created!")

    def serve_ship(self, ship, to_load, to_unload):
        logger.info(f"At dock {self.id} starting to serve ship {ship.name} to load: {to_load}, to unload: {to_unload}")
        self.is_free = False
        if self.load_thrd:
            logger.debug("Finishing previous loading...")
            self.load_thrd.join()

        if self.unload_thrd:
            logger.debug("Finishing previous unloading...")
            self.unload_thrd.join()

        self.unload_thrd = threading.Thread(target=self.move, args=(ship.holder, self.warehouse, to_unload, 0))
        self.load_thrd = threading.Thread(target=self.move, args=(self.warehouse, ship.holder, to_load, 1))

        self.flags = [False, False]

        logger.info(f"At dock {self.id} starting to unload {ship.name}")
        self.unload_thrd.start()

        logger.info(f"At dock {self.id } starting to load {ship.name}")
        self.load_thrd.start()

    def processing(self, working_time):
        while working_time:
            logger.debug(f'Dock-{self.id} | Remaining work: {working_time} sec...')
            time.sleep(1)
            working_time -= 1

    def move(self, source, destination, list_of_items, flag_index):
        is_ok = False
        logger.debug(f"Moving from {source.name} to {destination.name}")
        while not is_ok:
            is_ok = True
            for container in list_of_items:
                if source.has(container):
                    if destination.free_volume >= source.containers[container].volume:
                        c=source.pop(container)
                        destination.put(c)
                        self.processing(destination.containers[container].type * 3)
                        logger.info(
                            f"At dock {self.id} moved complete container {c.name} from {source.name} to {destination.name}")
                    else:
                        logger.info(f"Something gone wrong while moving from {source.name} to {destination.name}")
                        is_ok = False
            time.sleep(0.5)

        self.flags[flag_index] = True

        if self.flags[0] and self.flags[1]:
            logger.info(f"Moving from {source.name} to {destination.name} has been finished. Docker-{self.id} is free now!")
            self.is_free = True


class Port:
    def __init__(self, count_of_dockers):
        self.warehouse = Warehouse("Port warehouse", volume=100000)
        self.dockers = [Docker(i, self.warehouse) for i in range(count_of_dockers)]

        self.manage_table = {}

        self.queue = Queue()
        self.manage_thrd = threading.Thread(target=self.manage)
        self.manage_thrd.start()

    def add_ships(self, ship):
        self.queue.put(ship)
        print(f"{ship.name} has been put to the queue!")

    def manage(self):
        logger.info("Starting to manage dockers")
        while True:
            for docker in self.dockers:
                if docker.is_free:
                    ship = self.queue.pop()
                    if ship:
                        docker.serve_ship(ship,
                                          to_load=self.manage_table[ship.name]['to_load'],
                                          to_unload=self.manage_table[ship.name]['to_unload'])
                    else:
                        break
            time.sleep(10)
