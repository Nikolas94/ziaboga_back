import datetime

from django.shortcuts import render, redirect

# Create your views here.
# ViewSets define the view behavior.
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.utils import json

from data_manager.models import Erabiltzailea, Egutegia, Estropada, Kiniela, Taldea, GremErab, Gremioa, ErabPunt
from data_manager.serializers import ErabiltzaileaSerializer, EgutegiaSerializer, GlobalaSerializer, TaldeakSerializer


class ErabiltzaileZerrenda(ListAPIView):
    queryset = Erabiltzailea.objects.all()
    serializer_class = ErabiltzaileaSerializer

@permission_classes([AllowAny])
class ErabiltzaileaViewSet(viewsets.ModelViewSet):
    queryset = Erabiltzailea.objects.all()
    serializer_class = ErabiltzaileaSerializer

@permission_classes([AllowAny])
class EgutegiaViewSet(viewsets.ModelViewSet):
    queryset = Egutegia.objects.all().order_by("estropadaZenbakia")
    serializer_class = EgutegiaSerializer

@permission_classes([AllowAny])
class GlobalaViewSet(viewsets.ModelViewSet):
    queryset = ErabPunt.objects.all().order_by("-puntuak")
    serializer_class = GlobalaSerializer

@permission_classes([AllowAny])
class TaldeakViewSet(viewsets.ModelViewSet):
    queryset = Taldea.objects.all()
    serializer_class = TaldeakSerializer

def egutegiaDeskargatu(request):
    #FOR BAT EGIN BEHARKO DA ERREGISTROAK BANAN BANAN GORDETZEKO
    egutegia = Egutegia(estropadaZenbakia="1",estropadaIzena="1",lekua="1",eguna="2025-80-10",liga="ACT")
    egutegia.save()

def estropadaDeskargatu(request):
    estropadaIzena="lekeitio"
    postua = "lekeitio"
    taldeIzena = "lekeitio"
    denbora = "lekeitio"
    diferentzia = "lekeitio"
    puntuak = "lekeitio"
    estropada = Estropada(estropadaIzena,postua,taldeIzena,denbora,diferentzia,puntuak)
    estropada.save()


def datuak(request):
    print("datuak bistaratuko ziren")
    puntuazioaEzarri()
    return redirect('127.0.0.1:8000')

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def datuak_apiView(request):
    """
    List all code datuak, or create a new snippet.
    """
    # if request.method == 'GET':
    #     snippets = Snippet.objects.all()
    #     serializer = SnippetSerializer(snippets, many=True)
    #     return Response(serializer.data)

    if request.method == 'POST':
        print(request.data)
        val = request.data
        print(val["id"])
        a="DPM"
        x = '{ "name":"John", "age":30, "city":"New York"}'
        y = json.loads(x)
        # serializer = SnippetSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(status=status.HTTP_200_OK)
        return Response(y)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def erregistratu_apiView(request):

    if request.method == 'POST':

        val = request.data
        erabiltzaileDenak = Erabiltzailea.objects.all()

        for eraDenak in erabiltzaileDenak:
            if Erabiltzailea.objects.filter(motea=val["motea"]).exists():
                x = '{ "mezua":"existitzenDa"}'
                y = json.loads(x)
                return Response(y)


        erabiltzaileIzena = val["erabiltzaileIzena"]
        erabiltzaileAbizena = val["erabiltzaileAbizena"]
        motea = val["motea"]
        pasahitza = val["pasahitza"]
        email = val["email"]
        telefonoa = val["telefonoa"]
        erabiltzailea = Erabiltzailea(erabiltzaileIzena=erabiltzaileIzena, erabiltzaileAbizena=erabiltzaileAbizena, motea=motea,
                                      pasahitza=pasahitza, email=email, telefonoa=telefonoa)
        erabiltzailea.save()

        eraPuntEus = ErabPunt(motea=motea,liga="EUS",puntuak="0")
        eraPuntEus.save()
        eraPuntAct = ErabPunt(motea=motea,liga="ACT",puntuak="0")
        eraPuntAct.save()

        x = '{ "mezua":"erabiltzailea ondo sortu da"}'
        y = json.loads(x)
        return Response(y)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def gremioaSortu_apiView(request):

    if request.method == 'POST':

        val = request.data
        gremioDenak = Gremioa.objects.all()

        for gremDenak in gremioDenak:
            if Gremioa.objects.filter(gremioIzena=val["gremioIzena"]).exists():
                x = '{ "mezua":"existitzenDa"}'
                y = json.loads(x)
                return Response(y)

        gremioIzena = val["gremioIzena"]
        pasahitza = val["pasahitza"]
        motea = val["motea"]
        gremioa = Gremioa(gremioIzena=gremioIzena, pasahitza=pasahitza, gremioAdmin=motea)
        gremioa.save()

        gremErab = GremErab(gremioIzena=gremioIzena,motea=motea)
        gremErab.save()

        x = '{ "mezua":"Gremioa ondo sortu da"}'
        y = json.loads(x)
        return Response(y)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def gremioanSartu_apiView(request):

    if request.method == 'POST':

        val = request.data
        gremioDenak = Gremioa.objects.all()

        for gremDenak in gremioDenak:
            if Gremioa.objects.filter(gremioIzena=val["gremioIzena"],pasahitza=val["pasahitza"]).exists():
                if GremErab.objects.filter(gremioIzena=val["gremioIzena"],motea=val["motea"]):
                    x = '{ "mezua":"existitzenDa"}'
                    y = json.loads(x)
                    return Response(y)
                else:
                    gremErab = GremErab(gremioIzena=val["gremioIzena"], motea=val["motea"])
                    gremErab.save()

                    x = '{ "mezua":"Erabiltzailea ondo gehitu da"}'
                    y = json.loads(x)
                    return Response(y)


        x = '{ "mezua":"Gremioa edo pasahitza gaizki"}'
        y = json.loads(x)
        return Response(y)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


