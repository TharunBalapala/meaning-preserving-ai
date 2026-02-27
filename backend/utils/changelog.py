import difflib

def generate_changelog(original, enhanced):

    original_words = original.split()
    enhanced_words = enhanced.split()

    matcher = difflib.SequenceMatcher(None, original_words, enhanced_words)

    changes = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        for k in range(max(i2 - i1, j2 - j1)):

            o = original_words[i1 + k] if i1 + k < i2 else ""
            e = enhanced_words[j1 + k] if j1 + k < j2 else ""

            if o != e:
                changes.append([o, e, "Correction", "Improved clarity"])

    return changes if changes else [["-", "-", "No Change", "No modification needed"]]