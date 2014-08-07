from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from polls.models import Choice, Poll
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:10]
	return render_to_response('polls/index.html',
				  {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
	p = get_object_or_404(Poll, pk = poll_id)
	return render_to_response('polls/detail.html',
				  {'poll': p},
				  context_instance=RequestContext(request))

def results(request, poll_id, choice_id):
	p = get_object_or_404(Poll,pk = poll_id)
        q = p.choice_set.get(id=choice_id).choice
	return render_to_response('polls/results.html',
				  {'poll': p,
                   'chosen': q})

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render_to_response('polls/detail.html',
					  {'poll': p,
					   'error_message': "Not chosen!"}, context_instance=RequestContext(request))
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls.views.results', args=[p.id, selected_choice.id]))
