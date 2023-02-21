import maya.cmds as mc


if mc.window("dumWin0",exists = True):
    mc.deleteUI("dumWin0")

def basicRig(*args):
    print "basic Rigs"
    
    root_joint1 = mc.joint(p=(0, 62, -0.59), n="root_joint")
    
    
    pelvis1 = mc.joint(p=(0, 0, 0), n="pelvis01")
    spine1 = mc.joint(p=(-0, 9.3, 0.5), n="spine01")
    spine2 = mc.joint(p=(0, 6.7, 0.9), n="spine02")
    spine3 = mc.joint(p=(0, 5.5, -0.7), n="spine03")
    chest1 = mc.joint(p=(0, 7.1, -3.1), n="chest01")
    
    
    neck1 = mc.joint(p=(0, 7.5, -0.4), n="neck01")
    head1 = mc.joint(p=(0, 8.9, 5.5), n="head01")
    head2 = mc.joint(p=(0, 19.2, 2.1), n="head02")
    
    
    left_clavicle1 = mc.joint(p=(4.3, 6.3, 0.1), n="left_clavicle01")
    left_shoulder1 = mc.joint(p=(-8, 21, 0), n="left_shoulder01")
    left_elbow1 = mc.joint(p=(-12, 17, 0), n="left_elbow01")
    left_wrist1 = mc.joint(p=(-14, 13, 0), n="left_wrist01")
    left_hand1 = mc.joint(p=(-15, 11, 0), n="left_hand01")
    
    
    left_thumb1 = mc.joint(p=(-0.5, -0.2, 1.8), n="left_thumb01")
    left_thumb2 = mc.joint(p=(0.8, 1.0, 1.3), n="left_thumb02")
    left_thumb3 = mc.joint(p=(2.4, 0.3,-0.6), n="left_thumb03")
    
    
    left_index1 = mc.joint(p=(1.5, 0.0, 1.4), n="left_index01")
    left_index2 = mc.joint(p=(2.4, -0.5, 0.3), n="left_index02")
    left_index3 = mc.joint(p=(1.7, -0.2, 0.1), n="left_index03")
    left_index4 = mc.joint(p=(1.0, -0.0, 0.0), n="left_index04")
    
    
    left_middle1 = mc.joint(p=(1.4, 0.0, 0.1), n="left_middle01")
    left_middle2 = mc.joint(p=(2.4, -0.3, 0.0), n="left_middle02")
    left_middle3 = mc.joint(p=(2.3, -0.1, 0.2), n="left_middle03")
    left_middle4 = mc.joint(p=(1.2, -0.1, 0.0), n="left_middle04")
    
    
    left_ring1 = mc.joint(p=(1.4, 0.0, -0.4), n="left_ring01")
    left_ring2 = mc.joint(p=(2.2, -0.0, -0.2), n="left_ring02")
    left_ring3 = mc.joint(p=(2.1, -0.2, 0.0), n="left_ring03")
    left_ring4 = mc.joint(p=(1.0, 0.0, 0.0), n="left_ring04")
    
    
    left_pinky1 = mc.joint(p=(1.6, 0.0, -1.7), n="left_pinky01")
    left_pinky2 = mc.joint(p=(2.0, -0.1, 0.2), n="left_pinky02")
    left_pinky3 = mc.joint(p=(1.4, -0.1, 0.0), n="left_pinky03")
    left_pinky4 = mc.joint(p=(0.7, -0.0, -0.0), n="left_pinky04")
    
    
    
    right_clavicle1 = mc.joint(p=(4, 23, 0), n="right_clavicle01")
    right_shoulder1 = mc.joint(p=(8, 21, 0), n="right_shoulder01")
    right_elbow1 = mc.joint(p=(12, 17, 0), n="right_elbow01")
    right_wrist1 = mc.joint(p=(14, 13, 0), n="right_wrist01")
    right_hand1 = mc.joint(p=(15, 11, 0), n="right_hand01")
    
    
    right_thumb1 = mc.joint(p=(-0.5, -0.2 ,1.8), n="right_thumb01")
    right_thumb2 = mc.joint(p=(0.8, 1.0, 1.3), n="right_thumb02")
    right_thumb3 = mc.joint(p=(2.4, 0.3,-0.6), n="right_thumb03")
    
    
    right_index1 = mc.joint(p=(1.5, 0.0, 1.4), n="right_index01")
    right_index2 = mc.joint(p=(2.4, -0.5 ,0.3), n="right_index02")
    right_index3 = mc.joint(p=(1.7, -0.2, 0.1), n="right_index03")
    right_index4 = mc.joint(p=(1.0, -0.0, 0.0), n="right_index04")
    
    
    right_middle1 = mc.joint(p=(1.4, 0.0, 0.1), n="right_middle01")
    right_middle2 = mc.joint(p=(2.4, -0.3, 0.0), n="right_middle02")
    right_middle3 = mc.joint(p=(2.3, -0.1, 0.2), n="right_middle03")
    right_middle4 = mc.joint(p=(1.2, -0.1, 0.0), n="right_middle04")
    
    
    right_ring1 = mc.joint(p=(1.4, 0.0, -0.4), n="right_ring01")
    right_ring2 = mc.joint(p=(2.2, -0.0, -0.2), n="right_ring02")
    right_ring3 = mc.joint(p=(2.1, -0.2, 0.0), n="right_ring03")
    right_ring4 = mc.joint(p=(1.0, 0.0, 0.0), n="right_ring04")
    
    
    right_pinky1 = mc.joint(p=(1.6, 0.0, -1.7), n="right_pinky01")
    right_pinky2 = mc.joint(p=(2.0, -0.1, 0.2), n="right_pinky02")
    right_pinky3 = mc.joint(p=(1.4, -0.1, 0.0), n="right_pinky03")
    right_pinky4 = mc.joint(p=(0.7, -0.0, -0.0), n="right_pinky04")
    
    
    left_hip1 = mc.joint(p=(-3, 0, 0), n="left_hip01")
    left_knee1 = mc.joint(p=(-3, -7, 0), n="left_knee01")
    left_ankle1 = mc.joint(p=(-3, -14, 0), n="left_ankle01")
    left_foot1 = mc.joint(p=(-3, -16, 0), n="left_foot01")
    left_toe1 = mc.joint(p=(0, 0, 0), n="left_toe01")
    
    
    right_hip1 = mc.joint(p=(3, 0, 0), n="right_hip01")
    right_knee1 = mc.joint(p=(3, -7, 0), n="right_knee01")
    right_ankle1 = mc.joint(p=(3, -14, 0), n="right_ankle01")
    right_foot1 = mc.joint(p=(3, -16, 0), n="right_foot01")
    right_toe1 = mc.joint(p=(0, 0, 0), n="right_toe01")
    
    
    mc.parent("pelvis01", world=True)
    mc.parent("spine01", world=True)
    mc.parent("spine02", world=True)
    mc.parent("spine03", world=True)
    mc.parent("chest01", world=True)
    mc.parent("neck01", world=True)
    mc.parent("head01", world=True)
    
    mc.parent("left_clavicle01", world=True)
    mc.parent("left_shoulder01", world=True)
    mc.parent("left_elbow01", world=True)
    mc.parent("left_wrist01", world=True)
    mc.parent("left_hand01", world=True)
    
    mc.parent("left_thumb01", world=True)
    mc.parent("left_thumb02", world=True)
    mc.parent("left_thumb03", world=True)
    
    mc.parent("left_index01", world=True)
    mc.parent("left_index02", world=True)
    mc.parent("left_index03", world=True)
    mc.parent("left_index04", world=True)
    
    mc.parent("left_middle01", world=True)
    mc.parent("left_middle02", world=True)
    mc.parent("left_middle03", world=True)
    mc.parent("left_middle04", world=True)
    
    mc.parent("left_ring01", world=True)
    mc.parent("left_ring02", world=True)
    mc.parent("left_ring03", world=True)
    mc.parent("left_ring04", world=True)
    
    mc.parent("left_pinky01", world=True)
    mc.parent("left_pinky02", world=True)
    mc.parent("left_pinky03", world=True)
    mc.parent("left_pinky04", world=True)

    mc.parent("left_hip01", world=True)
    mc.parent("left_knee01", world=True)
    mc.parent("left_ankle01", world=True)
    mc.parent("left_foot01", world=True)
    mc.parent("left_toe01", world=True)
    
    mc.parent("right_clavicle01", world=True)
    mc.parent("right_shoulder01", world=True)
    mc.parent("right_elbow01", world=True)
    mc.parent("right_wrist01", world=True)
    mc.parent("right_hand01", world=True)
    
    mc.parent("right_thumb01", world=True)
    mc.parent("right_thumb02", world=True)
    mc.parent("right_thumb03", world=True)
    
    mc.parent("right_index01", world=True)
    mc.parent("right_index02", world=True)
    mc.parent("right_index03", world=True)
    mc.parent("right_index04", world=True)
    
    mc.parent("right_middle01", world=True)
    mc.parent("right_middle02", world=True)
    mc.parent("right_middle03", world=True)
    mc.parent("right_middle04", world=True)
    
    mc.parent("right_ring01", world=True)
    mc.parent("right_ring02", world=True)
    mc.parent("right_ring03", world=True)
    mc.parent("right_ring04", world=True)
    
    mc.parent("right_pinky01", world=True)
    mc.parent("right_pinky02", world=True)
    mc.parent("right_pinky03", world=True)
    mc.parent("right_pinky04", world=True)

    mc.parent("right_hip01", world=True)
    mc.parent("right_knee01", world=True)
    mc.parent("right_ankle01", world=True)
    mc.parent("right_foot01", world=True)
    mc.parent("right_toe01", world=True)
   
    
    
    mc.move(0, 61.8, -0.5, "root_joint")
    
    
    mc.move(0, 62.3, -0.5, "pelvis01")
    mc.move(0, 71.7, -0.0, "spine01")
    mc.move(0, 78.4, 0.8, "spine02")
    mc.move(0, 84.0, 0.1, "spine03")
    mc.move(0, 91.2, -2.9, "chest01")
    
    
    
    mc.move(0, 98.6, -4.4, "neck01")
    mc.move(0, 108.3, -0.0, "head01")
    mc.move(0, 127.7, -0.3, "head02")
    
    
    mc.move(4.3, 97.5, -3.6, "left_clavicle01")
    mc.move(10.9, 96.7, -3.5, "left_shoulder01")
    mc.move(28.1, 96.0, -6.0, "left_elbow01")
    mc.move(50, 95.8, 1.1, "left_wrist01")
    mc.move(52.6, 95.9, 1.9, "left_hand01")
    
    
    mc.move(51.3, 95.8, 3.4, "left_thumb01")
    mc.move(51.6, 95.1, 5.2, "left_thumb02")
    mc.move(53.9, 94.1, 7.3, "left_thumb03")
    
    
    mc.move(53.4, 96.1, 3.9, "left_index01")
    mc.move(55.5, 95.7, 5.2, "left_index02")
    mc.move(57.9, 95.6, 7.5, "left_index03")
    mc.move(59.5, 95.6, 9.1, "left_index04")
    
    
    mc.move(53.8, 96.0, 2.7, "left_middle01")
    mc.move(56.1, 95.7, 3.8, "left_middle02")
    mc.move(59.8, 95.6, 5.8, "left_middle03")
    mc.move(62.1, 95.5, 7.0, "left_middle04")
    
    
    mc.move(54.1, 95.9, 2.2, "left_ring01")
    mc.move(56.3, 95.9, 2.5, "left_ring02")
    mc.move(59.9, 95.7, 3.4, "left_ring03")
    mc.move(62.1, 95.3, 3.9, "left_ring04")
    
    
    mc.move(54.8, 95.7, 1.0, "left_pinky01")
    mc.move(56.8, 95.6, 1.3, "left_pinky02")
    mc.move(59.8, 95.5, 1.4, "left_pinky03")
    mc.move(61.2, 95.4, 1.5, "left_pinky04")
    
    
    
    mc.move(-4.3, 97.5, -3.6, "right_clavicle01")
    mc.move(-10.9, 96.7, -3.5, "right_shoulder01")
    mc.move(-28.1, 96.0, -6.0, "right_elbow01")
    mc.move(-50.2, 95.8, 1.1, "right_wrist01")
    mc.move(-52.6, 95.9, 1.9, "right_hand01")
    
    
    mc.move(-51.3, 95.8, 3.4, "right_thumb01")
    mc.move(-51.6, 95.3, 5.2, "right_thumb02")
    mc.move(-53.8, 94.1, 7.2, "right_thumb03")
    
    
    mc.move(-53.4, 96.1, 3.9, "right_index01")
    mc.move(-55.5, 95.6, 5.2, "right_index02")
    mc.move(-57.9, 95.5, 7.5, "right_index03")
    mc.move(-59.5, 95.5, 9.1, "right_index04")
    
    
    mc.move(-53.8, 96.0, 2.7, "right_middle01")
    mc.move(-56.1, 95.7, 3.8, "right_middle02")
    mc.move(-59.8, 95.6, 5.8, "right_middle03")
    mc.move(-62.1, 95.5, 7.0, "right_middle04")
    
   
    mc.move(-54.1, 95.9, 2.2, "right_ring01")
    mc.move(-56.3, 95.9, 2.5, "right_ring02")
    mc.move(-59.7, 95.7, 3.4, "right_ring03")
    mc.move(-62.1, 95.3, 3.9, "right_ring04")
    
    
    mc.move(-54.8, 95.7, 1.0, "right_pinky01")
    mc.move(-56.8, 95.6, 1.3, "right_pinky02")
    mc.move(-59.5, 95.5, 1.4, "right_pinky03")
    mc.move(-61.2, 95.4, 1.5, "right_pinky04")
    
    
    mc.move(4.7, 62.3, -0.5, "left_hip01")
    mc.move(4.7, 35.5, 3.8, "left_knee01")
    mc.move(4.8, 5.5, -0.8, "left_ankle01")
    mc.move(6.0, 1.3, 7.2, "left_foot01")
    mc.move(6.0, 1.2, 13.7, "left_toe01")
    
    
    mc.move(-4.7, 62.3, -0.5, "right_hip01")
    mc.move(-4.7, 35.5, 3.8, "right_knee01")
    mc.move(-4.8, 5.5, -0.8, "right_ankle01")
    mc.move(-6.0, 1.3, 7.2, "right_foot01")
    mc.move(-6.0, 1.2, 13.7, "right_toe01")
    
    
    mc.parent("pelvis01", "root_joint")
    mc.parent("spine01", "pelvis01")
    mc.parent("spine02", "spine01")
    mc.parent("spine03", "spine02")
    mc.parent("chest01", "spine03" )
    mc.parent("neck01",  "chest01")
    mc.parent("head01", "neck01")
    
    mc.parent("left_clavicle01", "chest01")
    mc.parent("left_shoulder01", "left_clavicle01")
    mc.parent("left_elbow01", "left_shoulder01")
    mc.parent("left_wrist01", "left_elbow01")
    mc.parent("left_hand01", "left_wrist01")
    
    mc.parent("left_thumb01", "left_hand01")
    mc.parent("left_thumb02", "left_thumb01")
    mc.parent("left_thumb03", "left_thumb02")
    
    mc.parent("left_index01", "left_hand01")
    mc.parent("left_index02", "left_index01")
    mc.parent("left_index03", "left_index02")
    mc.parent("left_index04", "left_index03")
    
    mc.parent("left_middle01", "left_hand01")
    mc.parent("left_middle02", "left_middle01")
    mc.parent("left_middle03", "left_middle02")
    mc.parent("left_middle04", "left_middle03")
    
    mc.parent("left_ring01", "left_hand01")
    mc.parent("left_ring02", "left_ring01")
    mc.parent("left_ring03", "left_ring02")
    mc.parent("left_ring04", "left_ring03")
    
    mc.parent("left_pinky01", "left_hand01")
    mc.parent("left_pinky02", "left_pinky01")
    mc.parent("left_pinky03", "left_pinky02")
    mc.parent("left_pinky04", "left_pinky03")

    mc.parent("left_hip01", "pelvis01")
    mc.parent("left_knee01", "left_hip01")
    mc.parent("left_ankle01", "left_knee01")
    mc.parent("left_foot01", "left_ankle01")
    mc.parent("left_toe01", "left_foot01")
    
    mc.parent("right_clavicle01", "chest01")
    mc.parent("right_shoulder01", "right_clavicle01")
    mc.parent("right_elbow01", "right_shoulder01")
    mc.parent("right_wrist01", "right_elbow01")
    mc.parent("right_hand01", "right_wrist01")
    
    mc.parent("right_thumb01", "right_hand01")
    mc.parent("right_thumb02", "right_thumb01")
    mc.parent("right_thumb03", "right_thumb02")
    
    mc.parent("right_index01", "right_hand01")
    mc.parent("right_index02", "right_index01")
    mc.parent("right_index03", "right_index02")
    mc.parent("right_index04", "right_index03")
    
    mc.parent("right_middle01", "right_hand01")
    mc.parent("right_middle02", "right_middle01")
    mc.parent("right_middle03", "right_middle02")
    mc.parent("right_middle04", "right_middle03")
    
    mc.parent("right_ring01", "right_hand01")
    mc.parent("right_ring02", "right_ring01")
    mc.parent("right_ring03", "right_ring02")
    mc.parent("right_ring04", "right_ring03")
    
    mc.parent("right_pinky01", "right_hand01")
    mc.parent("right_pinky02", "right_pinky01")
    mc.parent("right_pinky03", "right_pinky02")
    mc.parent("right_pinky04", "right_pinky03")

    mc.parent("right_hip01", "pelvis01")
    mc.parent("right_knee01", "right_hip01")
    mc.parent("right_ankle01", "right_knee01")
    mc.parent("right_foot01", "right_ankle01")
    mc.parent("right_toe01", "right_foot01")
    
    
window = mc.window("dumWin0",title= "Neon Maya Script Basic Skeleton Rig Ver0.1", widthHeight=(300, 200))

mc.columnLayout(adj=True)

mc.separator(height=50)

mc.setParent("..")

mc.columnLayout(columnAlign="center", width=100)

mc.text(label="Create a skeleton rig by clicking the button below.")

rig_button = mc.button(label = "Basic Skeleton Rigs", command = basicRig, width=100)

mc.setParent("..")

mc.separator(height=50)



window_width = mc.window(window, q=True, width=True)

button_width = mc.button(rig_button, q=True, width=True)

mc.button(rig_button, e=True, width=min(window_width -40, button_width))

mc.showWindow(window)




