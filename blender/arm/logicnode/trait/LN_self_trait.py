from arm.logicnode.arm_nodes import *

class SelfTraitNode(ArmLogicTreeNode):
    """Use to get the trait that owns this node."""
    bl_idname = 'LNSelfTraitNode'
    bl_label = 'Self Trait'
    arm_version = 1

    def init(self, context):
        super(SelfTraitNode, self).init(context)
        self.add_output('NodeSocketShader', 'Trait')

add_node(SelfTraitNode, category=PKG_AS_CATEGORY)
