import json
import requests
import pytest



@pytest.mark.django_db
def test_getNotes():
   response = requests.get('http://localhost:5000/api/notes')
   assert response.status_code == 200

def test_noteById():
   url = "http://localhost:8000/api/noteById"

   payload = json.dumps({
      "id": 5
   })
   headers = {
      'Content-Type': 'application/json'
   }

   response = requests.request("GET", url, headers=headers, data=payload)
   assert response.status_code == 200

def test_createNote():
   url = "http://localhost:8000/api/createNote"

   payload = json.dumps({
      "noteContent": "this is a test note 2"
   })
   headers = {
      'noteCreatedBy': 'suparna@gmail.com',
      'Content-Type': 'application/json'
   }

   response = requests.request("POST", url, headers=headers, data=payload)
   assert response.status_code == 200

def test_updateNoteById():
   url = "http://localhost:8000/api/updateNoteById"

   payload = json.dumps({
      "noteId": 2,
      "updatedContent": "Had tears in my eyes after watching 12th Fail",
      "noteUpdatedBy": "suparna@gmail.com"
   })
   headers = {
      'Content-Type': 'application/json'
   }

   response = requests.request("PUT", url, headers=headers, data=payload)
   assert response.status_code == 200

def test_deleteNoteById():
   url = "http://localhost:8000/api/deleteNoteById"

   payload = json.dumps({
      "noteId": 1
   })
   headers = {
      'Content-Type': 'application/json'
   }

   response = requests.request("DELETE", url, headers=headers, data=payload)

   assert response.status_code == 200

def test_searchNotes():
   url = "http://localhost:8000/api/searchNote"

   payload = json.dumps({
      "keywords": [
         "tears",
         "hey"
      ]
   })
   headers = {
      'Content-Type': 'application/json'
   }

   response = requests.request("GET", url, headers=headers, data=payload)
   assert response.status_code == 200

def test_shareNotesById():
   url = "http://localhost:8000/api/shareNotesById"

   payload = json.dumps({
      "noteId": 3,
      "noteSharedWith": "suparna@gmail.com"
   })
   headers = {
      'Content-Type': 'application/json'
   }

   response = requests.request("POST", url, headers=headers, data=payload)
   assert response.status_code == 200

