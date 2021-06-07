from .models import months,teachpaymonths,studentsdetail
from rest_framework.generics import ListAPIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.db.models import Avg, Max, Min,Sum,Count,F
from .serializers import monthsSerializer



@api_view(['GET'])
def allmoneyfromstudents(request,year):
    if request.method == 'GET':
        allmonth = months.objects.filter(years__year=year)
        # monthsss = monthsSerializer(allmonth)
        jan = allmonth.annotate(janur=Sum('january')) 
        feb =   allmonth.annotate(febr=Sum('february'))
        mar =   allmonth.annotate(marc=Sum('march')) 
        apr =   allmonth.annotate(apri=Sum('april')) 
        may =   allmonth.annotate(ma=Sum('may')) 
        june =   allmonth.annotate(jun=Sum('june')) 
        july =   allmonth.annotate(jul=Sum('july')) 
        aug =  allmonth.annotate(augu=Sum('august')) 
        sep =  allmonth.annotate(sept=Sum('september')) 
        octe =  allmonth.annotate(octo=Sum('october')) 
        nov =   allmonth.annotate(nove=Sum('november')) 
        dec =   allmonth.annotate(dece=Sum('december')) 
        monthscount = allmonth.count()
        
        
        jansum,febsum,marsum,maysum,aprsum,junsum,julysum,augsum,sepsum,octsum,novsum,decsum = 0,0,0,0,0,0,0,0,0,0,0,0
        
        for x in range(monthscount):
            jansum += jan[x].janur
            febsum += feb[x].febr
            marsum += mar[x].marc
            aprsum += apr[x].apri
            maysum += may[x].ma
            junsum += june[x].jun
            julysum += july[x].jul
            augsum += aug[x].augu
            sepsum += sep[x].sept
            octsum += octe[x].octo
            novsum += nov[x].nove
            decsum += dec[x].dece
        
        #sumserializer=["OrderedDict"([ ('january', jansum), ('february', febsum), ('march', marsum), ('april', aprsum), ('may', maysum), ('june', junsum), ('july', julysum), ('august', augsum), ('september', sepsum), ('october', octsum), ('november', novsum), ('december', decsum)])]
        # janSum,febsum,marsum,maysum,aprsum,junsum,julysum,augsum,sepsum,octsum,novsum,decsum =str(janSum),str(febsum),str(aprsum),str(marsum),str(maysum),str(junsum),str(julysum),str(augsum),str(sepsum),str(octsum),str(novsum),str(decsum),
        # sumserializer={"jansum": jansum, "febsum": febsum, "marsum": marsum, "aprsum": aprsum, "maysum": maysum, "junsum": junsum, "julsum": julysum, "augsum": augsum, "sepsum": sepsum, "octsum": octsum, "novsum": novsum, "decsum": decsum,"monthscount":monthscount}
        return JsonResponse({'jansum': jansum, 'febsum': febsum, 'marsum': marsum, 'aprsum': aprsum, 'maysum': maysum, 'junsum': junsum, 'julsum': julysum, 'augsum': augsum, 'sepsum': sepsum, 'octsum': octsum, 'novsum': novsum, 'decsum': decsum,'monthscount':monthscount})
        # allstudents = studentsdetail.objects.aggregate(Count('s_name'))
        
        # jan =  months.objects.filter(years__year=2021).annotate(
        #     jan=if F('april') !=  None: 
        #             F('april') 
        #     +F('february'))
        # jan[0].jan

#        