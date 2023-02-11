import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

Obiective Întâlnire 4

● Să înțelegi ce sunt, care sunt particularitățile și cum se folosesc
ciclurile repetitive:
○ while;
○ while else;
○ for each;
○ for;
○ for else.
● Să poți controla iterațiile cu:
○ break;
○ continue.

While / while else

● Se execută un bloc de cod atât timp cât o condiție e adevărată.
● Opțional: la final se poate pune else, această zonă se execută o dată, la final.

For / for else

● Se execută un bloc de cod pentru fiecare valoare din range.
● Range seamănă cu slicing. Ne spune:
○ De unde începem? Default e 0.
○ Până unde iterăm?
○ Opțional: pasul.
● Opțional: la final se poate pune else.
○ această zonă se execută o dată, la final.

For each

● Se parcurge o colecție și se salvează fiecare element într-o variabilă.
● La fiecare iterație, variabilă se va suprascrie cu valoarea actuală.
● Rând pe rând, se vor parcurge toate elementele dintr-o colecție.

Break

● Cuvântul cheie ‘break’ va opri iterația.
● Practic se iese automat din loop.
● Nu se mai execută codul de după break, din cadrul unui for/ while.

Continue

● Cuvântul cheie ‘continue’ va sări peste iterația actuală.
● E un fel de skip.
● Se va sări peste blocul de cod de după skip, care ține de for/ while.

Întrebări & curiozități?
j Întrebări de interviu:

➢ Când folosim break?
➢ Care este diferența dintre For și While?
➢ Când folosim Continue?
