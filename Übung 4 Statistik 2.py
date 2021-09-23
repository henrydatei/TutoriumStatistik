from typing_extensions import runtime
from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 4, Statistik 2")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"Methode der kleinsten Quadrate", r"Regression").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 2)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 4.1")

        t1 = Tex(r"Man möchte online einen Sitzplatz für einen Flug reservieren. Es gibt je drei Plätze links und rechts vom Gang. Angenommen, man bekommt einen Platz zufällig zugewiesen. Ein Manager ist im letzten Monat zehn Mal geflogen, davon vier Mal am Fenster, fünf Mal am Gang und ein Mal in der Mitte. Laut den Regeln der Flugfirma ist die Wahrscheinlichkeit, einen Fensterplatz zu ergattern, gleich der Wahrscheinlichkeit einen Platz am Gang zu bekommen, und beträgt $p$. Die Wahrscheinlichkeit in der Mitte zu sitzen, ist demnach $1 - 2p$. Schätzen Sie $p$ mit der kleinsten Quadrate Methode.", tex_environment = "flushleft").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 8)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(ueberschrift))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 4.2")

        t1 = Tex(r"Sechs Kunden einer Bäckerei wurden nach ihrer Körpergröße und ihrem Gewicht gefragt. Man erhielt folgendes Ergebnis", tex_environment = "flushleft").scale(0.7)
        table = IntegerTable([[164,171,186,179,161,174],[74,73,89,83,60,80]], row_labels = [Tex(r"Körpergröße $x_i$"), Tex(r"Gewicht $y_i$")]).scale(0.7)
        list = BulletedList(r"Stellen Sie die Daten graphisch dar!",
        r"Ermitteln Sie die Regressionsgerade von $Y$ bezüglich $X$.",
        r"Zeichnen Sie die Regressionsgerade sowie die Fehler des Models in die Abbildung!",
        r"Wie ist das erwartete Gewicht bei einer Körpergröße von 170?").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        table.next_to(t1, direction = DOWN, aligned_edge = LEFT)
        list.next_to(table, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 2)
        self.play(Write(table), run_time = 3)
        self.play(Write(list), run_time = 4)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list), FadeOut(table), FadeOut(ueberschrift))

class Aufgabe3(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 4.3")

        t1 = Tex(r"Man kann die Abhängigkeit zwischen der Anzahl der Fahrzeugen pro Minute (Variable $y$) auf der Straße und der Zeit (Variable $x$) zwischen 6-10 Uhr mit folgender Formel", tex_environment = "flushleft").scale(0.7)
        formel = MathTex(r"y_i = \kappa + 16x_i - x_i^2 + \varepsilon_i\quad \kappa\ge -60").scale(0.7)
        t2 = Tex(r"beschreiben, wobei die $\varepsilon_i$ die i.i.d. Störterme sind. Schätzen Sie das Modell anhand der folgenden Tabelle:", tex_environment = "flushleft").scale(0.7)
        table = MathTable([["6:00","7:00","7:30","7:45","8:00","8:45","9:15"],["6","9","8","10","11","9","5"]], row_labels = [Tex(r"$x_i$"), Tex(r"$y_i$")]).scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        formel.next_to(t1, direction = DOWN)
        t2.next_to(t1, direction = 4*DOWN, aligned_edge = LEFT)
        table.next_to(t2, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 3)
        self.play(Write(formel), run_time = 1)
        self.play(Write(t2), run_time = 2)
        self.play(Write(table), run_time = 3)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(t2), FadeOut(formel), FadeOut(table), FadeOut(ueberschrift))

