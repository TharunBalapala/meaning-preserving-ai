import difflib
from app.models.schemas import ChangeItem

def classify_change(original: str, enhanced: str) -> str:
    """
    Simple heuristic classification of change type.
    """

    # Spelling correction (minor character change)
    if len(original) > 3 and len(enhanced) > 3:
        if original.lower() != enhanced.lower() and abs(len(original) - len(enhanced)) <= 2:
            return "Spelling"

    # Grammar (verb agreement, tense markers)
    grammar_keywords = ["is", "are", "was", "were", "has", "have", "had"]
    if any(word in enhanced.lower() for word in grammar_keywords):
        return "Grammar"

    # Flow (connector words)
    flow_keywords = ["however", "therefore", "moreover", "thus", "additionally"]
    if any(word in enhanced.lower() for word in flow_keywords):
        return "Flow"

    return "Clarity"


def generate_diff(original_text: str, enhanced_text: str):
    original_words = original_text.split()
    enhanced_words = enhanced_text.split()

    diff = difflib.ndiff(original_words, enhanced_words)

    changes = []

    removed_word = None
    added_word = None

    for token in diff:
        if token.startswith("- "):
            removed_word = token[2:]
        elif token.startswith("+ "):
            added_word = token[2:]

        if removed_word and added_word:
            change_type = classify_change(removed_word, added_word)

            changes.append(
                ChangeItem(
                    original=removed_word,
                    enhanced=added_word,
                    change_type=change_type,
                    reason=f"{change_type} improvement"
                )
            )

            removed_word = None
            added_word = None

    return changes