'''
Erabiltzaile batek bere motea eta pasahitza sartzerakoan erabiltzaile horren dituen gremioak itzuliko ditu
'''
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def erabiltzaileaEgiaztatu_apiView(request):
    puntuazioaEzarri()
    if request.method == 'POST':

        val = request.data
        erabiltzaileDenak = Erabiltzailea.objects.all()
        kont = 0
        jsonGremioak={"mezua":"Datu zuzenak"}
        for eraDenak in erabiltzaileDenak:
            if Erabiltzailea.objects.filter(motea=val["motea"], pasahitza=val["pasahitza"]).exists():
                return Response(jsonGremioak)
                # if GremErab.objects.filter(motea=val["motea"]):
                #     for a in GremErab.objects.filter(motea=val["motea"]):
                #         kont = kont + 1
                #         zenb=str(kont)
                #
                #         auxJson=jsonGremioak
                #         srtGremioak = '{"g'+zenb+'":"'+a.gremioIzena+'"}'
                #         jsonGremioak = json.loads(srtGremioak)
                #         jsonGremioak.update(auxJson)
                #
                #     kopStr='{"kop":"'+zenb+'"}'
                #     kopJson=json.loads(kopStr)
                #     jsonGremioak.update(kopJson)
                #     return Response(jsonGremioak)
                # else:
                #     errStr = '{"mezua":"Ez dago gremio bakar batean"}'
                #     errJson = json.loads(errStr)
                #     return Response(errJson)

            else:
                errStr = '{"mezua":"Datuak gaizki idatzita daude"}'
                errJson = json.loads(errStr)
                return Response(errJson)
                # return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def gremiokoAurkariak_apiView(request):

    if request.method == 'POST':

        val = request.data
        gremiokoAurkariak = GremErab.objects.all()
        kont = 0
        taulak = 0
        jsonGremioak = {"mezua": "Datu zuzenak"}

        jsonG = {"mezua": "Datu zuzenak"}
        k=0
        gremioKop=0

        for eraDenak in gremiokoAurkariak:
            if GremErab.objects.filter(motea=val["motea"]).exists():
                moteGremio = GremErab.objects.filter(motea=val["motea"]).order_by("gremioIzena")

                for gremioa in moteGremio:
                    erabiltzaileak = GremErab.objects.filter(gremioIzena=gremioa.gremioIzena).order_by("motea")

                    z = str(gremioKop)
                    print("gremioa"+z+":" + gremioa.gremioIzena)
                    gremStr = '{"gremioa' + z + '":"' + gremioa.gremioIzena + '"}'
                    gremJson = json.loads(gremStr)
                    jsonG.update(gremJson)

                    gremioko = 0



                    for era in erabiltzaileak:

                        # denak = ErabPunt.objects.filter(motea=era.motea)
                        # ordenatutaDenak = sorted(denak, key=lambda x: x.puntuak, reverse=True)
                        # # filtratuta = filter(lambda motea: motea==era.motea, ordenatutaDenak)
                        #
                        # print("*****")
                        # for e in ordenatutaDenak:
                        #     print("Fil: "+e.motea + str(e.puntuak) + e.liga)
                        # print("*****")

                        motePunt = ErabPunt.objects.filter(motea=era.motea)
                        k2 = str(k)

                        print("motea"+k2+":"+era.motea)
                        motStr = '{"motea' + k2 + '":"' + era.motea + '"}'
                        motJson = json.loads(motStr)
                        jsonG.update(motJson)


                        for punt in motePunt:

                            print(""+punt.liga+k2+":"+str(punt.puntuak))
                            punStr = '{"'+punt.liga+ k2 + '":"' + str(punt.puntuak) + '"}'
                            punJson = json.loads(punStr)
                            jsonG.update(punJson)

                        print("------------")
                        k=k+1
                        gremioko=gremioko+1

                    print("mul"+z+":"+str(gremioko))
                    mulStr = '{"mul' + z + '":"' + str(gremioko) + '"}'
                    mulJson = json.loads(mulStr)
                    jsonG.update(mulJson)

                    gremioKop = gremioKop + 1
                # print("Erabiltzaile Kopurua: " + k2)

                print("Gremio Kopurua: "+str(gremioKop))
                tauStr = '{"taulak":"' + str(gremioKop) + '"}'
                tauJson = json.loads(tauStr)
                jsonG.update(tauJson)



                print(jsonG)

                return Response(jsonG)




                # for gremioa in moteGremio:
                #     gremioak = ErabPunt.objects.filter(motea=gremioa.motea)
                #     # print("gremioak: "+gremioa.gremioIzena)
                #
                #     kant=str(len(gremioak))
                #     mulStr = '{"mul'+str(taulak)+'":"' + kant + '"}'
                #     mulJson = json.loads(mulStr)
                #     jsonGremioak.update(mulJson)
                #     taulak = taulak + 1
                #
                #     o = sorted(gremioak, key=lambda x: x.puntuak, reverse=True)
                #     for erabiltzailea in o:
                #         zenb = str(kont)
                #
                #         auxJson = jsonGremioak
                #         srtGremioak = '{"motea' + zenb + '":"' + erabiltzailea.motea + '","gremioa' + zenb + '":"' + gremioa.gremioIzena + '","liga' + zenb + '":"' + erabiltzailea.liga + '","puntuak' + zenb + '":"' + str(
                #             erabiltzailea.puntuak) + '"}'
                #         kont = kont + 1
                #         jsonGremioak = json.loads(srtGremioak)
                #         jsonGremioak.update(auxJson)
                # kopStr = '{"kop":"' + zenb + '"}'
                # kopJson = json.loads(kopStr)
                # jsonGremioak.update(kopJson)
                #
                # tauStr = '{"taulak":"' + str(taulak) + '"}'
                # tauJson = json.loads(tauStr)
                # jsonGremioak.update(tauJson)
                #
                # return Response(jsonGremioak)


            else:
                errStr = '{"mezua":"Datuak gaizki idatzita daude"}'
                errJson = json.loads(errStr)
                return Response(errJson)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# '''
