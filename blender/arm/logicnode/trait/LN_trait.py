from arm.logicnode.arm_nodes import *

class TraitNode(ArmLogicTreeNode):
    """Use to hold a trait as a variable."""
    bl_idname = 'LNTraitNode'
    bl_label = 'Trait'
    arm_version = 1

    property0: StringProperty(name='', default='')

    def init(self, context):
        super(TraitNode, self).init(context)
        self.add_output('NodeSocketShader', 'Trait', is_var=True)

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')

add_node(TraitNode, category=PKG_AS_CATEGORY)
