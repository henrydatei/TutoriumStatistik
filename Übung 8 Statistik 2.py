from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 8, Statistik 2")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"Gütefunktion", r"Fehler 1. und 2. Art").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 2)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 8.1")

        t1 = Tex(r"Der mittlere Zeitaufwand $\mu$ für die Klausurvorbereitung einer Statistikklausur (in Stunden) wird untersucht. Eine Dozentin behauptet, dass ein Student im Durchschnitt nur 83 Stunden Vorbereitungszeit braucht, um die Klausur mit einer guten Note zu bestehen: \textit{über ein Semester von 15 Wochen fünf Stunden pro Woche (1.5 (Vorlesung) + 1.5 (Übung) + 2 (selber Zuhause)) und jeweils vier Stunden an den zwei Tagen vor der Klausur.} Sie fragt neun zufällig ausgewählte Studierende nach der Vorbereitungszeit und erhält eine Stichprobe $X = (X_1, X_2, ..., X_9)$. Daraus ergibt sich ein mittlerer Wert $\bar{x} = 86$ Stunden. Aus langjähriger Erfahrung weiß man, dass die einzelnen Variablen $X_i$ normalverteilt sind: $X_i \sim \mathcal{N}(\mu, \sigma^2)$, mit $\sigma^2 = 64$ Stunden$^2$. Die $X_i$ sind unabhängig voneinander. Der Student testet anhand der o.g. Stichprobe, ob der mittlere Zeitaufwand größer als 83 Stunden ist.", tex_environment = "flushleft").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 12)
        self.wait(2)
        self.play(FadeOut(t1))

        list2 = BulletedList(r"Leiten Sie die Gütefunktion her.",
        r"Wie groß ist die Wahrscheinlichkeit die Nullhypothese abzulehnen, wenn die wahre mittlere Vorbereitungszeit 84 Stunden beträgt? Macht man in diesem Fall einen Fehler? Wenn ja, welcher Art ist dieser Fehler?",
        r"Wie groß ist die Wahrscheinlichkeit die Nullhypothese nicht abzulehnen, wenn die wahre mittlere Vorbereitungszeit 84 Stunden beträgt? Macht man in diesem Fall einen Fehler? Wenn ja, welcher Art ist dieser Fehler?",
        r"Wie groß ist die Wahrscheinlichkeit die Nullhypothese abzulehnen, wenn die wahre mittlere Vorbereitungszeit 82 Stunden beträgt? Macht man in diesem Fall einen Fehler? Wenn ja, welcher Art ist dieser Fehler?").scale(0.7)
        list2.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(list2), run_time = 10)
        self.wait(2)
        self.play(FadeOut(list2), FadeOut(ueberschrift))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 8.2")

        t1 = Tex(r"In einem Betrieb werden u. a. grüne Bohnen in Dosen abgefüllt. Bei einer zufälligen Stichprobe von 25 Dosen wurden folgende Abfüllgewichte in g ermittelt: 173, 176, 172, 176, 175, 174, 172, 173, 173, 174, 172, 178, 176, 177, 175, 176, 173, 172, 175, 173, 174, 177, 176, 174, 174. Hieraus ergibt sich $\bar{x} =$ 174.4 g bei einer Streuung von $s =$ 1.756 g. Die Abfüllanlage arbeitet laut Herstellerangabe mit einer Standardabweichung von 4 g. Es wird angenommen, dass es sich bei den ermittelten Werten um Realisationen einer normalverteilten Zufallsgröße handelt.", tex_environment = "flushleft").scale(0.7)
        list = BulletedList(r"Untersuchen Sie, ob zum Niveau $\alpha = 0.05$ statistisch nachgewiesen werden kann, dass das angegebene Abfüllgewicht von 175 g unterschritten wird. Gehen Sie davon aus, dass $\sigma = 4$ g ist.",
        r"Berechnen Sie den $p$-Wert des durchgeführten Tests.",
        r"Berechnen Sie die Gütefunktion des durchgeführten Tests.",
        r"Wie groß ist die Wahrscheinlichkeit, dass beim Test $H_0$ nicht verworfen wird, obwohl $H_1$: $\mu = 174$ g richtig ist?",
        r"Wie groß muss der Stichprobenumfang gewählt werden, damit der obige Test eine Abweichung vom Sollwert (175 g) nach unten in Höhe von 1 g mit einer Sicherheit von mindestens 97.5 \% aufdeckt?").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 8)
        self.wait(2)
        self.play(FadeOut(t1))

        self.play(Write(list), run_time = 10)
        self.wait(2)
        self.play(FadeOut(list), FadeOut(ueberschrift))

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
