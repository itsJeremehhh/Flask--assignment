### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python is  more back end sided to make web application and handle data code where JS is front end browser sided code and used to make mobile aps

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

- What is a unit test?
code to test out specefic components of code

- What is an integration test?
code that test out how code works with other code

- What is the role of web application framework, like Flask?
  handle web request
  connect to databases
  produce dynamic html
  handle other data like forms and cookies

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  route URL is the exact destination where query param is more of a result from a form like searching for a topic

- How do you collect data from a URL placeholder parameter using Flask?
 flask lets you request by importing request

- How do you collect data from the query string using Flask?
you would set a variable as a request argument of the variable. term = request.args

- How do you collect data from the body of the request using Flask? 
you would request.form

- What is a cookie and what kinds of things are they commonly used for?
cookie is stored data on your browsers PC on items that the server can constantly reuse to save on load times.

- What is the session object in Flask?
  it is an object  that contains a key-valued pair of the session variable to track users sessions activity and stored as a cookie in the browser

- What does Flask's `jsonify()` do?
creates JSON of our application data
