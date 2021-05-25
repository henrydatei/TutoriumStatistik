from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 12, Statistik 1")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"Randwahrscheinlichkeiten und Randverteilung", r"bedingte Wahrscheinlichkeiten und Dichten", r"Kovarianz und Korrelation").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 3)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 12.1")

        t1 = VGroup(Tex(r"Aus langjähriger Erfahrung ist der Abteilung für Familie und Soziales einer"),
        Tex(r"Stadtverwaltung bekannt, wie sich die gemeinsame Verteilung der Anzahl der"),
        Tex(r"Kinder pro Familie $X_1$ und der Anzahl der PKW pro Familie $X_2$"),
        Tex(r"zusammensetzt. Die gemeinsame Wahrscheinlichkeitsfunktion von $X_1$ und $X_2$"),
        Tex(r"ist gegeben durch:")).scale(0.7)
        table = Tex(r"\begin{tabular}{c|ccc} & \multicolumn{3}{c}{Anzahl der PKW, $X_2$} \\ Anzahl der Kinder, $X_1$ & 1 & 2 & 3 \\ \hline 0 & 0.08 & 0.28& 0.01 \\ 1 & 0.10 & 0.14 & 0.06 \\ 2 & 0.07 & 0.05 & 0.06 \\ 3 & 0.06 & 0.03 & 0.01 \\ 4 & 0.04 & 0.01 & 0\end{tabular}").scale(0.7)

        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        table.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 5)
        self.play(Write(table), run_time = 2)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(table))

        t2 = Tex(r"Bestimmen Sie").scale(0.7)
        list = BulletedList(r"die Randwahrscheinlichkeiten von $X_1$ und $X_2$",
        r"die Randverteilungsfunktion von $X_1$",
        r"den Erwartungswert für die Anzahl der Kinder bzw. PKW pro Familie",
        r"die Wahrscheinlichkeit, dass es pro Familie genau zwei PKW und höchstens zwei Kinder gibt",
        r"die (bedingte) Wahrscheinlichkeitsfunktion der Anzahl der PKW für die Familien ohne Kinder",
        r"die (bedingte) erwartete Anzahl der PKW pro Familie ohne Kinder",
        r"die Kovarianz und die Korrelation zwischen $X_1$ und $X_2$").scale(0.7)

        t2.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t2, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(t2))
        self.play(Write(list), run_time = 7)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list), FadeOut(t2))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 12.2")

        t1 = Tex(r"Betrachten Sie folgende zweidimensionale Dichtefunktion").scale(0.65)
        formula = MathTex(r"f(x_1,x_2) = \begin{cases}\frac{4}{3}x_1x_2 & \text{für } x_1\in [1,2]\text{ und } x_2\in [0,1] \\ 0 & \text{sonst}\end{cases}").scale(0.65)
        list = BulletedList(r"Berechnen Sie die Randdichten $f_1(x_1)$ und $f_2(x_2)$.",
        r"Überprüfen Sie die Abhängigkeit der beiden Zufallsvariablen. Benutzen Sie dazu die zuvor bestimmten Randdichten.",
        r"Berechnen Sie die bedingten Dichten $f(x_1\vert x_2)$ bzw. $f(x_2\vert x_1)$.",
        r"Berechnen Sie die Erwartungswerte und Varianzen der beiden Zufallsvariablen. Benutzen Sie dazu die bedingten Dichten.",
        r"Bestimmen Sie die Wahrscheinlichkeit dafür, dass eine Realisation der Zufallsvariablen $X_1$ im Intervall $[0.5, 1.5]$ und gleichzeitig die von $X_2$ in $[-0.5, 0.5]$ liegt.").scale(0.65)

        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        formula.next_to(t1, direction = DOWN)
        list.next_to(formula, direction = DOWN).shift(1.6*RIGHT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1))
        self.play(Write(formula))
        self.play(Write(list), run_time = 7.5)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(formula), FadeOut(list), FadeOut(ueberschrift))

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
