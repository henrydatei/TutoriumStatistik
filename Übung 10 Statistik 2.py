from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 10, Statistik 2")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"Tests für Zusammenhangsmaße").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 1)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 10.1")

        t1 = Tex(r"Mit wachsender Umweltbelastung betrachten große Teile der Bevölkerung das Fahrrad wieder als umweltfreundliches Verkehrsmittel. In einer Studie sollte untersucht werden, ob allein der Bau von Radwegen den Fahrradanteil am Berufsverkehr positiv beeinflusst. Eine Stichprobe in 17 verschiedenen Städten ergab für den Rangkorrelationskoeffizienten nach Spearman zwischen der Radwegerschließung (Punkteskala, Merkmal $X$) und dem Radanteil am Berufsverkehr (in \%, Merkmal $Y$) einen Wert von $\hat{R} = 0.89$. Testen Sie, ob der gemessene positive (monotone) Zusammenhang zwischen Radwegerschließung und Radanteil statistisch signifikant ist (mit $\alpha = 0.01$). (Verwenden Sie eine Normalapproximation!)", tex_environment = "flushleft").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 10)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(ueberschrift))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 10.2")

        t1 = Tex(r"Studierende einer Hochschule wurden nach ihrer Einstellung zu einer Verkürzung der Pause zwischen zwei Vorlesungen von bisher 20 Minuten auf 10 Minuten befragt. Von 500 Befragten waren 200 weiblich und 300 männlich. Als Antworten waren die Werte positiv, unentschieden und negativ möglich. Das Ergebnis der Befragung ist nachstehend wiedergegeben.", tex_environment = "flushleft").scale(0.7)
        t2 = Tex(r"Testen Sie, ob weibliche und männliche Studierende im Durchschnitt unterschiedliche Meinungen haben.", tex_environment = "flushleft").scale(0.7)
        table = IntegerTable([[85,41,74],[90,52,158]], row_labels = [Tex("weiblich"), Tex("männlich")], col_labels = [Tex("positiv"), Tex("unentschieden"), Tex("negativ")], top_left_entry = Tex(r"$X/Y$")).scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        table.next_to(t1, direction = DOWN)
        t2.next_to(t1, direction = 12 * DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 5)
        self.play(Write(table), run_time = 2)
        self.play(Write(t2), run_time = 2)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(table), FadeOut(t2), FadeOut(ueberschrift))

class Aufgabe3(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 10.3")

        t1 = Tex(r"Aus einer Befragung von $n = 20$ Radfahrer*innen konnte für den Zusammenhang zwischen Alter $X$ und durchschnittliche wöchentliche Kilometerzahl $Y$ ein Korrelationskoeffizient von $r = -0.707$ ermittelt werden. Ist der lineare Zusammenhang zwischen Alter und Wegstrecke statistisch signifikant?", tex_environment = "flushleft").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 4)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(ueberschrift))

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
