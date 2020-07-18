# sqreen
*interview exercise for Sqreen*

### Please have a look into [backend folder](backend)

[![loicbaron](https://circleci.com/gh/loicbaron/sqreen.svg?style=svg)](<LINK>)


---
First plug an application to Sqreen and enable the webhook notifications (create a free account on https://my.sqreen.io).

We want to create a Python/Flask application that listen for webhook notifications from Sqreen.

On receiving a notification the application should:  
1 - Check that the signature is correct.  
2 - Redispatch the notification to multiple targets (e.g. log, email, HTTP, SMS, Slack).

Requirements:  
- Have a generic interface for target backends  
- Two target backends  
- Have relevant tests

Hints:  
- The application that is receiving webhook can itself be Sqreened  
- Detected attacks are batched 5-minutely between a running agent and Sqreen own backend (the first one will fire directly, then they are aggregated).  
- One can easily generate a notification by calling: curl -A Arachni/v1.2.1 http://sqreened_application

---
