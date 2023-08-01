from django.shortcuts import render,redirect
from django.views import View
from .forms import ItemForm
from .models import Item
import logging
    

logger=logging.getLogger("loggers")

class AddItemView(View):

    template_name='app1/Add.html'

    def get(self,request):
        form=ItemForm()
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form=ItemForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('new Item added')
        else:
            logger.error('invalid details  added')
            return redirect('Show_Items')
        return render(request,self.template_name,{'form':form})

class ItemShowView(View):
    template_name='app1/Show.html'

    def get(self,request):
        data=Item.objects.all()
        logger.info('items found')
        return render(request,self.template_name,{'data':data})

class ItemUpdateView(View):
    template_name='app1/Add.html'
    
    def get(self,request,pk):

        obj=Item.objects.get(Number=pk)
        form=ItemForm(instance=obj)

        return render(request,self.template_name,{'form':form})
    
    def post(self,request,pk):
        try:
            obj=Item.objects.get(Number=pk)
            logger.info('Item found')
        except:
            logger.error('invalid item no')
        form=ItemForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            logger.info('record is updated')
        else:
            logger.error('invalid details added')
            return redirect('Show_Items')
        return render(request,self.template_name,{'form':form})
   
class ItemDeleteView(View):
    template_name='app1/Confirm.html'

    def get(self,request,pk):
        return render(request,self.template_name)
    
    def post(self,request,pk):
        try:
            obj=Item.objects.get(Number=pk)
            logger.info('item to be deleted is found')
        except:
            logger.error('invalid item no')
        obj.delete()
        return redirect('Show_Items')
        
        


    
