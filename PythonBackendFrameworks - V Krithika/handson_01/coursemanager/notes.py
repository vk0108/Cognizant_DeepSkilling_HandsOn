'''
1. The GET/api/courses/ request which takes the input action from the client side and renders the list of courses from the database like how we fetch using queries. It returns as a JSON Payload to the client side.

- URL Router : The URL router looks at the URL the user had requested (url path, paramater) and decides which block of code (view) to execute.
- View : In View, the actualy logic happens where is receives the request from the URL router and decides what data is needed to be fetched and it asks the model to fetch that data and bring it back to the view.
- Model : Model represent the database as a Python class. It translated the request into a SQL query to fetch data from the database. The result is handed back to the view.
- Response : The view takes the data from model and builds a final response, and it is displayed via a HTML template.

2. Middleware sits around URL router and view. It is a series of layer that processes the request before it reaches the view and before the response reaches the browser from the view.

Two Django middleware classes : 
- django.contrib.auth.middleware.AuthenticationMiddleware : This run before the request reached the view. It check whether the user is logged in or not by seeing the session data. If logged in, it attaches an object called request.user to the request. So there is no need to write a session look-up code.
- django.contrib.sessions.middleware.SessionMiddleware : This handles reading and writing session data using cookies. When the request comes in, it reads the session cookie from it, looks-up for the matching session in the database and attaches it as request.session. When the response is sent back, the middleware saves those chnages back to the database and makes sure the response has correct session cookie.

3. WSGI and ASGI, both are specifications that define how a python web server can communicate with Python web application like Django. WSGI is only synchronous while ASGI is asynchronous capable.
In WSGI, when one request comes in, it is handled from the start till the end and the worker will be blocked from taking any other request until the ongoing request is completed. But in ASGI, a singke worker can juggle multiple requests at the same time.
In WSGI, each requesnt gets its own thread and whereas in ASGI, a single thread can handle multiple requests.
ASGI supports WebSockets, HTTP long-polling, Server-Sent Events, but WSGO does not.

By default Django uses WSGI. It can still be configured with ASGI, bit it is not the default gateway interface.

4. (M) Model : The data and the rules around it. Talks to the database, defines what fields exist, handles validation.
(V) View : What the user actually sees. (The presentation layer).
(C) Controller : Receives the request, decides what to do, pulls data from the Model, picks a View to render it with.

In MVT,
- Model maps to Model (MVC) only. No changes.
- View maps to Controller (MVC). Django's view is the logical layer which performs many tasks like fetching data, choosing the template, etc. This is Controller's job in MVC.
- Template maps to View (MVC). In MVT, the template is the rpesentation layer i.e., what the user sees. This is View's job in MVC.
'''