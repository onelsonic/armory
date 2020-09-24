from arm.logicnode.arm_nodes import *

class GetGroupNode(ArmLogicTreeNode):
    """Use to get a collection."""
    bl_idname = 'LNGetGroupNode'
    bl_label = 'Get Collection'
    arm_version = 1

    def init(self, context):
        super(GetGroupNode, self).init(context)
        self.add_input('NodeSocketString', 'Name')
        self.add_output('ArmNodeSocketArray', 'Objects')

add_node(GetGroupNode, category=PKG_AS_CATEGORY, section='collection')
