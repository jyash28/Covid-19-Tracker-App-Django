from django.shortcuts import render
import requests
import json


url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "9a4a8d6601msh6023a41c9a0088ap10f7bejsn94f35256c07b",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# print(response.text)

# Create your views here.
def helloworldview(request):
    mylist = []
    noofresults = int(response['results'])
    for x in range(0,noofresults):

        mylist.append(response['response'][x]['country'])

    if request.method=='POST':
        selectedcountry= request.POST['selectedcountry']
        noofresults = int(response['results'])
        # print(selectedcountry)
        for x in range(0,noofresults):
            if selectedcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {
            'selectedcountry':selectedcountry,'mylist':mylist,'new':new, 'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths
        }
        return render(request,'helloworld.html',context)
    noofresults = int(response['results'])
    mylist = []
    for x in range(0,noofresults):
        mylist.append(response['response'][x]['country'])
    context ={
        'mylist':mylist
    }
    return render(request,'helloworld.html',context)
