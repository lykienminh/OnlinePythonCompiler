from django.shortcuts import render

import sys

# Create your views here.

# Create index function.

def index(request):
    return render(request, 'index.html')

def runcode(request):
    if request.method == "POST":
        codeareadata = request.POST["codearea"]

        try:
            #save original standard output reference
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')  #change the standard output to the file we created

            #execute code
            exec(codeareadata)

            sys.stdout.close()

            sys.stdout = original_stdout    #reset the standard output to its original 

            #finally read output from file and save in output variable

            output = open('file.txt', 'r').read()

        except Exception as e:
            # to return error in the code
            sys.stdout = original_stdout
            output = e
        
    #finally return and render index page and send codedata and output to show on page
    return render(request, 'index.html', {"code": codeareadata, "output": output})

#URL /python/

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

@api_view(['POST'])
@permission_classes((AllowAny,))
def api_python(request):
    try:
        codeareadata = request.data['codearea']
        #save original standard output reference
        original_stdout = sys.stdout
        sys.stdout = open('file.txt', 'w')  #change the standard output to the file we created

        #execute code
        # codeObject = compile(codeareadata, 'codepython', 'exec')

        # exec(codeObject)
        exec(codeareadata)

        sys.stdout.close()

        sys.stdout = original_stdout    #reset the standard output to its original 

        #finally read output from file and save in output variable

        output = open('file.txt', 'r').read()

    except Exception as e:
        # to return error in the code
        sys.stdout = original_stdout
        output = str(e)
        
    return Response({'output': output})

    # "codearea": "for i in range (2):\n\tprint(\"Hello World!\")\n\tprint(\"Hi\")"

