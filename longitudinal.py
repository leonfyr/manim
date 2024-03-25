from manim import *
import os

class Longitudinal(Scene):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        self.position_path = os.path.join(os.getcwd(),"positions_long.txt")

    def construct(self):
        focus = 10

        timer = ValueTracker(0.0)

        shift = ValueTracker(0.0) #0 to 1.5

        def readData():
            global fps,t,n,data,fpos,original_length

            with open(self.position_path,"r") as f:
                data = f.read().split("\n")[:-1]
            fps = int(data[0].split(" ")[0])
            t   = float(data[0].split(" ")[1])
            data = data[1:]
            data = [i.split(" ")[:-1] for i in data]
            fpos = [i[focus] for i in data]
            n = len(data[0])
            original_length = float(data[0][1]) - float(data[0][0])

        def get_current_time():
            time = int(float(timer.get_value())*fps)
            try:
                len(data[time][0])
            except:
                time -= 1
            return time
            
        ## Updators
        def circles_updater(mobj):
            for i in range(len(mobj)):
                j = get_current_time()
                mobj[i].move_to(LEFT*6.5+RIGHT*float(data[j][i])+UP*shift.get_value())
                
            
        def arrow_updater(mobj):
            j = get_current_time()

            mobj.move_to(
                LEFT*6.5+RIGHT*float(data[j][focus])+UP*0.5
            )
            return mobj

        ## Main programme
        readData()

        circles = VGroup()
        for i in range(n):
            circles.add(Dot().set_fill(RED,opacity=1))

        circles.add_updater(circles_updater)
        
        farr = Arrow(start = DOWN,end=UP*0.5)
            
        farr.add_updater(arrow_updater)

        ftext = MathTex("x_{"+str(focus)+"}",font_size=70)
        ftext.add_updater(
            lambda x:x.next_to(farr,RIGHT)
        )

        Title = Text("Longitudinal Wave").move_to(UP*3)

        y_axis = Line(start=LEFT*5+DOWN*0.5,end=LEFT*5+DOWN*3.5)
        x_axis = Line(start=ORIGIN,end=RIGHT*10).next_to(y_axis,RIGHT,buff=0)
        ytext = MathTex("x_{"+str(focus)+"}",font_size=70).next_to(y_axis,UP)
        xtext = MathTex("t",font_size=70).next_to(x_axis,RIGHT)

        start_time = 5
        graph_time = 5
        graph = VGroup()
        for i in range(graph_time * fps - 1):
            graph.add(Line(start=UP,end=DOWN).set_fill(ORANGE,opacity = 1))
            
        def graph_updater(mobj):
            graph_length = 10
            length = graph_time * fps - 1
            time = get_current_time()
            lines = [-1 for i in range(length)]
            i = time - 1
            while time - graph_time * fps < i:
                if i < start_time * fps:
                    break
                lines[time-1-i] = [float(data[i+1][focus]) - original_length * focus,float(data[i][focus]) - original_length * focus]
                i = i - 1
            #print(lines)
            dx = graph_length / length
            for i in range(len(mobj)):
                if lines[i] == -1:
                    mobj[i].move_to(DOWN*10)
                else:
                    mobj[i].__init__(
                        start = LEFT*5+DOWN*2+dx*i*RIGHT+UP*lines[i][0],
                        end = LEFT*5+DOWN*2+dx*(i+1)*RIGHT+UP*lines[i][1],
                        color = ORANGE
                    )
                
            
        graph.add_updater(graph_updater)

        #self.add(graph)

        #self.add(y_axis,x_axis,xtext,ytext)
        
        self.add(circles)

        self.play(FadeIn(Title))

        # self.add(farr,ftext)

        self.play(timer.animate.set_value(5),run_time=5, rate_func=linear)
        self.play(timer.animate.set_value(6),shift.animate.set_value(1.5),run_time=1, rate_func=linear)
        self.play(timer.animate.set_value(7),FadeIn(y_axis,x_axis,xtext,ytext,farr,ftext,graph,run_time=1), rate_func=linear)
        self.play(timer.animate.set_value(20),run_time=13, rate_func=linear)
        self.remove(ytext,ftext)
        focus = 5
        ytext = MathTex("x_{"+str(focus)+"}",font_size=70).next_to(y_axis,UP)
        ftext = MathTex("x_{"+str(focus)+"}",font_size=70)
        ftext.add_updater(
            lambda x:x.next_to(farr,RIGHT)
        )
        self.add(ytext,ftext)
        self.play(timer.animate.set_value(23),run_time=3,rate_func=linear)
        self.remove(ytext,ftext)
        focus = 7
        ytext = MathTex("x_{"+str(focus)+"}",font_size=70).next_to(y_axis,UP)
        ftext = MathTex("x_{"+str(focus)+"}",font_size=70)
        ftext.add_updater(
            lambda x:x.next_to(farr,RIGHT)
        )
        self.add(ytext,ftext)
        self.play(timer.animate.set_value(26),run_time=3,rate_func=linear)
        self.remove(ytext,ftext)
        focus = 3
        ytext = MathTex("x_{"+str(focus)+"}",font_size=70).next_to(y_axis,UP)
        ftext = MathTex("x_{"+str(focus)+"}",font_size=70)
        ftext.add_updater(
            lambda x:x.next_to(farr,RIGHT)
        )
        self.add(ytext,ftext)
        self.play(timer.animate.set_value(t),run_time=t-26,rate_func=linear)
        # for i in range(len(graph)):
        #     print(i,":",graph[i].start,",",graph[i].end)

    def show_graph(self):
        pass