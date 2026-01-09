NEGATION_WORDS = [
    "not", "never", "no", "no longer",
    "refused", "denied", "avoided",
    "without", "against"
]

def negation_conflict(chunk_text, claim_text):
    """
    Returns True if chunk likely contradicts claim via negation.
    """
    chunk_lower = chunk_text.lower()
    claim_lower = claim_text.lower()

    # Check if any negation word appears in chunk
    has_negation = any(neg in chunk_lower for neg in NEGATION_WORDS)

    # Simple lexical overlap check (cheap semantic proxy)
    shared_terms = set(chunk_lower.split()) & set(claim_lower.split())

    if has_negation and len(shared_terms) > 0:
        return True

    return False
##Temporal conflicts
ABSOLUTE_WORDS = [
    "always", "never", "lifelong",
    "since childhood", "forever"
]

TEMPORAL_SHIFT_WORDS = [
    "later", "eventually", "by the end",
    "afterwards", "over time",
    "in his later years", "eventually"
]

def temporal_conflict(chunk_text, claim_text):
    """
    Returns True if chunk suggests a temporal change
    that contradicts an absolute claim.
    """
    chunk_lower = chunk_text.lower()
    claim_lower = claim_text.lower()

    has_absolute = any(word in claim_lower for word in ABSOLUTE_WORDS)
    has_temporal_shift = any(word in chunk_lower for word in TEMPORAL_SHIFT_WORDS)

    if has_absolute and has_temporal_shift:
        return True

    return False
contradictions = 0
supports = 0

for text in top_chunks:
    if negation_conflict(text, claim):
        contradictions += 1
    elif temporal_conflict(text, claim):
        contradictions += 1
    else:
        supports += 1
label = 0 if contradictions > supports else 1
for text in top_chunks:
    if negation_conflict(text, claim):
        print("Negation conflict detected")
    if temporal_conflict(text, claim):
        print("Temporal conflict detected")
