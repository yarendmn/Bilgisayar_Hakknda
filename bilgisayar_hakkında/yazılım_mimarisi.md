# YAZILIM ARCHİTECTURE BASİCS
## Monolith vs Microservice
![vs](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTx4Eh2S43YWm3f_jV2DK5btcrohyXDCYcUhafg_J8dVw&s=10 "Monolith vs Microservice")


A monolithic architecture is a model that uses one code base to perform multiple business functions. All the software components in a monolithic system are cooperate due to the data exchange mechanisms within the system. In contrast, microservices are an architectural approach that composes software into small independent components or services that communicate via APIs and handle their own specific functions and data.

**Key differences: monolithic vs. microservices**

Monolithic applications typically consist of a client-side UI, a database, and a server-side application. Developers build all of these modules on a single code base.

On the other hand, in a distributed architecture, each microservice works to accomplish a single feature or business logic. Instead of exchanging data within the same code base, microservices communicate with APIs.
## Architectural Patterns such as MVS and MVVM

Architectural patterns organize code to separate concerns, resulting in cleaner, testable, and maintainable codebases. Here is a concise breakdown of the two most prominent patterns for web and mobile development.

### MVC (MODEL VİEW CONTROLLER)

The pioneer of separation of concerns, heavily used in traditional web frameworks and straightforward mobile apps.

Model: Manages application data and core business logic.

View: Displays the UI to the user.

Controller: Acts as the mediator. It intercepts user input, updates the Model, and manually refreshes the View.

The Verdict: Best for straightforward applications requiring rapid development. It is easy to implement upfront but can become cumbersome if the app has highly complex, dynamic UI requirements.

### MVVM (Model-View-ViewModel)

The modern standard for cross-platform and reactive development (e.g., Flutter, React, Xamarin).

Model: Manages data and business logic.

View: Displays data and captures user interaction.

ViewModel: Connects the Model and View via two-way data binding. If the data changes, the UI updates automatically, and vice versa.

The Verdict: Best for data-heavy applications requiring real-time UI synchronization. It eliminates the need to write boilerplate code just to update UI elements manually

## What is a State Management?

State management is the process of handling, storing, and updating the data that determines an application’s behavior and user interface at any given moment.

**What is "State"?**

* Definition: State is any piece of data that can change while a program runs.
* Examples: User input in a text box, whether a dark mode toggle is on, a shopping cart list, or data fetched from a server.
* Role: It acts as the memory of an application, deciding what the user sees and how the app reacts to actions.

**Types of State**

* Local State: Data used by only one specific component or part of the user interface (like an open/closed dropdown menu).
* Global State: Data shared across many different components or pages (like a logged-in user's profile information)

## Layered Architecture (service-repository-controller)

The Controller-Service-Repository pattern is a layered software architecture that splits a backend application into three distinct levels to achieve a strict separation of concerns.Data flows linearly through the system: the Client talks to the Controller, the Controller calls the Service, the Service requests data from the Repository, and the Repository interacts directly with the Database.

1. Controller Layer (Presentation / API Layer)

The Controller is the external gatekeeper of your application. Its only job is to handle communications coming from the outside world (like a web browser or mobile app).

* Receives incoming HTTP requests (GET, POST, PUT, DELETE).
* Validates basic request formats and data transfer objects (DTOs).
* Delegates the actual work to the Service layer.
* Returns the HTTP response status code (e.g., 200 OK, 400 Bad Request) and data back to the client.
* Rule: It contains no business logic and no direct database queries.


2. Service Layer (Business Logic Layer)

The Service layer is the core "brain" of your application. It contains the rules, calculations, and evaluations that define how your business operates.

* Processes data sent from the controller.
* Enforces business rules (e.g., "An order cannot be placed if the items are out of stock").
* Coordinates transactions and cross-entity actions.
* Rule: It doesn't care how the data is displayed or where it is stored. It strictly orchestrates the workflow.

3. Repository Layer (Data Access Layer)

The Repository layer acts as a clean gateway to your persistent storage. It abstracts away complex database queries.

* Executes CRUD (Create, Read, Update, Delete) operations.

* Hides database-specific languages like SQL or MongoDB filters from the rest of the application.

* Maps raw database tables or collections into object entities used by the code.

* Rule: It never handles business choices. It only fulfills data requests from the Service layer.
