from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import publicLIKE,publicCOMMENT,publicPOST
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Q
from django.http import JsonResponse


# Create your views here.
@login_required(login_url="login")
def homepage(request):

    get_all_posts=publicPOST.objects.all().order_by('-id')
    
    logout=request.POST.get("logout")
    if logout:
        auth_logout(request)
        return HttpResponseRedirect("/")
    data_dict=[]
    for x in get_all_posts:

        get_all_likes=publicLIKE.objects.filter(post_id=x.id)
        # print("get_all_likes : ",len(get_all_likes))

        get_all_comments=publicCOMMENT.objects.filter(post_id=x.id)

        is_user_liked_the_post=publicLIKE.objects.filter(Q(LIKER_details=request.user)&Q(post_id=x.id))
        get_last_three_comments=publicCOMMENT.objects.filter(post_id=x.id).order_by('-id')[:3:-1]
        # print("++++++++++++++ : ",is_user_liked_the_post)

        data_dict.append({x.id:[{"post_details":x,"no_of_likes":len(get_all_likes),"no_of_comments":len(get_all_comments),"last_three_comments":get_last_three_comments,"liked_dta":get_all_likes,"is_user_liked_the_post":True if is_user_liked_the_post else False }]})

    # print("posts are : ",data_dict)

    data={
        "user_id":request.user.id,
        "posts":data_dict
    }
    # print("-------- : ",request.user.id)
    return render(request,"index.html",data)



def login(request):
    user_id=request.POST.get("mobile_no")
    password=request.POST.get("user_password")
    print("user _id : ",user_id)
    print("password : ",password)
    if user_id:
        user_check=authenticate(request,username=user_id,password=password)
        # print("user check : ",user_check)
        if user_check is not None:
                auth_login(request, user_check)
                # print("------------- : ",user_check)
                return HttpResponseRedirect("/")
        else:
            res_data={
            "login": False
            }
            print("Failed to login")
            return render(request,"login.html",res_data)
        


    return render(request,"login.html")
    


def signup(request):
    if request.method == 'POST': 
        umobile=request.POST.get("user_mobile")
        upassword=request.POST.get("user_password")
        print("we get data from FE is : ",umobile,upassword)
        if (umobile and upassword):
            try:
                check_for_user_exist=User.objects.get(username=str(umobile))
                if check_for_user_exist:
                    data={
                        "user_already_exist":True
                    }
                    return render(request,'signup.html',data)
            except:
                register_USER=User.objects.create_user(username=str(umobile),password=upassword)
                register_USER.save()
                user_check=authenticate(request,username=umobile,password=upassword)
                auth_login(request, user_check)


                data={
                        "user_created":True
                    }
                return HttpResponseRedirect("/")
    return render(request,'signup.html')

@csrf_exempt
def likes(request):
    get_user=User.objects.get(id=request.user.id)
    post_id_data=str(request.POST.get("post_id")).split("like_btn")[1]
    print("post id is : ",post_id_data)
    user_liked=publicLIKE.objects.create(
        LIKER_details=get_user,
        post_id=publicPOST.objects.get(id=int(post_id_data)))
    user_liked.save()
    return HttpResponse("success")

@csrf_exempt
def dislike(request):
    post_id_data=str(request.POST.get("post_id")).split("like_btn")[1]
    remove_like=publicLIKE.objects.filter(Q(LIKER_details=User.objects.get(id=request.user.id))&Q(post_id=post_id_data)).delete()
    print("id removed")
    return HttpResponse("success")



@csrf_exempt
def comments(request):
    dataa=request.POST.get("comment_data")
    post_id_data=request.POST.get("post_id")
    print("data : ",post_id_data)
    add_commenter=publicCOMMENT.objects.create(
        commenter_details=User.objects.get(id=request.user.id),
        post_id=publicPOST.objects.get(id=int(post_id_data)),
        text=dataa
    )
    print("successfully commented")
    return HttpResponse("success")



@csrf_exempt
def posts(request):
    dataa=request.POST.get("question_asked")
    data_image=request.FILES.get("post_image")
    print("data : ",dataa)
    print("data_image : ",data_image)
    if data_image:
        cre_data=publicPOST.objects.create(user_id=User.objects.get(id=request.user.id),post_content=dataa,post_image=data_image,is_question=False)
        cre_data.save()
    else:
        cre_data=publicPOST.objects.create(user_id=User.objects.get(id=request.user.id),post_content=dataa)
        cre_data.save()
    return HttpResponse("success")