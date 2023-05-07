from flask import Flask, render_template, request

import random


app = Flask(__name__)


# Liste de questions

questions = [

    {
    
        'question': 'Quel est le commandement pour initialiser un nouveau référentiel Git ?',
    
        'answer': 'git init'
    
    },
    
    {
    
        'question': 'Quelle est la méthode pour ajouter tous les fichiers modifiés ',
    
        'answer': 'git add .'
    
    },
    
    {
    
        'question': 'Quel est le mot-clé utilisé pour définir une fonction en Python ?',
    
        'answer': 'def'
    
    },
    
    {
    
        'question': 'Comment lister tous les fichiers dans un répertoire en utilisant Python ?',
    
        'answer': 'os.listdir()'
    
    },
    
    {
    
        'question': 'Quelle commande permet de changer le répertoire de travail courant en Python ?',
    
        'answer': 'os.chdir()'
    
    },
    
    {
    
        'question': 'Quelle commande permet de créer un répertoire en utilisant Linux ?',
    
        'answer': 'mkdir'
    
    },
    
    {
    
        'question': 'Comment afficher le répertoire de travail courant en utilisant Linux ?',
    
        'answer': 'pwd'
    
    },


    {
     
        'question': " Qu'est-ce que Git ?",
        
        'answer': "Git est un système de contrôle de version distribué utilisé pour gérer les versions de code source d'un projet."
        
    },
    
    {
     
        'question': " Quels sont les avantages de Python ?",
        
        'answer': "Python est un langage de programmation polyvalent et facile à apprendre. Il offre une syntaxe claire et concise, une grande communauté de développeurs et de nombreuses bibliothèques prêtes à l'emploi."
        
    },
    
    {
     
        'question': " Qu'est-ce qu'une distribution Linux ?",
        
        'answer': "Une distribution Linux est une version spécifique du système d'exploitation Linux, qui comprend le noyau Linux, des utilitaires système et des logiciels applicatifs. Les distributions Linux sont créées et maintenues par différentes organisations ou communautés."
        
    },
    
    {
        'question': " Qu'est-ce qu'un environnement virtuel en Python ?",
        
        'answer': "Un environnement virtuel en Python est un espace isolé qui permet d'installer des bibliothèques et des dépendances spécifiques à un projet Python sans interférer avec les autres projets. Cela permet de maintenir les dépendances du projet de manière indépendante et de garantir la cohérence de l'environnement de développement."
        
    },
    
    {
        'question': " Comment créer une nouvelle branche Git ?",
        
        'answer': "Pour créer une nouvelle branche Git, vous pouvez utiliser la commande 'git branch' suivie du nom de la nouvelle branche. Par exemple, 'git branch ma-branche' créera une nouvelle branche appelée 'ma-branche'."
        
    },
    
    {
        'question': " Qu'est-ce que PIP ?",
        
        'answer': "PIP est le gestionnaire de paquets par défaut pour Python. Il permet d'installer, de mettre à jour et de gérer les bibliothèques et les dépendances Python nécessaires à un projet."
        
    },
    
    {
        'question': " Qu'est-ce que l'interpréteur Python ?",
        
        'answer': "L'interpréteur Python est un programme qui lit et exécute le code Python. Il traduit les instructions écrites en Python en instructions exécutables par la machine."
        
    },
    
    {
     
        'question': " Qu'est-ce que la programmation orientée objet (POO) en Python ?",
        
        'answer': "La programmation orientée objet (POO) est un paradigme de programmation qui permet de structurer le code en utilisant des objets. En Python, les objets sont des instances de classes, qui regroupent des données (attributs) et des fonctionnalités (méthodes)."
        
    },
 
    {
        'question': " Quelle est la différence entre les méthodes GET et POST dans les requêtes HTTP ?",
        
        'answer': "La méthode GET est utilisée pour récupérer des données à partir d'une ressource spécifiée, tandis que la méthode POST est utilisée pour soumettre des données à une ressource spécifiée pour traitement. La méthode GET ajoute les données dans l'URL, tandis que la méthode POST les envoie dans le corps de la requête."
        
    },
    
    {
        'question': " Comment utiliser une boucle 'for' en Python ?",
        
        'answer': "Pour utiliser une boucle 'for' en Python, vous pouvez utiliser la syntaxe suivante : 'for element in sequence:', suivi du bloc de code à exécuter à chaque itération. Par exemple, 'for i in range(5):' exécutera le bloc de code 5 fois en faisant varier la valeur de 'i' de 0 à 4."
    },
    
    {
     
        'question': " Qu'est-ce qu'un gestionnaire d'environnement virtuel en Python ?",
        
        'answer': "Un gestionnaire d'environnement virtuel en Python est un outil qui permet de créer et de gérer des environnements virtuels. Il fournit un espace isolé où vous pouvez installer des bibliothèques et des dépendances spécifiques à un projet sans affecter les autres projets."
        
    },
    
    {
        'question': " Qu'est-ce que le package manager 'pip' en Python ?",
        
        'answer': "Le package manager 'pip' est un outil de ligne de commande qui permet d'installer, de mettre à jour et de gérer les packages Python. Il est largement utilisé pour installer des bibliothèques tierces et des dépendances nécessaires à un projet."
        
    },
    
    {
     
        'question': " Qu'est-ce qu'une boucle 'while' en Python ?",
        
        'answer': "Une boucle 'while' en Python est utilisée pour répéter un bloc de code tant qu'une condition donnée est vraie. Le bloc de code sera exécuté tant que la condition est évaluée à True. Une fois que la condition devient False, la boucle se termine."
        
    },
    
    {
     
        'question': " Comment utiliser une condition 'if' en Python ?",
        
        'answer': "Pour utiliser une condition 'if' en Python, vous pouvez utiliser la syntaxe suivante : 'if condition:', suivi du bloc de code à exécuter si la condition est vraie. Vous pouvez également utiliser les mots-clés 'else' et 'elif' pour gérer les conditions alternatives."
        
    },
    
    {
     
        'question': " Qu'est-ce qu'une fonction en Python ?",
        
        'answer': "Une fonction en Python est un bloc de code réutilisable qui effectue une tâche spécifique."
        

    }

]


# Page d'accueil

@app.route('/')

def home():

    question = random.choice(questions)
    
    return render_template('index.html', question=question['question'])
    
# Évaluation de la réponse

@app.route('/evaluate', methods=['POST'])

def evaluate():

    user_answer = request.form['answer']

    question = request.form['question']

    

    # Trouver la réponse attendue pour la question donnée

    for q in questions:

        if q['question'] == question:

            expected_answer = q['answer']

            break 
    

    # Vérifier si la réponse de l'utilisateur est correcte ou non

    if user_answer.lower() == expected_answer.lower():

        result = 'Réponse validée !'

    else:

        result = 'Réponse incorrecte !'

    
    return render_template('result.html', result=result)


if __name__ == '__main__':

        app.run(host='0.0.0.0', port=80,debug=True)





























