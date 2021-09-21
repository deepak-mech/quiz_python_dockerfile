# quiz_python_dockerfile

## FILES
### In this repository we have total 3 files: first is quiz.json consists questions, second is assignment.py having python code & third one is Dockerfile to create the image to deploy the application.

## DOCKER IMAGE
### The name of the image that I have created is 89303/quiz-app:1.0(user_name/image_name:tag). I have pushed this image on dockerhub & it's public so that anyone can acces it easily.
### To use this image simply follow some commands:
       - Pull the Image: docker pull 89303/quiz-app:1.0
       - Launch the Container: docker run -it --name <container_name> 89303/quiz-app:1.0
