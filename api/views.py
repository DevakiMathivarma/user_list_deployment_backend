from rest_framework.decorators import api_view
from rest_framework.response import Response

# make 50 users
USERS = [
    {"id": i, "name": f"User {i}", "email": f"user{i}@example.com"}
    for i in range(1, 51)
]

@api_view(["GET"])
def user_list(request):
    # pagination params ?page=1&per_page=10
    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        page = 1
    try:
        per_page = int(request.GET.get("per_page", 10))
    except ValueError:
        per_page = 10

    start = (page - 1) * per_page
    end = start + per_page
    total_pages = (len(USERS) + per_page - 1) // per_page

    return Response({
        "page": page,
        "per_page": per_page,
        "total": len(USERS),
        "total_pages": total_pages,
        "users": USERS[start:end],
    })
