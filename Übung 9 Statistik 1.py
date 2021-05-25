from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 9, Statistik 1")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"bedingte Wahrscheinlichkeiten", r"stochastische Unabhängigkeit").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 3)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 9.1")

        t1 = VGroup(Tex(r"Karl liebt den Alkohol. Die Wahrscheinlichkeit, dass er nach Büroschluss"),
        Tex(r"trinkt, ist 0.8. Karl ist vergesslich. Die Wahrscheinlichkeit, dass er seinen"),
        Tex(r"Schirm stehen lässt, ist 0.7. Wenn er getrunken hat, ist die Wahrscheinlichkeit"),
        Tex(r"sogar 0.8. Karl kommt ohne Schirm nach Hause. Wie groß ist die"),
        Tex(r"Wahrscheinlichkeit dafür, dass er dieses Mal nicht getrunken hat?")).scale(0.7)

        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 5)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 9.2")

        t1 = VGroup(Tex(r"Um ins Land Y reisen zu können, muss ein Visum beim zuständigen Konsulat"),
        Tex(r"beantragt werden. Im Konsulat sitzen drei Mitarbeiter. Wird der Visa-Antrag"),
        Tex(r"von einem der ersten beiden Mitarbeitern bearbeitet, erhält der Antragsteller"),
        Tex(r"das Visum in 90\% der Fälle innerhalb einer Woche. Bearbeitet dagegen der 3."),
        Tex(r"Mitarbeiter den Antrag, liegt das Visum gerade mal in 60\% der Fälle"),
        Tex(r"innerhalb einer Woche vor. Die Anträge werden zufällig (mit der selben"),
        Tex(r"Wahrscheinlichkeit) an die drei Mitarbeiter verteilt. Es wird angenommen,"),
        Tex(r"dass kein Visa-Antrag abgelehnt wird. Gegeben seien die Ereignisse: A -"),
        Tex(r" \textit{Visum wird innerhalb einer Woche bearbeitet.} und B - \textit{Der 3. Mitarbeiter}"),
        Tex(r"\textit{bearbeitet den Antrag.}")).scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 10)
        self.wait(2)
        self.play(FadeOut(t1))

        list2 = BulletedList(r"Wie wahrscheinlich wird ein Visum innerhalb einer Woche bearbeitet?",
        r"Mit welcher Wahrscheinlichkeit bearbeitet der 3. Mitarbeiter den Antrag, wenn ein Visum nach einer Woche immer noch nicht vorliegt?",
        r"Vier Freunde haben sich spontan entschlossen nach Y zu reisen. Der Flieger geht in genau einer Woche. Mit welcher Wahrscheinlichkeit haben alle vier Freunde rechtzeitig das Visum?").scale(0.7)
        list2.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.wait(1)
        self.play(Write(list2), run_time = 6)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list2))

class Aufgabe3(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 9.3")

        t1 = VGroup(Tex(r"Von drei Kästchen mit je zwei Schubfächern enthalte das Erste in jedem Fach"),
        Tex(r"eine Goldmünze, das Zweite in einem Fach eine Goldmünze, im Anderen eine"),
        Tex(r"Silbermünze und das Dritte in jedem Fach eine Silbermünze. Zufällig werde"),
        Tex(r"ein Kästchen ausgewählt und ein Schubfach geöffnet. Wie groß ist die"),
        Tex(r"Wahrscheinlichkeit, im anderen Fach des ausgewählten Kästchens eine"),
        Tex(r"Goldmünze zu finden, wenn das schon geöffnete Fach eine Goldmünze enthält?")).scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 6)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(ueberschrift))

class Aufgabe4(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 9.4")

        t1 = VGroup(Tex(r"Ein Würfel wird zweimal geworfen. Dabei bezeichnet A das Ereignis, dass eine"),
        Tex(r"gerade Augenzahl beim ersten Wurf geworfen wurde, B das Ereignis, dass eine"),
        Tex(r"gerade Augenzahl beim zweiten Wurf geworfen wurde, und C das Ereignis,"),
        Tex(r"dass die Summe beider Augenzahlen gerade ist. Sind die Ereignisse A, B und"),
        Tex(r"C unabhängig? Sind sie paarweise unabhängig?")).scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 5)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1))

class Aufgabe5(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 9.5")

        t1 = VGroup(Tex(r"Eine Hotelrezeption nimmt Beschwerden entgegen. Im Mittel beschwert sich"),
        Tex(r"jeder zehnte Gast. Von den Beschwerden beziehen sich 70\% auf Servicemängel"),
        Tex(r"des Hotels. Auf Nachfrage erfährt die Rezeption außerdem, dass 20\% der"),
        Tex(r"Gäste, die keine Beschwerde einreichen, dennoch den einen oder anderen"),
        Tex(r"Mangel am Service zu beanstanden haben.")).scale(0.7)
        list = BulletedList(r"Wie wahrscheinlich ist ein beliebig herausgegriffener Gast mit dem Hotelservice unzufrieden?",
        r"Wie wahrscheinlich beschwert sich ein Hotelgast, der mit dem Service nicht zufrieden ist?").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 5)
        self.play(Write(list), run_time = 3)
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
