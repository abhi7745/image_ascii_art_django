from django.shortcuts import render

# Create your views here.

import pywhatkit

def index(request):

    if request.method=='POST':
        fileimage=request.FILES['file-image']
        print(fileimage)

        pywhatkit.image_to_ascii_art(fileimage,'static/output.txt')

        # donload output file
        return render(request,'index.html',{'success':'success'})
        
    return render(request,'index.html',{})


# def viewer_page(request):

    # media_contents=os.listdir('media/') # colleecting media folder all images
    # print(media_contents)
    # for my_ascii in media_contents:
    #     print(my_ascii,'my_ascii')

    # return render(request,'index.html',{'success':'success'})