# <img src="https://new-static-server.vercel.app/y/images/favicon.png" /> - Twitter Clone
<img src="https://new-static-server.vercel.app/y/images/home.jpg" />

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Last Commit](https://img.shields.io/badge/last%20commit-1%20day%20ago-blue)
![Contributors](https://img.shields.io/badge/contributors-1-orange)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

#### You can access the functional version of the project at <a target="_blank" href="https://raulalbuquerque.pythonanywhere.com/">raulalbuquerque.pythonanywhere.com/</a>

<br>

## 📄 Description

This is a robust project developed with Django that replicates various functionalities of Twitter, providing a complete social media experience. It allows users to:

- Create an account: Users can sign up for the application by providing their personal details.

- Log in: Registered users can enter the platform using their username and password.

- Update their profile: Users are able to change their profile picture or share a motivational quote in their bio.

- Post tweets: Users can share their thoughts and ideas through tweets and also by posting images.

- Delete tweets: Users have the ability to manage their tweets and delete them whenever necessary.

- Like tweets: Users can engage with tweets from other users by liking them.

- Follow other users: Users have the option to follow other users, enabling them to view their tweets in their feed.

- Unfollow: If necessary, users have the choice to unfollow other users.

## 🛠️ Technologies:
* [HTML](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/css/)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)

## ⚙️ Prerequisites
```
Docker && docker-compose
```

## 🚀 Quickstart

1. Clone this project

   ```shell
   git clone git@github.com:Raul-Albuquerque/Y_twitter_clone.git
   ```

2. Enter into the project:

   ```shell
   cd Y_twitter_clone
   ```

3. Start the Docker Engine:

   <img src="https://new-static-server.vercel.app/y/images/engine.jpg" /><br>

4. Start and build (or rebuild) the services:
   ```shell
   docker-compose up -d --build 
   ```

5. Make migrations:
   ```shell
   docker-compose exec web python manage.py migrate
   ```

## 🔄 Contributing

1. **Fork the Project**: Fork the project to your personal GitHub.
<img src="https://servidor-estatico-eight-murex.vercel.app/fork.jpg" />

2. **Create your Feature Branch**:
    ```shell
    git checkout -b feature/AmazingFeature
    ```
3. **Commit your Changes**:
    ```shell
    git commit -m 'Add some AmazingFeature'
    ```
4. **Push to the Branch**:
    ```shell
    git commit -m 'git push origin feature/AmazingFeature'
    ```
5. **Open a Pull Request**: Go back to the original repository and open a pull request for your new feature.

## 📊 Status

The current status of the project is "completed"✅.

## 👨🏻‍💻 Author

This project was created by [Raul Albuquerque](https://github.com/Raul-Albuquerque).

## 📬 Contact

For more information or collaborations on the project, please contact raulmalbuquerque2014@gmail.com.