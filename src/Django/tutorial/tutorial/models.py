
# Create your views here.
class LanguageViewSet(viewsets.HyperlinkModelViewSet):
    queryset = Language.objects.all() 
    serializer_class = LangSerializer
   