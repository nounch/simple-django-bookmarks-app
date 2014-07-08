# Create your views here.

from notes.models import Note, Cathegory
from notes.models import NoteForm

from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# # No form creation included.
# def index(request):
#     latest_notes_list = Note.objects.all().order_by('-id')
#     return render_to_response('notesBase.html',
#                               {'latest_notes_list': latest_notes_list},)
#                               # context_instance=RequestContext(request))

# Includes Form generation.
def index(request):
    if request.method == 'POST':
        # if request.POST['deleteSubmit'] == 'delete':
        if request.POST.get('deleteSubmit'):
            print '#' * 80
            note = get_object_or_404(Note, pk=request.POST['deleteSubmit'])
            note.delete()
            return HttpResponseRedirect('')
        else:
            newNoteForm = NoteForm(request.POST)
            if newNoteForm.is_valid():
                newNoteForm.save()
                # Returns a redirect to prevent duplicates
                return HttpResponseRedirect('')
    else:
        newNoteForm = NoteForm()

    latest_notes_list = Note.objects.all().order_by('-id')

    # Add pagination
    paginator = Paginator(latest_notes_list, 6)
    page = request.GET.get('page')
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)

    return render_to_response('notesBase.html', {
                              'latest_notes_list': latest_notes_list,
                              'newNoteForm': newNoteForm,
                              'notes': notes,
                              },
                              context_instance=RequestContext(request))

def delete(request, deletion_candidate_id):
    note = get_object_or_404(Note, pk=deletion_candidate_id)
    note.delete()
    return HttpResponseRedirect('')
    # return render_to_response('notesBase.html')

def detail(request, note_id):
    try:
        note = get_object_or_404(Note, pk=note_id)
        description = get_object_or_404(Note, pk=note_id).description
        rating = get_object_or_404(Note, pk=note_id).rating
        url = get_object_or_404(Note, pk=note_id).url
        cathegory = get_object_or_404(Note, pk=note_id).cathegory
    except Note.DoesNotExist:
        raise Http404
    return render_to_response('notesDetail.html',
                              {
            'note': note,
            'description': description,
            'rating': rating,
            'url': url,
            'cathegory': cathegory,
            })

def archive(request):
    notes_list = Note.objects.all().order_by('-rating')
    output = '</br>'.join([p.description for p in notes_list])
    return HttpResponse(output)

def cathegory(request, note_cathegory):
    try:
        cathegory_label = get_object_or_404(Cathegory, label=note_cathegory).label
        cathegory_description = get_object_or_404(Cathegory, label=note_cathegory).description
        cathegory_id = get_object_or_404(Cathegory, label=note_cathegory).id
        cathegorized_notes = Note.objects.filter(cathegory=cathegory_id)
    except Cathegory.DoesNotExist:
        raise Http404
    return render_to_response('cathegoryDetail.html', {
            'cathegory_label': cathegory_label,
            'cathegory_description': cathegory_description,
            'cathegorized_notes': cathegorized_notes,
            })

def rating(request, note_rating):
    try:
        # FIXME: Multiple ratings with same value
        # rating = get_object_or_404(Note, rating=note_rating).rating
        rating = note_rating
        rated_notes = Note.objects.filter(rating=note_rating)
    except Note.DoesNotExist:
        raise Http404
    return render_to_response('ratingDetail.html', {
            'rating': rating,
            'rated_notes': rated_notes,
            })

