from django.shortcuts import render



from joblib import load  #inaleta model
model = load('savedmodels/model.joblib')

def Homeview(request):
    return render(request,'predict.html')

def Ndaniyaform(request):
    temperature = request.POST.get('temperature')
    humidity = request.POST.get('humidity')
    wind = request.POST.get('wind')
    soil = request.POST.get('soil')
    if soil.lower() == 'loam':
        soil=1
    elif soil.lower() == 'clay':
        soil=0
    elif soil.lower()== 'sand':
        soil=2
    elif soil.lower() == 'silt':
        soil = 3


    terrain = request.POST.get('terrain')
    if terrain.lower() == 'lowland':
        terrain = 0
    elif terrain.lower()== 'highland':
        terrain = 1
    elif terrain.lower() == 'lowland ':
        terrain = 0

    y_pred = model.predict([[temperature,humidity,wind,soil,terrain]])
    change = ', '.join(map(str,y_pred))
    if change.lower() == "sunny":
        results ="the farmer should plant crops suitable for sunny conditions or prepare to harvest"
    elif change.lower() == "cloudy":
        results = "the farmer should plan sunlight independent plants"
    elif change.lower() == "rainy":
        results = "the farmer should plant crops suitable for wet conditions"
    elif change.lower() == "snowy":
        results ="the weather is not suitable for planting"
                

    return render(request, 'results.html',{'prediction':change, 'crops':results})
