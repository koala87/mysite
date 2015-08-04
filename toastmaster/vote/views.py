from django.shortcuts import render_to_response

def home(request):


        # description, icon, page, disable
        path = '/static/pic/'
        modules = [
            ['Vote Best', 'vote.jpg', 'vote', False],
            ['Brain Timer', 'timer.jpg', 'timer', False],
            ['CC Manual', 'cc.jpg', 'cc_manual', False],
            ['CL Manual', 'cl.jpg', 'cl_manual', False],
            ['Hot News', 'news.jpg', 'news', True],
            ['Find Clubs', 'club.jpg', 'club', True],
            ['Star Member', 'people.jpg', 'people', True],
            ['Champion Video', 'video.jpg', 'video', True],
            ['Training Sign up', 'sign.jpg', 'sign', True],
        ] 
        for i in modules:
            i[1] = path + i[1]

        tmp = []
        for i in modules:
            tmp.append(i[1])

        return render_to_response('home.html', {'items':tmp, 'num':3})
    


