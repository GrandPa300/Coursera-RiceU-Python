# Mini Proj Prep 07
# ------------------
# Space Ship

import simplegui
import random
import math

# global values for user interface

WIDTH = 800
HEIGHT = 600
LIVES = 3
SCORE = 0
FRICTION = 0.1
ACC = 1
MISSILE_VEL = 1

time = 0 
missile_count = 0

# helper functions
def deg2rad(deg):
    return (deg/-180.0)*(math.pi)

def ang2vec(ang):
    return [math.cos(ang), math.sin(ang)]

# define ImageInfo Class to obtain info of image
class ImageInfo:
    def __init__(self, center, size, radius = 0, 
                 life_span = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if life_span:
            self.life_span = life_span
        else:
            self.life_span = float('inf')
        self.animated = animated
        
    def get_center(self):
        return self.center
    
    def get_size(self):
        return self.size
    
    def get_radius(self):
        return self.radius
    
    def get_life_span(self):
        return  self.life_span
    
    def get_animated(self):
        return self.animated

# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image\
              ("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris1_brown.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image\
               ("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2013.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image\
               ("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image\
             ("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 75)
missile_image = simplegui.load_image\
                ("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot1.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image\
                 ("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image\
                  ("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound\
             ("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound\
                ("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
thrust_sound = simplegui.load_sound\
                    ("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound\
                  ("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

missile_sound.set_volume(.3)
thrust_sound.set_volume(.3)

# define Ship Class:
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = deg2rad(angle) # angle in degree
        self.angle_vel = deg2rad(0) # angle in degree
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def __str__(self):
        return 'pos = ' + str(self.pos) + '\n' +\
               'vel = ' + str(self.vel) + '\n' +\
               'ang = ' + str(float(self.angle)/(math.pi)*180) + '\n' +\
               'cnt = ' + str(self.image_center) + '\n' +\
               'siz = ' + str(self.image_size)
        
    def draw(self, canvas):
        if self.thrust:
            canvas.draw_image(self.image, [135, 45], self.image_size,\
                                          self.pos, self.image_size, self.angle)
            
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, \
                                          self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        
        self.pos[0] += self.vel[0]
        self.pos[0] = self.pos[0] % WIDTH
        self.pos[1] += self.vel[1]
        self.pos[1] = self.pos[1] % HEIGHT
        
        if self.thrust:
            acceration = ACC
                   
        else:
            acceration = 0 
        
        self.vel[0] += (ang2vec(self.angle)[0]*acceration)
        self.vel[1] += (ang2vec(self.angle)[1]*acceration)
        self.vel[0] *= (1- FRICTION)
        self.vel[1] *= (1- FRICTION)
   
    def boost(self, boost):       
        self.thrust = boost 
        
        if self.thrust:
            thrust_sound.rewind()
            thrust_sound.play()
            
        else: 
            thrust_sound.pause()
    
    def shoot(self):
        global missile_set, missile_count
        projection = ang2vec(self.angle)
        missile_pos = [self.pos[0] + self.radius * projection[0], \
                       self.pos[1] + self.radius * projection[1]]
        missile_vel = [self.vel[0] + MISSILE_VEL * projection[0],\
                       self.vel[1] + MISSILE_VEL * projection[1]]
        
        if missile_count <= 4:
            missile_set.add(Sprite(missile_pos, missile_vel, self.angle, 0, \
                         missile_image, missile_info, missile_sound))
            missile_count += 1
        
        else:
            # add a cap to missiles, max is 5 (0 - 4)
            # when hit max missile number, pop one missile from set, reduce count by 1
            missile_set.pop() 
            missile_count -= 1
            
    
    def clk_wise_trun(self, angular_vel):
        self.angle_vel = -deg2rad(angular_vel)
        
    def cclk_wise_trun(self, angular_vel):
        self.angle_vel = deg2rad(angular_vel)

class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.life_span = info.get_life_span()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
    
    def __str__(self):
        return 'asteroid_pos = ' + str(self.pos) + '\n' +\
               'asteroid_vel = ' + str(self.vel) + '\n' +\
               'asteroid_ang = ' + str(float(self.angle)/(math.pi)*180) + '\n' +\
               'asteroid_ang_vel = ' + str(float(self.angle)/(math.pi)*180) + '\n' +\
               'asteroid_cnt = ' + str(self.image_center) + '\n' +\
               'asteroid_siz = ' + str(self.image_size)

    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, \
                                          self.pos, self.image_size, self.angle)

    def update(self):
        self.angle += self.angle_vel
        
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

def draw(canvas):
    global time

    # animiate background
    time += 1
    wtime = (time / 3) % WIDTH
    # debris moves 1 pixel every 3 ticks (1/60 s)
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), \
                      [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    for missile in missile_set:
        missile.life_span -= 1 
        if missile.life_span > 0:
            missile.draw(canvas)
        missile.update()
    space_ship.draw(canvas)
    space_ship.update()
    asteroid.draw(canvas)
    asteroid.update()
    
# asteroid refresh
def asteroid_refresh():
    global asteroid
    random_num = (-5,-4,-3,-2,-1,1,2,3,4,5)
    asteroid_cnt = [random.randrange(WIDTH), random.randrange(HEIGHT)]
    asteroid_dir = [random.choice(random_num)/10.0, random.choice(random_num)/10.0]
    asteroid = Sprite(asteroid_cnt, asteroid_dir, 0, deg2rad(0.5), asteroid_image, asteroid_info)
    return asteroid  
    
# initialize object

space_ship = Ship([400, 300], [0, 0], 0, ship_image, ship_info)
asteroid_refresh()
missile_set = set([])

# key handler
def down(key):
    if key == simplegui.KEY_MAP['left']:
        space_ship.clk_wise_trun(5)
    elif key == simplegui.KEY_MAP['right']:
        space_ship.cclk_wise_trun(5)
    elif key == simplegui.KEY_MAP['up']:
        space_ship.boost(True)
    elif key == simplegui.KEY_MAP['space']:
        space_ship.shoot()
        
def up(key):
    if key == simplegui.KEY_MAP['left']:
        space_ship.cclk_wise_trun(0)
    elif key == simplegui.KEY_MAP['right']:
        space_ship.clk_wise_trun(0)
    elif key == simplegui.KEY_MAP['up']:
        space_ship.boost(False)

# initialize frame
frame = simplegui.create_frame('Space Ship', WIDTH, HEIGHT)

# register handler
frame.set_draw_handler(draw)
frame.set_keydown_handler(down)
frame.set_keyup_handler(up)
timer = simplegui.create_timer(10000, asteroid_refresh)

# start frame and timer
frame.start()
timer.start()