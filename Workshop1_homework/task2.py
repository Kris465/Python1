# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ДЗ (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W)

def task2_hw():
    print("x y z w")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if (w and z) or not y or (x == w): # На счет последнего действия. Так как положение может быть либо 1, либо 0, очевидно, что если не x == не w, то x == w, прогнала, по выводу одно и тоже
                        print(x, y, z, w)

task2_hw()