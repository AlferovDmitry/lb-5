<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ваши Заметки</title>
  <!-- CSS только Bootstrap -->
  <link href="https://stackpath.bootstrapcdn.com/bootstrap/5.1.0/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <!-- Ваш контент здесь -->
</body>
</html>

шапка сайта 

<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Заметки</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Все Заметки</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Мои Заметки</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Создать Заметку</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Вход</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Регистрация</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

Для подвала сайта с иконками социальных сетей:

<footer class="bg-light text-center text-lg-start">
  <div class="container p-4">
    <div class="row">
      <div class="col-lg-6 col-md-12 mb-4 mb-md-0">
        <p>Социальные сети:</p>
        <a href="https://vk.com"><img src="vk-icon.png" alt="VK"/></a>
        <a href="https://github.com"><img src="github-icon.png" alt="GitHub"/></a>
        <a href="https://facebook.com"><img src="facebook-icon.png" alt="Facebook"/></a>
        <a href="https://linkedin.com"><img src="linkedin-icon.png" alt="LinkedIn"/></a>
      </div>
    </div>
  </div>
</footer>


 "Все Заметки" и "Мои Заметки" 

<div class="card" style="width: 18rem;">
  <img src="note-image.jpg" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Заголовок заметки</h5>
    <p class="card-text">Краткое описание заметки...</p>
    <a href="#" class="btn btn-primary">Подробнее</a>
  </div>
</div>

"Создать заметку":

<form>
  <div class="mb-3">
    <label for="noteTitle" class="form-label">Заголовок</label>
    <input type="text" class="form-control" id="noteTitle" placeholder="Введите заголовок">
  </div>
  <div class="mb-3">
    <label for="noteText" class="form-label">Текст заметки</label>
    <textarea class="form-control" id="noteText" rows="3"></textarea>
  </div>
  <button type="submit" class="btn btn-primary">Отправить</button>
</form>
