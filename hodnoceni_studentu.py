class StudentsGrades:
    def __init__(self, scores):
       #při vytvoření objektu uloží předaný seznam bodů do atributu self.scores
        self.scores = scores

    def get_by_index(self, index):
        #vrátí počet bodů studenta na zadané pozici
        return self.scores[index]

    def count(self):
        #vrátí počet studentů (délku seznamu)
        return len(self.scores)

    def get_grade(self, index):
        score = self.get_by_index(index)
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, target_score):
        found_index = []
        for i in range(len(self.scores)):
            #prochazi seznam scores pomoci indexu (0 az delka seznamu)
            #pokud se hodnota na indexu i rovna hledanemu poctu bodu
            if self.scores[i] == target_score:
                found_index.append(i)
        return found_index

    def get_sorted(self):
        scores = self.scores.copy() # musim udelat kopii
        n = len(scores)
        # tohle je jako bubble sort:
        for i in range(n):
            for j in range(0, n - i - 1):
                if scores[j] > scores[j + 1]:
                    #prohozeni prvku:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]
        return scores



if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]

    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)

    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []

    print(results.get_sorted())   # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)         # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny

    print(f"Test psalo {results.count()} studentu.")

    for i in range(results.count()):
        points = results.get_by_index(i)
        grade = results.get_grade(i)
        print(f"student {i}: {points} points – {grade}")

    full_score_students = results.find(100)
    print(f"indexy studentu s plnym poctem bodu(100): {full_score_students}")

    sorted_results = results.get_sorted()
    print(f"serazene vysledky (od nejhorsiho): {sorted_results}")

# kdyz vlozim random:
    from sorting import random_numbers

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())