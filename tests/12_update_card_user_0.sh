curl -i -X PUT "https://card-backend-sas.herokuapp.com/v1/card" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"id\": \"5f38ec7008a22a6a20833fba\", \"cardname\": \"CardName1Update\",  \"business\": \"ProgUpdate\",  \"cardnumber\": \"123456789\",  \"barcode\": \"987654321\",  \"cardcategory\": \"Sales\"}" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTc0MTIzOTEsIm5iZiI6MTU5NzQxMjM5MSwianRpIjoiODI4OGUzNzEtZTRkOC00MzBmLWE4ZDEtY2RhNzlkN2Y0ZDY1IiwiaWRlbnRpdHkiOiIxMjM0NTYiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ._hxsKnRZEjVwu3RyM-qe5FO3FVdLVLa1V6ydlZXiFU0"
