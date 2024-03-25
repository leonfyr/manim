from manim import *
import os

class Transverse(Scene):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        self.position_path = os.path.join(os.getcwd(),"positions_trans.txt")

    def construct(self):
        timer = ValueTracker(0.0)

        def readData():
            global fps,t,n,data,o
            with open(self.position_path,"r") as f:
                data = f.read().split("\n")[:-1]
            fps = float(data[0].split(" ")[0])
            t   = float(data[0].split(" ")[1])
            o = float(data[0].split(" ")[2])
            data = data[1:]
            data = [i.split(" ")[:-1] for i in data]
            n = len(data[0])

        def get_current_time():
            time = int(float(timer.get_value())*fps)
            try:
                len(data[time][0])
            except:
                time -= 1
            return time
        
        def circles_updator(mobj):
            for i in range(len(mobj)):
                j=get_current_time()
                mobj[i].move_to(LEFT*6.5+RIGHT*i*o+UP*float(data[j][i])+DOWN*0.5)
        
        readData()

        circles = VGroup()
        for i in range(n):
            circles.add(Dot().set_fill(RED,opacity=1))

        circles.add_updater(circles_updator)

        Title = Text("Transverse Wave").move_to(UP*3)

        self.add(circles)

        self.play(FadeIn(Title))

        self.play(timer.animate.set_value(t),run_time=t, rate_func=linear)

