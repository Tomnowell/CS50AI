from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # The two options
    Or(AKnight, AKnave), 
    # Is it possible to be true what A says?
    Or(And(AKnight, AKnave), AKnave), 
)

# Puzzle 1
# A says "We are both knaves."
# This cannot be true so at least 1 is a knave. We know A is a knave because they lied
# So B must be a knight because they can't both be knaves - that would make the statement true and A a knight...
# B says nothing.
knowledge1 = And(

    Or(AKnight, AKnave),
    Or(BKnight, BKnave),

    # Either A is telling the truth which would make A a knight or A is a knave
    Or(And(AKnight, BKnave), AKnave),  
    # If A and B are not both knaves then A is a knave
    And(Not(And(AKnave, BKnave)), AKnave),
    # If A is a knave then B is a knight - The AI should find this
)
# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),

    # same kind = both knight - if both knave then A telling the truth so paradox.
    Or(And(AKnight, BKnight), AKnave), 
    Or(And(AKnave, BKnave), AKnave),

    # B is knight if they are different
    Or(And(BKnight, AKnave), BKnight),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),

    #
    BKnave,
    # Work through B's lies
    Or(And(BKnight, CKnave), Not(AKnave), 
       And(CKnight, AKnight, Not(BKnight)))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
