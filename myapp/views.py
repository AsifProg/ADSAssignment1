from django.shortcuts import render,HttpResponse, get_object_or_404, redirect

from .models import Records
from .forms import RecordForm


def home(request):
    record = Records.objects.all()
    context = {'record': record}
    return render (request,'myapp/homepage.html',context)



def add_record(request):
    if(request.method=='POST'):
        record_id=request.POST.get('recordid')
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')

        rec=Records(first_name=first_name,last_name=last_name,record_id=record_id)
        rec.save();
    return redirect('home')
    #return render (request,'myapp/homepage.html')

def delete_record(request, id):
    record = Records.objects.get(id=id)
    if request.method == "POST":
        record.delete()
    #record = get_object_or_404(Records, id=record_id)
    return redirect('home')
def update_record(request, id):
    record = get_object_or_404(Records, id=id)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecordForm(instance=record)
    return render(request, 'myapp/form.html', {'form': form})
