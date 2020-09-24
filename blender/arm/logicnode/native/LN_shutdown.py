from arm.logicnode.arm_nodes import *

class ShutdownNode(ArmLogicTreeNode):
    """Use to close the application."""
    bl_idname = 'LNShutdownNode'
    bl_label = 'Shutdown'
    arm_version = 1

    def init(self, context):
        super(ShutdownNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(ShutdownNode, category=PKG_AS_CATEGORY)
