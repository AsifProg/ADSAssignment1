from django.shortcuts import render,HttpResponse, get_object_or_404, redirect

from .models import Records



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

def delete_record(request, record_id):
    record = get_object_or_404(Records, id=record_id)
    record.delete()
    return redirect('home')
def update_record(request, record_id):
    record = get_object_or_404(Records, id=record_id)
    if request.method == 'POST':
        form = Records(request.POST, instance=record)  # Bind existing data
        if form.is_valid():
            form.save()  # Save updated data
            return redirect('home')  # Redirect to list page
    else:
        form = Records(instance=record)  # Pre-fill form with existing data

    return render(request, 'update_record.html', {'form': form})