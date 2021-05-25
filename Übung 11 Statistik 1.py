from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 11, Statistik 1")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"Dichte und Verteilungsfunktion", r"Erwartungswert", r"Varianz", r"bedingte Wahrscheinlichkeiten").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 3)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 11.1")

        t1 = Tex(r"Gegeben ist folgende Dichtefunktion einer Zufallsvariablen $Y$.").scale(0.7)
        formula = MathTex(r"f(y)=\begin{cases}\frac{1}{12}y & \text{für } 1\le y \le 5\\ 0 & \text{sonst} \end{cases}").scale(0.7)
        list = BulletedList(r"Bestimmen Sie die Verteilungsfunktion dieser Zufallsvariablen!",
        r"Bestimmen Sie die Wahrscheinlichkeit des Ereignisses $2 < Y < 3$!").scale(0.7)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        formula.next_to(t1, direction = DOWN)
        list.next_to(formula, direction = DOWN).shift(0.4*RIGHT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1))
        self.play(Write(formula))
        self.play(Write(list), run_time = 3)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1), FadeOut(formula), FadeOut(list))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 11.2")

        t1 = VGroup(Tex(r"Ein Unternehmer hat die Erfahrung gemacht, dass seine Einnahmen $Z$ (in"), Tex(r"Euro) von der Anzahl der am Betrieb vorbeilaufenden Passanten $X$ abhängen."), Tex(r"Dabei sei:")).scale(0.7)
        formula = MathTex(r"Z = \frac{1}{2} + \frac{1}{50}X").scale(0.7)
        t2 = Tex(r"mit $\mathbb{E}(X) = 100$ und $\text{Var}(X) = 900$. Bestimmen Sie $\mathbb{E}(Z)$ und $\text{Var}(Z)$.").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        formula.next_to(t1, direction = DOWN)
        t2.next_to(formula, direction = DOWN).shift(-0.6*RIGHT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 3)
        self.play(Write(formula))
        self.play(Write(t2))
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(formula), FadeOut(t2), FadeOut(ueberschrift))

class Aufgabe3(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 11.3")

        t1 = VGroup(Tex(r"Die Zufallsvariable $X$ genüge $\mathbb{E}(X) = 10$ und $\text{Var}(X) = 9$ und $Y$ genüge"),
        Tex(r"$\mathbb{E}(Y) = \mu$ und $\text{Var}(Y) = \sigma^2$. $X$ und $Y$ seien unabhängig voneinander. Man"),
        Tex(r"berechne")).scale(0.7)
        list = BulletedList(r"$\mathbb{E}(X - 5)$ und $\text{Var}(X - 5)$",
        r"$\mathbb{E}(2X - 10)$ und $\text{Var}(2X - 10)$",
        r"$\mathbb{E}\left(\frac{1}{3}X\right)$ und $\text{Var}\left(\frac{1}{3}X\right)$",
        r"$\mathbb{E}\left[\frac{1}{3}(X-10)\right]$ und $\text{Var}\left[\frac{1}{3}(X-10)\right]$").scale(0.7)
        list2 = BulletedList(r"$\mathbb{E}\left(X^2\right)$",
        r"$\mathbb{E}(2X - 3Y)$ und $\text{Var}(2X - 3Y)$",
        r"$\mathbb{E}\left(\frac{Y - \mu}{\sigma}\right)$ und $\text{Var}\left(\frac{Y - \mu}{\sigma}\right)$",
        r"$\mathbb{E}[\text{Var}(X)]$ und $\text{Var}[\mathbb{E}(X)]$").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)
        list2.next_to(list, direction = RIGHT).shift(0.5*RIGHT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 3)
        self.play(Write(list), run_time = 3)
        self.play(Write(list2), run_time = 3)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list), FadeOut(list2), FadeOut(ueberschrift))

class Aufgabe4(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 11.4")

        t1 = VGroup(Tex(r"Nach mehreren Befragungen kennt man die Verteilung des Einkommens (in"),
        Tex(r"Euro) und des Alters (in Jahren) der Beschäftigten einer Firma. Die"),
        Tex(r"gemeinsame Verteilung ist in der folgenden Tabelle gegeben:")).scale(0.7)
        table = Tex(r"\begin{tabular}{c|ccc} & \multicolumn{3}{c}{Alter} \\ Einkommen & $[20,30)$ & [30,45) & [45,70) \\ \hline < 1500 & 0.2 & 0.2 & 0.1 \\ $\ge$ 1500 & 0.1 & 0.2 & 0.2\end{tabular}").scale(0.7)

        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        table.next_to(t1, direction = DOWN, aligned_edge = LEFT)


        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 3)
        self.play(Write(table))
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(table))

        list = BulletedList(r"Bestimmen Sie die relativen Randwahrscheinlichkeiten.",
        r"Bestimmen Sie das erwartete Alter.",
        r"Bestimmen Sie die bedingten relativen Wahrscheinlichkeiten des Einkommens für die erste Altersgruppe.",
        r"Berechnen Sie die bedingte Wahrscheinlichkeit dafür, dass sich eine Person in der zweiten Einkommensgruppe befindet unter der Bedingung, dass sie aus der ersten oder zweiten Altersgruppe ist.").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(list), run_time = 6)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

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
