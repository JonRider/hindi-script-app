from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
#from django.contrib.auth.models import User

# Views


def index(request):
    """Temporary Main Page. Login Page to become Index"""

    if not request.user.is_authenticated:
        return render(request, "script/login.html")

    if request.method == "POST":
        level = int(request.POST["level"])
    else:
        level = 1

    # Return test context
    if level == 2:
        context = {
            "level": level,
            "level_words": ["रब", "गाना", "सर", "दास", "पाल", "बाप", "नल", "नाल", "नाप", "बन", "बनना", "मानना", "मन", "पान"],
            "level_roman": ["rab", "gaana", "sar", "daas", "paal", "baap", "nal", "naal", "naap", "ban", "ban-naa", "maan-naa", "man", "paan"],
            "level_letters": ["ग", "स", "प", "र", "ब", "ा", "ल", "ग", "क", "न", "म"],

        }
    else:
        context = {
            "level": level,
            "level_words": ["पल", "पर", "बल", "बाल", "पाल", "बाप", "नल", "नाल", "नाप", "बन", "बनना", "मानना", "मन", "पान"],
            "level_roman": ["pal", "par", "bal", "baal", "paal", "baap", "nal", "naal", "naap", "ban", "ban-naa", "maan-naa", "man", "paan"],
            "level_letters": ["प", "र", "ब", "ा", "ल", "ग", "क", "न", "म"],

        }

    return render(request, "script/index.html", context)


def login(request):
    """Login Page. If user not authenticated they are directed here."""

    # Automatically Redirect Logged in users to the main page
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    return render(request, "script/login.html")


def logout_view(request):
    """Logout user."""
    logout(request)
    return render(request, "script/login.html")
