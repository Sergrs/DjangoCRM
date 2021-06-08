from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class AgentListView(LoginRequiredMixin, generic.ListView):
    template_list = "agents/agent_list.html"