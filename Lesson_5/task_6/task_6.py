"""
Задание 6.

Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и лабораторных
занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий
название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика:   100(л)   50(пр)   20(лаб).
Физика:   30(л)   —   10(лаб)
Физкультура:   —   30(пр)   —

Пример словаря: {"Информатика": 170, "Физика": 40, "Физкультура": 30}
"""
subject_dict = {}

with open("input.txt", "r", encoding='utf-8') as f:
    for line in f:
        clear_line = line.replace("(л)", "").replace(
            "(пр)", "").replace("(лаб)", "").replace(".", "")
        subject, lecture, practice, lab = clear_line.split()

        LECT_INT = 0
        PRACTICE_INT = 0
        LAB_INT = 0
        if lecture != "-":
            LECT_INT = int(lecture)
        if practice != "-":
            PRACTICE_INT = int(practice)
        if lab != "-":
            LAB_INT = int(lab)
        subject_dict[subject] = LECT_INT + PRACTICE_INT + LAB_INT
    print(f"{subject_dict}")
    f.close()