class Aufgabe4(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 4.4")

        t1 = Tex(r"Man untersucht die Abhängigkeit zwischen dem Alter eines Autos und seinem relativen Restwert (= Verkaufspreis/Preis des neuen Autos). Die Ergebnisse sind in der folgenden Tabelle zusammengefasst", tex_environment = "flushleft").scale(0.7)
        table1 = DecimalTable([[3.1,9,8,8.2,0,10,5,1,7,8.9],[0.49,0.12,0.14,0.15,1.00,0.05,0.29,0.78,0.17,0.10]], element_to_mobject_config = {"num_decimal_places":2}, row_labels = [Tex(r"Alter in Jahren $x_i$"), Tex(r"rel. Restwert $y_i$")]).scale(0.45)
        table2 = DecimalTable([[3.4,7.5,5.9,8.6,2,8.7,6.3,1.3,8.4,9.3],[0.43,0.15,0.24,0.11,0.62,0.08,0.2,0.71,0.13,0.03]], element_to_mobject_config = {"num_decimal_places":2}, row_labels = [Tex(r"Alter in Jahren $x_i$"), Tex(r"rel. Restwert $y_i$")]).scale(0.45)
        t2 = Tex(r"und sind graphisch dargestellt").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        table1.next_to(t1, direction = DOWN, aligned_edge = LEFT)
        table2.next_to(table1, direction = DOWN, aligned_edge = LEFT)
        t2.next_to(table2, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 3)
        self.play(Write(table1), run_time = 3)
        self.play(Write(table2), run_time = 3)
        self.play(Write(t2), run_time = 1)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(table1), FadeOut(table2), FadeOut(t2))

        ax = Axes(x_range=[0, 10, 1], y_range=[0, 1, 0.1], y_length = 5.5).shift(0.5*DOWN)
        xlabel = ax.get_x_axis_label(Text("Alter").scale(0.5), edge = DOWN, direction = DOWN)
        ylabel = ax.get_y_axis_label(Text("Werteverfall").scale(0.5).rotate(90*DEGREES), edge = LEFT, direction = LEFT)
        xvalues = [3.1,9,8,8.2,0,10,5,1,7,8.9,3.4,7.5,5.9,8.6,2,8.7,6.3,1.3,8.4,9.3]
        yvalues = [0.49,0.12,0.14,0.15,1.00,0.05,0.29,0.78,0.17,0.10,0.43,0.15,0.24,0.11,0.62,0.08,0.2,0.71,0.13,0.03]

        self.play(Write(ax), Write(xlabel), Write(ylabel))
        allDots = []
        for x, y in zip(xvalues,yvalues):
            point = ax.coords_to_point(x, y)
            dot = Dot(point, color = BLUE_D)
            allDots.append(dot)
            self.play(GrowFromCenter(dot), run_time = 0.15)

        self.wait(2)
        self.play(FadeOut(ax), FadeOut(xlabel), FadeOut(ylabel), FadeOut(VGroup(*allDots)))

        t3 = Tex(r"Man vermutet eine exponentielle Abhängigkeit zwischen $Y$ und $X$. Schätzen Sie die Koeffizienten des Models", tex_environment = "flushleft").scale(0.7)
        formel = MathTex(r"y_i = \beta_0\cdot e^{\beta_1 x_i + \varepsilon_i}").scale(0.7)
        t4 = Tex(r"wobei die $\varepsilon_i$ die i.i.d Störterme sind. Aus den Daten ergeben sich die folgenden Zwischenergebnisse: $\sum_{i=1}^{20} x_i = 121.6$, $\sum_{i=1}^{20} \log(y_i) = -32.131$, $\sum_{i=1}^{20} x_i^2 = 930.76$, $\sum_{i=1}^{20} \log(y_i)^2 = 68.473$, $\sum_{i=1}^{20} x_i\cdot\log(y_i) = -249.635$", tex_environment = "flushleft").scale(0.7)
        t3.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        formel.next_to(t3, direction = DOWN)
        t4.next_to(t3, direction = 4*DOWN, aligned_edge = LEFT)
        
        self.play(Write(t3), run_time = 1.5)
        self.play(Write(formel))
        self.play(Write(t4), run_time = 3)
        self.wait(2)
        self.play(FadeOut(t3), FadeOut(t4), FadeOut(formel), FadeOut(ueberschrift))

class Ende(Scene):
    def construct(self):
        text = Text("Viel Erfolg!")
        subtext = Tex(r"Fragen $\to$ Forum").scale(0.7)
        subtext.next_to(text, direction = DOWN)

        self.play(Write(text))
        self.wait(1)
        self.play(Write(subtext))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(subtext))

class Trenner(Scene):
    def construct(self):
        self.wait(0.5)
