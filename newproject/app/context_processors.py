def add_user_to_context(request):
    return {
        'username': request.user.username if request.user.is_authenticated else 'Guest'
    }