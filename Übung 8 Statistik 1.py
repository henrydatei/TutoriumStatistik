from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 8, Statistik 1")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"Mengenoperationen", r"Laplace-Wahrscheinlichkeit", r"stochastische Unabhängigkeit").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 3)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 8.1")

        t1 = VGroup(Tex(r"Geben Sie für die folgenden Ereignisoperationen die Ergebnisse an."),
        Tex(r"$\Omega$ - Grundgesamtheit, $A,B \subset \Omega$, und $B \subset A$:"),
        Tex(r"$A\cup A$, $A\cap A$, $A\cup\emptyset$, $A\cap\emptyset$, $\emptyset\cap\Omega$, $A\cup\Omega$, $A\cap\Omega$, $A\cup A$, $A\cap A$, $A\cup B$, $A\cap B$,"),
        Tex(r"$A\cup \bar{B}$, $A\cap \bar{B}$, $\bar{A}\cap B$, $\bar{A}\cup \bar{B}$ $\bar{A}\cap \bar{B}$")).scale(0.7)

        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 4.5)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 8.2")

        t1 = VGroup(VGroup(Tex(r"Ein technisches System bestehe aus "), Tex(r"drei"), Tex(r" Teilsystemen, die in einem")).arrange(RIGHT), Tex(r"betrachteten Zeitraum zufallsbedingt entweder funktionieren oder ausfallen.")).scale(0.7)
        list = BulletedList(r"Geben Sie bitte den Stichprobenraum für die möglichen Zustände des Gesamtsystems $\Omega$ an! Verwenden Sie dazu eine Kodierung für die Zustände jedes Teilsystems, wobei die Kodierung 0 = \textit{das Teilsystem fällt aus} und 1 = \textit{das Teilsystem funktioniert} lautet.",
        r"Für die zufälligen Ereignisse $A$ - \textit{Genau zwei Teilsysteme fallen aus} und $B$ - \textit{Das Teilsystem 1 fällt aus} bestimme man $A\cap B$, $A\cup B$, $A\setminus B$, mit $A, B$ als Teilmengen von $\Omega$ und formuliere diese zufälligen Ereignisse in Worten.").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        frame = SurroundingRectangle(t1[0][1])

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 2)
        self.play(Create(frame))
        self.play(Write(list), run_time = 7)
        self.wait(2)
        self.play(FadeOut(list), FadeOut(t1), FadeOut(frame))

        list2 = BulletedList(r"Man bestimme die Teilmengen für die zufälligen Ereignisse $C$ - \textit{Kein Teilsystem fällt aus.}, $D$ - \textit{Höchstens ein Teilsystem fällt aus.}, $E$ - \textit{Mindestens ein Teilsystem fällt aus.}, sowie für $A\cap E$, $E\setminus B$, $B\cap C$, $B\cap D$.",
        r"Welche der Ereignisse $A$, $B$, $C$, $D$ und $E$ sind paarweise unvereinbar?").scale(0.7)
        list2.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.wait(1)
        self.play(Write(list2), run_time = 4)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list2))

class Aufgabe3(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 8.3")

        t1 = VGroup(Tex(r"Eine Befragung von 10 Passanten in der Einkaufsstraße einer Großstadt"), Tex(r"lieferte folgende Urliste:")).scale(0.7)
        table = Tex(r"\begin{tabular}{cccc}\hline Passant $i$ & Geschlecht & Verkehrsmittel & Anzahl Geschäfte \\ \hline 1 & männlich & ÖPNV & 6 \\ 2 & weiblich & ÖPNV & 4 \\ 3 & weiblich & Auto & 1 \\ 4 & weiblich & ÖPNV & 8 \\ 5 & weiblich & Auto & 2 \\ 6 & männlich & Auto & 1 \\ 7 & männlich & Auto & 5 \\ 8 & weiblich & Auto & 8 \\ 9 & weiblich & Auto & 3 \\ 10 & männlich & ÖPNV & 1 \end{tabular}").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        table.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1))
        self.play(Write(table), run_time = 4.5)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(table))
        self.wait(1)

        list = BulletedList(r"Wie wahrscheinlich ist ein zufällig ausgewählter Passant männlich?",
        r"Wie wahrscheinlich fährt ein zufällig ausgewählter Passant mit dem Auto zum Einkaufen?",
        r"Wie wahrscheinlich besucht ein zufällig ausgewählter Passant mehr als drei Geschäfte?",
        r"Mit welcher Wahrscheinlichkeit besucht ein männlicher Passant mehr als drei Geschäfte? Sind die beiden Ereignisse \textit{männlicher Passant} und \textit{mehr als drei Geschäfte besucht} stochastisch unabhängig?",
        r"Mit welcher Wahrscheinlichkeit besucht ein Passant, der mit dem Auto zum Einkaufen gefahren ist, mehr als drei Geschäfte? Sind die beiden Ereignisse \textit{mit Auto zum Einkaufen gefahren} und \textit{mehr als drei Geschäfte besucht} stochastisch unabhängig?").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(list), run_time = 7.5)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe4(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 8.4")

        t1 = Tex(r"Es sei $\mathbb{P}(\cdot)$ ein Wahrscheinlichkeitsmaß. Zeigen Sie die folgende Gleichungen").scale(0.7)
        list = BulletedList(r"$\mathbb{P}(\bar{A})=1-\mathbb{P}(A)$",
        r"$\mathbb{P}(\emptyset)=0$",
        r"$\mathbb{P}(A)=\mathbb{P}(A\cap B) + \mathbb{P}(A\cap\bar{B})$",
        r"Ist $B\subseteq A$, so ist $\mathbb{P}(B)\le\mathbb{P}(A)$",
        r"$\mathbb{P}(A\cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A\cap B)$").scale(0.7)

        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1))
        self.play(Write(list), run_time = 4.5)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1), FadeOut(list))

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
