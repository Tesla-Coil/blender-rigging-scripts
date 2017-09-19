import bpy

bl_info = {
    "name": "Automatic Weight Selected",
    "description": "Create automatic weights only for selected bones.",
    "author": "Les Fées Spéciales",
    "version": (0, 0, 1),
    "blender": (2, 79, 0),
    "location": "View3D",
    "warning": "Add",
    "wiki_url": "",
    "category": "Paint" }
    
def_bones = {}

def main(self, context):
    obj = context.object
    # Get armature object
    arm_obj = set(context.selected_objects)
    arm_obj.discard(obj)
    arm_obj = tuple(arm_obj)[0]
    
    for pb in arm_obj.pose.bones:
        # Store DEF setting
        def_bones[pb.name] = pb.bone.use_deform
        if not pb in context.selected_pose_bones:
            pb.bone.use_deform = False
        else:
            if not pb.bone.use_deform:
                self.report({'INFO'}, 'Bonet %s is non-deforming.' % pb.name)
    
    # Automatic weight
    bpy.ops.paint.weight_from_bones(type='AUTOMATIC')
    
    # Restore DEF setting
    for pb in arm_obj.pose.bones:
        pb.bone.use_deform = def_bones[pb.name]
    def_bones.clear()
    
    print("DONE")
    
class AutomaticWeightSelected(bpy.types.Operator):
    bl_idname = "paint.automatic_weight_selected"
    bl_label = "Automatic Weight Selected"
    bl_description = "Add weight only to selected bones"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return (context.mode == 'PAINT_WEIGHT'
#                and context.object.type == 'MESH'
                and len(context.selected_objects) == 2)

    def execute(self, context):
        main(self, context)
        return {"FINISHED"}
        
def weight_tools_panel(self, context):
    layout = self.layout
    layout.operator("paint.automatic_weight_selected")


def register():
    bpy.utils.register_class(AutomaticWeightSelected)
    bpy.types.VIEW3D_PT_tools_weightpaint.append(weight_tools_panel)


def unregister():
    bpy.utils.unregister_class(AutomaticWeightSelected)
    bpy.types.VIEW3D_PT_tools_weightpaint.remove(render_panel)


if __name__ == "__main__":
    register()