from manim import *
import numpy as np

def verteilungsfunktion(x):
    if x < 2:
        return 0
    if x >= 2 and x < 3:
        return 0.1
    if x >= 3 and x < 4:
        return 0.2
    if x >= 4 and x < 5:
        return 0.4
    if x >= 5 and x < 8:
        return 0.7
    if x >= 8 and x < 9:
        return 0.9
    if x >= 9:
        return 1

class Titel(Scene):
    def construct(self):
        title = Text("Übung 10, Statistik 1")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"Verteilungsfunktion", r"Erwartungswert", r"Varianz", r"stetige Zufallsvariablen").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 3)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 10.1")

        t1 = Tex(r"Gegeben ist folgende Verteilungsfunktion:").scale(0.7)
        formula = MathTex(r"F(x)=\begin{cases}0 & \text{für } x < 1\\ 0.2 & \text{für } 1 \le x < 3\\ 0.5 & \text{für } 3 \le x < 7\\ 1 & \text{für } 7 \le x\end{cases}").scale(0.7)
        list = BulletedList(r"Wie lautet die zugehörige Wahrscheinlichkeitsfunktion? Bitte graphisch darstellen.",
        r"Bestimmen Sie die Wahrscheinlichkeiten $\mathbb{P}(1 \le X < 3)$, $\mathbb{P}(0 \le X < 3)$, $\mathbb{P}(1 \le X < 4)$ und $\mathbb{P}(1 < X < 7)$!",
        r"Berechnen Sie den Erwartungswert und die Varianz!").scale(0.7)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        formula.next_to(t1, direction = DOWN)
        list.next_to(formula, direction = DOWN).shift(3*RIGHT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1))
        self.play(Write(formula))
        self.play(Write(list), run_time = 4.5)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1), FadeOut(formula), FadeOut(list))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 10.2")

        t1 = VGroup(Tex(r"Die folgende Tabelle zeigt die Wahrscheinlichkeit für die Gewinne des"),
        Tex(r"\textit{RealProfit} Unternehmens im nächsten Jahr:")).scale(0.7)
        table = Tex(r"\begin{tabular}{c|ccccccc} \hline Gewinn $x$ & -10 000 & 0 & 5 000 & 10 000 & 15 000 & 20 000 & sonst \\ $\mathbb{P}(X=x)$ & & 0.2 & 0.1 & 0.25 & 0.1 & & 0 \\ \hline\end{tabular}").scale(0.7)
        list = BulletedList(r"Ergänzen Sie die fehlenden Werte so, dass das Unternehmen \textit{RealProfit} mit der Wahrscheinlichkeit 0.75 profitabel arbeitet (positiven Gewinn erwirtschaftet)!",
        r"Wie groß ist die Wahrscheinlichkeit für einen negativen Gewinn?",
        r"Bestimmen Sie den erwarteten Gewinn!",
        r"Berechnen Sie die Varianz der Zufallsvariable $X$!").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        table.next_to(t1, direction = DOWN)
        list.next_to(table, direction = DOWN).shift(0.75*RIGHT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 2)
        self.play(Write(table))
        self.play(Write(list), run_time = 6)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(table), FadeOut(list), FadeOut(ueberschrift))

class Aufgabe3(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=-1,
            x_max=11,
            y_min=0,
            y_max=1,
            x_axis_config={"tick_frequency": 1},
            y_axis_config={"tick_frequency": 0.1, "decimal_number_config": {"num_decimal_places": 1}},
            x_labeled_nums=np.array([-1,0,1,2,3,4,5,6,7,8,9,10,11]),
            y_labeled_nums=np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]),
            x_axis_label="$x$",
            y_axis_label="$F$",
            x_axis_width = 9 * 0.7,
            y_axis_height = 6 * 0.7,
            graph_origin = 4 * LEFT + 3 * DOWN,
            **kwargs
        )

    def construct(self):
        ueberschrift = Title("Aufgabe 10.3")

        t1 = Tex(r"Gegeben ist folgende grafische Darstellung einer Verteilungsfunktion:").scale(0.7)

        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)


        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1))
        self.setup_axes(animate = True)
        graph = self.get_graph(verteilungsfunktion)
        graph.make_jagged()
        self.play(Create(graph))
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(graph), FadeOut(self.axes))

        t2 = Tex(r"Bestimmen Sie die folgenden Wahrscheinlichkeiten:").scale(0.7)
        list = BulletedList(r"$\mathbb{P}(X \le 5)$",
        r"$\mathbb{P}(X = 5)$",
        r"$\mathbb{P}(X = 10)$",
        r"$\mathbb{P}(4.5 < X < 5.5)$",
        r"$\mathbb{P}(4.5 < X < 7.5)$",
        r"$\mathbb{P}(5 < X < 8)$",
        r"$\mathbb{P}(-1 \le X < 10)$",
        r"$\mathbb{P}(-1 \le X < 9)$").scale(0.7)
        t2.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t2, direction = DOWN, aligned_edge = LEFT)

        self.wait(1)
        self.play(Write(t2))
        self.play(Write(list), run_time = 4)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t2), FadeOut(list))

class Aufgabe4(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 10.4")

        t1 = Tex(r"$X$ sei eine stetige Zufallsvariable mit der Dichte").scale(0.7)
        formula = MathTex(r"f(x) = \begin{cases}cx(1-x) & \text{für } 0\le x \le 1 \\ 0 & \text{sonst}\end{cases}").scale(0.7)
        list = BulletedList(r"Bestimmen Sie die Konstante $c$!",
        r"Wie lautet die Verteilungsfunktion $F$ der Zufallsvariablen $X$?",
        r"Berechnen Sie $\mathbb{P}\left(X\le \frac{1}{2}\right)$, $\mathbb{P}\left(X> \frac{2}{3}\right)$, $\mathbb{P}\left(\frac{1}{2} < X \le \frac{2}{3}\right)$, $\mathbb{P}\left(2 < X \le 3\right)$",
        r"Berechnen Sie $\mathbb{E}(X)$ und Var$(X)$!").scale(0.7)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        formula.next_to(t1, direction = DOWN)
        list.next_to(formula, direction = DOWN).shift(1.5*RIGHT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1))
        self.play(Write(formula))
        self.play(Write(list), run_time = 6)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1), FadeOut(formula), FadeOut(list))

class Aufgabe5(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 10.5")

        t1 = Tex(r"Für eine stetige Zufallsvariable $X$ gilt:").scale(0.7)
        formula = MathTex(r"F(x) = \begin{cases}0 & \text{für } x < 0 \\ 0.2\cdot x^2 & \text{für } 0 \le x < 1 \\ -0.05\cdot x^2 + 0.5\cdot x - 0.25 & \text{für } 1 \le x < 5 \\ 1 & \text{für } x \ge 5\end{cases}").scale(0.7)
        t2 = VGroup(Tex(r"Ermitteln Sie die zugehörige Dichte $f(x)$. Berechnen Sie den Erwartungswert"),
        Tex(r"sowie die Varianz von $X$.")).scale(0.7)
        t2.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        formula.next_to(t1, direction = DOWN).shift(2*RIGHT)
        t2.next_to(formula, direction = DOWN).shift(RIGHT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1))
        self.play(Write(formula))
        self.play(Write(t2), run_time = 2)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1), FadeOut(formula), FadeOut(t2))

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
