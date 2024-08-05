from vpython import canvas, box, cylinder, vector, color, rate
import time
scene = canvas(w=800, h=600,background= color.white)
def d_cuboid(pos, length, width, height, color):
    cuboid = box(pos=vector(*pos), length=length, width=width, height=height, color=color)
    return cuboid
def d_cyl(pos, radius, height, color):
    cyl = cylinder(pos = vector(*pos), radius=radius, height =height, color=color)
    return  cyl
def translate(obj, dx, dy, dz):
    obj.pos += vector(dx, dy, dz)
def rotate(obj, angle, axis):
    obj.rotate(angle=angle, axis= vector(*axis))
def scale(obj, sx, sy, sz):
    obj.size = vector(obj.size.x*sx, obj.size.y*sy, obj.size.z*sz)
cuboid = d_cuboid((-2,0,0), 2,2,2, color.blue)
translate(cuboid, 4,0,0)
time.sleep(1)
rotate(cuboid,45, (0,1,0))
time.sleep(1)
scale(cuboid, 1.5,1.5,1.5)
time.sleep(1)
cylinder = d_cyl((5,2,0), 1,10,color.red)
translate(cylinder,0,-2,0)
time.sleep(1)
rotate(cylinder, 45,(0,1,0))
time.sleep(1)
scale(cylinder, 1.5,1.5,1.5)
time.sleep(1)
while True:
    rate(30)
