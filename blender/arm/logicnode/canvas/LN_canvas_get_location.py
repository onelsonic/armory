from arm.logicnode.arm_nodes import *

class CanvasGetLocationNode(ArmLogicTreeNode):
    """Use to get the location of a UI element (in pixels)."""
    bl_idname = 'LNCanvasGetLocationNode'
    bl_label = 'Canvas Get Location'
    arm_version = 1

    def init(self, context):
        super(CanvasGetLocationNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketString', 'Element')
        self.add_output('ArmNodeSocketAction', 'Out')
        self.add_output('NodeSocketFloat', 'X')
        self.add_output('NodeSocketFloat', 'Y')

add_node(CanvasGetLocationNode, category=PKG_AS_CATEGORY)
