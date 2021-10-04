from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 9, Statistik 2")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"Zweistichproben-$t$-Test", r"Welch-Test").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 2)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 9.1")

        t1 = Tex(r"Mithilfe zweier Maschinen A und B wird Tee abgepackt. Man weiß, dass die Füllgewichte der beiden Maschinen annähernd normalverteilt sind. Eine Zufallsstichprobe vom Umfang $n_X = 16$ aus der Produktion der Maschine A liefert ein durchschnittliches Füllgewicht von $\bar{x} =$ 140 g mit Stichprobenvarianz $s^2_X =$ 51 g$^2$. Eine Zufallsstichprobe vom Umfang $n_Y = 11$ aus der Produktion der Maschine B liefert ein durchschnittliches Füllgewicht von $\bar{y}=$ 134 g mit $s^2_Y =$ 46 g$^2$. Auf Stichprobenbasis soll nachgewiesen werden, dass die Maschine A mit einem größeren durchschnittlichen Füllgewicht arbeitet als die Maschine B.", tex_environment = "flushleft").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 9)
        self.wait(2)
        self.play(FadeOut(t1))

        list2 = BulletedList(r"Führen Sie einen geeigneten Test durch ($\alpha = 0.01$).",
        r"Da die Varianzen unbekannt sind, kann es auch sein, dass sie gleich sind. Falls man den Zweistichproben-$t$-Test anwenden möchte, muss die Varianzengleichheit getestet werden. Führen Sie den geeigneten Test durch ($\alpha = 0.02$).",
        r"Führen Sie unter der Annahme, dass die Varianzen gleich sind, einen Test durch ($\alpha = 0.01$).").scale(0.7)
        list2.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(list2), run_time = 5)
        self.wait(2)
        self.play(FadeOut(list2), FadeOut(ueberschrift))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 9.2")

        t1 = Tex(r"Ein pharmakologisches Unternehmen hat ein neues blutdrucksenkendes Medikament entwickelt. Ein Forscher untersucht, ob das Medikament tatsächlich einen Effekt hat.", tex_environment = "flushleft").scale(0.7)
        list = BulletedList(r"Er bildet per Zufallswahl zwei Gruppen: eine Gruppe bekommt das neuartige Medikament, die andere ein Placebo. Beide Gruppen umfassen 20 Proband*innen. In der Gruppe, die das neuartige Medikament bekommt, war die durchschnittliche Blutdrucksänderung -10.7 mmHg mit einer Standardabweichung von 9.8. Die Gruppe ohne Wirkstoff erreicht eine durchschnittliche Blutdrucksänderung von -1.6 mmHg mit einer Standardabweichung von 11.1. Hat die Gruppe, die das Medikament bekam, eine größere Blutdruckreduktion zu verzeichnen als die Placebogruppe ($\alpha = 0.05$)? Ist der Blutdruck in der ersten Gruppe mehr um seinen Mittelwert konzentriert als der der zweiten Gruppe?").scale(0.7)
        list2 = BulletedList(r"In einem zweiten Test untersucht er vor und nach der Therapie den Blutdruck von 5 Patient*innen, die das neue Medikament bekommen. Hat sich der mittlere Blutdruck der Proband*innen während des Experiments signifikant mit $\alpha = 0.05$ reduziert?").scale(0.7)
        table = DecimalTable([[132.4,117.3,142.4,149.5,118.8],[130.7,119.0,122.0,124.9,122.3]], element_to_mobject_config = {"num_decimal_places":1}, row_labels = [Tex("vor Therapie"), Tex("nach Therapie")]).scale(0.7)
        list3 = BulletedList(r"Mit $\alpha = 0.12$ ließe sich die Nullhypothese in (b) verwerfen. Warum wäre es in diesem Fall falsch zu sagen, dass das Medikament mit $\alpha = 0.12$ den Blutdruck senkt?").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)
        list2.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        table.next_to(list2, direction = DOWN)
        list3.next_to(list2, direction = 9 * DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 3)
        self.play(Write(list), run_time = 10)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list))

        self.play(Write(list2), run_time = 4)
        self.play(Write(table))
        self.play(Write(list3), run_time = 3)
        self.wait(2)
        self.play(FadeOut(list2), FadeOut(table), FadeOut(list3), FadeOut(ueberschrift))

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