# Gremio zehartz bateko datuak itzuliko ditu
# '''
#
# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
# def gremiokoAurkariak_apiView(request):
#
#     if request.method == 'POST':
#
#         val = request.data
#         gremiokoAurkariak = GremErab.objects.all()
#         kont = 0
#         taulak = 0
#         jsonGremioak = {"mezua": "Datu zuzenak"}
#         for eraDenak in gremiokoAurkariak:
#             if GremErab.objects.filter(motea=val["motea"]).exists():
#                 moteduna = GremErab.objects.filter(motea=val["motea"]).order_by("gremioIzena").order_by("liga")
#                 for gremiodunak in moteduna:
#                     gremioak = GremErab.objects.filter(gremioIzena=gremiodunak.gremioIzena, liga=gremiodunak.liga)
#
#                     kant=str(len(gremioak))
#                     mulStr = '{"mul'+str(taulak)+'":"' + kant + '"}'
#                     mulJson = json.loads(mulStr)
#                     jsonGremioak.update(mulJson)
#                     taulak = taulak + 1
#
#                     o = sorted(gremioak, key=lambda x: x.puntuak, reverse=True)
#                     for erabiltzailea in o:
#                         zenb = str(kont)
#
#                         auxJson = jsonGremioak
#                         srtGremioak = '{"motea' + zenb + '":"' + erabiltzailea.motea + '","gremioa' + zenb + '":"' + erabiltzailea.gremioIzena + '","liga' + zenb + '":"' + erabiltzailea.liga + '","puntuak' + zenb + '":"' + str(
#                             erabiltzailea.puntuak) + '"}'
#                         kont = kont + 1
#                         jsonGremioak = json.loads(srtGremioak)
#                         jsonGremioak.update(auxJson)
#                 kopStr = '{"kop":"' + zenb + '"}'
#                 kopJson = json.loads(kopStr)
#                 jsonGremioak.update(kopJson)
#
#                 tauStr = '{"taulak":"' + str(taulak) + '"}'
#                 tauJson = json.loads(tauStr)
#                 jsonGremioak.update(tauJson)
#
#                 return Response(jsonGremioak)
#
#
#             else:
#                 errStr = '{"mezua":"Datuak gaizki idatzita daude"}'
#                 errJson = json.loads(errStr)
#                 return Response(errJson)
#                 return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

