<!--This project is written in Python 3.10.1.
All packages and their versions used in the project can be found in the requirements.txt file.
This code is a web application that provides an API for paraphrasing sentences using permutations of noun phrases (NPs) in a dependency tree passed as a string. The code uses the NLTK library to work with syntax trees and Flask to create a web server.

The function find_phrases recursively iterates through all child nodes of the syntax tree and searches for NPs (noun phrases). All found noun phrases are stored in a list.

The function generate_permutations generates all possible permutations between NPs using the created list of noun phrases.

The final method, paraphrase, processes a request to obtain NP permutations from the tree, using the input data from the tree. The tree is passed as a string, and other parameters such as permutation limit are passed through URL parameters. The function returns a list in JSON format that contains the tree and all possible NP permutations. -->

<!-- Цей проект написаний на Python 3.10.1.
Усі пакети та їх версії, що використовувалися в проекті, можна знайти у файлі requirements.txt.
Цей код є веб-додатком, який надає API для перефразування речень з використанням перестановки іменникових фраз (NP) в дереві залежностей, яке передається у вигляді рядка. Код використовує бібліотеку NLTK для роботи з синтаксичними деревами та Flask для створення веб-сервера.

Функція find_phrases рекурсивно перебирає всі дочірні вузли синтаксичного дерева та шукає NP (іменникові фрази). Всі знайдені іменникові фрази зберігаються в списку.

Функція generate_permutations генерує всі можливі перестановки між NP, використовуючи створений список іменникових фраз.

Кінцевий метод paraphrase обробляє запит на отримання перестановок NP з дерева, використовуючи введені дані з дерева. Дерево передається у вигляді рядка, інші параметри, такі як ліміт перестановок, передаються через параметри URL-адреси. Функція повертає список у форматі JSON, який містить дерево і всі можливі перестановки NP. 
Приклад запиту до цього веб-застосунку виглядатиме так:
'http://127.0.0.1:5000/paraphrase?tree=(ROOT(S(NP(John))(VP(loves)(NP(Mary)))))&limit=10'   -->
