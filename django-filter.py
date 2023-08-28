# <!-- Price Range Filter -->

def hotel_list(request):
    # Retrieve filter values from request.GET
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Filter hotels based on price range
    hotels = Hotel.objects.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'hotels': hotels,
        'min_price': min_price,
        'max_price': max_price,
    }

    return render(request, 'your_template.html', context)

# <!-- Facilities Filter -->
  
def hotel_list(request):
    # Retrieve filter choices from request.GET
    has_pool = request.GET.get('has_pool')
    has_gym = request.GET.get('has_gym')
    has_wifi = request.GET.get('has_wifi')
    has_parking = request.GET.get('has_parking')

    # Fetch hotels based on filter choices
    # You can filter the hotels using the selected facilities here

    context = {
        'has_pool': has_pool,
        'has_gym': has_gym,
        'has_wifi': has_wifi,
        'has_parking': has_parking,
    }

    return render(request, 'your_template.html', context)

# <!-- Cities Filter -->

def hotel_search(request):
    # Get all available locations from the Location model
    locations = Location.objects.all()

    context = {
        'locations': locations,
        # Other context variables you might have
    }

    return render(request, 'your_template_name.html', context)

