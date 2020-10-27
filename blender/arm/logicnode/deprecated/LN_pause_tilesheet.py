from arm.logicnode.arm_nodes import *

class PauseTilesheetNode(ArmLogicTreeNode):
    """Pauses the given tilesheet action."""
    bl_idname = 'LNPauseTilesheetNode'
    bl_label = 'Pause Tilesheet'
    bl_description = "Please use the \"Set Tilesheet Paused\" node instead"
    bl_icon = 'ERROR'
    arm_section = 'tilesheet'
    arm_is_obsolete = True
    arm_version = 2

    def init(self, context):
        super(PauseTilesheetNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_output('ArmNodeSocketAction', 'Out')
