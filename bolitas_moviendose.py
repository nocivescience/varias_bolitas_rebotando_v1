from manim import *
import itertools as it
class Eter(Scene):
    conf={
        'n_part':60,
        'colors':[GREEN,YELLOW,BLUE,RED,PURPLE,WHITE]
    }
    def construct(self):
        self.get_wind(False)
        self.wait(5)
    def get_wind(self,horizontal=True):
        setColor=it.cycle(self.conf['colors'])
        dots=VGroup()
        positions=np.array([
            [np.random.uniform(-config['frame_width']/2,config['frame_width']/2),np.random.uniform(-config['frame_height']/2,config['frame_height']/2),0] for _ in range(self.conf['n_part'])
        ])
        for pos in positions:
            radio=np.random.random()
            if radio<0.5:
                radio=0.5
            dot=Dot(radius=radio/2).move_to(pos)
            dot.set_color(next(setColor))
            if horizontal:
                velocity=np.random.random()*RIGHT*3
            else:
                velocity=np.random.random()*DOWN*3
            dot.velocity=velocity
            dots.add(dot)
        def get_update(dots,dt):
            for dot in dots:
                dot.acceleration=np.array([0,-5,0])
                dot.velocity=dot.velocity+dot.acceleration*dt
                textos=self.inner_text(dot,'a')
                dot.shift(dot.velocity)
                if horizontal:
                    if dot.get_center()[0]+dot.radius>config['frame_width']/2:
                        dot.velocity[0]=-np.abs(dot.velocity[0])
                    elif dot.get_center()[0]-dot.radius<-config['frame_width']/2:
                        dot.velocity[0]=np.abs(dot.velocity[0])
                else:
                    if dot.get_center()[1]+dot.radius>config['frame_height']/2:
                        dot.velocity[1]=-np.abs(dot.velocity[1])
                    elif dot.get_center()[1]-dot.radius<-config['frame_height']/2:
                        dot.velocity[1]=np.abs(dot.velocity[1])
                self.add(textos)
        dots.add_updater(get_update)
        self.add(dots)
    def inner_text(self,ball,number):
        texto=Tex(number).set_height(ball.radius) #no use Text porque no resilta
        texto.add_updater(lambda t: t.move_to(ball.get_center()))
        texto.set_color(BLACK)
        return texto