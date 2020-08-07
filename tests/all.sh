curl -i -X POST "http://127.0.0.1:5000/v1/user" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"accountid\": \"123456\",  \"name\": \"Name1\",  \"surname\": \"Surname2\",  \"birthdate\": \"01.01.2020\",  \"gender\": \"Male\",  \"email\": \"name@example.com\"}"

curl -i -X POST "http://127.0.0.1:5000/v1/user" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"accountid\": \"789012\",  \"name\": \"Name2\",  \"surname\": \"Surname3\",  \"birthdate\": \"02.01.2020\",  \"gender\": \"Male\",  \"email\": \"name2@example.com\"}"

curl -i -X POST "http://127.0.0.1:5000/v1/card/123456" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"cardname\": \"CardName1\",  \"business\": \"Prog\",  \"cardnumber\": \"123456789\",  \"barcode\": \"987654321\",  \"cardcategory\": \"Sales\"}"

curl -i -X POST "http://127.0.0.1:5000/v1/card/123456" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"cardname\": \"CardName2\",  \"business\": \"Prog\",  \"cardnumber\": \"1234567892\",  \"barcode\": \"9876543212\",  \"cardcategory\": \"Sales\"}"

curl -i -X POST "http://127.0.0.1:5000/v1/card/789012" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"cardname\": \"CardName1\",  \"business\": \"Prog\",  \"cardnumber\": \"123456789\",  \"barcode\": \"987654321\",  \"cardcategory\": \"Sales\"}"