'''
Kiniela bat gordetzen du
'''
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def kinielaBete_apiView(request):

    if request.method == 'POST':

        val = request.data
        kinielaDenak = Kiniela.objects.all()

        for eraDenak in kinielaDenak:
            if Kiniela.objects.filter(motea=val["motea"],estropadaIzena=val["estropadaIzena"]).exists():
                Kiniela.objects.filter(motea=val["motea"],estropadaIzena=val["estropadaIzena"]).delete()

                #gremioIzena = val["gremioIzena"]
                motea = val["motea"]
                estropadaIzena = val["estropadaIzena"]
                bat = val["bat"]
                bi = val["bi"]
                hiru = val["hiru"]
                lau = val["lau"]
                bost = val["bost"]
                sei = val["sei"]
                zazpi = val["zazpi"]
                zortzi = val["zortzi"]
                bederatzi = val["bederatzi"]
                hamar = val["hamar"]
                hamaika = val["hamaika"]
                hamabi = val["hamabi"]
                liga = val["liga"]
                puntuak = val["puntuak"]

                kiniela = Kiniela(motea=motea, estropadaIzena=estropadaIzena,
                                  bat=bat, bi=bi, hiru=hiru, lau=lau, bost=bost, sei=sei, zazpi=zazpi,
                                  zortzi=zortzi, bederatzi=bederatzi, hamar=hamar, hamaika=hamaika,
                                  hamabi=hamabi, liga=liga, puntuak=puntuak)
                kiniela.save()

                x = '{ "mezua":"Apostua eguneratuta!"}'
                y = json.loads(x)
                return Response(y)

        # gremioIzena = val["gremioIzena"]
        motea = val["motea"]
        estropadaIzena = val["estropadaIzena"]
        bat = val["bat"]
        bi = val["bi"]
        hiru = val["hiru"]
        lau = val["lau"]
        bost = val["bost"]
        sei = val["sei"]
        zazpi = val["zazpi"]
        zortzi = val["zortzi"]
        bederatzi = val["bederatzi"]
        hamar = val["hamar"]
        hamaika = val["hamaika"]
        hamabi = val["hamabi"]
        liga = val["liga"]
        puntuak = val["puntuak"]

        kiniela = Kiniela(motea=motea, estropadaIzena=estropadaIzena,
                                      bat=bat, bi=bi, hiru=hiru, lau=lau, bost=bost, sei=sei, zazpi=zazpi,
                                      zortzi=zortzi, bederatzi=bederatzi, hamar=hamar, hamaika=hamaika,
                                      hamabi=hamabi,liga=liga, puntuak=puntuak)
        kiniela.save()

        x = '{ "mezua":"Apostua ondo sortu da"}'
        y = json.loads(x)
        return Response(y)
