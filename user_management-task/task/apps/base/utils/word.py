SINGULAR_UNINFLECTED = ['gas', 'asbestos', 'womens', 'childrens', 'sales', 'physics']
SINGULAR_SUFFIX = [
    ('people', 'person'),
    ('men', 'man'),
    ('wives', 'wife'),
    ('menus', 'menu'),
    ('us', 'us'),
    ('ss', 'ss'),
    ('is', 'is'),
    ("'s", "'s"),
    ('ies', 'y'),
    ('ies', 'y'),
    ('es', 'e'),
    ('s', '')
]


def singularize_word( word ):
    for ending in SINGULAR_UNINFLECTED:
        if word.lower().endswith(ending):
            return word
    for suffix, singular_suffix in SINGULAR_SUFFIX:
        if word.endswith(suffix):
            return word[:-len(suffix)] + singular_suffix
    return word
