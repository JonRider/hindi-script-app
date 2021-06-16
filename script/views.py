from django.shortcuts import render

# Views

# Homepage


def index(request):
    """Temporary Main Page. Login Page to become Index"""

    # Return test context
    context = {
        "user": "Jon",
        "level_words": ["पल", "पर", "बल", "बाल", "पाल", "बाप", "नल", "नाल", "नाप", "बन", "बनना", "मानना", "मन", "पान"],
        "level_roman": ["pal", "par", "bal", "baal", "paal", "baap", "nal", "naal", "naap", "ban", "ban-naa", "maan-naa", "man", "paan"],
        "level_letters": ["प", "र", "ब", "ा", "ल", "ग", "क", "न", "म"],

    }

    return render(request, "script/index.html", context)
