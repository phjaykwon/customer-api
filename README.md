
# Customer API
 
The Customer API provides the ability to access data in financial institutions. An application communicates with the Customer API using REST (RESTful Web Services).

A client application initiates REST calls with its credentials to create a session with the server. The API calls are sent to the Financial Institutions to obtain the requested data, and that data is returned to the application. Some functionalities of the API are: get a list of available institutions, manage customer accounts, get customer account transactions, etc.

Customer API calls are contained in views.py.

# Index

/institutions [GET, POST] 
/institutions/{institution_id} [GET]
/institutions/{institution_id}/login [POST]
/institutions/{institution_id}/logins [POST]
/accounts [GET]
/logins/{login_id}/accounts [GET, POST]
/accounts/{account_id} [GET, PUT, DELETE]
/accounts/{account_id}/transactions [GET, POST]
/logins/{login_id} [PUT] 
