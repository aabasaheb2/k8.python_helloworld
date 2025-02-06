# Full Stack Web Messaging Application

This is a full stack web-based messaging application built using Python, Docker, MongoDB, and Kubernetes. The application allows users to store, delete, and view messages, and it is fully deployed on a Kubernetes cluster with MongoDB running in its own pod. 

### Features
- **Store Messages**: Users can store messages through a web interface.
- **Delete Messages**: Users can delete messages that they no longer need.
- **View Messages**: Users can view their stored messages in the browser.
- **MongoDB Integration**: Messages are stored in MongoDB for persistence.
- **Kubernetes Deployment**: The entire application, including MongoDB, is deployed in a Kubernetes cluster.
- **Web Access**: The application is accessible via a web browser on a custom domain at [http://www.msgapp.com].

### Architecture

- **Frontend**: Python-based web application (using a web framework Flask).
- **Backend**: The Python application interacts with MongoDB to store, retrieve, and delete messages.
- **Database**: MongoDB is used for persistent storage of messages.
- **Deployment**: The application and MongoDB are deployed as separate pods within a Kubernetes cluster.
- **Ingress**: The application is exposed to the outside world using Kubernetes Ingress, allowing users to access it via a custom domain (`http://www.msgapp.com`).


### Technologies Used

- **Python**: Used for building the web application backend.
- **Flask**: (depending on your framework) used to serve the web application.
- **MongoDB**: Database used to store user messages.
- **Docker**: Containerization of the web application for deployment.
- **Kubernetes**: Orchestration platform for managing the deployment of the application and MongoDB.
- **Kubernetes Ingress**: Exposing the application externally with a custom domain.


### Dependencies

- **Python**: 3.x
- **Flask**: (for Python web framework)
- **MongoDB**:
- **Docker**:
- **Kubernetes/minikube**:
