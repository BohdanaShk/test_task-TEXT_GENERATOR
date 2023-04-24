from nltk.tree import Tree
from flask import Flask, request, jsonify

app = Flask(__name__)


def find_phrases(t):
    """
    A recursive function to find all NPs in a dependency tree can be implemented as follows
    """
    phrases = []
    for child in t:
        if type(child) == Tree and child.label() == 'NP':
            phrases.append(' '.join(child.leaves()))
        else:
            phrases += find_phrases(child)
    return phrases


def generate_permutations(phrases):

    """
   A function to generate permutations between NPs can be implemented as follows
    """
    permutations = []
    for i in range(len(phrases)):
        for j in range(i+1, len(phrases)):
            new_phrases = list(phrases)
            new_phrases[i], new_phrases[j] = new_phrases[j], new_phrases[i]
            permutations.append(new_phrases)
    return permutations


@app.route('/paraphrase')
def paraphrase():
    # We obtain a syntax tree
    tree_str = request.args.get('tree')
    if not tree_str:
        return jsonify({'error': 'Syntax tree is required.'}), 400
    try:
        tree = Tree.fromstring(tree_str)
    except Exception as e:
        return jsonify({'error': f'Invalid syntax tree: {str(e)}'}), 400

    # Find all NP in a tree
    phrases = find_phrases(tree)

    # "Generating permutations between NP
    limit = int(request.args.get('limit', 20))
    permutations = generate_permutations(phrases)[:limit]

    # Forming the answer
    response = [{'tree': tree_str, 'permutation': ' '.join(p)} for p in permutations]
    return jsonify(response)


if __name__ == '__main__':
    app.run()

