from django.shortcuts import render

# Views

# Homepage
def index(request):
    """Temporary Main Page. Login Page to become Index"""

    # Return test context
    context = {
     "test_context": "Testing...",
    }

    return render(request, "script/index.html", context)
