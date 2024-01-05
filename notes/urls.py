from django.urls import path

from .classes.createNote import createNoteRequestsListener
from .classes.deleteNoteById import deleteNoteByIdRequestsListener
from .classes.registerUser import registerRequestsListener
from .classes.request_listener import RequestsListener
from .classes.getNotes import getNotesRequestsListener
from .classes.getNoteById import getNoteByIdRequestsListener
from .classes.searchNote import searchNoteRequestsListener
from .classes.shareNotesById import shareNoteByIdRequestsListener
from .classes.updateNoteById import updateNoteByIdRequestsListener

urlpatterns = [
    path('test', RequestsListener.as_view({'get': 'test'})),
    path('notes', getNotesRequestsListener.as_view({'get': 'getNotes'})),
    path('noteById', getNoteByIdRequestsListener.as_view({'get': 'getNotesById'})),
    path('createNote', createNoteRequestsListener.as_view({'post': 'createNote'})),
    path('updateNoteById', updateNoteByIdRequestsListener.as_view({'put': 'updateNotesById'})),
    path('deleteNoteById', deleteNoteByIdRequestsListener.as_view({'delete': 'deleteNoteById'})),
    path('searchNote', searchNoteRequestsListener.as_view({'get': 'searchNote'})),
    path('shareNotesById', shareNoteByIdRequestsListener.as_view({'post': 'shareNotesById'})),
    path('register', registerRequestsListener.as_view({'post': 'registerUser'})),



]