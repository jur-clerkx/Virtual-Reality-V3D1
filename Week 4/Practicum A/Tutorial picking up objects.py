import viz
import vizact
import vizmat
import viztracker

viz.setMultiSample(4)
viz.fov(60)
viz.go()

piazza = viz.add('piazza.osgb')

#Add crates marker for participant to walk to
crate1 = viz.addChild('crate.osgb',pos=[-0.3,0.3,4],scale=[0.6,0.6,0.6])
crate2 = crate1.clone(pos=[0.35,0.3,4],euler=[5,0,0],scale=[0.6,0.6,0.6])
crate3 = crate1.clone(pos=[0.3,0.9,4.1],euler=[-5,0,0],scale=[0.6,0.6,0.6])

arrow = viz.addChild('arrow.wrl',scale=[0.3,0.3,0.3])

#enable physics and apply shapes
viz.phys.enable() 
piazza.collideMesh()
crate1.collideBox()
crate2.collideBox()
crate3.collideBox()
arrow.collideBox()
arrow.disable( viz.DYNAMICS )
arrow.disable( viz.PHYSICS )

#Link arrow to mousetracker
viewTracker = viztracker.Keyboard6DOF()
viewlink = viz.link( viewTracker, viz.MainView )
viewlink.preTrans([0,1.5,0])
tracker = viztracker.MouseTracker()
trackerlink = viz.link( tracker, arrow )
trackerlink.postTrans([0,0,-5])
closest = None

def updateClosest():
	global closest
	list = viz.phys.intersectNode( arrow )
	
	if list != []:
		
		for object in list:
			if object == piazza:
				list.remove(piazza)

		closestDistance = 999999
			
		arrowPos = arrow.getPosition()
		for object in list:
			distance = vizmat.Distance(arrowPos,object.getPosition())
			if distance < closestDistance:
				closest = object
				closestDistance = distance
	else:
		closest = None
			
				
vizact.onupdate(viz.PRIORITY_DEFAULT,updateClosest)

link = None
grabbedObject = None
def onMouseDown():
	global link, grabbedObject
	if closest is not None:
		link = viz.grab( arrow, closest )
		grabbedObject = closest
		
def onMouseUp():
	global link, grabbedObject
	if grabbedObject is not None:
		link.remove()
		grabbedObject = None
		
vizact.onmousedown( viz.MOUSEBUTTON_LEFT, onMouseDown )
vizact.onmouseup( viz.MOUSEBUTTON_LEFT, onMouseUp )