from stores import Container, ContainerTypes, Ship, Warehouse
from port import Port
import logging

logging.basicConfig(level=logging.INFO)

port = Port(3)
ship_A = Ship("Ship A",10000)
ship_B = Ship("Ship B",10000)
ship_C = Ship("Ship C",10000)
ship_D = Ship("Ship D",10000)
ship_E = Ship("Ship E",10000)

ship_A.holder.put(Container("A1",100,ContainerTypes.LIGHT))
ship_A.holder.put(Container("A2",400,ContainerTypes.HEAVY))
ship_A.holder.put(Container("A3",400,ContainerTypes.HEAVY))
ship_A.holder.put(Container("A4",200,ContainerTypes.MEDIUM))

ship_B.holder.put(Container("B1",200,ContainerTypes.MEDIUM))
ship_B.holder.put(Container("B2",200,ContainerTypes.MEDIUM))
ship_B.holder.put(Container("B3",200,ContainerTypes.MEDIUM))

ship_C.holder.put(Container("C1",400,ContainerTypes.HEAVY))
ship_C.holder.put(Container("C2",400,ContainerTypes.HEAVY))
ship_C.holder.put(Container("C3",100,ContainerTypes.LIGHT))
ship_C.holder.put(Container("C4",100,ContainerTypes.LIGHT))
ship_C.holder.put(Container("C5",100,ContainerTypes.LIGHT))

ship_D.holder.put(Container("D1",200,ContainerTypes.MEDIUM))
ship_D.holder.put(Container("D2",400,ContainerTypes.HEAVY))

ship_E.holder.put(Container("E1",200,ContainerTypes.MEDIUM))
ship_E.holder.put(Container("E2",400,ContainerTypes.HEAVY))
ship_E.holder.put(Container("E3",100,ContainerTypes.LIGHT))
ship_E.holder.put(Container("E4",100,ContainerTypes.LIGHT))

port.warehouse.put(Container("P1",100,ContainerTypes.LIGHT))
port.warehouse.put(Container("P2",100,ContainerTypes.LIGHT))
port.warehouse.put(Container("P3",100,ContainerTypes.LIGHT))
port.warehouse.put(Container("P4",100,ContainerTypes.MEDIUM))
port.warehouse.put(Container("P5",100,ContainerTypes.MEDIUM))
port.warehouse.put(Container("P6",100,ContainerTypes.MEDIUM))
port.warehouse.put(Container("P7",100,ContainerTypes.HEAVY))
port.warehouse.put(Container("P8",100,ContainerTypes.HEAVY))
port.warehouse.put(Container("P9",100,ContainerTypes.HEAVY))

port.manage_table["Ship A"]={"to_load":["P1","P2","B1"],"to_unload":["A1","A2","A3"]}
port.manage_table["Ship B"]={"to_load":["P3","P4","A1","A2","C1","C2"],"to_unload":["B1","B2","B3"]}
port.manage_table["Ship C"]={"to_load":["P5","A3","B2","E2"],"to_unload":["C1","C2","C3","C4","C5"]}
port.manage_table["Ship D"]={"to_load":["P6","P7","B3","C3","C4","E1","E3"],"to_unload":["D1","D2"]}
port.manage_table["Ship E"]={"to_load":["P8","P9","C5","D1","D2"],"to_unload":["E1","E2","E3","E4"]}

port.queue.put(ship_A)
port.queue.put(ship_B)
port.queue.put(ship_C)
port.queue.put(ship_D)
port.queue.put(ship_E)