'''
Apostatutakoa orden pertsonala itzultzen du
'''
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def estropadakoEmaitza_apiView(request):

    if request.method == 'POST':

        val = request.data
        estropadaDenak = Estropada.objects.all()
        kont = 0
        jsonApostua={"mezua":"Datu zuzenak"}
        a=val["estropadaIzena"]

        for esDenak in estropadaDenak:
            if Estropada.objects.filter(estropadaIzena=val["estropadaIzena"]).exists():
                for a in Estropada.objects.filter(estropadaIzena=val["estropadaIzena"]):
                    kont = kont + 1
                    zenb = str(kont)

                    auxJson = jsonApostua
                    srtApostuak = '{"p' + zenb + '":"' + a.taldeIzena + '"}'
                    jsonApostua = json.loads(srtApostuak)
                    jsonApostua.update(auxJson)

                kopStr = '{"kop":"' + zenb + '"}'
                kopJson = json.loads(kopStr)
                jsonApostua.update(kopJson)
                return Response(jsonApostua)
            else:
                errStr = '{"mezua":"Ez da estropada egin oraindik"}'
                errJson = json.loads(errStr)
                return Response(errJson)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def kinielaJaso_apiView(request):

    if request.method == 'POST':

        val = request.data
        kont = 0
        jsonKiniela={"mezua":"Datu zuzenak"}

        if Kiniela.objects.filter(motea=val["motea"],estropadaIzena=val["estropadaIzena"]).exists():
            for a in Kiniela.objects.filter(motea=val["motea"],estropadaIzena=val["estropadaIzena"]):
                print(a.motea)
                print(a.estropadaIzena)
                auxJson = jsonKiniela
                srtGremioak = '{"bat":"' + a.bat + '","bi":"' + a.bi + '","hiru":"' + a.hiru + '","lau":"' + a.lau + '","bost":"' + a.bost + '","sei":"' + a.sei + '","zazpi":"' + a.zazpi + '","zortzi":"' + a.zortzi + '","bederatzi":"' + a.bederatzi + '","hamar":"' + a.hamar + '","hamaika":"' + a.hamaika + '","hamabi":"' + a.hamabi + '"} '
                jsonGremioak = json.loads(srtGremioak)
                jsonGremioak.update(auxJson)
                print(jsonGremioak)


            return Response(jsonGremioak)
        else:
            errStr = '{"mezua":"Ez dago kiniela jarrita"}'
            errJson = json.loads(errStr)
            return Response(errJson)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def taldeakJaso_apiView(request):

    if request.method == 'POST':

        val = request.data
        erabiltzaileDenak = Erabiltzailea.objects.all()
        kont = 0
        print(val["liga"])
        jsonGremioak={"mezua":"Datu zuzenak"}
        for eraDenak in erabiltzaileDenak:
            if Taldea.objects.filter(liga=val["liga"]).exists():
                if Taldea.objects.filter(liga=val["liga"]):
                    for a in Taldea.objects.filter(liga=val["liga"]):
                        kont = kont + 1
                        zenb=str(kont)

                        auxJson=jsonGremioak
                        srtGremioak = '{"t'+zenb+'":"'+a.taldeIzena+'"}'
                        jsonGremioak = json.loads(srtGremioak)
                        jsonGremioak.update(auxJson)

                    kopStr='{"kop":"'+zenb+'"}'
                    kopJson=json.loads(kopStr)
                    jsonGremioak.update(kopJson)
                    return Response(jsonGremioak)
                else:
                    errStr = '{"mezua":"Ez dago gremio bakar batean"}'
                    errJson = json.loads(errStr)
                    return Response(errJson)

            else:
                errStr = '{"mezua":"Datuak gaizki idatzita daude"}'
                errJson = json.loads(errStr)
                return Response(errJson)
                # return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def puntuazioaEzarri():

    #val = request.data

    egutegia = Egutegia.objects.all()

    estropadaIzena = "Lekeitioko estropada"
    motea = "txantxo"
    liga = "ACT"

    for egEs in egutegia:
        print("estropadaIzenaEgutegia: "+egEs.estropadaIzena)
        #TODO: Kontrolatu fetxa IF batekin

        #TODO/

        estropada = Estropada.objects.filter(estropadaIzena=egEs.estropadaIzena)
        esEma=[]
        k=1
        for es in estropada:
            esEma.append([k,es.taldeIzena])
            k=k+1
        print("Estropada emaitza: ")
        for es in esEma:
            print(str(es[0])+"-"+es[1])

        kinielakEstropadako = Kiniela.objects.filter(estropadaIzena=egEs.estropadaIzena)
        kiEma=[]
        k=1
        for eraEs in kinielakEstropadako:
            kiEma.clear()
            kiEma.append([k, eraEs.bat])
            kiEma.append([k+1, eraEs.bi])
            kiEma.append([k+2, eraEs.hiru])
            kiEma.append([k+3, eraEs.lau])
            kiEma.append([k+4, eraEs.bost])
            kiEma.append([k+5, eraEs.sei])
            kiEma.append([k+6, eraEs.zazpi])
            kiEma.append([k+7, eraEs.zortzi])

            liga = eraEs.liga
            if liga == "ACT":
                kiEma.append([k+8, eraEs.bederatzi])
                kiEma.append([k+9, eraEs.hamar])
                kiEma.append([k+10, eraEs.hamaika])
                kiEma.append([k+11, eraEs.hamabi])
            print(eraEs.motea+"-ren kiniela:")
            for d in kiEma:
                print(str(d[0])+"/"+d[1])
            igarri = 0
            hutzBat = 0
            hutzBi = 0
            ezIgarri = 0
            difPuntuetan=0
            print(eraEs.motea + "-ren igarketak:")
            for es in esEma:
                #print("es: "+es[1]+" pos: "+str(es[0]))

                for ki in kiEma:
                    #print("ki: " + ki[1]+" pos: "+str(ki[1]))
                    if es[1].__eq__(ki[1]):
                        if es[0]==ki[0]:
                            print(es[1]+" == "+ki[1])
                            igarri+=1
                            break
                        else:
                            dif=es[0]-ki[0]
                            if dif<0:
                                dif=dif*(-1)
                            if dif==1:
                                hutzBat+=1
                            elif dif==2:
                                hutzBi+=1
                            else:
                                ezIgarri+=1
                            difPuntuetan+=dif
                            print("Diferentzia: " + str(dif))

            print("Igarri: " + str(igarri))
            print("hutzBat: " + str(hutzBat))
            print("hutzBi: " + str(hutzBi))
            print("ezIgarri: "+str(ezIgarri))

            ################ Ondo=3, Fallo bat=1, Txarto= x!(Negatibauan)
            # neg=0
            # ran = range(ezIgarri)
            # for i in ran:
            #     neg+=1
            #     neg+=i
            # puntuak=(igarri*3)+(hutzBat)+(-1*neg)
            ################

            ################ Ondo=3, Fallo bat=1, Fallo bi=0, Txarto= x!(Negatibauan)
            neg=0
            ran = range(ezIgarri)
            for i in ran:
                neg+=1
                neg+=i
            puntuak=(igarri*3)+(hutzBat)+(-1*neg)
            ################

            ################ Ondo=3, Fallo bat=1, Txarto= -2
            #puntuak = (igarri * 3) + (hutzBat) + (-2 * ezIgarri)
            ################

            ################ 12 punto - diferentzia
            # puntuak=144-difPuntuetan
            # print("Puntuazioa: " + str(puntuak))
            ################

            print("Puntuazioa: "+str(puntuak))

            eraEs.puntuak=puntuak
            eraEs.save()

            erabPunt = ErabPunt.objects.filter(motea=eraEs.motea,liga=eraEs.liga)
            for erPu in erabPunt:
                #erPu.puntuak=0
                erPu.puntuak+=puntuak
                erPu.save()
            print("/////////")

        print("******")



        #kiniela = Kiniela.objects.filter(estropadaIzena=val["estropadaIzena"],motea=val["motea"], liga=val["liga"])
        #estropada=Estropada.objects.filter(estropadaIzena=val["estropadaIzena"],liga=val["liga"])


















