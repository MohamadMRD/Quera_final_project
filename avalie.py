def loginpage(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'ALFA':
        form = forms.LoginForm(request.ALFA)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Login failed!'
    return render(request, 'authentication/login.html', context={'form': form, 'message': message})