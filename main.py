from Read_data import ReadData
from singlell import SingleLL

inst_read = ReadData()
inst_single = SingleLL()

inst_single.prepend_node("B")
inst_single.prepend_node("A")
inst_single.show_nodes_list()
inst_single.append_node("C")
inst_single.append_node("D")
inst_single.show_nodes_list()
inst_single.get(3)
inst_single.update(1,3)
inst_single.show_nodes_list()
inst_single.insert(3,2)
inst_single.show_nodes_list()
inst_single.remove(3)
inst_single.show_nodes_list()
inst_single.reverse()
inst_single.show_nodes_list()
inst_single.empty()
inst_single.show_nodes_list()

